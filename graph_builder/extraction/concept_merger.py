"""
@file concept_merger.py
@description Merges per-section concept lists paper-wide and runs the dedup cascade.

Intra-paper dedup groups concepts by slug; the richest version (longest
formal_spec, union of components) is kept. Each unique concept is then
resolved against the vault via run_dedup_cascade.
"""

from dataclasses import dataclass

from graph_builder.extraction.dedup.dedup_cascade import DedupResult, run_dedup_cascade
from graph_builder.extraction.dedup.embedding_client import EmbeddingClient
from graph_builder.graph.graph_reader import GraphReader
from graph_builder.llm.llm_client import DeepSeekClient
from graph_builder.models.concept import ConceptNode
from graph_builder.models.provenance import ProvenanceNode


@dataclass
class MergedConcept:
    """A concept after intra-paper dedup and cross-vault resolution."""

    concept: ConceptNode
    dedup_result: DedupResult
    provenance: ProvenanceNode


async def merge_concepts(
    per_section_concepts: list[list[ConceptNode]],
    graph_reader: GraphReader,
    embedding_client: EmbeddingClient,
    llm_client: DeepSeekClient | None = None,
    source_arxiv_id: str = "",
) -> list[MergedConcept]:
    """Merge per-section concept lists and resolve each against the vault.

    Steps:
    1. Flatten all per-section concepts.
    2. Group by slug; keep the richest version (longest formal_spec,
       union of components).
    3. Run run_dedup_cascade per unique concept.
    4. Build ProvenanceNode with source_arxiv_id and formal_spec.
    5. Return list of MergedConcept.

    @param per_section_concepts Nested list — one inner list per section.
    @param graph_reader Read access to the knowledge graph vault.
    @param embedding_client Embedding API wrapper for similarity search.
    @param llm_client Optional LLM for ambiguous dedup confirmations.
    @param source_arxiv_id ArXiv identifier of the source paper.
    @returns List of MergedConcept, one per unique concept slug.
    """
    flat = _flatten(per_section_concepts)
    if not flat:
        return []

    grouped = _group_by_slug(flat)
    unique = [_pick_richest(group) for group in grouped.values()]

    results: list[MergedConcept] = []
    for concept in unique:
        dedup_result = await run_dedup_cascade(
            concept,
            graph_reader,
            embedding_client,
            llm_client,
        )
        provenance = _build_provenance(concept, source_arxiv_id)
        results.append(
            MergedConcept(
                concept=concept,
                dedup_result=dedup_result,
                provenance=provenance,
            )
        )

    return results


# ---------------------------------------------------------------------------
# Private helpers
# ---------------------------------------------------------------------------


def _flatten(per_section: list[list[ConceptNode]]) -> list[ConceptNode]:
    """Flatten a nested list of ConceptNode lists into a single list.

    @param per_section Nested concept lists.
    @returns Flat list of all ConceptNodes.
    """
    return [concept for section in per_section for concept in section]


def _group_by_slug(
    concepts: list[ConceptNode],
) -> dict[str, list[ConceptNode]]:
    """Group concepts by their slug.

    @param concepts Flat list of ConceptNodes.
    @returns Dict mapping slug -> list of ConceptNodes with that slug.
    """
    groups: dict[str, list[ConceptNode]] = {}
    for concept in concepts:
        groups.setdefault(concept.slug, []).append(concept)
    return groups


def _pick_richest(group: list[ConceptNode]) -> ConceptNode:
    """Select and return the richest concept from a same-slug group.

    Richest = longest formal_spec; ties broken by most components.
    The returned concept's components are the union across the group.

    @param group Non-empty list of ConceptNodes sharing the same slug.
    @returns Single ConceptNode with merged components and longest formal_spec.
    """
    best = max(group, key=lambda c: (len(c.formal_spec), len(c.components)))
    merged_components = list({comp for c in group for comp in c.components})
    return best.model_copy(update={"components": merged_components})


def _build_provenance(concept: ConceptNode, source_arxiv_id: str) -> ProvenanceNode:
    """Build a ProvenanceNode for the given concept and paper.

    @param concept The merged concept.
    @param source_arxiv_id ArXiv identifier of the source paper.
    @returns Populated ProvenanceNode.
    """
    return ProvenanceNode(
        concept_slug=concept.slug,
        source_arxiv_id=source_arxiv_id,
        formulation=concept.canonical_definition,
        formal_spec=concept.formal_spec,
    )
