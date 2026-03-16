"""
@file test_dedup_cascade.py
@description Tests for the full dedup cascade orchestration.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from graph_builder.models.concept import ConceptNode
from graph_builder.extraction.dedup.dedup_cascade import DedupResult, run_dedup_cascade
from graph_builder.extraction.dedup.embedding_client import EmbeddingClient


def _make_concept(name: str, aliases: list[str] = []) -> ConceptNode:
    """Build a ConceptNode for testing."""
    return ConceptNode(name=name, semantic_type="set", aliases=aliases)


def _make_graph_reader(
    existing_slugs: list[str] | None = None,
    existing_concept: ConceptNode | None = None,
    vector_results: list[tuple[str, float]] | None = None,
) -> MagicMock:
    """Build a mock GraphReader with configurable responses."""
    reader = MagicMock()
    reader.get_all_concept_slugs = AsyncMock(return_value=existing_slugs or [])
    reader.get_existing_concept = AsyncMock(return_value=existing_concept)
    reader.vector_similarity_search = AsyncMock(return_value=vector_results or [])
    return reader


def _make_embedding_client(embedding: list[float] | None = None) -> EmbeddingClient:
    """Build a mock EmbeddingClient."""
    vec = embedding or [0.1] * 1536
    client = MagicMock(spec=EmbeddingClient)
    client.embed_single = AsyncMock(return_value=vec)
    return client


def _make_llm_client(is_same: bool = True) -> MagicMock:
    """Build a mock DeepSeekClient returning a confirmation response."""
    import json
    response = MagicMock()
    response.content = json.dumps({"is_same_concept": is_same})
    client = MagicMock()
    client.call = AsyncMock(return_value=response)
    return client


class TestDedupCascadeAliasMatch:
    """Tests for the alias-match step of the cascade."""

    @pytest.mark.asyncio
    async def test_it_should_auto_resolve_exact_alias_match(self):
        """It should resolve when an existing concept's alias matches the slug."""
        concept = _make_concept("MDP")
        existing = _make_concept("Markov Decision Process", aliases=["mdp"])
        reader = _make_graph_reader(
            existing_slugs=["markov-decision-process"],
            existing_concept=existing,
        )
        embedding_client = _make_embedding_client()

        result = await run_dedup_cascade(concept, reader, embedding_client)

        assert result.is_new is False
        assert result.match_method == "alias"
        assert result.match_confidence == pytest.approx(1.0)
        assert result.existing_slug == "markov-decision-process"

    @pytest.mark.asyncio
    async def test_it_should_propagate_confidence_correctly_for_alias(self):
        """It should set confidence to 1.0 for alias matches."""
        concept = _make_concept("RL")
        existing = _make_concept("Reinforcement Learning", aliases=["rl"])
        reader = _make_graph_reader(
            existing_slugs=["reinforcement-learning"],
            existing_concept=existing,
        )
        embedding_client = _make_embedding_client()

        result = await run_dedup_cascade(concept, reader, embedding_client)

        assert result.match_confidence == pytest.approx(1.0)


class TestDedupCascadeEmbedding:
    """Tests for the embedding similarity step of the cascade."""

    @pytest.mark.asyncio
    async def test_it_should_auto_resolve_high_embedding_similarity(self):
        """It should auto-resolve when embedding score > 0.85."""
        concept = _make_concept("Markov Chains")
        reader = _make_graph_reader(
            existing_slugs=["markov-chain"],
            vector_results=[("markov-chain", 0.92)],
        )
        embedding_client = _make_embedding_client()

        result = await run_dedup_cascade(concept, reader, embedding_client)

        assert result.is_new is False
        assert result.match_method == "embedding"
        assert result.match_confidence == pytest.approx(0.92)
        assert result.existing_slug == "markov-chain"

    @pytest.mark.asyncio
    async def test_it_should_create_new_concept_for_low_similarity(self):
        """It should create a new concept when embedding score < 0.60."""
        concept = _make_concept("Banach Space")
        reader = _make_graph_reader(
            existing_slugs=["markov-chain"],
            vector_results=[("markov-chain", 0.30)],
        )
        embedding_client = _make_embedding_client()

        result = await run_dedup_cascade(concept, reader, embedding_client)

        assert result.is_new is True
        assert result.match_method == "new"
        assert result.existing_slug is None


