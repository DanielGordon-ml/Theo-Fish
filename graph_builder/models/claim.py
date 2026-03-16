"""
@file claim.py
@description ClaimNode dataclass for Graph B.
"""

from pydantic import BaseModel, model_validator

from graph_builder.shared.slugify import slugify


class ClaimNode(BaseModel):
    """An assertion in Graph B (Reasoning Graph)."""

    slug: str = ""
    source_paper_slug: str
    label: str
    name: str = ""
    claim_type: str
    assumptions: list[str] = []
    conclusion: str = ""
    proof_technique: str = ""
    strength: str = ""
    statement: str = ""
    proof: str = ""
    section: str = ""
    status: str = "unverified"
    confidence: float = 0.0
    human_notes: str = ""
    date_modified: str = ""

    @model_validator(mode="after")
    def _derive_fields(self):
        """Derive name from label and compose slug from paper slug + label."""
        if not self.name:
            self.name = self.label
        if not self.slug:
            label_slug = slugify(self.label)
            self.slug = f"{self.source_paper_slug}--{label_slug}"
        return self
