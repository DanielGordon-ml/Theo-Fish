"""
@file test_orchestrator.py
@description Tests for the async batch orchestrator.
"""

import pytest
from pathlib import Path
from data_loader.orchestrator import process_batch
from data_loader.models import PaperInput, PaperMetadata, ConversionResult, BatchResult


@pytest.mark.asyncio
class TestProcessBatch:
    async def test_processes_papers(self, tmp_data_dir, monkeypatch):
        """It should process papers and return BatchResult."""
        async def mock_fetch_all(papers, client):
            return {
                "2706.03762": PaperMetadata(
                    arxiv_id="2706.03762",
                    title="Test Paper",
                    authors=["Author"],
                    abstract="Abstract",
                    publication_date="2017-06-12",
                    categories=["cs.CL"],
                    primary_category="cs.CL",
                    math_subject="cs.CL",
                    source="arxiv_api",
                ),
            }

        async def mock_convert(arxiv_id, papers_dir):
            return ConversionResult(
                arxiv_id=arxiv_id,
                markdown_content="# Test\nContent",
                converter_used="arxiv2md",
                conversion_warnings=[],
            )

        monkeypatch.setattr("data_loader.orchestrator.fetch_all_metadata", mock_fetch_all)
        monkeypatch.setattr("data_loader.orchestrator.convert_paper", mock_convert)

        papers = [PaperInput(arxiv_id="2706.03762", paper_name="Test Paper")]
        processed_dir = tmp_data_dir / "processed"
        papers_dir = tmp_data_dir / "papers"

        result = await process_batch(
            papers=papers,
            processed_dir=processed_dir,
            papers_dir=papers_dir,
            concurrency=5,
            force=False,
        )

        assert isinstance(result, BatchResult)
        assert result.processed == 1
        assert result.arxiv2md == 1
        assert result.failed == 0
        assert len(result.results) == 1
        assert result.results[0].status == "processed"
        assert (processed_dir / "2706.03762.json").exists()

    async def test_skips_existing(self, tmp_data_dir, monkeypatch):
        """It should skip already-processed papers."""
        async def mock_fetch_all(papers, client):
            return {}

        monkeypatch.setattr("data_loader.orchestrator.fetch_all_metadata", mock_fetch_all)

        processed_dir = tmp_data_dir / "processed"
        (processed_dir / "2706.03762.json").write_text("{}")

        papers = [PaperInput(arxiv_id="2706.03762")]
        result = await process_batch(
            papers=papers,
            processed_dir=processed_dir,
            papers_dir=tmp_data_dir / "papers",
            concurrency=5,
            force=False,
        )

        assert isinstance(result, BatchResult)
        assert result.skipped == 1
        assert result.processed == 0

    async def test_handles_conversion_failure(self, tmp_data_dir, monkeypatch):
        """It should count papers that fail conversion as failed."""
        async def mock_fetch_all(papers, client):
            return {
                "2706.03762": PaperMetadata(
                    arxiv_id="2706.03762", title="T", authors=[], abstract="",
                    publication_date="", categories=[], primary_category="",
                    math_subject="", source="arxiv_api",
                ),
            }

        async def mock_convert(arxiv_id, papers_dir):
            return None  # Both converters failed

        monkeypatch.setattr("data_loader.orchestrator.fetch_all_metadata", mock_fetch_all)
        monkeypatch.setattr("data_loader.orchestrator.convert_paper", mock_convert)

        papers = [PaperInput(arxiv_id="2706.03762")]
        result = await process_batch(
            papers=papers,
            processed_dir=tmp_data_dir / "processed",
            papers_dir=tmp_data_dir / "papers",
            concurrency=5,
            force=False,
        )

        assert isinstance(result, BatchResult)
        assert result.failed == 1
        assert result.processed == 0
