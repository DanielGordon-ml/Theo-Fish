"""
@file test_metadata_fetcher.py
@description Tests for ArXiv metadata fetching.
"""

import pytest
import httpx
from data_loader.metadata_fetcher import (
    get_math_subject,
    parse_arxiv_entry,
    parse_frontmatter_metadata,
    fetch_all_metadata,
    build_local_metadata,
)
from data_loader.models import PaperInput


class TestGetMathSubject:
    def test_known_category(self):
        """It should resolve known math categories to human-readable names."""
        assert get_math_subject("math.AG") == "Algebraic Geometry"

    def test_unknown_math_category(self):
        """It should return raw code for unknown math subcategories."""
        result = get_math_subject("math.ZZ")
        assert result == "math.ZZ"

    def test_non_math_category(self):
        """It should return raw code for non-math categories."""
        assert get_math_subject("cs.CL") == "cs.CL"

    def test_physics_category(self):
        """It should return raw code for physics categories."""
        assert get_math_subject("hep-th") == "hep-th"


# Sample Atom XML entry as returned by ArXiv API
SAMPLE_ENTRY_XML = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:arxiv="http://arxiv.org/schemas/atom">
  <entry>
    <id>http://arxiv.org/abs/2706.03762v1</id>
    <title>Attention Is All You Need</title>
    <summary>The dominant sequence transduction models...</summary>
    <published>2017-06-12T17:57:34Z</published>
    <author><name>Ashish Vaswani</name></author>
    <author><name>Noam Shazeer</name></author>
    <arxiv:primary_category term="cs.CL" />
    <category term="cs.CL" />
    <category term="cs.LG" />
  </entry>
</feed>"""


class TestParseArxivEntry:
    def test_parses_entry(self):
        """It should parse a feedparser entry into PaperMetadata."""
        import feedparser
        feed = feedparser.parse(SAMPLE_ENTRY_XML)
        entry = feed.entries[0]
        metadata = parse_arxiv_entry(entry)
        assert metadata.arxiv_id == "2706.03762"
        assert metadata.title == "Attention Is All You Need"
        assert metadata.authors == ["Ashish Vaswani", "Noam Shazeer"]
        assert metadata.publication_date == "2017-06-12"
        assert metadata.categories == ["cs.CL", "cs.LG"]
        assert metadata.primary_category == "cs.CL"
        assert metadata.source == "arxiv_api"


class TestBuildLocalMetadata:
    def test_uses_paper_name_as_title(self):
        """It should use paper_name as title for local papers."""
        paper = PaperInput(
            arxiv_id="my_paper",
            paper_name="My Great Paper",
            is_local=True,
            local_filename="my_paper.pdf",
        )
        meta = build_local_metadata(paper)
        assert meta.arxiv_id == "my_paper"
        assert meta.title == "My Great Paper"
        assert meta.source == "local"
        assert meta.authors == []
        assert meta.abstract == ""

    def test_falls_back_to_arxiv_id_for_title(self):
        """It should use arxiv_id as title when paper_name is missing."""
        paper = PaperInput(
            arxiv_id="my_paper",
            is_local=True,
            local_filename="my_paper.pdf",
        )
        meta = build_local_metadata(paper)
        assert meta.title == "my_paper"


@pytest.mark.asyncio
class TestParseFrontmatterMetadata:
    async def test_returns_none_on_failure(self, monkeypatch):
        """It should return None when arxiv2md fails."""
        async def mock_ingest(paper_id, **kwargs):
            raise RuntimeError("No HTML version")

        monkeypatch.setattr(
            "data_loader.metadata_fetcher._call_arxiv2md_frontmatter",
            mock_ingest,
        )
        result = await parse_frontmatter_metadata("9999.99999")
        assert result is None


@pytest.mark.asyncio
class TestFetchAllMetadata:
    async def test_fetches_batch(self, monkeypatch):
        """It should fetch metadata for a batch of papers."""
        async def mock_get(self, url, **kwargs):
            class MockResponse:
                status_code = 200
                text = SAMPLE_ENTRY_XML
                def raise_for_status(self):
                    pass
            return MockResponse()

        monkeypatch.setattr(httpx.AsyncClient, "get", mock_get)

        papers = [PaperInput(arxiv_id="2706.03762")]
        async with httpx.AsyncClient() as client:
            result = await fetch_all_metadata(papers, client)

        assert "2706.03762" in result
        assert result["2706.03762"].title == "Attention Is All You Need"

    async def test_handles_timeout(self, monkeypatch):
        """It should return empty dict on API timeout, not crash."""
        async def mock_get(self, url, **kwargs):
            raise httpx.TimeoutException("Connection timed out")

        monkeypatch.setattr(httpx.AsyncClient, "get", mock_get)

        papers = [PaperInput(arxiv_id="2706.03762")]
        async with httpx.AsyncClient() as client:
            result = await fetch_all_metadata(papers, client)

        assert result == {}

    async def test_returns_empty_for_missing(self, monkeypatch):
        """It should omit papers not found in the API response."""
        async def mock_get(self, url, **kwargs):
            class MockResponse:
                status_code = 200
                text = SAMPLE_ENTRY_XML  # Only has 2706.03762
                def raise_for_status(self):
                    pass
            return MockResponse()

        monkeypatch.setattr(httpx.AsyncClient, "get", mock_get)

        papers = [
            PaperInput(arxiv_id="2706.03762"),
            PaperInput(arxiv_id="9999.99999"),
        ]
        async with httpx.AsyncClient() as client:
            result = await fetch_all_metadata(papers, client)

        assert "2706.03762" in result
        assert "9999.99999" not in result

    async def test_skips_local_papers(self, monkeypatch):
        """It should not send local papers to the ArXiv API."""
        api_called_with = []

        async def mock_get(self, url, **kwargs):
            api_called_with.append(url)

            class MockResponse:
                status_code = 200
                text = SAMPLE_ENTRY_XML
                def raise_for_status(self):
                    pass
            return MockResponse()

        monkeypatch.setattr(httpx.AsyncClient, "get", mock_get)

        papers = [
            PaperInput(arxiv_id="2706.03762"),
            PaperInput(
                arxiv_id="local_paper",
                is_local=True,
                local_filename="local_paper.pdf",
            ),
        ]
        async with httpx.AsyncClient() as client:
            await fetch_all_metadata(papers, client)

        # Only the ArXiv paper should be in the API call
        assert len(api_called_with) == 1
        assert "local_paper" not in api_called_with[0]
        assert "2706.03762" in api_called_with[0]
