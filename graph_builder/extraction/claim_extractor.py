"""
@file claim_extractor.py
@description Per-section claim extractor: builds prompts, calls the LLM,
parses the response, and generates ABOUT coupling edges linking each claim
to the concept slugs listed in its about_concepts field.
"""

import logging

from graph_builder.config.schema_types import GraphSchema
from graph_builder.extraction.prompt_generator import build_claim_prompt
from graph_builder.llm.protocol import LLMClient
from graph_builder.llm.response_parser import parse_claims
from graph_builder.models.claim import ClaimNode
from graph_builder.models.edges import CouplingEdge
from graph_builder.models.section import Section

logger = logging.getLogger("graph_builder")


async def extract_claims_from_section(
    section: Section,
    schema: GraphSchema,
    llm_client: LLMClient,
    concept_list: list[dict],
    paper_slug: str,
    proof_map: dict[str, str] | None = None,
) -> tuple[list[ClaimNode], list[CouplingEdge]]:
    """Extract claim nodes and ABOUT coupling edges from a single paper section.

    Builds a schema-driven system prompt (with concept grounding) and a user
    prompt embedding the section content. Parses the LLM response into
    ClaimNode objects, then derives CouplingEdge objects from each claim's
    about_concepts field. Returns empty lists on LLM failure or bad JSON.

    @param section The paper section to process.
    @param schema The GraphSchema used to build prompts and validate output.
    @param llm_client Async LLM client for the extraction call.
    @param concept_list Section-local concept dicts with name/slug/type keys.
    @param paper_slug Slug of the source paper for composing claim slugs.
    @param proof_map Optional mapping of claim labels to deferred proof text.
    @returns Tuple of (claims, coupling_edges), both empty on failure.
    """
    system_prompt = build_claim_prompt(schema, concept_list)
    user_prompt = _build_user_prompt(section.content, proof_map)

    try:
        response = await llm_client.call(system_prompt, user_prompt)
    except Exception as err:
        logger.error(
            "LLM call failed for section '%s': %s",
            section.heading,
            err,
        )
        return [], []

    raw_data = _safe_parse_json(response.content)
    if raw_data is None:
        return [], []

    claims = parse_claims(response.content, paper_slug, schema)
    raw_claim_dicts = raw_data.get("claims", [])
    coupling_edges = _build_coupling_edges(claims, raw_claim_dicts)

    return claims, coupling_edges


def _safe_parse_json(content: str) -> dict | None:
    """Attempt to parse a JSON string, returning None on failure.

    @param content Raw string from the LLM response.
    @returns Parsed dict, or None if parsing failed.
    """
    import json

    try:
        return json.loads(content)
    except (json.JSONDecodeError, ValueError):
        return None


def _build_coupling_edges(
    claims: list[ClaimNode],
    raw_claim_dicts: list,
) -> list[CouplingEdge]:
    """Build ABOUT CouplingEdge objects from parsed claims and their raw dicts.

    Pairs each ClaimNode with its corresponding raw dict by position, then
    converts each slug in about_concepts into a CouplingEdge.

    @param claims Validated ClaimNode list (parallel to raw_claim_dicts).
    @param raw_claim_dicts Raw list of claim dicts from the LLM response.
    @returns Flat list of CouplingEdge objects.
    """
    edges: list[CouplingEdge] = []

    for claim, raw in zip(claims, raw_claim_dicts):
        if not isinstance(raw, dict):
            continue
        about = raw.get("about_concepts")
        if not isinstance(about, list):
            continue
        edges.extend(_edges_for_claim(claim.slug, about))

    return edges


def _edges_for_claim(claim_slug: str, concept_slugs: list) -> list[CouplingEdge]:
    """Convert a list of concept slugs into CouplingEdge objects for one claim.

    @param claim_slug Slug of the source claim.
    @param concept_slugs List of concept slugs from about_concepts.
    @returns List of CouplingEdge objects.
    """
    edges = []
    for slug in concept_slugs:
        if isinstance(slug, str) and slug:
            edges.append(CouplingEdge(claim_slug=claim_slug, concept_slug=slug))
    return edges


def _build_user_prompt(
    section_content: str,
    proof_map: dict[str, str] | None,
) -> str:
    """Build user prompt, injecting deferred proofs if they match.

    @param section_content Raw section text
    @param proof_map Optional mapping of claim labels to proof text
    @returns User prompt with any deferred proofs appended
    """
    if not proof_map:
        return section_content

    injections = _find_matching_proofs(section_content, proof_map)
    if not injections:
        return section_content

    parts = [section_content, "", "--- DEFERRED PROOF (from appendix) ---"]
    for label, proof_text in injections:
        parts.append(f"Proof of {label}: {proof_text}")
    return "\n".join(parts)


def _find_matching_proofs(
    content: str,
    proof_map: dict[str, str],
) -> list[tuple[str, str]]:
    """Find proof map entries whose labels appear in the section content.

    @param content Section text to search
    @param proof_map Mapping of labels to proof text
    @returns List of (label, proof_text) tuples for matches
    """
    matches = []
    for label, proof_text in proof_map.items():
        if label in content:
            matches.append((label, proof_text))
    return matches
