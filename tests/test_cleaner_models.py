"""
@file test_cleaner_models.py
@description Tests for data cleaner Pydantic models.
"""

from data_cleaner.models import CleaningBatchReport, CleaningReport, StageResult


class TestStageResult:
    def test_create_with_all_fields(self):
        """It should create a StageResult with all fields."""
        result = StageResult(
            stage_name="newline_normalizer",
            changes_made=5,
            details={"literal_newlines": 3, "prefix_stripped": 1},
        )
        assert result.stage_name == "newline_normalizer"
        assert result.changes_made == 5
        assert result.details["literal_newlines"] == 3
        assert result.skipped is False
        assert result.error is None

    def test_create_skipped(self):
        """It should create a skipped StageResult."""
        result = StageResult(
            stage_name="newline_normalizer",
            changes_made=0,
            details={},
            skipped=True,
        )
        assert result.skipped is True
        assert result.changes_made == 0

    def test_create_with_error(self):
        """It should create a StageResult with an error."""
        result = StageResult(
            stage_name="latex_normalizer",
            changes_made=0,
            details={},
            error="Regex timeout",
        )
        assert result.error == "Regex timeout"


class TestCleaningReport:
    def test_create_cleaned_report(self):
        """It should create a report for a successfully cleaned paper."""
        stage = StageResult(
            stage_name="whitespace_cleaner",
            changes_made=2,
            details={"collapsed_newlines": 2},
        )
        report = CleaningReport(
            arxiv_id="1904.07272",
            input_path="Data/processed/1904.07272.json",
            output_path="Data/cleaned/1904.07272.json",
            stages=[stage],
            total_changes=2,
            cleaned_at="2026-03-15T00:00:00+00:00",
            status="cleaned",
        )
        assert report.arxiv_id == "1904.07272"
        assert report.status == "cleaned"
        assert len(report.stages) == 1
        assert report.total_changes == 2

    def test_create_skipped_report(self):
        """It should create a report for a skipped paper."""
        report = CleaningReport(
            arxiv_id="1904.07272",
            input_path="Data/processed/1904.07272.json",
            output_path="Data/cleaned/1904.07272.json",
            stages=[],
            total_changes=0,
            cleaned_at="2026-03-15T00:00:00+00:00",
            status="skipped",
        )
        assert report.status == "skipped"
        assert report.stages == []

    def test_create_failed_report(self):
        """It should create a report for a failed paper."""
        report = CleaningReport(
            arxiv_id="1904.07272",
            input_path="Data/processed/1904.07272.json",
            output_path="",
            stages=[],
            total_changes=0,
            cleaned_at="2026-03-15T00:00:00+00:00",
            status="failed",
        )
        assert report.status == "failed"


class TestCleaningBatchReport:
    def test_create_batch_report(self):
        """It should create an aggregate batch report."""
        report = CleaningBatchReport(
            total=3,
            cleaned=2,
            skipped=1,
            failed=0,
            reports=[],
        )
        assert report.total == 3
        assert report.cleaned == 2
        assert report.skipped == 1
        assert report.failed == 0

    def test_batch_report_with_individual_reports(self):
        """It should include individual cleaning reports."""
        individual = CleaningReport(
            arxiv_id="1011.4748",
            input_path="in.json",
            output_path="out.json",
            stages=[],
            total_changes=0,
            cleaned_at="2026-03-15T00:00:00+00:00",
            status="cleaned",
        )
        batch = CleaningBatchReport(
            total=1,
            cleaned=1,
            skipped=0,
            failed=0,
            reports=[individual],
        )
        assert len(batch.reports) == 1
        assert batch.reports[0].arxiv_id == "1011.4748"
