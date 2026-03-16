"""
@file models.py
@description Pydantic models for the data cleaner pipeline.
"""

from pydantic import BaseModel


class StageResult(BaseModel):
    """Result of running a single cleaning stage."""

    stage_name: str
    changes_made: int
    details: dict[str, int]
    skipped: bool = False
    error: str | None = None


class CleaningReport(BaseModel):
    """Report for cleaning a single paper."""

    arxiv_id: str
    input_path: str
    output_path: str
    stages: list[StageResult]
    total_changes: int
    cleaned_at: str
    status: str  # "cleaned" | "skipped" | "failed"


class CleaningBatchReport(BaseModel):
    """Aggregate report for a batch cleaning run."""

    total: int
    cleaned: int
    skipped: int
    failed: int
    reports: list[CleaningReport]
