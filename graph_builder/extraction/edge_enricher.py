"""
@file edge_enricher.py
@description Section-batched edge enricher (Pass 3a): extracts claim-to-claim
and claim-to-concept coupling edges for all claims in a section in one LLM call.
"""

import json
import logging

from graph_builder.config.schema_types import GraphSchema
from graph_builder.extraction.prompt_generator import build_edge_enrichment_prompt
from graph_builder.llm.protocol import LLMClient
from graph_builder.llm.response_parser import parse_edges
from graph_builder.models.claim import ClaimNode
from graph_builder.models.concept import ConceptNode
from graph_builder.models.edges import ClaimEdge, CouplingEdge

logger = logging.getLogger("graph_builder")


async def enrich_section_edges(
    section_claims: list[ClaimNode],
    section_text: str,
    all_concepts: list[ConceptNode],
    all_claims: list[ClaimNode],
    schema: GraphSchema,
    llm_client: LLMClient,
) -> tuple[list[ClaimEdge], list[CouplingEdge]]:
    """Extract edges for all claims in a section in one LLM call.

    Batches all section claims into a single prompt with their statements,
    conclusions, proofs, and concept/claim reference lists. Returns empty
    lists on LLM failure or invalid JSON.

    @param section_claims Claims belonging to this section.
    @param section_text Raw section text for context.
    @param all_concepts Full concept list for grounding references.
    @param all_claims Full claim list for grounding references.
    @param schema GraphSchema used to build the system prompt.
    @param llm_client Async LLM client for the extraction call.
    @returns Tuple of (claim_edges, coupling_edges), both empty on failure.
    """
    if not section_claims:
        return [], []

    system_prompt = build_edge_enrichment_prompt(schema)
    user_prompt = _build_user_prompt(
        section_claims, section_text, all_concepts, all_claims
    )

    try:
        response = await llm_client.call(system_prompt, user_prompt)
    except Exception as err:
        logger.error("LLM call failed in enrich_section_edges: %s", err)
        return [], []

    parsed = _safe_parse_json(response.content)
    if parsed is None:
        return [], []

    _, claim_edges, coupling_edges = parse_edges(response.content, schema)
    return claim_edges, coupling_edges


def _build_user_prompt(
    section_claims: list[ClaimNode],
    section_text: str,
    all_concepts: list[ConceptNode],
    all_claims: list[ClaimNode],
) -> str:
    """Compose the user prompt with claim details and reference lists.

    @param section_claims Claims to enrich in this batch.
    @param section_text Raw section text for context.
    @param all_concepts All concepts for slug grounding.
    @param all_claims All claims for slug grounding.
    @returns Formatted user prompt string.
    """
    parts = [
        "## Section Text",
        section_text,
        "",
        "## Claims to Enrich",
        "",
    ]
    parts.extend(_format_claims_block(section_claims))
    parts.append("")
    parts.extend(_format_reference_block(all_concepts, all_claims))
    return "\n".join(parts)


def _format_claims_block(claims: list[ClaimNode]) -> list[str]:
    """Format each claim with its slug, conclusion, and proof for the prompt.

    @param claims List of ClaimNode objects to format.
    @returns List of prompt lines.
    """
    lines: list[str] = []
    for claim in claims:
        lines.append(f"- slug: {claim.slug}")
        if claim.conclusion:
            lines.append(f"  conclusion: {claim.conclusion}")
        if claim.proof:
            lines.append(f"  proof: {claim.proof}")
        if claim.statement:
            lines.append(f"  statement: {claim.statement}")
    return lines


def _format_reference_block(
    all_concepts: list[ConceptNode],
    all_claims: list[ClaimNode],
) -> list[str]:
    """Format concept and claim reference lists for grounding.

    @param all_concepts All concepts (name, slug, type).
    @param all_claims All claims (slug, type).
    @returns List of prompt lines.
    """
    lines = ["## Reference: Concepts"]
    for c in all_concepts:
        lines.append(f"- {c.name} (slug: {c.slug}, type: {c.semantic_type})")
    lines.append("")
    lines.append("## Reference: Claims")
    for cl in all_claims:
        lines.append(f"- {cl.slug} (type: {cl.claim_type})")
    return lines


def _safe_parse_json(content: str) -> dict | None:
    """Attempt to parse JSON, returning None on failure.

    @param content Raw string from the LLM response.
    @returns Parsed dict, or None if parsing failed.
    """
    try:
        return json.loads(content)
    except (json.JSONDecodeError, ValueError):
        return None
