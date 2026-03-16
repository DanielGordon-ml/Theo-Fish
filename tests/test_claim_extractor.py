"""
@file test_claim_extractor.py
@description Tests for the per-section claim extractor with mocked LLM client.
"""

import json
from unittest.mock import AsyncMock, MagicMock

import pytest

from graph_builder.config.schema_types import (
    ClaimTypeDef,
    ConceptTypeDef,
    EdgeCategories,
    FieldOwnership,
    GraphSchema,
    ValidationConfig,
)
from graph_builder.extraction.claim_extractor import extract_claims_from_section
from graph_builder.llm.llm_client import LLMResponse
from graph_builder.models.claim import ClaimNode
from graph_builder.models.edges import CouplingEdge
from graph_builder.models.section import Section


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_schema() -> GraphSchema:
    """Build a minimal GraphSchema sufficient for claim extractor tests."""
    return GraphSchema(
        version="1.0",
        last_updated="2026-01-01",
        concept_types={
            "structure": ConceptTypeDef(
                description="A named mathematical structure",
                required_fields=["name", "semantic_type"],
            ),
            "quantity": ConceptTypeDef(
                description="A measurable quantity",
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
        edges=EdgeCategories(),
        validation=ValidationConfig(),
        field_ownership=FieldOwnership(),
    )


def _make_section(
    heading: str = "3 Main Results",
    content: str = "Theorem 1.1: The regret is bounded by O(sqrt(T)).",
    index: int = 0,
) -> Section:
    """Build a Section for use in tests."""
    return Section(
        heading=heading,
        level=2,
        content=content,
        char_count=len(content),
        index=index,
    )


def _make_llm_response(claims: list[dict]) -> LLMResponse:
    """Build an LLMResponse whose content is a claims JSON payload."""
    return LLMResponse(
        content=json.dumps({"claims": claims}),
        input_tokens=100,
        output_tokens=50,
        model="deepseek-chat",
    )


def _make_mock_client(claims: list[dict]) -> MagicMock:
    """Return a mock DeepSeekClient that returns the given claims."""
    client = MagicMock()
    client.call = AsyncMock(return_value=_make_llm_response(claims))
    return client


_VALID_CLAIM = {
    "label": "Theorem 1.1",
    "claim_type": "theorem",
    "conclusion": "Regret is O(sqrt(T)).",
    "about_concepts": ["regret", "action-space"],
}

_CONCEPT_LIST = [
    {"name": "regret", "slug": "regret", "type": "quantity"},
    {"name": "action space", "slug": "action-space", "type": "structure"},
    {"name": "MDP", "slug": "mdp", "type": "structure"},
]


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestExtractClaimsFromSection:
    """Tests for extract_claims_from_section()."""

    @pytest.mark.asyncio
    async def test_it_should_extract_claims_and_return_nodes_and_edges(self):
        """It should return (list[ClaimNode], list[CouplingEdge]) from a section."""
        schema = _make_schema()
        section = _make_section()
        client = _make_mock_client([_VALID_CLAIM])

        claims, edges = await extract_claims_from_section(
            section, schema, client, _CONCEPT_LIST, "test-paper",
        )

        assert len(claims) == 1
        assert isinstance(claims[0], ClaimNode)
        assert isinstance(edges, list)

    @pytest.mark.asyncio
    async def test_it_should_inject_section_local_concepts_into_system_prompt(self):
        """It should pass concept_list into the system prompt via build_claim_prompt."""
        schema = _make_schema()
        section = _make_section()
        client = _make_mock_client([_VALID_CLAIM])

        await extract_claims_from_section(
            section, schema, client, _CONCEPT_LIST, "test-paper",
        )

        system_prompt, _ = client.call.call_args[0]
        assert "regret" in system_prompt
        assert "action-space" in system_prompt

    @pytest.mark.asyncio
    async def test_it_should_set_source_paper_slug_on_each_claim(self):
        """It should stamp source_paper_slug on every returned ClaimNode."""
        schema = _make_schema()
        section = _make_section()
        client = _make_mock_client([
            _VALID_CLAIM,
            {
                "label": "Lemma 2.1",
                "claim_type": "lemma",
                "conclusion": "The bound is tight.",
                "about_concepts": ["regret"],
            },
        ])

        claims, _ = await extract_claims_from_section(
            section, schema, client, _CONCEPT_LIST, "my-paper",
        )

        assert all(c.source_paper_slug == "my-paper" for c in claims)

    @pytest.mark.asyncio
    async def test_it_should_generate_about_coupling_edges(self):
        """It should produce one CouplingEdge per entry in about_concepts."""
        schema = _make_schema()
        section = _make_section()
        client = _make_mock_client([_VALID_CLAIM])

        claims, edges = await extract_claims_from_section(
            section, schema, client, _CONCEPT_LIST, "test-paper",
        )

        assert len(edges) == 2
        assert all(isinstance(e, CouplingEdge) for e in edges)
        concept_slugs = {e.concept_slug for e in edges}
        assert concept_slugs == {"regret", "action-space"}
        assert all(e.claim_slug == claims[0].slug for e in edges)

    @pytest.mark.asyncio
    async def test_it_should_return_empty_lists_for_section_with_no_claims(self):
        """It should return ([], []) when the LLM extracts no claims."""
        schema = _make_schema()
        section = _make_section(content="This section is purely introductory.")
        client = _make_mock_client([])

        claims, edges = await extract_claims_from_section(
            section, schema, client, _CONCEPT_LIST, "test-paper",
        )

        assert claims == []
        assert edges == []

    @pytest.mark.asyncio
    async def test_it_should_handle_malformed_llm_response_gracefully(self):
        """It should return ([], []) when the LLM returns invalid JSON."""
        schema = _make_schema()
        section = _make_section()
        client = MagicMock()
        client.call = AsyncMock(return_value=LLMResponse(
            content="not valid json {{{",
            input_tokens=10,
            output_tokens=5,
            model="deepseek-chat",
        ))

        claims, edges = await extract_claims_from_section(
            section, schema, client, _CONCEPT_LIST, "test-paper",
        )

        assert claims == []
        assert edges == []

    @pytest.mark.asyncio
    async def test_it_should_include_section_content_in_user_prompt(self):
        """It should embed the raw section content in the user prompt."""
        schema = _make_schema()
        content = "Theorem 1.1 states that regret is sublinear."
        section = _make_section(content=content)
        client = _make_mock_client([])

        await extract_claims_from_section(
            section, schema, client, _CONCEPT_LIST, "test-paper",
        )

        _, user_prompt = client.call.call_args[0]
        assert content in user_prompt

    @pytest.mark.asyncio
    async def test_it_should_skip_about_concepts_for_claims_with_none(self):
        """It should produce no coupling edges when about_concepts is absent."""
        schema = _make_schema()
        section = _make_section()
        claim_no_about = {
            "label": "Theorem 2.0",
            "claim_type": "theorem",
            "conclusion": "Some bound.",
        }
        client = _make_mock_client([claim_no_about])

        claims, edges = await extract_claims_from_section(
            section, schema, client, _CONCEPT_LIST, "test-paper",
        )

        assert len(claims) == 1
        assert edges == []

    @pytest.mark.asyncio
    async def test_it_should_handle_llm_call_exception_gracefully(self):
        """It should return ([], []) when the LLM call raises an exception."""
        schema = _make_schema()
        section = _make_section()
        client = MagicMock()
        client.call = AsyncMock(side_effect=RuntimeError("LLM unavailable"))

        claims, edges = await extract_claims_from_section(
            section, schema, client, _CONCEPT_LIST, "test-paper",
        )

        assert claims == []
        assert edges == []

    @pytest.mark.asyncio
    async def test_it_should_inject_deferred_proof_into_user_prompt(self):
        """It should append deferred proof text to the section content."""
        schema = _make_schema()
        section = _make_section(
            heading="Main Results",
            content="Theorem III.3. The bound is tight.",
        )
        client = _make_mock_client([_VALID_CLAIM])
        proof_map = {"Theorem III.3": "We proceed by induction."}

        await extract_claims_from_section(
            section, schema, client, _CONCEPT_LIST, "test-paper",
            proof_map=proof_map,
        )

        _, user_prompt = client.call.call_args[0]
        assert "DEFERRED PROOF" in user_prompt
        assert "We proceed by induction" in user_prompt

    @pytest.mark.asyncio
    async def test_it_should_not_inject_when_no_matching_proof(self):
        """It should not modify the prompt when no proof matches."""
        schema = _make_schema()
        section = _make_section(content="Theorem 99. Something else.")
        client = _make_mock_client([])
        proof_map = {"Theorem III.3": "Some proof."}

        await extract_claims_from_section(
            section, schema, client, _CONCEPT_LIST, "test-paper",
            proof_map=proof_map,
        )

        _, user_prompt = client.call.call_args[0]
        assert "DEFERRED PROOF" not in user_prompt
