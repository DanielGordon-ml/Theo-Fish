"""
@file test_metadata_repairer.py
@description Tests for Stage 5: metadata repairer.
"""

from data_loader.models import PaperDocument

from data_cleaner.metadata_repairer import repair_metadata


def _make_doc(**overrides) -> PaperDocument:
    """Create a PaperDocument with sensible defaults, overriding specified fields."""
    defaults = {
        "paper_name": "test",
        "arxiv_id": "0000.0000",
        "title": "",
        "authors": [],
        "abstract": "",
        "publication_date": "",
        "categories": [],
        "primary_category": "",
        "math_subject": "",
        "extracted_text_markdown": "",
        "metadata_source": "local",
        "converter_used": "mineru",
        "conversion_warnings": [],
        "processed_at": "2026-03-15T00:00:00+00:00",
    }
    defaults.update(overrides)
    return PaperDocument(**defaults)


class TestTitleExtraction:
    def test_should_extract_title_from_first_h1(self):
        """It should extract title from the first # heading."""
        md = "# My Great Paper\n\nSome content."
        doc = _make_doc(extracted_text_markdown=md)
        result, stage = repair_metadata(doc)
        assert result.title == "My Great Paper"
        assert stage.details["title_extracted"] == 1

    def test_should_not_overwrite_existing_title(self):
        """It should skip title extraction when title is already set."""
        md = "# Heading\n\nContent."
        doc = _make_doc(title="Existing Title", extracted_text_markdown=md)
        result, stage = repair_metadata(doc)
        assert result.title == "Existing Title"
        assert stage.details.get("title_extracted", 0) == 0


class TestAuthorExtraction:
    def test_should_extract_authors_after_title(self):
        """It should parse author names between title and Abstract."""
        md = "# Paper Title\n\nJohn Smith, Jane Doe, and Bob Jones\n\n## Abstract\n\nText."
        doc = _make_doc(extracted_text_markdown=md)
        result, stage = repair_metadata(doc)
        assert "John Smith" in result.authors
        assert "Jane Doe" in result.authors
        assert "Bob Jones" in result.authors
        assert stage.details["authors_extracted"] == 1

    def test_should_handle_comma_separated_authors(self):
        """It should parse comma-separated author names."""
        md = "# Title\n\nAlice Brown, Charlie Davis\n\n## Abstract\n\nText."
        doc = _make_doc(extracted_text_markdown=md)
        result, _ = repair_metadata(doc)
        assert "Alice Brown" in result.authors
        assert "Charlie Davis" in result.authors

    def test_should_not_overwrite_existing_authors(self):
        """It should skip when authors are already populated."""
        md = "# Title\n\nNew Author\n\n## Abstract\n\nText."
        doc = _make_doc(authors=["Existing Author"], extracted_text_markdown=md)
        result, _ = repair_metadata(doc)
        assert result.authors == ["Existing Author"]


class TestAbstractExtraction:
    def test_should_extract_abstract_section(self):
        """It should extract text under ## Abstract heading."""
        md = "# Title\n\n## Abstract\n\nThis is the abstract text.\n\n## Introduction\n\nBody."
        doc = _make_doc(extracted_text_markdown=md)
        result, stage = repair_metadata(doc)
        assert "This is the abstract text." in result.abstract
        assert stage.details["abstract_extracted"] == 1

    def test_should_not_overwrite_existing_abstract(self):
        """It should skip when abstract is already populated."""
        md = "# Title\n\n## Abstract\n\nNew abstract.\n\n## Intro\n"
        doc = _make_doc(abstract="Existing abstract", extracted_text_markdown=md)
        result, _ = repair_metadata(doc)
        assert result.abstract == "Existing abstract"


class TestDateExtraction:
    def test_should_extract_year_from_text(self):
        """It should find a 4-digit year in the first 2000 chars."""
        md = "# Title\n\nPublished 2019\n\n## Abstract\n\nContent."
        doc = _make_doc(extracted_text_markdown=md)
        result, stage = repair_metadata(doc)
        assert "2019" in result.publication_date
        assert stage.details["date_extracted"] == 1

    def test_should_not_overwrite_existing_date(self):
        """It should skip when publication_date is already set."""
        md = "# Title\n\n2025 paper.\n"
        doc = _make_doc(publication_date="2020-01-01", extracted_text_markdown=md)
        result, _ = repair_metadata(doc)
        assert result.publication_date == "2020-01-01"


class TestSkipLogic:
    def test_should_skip_when_all_metadata_populated(self):
        """It should skip entirely when all metadata fields are filled."""
        doc = _make_doc(
            title="Title",
            authors=["Author"],
            abstract="Abstract text",
            publication_date="2020-01-01",
            extracted_text_markdown="# Title\n\nContent.",
        )
        result, stage = repair_metadata(doc)
        assert stage.skipped is True
        assert stage.changes_made == 0


class TestStageMetadata:
    def test_should_return_correct_stage_name(self):
        """It should return 'metadata_repairer' as stage_name."""
        doc = _make_doc(extracted_text_markdown="text")
        _, stage = repair_metadata(doc)
        assert stage.stage_name == "metadata_repairer"
