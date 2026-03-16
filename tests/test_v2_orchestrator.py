"""
@file test_v2_orchestrator.py
@description Tests for the single-paper orchestrator pipeline with mocked
LLM, Neo4j, and embedding clients. Verifies pass ordering, skip logic,
partial failure handling, abort threshold, and BuildResult correctness.
"""

from contextlib import contextmanager
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from graph_builder.config.schema_types import (
    ClaimTypeDef,
    ConceptTypeDef,
    EdgeCategories,
    FieldOwnership,
    GraphSchema,
    ValidationConfig,
)
from graph_builder.extraction.concept_merger import MergedConcept
from graph_builder.extraction.dedup.dedup_cascade import DedupResult
from graph_builder.models.claim import ClaimNode
from graph_builder.models.concept import ConceptNode
from graph_builder.models.edges import ClaimEdge, CouplingEdge
from graph_builder.models.provenance import ProvenanceNode
from graph_builder.models.section import Section
from graph_builder.orchestrator.orchestrator import PipelineOptions, process_paper

_MODULE = "graph_builder.orchestrator.orchestrator"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_schema() -> GraphSchema:
    """Build a minimal GraphSchema for orchestrator tests."""
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


def _make_section(heading: str, index: int) -> Section:
    """Build a Section with enough content to avoid stub detection."""
    content = f"Section {heading} with enough content to pass the minimum character check for sections."
    return Section(
        heading=heading, level=2, content=content,
        char_count=len(content), index=index,
    )


def _make_concept(name: str) -> ConceptNode:
    """Build a ConceptNode with the given name."""
    return ConceptNode(name=name, semantic_type="structure")


def _make_claim(label: str, paper_slug: str) -> ClaimNode:
    """Build a ClaimNode with the given label."""
    return ClaimNode(
        label=label, source_paper_slug=paper_slug,
        claim_type="theorem", conclusion=f"{label} conclusion",
        section="section-1",
    )


def _make_merged(name: str, arxiv_id: str) -> MergedConcept:
    """Build a MergedConcept with a new-concept DedupResult."""
    concept = _make_concept(name)
    return MergedConcept(
        concept=concept,
        dedup_result=DedupResult(
            slug=concept.slug, is_new=True,
            match_method="new", match_confidence=0.0,
        ),
        provenance=ProvenanceNode(
            concept_slug=concept.slug, source_arxiv_id=arxiv_id,
            formulation="test definition", formal_spec="test spec",
        ),
    )


def _make_options(**kwargs) -> PipelineOptions:
    """Build PipelineOptions, forwarding keyword overrides."""
    defaults = {"schema": _make_schema(), "concurrency": 2}
    defaults.update(kwargs)
    return PipelineOptions(**defaults)


def _mock_neo4j() -> MagicMock:
    """Build a mock Neo4jClient."""
    return MagicMock()


def _mock_embedding() -> MagicMock:
    """Build a mock EmbeddingClient."""
    client = MagicMock()
    client.embed_single = AsyncMock(return_value=[0.1] * 10)
    client.embed_batch = AsyncMock(return_value=[[0.1] * 10])
    return client


def _valid_result() -> MagicMock:
    """Build a MagicMock ValidationResult with is_valid=True."""
    return MagicMock(is_valid=True, errors=[], warnings=[])


