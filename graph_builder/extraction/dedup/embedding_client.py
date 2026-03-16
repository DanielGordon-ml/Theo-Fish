"""
@file embedding_client.py
@description Batch embedding via OpenAI API for concept similarity search.
"""

from openai import AsyncOpenAI

from graph_builder.config.config import (
    EMBEDDING_MODEL,
    OPENAI_API_KEY,
)


class EmbeddingClient:
    """Async client for generating text embeddings via the OpenAI API."""

    def __init__(
        self,
        openai_client: AsyncOpenAI | None = None,
        model: str = EMBEDDING_MODEL,
    ):
        """Initialize the embedding client.

        @param openai_client Optional pre-built AsyncOpenAI instance (for testing)
        @param model Embedding model name
        """
        self._client = openai_client or AsyncOpenAI(api_key=OPENAI_API_KEY)
        self._model = model

    async def embed_batch(self, texts: list[str]) -> list[list[float]]:
        """Compute embeddings for a batch of texts.

        @param texts List of strings to embed
        @returns List of embedding vectors, one per input text
        """
        if not texts:
            return []
        response = await self._client.embeddings.create(
            input=texts,
            model=self._model,
        )
        return [item.embedding for item in response.data]

    async def embed_single(self, text: str) -> list[float]:
        """Compute embedding for a single text.

        @param text String to embed
        @returns Embedding vector as a list of floats
        """
        results = await self.embed_batch([text])
        return results[0]
