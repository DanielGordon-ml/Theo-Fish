"""
@file orchestrator.py
@description Single-paper pipeline orchestrator that wires all extraction
passes together: concept extraction, merging, claim extraction, edge
enrichment, cross-section gap-fill, claim verification, validation,
and Neo4j writes. Supports dual LLM clients and clear-on-force.
"""

import asyncio
import logging
from dataclasses import dataclass

from graph_builder.config.config import (
    DEFAULT_CONCURRENCY,
    LLM_FAILURE_ABORT_RATIO,
)
from graph_builder.config.schema_types import GraphSchema
from graph_builder.extraction.concept_merger import MergedConcept, merge_concepts
from graph_builder.extraction.cross_section_linker import find_cross_section_edges
from graph_builder.extraction.dedup.embedding_client import EmbeddingClient
from graph_builder.extraction.proof_linker import build_proof_map
from graph_builder.graph.graph_reader import GraphReader
from graph_builder.graph.graph_writer import GraphWriter
from graph_builder.graph.neo4j_client import Neo4jClient
from graph_builder.llm.llm_client import DeepSeekClient
from graph_builder.llm.protocol import LLMClient
from graph_builder.models.claim import ClaimNode
from graph_builder.models.concept import ConceptNode
from graph_builder.models.edges import ClaimEdge, CouplingEdge
from graph_builder.models.results import BuildResult
from graph_builder.models.section import Section
from graph_builder.orchestrator.pass_helpers import (
    build_concept_list,
    enrich_section_guarded,
    extract_claims_guarded,
    extract_concepts_guarded,
    fallback_merge,
    flatten_claim_results,
    flatten_edge_results,
    get_existing_concepts,
    group_claims_by_section,
    verify_section_guarded,
)
from graph_builder.orchestrator.pipeline_loader import check_already_built, load_paper
from graph_builder.orchestrator.pipeline_writer import build_source_node, write_to_neo4j
from graph_builder.shared.slugify import slugify
from graph_builder.validation.validator import validate_paper

logger = logging.getLogger("graph_builder")


@dataclass
class PipelineOptions:
    """Configuration for a single-paper pipeline run."""

    schema: GraphSchema
    concurrency: int = DEFAULT_CONCURRENCY
    force: bool = False
    thinking: bool = True


async def process_paper(
    arxiv_id: str,
    options: PipelineOptions,
    llm_client: DeepSeekClient,
    neo4j_client: Neo4jClient,
    embedding_client: EmbeddingClient | None = None,
    claim_llm_client: LLMClient | None = None,
) -> BuildResult:
    """Process a single paper through the full extraction pipeline.

    Runs passes P1-P4, validates, and writes to Neo4j. Returns a
    BuildResult with status 'built', 'skipped', or 'failed'.

    @param arxiv_id ArXiv identifier for the paper
    @param options Pipeline configuration
    @param llm_client LLM client for extraction calls
    @param neo4j_client Neo4j connection for reads and writes
    @param embedding_client Optional embedding client for dedup cascade
    @param claim_llm_client Optional LLM client for claim passes; falls back to llm_client
    @returns BuildResult with status and counts
    """
    effective_claim_llm = claim_llm_client or llm_client
    try:
        return await _execute_pipeline(
            arxiv_id, options, llm_client, neo4j_client,
            embedding_client, effective_claim_llm,
        )
    except Exception as err:
        logger.error("Pipeline failed for %s: %s", arxiv_id, err)
        return BuildResult(
            arxiv_id=arxiv_id, status="failed", error=str(err),
        )


async def _execute_pipeline(
    arxiv_id: str,
    options: PipelineOptions,
    llm_client: DeepSeekClient,
    neo4j_client: Neo4jClient,
    embedding_client: EmbeddingClient | None,
    claim_llm_client: LLMClient,
) -> BuildResult:
    """Run the full pipeline, raising on unrecoverable errors."""
    title, sections, full_text = await load_paper(arxiv_id)

    if not options.force and await check_already_built(arxiv_id, neo4j_client):
        return BuildResult(arxiv_id=arxiv_id, status="skipped")

    return await _run_all_passes(
        arxiv_id, title, sections, full_text, options,
        llm_client, neo4j_client, embedding_client, claim_llm_client,
    )