@contextmanager
def _patch_pipeline(overrides: dict | None = None):
    """Patch all pipeline helpers with sensible defaults.

    Yields a dict of mock objects keyed by short names:
    load, check, p1, merge, p2, p3a, p3b, validate, write.

    Pass overrides to change specific return_values. Keys match the
    short names; values are the desired return_value.
    """
    overrides = overrides or {}

    defaults = {
        "load": ("Test Paper", [_make_section("Intro", 0)]),
        "check": False,
        "p1": [[_make_concept("X")]],
        "merge": [_make_merged("X", "2401.00001")],
        "p2": ([_make_claim("Thm1", "test-paper")], []),
        "p3a": ([], []),
        "p3b": [],
        "validate": _valid_result(),
        "write": {"concepts": 1, "claims": 1, "edges": 0},
    }
    defaults.update(overrides)

    targets = {
        "load": f"{_MODULE}.load_paper",
        "check": f"{_MODULE}.check_already_built",
        "p1": f"{_MODULE}._run_pass1",
        "merge": f"{_MODULE}._run_merge",
        "p2": f"{_MODULE}._run_pass2",
        "p3a": f"{_MODULE}._run_pass3a",
        "p3b": f"{_MODULE}._run_pass3b",
        "validate": f"{_MODULE}.validate_paper",
        "write": f"{_MODULE}.write_to_neo4j",
    }

    # validate_paper is sync; the rest are async
    async_keys = {"load", "check", "p1", "merge", "p2", "p3a", "p3b", "write"}

    patches = {}
    active = []
    for key, target in targets.items():
        kwargs = {}
        if key in async_keys:
            kwargs["new_callable"] = AsyncMock
        p = patch(target, **kwargs)
        mock_obj = p.start()
        if key in async_keys:
            mock_obj.return_value = defaults[key]
        else:
            mock_obj.return_value = defaults[key]
        patches[key] = mock_obj
        active.append(p)

    try:
        yield patches
    finally:
        for p in active:
            p.stop()


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestProcessPaperPassOrder:
    """Tests that passes execute in the correct order."""

    @pytest.mark.asyncio
    async def test_it_should_execute_passes_in_correct_order(self):
        """It should run P1, merge, P2, P3a, P3b, validate, write in order."""
        call_order: list[str] = []
        arxiv_id = "2401.00001"
        llm = MagicMock()
        llm.call = AsyncMock()

        concepts = [_make_concept("Hilbert Space")]
        merged = [_make_merged("Hilbert Space", arxiv_id)]
        claim = _make_claim("Theorem 1", "test-paper")
        coupling = CouplingEdge(
            claim_slug=claim.slug, concept_slug=concepts[0].slug,
        )
        write_counts = {"concepts": 1, "claims": 1, "edges": 1}

        with _patch_pipeline({
            "p1": [concepts],
            "merge": merged,
            "p2": ([claim], [coupling]),
            "write": write_counts,
        }) as mocks:
            mocks["p1"].side_effect = lambda *a, **kw: (
                call_order.append("pass1") or [concepts]
            )
            mocks["merge"].side_effect = lambda *a, **kw: (
                call_order.append("merge") or merged
            )
            mocks["p2"].side_effect = lambda *a, **kw: (
                call_order.append("pass2") or ([claim], [coupling])
            )
            mocks["p3a"].side_effect = lambda *a, **kw: (
                call_order.append("pass3a") or ([], [])
            )
            mocks["p3b"].side_effect = lambda *a, **kw: (
                call_order.append("pass3b") or []
            )
            mocks["validate"].side_effect = lambda *a, **kw: (
                call_order.append("validate") or _valid_result()
            )
            mocks["write"].side_effect = lambda *a, **kw: (
                call_order.append("write") or write_counts
            )

            result = await process_paper(
                arxiv_id, _make_options(), llm, _mock_neo4j(), _mock_embedding(),
            )

        expected = ["pass1", "merge", "pass2", "pass3a", "pass3b", "validate", "write"]
        assert call_order == expected
        assert result.status == "built"


class TestProcessPaperSkip:
    """Tests for skip-already-built logic."""

    @pytest.mark.asyncio
    async def test_it_should_skip_already_built_papers(self):
        """It should return 'skipped' if paper is already built and force=False."""
        arxiv_id = "2401.00001"

        with _patch_pipeline({"check": True}) as mocks:
            result = await process_paper(
                arxiv_id, _make_options(), MagicMock(), _mock_neo4j(),
            )

        assert result.status == "skipped"
        assert result.arxiv_id == arxiv_id

    @pytest.mark.asyncio
    async def test_it_should_not_skip_when_force_is_true(self):
        """It should process even if paper exists when force=True."""
        arxiv_id = "2401.00001"
        options = _make_options(force=True)
        llm = MagicMock()
        llm.call = AsyncMock()

        with _patch_pipeline({"check": True}):
            result = await process_paper(
                arxiv_id, options, llm, _mock_neo4j(), _mock_embedding(),
            )

        assert result.status == "built"


