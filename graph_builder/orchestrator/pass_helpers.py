"""
@file pass_helpers.py
@description Internal helper functions for pipeline pass execution: guarded
extraction wrappers, result flattening, concept list building, and
fallback merge. Extracted from orchestrator.py to keep files under 600 lines.
"""

import asyncio
import logging

from graph_builder.config.schema_types import GraphSchema
from graph_builder.extraction.claim_extractor import extract_claims_from_section
from graph_builder.extraction.claim_verifier import verify_section_claims
from graph_builder.extraction.concept_extractor import extract_concepts_from_section
from graph_builder.extraction.concept_merger import MergedConcept
from graph_builder.extraction.edge_enricher import enrich_section_edges
from graph_builder.graph.graph_reader import GraphReader
from graph_builder.llm.protocol import LLMClient
from graph_builder.models.claim import ClaimNode
from graph_builder.models.concept import ConceptNode
from graph_builder.models.edges import ClaimEdge, CouplingEdge
from graph_builder.models.provenance import ProvenanceNode
from graph_builder.models.section import Section

logger = logging.getLogger("graph_builder")


# ---------------------------------------------------------------------------
# Result flattening
# ---------------------------------------------------------------------------


def flatten_claim_results(
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


def flatten_edge_results(
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


# ---------------------------------------------------------------------------
# Concept utilities
# ---------------------------------------------------------------------------


def build_concept_list(
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


def group_claims_by_section(
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


async def get_existing_concepts(
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


# ---------------------------------------------------------------------------
# Fallback merge
# ---------------------------------------------------------------------------


def fallback_merge(
    per_section_concepts: list[list[ConceptNode]],
    arxiv_id: str,
) -> list[MergedConcept]:
    """Merge without embedding client -- simple slug-based dedup only.

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

    return _build_merged_list(seen, arxiv_id, DedupResult)


def _build_merged_list(
    seen: dict[str, ConceptNode],
    arxiv_id: str,
    dedup_cls: type,
) -> list[MergedConcept]:
    """Build MergedConcept list from deduplicated concept dict.

    @param seen Dict of slug -> ConceptNode
    @param arxiv_id Source paper ArXiv ID
    @param dedup_cls DedupResult class for constructing results
    @returns List of MergedConcept
    """
    results: list[MergedConcept] = []
    for concept in seen.values():
        results.append(MergedConcept(
            concept=concept,
            dedup_result=dedup_cls(
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


# ---------------------------------------------------------------------------
# Guarded extraction wrappers
# ---------------------------------------------------------------------------


async def extract_concepts_guarded(
    section: Section,
    schema: GraphSchema,
    llm_client: LLMClient,
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


async def extract_claims_guarded(
    section: Section,
    schema: GraphSchema,
    llm_client: LLMClient,
    concept_list: list[dict],
    paper_slug: str,
    semaphore: asyncio.Semaphore,
    proof_map: dict[str, str] | None = None,
) -> tuple[list[ClaimNode], list[CouplingEdge]]:
    """Extract claims with semaphore gating and error isolation.

    @param section Section to extract from
    @param schema Graph schema
    @param llm_client LLM client
    @param concept_list Concept grounding list
    @param paper_slug Paper slug
    @param semaphore Concurrency limiter
    @param proof_map Optional mapping of claim labels to proof text
    @returns Tuple of (claims, coupling_edges), empty on failure
    """
    async with semaphore:
        try:
            return await extract_claims_from_section(
                section, schema, llm_client,
                concept_list, paper_slug, proof_map,
            )
        except Exception as err:
            logger.warning(
                "Claim extraction failed for '%s': %s",
                section.heading, err,
            )
            return [], []


async def enrich_section_guarded(
    section: Section,
    section_claims: list[ClaimNode],
    all_concepts: list[ConceptNode],
    all_claims: list[ClaimNode],
    schema: GraphSchema,
    llm_client: LLMClient,
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


async def verify_section_guarded(
    section: Section,
    section_claims: list[ClaimNode],
    proof_map: dict[str, str],
    llm_client: LLMClient,
    paper_slug: str,
    semaphore: asyncio.Semaphore,
) -> tuple[list[ClaimNode], list[CouplingEdge]]:
    """Verify a section's claims with error isolation.

    @param section Section to verify
    @param section_claims Claims in this section
    @param proof_map Mapping of claim labels to proof text
    @param llm_client LLM client for verification
    @param paper_slug Paper slug for new claim IDs
    @param semaphore Concurrency limiter
    @returns Tuple of (new_claims, new_coupling_edges), empty on failure
    """
    async with semaphore:
        try:
            return await verify_section_claims(
                section.content, proof_map, section_claims,
                None, llm_client, paper_slug, section.heading,
            )
        except Exception as err:
            logger.warning(
                "Verification failed for '%s': %s",
                section.heading, err,
            )
            return [], []
