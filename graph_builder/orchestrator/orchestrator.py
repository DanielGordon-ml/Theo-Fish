"""
@file orchestrator.py
@description Single-paper pipeline orchestrator that wires all extraction
passes together: concept extraction, merging, claim extraction, edge
enrichment, cross-section gap-fill, validation, and Neo4j writes.
"""

import asyncio
import logging
from dataclasses import dataclass

from graph_builder.config.config import (
    DEFAULT_CONCURRENCY,
    LLM_FAILURE_ABORT_RATIO,
)
from graph_builder.config.schema_types import GraphSchema
from graph_builder.extraction.claim_extractor import extract_claims_from_section
from graph_builder.extraction.concept_extractor import extract_concepts_from_section
from graph_builder.extraction.concept_merger import MergedConcept, merge_concepts
from graph_builder.extraction.cross_section_linker import find_cross_section_edges
from graph_builder.extraction.dedup.embedding_client import EmbeddingClient
from graph_builder.extraction.edge_enricher import enrich_section_edges
from graph_builder.graph.graph_reader import GraphReader
from graph_builder.graph.graph_writer import GraphWriter
from graph_builder.graph.neo4j_client import Neo4jClient
from graph_builder.llm.llm_client import DeepSeekClient
from graph_builder.models.claim import ClaimNode
from graph_builder.models.concept import ConceptNode
from graph_builder.models.edges import ClaimEdge, CouplingEdge
from graph_builder.models.provenance import ProvenanceNode
from graph_builder.models.results import BuildResult
from graph_builder.models.section import Section
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
) -> BuildResult:
    """Process a single paper through the full extraction pipeline.

    Runs passes P1-P3b, validates, and writes to Neo4j. Returns a
    BuildResult with status 'built', 'skipped', or 'failed'.

    @param arxiv_id ArXiv identifier for the paper
    @param options Pipeline configuration
    @param llm_client LLM client for extraction calls
    @param neo4j_client Neo4j connection for reads and writes
    @param embedding_client Optional embedding client for dedup cascade
    @returns BuildResult with status and counts
    """
    try:
        return await _execute_pipeline(
            arxiv_id, options, llm_client, neo4j_client, embedding_client,
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
) -> BuildResult:
    """Run the full pipeline, raising on unrecoverable errors."""
    title, sections = await load_paper(arxiv_id)

    if not options.force and await check_already_built(arxiv_id, neo4j_client):
        return BuildResult(arxiv_id=arxiv_id, status="skipped")

    return await _run_all_passes(
        arxiv_id, title, sections, options,
        llm_client, neo4j_client, embedding_client,
    )