async def _run_all_passes(
    arxiv_id: str,
    title: str,
    sections: list[Section],
    full_text: str,
    options: PipelineOptions,
    llm_client: DeepSeekClient,
    neo4j_client: Neo4jClient,
    embedding_client: EmbeddingClient | None,
    claim_llm_client: LLMClient,
) -> BuildResult:
    """Execute P1 through write sequentially."""
    reader = GraphReader(neo4j_client)
    paper_slug = slugify(title)

    per_section_concepts = await _run_pass1(
        sections, options.schema, llm_client, reader, options.concurrency,
    )

    if _check_failure_ratio(per_section_concepts, len(sections)):
        return _abort_result(arxiv_id)

    merged = await _run_merge(
        per_section_concepts, reader, embedding_client, llm_client, arxiv_id,
    )

    # Build proof map before claim extraction so proofs are available
    proof_map = build_proof_map(full_text)

    claims, coupling_edges = await _run_pass2(
        sections, options.schema, claim_llm_client, merged, paper_slug,
        options.concurrency, proof_map,
    )

    claim_edges, extra_coupling = await _run_pass3a(
        sections, claims, merged, options.schema, llm_client,
        options.concurrency,
    )
    coupling_edges.extend(extra_coupling)

    # Deduplicate coupling edges — Pass 3a entries override Pass 2
    coupling_edges = _dedup_coupling_edges(coupling_edges)

    gap_fill_edges = await _run_pass3b(
        claims, merged, claim_edges, options.schema, llm_client,
    )
    claim_edges.extend(gap_fill_edges)

    # Pass 4: claim verification with proof context
    p4_claims, p4_coupling = await _run_pass4(
        sections, claims, proof_map, claim_llm_client,
        paper_slug, options.concurrency,
    )
    claims.extend(p4_claims)
    coupling_edges.extend(p4_coupling)

    return await _build_and_write(
        arxiv_id, title, sections, options, merged, claims,
        claim_edges, coupling_edges, neo4j_client, paper_slug,
    )


async def _build_and_write(
    arxiv_id: str,
    title: str,
    sections: list[Section],
    options: PipelineOptions,
    merged: list[MergedConcept],
    claims: list[ClaimNode],
    claim_edges: list[ClaimEdge],
    coupling_edges: list[CouplingEdge],
    neo4j_client: Neo4jClient,
    paper_slug: str,
) -> BuildResult:
    """Validate results, clear on force, and write to Neo4j.

    @param arxiv_id ArXiv identifier
    @param title Paper title
    @param sections Paper sections
    @param options Pipeline options
    @param merged Merged concepts
    @param claims All claims
    @param claim_edges All claim edges
    @param coupling_edges All coupling edges
    @param neo4j_client Neo4j connection
    @param paper_slug Slugified paper title
    @returns BuildResult with counts
    """
    concept_list = [m.concept for m in merged]
    provenance_list = [m.provenance for m in merged]

    validation_result = validate_paper(
        concept_list, claims, [], claim_edges, coupling_edges,
        provenance_list, options.schema,
    )

    if validation_result.warnings:
        for w in validation_result.warnings:
            logger.warning("Validation warning [%s]: %s", arxiv_id, w)

    # Clear existing claims and provenances on force rebuild
    if options.force:
        force_writer = GraphWriter(neo4j_client)
        await force_writer.clear_paper_claims(paper_slug)
        await force_writer.clear_paper_provenances(arxiv_id)

    writer = GraphWriter(neo4j_client)
    source = build_source_node(arxiv_id, title)
    counts = await write_to_neo4j(
        writer, source, merged, claims, claim_edges, coupling_edges,
    )

    return BuildResult(
        arxiv_id=arxiv_id,
        status="built",
        concept_count=counts["concepts"],
        claim_count=counts["claims"],
        edge_count=counts["edges"],
    )


# ---------------------------------------------------------------------------
# Pass runners
# ---------------------------------------------------------------------------


async def _run_pass1(
    sections: list[Section],
    schema: GraphSchema,
    llm_client: DeepSeekClient,
    reader: GraphReader,
    concurrency: int,
) -> list[list[ConceptNode]]:
    """Pass 1: parallel per-section concept extraction.

    @param sections Paper sections to process
    @param schema Graph schema for prompt generation
    @param llm_client LLM client for extraction
    @param reader Graph reader for existing concept lookup
    @param concurrency Max parallel LLM calls
    @returns Nested list of concepts, one inner list per section
    """
    existing = await get_existing_concepts(reader)
    semaphore = asyncio.Semaphore(concurrency)
    tasks = [
        extract_concepts_guarded(
            section, schema, llm_client, existing, semaphore,
        )
        for section in sections
    ]
    return await asyncio.gather(*tasks)


def _check_failure_ratio(
    per_section_results: list[list],
    total_sections: int,
) -> bool:
    """Check if the failure ratio exceeds the abort threshold.

    A section is considered failed if its result list is empty.

    @param per_section_results Nested list of results per section
    @param total_sections Total number of sections in the paper
    @returns True if pipeline should abort
    """
    if total_sections == 0:
        return True
    failed = sum(1 for r in per_section_results if not r)
    ratio = failed / total_sections
    return ratio > LLM_FAILURE_ABORT_RATIO


def _abort_result(arxiv_id: str) -> BuildResult:
    """Build a failed BuildResult for an aborted pipeline.

    @param arxiv_id ArXiv identifier
    @returns BuildResult with status='failed'
    """
    logger.error("Aborting %s: too many section failures", arxiv_id)
    return BuildResult(
        arxiv_id=arxiv_id,
        status="failed",
        error="Abort: >50% of section extractions failed",
    )


