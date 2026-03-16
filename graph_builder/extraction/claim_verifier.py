"""
@file claim_verifier.py
@description Pass 4 verification: checks extraction quality against source text
and auto-fixes issues. Routes low-confidence claims to review.
"""

import json
import logging

from graph_builder.llm.llm_client import LLMResponse
from graph_builder.llm.protocol import LLMClient
from graph_builder.models.claim import ClaimNode
from graph_builder.models.edges import CouplingEdge

logger = logging.getLogger("graph_builder")

_REVIEW_CONFIDENCE_THRESHOLD = 0.7
_FORBIDDEN_CORRECTION_FIELDS = {"label", "slug", "source_paper_slug"}


async def verify_section_claims(
    section_text: str,
    proof_map: dict[str, str],
    claims: list[ClaimNode],
    schema,
    llm_client: LLMClient,
    paper_slug: str,
    section_heading: str,
) -> tuple[list[ClaimNode], list[CouplingEdge]]:
    """Verify extracted claims against source text and auto-fix issues.

    @param section_text Original section text
    @param proof_map Mapping of claim labels to deferred proof text
    @param claims Extracted claims for this section (mutated in-place)
    @param schema GraphSchema (reserved for future use)
    @param llm_client LLM client for verification call
    @param paper_slug Source paper slug for new claims
    @param section_heading Section heading for new claims
    @returns Tuple of (new_claims, new_coupling_edges)
    """
    if not claims:
        return [], []

    try:
        response = await llm_client.call(
            _build_system_prompt(),
            _build_user_prompt(section_text, proof_map, claims),
        )
    except Exception as err:
        logger.error("Verification failed for '%s': %s", section_heading, err)
        return [], []

    result = _safe_parse_json(response.content)
    if result is None:
        return [], []

    apply_corrections(claims, result.get("corrections", []))
    apply_flags(claims, result.get("flags", []))
    return build_missing_claims(
        result.get("missing_claims", []), paper_slug, section_heading,
    )


def apply_corrections(claims: list[ClaimNode], corrections: list[dict]) -> None:
    """Apply field corrections to claims in-place. Skips forbidden fields.

    @param claims List of ClaimNodes to mutate
    @param corrections List of correction dicts from verifier
    """
    claim_index = {c.slug: c for c in claims}
    for corr in corrections:
        _apply_single_correction(claim_index, corr)


def _apply_single_correction(
    claim_index: dict[str, ClaimNode], corr: dict,
) -> None:
    """Apply one correction entry to the matching claim."""
    slug = corr.get("claim_slug", "")
    field = corr.get("field", "")
    value = corr.get("corrected_value", "")
    if field in _FORBIDDEN_CORRECTION_FIELDS:
        logger.warning("Skipping forbidden correction to '%s'", field)
        return
    claim = claim_index.get(slug)
    if claim is not None and hasattr(claim, field):
        setattr(claim, field, value)


def apply_flags(claims: list[ClaimNode], flags: list[dict]) -> None:
    """Route low-confidence claims to review.

    @param claims List of ClaimNodes to mutate
    @param flags List of flag dicts from verifier
    """
    claim_index = {c.slug: c for c in claims}
    for flag in flags:
        _apply_single_flag(claim_index, flag)


def _apply_single_flag(
    claim_index: dict[str, ClaimNode], flag: dict,
) -> None:
    """Apply one flag entry, setting review_needed if below threshold."""
    slug = flag.get("claim_slug", "")
    confidence = flag.get("confidence", 1.0)
    if confidence >= _REVIEW_CONFIDENCE_THRESHOLD:
        return
    claim = claim_index.get(slug)
    if claim is not None:
        claim.status = "review_needed"


def build_missing_claims(
    missing: list[dict], paper_slug: str, section_heading: str,
) -> tuple[list[ClaimNode], list[CouplingEdge]]:
    """Construct ClaimNodes and coupling edges from missing claim data.

    @param missing List of missing claim dicts from verifier
    @param paper_slug Source paper slug
    @param section_heading Section heading for provenance
    @returns Tuple of (claims, coupling_edges)
    """
    claims: list[ClaimNode] = []
    edges: list[CouplingEdge] = []
    for entry in missing:
        result = _build_single_missing(entry, paper_slug, section_heading)
        if result is None:
            continue
        claim, entry_edges = result
        claims.append(claim)
        edges.extend(entry_edges)
    return claims, edges


def _build_single_missing(
    entry: dict, paper_slug: str, section_heading: str,
) -> tuple[ClaimNode, list[CouplingEdge]] | None:
    """Build one ClaimNode and its coupling edges from a missing entry."""
    label = entry.get("label", "")
    if not label:
        return None
    claim = ClaimNode(
        source_paper_slug=paper_slug, label=label,
        claim_type=entry.get("claim_type", "theorem"),
        statement=entry.get("statement", ""), section=section_heading,
    )
    edges = _build_concept_edges(claim.slug, entry.get("about_concepts", []))
    return claim, edges


def _build_concept_edges(
    claim_slug: str, concepts: list,
) -> list[CouplingEdge]:
    """Create CouplingEdge instances for each valid concept slug."""
    return [
        CouplingEdge(claim_slug=claim_slug, concept_slug=slug)
        for slug in concepts
        if isinstance(slug, str) and slug
    ]


def _build_system_prompt() -> str:
    """Build the system prompt for claim verification."""
    return (
        "You are a mathematical claim verification agent.\n"
        "You are given the original section text and extracted claims as JSON.\n"
        "Check each claim for:\n"
        "1. Completeness - are there claims in the text that weren't extracted?\n"
        "2. Fidelity - does each statement match the source verbatim?\n"
        "3. Proof completeness - is the proof text complete or truncated?\n"
        "4. Classification - is claim_type correct?\n"
        "5. proof_technique - is the label accurate?\n"
        "6. about_concepts - are references correct and non-duplicate?\n\n"
        "Return ONLY valid JSON with no additional text:\n"
        '{"missing_claims": [...], "corrections": [...], "flags": [...]}\n\n'
        "Rules:\n"
        "- Do NOT correct the 'label' field. Flag it instead.\n"
        "- Only flag claims with confidence below 0.7.\n"
        "- If everything looks correct, return empty arrays."
    )


def _build_user_prompt(
    section_text: str, proof_map: dict[str, str], claims: list[ClaimNode],
) -> str:
    """Build the user prompt with section text and extracted claims."""
    claims_json = _serialize_claims(claims)
    parts = ["## Source Text\n", section_text]
    if proof_map:
        parts.append("\n\n## Deferred Proofs\n")
        for label, text in proof_map.items():
            parts.append(f"Proof of {label}: {text}\n")
    parts.append(f"\n\n## Extracted Claims\n```json\n{claims_json}\n```")
    return "\n".join(parts)


def _serialize_claims(claims: list[ClaimNode]) -> str:
    """Serialize claims to JSON for the verification prompt."""
    return json.dumps(
        [{"slug": c.slug, "label": c.label, "claim_type": c.claim_type,
          "statement": c.statement, "proof": c.proof,
          "proof_technique": c.proof_technique, "strength": c.strength}
         for c in claims], indent=2,
    )


def _safe_parse_json(content: str) -> dict | None:
    """Parse JSON, returning None on failure."""
    try:
        return json.loads(content)
    except (json.JSONDecodeError, ValueError):
        logger.warning("Verifier returned invalid JSON")
        return None