async def _run_all_passes(
    arxiv_id: str,
    title: str,
    sections: list[Section],
    options: PipelineOptions,
    llm_client: DeepSeekClient,
    neo4j_client: Neo4jClient,
    embedding_client: EmbeddingClient | None,
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

    claims, coupling_edges = await _run_pass2(
        sections, options.schema, llm_client, merged, paper_slug,
        options.concurrency,
    )

    claim_edges, extra_coupling = await _run_pass3a(
        sections, claims, merged, options.schema, llm_client,
        options.concurrency,
    )
    coupling_edges.extend(extra_coupling)

    gap_fill_edges = await _run_pass3b(
        claims, merged, claim_edges, options.schema, llm_client,
    )
    claim_edges.extend(gap_fill_edges)

    concept_list = [m.concept for m in merged]
    provenance_list = [m.provenance for m in merged]

    validation_result = validate_paper(
        concept_list, claims, [], claim_edges, coupling_edges,
        provenance_list, options.schema,
    )

    if validation_result.warnings:
        for w in validation_result.warnings:
            logger.warning("Validation warning [%s]: %s", arxiv_id, w)

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
# Pass helpers
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
    existing = await _get_existing_concepts(reader)
    semaphore = asyncio.Semaphore(concurrency)
    tasks = [
        _extract_concepts_guarded(
            section, schema, llm_client, existing, semaphore,
        )
        for section in sections
    ]
    return await asyncio.gather(*tasks)


async def _get_existing_concepts(
    reader: GraphReader,
) -> list[dict]:
    """Fetch existing concept slugs for grounding.

    @param reader Graph reader
    @returns List of dicts with slug and semantic_type keys
    """
    slugs = await reader.get_all_concept_slugs()
    results: list[dict] = []
    for slug in slugs:
        concept = await reader.get_existing_concept(slug)
        if concept is not None:
            results.append({
                "slug": concept.slug,
                "semantic_type": concept.semantic_type,
            })
    return results


async def _extract_concepts_guarded(
    section: Section,
    schema: GraphSchema,
    llm_client: DeepSeekClient,
    existing: list[dict],
    semaphore: asyncio.Semaphore,
) -> list[ConceptNode]:
    """Extract concepts with semaphore gating and error isolation.

    @param section Section to extract from
    @param schema Graph schema
    @param llm_client LLM client
    @param existing Known concept shortlist
    @param semaphore Concurrency limiter
    @returns List of concepts, empty on failure
    """
    async with semaphore:
        try:
            return await extract_concepts_from_section(
                section, schema, llm_client,
                existing_concepts=existing,
            )
        except Exception as err:
            logger.warning(
                "Concept extraction failed for '%s': %s",
                section.heading, err,
            )
            return []


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
        return _fallback_merge(per_section_concepts, arxiv_id)
    return await merge_concepts(
        per_section_concepts, reader, embedding_client,
        llm_client, arxiv_id,
    )


def _fallback_merge(
    per_section_concepts: list[list[ConceptNode]],
    arxiv_id: str,
) -> list[MergedConcept]:
    """Merge without embedding client — simple slug-based dedup only.

    @param per_section_concepts Concepts grouped by section
    @param arxiv_id Source paper ArXiv ID
    @returns List of MergedConcept with is_new=True
    """
    from graph_builder.extraction.dedup.dedup_cascade import DedupResult

    seen: dict[str, ConceptNode] = {}
    for section_concepts in per_section_concepts:
        for concept in section_concepts:
            if concept.slug not in seen:
                seen[concept.slug] = concept

    results: list[MergedConcept] = []
    for concept in seen.values():
        results.append(MergedConcept(
            concept=concept,
            dedup_result=DedupResult(
                slug=concept.slug, is_new=True,
                match_method="new", match_confidence=0.0,
            ),
            provenance=ProvenanceNode(
                concept_slug=concept.slug,
                source_arxiv_id=arxiv_id,
                formulation=concept.canonical_definition,
                formal_spec=concept.formal_spec,
            ),
        ))
    return results


async def _run_pass2(
    sections: list[Section],
    schema: GraphSchema,
    llm_client: DeepSeekClient,
    merged: list[MergedConcept],
    paper_slug: str,
    concurrency: int,
) -> tuple[list[ClaimNode], list[CouplingEdge]]:
    """Pass 2: parallel per-section claim extraction.

    @param sections Paper sections
    @param schema Graph schema
    @param llm_client LLM client
    @param merged Merged concepts for grounding
    @param paper_slug Paper slug for claim ID composition
    @param concurrency Max parallel calls
    @returns Tuple of (all_claims, all_coupling_edges)
    """
    concept_list = _build_concept_list(merged)
    semaphore = asyncio.Semaphore(concurrency)
    tasks = [
        _extract_claims_guarded(
            section, schema, llm_client, concept_list, paper_slug, semaphore,
        )
        for section in sections
    ]
    results = await asyncio.gather(*tasks)
    return _flatten_claim_results(results)


def _build_concept_list(
    merged: list[MergedConcept],
) -> list[dict]:
    """Convert merged concepts to dicts for claim prompt grounding.

    @param merged List of MergedConcept
    @returns List of dicts with name, slug, type keys
    """
    return [
        {
            "name": m.concept.name,
            "slug": m.concept.slug,
            "type": m.concept.semantic_type,
        }
        for m in merged
    ]


async def _extract_claims_guarded(
    section: Section,
    schema: GraphSchema,
    llm_client: DeepSeekClient,
    concept_list: list[dict],
    paper_slug: str,
    semaphore: asyncio.Semaphore,
) -> tuple[list[ClaimNode], list[CouplingEdge]]:
    """Extract claims with semaphore gating and error isolation.

    @param section Section to extract from
    @param schema Graph schema
    @param llm_client LLM client
    @param concept_list Concept grounding list
    @param paper_slug Paper slug
    @param semaphore Concurrency limiter
    @returns Tuple of (claims, coupling_edges), empty on failure
    """
    async with semaphore:
        try:
            return await extract_claims_from_section(
                section, schema, llm_client, concept_list, paper_slug,
            )
        except Exception as err:
            logger.warning(
                "Claim extraction failed for '%s': %s",
                section.heading, err,
            )
            return [], []


def _flatten_claim_results(
    results: list[tuple[list[ClaimNode], list[CouplingEdge]]],
) -> tuple[list[ClaimNode], list[CouplingEdge]]:
    """Flatten per-section claim results into single lists.

    @param results List of (claims, coupling_edges) tuples
    @returns Tuple of (all_claims, all_coupling_edges)
    """
    all_claims: list[ClaimNode] = []
    all_coupling: list[CouplingEdge] = []
    for claims, couplings in results:
        all_claims.extend(claims)
        all_coupling.extend(couplings)
    return all_claims, all_coupling


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
    claims_by_section = _group_claims_by_section(claims, sections)
    semaphore = asyncio.Semaphore(concurrency)

    tasks = [
        _enrich_section_guarded(
            section, claims_by_section.get(section.heading, []),
            all_concepts, claims, schema, llm_client, semaphore,
        )
        for section in sections
    ]
    results = await asyncio.gather(*tasks)
    return _flatten_edge_results(results)


def _group_claims_by_section(
    claims: list[ClaimNode],
    sections: list[Section],
) -> dict[str, list[ClaimNode]]:
    """Group claims by their section heading.

    @param claims All claims
    @param sections Paper sections
    @returns Dict mapping heading -> list of claims
    """
    groups: dict[str, list[ClaimNode]] = {}
    for claim in claims:
        groups.setdefault(claim.section, []).append(claim)
    return groups


async def _enrich_section_guarded(
    section: Section,
    section_claims: list[ClaimNode],
    all_concepts: list[ConceptNode],
    all_claims: list[ClaimNode],
    schema: GraphSchema,
    llm_client: DeepSeekClient,
    semaphore: asyncio.Semaphore,
) -> tuple[list[ClaimEdge], list[CouplingEdge]]:
    """Enrich edges for a section with error isolation.

    @param section Section to process
    @param section_claims Claims in this section
    @param all_concepts All concepts for grounding
    @param all_claims All claims for grounding
    @param schema Graph schema
    @param llm_client LLM client
    @param semaphore Concurrency limiter
    @returns Tuple of (claim_edges, coupling_edges), empty on failure
    """
    async with semaphore:
        try:
            return await enrich_section_edges(
                section_claims, section.content, all_concepts,
                all_claims, schema, llm_client,
            )
        except Exception as err:
            logger.warning(
                "Edge enrichment failed for '%s': %s",
                section.heading, err,
            )
            return [], []


def _flatten_edge_results(
    results: list[tuple[list[ClaimEdge], list[CouplingEdge]]],
) -> tuple[list[ClaimEdge], list[CouplingEdge]]:
    """Flatten per-section edge results into single lists.

    @param results List of (claim_edges, coupling_edges) tuples
    @returns Tuple of (all_claim_edges, all_coupling_edges)
    """
    all_claim_edges: list[ClaimEdge] = []
    all_coupling: list[CouplingEdge] = []
    for claim_edges, couplings in results:
        all_claim_edges.extend(claim_edges)
        all_coupling.extend(couplings)
    return all_claim_edges, all_coupling


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