async def _run_merge(
    per_section_concepts: list[list[ConceptNode]],
    reader: GraphReader,
    embedding_client: EmbeddingClient | None,
    llm_client: DeepSeekClient,
    arxiv_id: str,
) -> list[MergedConcept]:
    """Pass merge: intra-paper dedup + cross-vault cascade.

    @param per_section_concepts Concepts grouped by section
    @param reader Graph reader for vault lookups
    @param embedding_client Embedding client for similarity
    @param llm_client LLM client for ambiguous dedup
    @param arxiv_id Source paper ArXiv ID
    @returns List of merged concepts
    """
    if embedding_client is None:
        return fallback_merge(per_section_concepts, arxiv_id)
    return await merge_concepts(
        per_section_concepts, reader, embedding_client,
        llm_client, arxiv_id,
    )


async def _run_pass2(
    sections: list[Section],
    schema: GraphSchema,
    llm_client: LLMClient,
    merged: list[MergedConcept],
    paper_slug: str,
    concurrency: int,
    proof_map: dict[str, str] | None = None,
) -> tuple[list[ClaimNode], list[CouplingEdge]]:
    """Pass 2: parallel per-section claim extraction.

    @param sections Paper sections
    @param schema Graph schema
    @param llm_client LLM client for claim extraction
    @param merged Merged concepts for grounding
    @param paper_slug Paper slug for claim ID composition
    @param concurrency Max parallel calls
    @param proof_map Optional mapping of claim labels to proof text
    @returns Tuple of (all_claims, all_coupling_edges)
    """
    concept_list_data = build_concept_list(merged)
    semaphore = asyncio.Semaphore(concurrency)
    tasks = [
        extract_claims_guarded(
            section, schema, llm_client, concept_list_data,
            paper_slug, semaphore, proof_map,
        )
        for section in sections
    ]
    results = await asyncio.gather(*tasks)
    return flatten_claim_results(results)


async def _run_pass3a(
    sections: list[Section],
    claims: list[ClaimNode],
    merged: list[MergedConcept],
    schema: GraphSchema,
    llm_client: DeepSeekClient,
    concurrency: int,
) -> tuple[list[ClaimEdge], list[CouplingEdge]]:
    """Pass 3a: section-batched edge enrichment.

    @param sections Paper sections
    @param claims All extracted claims
    @param merged All merged concepts
    @param schema Graph schema
    @param llm_client LLM client
    @param concurrency Max parallel calls
    @returns Tuple of (claim_edges, extra_coupling_edges)
    """
    all_concepts = [m.concept for m in merged]
    claims_by_section = group_claims_by_section(claims, sections)
    semaphore = asyncio.Semaphore(concurrency)

    tasks = [
        enrich_section_guarded(
            section, claims_by_section.get(section.heading, []),
            all_concepts, claims, schema, llm_client, semaphore,
        )
        for section in sections
    ]
    results = await asyncio.gather(*tasks)
    return flatten_edge_results(results)


async def _run_pass3b(
    claims: list[ClaimNode],
    merged: list[MergedConcept],
    existing_edges: list[ClaimEdge],
    schema: GraphSchema,
    llm_client: DeepSeekClient,
) -> list[ClaimEdge]:
    """Pass 3b: cross-section gap-fill.

    @param claims All claims
    @param merged All merged concepts
    @param existing_edges Edges found in Pass 3a
    @param schema Graph schema
    @param llm_client LLM client
    @returns New cross-section claim edges
    """
    all_concepts = [m.concept for m in merged]
    try:
        return await find_cross_section_edges(
            claims, all_concepts, existing_edges, schema, llm_client,
        )
    except Exception as err:
        logger.warning("Cross-section gap-fill failed: %s", err)
        return []


def _dedup_coupling_edges(
    edges: list[CouplingEdge],
) -> list[CouplingEdge]:
    """Deduplicate coupling edges, keeping later entries (Pass 3a over Pass 2).

    @param edges Combined coupling edges from all passes
    @returns Deduplicated list
    """
    seen: dict[tuple[str, str], CouplingEdge] = {}
    for edge in edges:
        key = (edge.claim_slug, edge.concept_slug)
        seen[key] = edge
    return list(seen.values())


async def _run_pass4(
    sections: list[Section],
    claims: list[ClaimNode],
    proof_map: dict[str, str],
    llm_client: LLMClient,
    paper_slug: str,
    concurrency: int,
) -> tuple[list[ClaimNode], list[CouplingEdge]]:
    """Pass 4: parallel per-section claim verification.

    @param sections Paper sections
    @param claims All claims extracted so far
    @param proof_map Mapping of claim labels to proof text
    @param llm_client LLM client for verification
    @param paper_slug Paper slug for new claim IDs
    @param concurrency Max parallel calls
    @returns Tuple of (new_claims, new_coupling_edges)
    """
    claims_by_section = group_claims_by_section(claims, sections)
    semaphore = asyncio.Semaphore(concurrency)
    tasks = [
        verify_section_guarded(
            section, claims_by_section.get(section.heading, []),
            proof_map, llm_client, paper_slug, semaphore,
        )
        for section in sections
    ]
    results = await asyncio.gather(*tasks)
    return flatten_claim_results(results)
