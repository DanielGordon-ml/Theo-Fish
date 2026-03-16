"""
@file response_parser.py
@description Parses LLM JSON responses into typed graph model objects.
"""

import json
import logging
from typing import Any

from graph_builder.config.schema_types import GraphSchema
from graph_builder.models.claim import ClaimNode
from graph_builder.models.concept import ConceptNode
from graph_builder.models.edges import ClaimEdge, ConceptEdge, CouplingEdge

logger = logging.getLogger("graph_builder")

# Keys the LLM returns that are not ClaimNode fields — filter before construction
_CLAIM_EXTRA_KEYS = {"about_concepts", "location"}


def parse_concepts(json_str: str, schema: GraphSchema) -> list[ConceptNode]:
    """Parse LLM JSON response for concept extraction into ConceptNode objects.

    Skips entries with missing required fields or unknown semantic_type values.
    Logs a warning for each skipped entry and for unparseable JSON.

    @param json_str Raw JSON string from LLM response
    @param schema GraphSchema for validating semantic_type values
    @returns List of validated ConceptNode objects
    """
    data = _parse_json(json_str)
    if data is None:
        return []

    raw_concepts = data.get("concepts")
    if not isinstance(raw_concepts, list):
        logger.warning("parse_concepts: 'concepts' key missing or not a list")
        return []

    valid_types = set(schema.concept_types.keys())
    nodes: list[ConceptNode] = []

    for entry in raw_concepts:
        node = _build_concept(entry, valid_types)
        if node is not None:
            nodes.append(node)

    return nodes


def parse_claims(
    json_str: str,
    paper_slug: str,
    schema: GraphSchema,
) -> list[ClaimNode]:
    """Parse LLM JSON response for claim extraction into ClaimNode objects.

    Skips entries with missing required fields or unknown claim_type values.
    Logs a warning for each skipped entry and for unparseable JSON.

    @param json_str Raw JSON string from LLM response
    @param paper_slug Slug of the source paper for composing claim slugs
    @param schema GraphSchema for validating claim_type values
    @returns List of validated ClaimNode objects
    """
    data = _parse_json(json_str)
    if data is None:
        return []

    raw_claims = data.get("claims")
    if not isinstance(raw_claims, list):
        logger.warning("parse_claims: 'claims' key missing or not a list")
        return []

    valid_types = set(schema.claim_types.keys())
    nodes: list[ClaimNode] = []

    for entry in raw_claims:
        node = _build_claim(entry, paper_slug, valid_types)
        if node is not None:
            nodes.append(node)

    return nodes


def parse_edges(
    json_str: str,
    schema: GraphSchema,
) -> tuple[list[ConceptEdge], list[ClaimEdge], list[CouplingEdge]]:
    """Parse LLM JSON response for edge extraction into typed edge objects.

    Handles concept_edges, claim_edges, and coupling_edges keys.
    Skips malformed entries and logs warnings.

    @param json_str Raw JSON string from LLM response
    @param schema GraphSchema (reserved for future edge-type validation)
    @returns Tuple of (concept_edges, claim_edges, coupling_edges)
    """
    data = _parse_json(json_str)
    if data is None:
        return [], [], []

    concept_edges = _build_concept_edges(data.get("concept_edges", []))
    claim_edges = _build_claim_edges(data.get("claim_edges", []))
    coupling_edges = _build_coupling_edges(data.get("coupling_edges", []))

    return concept_edges, claim_edges, coupling_edges


# ---------------------------------------------------------------------------
# Private helpers
# ---------------------------------------------------------------------------

def _parse_json(json_str: str) -> dict | None:
    """Attempt to parse a JSON string, logging a warning on failure.

    @param json_str Raw JSON input
    @returns Parsed dict, or None if parsing failed
    """
    try:
        return json.loads(json_str)
    except (json.JSONDecodeError, ValueError) as err:
        logger.warning("Response parser: invalid JSON — %s", err)
        return None


