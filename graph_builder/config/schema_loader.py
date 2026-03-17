"""
@file schema_loader.py
@description Reads _meta/schema.yaml into typed dataclasses.
"""

from pathlib import Path

import yaml

from graph_builder.config.schema_types import (
    ClaimTypeDef,
    ConceptTypeDef,
    EdgeCategories,
    EdgeDef,
    FieldOwnership,
    GraphSchema,
    ValidationConfig,
    ValidationSeverity,
)

_VALID_TOP_KEYS = {
    "version",
    "last_updated",
    "concept_types",
    "claim_types",
    "edges",
    "validation",
    "field_ownership",
}


def load_schema(path: Path) -> GraphSchema:
    """Load and validate schema.yaml into a GraphSchema dataclass.

    @param path Path to schema.yaml
    @raises ValueError on unknown keys or malformed YAML
    """
    with open(path, "r", encoding="utf-8") as f:
        raw = yaml.safe_load(f)

    _check_unknown_keys(raw)

    return GraphSchema(
        version=str(raw["version"]),
        last_updated=str(raw.get("last_updated", "")),
        concept_types=_parse_concept_types(raw.get("concept_types", {})),
        claim_types=_parse_claim_types(raw.get("claim_types", {})),
        edges=_parse_edges(raw.get("edges", {})),
        validation=_parse_validation(raw.get("validation", {})),
        field_ownership=_parse_field_ownership(raw.get("field_ownership", {})),
    )


def _check_unknown_keys(raw: dict) -> None:
    """Reject unrecognized top-level keys."""
    unknown = set(raw.keys()) - _VALID_TOP_KEYS
    if unknown:
        raise ValueError(f"Unknown top-level keys in schema.yaml: {unknown}")


def _parse_concept_types(raw: dict) -> dict[str, ConceptTypeDef]:
    """Parse concept type definitions from raw YAML."""
    return {
        name: ConceptTypeDef(
            description=defn.get("description", ""),
            required_fields=defn.get("required_fields", []),
            optional_fields=defn.get("optional_fields", []),
            examples=defn.get("examples", []),
        )
        for name, defn in raw.items()
    }


def _parse_claim_types(raw: dict) -> dict[str, ClaimTypeDef]:
    """Parse claim type definitions from raw YAML."""
    return {
        name: ClaimTypeDef(
            description=defn.get("description", ""),
            required_fields=defn.get("required_fields", []),
            optional_fields=defn.get("optional_fields", []),
            strength_values=defn.get("strength_values", []),
            status_values=defn.get("status_values", []),
        )
        for name, defn in raw.items()
    }


def _parse_edges(raw: dict) -> EdgeCategories:
    """Parse all edge category definitions."""
    return EdgeCategories(
        concept_edges=_parse_edge_group(raw.get("concept_edges", {})),
        claim_edges=_parse_edge_group(raw.get("claim_edges", {})),
        coupling_edges=_parse_edge_group(raw.get("coupling_edges", {})),
        provenance_edges=_parse_edge_group(raw.get("provenance_edges", {})),
    )


def _parse_edge_group(raw: dict) -> dict[str, EdgeDef]:
    """Parse a single group of edge definitions."""
    return {
        name: EdgeDef(
            description=defn.get("description", ""),
            attributes=defn.get("attributes", []),
            inverse=defn.get("inverse"),
            role_values=defn.get("role_values", []),
            nature_values=defn.get("nature_values", []),
            dimension_values=defn.get("dimension_values", []),
        )
        for name, defn in raw.items()
        if isinstance(defn, dict)
    }


def _parse_validation(raw: dict) -> ValidationConfig:
    """Parse validation rules and severity levels."""
    sev = raw.get("severity", {})
    return ValidationConfig(
        rules=raw.get("rules", []),
        severity=ValidationSeverity(
            error=sev.get("error", []),
            warning=sev.get("warning", []),
            info=sev.get("info", []),
        ),
    )


def _parse_field_ownership(raw: dict) -> FieldOwnership:
    """Parse field ownership categories."""
    return FieldOwnership(
        pipeline_owned=raw.get("pipeline_owned", []),
        human_owned=raw.get("human_owned", []),
        shared=raw.get("shared", []),
    )