class TestProcessPaperPartialFailure:
    """Tests for partial LLM failure handling."""

    @pytest.mark.asyncio
    async def test_it_should_handle_partial_llm_failures(self):
        """It should skip failed sections and continue with successful ones."""
        arxiv_id = "2401.00001"
        llm = MagicMock()
        llm.call = AsyncMock()

        # 3 sections: first and third succeed, second fails (empty)
        section_concepts = [
            [_make_concept("Space A")],
            [],
            [_make_concept("Space C")],
        ]
        merged = [
            _make_merged("Space A", arxiv_id),
            _make_merged("Space C", arxiv_id),
        ]
        sections = [_make_section(f"Sec {i}", i) for i in range(3)]

        with _patch_pipeline({
            "load": ("Test Paper", sections),
            "p1": section_concepts,
            "merge": merged,
            "write": {"concepts": 2, "claims": 1, "edges": 1},
        }):
            result = await process_paper(
                arxiv_id, _make_options(), llm, _mock_neo4j(), _mock_embedding(),
            )

        assert result.status == "built"
        assert result.concept_count == 2


class TestProcessPaperAbortThreshold:
    """Tests for >50% failure abort logic."""

    @pytest.mark.asyncio
    async def test_it_should_abort_when_majority_sections_fail(self):
        """It should abort paper when >50% of section extractions fail."""
        arxiv_id = "2401.00001"
        sections = [_make_section(f"Sec {i}", i) for i in range(4)]
        # 4 sections: 3 fail (empty), 1 succeeds -> 75% failure
        section_concepts = [[], [], [], [_make_concept("X")]]

        with _patch_pipeline({
            "load": ("Test Paper", sections),
            "p1": section_concepts,
        }):
            result = await process_paper(
                arxiv_id, _make_options(), MagicMock(), _mock_neo4j(), _mock_embedding(),
            )

        assert result.status == "failed"
        assert "abort" in result.error.lower()


class TestProcessPaperValidationPartialWrite:
    """Tests for partial writes on validation errors."""

    @pytest.mark.asyncio
    async def test_it_should_write_valid_concepts_when_claims_fail_validation(self):
        """It should write valid data even when some claims fail validation."""
        arxiv_id = "2401.00001"
        llm = MagicMock()
        llm.call = AsyncMock()

        invalid_validation = MagicMock(
            is_valid=False,
            errors=["missing_about: claim 'x' has no ABOUT edge"],
            warnings=[],
        )

        with _patch_pipeline({
            "validate": invalid_validation,
            "write": {"concepts": 1, "claims": 0, "edges": 0},
        }) as mocks:
            result = await process_paper(
                arxiv_id, _make_options(), llm, _mock_neo4j(), _mock_embedding(),
            )

        assert result.status == "built"
        assert result.concept_count == 1
        mocks["write"].assert_called_once()


class TestProcessPaperBuildResult:
    """Tests that BuildResult is returned with correct counts."""

    @pytest.mark.asyncio
    async def test_it_should_return_build_result_with_correct_counts(self):
        """It should populate concept_count, claim_count, edge_count correctly."""
        arxiv_id = "2401.00001"
        llm = MagicMock()
        llm.call = AsyncMock()

        concepts = [_make_concept("Hilbert Space"), _make_concept("Operator")]
        merged = [_make_merged("Hilbert Space", arxiv_id), _make_merged("Operator", arxiv_id)]
        claims = [
            _make_claim("Theorem 1", "test-paper"),
            _make_claim("Lemma 2", "test-paper"),
            _make_claim("Corollary 3", "test-paper"),
        ]
        coupling = CouplingEdge(
            claim_slug=claims[0].slug, concept_slug=concepts[0].slug,
        )

        with _patch_pipeline({
            "p1": [concepts],
            "merge": merged,
            "p2": (claims, [coupling]),
            "p3a": ([ClaimEdge(source_slug="s1", target_slug="s2", edge_type="depends_on")], []),
            "p3b": [ClaimEdge(source_slug="s3", target_slug="s4", edge_type="enables")],
            "write": {"concepts": 2, "claims": 3, "edges": 4},
        }):
            result = await process_paper(
                arxiv_id, _make_options(), llm, _mock_neo4j(), _mock_embedding(),
            )

        assert result.arxiv_id == arxiv_id
        assert result.status == "built"
        assert result.concept_count == 2
        assert result.claim_count == 3
        assert result.edge_count == 4

    @pytest.mark.asyncio
    async def test_it_should_return_failed_result_on_load_error(self):
        """It should return status='failed' when paper loading fails."""
        arxiv_id = "9999.99999"

        with _patch_pipeline() as mocks:
            mocks["load"].side_effect = FileNotFoundError("No cleaned JSON found")
            result = await process_paper(
                arxiv_id, _make_options(), MagicMock(), _mock_neo4j(),
            )

        assert result.status == "failed"
        assert result.arxiv_id == arxiv_id
        assert result.error is not None
