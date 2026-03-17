"""
@file test_cleaner_cli.py
@description Tests for the data cleaner CLI.
"""

import subprocess
import sys


from data_loader.models import PaperDocument

from data_cleaner.cli import build_parser


def _make_paper_json(arxiv_id="0000.0000", markdown="# Title\n\nContent.\n"):
    """Create a minimal PaperDocument JSON string."""
    doc = PaperDocument(
        paper_name="test",
        arxiv_id=arxiv_id,
        title="Test",
        authors=["Author"],
        abstract="Abstract.",
        publication_date="2020-01-01",
        categories=["math.CO"],
        primary_category="math.CO",
        math_subject="math.CO",
        extracted_text_markdown=markdown,
        metadata_source="arxiv_api",
        converter_used="mineru",
        conversion_warnings=[],
        processed_at="2026-03-15T00:00:00+00:00",
    )
    return doc.model_dump_json(indent=2)


class TestBuildParser:
    def test_should_parse_defaults(self):
        """It should parse with default values when no args given."""
        parser = build_parser()
        args = parser.parse_args([])
        assert args.force is False
        assert args.concurrency == 8

    def test_should_parse_force_flag(self):
        """It should accept --force flag."""
        parser = build_parser()
        args = parser.parse_args(["--force"])
        assert args.force is True

    def test_should_parse_concurrency(self):
        """It should accept --concurrency N."""
        parser = build_parser()
        args = parser.parse_args(["--concurrency", "4"])
        assert args.concurrency == 4

    def test_should_parse_paper_id(self):
        """It should accept --paper ID for single-paper mode."""
        parser = build_parser()
        args = parser.parse_args(["--paper", "1234.5678"])
        assert args.paper == "1234.5678"

    def test_should_parse_input_and_output(self):
        """It should accept --input and --output paths."""
        parser = build_parser()
        args = parser.parse_args(["--input", "/tmp/in", "--output", "/tmp/out"])
        assert args.input == "/tmp/in"
        assert args.output == "/tmp/out"


class TestCliExecution:
    def test_should_run_as_module(self, tmp_path):
        """It should run via python -m data_cleaner."""
        input_dir = tmp_path / "processed"
        output_dir = tmp_path / "cleaned"
        input_dir.mkdir()
        output_dir.mkdir()

        paper_file = input_dir / "0000.0000.json"
        paper_file.write_text(_make_paper_json(), encoding="utf-8")

        result = subprocess.run(
            [
                sys.executable, "-m", "data_cleaner",
                "--input", str(input_dir),
                "--output", str(output_dir),
            ],
            capture_output=True,
            text=True,
            cwd=str(tmp_path.parent.parent),
            timeout=30,
        )
        assert result.returncode == 0
        assert (output_dir / "0000.0000.json").exists()

    def test_should_run_single_paper(self, tmp_path):
        """It should clean a single paper with --paper flag."""
        input_dir = tmp_path / "processed"
        output_dir = tmp_path / "cleaned"
        input_dir.mkdir()
        output_dir.mkdir()

        paper_file = input_dir / "1234.5678.json"
        paper_file.write_text(
            _make_paper_json(arxiv_id="1234.5678"), encoding="utf-8",
        )

        result = subprocess.run(
            [
                sys.executable, "-m", "data_cleaner",
                "--input", str(input_dir),
                "--output", str(output_dir),
                "--paper", "1234.5678",
            ],
            capture_output=True,
            text=True,
            cwd=str(tmp_path.parent.parent),
            timeout=30,
        )
        assert result.returncode == 0
        assert (output_dir / "1234.5678.json").exists()
