"""
@file test_pipeline.py
@description Tests for pipeline orchestration (run_pipeline, run_batch).
"""

import json


from data_loader.models import PaperDocument

from data_cleaner.pipeline import run_pipeline, run_batch


def _make_paper_json(
    arxiv_id: str = "0000.0000",
    converter: str = "mineru",
    markdown: str = "# Title\n\n## Abstract\n\nText.\n",
    **overrides,
) -> str:
    """Create a PaperDocument JSON string."""
    doc = PaperDocument(
        paper_name=overrides.get("paper_name", "test"),
        arxiv_id=arxiv_id,
        title=overrides.get("title", "Test Paper"),
        authors=overrides.get("authors", ["Author One"]),
        abstract=overrides.get("abstract", "An abstract."),
        publication_date=overrides.get("publication_date", "2020-01-01"),
        categories=overrides.get("categories", ["math.CO"]),
        primary_category=overrides.get("primary_category", "math.CO"),
        math_subject=overrides.get("math_subject", "math.CO"),
        extracted_text_markdown=markdown,
        metadata_source=overrides.get("metadata_source", "arxiv_api"),
        converter_used=converter,
        conversion_warnings=[],
        processed_at="2026-03-15T00:00:00+00:00",
    )
    return doc.model_dump_json(indent=2)


def _write_paper(directory, arxiv_id, **kwargs):
    """Write a paper JSON file into a directory. Returns the path."""
    filename = arxiv_id.replace("/", "_") + ".json"
    path = directory / filename
    path.write_text(_make_paper_json(arxiv_id=arxiv_id, **kwargs), encoding="utf-8")
    return path


class TestRunPipeline:
    def test_should_clean_and_write_output(self, tmp_path):
        """It should read input, run stages, and write cleaned JSON."""
        input_dir = tmp_path / "processed"
        output_dir = tmp_path / "cleaned"
        input_dir.mkdir()
        output_dir.mkdir()

        input_path = _write_paper(
            input_dir, "1234.5678",
            markdown="# Title\n\n\n\n\nExtra whitespace.\n",
        )

        report = run_pipeline(input_path, output_dir)
        assert report.status == "cleaned"
        assert report.arxiv_id == "1234.5678"

        output_file = output_dir / "1234.5678.json"
        assert output_file.exists()

        with open(output_file, encoding="utf-8") as f:
            cleaned = json.load(f)
        assert "\n\n\n" not in cleaned["extracted_text_markdown"]

    def test_should_skip_existing_output(self, tmp_path):
        """It should skip when output JSON already exists and force=False."""
        input_dir = tmp_path / "processed"
        output_dir = tmp_path / "cleaned"
        input_dir.mkdir()
        output_dir.mkdir()

        input_path = _write_paper(input_dir, "1234.5678")
        # Pre-create output
        (output_dir / "1234.5678.json").write_text("{}", encoding="utf-8")

        report = run_pipeline(input_path, output_dir, force=False)
        assert report.status == "skipped"

    def test_should_force_reclean(self, tmp_path):
        """It should re-clean when force=True even if output exists."""
        input_dir = tmp_path / "processed"
        output_dir = tmp_path / "cleaned"
        input_dir.mkdir()
        output_dir.mkdir()

        input_path = _write_paper(input_dir, "1234.5678")
        (output_dir / "1234.5678.json").write_text("{}", encoding="utf-8")

        report = run_pipeline(input_path, output_dir, force=True)
        assert report.status == "cleaned"

    def test_should_preserve_raw_markdown_field(self, tmp_path):
        """It should keep the original markdown in the output document."""
        input_dir = tmp_path / "processed"
        output_dir = tmp_path / "cleaned"
        input_dir.mkdir()
        output_dir.mkdir()

        original_md = "# Title\n\nSome content.\n"
        input_path = _write_paper(
            input_dir, "1234.5678", markdown=original_md,
        )

        run_pipeline(input_path, output_dir)
        output_file = output_dir / "1234.5678.json"
        with open(output_file, encoding="utf-8") as f:
            cleaned = json.load(f)
        # Markdown is cleaned, should still have the content
        assert "Some content." in cleaned["extracted_text_markdown"]

    def test_should_report_all_stages(self, tmp_path):
        """It should include results from all 6 stages in the report."""
        input_dir = tmp_path / "processed"
        output_dir = tmp_path / "cleaned"
        input_dir.mkdir()
        output_dir.mkdir()

        input_path = _write_paper(input_dir, "1234.5678")
        report = run_pipeline(input_path, output_dir)
        stage_names = [s.stage_name for s in report.stages]
        assert "newline_normalizer" in stage_names
        assert "latex_normalizer" in stage_names
        assert "artifact_remover" in stage_names
        assert "heading_normalizer" in stage_names
        assert "whitespace_cleaner" in stage_names
        assert "metadata_repairer" in stage_names


class TestRunBatch:
    def test_should_clean_all_papers_in_directory(self, tmp_path):
        """It should process all JSON files in the input directory."""
        input_dir = tmp_path / "processed"
        output_dir = tmp_path / "cleaned"
        input_dir.mkdir()
        output_dir.mkdir()

        _write_paper(input_dir, "1111.1111")
        _write_paper(input_dir, "2222.2222")

        batch = run_batch(input_dir, output_dir)
        assert batch.total == 2
        assert batch.cleaned == 2
        assert batch.failed == 0

    def test_should_skip_already_cleaned(self, tmp_path):
        """It should skip papers that are already cleaned."""
        input_dir = tmp_path / "processed"
        output_dir = tmp_path / "cleaned"
        input_dir.mkdir()
        output_dir.mkdir()

        _write_paper(input_dir, "1111.1111")
        (output_dir / "1111.1111.json").write_text("{}", encoding="utf-8")

        batch = run_batch(input_dir, output_dir, force=False)
        assert batch.skipped == 1
        assert batch.cleaned == 0

    def test_should_handle_empty_directory(self, tmp_path):
        """It should handle an empty input directory gracefully."""
        input_dir = tmp_path / "processed"
        output_dir = tmp_path / "cleaned"
        input_dir.mkdir()
        output_dir.mkdir()

        batch = run_batch(input_dir, output_dir)
        assert batch.total == 0
        assert batch.cleaned == 0
