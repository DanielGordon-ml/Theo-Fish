"""
@file test_main_stages.py
@description Tests for main.py pipeline stage functions and --from flag.
"""

import argparse
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from main import _build_arg_parser, _clean_stage, _load_stage


class TestBuildArgParser:
    """Tests for the --from CLI flag."""

    def test_should_default_from_to_load(self):
        """It should default --from to 'load' when not specified."""
        parser = _build_arg_parser()
        args = parser.parse_args(["2502.00425"])
        assert args.from_stage == "load"

    def test_should_accept_from_clean(self):
        """It should accept --from clean."""
        parser = _build_arg_parser()
        args = parser.parse_args(["--from", "clean", "2502.00425"])
        assert args.from_stage == "clean"

    def test_should_accept_from_process(self):
        """It should accept --from process."""
        parser = _build_arg_parser()
        args = parser.parse_args(["--from", "process", "2502.00425"])
        assert args.from_stage == "process"

    def test_should_reject_invalid_from_value(self):
        """It should reject invalid --from values."""
        parser = _build_arg_parser()
        with pytest.raises(SystemExit):
            parser.parse_args(["--from", "invalid", "2502.00425"])


class TestLoadStage:
    """Tests for _load_stage()."""

    @pytest.mark.asyncio
    async def test_should_call_sdk_with_csv(self):
        """It should call load_papers with csv_path when csv provided."""
        mock_result = MagicMock()
        mock_result.total = 3
        mock_result.processed = 2
        mock_result.skipped = 1
        mock_result.failed = 0

        with patch("main.load_papers", new_callable=AsyncMock) as mock_load:
            mock_load.return_value = mock_result
            await _load_stage(
                arxiv_id=None,
                csv_path="../Data/papers.csv",
                force=False,
            )
            mock_load.assert_called_once_with(
                arxiv_ids=[],
                csv_path=Path("../Data/papers.csv"),
                force=False,
            )

    @pytest.mark.asyncio
    async def test_should_call_sdk_with_single_id(self):
        """It should call load_papers with arxiv_ids for a single paper."""
        mock_result = MagicMock()
        mock_result.total = 1
        mock_result.processed = 1
        mock_result.skipped = 0
        mock_result.failed = 0

        with patch("main.load_papers", new_callable=AsyncMock) as mock_load:
            mock_load.return_value = mock_result
            await _load_stage(
                arxiv_id="2502.00425",
                csv_path=None,
                force=True,
            )
            mock_load.assert_called_once_with(
                arxiv_ids=["2502.00425"],
                force=True,
            )

    @pytest.mark.asyncio
    async def test_should_propagate_force(self):
        """It should pass force=True to load_papers."""
        mock_result = MagicMock()
        mock_result.total = 1
        mock_result.processed = 1
        mock_result.skipped = 0
        mock_result.failed = 0

        with patch("main.load_papers", new_callable=AsyncMock) as mock_load:
            mock_load.return_value = mock_result
            await _load_stage(
                arxiv_id="2502.00425",
                csv_path=None,
                force=True,
            )
            _, kwargs = mock_load.call_args
            assert kwargs["force"] is True

    @pytest.mark.asyncio
    async def test_should_not_raise_on_failure(self):
        """It should log but not raise when load_papers fails."""
        with patch("main.load_papers", new_callable=AsyncMock) as mock_load:
            mock_load.side_effect = Exception("download failed")
            # Should not raise — failures are non-fatal
            await _load_stage(
                arxiv_id="2502.00425",
                csv_path=None,
                force=False,
            )


