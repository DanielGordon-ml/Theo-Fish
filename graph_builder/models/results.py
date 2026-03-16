"""
@file results.py
@description Pipeline result models.
"""

from pydantic import BaseModel


class ValidationResult(BaseModel):
    """Result of schema validation for a single paper."""

    is_valid: bool
    errors: list[str] = []
    warnings: list[str] = []


class BuildResult(BaseModel):
    """Result of building a knowledge graph for a single paper."""

    arxiv_id: str
    status: str
    concept_count: int = 0
    claim_count: int = 0
    edge_count: int = 0
    error: str | None = None


class BatchBuildResult(BaseModel):
    """Aggregate result of building graphs for a batch of papers."""

    total: int
    built: int
    skipped: int
    failed: int
    results: list[BuildResult]
