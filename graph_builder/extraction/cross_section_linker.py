"""
@file cross_section_linker.py
@description Cross-section gap-fill linker (Pass 3b): finds implicit dependencies
between claims in different sections that were not captured per-section. Sends only
claim conclusions and concept formal_specs to minimise token usage.
"""

import json
import logging

from graph_builder.config.schema_types import GraphSchema
from graph_builder.extraction.prompt_generator import build_gap_fill_prompt
from graph_builder.llm.protocol import LLMClient
from graph_builder.models.claim import ClaimNode
from graph_builder.models.concept import ConceptNode
from graph_builder.models.edges import ClaimEdge

logger = logging.getLogger("graph_builder")

# Identifies an edge uniquely for deduplication purposes
_EdgeKey = tuple[str, str, str]


async def find_cross_section_edges(
    all_claims: list[ClaimNode],
    all_concepts: list[ConceptNode],
    existing_edges: list[ClaimEdge],
    schema: GraphSchema,
    llm_client: LLMClient,
) -> list[ClaimEdge]:
    """Find cross-section implicit dependencies not yet in existing_edges.

    Sends only claim conclusions and concept formal_specs (not full text) to
    minimise tokens. Filters out edges whose (source, target, type) triple
    already exists in existing_edges.

    @param all_claims All claims across the paper.
    @param all_concepts All concepts across the paper.
    @param existing_edges Edges already found by the section-batched enricher.
    @param schema GraphSchema used to build the system prompt.
    @param llm_client Async LLM client for the gap-fill call.
    @returns List of new ClaimEdge objects, empty on failure.
    """
    system_prompt = build_gap_fill_prompt(schema)
    user_prompt = _build_user_prompt(all_claims, all_concepts)

    try:
        response = await llm_client.call(system_prompt, user_prompt)
    except Exception as err:
        logger.error("LLM call failed in find_cross_section_edges: %s", err)
        return []

    parsed = _safe_parse_json(response.content)
    if parsed is None:
        return []

    candidate_edges = _parse_claim_edges(parsed.get("edges", []))
    existing_keys = _build_edge_key_set(existing_edges)
    return [e for e in candidate_edges if _edge_key(e) not in existing_keys]


def _build_user_prompt(
    all_claims: list[ClaimNode],
    all_concepts: list[ConceptNode],
) -> str:
    """Compose the minimal user prompt using only conclusions and formal_specs.

    @param all_claims All claims (slug, section, conclusion only).
    @param all_concepts All concepts (slug, name, formal_spec only).
    @returns Formatted user prompt string.
    """
    parts = ["## Claims (conclusions only)", ""]
    parts.extend(_format_claim_summaries(all_claims))
    parts.append("")
    parts.extend(_format_concept_summaries(all_concepts))
    return "\n".join(parts)


def _format_claim_summaries(claims: list[ClaimNode]) -> list[str]:
    """Format claims as slug + section + conclusion lines.

    @param claims List of ClaimNode objects.
    @returns List of prompt lines.
    """
    lines: list[str] = []
    for claim in claims:
        lines.append(f"- slug: {claim.slug} (section: {claim.section})")
        if claim.conclusion:
            lines.append(f"  conclusion: {claim.conclusion}")
    return lines


def _format_concept_summaries(concepts: list[ConceptNode]) -> list[str]:
    """Format concepts as slug + name + formal_spec lines.

    @param concepts List of ConceptNode objects.
    @returns List of prompt lines.
    """
    lines = ["## Concepts (formal_specs only)", ""]
    for concept in concepts:
        lines.append(f"- slug: {concept.slug}, name: {concept.name}")
        if concept.formal_spec:
            lines.append(f"  formal_spec: {concept.formal_spec}")
    return lines


def _parse_claim_edges(raw_list: list) -> list[ClaimEdge]:
    """Parse raw edge dicts from the gap-fill response into ClaimEdge objects.

    Skips malformed entries and logs warnings.

    @param raw_list List of raw edge dicts from the LLM response.
    @returns List of valid ClaimEdge objects.
    """
    edges: list[ClaimEdge] = []
    for entry in raw_list:
        edge = _try_build_claim_edge(entry)
        if edge is not None:
            edges.append(edge)
    return edges


def _try_build_claim_edge(entry: object) -> ClaimEdge | None:
    """Attempt to build a ClaimEdge from a raw dict.

    Maps gap-fill format (source/target keys) to ClaimEdge fields.

    @param entry Raw dict from the LLM response.
    @returns ClaimEdge or None on failure.
    """
    if not isinstance(entry, dict):
        logger.warning("Skipping non-dict gap-fill edge entry: %r", entry)
        return None
    try:
        source = entry.get("source") or entry.get("source_slug", "")
        target = entry.get("target") or entry.get("target_slug", "")
        edge_type = entry.get("type") or entry.get("edge_type", "")
        attrs = entry.get("attributes", {})
        if not (source and target and edge_type):
            return None
        return ClaimEdge(
            source_slug=source,
            target_slug=target,
            edge_type=edge_type,
            attributes=attrs if isinstance(attrs, dict) else {},
        )
    except Exception as err:
        logger.warning("Skipping invalid gap-fill edge: %s — %r", err, entry)
        return None


def _edge_key(edge: ClaimEdge) -> _EdgeKey:
    """Return a deduplication key for a ClaimEdge.

    @param edge The ClaimEdge to key.
    @returns Tuple of (source_slug, target_slug, edge_type).
    """
    return (edge.source_slug, edge.target_slug, edge.edge_type)


def _build_edge_key_set(edges: list[ClaimEdge]) -> set[_EdgeKey]:
    """Build a set of edge keys from an existing edge list.

    @param edges List of existing ClaimEdge objects.
    @returns Set of (source_slug, target_slug, edge_type) tuples.
    """
    return {_edge_key(e) for e in edges}


def _safe_parse_json(content: str) -> dict | None:
    """Attempt to parse JSON, returning None on failure.

    @param content Raw string from the LLM response.
    @returns Parsed dict, or None if parsing failed.
    """
    try:
        return json.loads(content)
    except (json.JSONDecodeError, ValueError):
        return None
