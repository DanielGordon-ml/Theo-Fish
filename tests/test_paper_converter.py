"""
@file test_paper_converter.py
@description Tests for paper conversion with arxiv2md and MinerU fallback.
"""

import pytest
from pathlib import Path
from data_loader.paper_converter import (
    convert_with_arxiv2md,
    convert_paper,
    convert_local_pdf,
)
from data_loader.models import PaperInput, ConversionResult


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


@pytest.mark.asyncio
class TestConvertLocalPdf:
    async def test_success(self, tmp_path, monkeypatch):
        """It should convert a local PDF using MinerU."""
        # Create a fake PDF file
        for_process_dir = tmp_path / "for_process"
        for_process_dir.mkdir()
        pdf_file = for_process_dir / "my_paper.pdf"
        pdf_file.write_bytes(b"%PDF-1.4 fake content")

        # Patch run_in_executor to call _run_mineru synchronously
        # (ProcessPoolExecutor can't pickle local mock functions)
        async def mock_run_in_executor(executor, func, *args):
            return "# Extracted Content\n\nSome text from PDF."

        import asyncio

        loop = asyncio.get_event_loop()
        monkeypatch.setattr(loop, "run_in_executor", mock_run_in_executor)

        paper = PaperInput(
            arxiv_id="my_paper",
            is_local=True,
            local_filename="my_paper.pdf",
        )
        result = await convert_local_pdf(paper, for_process_dir)
        assert result is not None
        assert result.arxiv_id == "my_paper"
        assert result.converter_used == "mineru"
        assert "Extracted Content" in result.markdown_content

    async def test_missing_pdf_returns_none(self, tmp_path):
        """It should return None when the PDF file does not exist."""
        for_process_dir = tmp_path / "for_process"
        for_process_dir.mkdir()

        paper = PaperInput(
            arxiv_id="missing",
            is_local=True,
            local_filename="missing.pdf",
        )
        result = await convert_local_pdf(paper, for_process_dir)
        assert result is None

    async def test_mineru_failure_returns_none(self, tmp_path, monkeypatch):
        """It should return None when MinerU fails on a local PDF."""
        for_process_dir = tmp_path / "for_process"
        for_process_dir.mkdir()
        pdf_file = for_process_dir / "bad.pdf"
        pdf_file.write_bytes(b"%PDF-1.4 corrupt")

        async def mock_run_in_executor(executor, func, *args):
            raise RuntimeError("MinerU parse error")

        import asyncio

        loop = asyncio.get_event_loop()
        monkeypatch.setattr(loop, "run_in_executor", mock_run_in_executor)

        paper = PaperInput(
            arxiv_id="bad",
            is_local=True,
            local_filename="bad.pdf",
        )
        result = await convert_local_pdf(paper, for_process_dir)
        assert result is None
