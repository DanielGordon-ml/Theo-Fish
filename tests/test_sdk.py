"""
@file test_sdk.py
@description Tests for the high-level SDK functions.
"""

import pytest
from data_loader.sdk import load_paper, load_papers, is_processed
from data_loader.errors import LoaderError
from data_loader.models import (
    PaperResult,
    BatchResult,
)


@pytest.mark.asyncio
class TestLoadPaper:
    async def test_success(self, tmp_data_dir, monkeypatch):
        """It should return PaperResult on success."""

        async def mock_process_batch(
            papers, processed_dir, papers_dir, concurrency, force
        ):
            return BatchResult(
                total=1,
                processed=1,
                skipped=0,
                failed=0,
                arxiv2md=1,
                mineru=0,
                results=[
                    PaperResult(
                        arxiv_id="2706.03762",
                        status="processed",
                        converter="arxiv2md",
                        output_path=str(tmp_data_dir / "processed" / "2706.03762.json"),
                    )
                ],
            )

        monkeypatch.setattr("data_loader.sdk.process_batch", mock_process_batch)

        result = await load_paper(
            "2706.03762",
            output_dir=tmp_data_dir / "processed",
            papers_dir=tmp_data_dir / "papers",
        )
        assert result.status == "processed"
        assert result.arxiv_id == "2706.03762"

    async def test_failure_raises_loader_error(self, tmp_data_dir, monkeypatch):
        """It should raise LoaderError when processing fails."""

        async def mock_process_batch(
            papers, processed_dir, papers_dir, concurrency, force
        ):
            return BatchResult(
                total=1,
                processed=0,
                skipped=0,
                failed=1,
                arxiv2md=0,
                mineru=0,
                results=[
                    PaperResult(
                        arxiv_id="9999.99999",
                        status="failed",
                        error="Both converters failed",
                    )
                ],
            )

        monkeypatch.setattr("data_loader.sdk.process_batch", mock_process_batch)

        with pytest.raises(LoaderError) as exc_info:
            await load_paper(
                "9999.99999",
                output_dir=tmp_data_dir / "processed",
                papers_dir=tmp_data_dir / "papers",
            )
        assert "9999.99999" in str(exc_info.value)

    async def test_normalizes_id(self, tmp_data_dir, monkeypatch):
        """It should normalize ArXiv IDs before processing."""
        captured_papers = []

        async def mock_process_batch(
            papers, processed_dir, papers_dir, concurrency, force
        ):
            captured_papers.extend(papers)
            return BatchResult(
                total=1,
                processed=1,
                skipped=0,
                failed=0,
                arxiv2md=1,
                mineru=0,
                results=[
                    PaperResult(
                        arxiv_id="2706.03762",
                        status="processed",
                        converter="arxiv2md",
                    )
                ],
            )

        monkeypatch.setattr("data_loader.sdk.process_batch", mock_process_batch)

        await load_paper(
            "https://arxiv.org/abs/2706.03762v2",
            output_dir=tmp_data_dir / "processed",
            papers_dir=tmp_data_dir / "papers",
        )
        assert captured_papers[0].arxiv_id == "2706.03762"

    async def test_invalid_id_raises(self, tmp_data_dir):
        """It should raise LoaderError for invalid IDs."""
        with pytest.raises(LoaderError):
            await load_paper(
                "not-a-valid-id",
                output_dir=tmp_data_dir / "processed",
                papers_dir=tmp_data_dir / "papers",
            )


@pytest.mark.asyncio
class TestLoadPapers:
    async def test_returns_batch_result(self, tmp_data_dir, monkeypatch):
        """It should return BatchResult for multiple papers."""

        async def mock_process_batch(
            papers, processed_dir, papers_dir, concurrency, force
        ):
            return BatchResult(
                total=2,
                processed=2,
                skipped=0,
                failed=0,
                arxiv2md=2,
                mineru=0,
                results=[
                    PaperResult(
                        arxiv_id="2706.03762", status="processed", converter="arxiv2md"
                    ),
                    PaperResult(
                        arxiv_id="1810.04805", status="processed", converter="arxiv2md"
                    ),
                ],
            )

        monkeypatch.setattr("data_loader.sdk.process_batch", mock_process_batch)

        result = await load_papers(
            ["2706.03762", "1810.04805"],
            output_dir=tmp_data_dir / "processed",
            papers_dir=tmp_data_dir / "papers",
        )
        assert isinstance(result, BatchResult)
        assert result.total == 2
        assert result.processed == 2

    async def test_never_raises(self, tmp_data_dir, monkeypatch):
        """It should never raise, even on failures — captures in BatchResult."""

        async def mock_process_batch(
            papers, processed_dir, papers_dir, concurrency, force
        ):
            return BatchResult(
                total=1,
                processed=0,
                skipped=0,
                failed=1,
                arxiv2md=0,
                mineru=0,
                results=[
                    PaperResult(
                        arxiv_id="9999.99999",
                        status="failed",
                        error="test",
                    )
                ],
            )

        monkeypatch.setattr("data_loader.sdk.process_batch", mock_process_batch)

        result = await load_papers(
            ["9999.99999"],
            output_dir=tmp_data_dir / "processed",
            papers_dir=tmp_data_dir / "papers",
        )
        assert result.failed == 1


class TestIsProcessed:
    def test_returns_true_when_exists(self, tmp_data_dir):
        """It should return True when JSON file exists."""
        processed = tmp_data_dir / "processed"
        (processed / "2706.03762.json").write_text("{}")
        assert is_processed("2706.03762", output_dir=processed) is True

    def test_returns_false_when_missing(self, tmp_data_dir):
        """It should return False when JSON file is missing."""
        processed = tmp_data_dir / "processed"
        assert is_processed("2706.03762", output_dir=processed) is False
