"""
@file frontmatter_builder.py
@description Builds YAML frontmatter dicts for Obsidian vault files.

Each edge type gets two keys written atomically:
- A flat wikilink list (e.g. generalizes) for Obsidian graph view.
- A companion _meta list (e.g. generalizes_meta) with structured attributes.

Human-owned fields (human_notes) are set to empty string on new files so
Obsidian surfaces them in the properties panel without overwriting existing edits.
"""

from graph_builder.models.claim import ClaimNode
from graph_builder.models.concept import ConceptNode
from graph_builder.models.edges import (
    ClaimEdge,
    ConceptEdge,
    CouplingEdge,
    SourcedFromEdge,
)
from graph_builder.models.source import SourceNode

# Edge types recognised on ConceptNode files.
_CONCEPT_EDGE_TYPES = [
    "generalizes",
    "has_component",
    "depends_on",
    "related_to",
    "equivalent_to",
    "instantiates",
]


def _concept_wikilink(slug: str) -> str:
    """Return the Obsidian wikilink for a concept slug."""
    return f"[[concepts/{slug}]]"


def _claim_wikilink(slug: str) -> str:
    """Return the Obsidian wikilink for a claim slug."""
    return f"[[claims/{slug}]]"


def _source_wikilink(arxiv_id: str, title: str) -> str:
    """Return the Obsidian wikilink for a source, with display text."""
    if title:
        return f"[[sources/{arxiv_id}|{title}]]"
    return f"[[sources/{arxiv_id}]]"


def _build_sourced_from_pairs(
    sourced_from: list[SourcedFromEdge],
    title_map: dict[str, str],
) -> tuple[list[str], list[dict]]:
    """Return (wikilinks, meta_dicts) for a list of SourcedFromEdge."""
    links: list[str] = []
    meta: list[dict] = []
    for edge in sourced_from:
        title = title_map.get(edge.source_arxiv_id, "")
        link = _source_wikilink(edge.source_arxiv_id, title)
        links.append(link)
        meta.append(
            {
                "target": link,
                "section": edge.section,
                "page": edge.page,
                "confidence": edge.confidence,
            }
        )
    return links, meta


def build_concept_frontmatter(
    concept: ConceptNode,
    concept_edges: list[ConceptEdge],
    sourced_from: list[SourcedFromEdge],
    *,
    source_titles: dict[str, str] | None = None,
) -> dict:
    """Build YAML frontmatter dict for a concept file.

    Writes pipeline-owned fields from the ConceptNode, flat wikilink lists
    for each concept edge type, companion _meta lists with edge attributes,
    and sourced_from wikilinks.  Human-owned fields default to empty string.

    @param concept: The concept node to render.
    @param concept_edges: Outbound concept->concept edges for this node.
    @param sourced_from: Edges linking this concept to its source papers.
    @param source_titles: Optional mapping of arxiv_id -> paper title for
        display text in sourced_from wikilinks.
    """
    titles = source_titles or {}

    fm: dict = {
        "slug": concept.slug,
        "name": concept.name,
        "semantic_type": concept.semantic_type,
        "canonical_definition": concept.canonical_definition,
        "formal_spec": concept.formal_spec,
        "aliases": list(concept.aliases),
        "status": concept.status,
        "human_notes": concept.human_notes if concept.human_notes else "",
    }

    _populate_concept_edge_keys(fm, concept_edges)

    links, meta = _build_sourced_from_pairs(sourced_from, titles)
    fm["sourced_from"] = links
    fm["sourced_from_meta"] = meta

    return fm


def _populate_concept_edge_keys(
    fm: dict,
    concept_edges: list[ConceptEdge],
) -> None:
    """Populate flat wikilink and _meta keys for each concept edge type."""
    for edge_type in _CONCEPT_EDGE_TYPES:
        fm[edge_type] = []
        fm[f"{edge_type}_meta"] = []

    for edge in concept_edges:
        link = _concept_wikilink(edge.target_slug)
        edge_type = edge.edge_type
        if edge_type not in fm:
            fm[edge_type] = []
            fm[f"{edge_type}_meta"] = []
        fm[edge_type].append(link)
        fm[f"{edge_type}_meta"].append({"target": link, **edge.attributes})


def build_claim_frontmatter(
    claim: ClaimNode,
    claim_edges: list[ClaimEdge],
    coupling_edges: list[CouplingEdge],
    sourced_from: list[SourcedFromEdge],
    *,
    source_titles: dict[str, str] | None = None,
) -> dict:
    """Build YAML frontmatter dict for a claim file.

    Writes pipeline-owned fields, about/about_meta from CouplingEdges,
    depends_on/depends_on_meta grouped by edge_type, and sourced_from links.
    Human-owned fields default to empty string.

    @param claim: The claim node to render.
    @param claim_edges: Outbound claim->claim edges for this node.
    @param coupling_edges: ABOUT edges linking this claim to concepts.
    @param sourced_from: Edges linking this claim to its source papers.
    @param source_titles: Optional mapping of arxiv_id -> paper title.
    """
    titles = source_titles or {}

    fm: dict = {
        "slug": claim.slug,
        "label": claim.label,
        "claim_type": claim.claim_type,
        "statement": claim.statement,
        "proof": claim.proof,
        "strength": claim.strength,
        "status": claim.status,
        "human_notes": claim.human_notes if claim.human_notes else "",
    }

    _populate_about_keys(fm, coupling_edges)
    _populate_claim_edge_keys(fm, claim_edges)

    links, meta = _build_sourced_from_pairs(sourced_from, titles)
    fm["sourced_from"] = links
    fm["sourced_from_meta"] = meta

    return fm


def _populate_about_keys(
    fm: dict,
    coupling_edges: list[CouplingEdge],
) -> None:
    """Populate about and about_meta from CouplingEdges."""
    fm["about"] = []
    fm["about_meta"] = []
    for edge in coupling_edges:
        link = _concept_wikilink(edge.concept_slug)
        fm["about"].append(link)
        fm["about_meta"].append(
            {
                "target": link,
                "role": edge.role,
                "aspect": edge.aspect,
            }
        )


def _populate_claim_edge_keys(
    fm: dict,
    claim_edges: list[ClaimEdge],
) -> None:
    """Populate flat wikilink and _meta keys for each claim edge type."""
    fm["depends_on"] = []
    fm["depends_on_meta"] = []

    for edge in claim_edges:
        link = _claim_wikilink(edge.target_slug)
        edge_type = edge.edge_type
        if edge_type not in fm:
            fm[edge_type] = []
            fm[f"{edge_type}_meta"] = []
        fm[edge_type].append(link)
        fm[f"{edge_type}_meta"].append({"target": link, **edge.attributes})


def build_source_frontmatter(source: SourceNode) -> dict:
    """Build YAML frontmatter dict for a source file.

    Writes all SourceNode fields and sets human-owned fields to empty string
    so Obsidian surfaces them without overwriting any human edits.

    @param source: The source node to render.
    """
    return {
        "arxiv_id": source.arxiv_id,
        "title": source.title,
        "authors": list(source.authors),
        "date_published": source.date_published,
        "date_extracted": source.date_extracted,
        "human_notes": source.human_notes if source.human_notes else "",
    }
