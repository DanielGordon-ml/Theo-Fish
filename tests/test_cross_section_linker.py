"""
@file test_cross_section_linker.py
@description Tests for the cross-section gap-fill linker (Pass 3b) with mocked LLM.
"""

import json
from unittest.mock import AsyncMock, MagicMock

import pytest

from graph_builder.config.schema_types import (
    ClaimTypeDef,
    ConceptTypeDef,
    EdgeCategories,
    EdgeDef,
    FieldOwnership,
    GraphSchema,
    ValidationConfig,
)
from graph_builder.extraction.cross_section_linker import find_cross_section_edges
from graph_builder.llm.llm_client import LLMResponse
from graph_builder.models.claim import ClaimNode
from graph_builder.models.concept import ConceptNode
from graph_builder.models.edges import ClaimEdge


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _make_schema() -> GraphSchema:
    """Build a minimal GraphSchema with claim edge types for gap-fill."""
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
            "lemma": ClaimTypeDef(
                description="A supporting lemma",
                required_fields=["label", "claim_type", "conclusion"],
            ),
        },
        edges=EdgeCategories(
            claim_edges={
                "depends_on": EdgeDef(
                    description="Claim A depends on Claim B",
                    attributes=["condition"],
                ),
                "enables": EdgeDef(
                    description="Claim A enables Claim B",
                    attributes=["role"],
                ),
            },
        ),
        validation=ValidationConfig(),
        field_ownership=FieldOwnership(),
    )


def _make_claim(
    label: str = "Theorem 1.1",
    claim_type: str = "theorem",
    conclusion: str = "Regret is O(sqrt(T)).",
    section: str = "3 Main Results",
    paper_slug: str = "test-paper",
) -> ClaimNode:
    """Build a minimal ClaimNode for tests."""
    return ClaimNode(
        source_paper_slug=paper_slug,
        label=label,
        claim_type=claim_type,
        conclusion=conclusion,
        section=section,
    )


def _make_concept(
    name: str = "regret",
    semantic_type: str = "structure",
    formal_spec: str = "R_T",
) -> ConceptNode:
    """Build a minimal ConceptNode for tests."""
    return ConceptNode(name=name, semantic_type=semantic_type, formal_spec=formal_spec)


def _make_llm_response(edges: list[dict]) -> LLMResponse:
    """Build an LLMResponse with an edge list payload."""
    return LLMResponse(
        content=json.dumps({"edges": edges}),
        input_tokens=100,
        output_tokens=50,
        model="deepseek-chat",
    )


def _make_mock_client(edges: list[dict] | None = None) -> MagicMock:
    """Return a mock DeepSeekClient that returns the given edges."""
    client = MagicMock()
    client.call = AsyncMock(return_value=_make_llm_response(edges or []))
    return client


_CLAIM_A = _make_claim("Theorem 1.1", section="2 Preliminaries")
_CLAIM_B = _make_claim(
    "Lemma 3.1", "lemma", "Bound is tight.", section="3 Main Results"
)

_NEW_CROSS_EDGE = {
    "source_slug": _CLAIM_B.slug,
    "target_slug": _CLAIM_A.slug,
    "edge_type": "depends_on",
    "attributes": {},
}

_EXISTING_EDGE = ClaimEdge(
    source_slug=_CLAIM_B.slug,
    target_slug=_CLAIM_A.slug,
    edge_type="depends_on",
)


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


