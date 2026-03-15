"""
@file test_models.py
@description Tests for Pydantic data models.
"""

from data_loader.models import (
    PaperInput,
    PaperMetadata,
    ConversionResult,
    PaperDocument,
    PaperResult,
    BatchResult,
)


class TestPaperInput:
    def test_create_with_all_fields(self):
        """It should create PaperInput with all fields."""
        p = PaperInput(
            paper_name="Test Paper",
            arxiv_id="2706.03762",
            file_type="pdf",
        )
        assert p.paper_name == "Test Paper"
        assert p.arxiv_id == "2706.03762"
        assert p.file_type == "pdf"

    def test_create_minimal(self):
        """It should create PaperInput with only arxiv_id."""
        p = PaperInput(arxiv_id="2706.03762")
        assert p.paper_name is None
        assert p.file_type is None


class TestPaperMetadata:
    def test_create_full(self):
        """It should create PaperMetadata with all fields."""
        m = PaperMetadata(
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
        assert m.title == "Attention Is All You Need"
        assert len(m.authors) == 2
        assert m.source == "arxiv_api"


class TestConversionResult:
    def test_create(self):
        """It should create ConversionResult with markdown content."""
        c = ConversionResult(
            arxiv_id="2706.03762",
            markdown_content="# Title\nSome content with $E=mc^2$",
            converter_used="arxiv2md",
            conversion_warnings=[],
        )
        assert c.converter_used == "arxiv2md"
        assert "$E=mc^2$" in c.markdown_content


class TestPaperDocument:
    def test_create_full(self):
        """It should create PaperDocument with all fields."""
        d = PaperDocument(
            paper_name="Attention Is All You Need",
            arxiv_id="2706.03762",
            title="Attention Is All You Need",
            authors=["Vaswani", "Shazeer"],
            abstract="The dominant sequence...",
            publication_date="2017-06-12",
            categories=["cs.CL", "cs.LG"],
            primary_category="cs.CL",
            math_subject="cs.CL",
            extracted_text_markdown="# Full paper markdown",
            metadata_source="arxiv_api",
            converter_used="arxiv2md",
            conversion_warnings=[],
            processed_at="2026-03-15T14:30:00",
        )
        assert d.paper_name == "Attention Is All You Need"
        assert d.processed_at == "2026-03-15T14:30:00"

    def test_json_roundtrip(self):
        """It should survive JSON serialization roundtrip."""
        d = PaperDocument(
            paper_name="Test",
            arxiv_id="2706.03762",
            title="Test",
            authors=["A"],
            abstract="abs",
            publication_date="2017-06-12",
            categories=["math.AG"],
            primary_category="math.AG",
            math_subject="Algebraic Geometry",
            extracted_text_markdown="# Content",
            metadata_source="arxiv_api",
            converter_used="arxiv2md",
            conversion_warnings=["minor issue"],
            processed_at="2026-03-15T14:30:00",
        )
        json_str = d.model_dump_json(indent=2)
        d2 = PaperDocument.model_validate_json(json_str)
        assert d == d2


class TestPaperResult:
    def test_create_processed(self):
        """It should create a processed PaperResult."""
        r = PaperResult(
            arxiv_id="2706.03762",
            status="processed",
            converter="arxiv2md",
            output_path="/some/path.json",
        )
        assert r.status == "processed"
        assert r.converter == "arxiv2md"

    def test_create_failed(self):
        """It should create a failed PaperResult with error."""
        r = PaperResult(
            arxiv_id="2706.03762",
            status="failed",
            error="Both converters failed",
        )
        assert r.status == "failed"
        assert r.error == "Both converters failed"
        assert r.converter is None


class TestBatchResult:
    def test_create(self):
        """It should create BatchResult with counts and results list."""
        results = [
            PaperResult(arxiv_id="2706.03762", status="processed", converter="arxiv2md"),
            PaperResult(arxiv_id="1810.04805", status="skipped"),
        ]
        b = BatchResult(
            total=2,
            processed=1,
            skipped=1,
            failed=0,
            arxiv2md=1,
            mineru=0,
            results=results,
        )
        assert b.total == 2
        assert b.processed == 1
        assert len(b.results) == 2

    def test_json_roundtrip(self):
        """It should survive JSON serialization roundtrip."""
        b = BatchResult(
            total=1,
            processed=1,
            skipped=0,
            failed=0,
            arxiv2md=1,
            mineru=0,
            results=[
                PaperResult(arxiv_id="2706.03762", status="processed"),
            ],
        )
        json_str = b.model_dump_json(indent=2)
        b2 = BatchResult.model_validate_json(json_str)
        assert b == b2