class TestDedupCascadeLLMConfirmation:
    """Tests for the LLM confirmation step of the cascade."""

    @pytest.mark.asyncio
    async def test_it_should_confirm_moderate_similarity_via_llm(self):
        """It should use LLM to confirm when embedding score is 0.60-0.85."""
        concept = _make_concept("Value Iteration Method")
        reader = _make_graph_reader(
            existing_slugs=["value-iteration"],
            vector_results=[("value-iteration", 0.72)],
        )
        embedding_client = _make_embedding_client()
        llm_client = _make_llm_client(is_same=True)

        result = await run_dedup_cascade(concept, reader, embedding_client, llm_client)

        assert result.is_new is False
        assert result.match_method == "embedding+llm"
        assert result.existing_slug == "value-iteration"

    @pytest.mark.asyncio
    async def test_it_should_create_new_when_llm_denies_match(self):
        """It should create a new concept when LLM says concepts are different."""
        concept = _make_concept("Temporal Difference")
        reader = _make_graph_reader(
            existing_slugs=["bellman-equation"],
            vector_results=[("bellman-equation", 0.70)],
        )
        embedding_client = _make_embedding_client()
        llm_client = _make_llm_client(is_same=False)

        result = await run_dedup_cascade(concept, reader, embedding_client, llm_client)

        assert result.is_new is True
        assert result.match_method == "new"

    @pytest.mark.asyncio
    async def test_it_should_fallback_to_new_when_llm_is_none(self):
        """It should fallback to 'new' when no LLM client is provided."""
        concept = _make_concept("Q-Learning Algorithm")
        reader = _make_graph_reader(
            existing_slugs=["q-learning"],
            vector_results=[("q-learning", 0.75)],
        )
        embedding_client = _make_embedding_client()

        result = await run_dedup_cascade(concept, reader, embedding_client, llm_client=None)

        assert result.is_new is True
        assert result.match_method == "new"

    @pytest.mark.asyncio
    async def test_it_should_fallback_to_new_when_llm_confirmation_fails(self):
        """It should fallback to 'new' when LLM raises an exception."""
        concept = _make_concept("Policy Gradient Method")
        reader = _make_graph_reader(
            existing_slugs=["policy-gradient"],
            vector_results=[("policy-gradient", 0.73)],
        )
        embedding_client = _make_embedding_client()
        llm_client = MagicMock()
        llm_client.call = AsyncMock(side_effect=RuntimeError("LLM unavailable"))

        result = await run_dedup_cascade(concept, reader, embedding_client, llm_client)

        assert result.is_new is True
        assert result.match_method == "new"


class TestDedupCascadeNewConcept:
    """Tests for the new-concept path of the cascade."""

    @pytest.mark.asyncio
    async def test_it_should_return_new_when_graph_is_empty(self):
        """It should create a new concept when the graph has no concepts."""
        concept = _make_concept("Hilbert Space")
        reader = _make_graph_reader(existing_slugs=[], vector_results=[])
        embedding_client = _make_embedding_client()

        result = await run_dedup_cascade(concept, reader, embedding_client)

        assert result.is_new is True
        assert result.match_method == "new"
        assert result.existing_slug is None

    @pytest.mark.asyncio
    async def test_it_should_propagate_slug_of_new_concept(self):
        """It should include the concept's slug in the result."""
        concept = _make_concept("Hilbert Space")
        reader = _make_graph_reader(existing_slugs=[], vector_results=[])
        embedding_client = _make_embedding_client()

        result = await run_dedup_cascade(concept, reader, embedding_client)

        assert result.slug == concept.slug