class TestFindCrossSectionEdges:
    """Tests for find_cross_section_edges()."""

    @pytest.mark.asyncio
    async def test_it_should_find_cross_section_implicit_dependencies(self):
        """It should return new ClaimEdge objects for cross-section links."""
        schema = _make_schema()
        claims = [_CLAIM_A, _CLAIM_B]
        concepts = [_make_concept()]
        client = _make_mock_client(edges=[_NEW_CROSS_EDGE])

        result = await find_cross_section_edges(claims, concepts, [], schema, client)

        assert len(result) == 1
        assert isinstance(result[0], ClaimEdge)
        assert result[0].source_slug == _CLAIM_B.slug
        assert result[0].target_slug == _CLAIM_A.slug

    @pytest.mark.asyncio
    async def test_it_should_not_duplicate_edges_already_found_by_enricher(self):
        """It should filter out edges already present in existing_edges."""
        schema = _make_schema()
        claims = [_CLAIM_A, _CLAIM_B]
        concepts = [_make_concept()]
        existing = [_EXISTING_EDGE]
        client = _make_mock_client(edges=[_NEW_CROSS_EDGE])

        result = await find_cross_section_edges(
            claims, concepts, existing, schema, client
        )

        assert result == []

    @pytest.mark.asyncio
    async def test_it_should_use_conclusions_and_formal_specs_not_full_text(self):
        """It should send only conclusions + formal_specs, not full claim text."""
        schema = _make_schema()
        claim = ClaimNode(
            source_paper_slug="test-paper",
            label="Theorem 1.1",
            claim_type="theorem",
            conclusion="Tight bound.",
            statement="Long statement text.",
            section="2 Preliminaries",
        )
        concept = _make_concept(formal_spec="R_T = sum_t r_t", name="regret")
        client = _make_mock_client()

        await find_cross_section_edges([claim], [concept], [], schema, client)

        _, user_prompt = client.call.call_args[0]
        assert "Tight bound." in user_prompt
        assert "R_T = sum_t r_t" in user_prompt
        assert "Long statement text." not in user_prompt

    @pytest.mark.asyncio
    async def test_it_should_handle_llm_failure_gracefully(self):
        """It should return [] when the LLM call raises an exception."""
        schema = _make_schema()
        claims = [_CLAIM_A, _CLAIM_B]
        concepts = [_make_concept()]
        client = MagicMock()
        client.call = AsyncMock(side_effect=RuntimeError("LLM unavailable"))

        result = await find_cross_section_edges(claims, concepts, [], schema, client)

        assert result == []

    @pytest.mark.asyncio
    async def test_it_should_handle_invalid_json_response_gracefully(self):
        """It should return [] when the LLM returns invalid JSON."""
        schema = _make_schema()
        claims = [_CLAIM_A, _CLAIM_B]
        client = MagicMock()
        client.call = AsyncMock(
            return_value=LLMResponse(
                content="not valid json {{{",
                input_tokens=10,
                output_tokens=5,
                model="deepseek-chat",
            )
        )

        result = await find_cross_section_edges(claims, [], [], schema, client)

        assert result == []

    @pytest.mark.asyncio
    async def test_it_should_include_claim_slugs_in_user_prompt(self):
        """It should include claim slugs in the user prompt for grounding."""
        schema = _make_schema()
        claim = _make_claim()
        client = _make_mock_client()

        await find_cross_section_edges([claim], [], [], schema, client)

        _, user_prompt = client.call.call_args[0]
        assert claim.slug in user_prompt

    @pytest.mark.asyncio
    async def test_it_should_deduplicate_multiple_new_edges_against_existing(self):
        """It should filter only the duplicates, keeping truly new edges."""
        schema = _make_schema()
        claim_c = _make_claim("Corollary 4.1", section="4 Extensions")
        new_edge_1 = {
            "source_slug": _CLAIM_B.slug,
            "target_slug": _CLAIM_A.slug,
            "edge_type": "depends_on",
            "attributes": {},
        }
        new_edge_2 = {
            "source_slug": claim_c.slug,
            "target_slug": _CLAIM_A.slug,
            "edge_type": "enables",
            "attributes": {},
        }
        existing = [_EXISTING_EDGE]
        client = _make_mock_client(edges=[new_edge_1, new_edge_2])

        result = await find_cross_section_edges(
            [_CLAIM_A, _CLAIM_B, claim_c], [], existing, schema, client
        )

        assert len(result) == 1
        assert result[0].source_slug == claim_c.slug
        assert result[0].edge_type == "enables"