class TestCleanStage:
    """Tests for _clean_stage()."""

    def test_should_call_clean_per_paper(self, tmp_path):
        """It should call clean_paper for each paper with a processed JSON."""
        # Create fake processed files
        for aid in ["2502.00425", "1904.07272"]:
            (tmp_path / f"{aid}.json").write_text("{}", encoding="utf-8")

        with patch("main.clean_paper") as mock_clean, \
             patch("main.PROCESSED_DIR", tmp_path), \
             patch("main.CLEANED_DIR", tmp_path / "cleaned"):
            mock_clean.return_value = MagicMock(status="cleaned")
            _clean_stage(["2502.00425", "1904.07272"], force=False)
            assert mock_clean.call_count == 2

    def test_should_skip_missing_processed(self, tmp_path):
        """It should skip papers without processed JSON."""
        # Only create one file — second paper has no processed JSON
        (tmp_path / "2502.00425.json").write_text("{}", encoding="utf-8")

        with patch("main.clean_paper") as mock_clean, \
             patch("main.PROCESSED_DIR", tmp_path), \
             patch("main.CLEANED_DIR", tmp_path / "cleaned"):
            mock_clean.return_value = MagicMock(status="cleaned")
            _clean_stage(["2502.00425", "1904.07272"], force=False)
            assert mock_clean.call_count == 1

    def test_should_propagate_force(self, tmp_path):
        """It should pass force to clean_paper."""
        (tmp_path / "2502.00425.json").write_text("{}", encoding="utf-8")

        with patch("main.clean_paper") as mock_clean, \
             patch("main.PROCESSED_DIR", tmp_path), \
             patch("main.CLEANED_DIR", tmp_path / "cleaned"):
            mock_clean.return_value = MagicMock(status="cleaned")
            _clean_stage(["2502.00425"], force=True)
            _, kwargs = mock_clean.call_args
            assert kwargs["force"] is True

    def test_should_handle_clean_error_gracefully(self, tmp_path):
        """It should log but not raise when clean_paper fails."""
        (tmp_path / "2502.00425.json").write_text("{}", encoding="utf-8")

        with patch("main.clean_paper") as mock_clean, \
             patch("main.PROCESSED_DIR", tmp_path), \
             patch("main.CLEANED_DIR", tmp_path / "cleaned"):
            mock_clean.side_effect = Exception("bad json")
            # Should not raise
            _clean_stage(["2502.00425"], force=False)


class TestFromFlagIntegration:
    """Tests for --from flag controlling which stages run."""

    @pytest.mark.asyncio
    async def test_should_run_all_stages_by_default(self):
        """It should run load, clean, and process when no --from given."""
        with patch("main._load_stage", new_callable=AsyncMock) as mock_load, \
             patch("main._clean_stage") as mock_clean, \
             patch("main._process_stage", new_callable=AsyncMock) as mock_proc:
            mock_proc.return_value = (1, 0, 0)
            from main import _run
            args = argparse.Namespace(
                arxiv_id="2502.00425", csv_path=None,
                from_stage="load", force=False,
                concurrency=10, no_export=True,
            )
            await _run(args)
            mock_load.assert_called_once()
            mock_clean.assert_called_once()
            mock_proc.assert_called_once()

    @pytest.mark.asyncio
    async def test_should_skip_load_when_from_clean(self):
        """It should skip load stage when --from clean."""
        with patch("main._load_stage", new_callable=AsyncMock) as mock_load, \
             patch("main._clean_stage") as mock_clean, \
             patch("main._process_stage", new_callable=AsyncMock) as mock_proc:
            mock_proc.return_value = (1, 0, 0)
            from main import _run
            args = argparse.Namespace(
                arxiv_id="2502.00425", csv_path=None,
                from_stage="clean", force=False,
                concurrency=10, no_export=True,
            )
            await _run(args)
            mock_load.assert_not_called()
            mock_clean.assert_called_once()
            mock_proc.assert_called_once()

    @pytest.mark.asyncio
    async def test_should_skip_load_and_clean_when_from_process(self):
        """It should skip load and clean when --from process."""
        with patch("main._load_stage", new_callable=AsyncMock) as mock_load, \
             patch("main._clean_stage") as mock_clean, \
             patch("main._process_stage", new_callable=AsyncMock) as mock_proc:
            mock_proc.return_value = (1, 0, 0)
            from main import _run
            args = argparse.Namespace(
                arxiv_id="2502.00425", csv_path=None,
                from_stage="process", force=False,
                concurrency=10, no_export=True,
            )
            await _run(args)
            mock_load.assert_not_called()
            mock_clean.assert_not_called()
            mock_proc.assert_called_once()

    @pytest.mark.asyncio
    async def test_should_propagate_force_to_stages(self):
        """It should pass force=True to all active stages."""
        with patch("main._load_stage", new_callable=AsyncMock) as mock_load, \
             patch("main._clean_stage") as mock_clean, \
             patch("main._process_stage", new_callable=AsyncMock) as mock_proc:
            mock_proc.return_value = (1, 0, 0)
            from main import _run
            args = argparse.Namespace(
                arxiv_id="2502.00425", csv_path=None,
                from_stage="load", force=True,
                concurrency=10, no_export=True,
            )
            await _run(args)
            _, load_kwargs = mock_load.call_args
            assert load_kwargs["force"] is True
            _, clean_kwargs = mock_clean.call_args
            assert clean_kwargs["force"] is True
