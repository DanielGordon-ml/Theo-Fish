"""
@file concept.py
@description ConceptNode dataclass for Graph A.
"""

from typing import Any

from pydantic import BaseModel, field_validator, model_validator

from graph_builder.shared.slugify import slugify


class ConceptNode(BaseModel):
    """A mathematical concept in Graph A (Concept Ontology)."""

    slug: str = ""
    name: str
    semantic_type: str
    rhetorical_origin: str = ""
    canonical_definition: str = ""
    formal_spec: str = ""
    components: list[str] = []
    ts_domain: str = ""
    ts_codomain: str = ""
    ts_applies_to: str = ""
    ts_member_type: str = ""
    ts_objective: str = ""
    type_specific_fields: dict[str, Any] = {}
    aliases: list[str] = []
    status: str = "canonical"
    embedding: list[float] = []
    human_notes: str = ""
    date_modified: str = ""

    @model_validator(mode="after")
    def _derive_slug(self):
        """Derive slug from name if not provided."""
        if not self.slug:
            self.slug = slugify(self.name)
        return self

    @field_validator("aliases", mode="after")
    @classmethod
    def _dedup_sort_aliases(cls, v: list[str]) -> list[str]:
        """Deduplicate and sort aliases."""
        return sorted(set(v))
