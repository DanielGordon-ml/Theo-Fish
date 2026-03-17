"""
@file test_embedding_client.py
@description Tests for the EmbeddingClient OpenAI wrapper.
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

from graph_builder.extraction.dedup.embedding_client import EmbeddingClient


def _make_mock_openai(embeddings: list[list[float]]):
    """Build a mock AsyncOpenAI client returning given embeddings."""
    mock_data = [MagicMock(embedding=e) for e in embeddings]
    mock_response = MagicMock()
    mock_response.data = mock_data
    mock_client = MagicMock()
    mock_client.embeddings.create = AsyncMock(return_value=mock_response)
    return mock_client


class TestEmbeddingClientEmbedBatch:
    """Tests for EmbeddingClient.embed_batch()."""

    @pytest.mark.asyncio
    async def test_it_should_return_correct_dimensionality(self):
        """It should return embeddings with 1536 dimensions."""
        dims = 1536
        fake_embedding = [0.1] * dims
        mock_client = _make_mock_openai([fake_embedding])

        client = EmbeddingClient(openai_client=mock_client)
        results = await client.embed_batch(["markov chain"])

        assert len(results) == 1
        assert len(results[0]) == dims

    @pytest.mark.asyncio
    async def test_it_should_return_embeddings_for_multiple_texts(self):
        """It should return one embedding per text in a batch."""
        dims = 1536
        fake_embeddings = [[0.1] * dims, [0.2] * dims, [0.3] * dims]
        mock_client = _make_mock_openai(fake_embeddings)

        client = EmbeddingClient(openai_client=mock_client)
        results = await client.embed_batch(
            ["markov chain", "neural network", "banach space"],
        )

        assert len(results) == 3

    @pytest.mark.asyncio
    async def test_it_should_call_openai_with_correct_model(self):
        """It should call the OpenAI API with the configured model."""
        fake_embedding = [0.0] * 1536
        mock_client = _make_mock_openai([fake_embedding])

        client = EmbeddingClient(openai_client=mock_client, model="text-embedding-3-small")
        await client.embed_batch(["test"])

        mock_client.embeddings.create.assert_called_once()
        call_kwargs = mock_client.embeddings.create.call_args
        assert call_kwargs.kwargs["model"] == "text-embedding-3-small"

    @pytest.mark.asyncio
    async def test_it_should_handle_empty_batch(self):
        """It should return an empty list for an empty batch."""
        mock_client = _make_mock_openai([])

        client = EmbeddingClient(openai_client=mock_client)
        results = await client.embed_batch([])

        assert results == []


class TestEmbeddingClientEmbedSingle:
    """Tests for EmbeddingClient.embed_single()."""

    @pytest.mark.asyncio
    async def test_it_should_return_single_embedding(self):
        """It should return a single embedding vector."""
        fake_embedding = [0.5] * 1536
        mock_client = _make_mock_openai([fake_embedding])

        client = EmbeddingClient(openai_client=mock_client)
        result = await client.embed_single("markov chain")

        assert len(result) == 1536
        assert result == fake_embedding

    @pytest.mark.asyncio
    async def test_it_should_delegate_to_embed_batch(self):
        """It should call embed_batch internally with a single-item list."""
        fake_embedding = [0.1] * 1536
        mock_client = _make_mock_openai([fake_embedding])

        client = EmbeddingClient(openai_client=mock_client)
        result = await client.embed_single("test concept")

        mock_client.embeddings.create.assert_called_once()
        assert isinstance(result, list)
