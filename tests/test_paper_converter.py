"""
@file test_paper_converter.py
@description Tests for paper conversion with arxiv2md and MinerU fallback.
"""

import pytest
from pathlib import Path
from data_loader.paper_converter import convert_with_arxiv2md, convert_with_mineru, convert_paper
from data_loader.models import ConversionResult


@pytest.mark.asyncio
class TestConvertWithArxiv2md:
    async def test_success(self, monkeypatch):
        """It should return ConversionResult when arxiv2md succeeds."""
        async def mock_ingest(paper_id, **kwargs):
            class MockResult:
                markdown = "# Test Paper\n\nContent with $E=mc^2$"
            return MockResult()

        monkeypatch.setattr(
            "data_loader.paper_converter._call_arxiv2md",
            mock_ingest,
        )
        result = await convert_with_arxiv2md("2706.03762")
        assert result is not None
        assert result.converter_used == "arxiv2md"
        assert "$E=mc^2$" in result.markdown_content

    async def test_failure_returns_none(self, monkeypatch):
        """It should return None when arxiv2md raises."""
        async def mock_ingest(paper_id, **kwargs):
            raise RuntimeError("No HTML version available")

        monkeypatch.setattr(
            "data_loader.paper_converter._call_arxiv2md",
            mock_ingest,
        )
        result = await convert_with_arxiv2md("2706.03762")
        assert result is None


@pytest.mark.asyncio
class TestConvertPaper:
    async def test_uses_arxiv2md_when_available(self, monkeypatch):
        """It should use arxiv2md as primary converter."""
        async def mock_arxiv2md(arxiv_id):
            return ConversionResult(
                arxiv_id=arxiv_id,
                markdown_content="# From arxiv2md",
                converter_used="arxiv2md",
                conversion_warnings=[],
            )

        monkeypatch.setattr(
            "data_loader.paper_converter.convert_with_arxiv2md",
            mock_arxiv2md,
        )
        result = await convert_paper("2706.03762", papers_dir=Path("/tmp"))
        assert result is not None
        assert result.converter_used == "arxiv2md"

    async def test_falls_back_to_mineru(self, monkeypatch):
        """It should fall back to MinerU when arxiv2md fails."""
        async def mock_arxiv2md(arxiv_id):
            return None

        async def mock_mineru(arxiv_id, papers_dir):
            return ConversionResult(
                arxiv_id=arxiv_id,
                markdown_content="# From MinerU",
                converter_used="mineru",
                conversion_warnings=[],
            )

        monkeypatch.setattr(
            "data_loader.paper_converter.convert_with_arxiv2md",
            mock_arxiv2md,
        )
        monkeypatch.setattr(
            "data_loader.paper_converter.convert_with_mineru",
            mock_mineru,
        )
        result = await convert_paper("2706.03762", papers_dir=Path("/tmp"))
        assert result is not None
        assert result.converter_used == "mineru"

    async def test_both_fail_returns_none(self, monkeypatch):
        """It should return None when both converters fail."""
        async def mock_arxiv2md(arxiv_id):
            return None

        async def mock_mineru(arxiv_id, papers_dir):
            return None

        monkeypatch.setattr(
            "data_loader.paper_converter.convert_with_arxiv2md",
            mock_arxiv2md,
        )
        monkeypatch.setattr(
            "data_loader.paper_converter.convert_with_mineru",
            mock_mineru,
        )
        result = await convert_paper("2706.03762", papers_dir=Path("/tmp"))
        assert result is None
