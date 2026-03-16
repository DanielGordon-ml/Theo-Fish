"""
@file test_batch_processor.py
@description Tests for the batch processor that discovers and processes
multiple papers from an input directory in parallel. All calls to
process_paper are mocked so no real LLM or Neo4j I/O occurs.
"""

import asyncio
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from graph_builder.models.results import BatchBuildResult, BuildResult
from graph_builder.orchestrator.orchestrator import PipelineOptions
from graph_builder.config.schema_types import (
    ClaimTypeDef,
    ConceptTypeDef,
    EdgeCategories,
    FieldOwnership,
    GraphSchema,
    ValidationConfig,
)

_MODULE = "graph_builder.orchestrator.batch_processor"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_schema() -> GraphSchema:
    """Build a minimal GraphSchema for batch processor tests."""
    return GraphSchema(
        version="1.0",
        last_updated="2026-01-01",
        concept_types={
            "structure": ConceptTypeDef(
                description="A named mathematical structure",
                required_fields=["name", "semantic_type"],
            ),
        },
        claim_types={
            "theorem": ClaimTypeDef(
                description="A proven theorem",
                required_fields=["label", "claim_type", "conclusion"],
            ),
        },
        edges=EdgeCategories(),
        validation=ValidationConfig(),
        field_ownership=FieldOwnership(),
    )


def _make_options(**kwargs) -> PipelineOptions:
    """Build PipelineOptions with defaults, accepting overrides."""
    defaults = {"schema": _make_schema(), "concurrency": 2}
    defaults.update(kwargs)
    return PipelineOptions(**defaults)


def _make_build_result(arxiv_id: str, status: str = "built") -> BuildResult:
    """Build a BuildResult for a given arxiv_id and status."""
    return BuildResult(arxiv_id=arxiv_id, status=status)


def _write_json_files(directory: Path, arxiv_ids: list[str]) -> None:
    """Write empty .json stub files for each arxiv_id."""
    for arxiv_id in arxiv_ids:
        (directory / f"{arxiv_id}.json").write_text("{}", encoding="utf-8")


def _mock_clients() -> tuple[MagicMock, MagicMock, MagicMock]:
    """Return (llm_client, neo4j_client, embedding_client) mocks."""
    return MagicMock(), MagicMock(), MagicMock()


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestPaperDiscovery:
    """Tests for *.json file discovery in the input directory."""

    @pytest.mark.asyncio
    async def test_it_should_discover_papers_from_input_directory(
        self, tmp_path: Path,
    ):
        """It should find all *.json files in input_dir and process them."""
        from graph_builder.orchestrator.batch_processor import process_batch

        arxiv_ids = ["2401.00001", "2401.00002", "2401.00003"]
        _write_json_files(tmp_path, arxiv_ids)
        llm, neo4j, emb = _mock_clients()

        side_effects = [_make_build_result(aid) for aid in arxiv_ids]
        with patch(f"{_MODULE}.process_paper", new=AsyncMock(side_effect=side_effects)):
            result = await process_batch(tmp_path, _make_options(), llm, neo4j, emb)

        assert result.total == 3
        discovered_ids = {r.arxiv_id for r in result.results}
        assert discovered_ids == set(arxiv_ids)

    @pytest.mark.asyncio
    async def test_it_should_handle_empty_input_directory(
        self, tmp_path: Path,
    ):
        """It should return a BatchBuildResult with all zeros for an empty dir."""
        from graph_builder.orchestrator.batch_processor import process_batch

        llm, neo4j, emb = _mock_clients()
        with patch(f"{_MODULE}.process_paper", new=AsyncMock()):
            result = await process_batch(tmp_path, _make_options(), llm, neo4j, emb)

        assert isinstance(result, BatchBuildResult)
        assert result.total == 0
        assert result.built == 0
        assert result.skipped == 0
        assert result.failed == 0
        assert result.results == []


class TestParallelProcessing:
    """Tests for semaphore-gated parallel execution."""

    @pytest.mark.asyncio
    async def test_it_should_process_papers_in_parallel_with_semaphore(
        self, tmp_path: Path,
    ):
        """It should respect concurrency limit via asyncio.Semaphore."""
        from graph_builder.orchestrator.batch_processor import process_batch

        arxiv_ids = ["2401.00001", "2401.00002"]
        _write_json_files(tmp_path, arxiv_ids)
        llm, neo4j, emb = _mock_clients()

        active_count = 0
        max_active = 0

        async def _fake_process_paper(arxiv_id, options, llm_c, neo4j_c, emb_c=None):
            nonlocal active_count, max_active
            active_count += 1
            max_active = max(max_active, active_count)
            await asyncio.sleep(0)
            active_count -= 1
            return _make_build_result(arxiv_id)

        with patch(f"{_MODULE}.process_paper", side_effect=_fake_process_paper):
            result = await process_batch(
                tmp_path, _make_options(concurrency=1), llm, neo4j, emb,
            )

        assert max_active <= 1
        assert result.total == 2

    @pytest.mark.asyncio
    async def test_it_should_continue_when_one_paper_fails(
        self, tmp_path: Path,
    ):
        """It should process remaining papers even if one raises an exception."""
        from graph_builder.orchestrator.batch_processor import process_batch

        _write_json_files(tmp_path, ["2401.00001", "2401.00002", "2401.00003"])
        llm, neo4j, emb = _mock_clients()

        async def _fake_process_paper(arxiv_id, options, llm_c, neo4j_c, emb_c=None):
            if arxiv_id == "2401.00002":
                raise RuntimeError("LLM exploded")
            return _make_build_result(arxiv_id)

        with patch(f"{_MODULE}.process_paper", side_effect=_fake_process_paper):
            result = await process_batch(tmp_path, _make_options(), llm, neo4j, emb)

        assert result.total == 3
        assert result.failed == 1
        statuses = {r.arxiv_id: r.status for r in result.results}
        assert statuses["2401.00001"] == "built"
        assert statuses["2401.00002"] == "failed"
        assert statuses["2401.00003"] == "built"


class TestBatchBuildResult:
    """Tests that BatchBuildResult tallies are computed correctly."""

    @pytest.mark.asyncio
    async def test_it_should_return_batch_build_result_with_correct_totals(
        self, tmp_path: Path,
    ):
        """It should aggregate built/skipped/failed counts from all results."""
        from graph_builder.orchestrator.batch_processor import process_batch

        _write_json_files(tmp_path, ["2401.00001", "2401.00002", "2401.00003"])
        llm, neo4j, emb = _mock_clients()

        fake_results = [
            _make_build_result("2401.00001", "built"),
            _make_build_result("2401.00002", "skipped"),
            _make_build_result("2401.00003", "failed"),
        ]
        with patch(
            f"{_MODULE}.process_paper",
            new=AsyncMock(side_effect=fake_results),
        ):
            result = await process_batch(tmp_path, _make_options(), llm, neo4j, emb)

        assert isinstance(result, BatchBuildResult)
        assert result.total == 3
        assert result.built == 1
        assert result.skipped == 1
        assert result.failed == 1
        assert len(result.results) == 3
