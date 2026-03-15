"""
@file test_json_writer.py
@description Tests for JSON document assembly and writing.
"""

import json
import pytest
from pathlib import Path
from data_loader.json_writer import assemble_document, write_document, should_skip
from data_loader.models import PaperInput, PaperMetadata, ConversionResult, PaperDocument


@pytest.fixture
def sample_metadata():
    """Sample PaperMetadata for testing."""
    return PaperMetadata(
        arxiv_id="2706.03762",
        title="Attention Is All You Need",
        authors=["Vaswani", "Shazeer"],
        abstract="The dominant sequence...",
        publication_date="2017-06-12",
        categories=["cs.CL", "cs.LG"],
        primary_category="cs.CL",
        math_subject="cs.CL",
        source="arxiv_api",
    )


@pytest.fixture
def sample_conversion():
    """Sample ConversionResult for testing."""
    return ConversionResult(
        arxiv_id="2706.03762",
        markdown_content="# Attention Is All You Need\n\nContent...",
        converter_used="arxiv2md",
        conversion_warnings=[],
    )


class TestAssembleDocument:
    def test_assembles_with_csv_name(self, sample_metadata, sample_conversion):
        """It should use the CSV paper_name when available."""
        paper_input = PaperInput(arxiv_id="2706.03762", paper_name="Custom Name")
        doc = assemble_document(paper_input, sample_metadata, sample_conversion)
        assert doc.paper_name == "Custom Name"
        assert doc.title == "Attention Is All You Need"
        assert doc.metadata_source == "arxiv_api"
        assert doc.converter_used == "arxiv2md"
        assert doc.processed_at  # should be set

    def test_uses_title_when_no_paper_name(self, sample_metadata, sample_conversion):
        """It should fall back to metadata title when no paper_name."""
        paper_input = PaperInput(arxiv_id="2706.03762")
        doc = assemble_document(paper_input, sample_metadata, sample_conversion)
        assert doc.paper_name == "Attention Is All You Need"

    def test_uses_arxiv_id_when_no_name_or_title(self, sample_conversion):
        """It should fall back to arxiv_id when no name or title."""
        metadata = PaperMetadata(
            arxiv_id="2706.03762", title="", authors=[], abstract="",
            publication_date="", categories=[], primary_category="",
            math_subject="", source="arxiv_api",
        )
        paper_input = PaperInput(arxiv_id="2706.03762")
        doc = assemble_document(paper_input, metadata, sample_conversion)
        assert doc.paper_name == "2706.03762"


class TestShouldSkip:
    def test_skip_when_exists(self, tmp_data_dir):
        """It should skip when JSON already exists."""
        processed = tmp_data_dir / "processed"
        (processed / "2706.03762.json").write_text("{}")
        assert should_skip("2706.03762", processed, force=False) is True

    def test_no_skip_when_missing(self, tmp_data_dir):
        """It should not skip when JSON is missing."""
        processed = tmp_data_dir / "processed"
        assert should_skip("2706.03762", processed, force=False) is False

    def test_no_skip_when_force(self, tmp_data_dir):
        """It should not skip when force is True."""
        processed = tmp_data_dir / "processed"
        (processed / "2706.03762.json").write_text("{}")
        assert should_skip("2706.03762", processed, force=True) is False

    def test_skip_legacy_id_with_slash(self, tmp_data_dir):
        """It should handle legacy IDs with slashes in filenames."""
        processed = tmp_data_dir / "processed"
        (processed / "cs_0512078.json").write_text("{}")
        assert should_skip("cs/0512078", processed, force=False) is True


class TestWriteDocument:
    def test_writes_valid_json(self, tmp_data_dir, sample_metadata, sample_conversion):
        """It should write valid JSON to disk."""
        paper_input = PaperInput(arxiv_id="2706.03762", paper_name="Test")
        doc = assemble_document(paper_input, sample_metadata, sample_conversion)
        processed = tmp_data_dir / "processed"
        write_document(doc, processed)

        json_file = processed / "2706.03762.json"
        assert json_file.exists()

        data = json.loads(json_file.read_text())
        assert data["arxiv_id"] == "2706.03762"
        assert data["title"] == "Attention Is All You Need"

    def test_json_roundtrips(self, tmp_data_dir, sample_metadata, sample_conversion):
        """It should produce JSON that roundtrips through PaperDocument."""
        paper_input = PaperInput(arxiv_id="2706.03762", paper_name="Test")
        doc = assemble_document(paper_input, sample_metadata, sample_conversion)
        processed = tmp_data_dir / "processed"
        write_document(doc, processed)

        loaded = PaperDocument.model_validate_json(
            (processed / "2706.03762.json").read_text()
        )
        assert loaded == doc
