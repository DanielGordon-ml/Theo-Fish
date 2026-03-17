"""
@file body_renderer.py
@description Renders the markdown body for concept, claim, and source vault
files. Body contains ONLY mathematical prose and wikilinks; all machine-
readable edge data lives exclusively in frontmatter.
"""

from graph_builder.models.concept import ConceptNode
from graph_builder.models.claim import ClaimNode
from graph_builder.models.source import SourceNode
from graph_builder.models.provenance import ProvenanceNode

_TABLE_HEADER = (
    "| Source | Section | Formulation | Confidence |\n"
    "|--------|---------|-------------|------------|\n"
)


def _provenance_row(prov: ProvenanceNode) -> str:
    """Format a single provenance record as a markdown table row.

    The source column uses a wikilink to the source file under sources/.
    """
    source_link = f"[[sources/{prov.source_arxiv_id}]]"
    return (
        f"| {source_link} | {prov.section} "
        f'| "{prov.formulation}" | {prov.extraction_confidence} |\n'
    )


def _provenance_table(provenances: list[ProvenanceNode]) -> str:
    """Build the full ## Provenance section from a list of ProvenanceNodes."""
    rows = "".join(_provenance_row(p) for p in provenances)
    return f"## Provenance\n\n{_TABLE_HEADER}{rows}"


def render_concept_body(
    concept: ConceptNode,
    provenances: list[ProvenanceNode],
) -> str:
    """Render markdown body for a concept file.

    Includes a top-level heading, canonical definition, and an optional
    provenance table when provenance records are provided.
    """
    parts: list[str] = [f"# {concept.name}\n\n{concept.canonical_definition}\n"]

    if provenances:
        parts.append(f"\n{_provenance_table(provenances)}")

    return "\n".join(parts)


def render_claim_body(claim: ClaimNode) -> str:
    """Render markdown body for a claim file.

    Includes heading, statement text, and an optional ## Proof section that
    is omitted when the claim has no proof text.
    """
    parts: list[str] = [f"# {claim.name}\n\n{claim.statement}\n"]

    if claim.proof:
        parts.append(f"\n## Proof\n\n{claim.proof}\n")

    return "\n".join(parts)


def _entity_list(slugs: list[str], prefix: str) -> str:
    """Render a bulleted wikilink list for concept or claim slugs."""
    lines = "\n".join(f"- [[{prefix}/{s}|{s}]]" for s in slugs)
    return lines


def render_source_body(
    source: SourceNode,
    concept_slugs: list[str],
    claim_slugs: list[str],
) -> str:
    """Render markdown body for a source file.

    Includes heading, paper metadata, extracted concept wikilinks, and
    extracted claim wikilinks.
    """
    authors_str = ", ".join(source.authors) if source.authors else ""
    meta_lines = [
        f"**arXiv:** {source.arxiv_id}",
        f"**Authors:** {authors_str}",
        f"**Published:** {source.date_published}",
    ]
    metadata_block = "\n".join(meta_lines)

    parts: list[str] = [f"# {source.title}\n\n{metadata_block}\n"]

    if concept_slugs:
        concept_list = _entity_list(concept_slugs, "concepts")
        parts.append(f"\n## Concepts\n\n{concept_list}\n")

    if claim_slugs:
        claim_list = _entity_list(claim_slugs, "claims")
        parts.append(f"\n## Claims\n\n{claim_list}\n")

    return "\n".join(parts)
