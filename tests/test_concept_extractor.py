"""
@file test_concept_extractor.py
@description Tests for the per-section concept extractor with mocked LLM client.
"""

import json
from unittest.mock import AsyncMock, MagicMock

import pytest

from graph_builder.config.schema_types import (
    ConceptTypeDef,
    ClaimTypeDef,
    EdgeCategories,
    FieldOwnership,
    GraphSchema,
    ValidationConfig,
)
from graph_builder.extraction.concept_extractor import extract_concepts_from_section
from graph_builder.llm.llm_client import LLMResponse
from graph_builder.models.concept import ConceptNode
from graph_builder.models.section import Section


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_schema() -> GraphSchema:
    """Build a minimal GraphSchema sufficient for concept extractor tests."""
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
        },
        edges=EdgeCategories(),
        validation=ValidationConfig(),
        field_ownership=FieldOwnership(),
    )


def _make_section(
    heading: str = "2 Preliminaries",
    content: str = "Let M be a Markov Decision Process.",
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


def _make_llm_response(concepts: list[dict]) -> LLMResponse:
    """Build an LLMResponse whose content is a concepts JSON payload."""
    return LLMResponse(
        content=json.dumps({"concepts": concepts}),
        input_tokens=100,
        output_tokens=50,
        model="deepseek-chat",
    )


def _make_mock_client(concepts: list[dict]) -> MagicMock:
    """Return a mock DeepSeekClient that returns the given concepts."""
    client = MagicMock()
    client.call = AsyncMock(return_value=_make_llm_response(concepts))
    return client


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestExtractConceptsFromSection:
    """Tests for extract_concepts_from_section()."""

    @pytest.mark.asyncio
    async def test_it_should_extract_concepts_and_return_concept_node_list(self):
        """It should call the LLM and return a list of ConceptNode objects."""
        schema = _make_schema()
        section = _make_section()
        client = _make_mock_client([
            {"name": "Markov Decision Process", "semantic_type": "structure"},
            {"name": "regret", "semantic_type": "quantity"},
        ])

        result = await extract_concepts_from_section(section, schema, client)

        assert len(result) == 2
        assert all(isinstance(c, ConceptNode) for c in result)
        assert result[0].name == "Markov Decision Process"
        assert result[1].name == "regret"

    @pytest.mark.asyncio
    async def test_it_should_return_empty_list_for_section_with_no_concepts(self):
        """It should return an empty list when the LLM finds no concepts."""
        schema = _make_schema()
        section = _make_section(content="This section has no mathematical content.")
        client = _make_mock_client([])

        result = await extract_concepts_from_section(section, schema, client)

        assert result == []

    @pytest.mark.asyncio
    async def test_it_should_inject_existing_concepts_into_user_prompt(self):
        """It should include existing concept shortlist in the user prompt."""
        schema = _make_schema()
        section = _make_section()
        existing_concepts = [
            {"slug": "markov-decision-process", "semantic_type": "structure"},
            {"slug": "regret", "semantic_type": "quantity"},
        ]
        client = _make_mock_client([
            {"name": "policy", "semantic_type": "structure"},
        ])

        await extract_concepts_from_section(
            section, schema, client, existing_concepts=existing_concepts,
        )

        _, user_prompt = client.call.call_args[0]
        assert "markov-decision-process" in user_prompt
        assert "regret" in user_prompt

    @pytest.mark.asyncio
    async def test_it_should_handle_llm_returning_malformed_json_gracefully(self):
        """It should return an empty list when the LLM returns malformed JSON."""
        schema = _make_schema()
        section = _make_section()
        client = MagicMock()
        client.call = AsyncMock(return_value=LLMResponse(
            content="this is not json {{{",
            input_tokens=10,
            output_tokens=5,
            model="deepseek-chat",
        ))

        result = await extract_concepts_from_section(section, schema, client)

        assert result == []

    @pytest.mark.asyncio
    async def test_it_should_set_section_heading_on_each_concept(self):
        """It should set the section field on each extracted ConceptNode."""
        schema = _make_schema()
        section = _make_section(heading="3 Main Results")
        client = _make_mock_client([
            {"name": "MDP", "semantic_type": "structure"},
        ])

        result = await extract_concepts_from_section(section, schema, client)

        assert len(result) == 1
        assert result[0].rhetorical_origin == "3 Main Results"

    @pytest.mark.asyncio
    async def test_it_should_not_inject_concept_shortlist_when_none(self):
        """It should omit the known-concepts block when existing_concepts is None."""
        schema = _make_schema()
        section = _make_section()
        client = _make_mock_client([])

        await extract_concepts_from_section(section, schema, client)

        _, user_prompt = client.call.call_args[0]
        assert "Known concepts" not in user_prompt

    @pytest.mark.asyncio
    async def test_it_should_pass_system_prompt_built_from_schema(self):
        """It should pass a schema-derived system prompt as the first argument."""
        schema = _make_schema()
        section = _make_section()
        client = _make_mock_client([])

        await extract_concepts_from_section(section, schema, client)

        system_prompt, _ = client.call.call_args[0]
        assert "structure" in system_prompt
        assert "quantity" in system_prompt

    @pytest.mark.asyncio
    async def test_it_should_include_section_content_in_user_prompt(self):
        """It should embed the section content in the user prompt."""
        schema = _make_schema()
        content = "Let V be a vector space over the reals."
        section = _make_section(content=content)
        client = _make_mock_client([])

        await extract_concepts_from_section(section, schema, client)

        _, user_prompt = client.call.call_args[0]
        assert content in user_prompt
