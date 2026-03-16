"""
@file test_edge_enricher.py
@description Tests for section-batched edge enricher (Pass 3a) with mocked LLM.
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
from graph_builder.extraction.edge_enricher import enrich_section_edges
from graph_builder.llm.llm_client import LLMResponse
from graph_builder.models.claim import ClaimNode
from graph_builder.models.concept import ConceptNode
from graph_builder.models.edges import ClaimEdge, CouplingEdge


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_schema() -> GraphSchema:
    """Build a minimal GraphSchema with claim and coupling edge types."""
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
                    description="Claim A logically depends on Claim B",
                    attributes=["condition", "technique"],
                ),
                "enables": EdgeDef(
                    description="Claim A enables Claim B",
                    attributes=["role"],
                ),
            },
            coupling_edges={
                "ABOUT": EdgeDef(
                    description="Claim is about a concept",
                    attributes=["role", "aspect"],
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
) -> ConceptNode:
    """Build a minimal ConceptNode for tests."""
    return ConceptNode(name=name, semantic_type=semantic_type, formal_spec="R_T")


def _make_llm_response(claim_edges: list[dict], coupling_edges: list[dict]) -> LLMResponse:
    """Build an LLMResponse with claim and coupling edge payloads."""
    return LLMResponse(
        content=json.dumps({
            "claim_edges": claim_edges,
            "coupling_edges": coupling_edges,
        }),
        input_tokens=100,
        output_tokens=50,
        model="deepseek-chat",
    )


def _make_mock_client(
    claim_edges: list[dict] | None = None,
    coupling_edges: list[dict] | None = None,
) -> MagicMock:
    """Return a mock DeepSeekClient that returns the given edges."""
    client = MagicMock()
    client.call = AsyncMock(
        return_value=_make_llm_response(
            claim_edges or [],
            coupling_edges or [],
        )
    )
    return client


_VALID_CLAIM_EDGE = {
    "source_slug": "test-paper--theorem-1-1",
    "target_slug": "test-paper--lemma-2-1",
    "edge_type": "depends_on",
    "attributes": {"condition": "compactness", "technique": "induction"},
}

_VALID_COUPLING_EDGE = {
    "claim_slug": "test-paper--theorem-1-1",
    "concept_slug": "regret",
    "role": "primary",
    "aspect": "upper-bound",
}


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestEnrichSectionEdges:
    """Tests for enrich_section_edges()."""

    @pytest.mark.asyncio
    async def test_it_should_enrich_edges_for_all_claims_in_one_llm_call(self):
        """It should batch all section claims into a single LLM call."""
        schema = _make_schema()
        claims = [_make_claim("Theorem 1.1"), _make_claim("Lemma 2.1", "lemma")]
        concepts = [_make_concept("regret")]
        section_text = "Theorem 1.1: Regret is bounded. Lemma 2.1 supports it."
        client = _make_mock_client(claim_edges=[_VALID_CLAIM_EDGE])

        await enrich_section_edges(
            claims, section_text, concepts, claims, schema, client
        )

        assert client.call.call_count == 1

    @pytest.mark.asyncio
    async def test_it_should_return_claim_edge_and_coupling_edge_lists(self):
        """It should return (list[ClaimEdge], list[CouplingEdge]) on success."""
        schema = _make_schema()
        claims = [_make_claim()]
        concepts = [_make_concept()]
        section_text = "Theorem 1.1: Regret is O(sqrt(T))."
        client = _make_mock_client(
            claim_edges=[_VALID_CLAIM_EDGE],
            coupling_edges=[_VALID_COUPLING_EDGE],
        )

        claim_edges, coupling_edges = await enrich_section_edges(
            claims, section_text, concepts, claims, schema, client
        )

        assert len(claim_edges) == 1
        assert isinstance(claim_edges[0], ClaimEdge)
        assert len(coupling_edges) == 1
        assert isinstance(coupling_edges[0], CouplingEdge)

    @pytest.mark.asyncio
    async def test_it_should_populate_conditional_attributes(self):
        """It should preserve role, condition, and technique in edge attributes."""
        schema = _make_schema()
        claims = [_make_claim()]
        concepts = [_make_concept()]
        section_text = "Theorem 1.1 depends on Lemma 2.1 under compactness."
        client = _make_mock_client(claim_edges=[_VALID_CLAIM_EDGE])

        claim_edges, _ = await enrich_section_edges(
            claims, section_text, concepts, claims, schema, client
        )

        attrs = claim_edges[0].attributes
        assert attrs.get("condition") == "compactness"
        assert attrs.get("technique") == "induction"

    @pytest.mark.asyncio
    async def test_it_should_return_empty_lists_for_section_with_no_claims(self):
        """It should return ([], []) when given an empty claims list."""
        schema = _make_schema()
        concepts = [_make_concept()]
        client = MagicMock()
        client.call = AsyncMock()

        claim_edges, coupling_edges = await enrich_section_edges(
            [], "No claims here.", concepts, [], schema, client
        )

        assert claim_edges == []
        assert coupling_edges == []
        client.call.assert_not_called()

    @pytest.mark.asyncio
    async def test_it_should_handle_llm_failure_gracefully(self):
        """It should return ([], []) when the LLM call raises an exception."""
        schema = _make_schema()
        claims = [_make_claim()]
        concepts = [_make_concept()]
        client = MagicMock()
        client.call = AsyncMock(side_effect=RuntimeError("LLM unavailable"))

        claim_edges, coupling_edges = await enrich_section_edges(
            claims, "Theorem 1.1.", concepts, claims, schema, client
        )

        assert claim_edges == []
        assert coupling_edges == []

    @pytest.mark.asyncio
    async def test_it_should_include_claim_statements_in_user_prompt(self):
        """It should embed claim statements and conclusions in the user prompt."""
        schema = _make_schema()
        claim = _make_claim(conclusion="Regret is O(sqrt(T)).")
        client = _make_mock_client()

        await enrich_section_edges(
            [claim], "Section text.", [], [claim], schema, client
        )

        _, user_prompt = client.call.call_args[0]
        assert "Regret is O(sqrt(T))." in user_prompt

    @pytest.mark.asyncio
    async def test_it_should_include_concept_reference_in_user_prompt(self):
        """It should include concept slugs and names in the user prompt."""
        schema = _make_schema()
        claims = [_make_claim()]
        concept = _make_concept("regret")
        client = _make_mock_client()

        await enrich_section_edges(
            claims, "Section.", [concept], claims, schema, client
        )

        _, user_prompt = client.call.call_args[0]
        assert "regret" in user_prompt

    @pytest.mark.asyncio
    async def test_it_should_handle_invalid_json_response_gracefully(self):
        """It should return ([], []) when the LLM returns invalid JSON."""
        schema = _make_schema()
        claims = [_make_claim()]
        client = MagicMock()
        client.call = AsyncMock(return_value=LLMResponse(
            content="not valid json {{{",
            input_tokens=10,
            output_tokens=5,
            model="deepseek-chat",
        ))

        claim_edges, coupling_edges = await enrich_section_edges(
            claims, "Section.", [], claims, schema, client
        )

        assert claim_edges == []
        assert coupling_edges == []
