"""
@file test_graph_reader.py
@description Unit tests for GraphReader — all Neo4j calls are mocked.
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

from graph_builder.graph.graph_reader import GraphReader
from graph_builder.models.concept import ConceptNode


def _make_mock_client() -> MagicMock:
    """Build a mock Neo4jClient with async read/write methods."""
    client = MagicMock()
    client.execute_read = AsyncMock(return_value=[])
    client.execute_write = AsyncMock(return_value=[])
    return client


class TestGetAllConceptSlugs:
    """Tests for GraphReader.get_all_concept_slugs()."""

    @pytest.mark.asyncio
    async def test_it_should_return_list_of_slug_strings(self):
        """Returns a flat list of slug strings from Neo4j."""
        mock_client = _make_mock_client()
        mock_client.execute_read = AsyncMock(
            return_value=[
                {"slug": "banach-space"},
                {"slug": "hilbert-space"},
                {"slug": "normed-space"},
            ]
        )
        reader = GraphReader(mock_client)

        slugs = await reader.get_all_concept_slugs()

        assert slugs == ["banach-space", "hilbert-space", "normed-space"]
        mock_client.execute_read.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_it_should_return_empty_list_when_no_concepts(self):
        """Returns empty list when the graph has no concepts."""
        mock_client = _make_mock_client()
        reader = GraphReader(mock_client)

        slugs = await reader.get_all_concept_slugs()

        assert slugs == []


class TestGetExistingConcept:
    """Tests for GraphReader.get_existing_concept()."""

    @pytest.mark.asyncio
    async def test_it_should_return_concept_node_when_found(self):
        """Returns a fully hydrated ConceptNode from the DB record."""
        mock_client = _make_mock_client()
        mock_client.execute_read = AsyncMock(
            return_value=[
                {
                    "slug": "banach-space",
                    "name": "Banach Space",
                    "semantic_type": "space",
                    "canonical_definition": "A complete normed space.",
                    "formal_spec": "(V, ||·||)",
                    "aliases": ["B-space"],
                    "status": "canonical",
                    "embedding": [],
                }
            ]
        )
        reader = GraphReader(mock_client)

        result = await reader.get_existing_concept("banach-space")

        assert result is not None
        assert isinstance(result, ConceptNode)
        assert result.slug == "banach-space"
        assert result.name == "Banach Space"
        assert result.semantic_type == "space"

    @pytest.mark.asyncio
    async def test_it_should_return_none_when_not_found(self):
        """Returns None when no Concept node matches the slug."""
        mock_client = _make_mock_client()
        reader = GraphReader(mock_client)

        result = await reader.get_existing_concept("nonexistent-concept")

        assert result is None


class TestGetConceptNeighbors:
    """Tests for GraphReader.get_concept_neighbors()."""

    @pytest.mark.asyncio
    async def test_it_should_return_neighboring_concepts(self):
        """Returns ConceptNodes connected via Graph A edges."""
        mock_client = _make_mock_client()
        mock_client.execute_read = AsyncMock(
            return_value=[
                {
                    "slug": "normed-space",
                    "name": "Normed Space",
                    "semantic_type": "space",
                },
                {
                    "slug": "metric-space",
                    "name": "Metric Space",
                    "semantic_type": "space",
                },
            ]
        )
        reader = GraphReader(mock_client)

        neighbors = await reader.get_concept_neighbors(["banach-space"])

        assert len(neighbors) == 2
        assert all(isinstance(n, ConceptNode) for n in neighbors)
        slugs = [n.slug for n in neighbors]
        assert "normed-space" in slugs
        assert "metric-space" in slugs

    @pytest.mark.asyncio
    async def test_it_should_return_empty_list_for_no_neighbors(self):
        """Returns empty list when concept has no Graph A edges."""
        mock_client = _make_mock_client()
        reader = GraphReader(mock_client)

        neighbors = await reader.get_concept_neighbors(["isolated-concept"])

        assert neighbors == []


class TestVectorSimilaritySearch:
    """Tests for GraphReader.vector_similarity_search()."""

    @pytest.mark.asyncio
    async def test_it_should_return_slug_score_tuples(self):
        """Returns list of (slug, score) from vector index query."""
        mock_client = _make_mock_client()
        mock_client.execute_read = AsyncMock(
            return_value=[
                {"slug": "banach-space", "score": 0.95},
                {"slug": "hilbert-space", "score": 0.88},
            ]
        )
        reader = GraphReader(mock_client)

        embedding = [0.1] * 128
        results = await reader.vector_similarity_search(embedding, top_k=5)

        assert len(results) == 2
        assert results[0] == ("banach-space", 0.95)
        assert results[1] == ("hilbert-space", 0.88)
        mock_client.execute_read.assert_awaited_once()
        cypher = mock_client.execute_read.call_args[0][0]
        assert "vector" in cypher.lower() or "db.index.vector" in cypher

    @pytest.mark.asyncio
    async def test_it_should_use_top_k_default_of_twenty(self):
        """Default top_k is 20 when not specified."""
        mock_client = _make_mock_client()
        reader = GraphReader(mock_client)

        await reader.vector_similarity_search([0.1] * 128)

        kwargs = mock_client.execute_read.call_args[1]
        assert kwargs["top_k"] == 20


class TestIsPaperBuilt:
    """Tests for GraphReader.is_paper_built()."""

    @pytest.mark.asyncio
    async def test_it_should_return_true_when_source_exists(self):
        """Returns True if a Source node for the arxiv_id exists."""
        mock_client = _make_mock_client()
        mock_client.execute_read = AsyncMock(
            return_value=[{"count": 1}]
        )
        reader = GraphReader(mock_client)

        result = await reader.is_paper_built("2301.00001")

        assert result is True

    @pytest.mark.asyncio
    async def test_it_should_return_false_when_source_missing(self):
        """Returns False if no Source node for the arxiv_id exists."""
        mock_client = _make_mock_client()
        mock_client.execute_read = AsyncMock(
            return_value=[{"count": 0}]
        )
        reader = GraphReader(mock_client)

        result = await reader.is_paper_built("9999.99999")

        assert result is False