def _build_concept(entry: Any, valid_types: set[str]) -> ConceptNode | None:
    """Validate and construct a ConceptNode from a raw dict.

    @param entry Raw dict from LLM response
    @param valid_types Set of allowed semantic_type values from schema
    @returns ConceptNode or None if validation fails
    """
    if not isinstance(entry, dict):
        logger.warning("Skipping malformed concept entry (not a dict): %r", entry)
        return None

    name = entry.get("name")
    semantic_type = entry.get("semantic_type") or entry.get("type")

    if not name:
        logger.warning("Skipping invalid concept entry: missing 'name' — %r", entry)
        return None

    # Normalize the key for downstream consumption
    if semantic_type and "semantic_type" not in entry:
        entry["semantic_type"] = semantic_type

    if semantic_type not in valid_types:
        logger.warning(
            "Skipping concept '%s': unknown semantic_type '%s'",
            name,
            semantic_type,
        )
        return None

    try:
        return ConceptNode(**{k: v for k, v in entry.items() if v is not None})
    except Exception as err:
        logger.warning("Skipping malformed concept entry '%s': %s", name, err)
        return None


def _build_claim(
    entry: Any,
    paper_slug: str,
    valid_types: set[str],
) -> ClaimNode | None:
    """Validate and construct a ClaimNode from a raw dict.

    @param entry Raw dict from LLM response
    @param paper_slug Source paper slug for slug composition
    @param valid_types Set of allowed claim_type values from schema
    @returns ClaimNode or None if validation fails
    """
    if not isinstance(entry, dict):
        logger.warning("Skipping malformed claim entry (not a dict): %r", entry)
        return None

    label = entry.get("label") or entry.get("name")
    claim_type = entry.get("claim_type") or entry.get("type")

    if not label:
        logger.warning("Skipping invalid claim entry: missing 'label' — %r", entry)
        return None

    # Normalize keys for downstream consumption
    if label and "label" not in entry:
        entry["label"] = label
    if claim_type and "claim_type" not in entry:
        entry["claim_type"] = claim_type

    if claim_type not in valid_types:
        logger.warning(
            "Skipping claim '%s': unknown claim_type '%s'",
            label,
            claim_type,
        )
        return None

    try:
        filtered = {k: v for k, v in entry.items()
                    if v is not None and k not in _CLAIM_EXTRA_KEYS}
        return ClaimNode(
            source_paper_slug=paper_slug,
            **filtered,
        )
    except Exception as err:
        logger.warning("Skipping malformed claim entry '%s': %s", label, err)
        return None


def _build_concept_edges(raw_list: Any) -> list[ConceptEdge]:
    """Parse a list of raw dicts into ConceptEdge objects.

    @param raw_list List from LLM response (may be malformed)
    @returns List of valid ConceptEdge objects
    """
    if not isinstance(raw_list, list):
        return []

    edges: list[ConceptEdge] = []
    for entry in raw_list:
        edge = _try_build_edge(entry, ConceptEdge, "concept")
        if edge is not None:
            edges.append(edge)
    return edges


def _build_claim_edges(raw_list: Any) -> list[ClaimEdge]:
    """Parse a list of raw dicts into ClaimEdge objects.

    @param raw_list List from LLM response (may be malformed)
    @returns List of valid ClaimEdge objects
    """
    if not isinstance(raw_list, list):
        return []

    edges: list[ClaimEdge] = []
    for entry in raw_list:
        edge = _try_build_edge(entry, ClaimEdge, "claim")
        if edge is not None:
            edges.append(edge)
    return edges


def _build_coupling_edges(raw_list: Any) -> list[CouplingEdge]:
    """Parse a list of raw dicts into CouplingEdge objects.

    @param raw_list List from LLM response (may be malformed)
    @returns List of valid CouplingEdge objects
    """
    if not isinstance(raw_list, list):
        return []

    edges: list[CouplingEdge] = []
    for entry in raw_list:
        edge = _try_build_edge(entry, CouplingEdge, "coupling")
        if edge is not None:
            edges.append(edge)
    return edges


def _try_build_edge(entry: Any, model_cls: type, kind: str) -> Any:
    """Attempt to construct a typed edge from a raw dict.

    @param entry Raw dict from LLM response
    @param model_cls Pydantic model class to instantiate
    @param kind Human-readable edge category name for logging
    @returns Model instance or None on failure
    """
    if not isinstance(entry, dict):
        logger.warning("Skipping malformed %s edge (not a dict): %r", kind, entry)
        return None
    try:
        return model_cls(**entry)
    except Exception as err:
        logger.warning("Skipping invalid %s edge entry: %s — %r", kind, err, entry)
        return None
