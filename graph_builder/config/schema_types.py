"""
@file schema_types.py
@description Typed dataclass definitions for the parsed schema.yaml.
"""

from dataclasses import dataclass, field


@dataclass
class ConceptTypeDef:
    """Definition of a concept type from schema.yaml."""

    description: str
    required_fields: list[str]
    optional_fields: list[str] = field(default_factory=list)
    examples: list[str] = field(default_factory=list)


@dataclass
class ClaimTypeDef:
    """Definition of a claim type from schema.yaml."""

    description: str
    required_fields: list[str]
    optional_fields: list[str] = field(default_factory=list)
    strength_values: list[str] = field(default_factory=list)
    status_values: list[str] = field(default_factory=list)


@dataclass
class EdgeDef:
    """Definition of an edge type from schema.yaml."""

    description: str
    attributes: list[str] = field(default_factory=list)
    inverse: str | None = None
    role_values: list[str] = field(default_factory=list)
    nature_values: list[str] = field(default_factory=list)
    dimension_values: list[str] = field(default_factory=list)


@dataclass
class EdgeCategories:
    """All edge types grouped by category."""

    concept_edges: dict[str, EdgeDef] = field(default_factory=dict)
    claim_edges: dict[str, EdgeDef] = field(default_factory=dict)
    coupling_edges: dict[str, EdgeDef] = field(default_factory=dict)
    provenance_edges: dict[str, EdgeDef] = field(default_factory=dict)


@dataclass
class ValidationSeverity:
    """Validation rule severity classifications."""

    error: list[str] = field(default_factory=list)
    warning: list[str] = field(default_factory=list)
    info: list[str] = field(default_factory=list)

    def __getitem__(self, key: str) -> list[str]:
        """Allow dict-style access for severity levels."""
        return getattr(self, key)


@dataclass
class ValidationConfig:
    """Validation rules and severity levels."""

    rules: list[str] = field(default_factory=list)
    severity: ValidationSeverity = field(default_factory=ValidationSeverity)


@dataclass
class FieldOwnership:
    """Field ownership categories for export/sync-back."""

    pipeline_owned: list[str] = field(default_factory=list)
    human_owned: list[str] = field(default_factory=list)
    shared: list[str] = field(default_factory=list)


@dataclass
class GraphSchema:
    """Complete parsed schema.yaml."""

    version: str
    last_updated: str
    concept_types: dict[str, ConceptTypeDef]
    claim_types: dict[str, ClaimTypeDef]
    edges: EdgeCategories
    validation: ValidationConfig
    field_ownership: FieldOwnership
