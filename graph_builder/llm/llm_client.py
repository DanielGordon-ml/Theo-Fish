"""
@file llm_client.py
@description DeepSeek V3 client via OpenAI SDK with rate limiting and retries.
"""

import asyncio
import logging
import random

from openai import AsyncOpenAI, APIError, RateLimitError
from pydantic import BaseModel

from graph_builder.config.config import (
    DEEPSEEK_API_KEY,
    DEEPSEEK_BASE_URL,
    DEEPSEEK_MODEL,
    DEFAULT_CONCURRENCY,
    LLM_THINKING,
    MAX_RETRIES,
)

logger = logging.getLogger("graph_builder")

# HTTP status codes that warrant a retry
_RETRYABLE_CODES = {429, 500, 502, 503}

# Base delay in seconds for exponential backoff
_BASE_DELAY = 1.0


class LLMResponse(BaseModel):
    """Response from the LLM including token usage."""

    content: str
    input_tokens: int
    output_tokens: int
    model: str


class DeepSeekClient:
    """Async client for DeepSeek V3 with rate limiting and retries."""

    def __init__(
        self,
        api_key: str | None = DEEPSEEK_API_KEY,
        concurrency: int = DEFAULT_CONCURRENCY,
        thinking: bool | None = None,
    ):
        """Initialize the DeepSeek client.

        @param api_key DeepSeek API key
        @param concurrency Max concurrent LLM calls
        @param thinking Enable thinking mode (None falls back to config)
        @raises ValueError if api_key is not set
        """
        if not api_key:
            raise ValueError(
                "DEEPSEEK_API_KEY is required. "
                "Set it in Theo-Fish/.env or pass explicitly.",
            )

        self._client = AsyncOpenAI(
            base_url=DEEPSEEK_BASE_URL,
            api_key=api_key,
        )
        self._semaphore = asyncio.Semaphore(concurrency)
        self._model = DEEPSEEK_MODEL
        self._thinking = thinking if thinking is not None else LLM_THINKING

    async def call(
        self,
        system_prompt: str,
        user_prompt: str,
        thinking: bool | None = None,
    ) -> LLMResponse:
        """Send a chat completion request with JSON mode.

        @param system_prompt System message content
        @param user_prompt User message content
        @param thinking Per-call thinking override (None uses init value)
        @raises APIError after exhausting retries
        """
        async with self._semaphore:
            return await self._call_with_retries(
                system_prompt,
                user_prompt,
                thinking,
            )

    async def _call_with_retries(
        self,
        system_prompt: str,
        user_prompt: str,
        thinking: bool | None = None,
    ) -> LLMResponse:
        """Execute the LLM call with exponential backoff retries."""
        resolved = thinking if thinking is not None else self._thinking
        last_error: Exception | None = None

        for attempt in range(MAX_RETRIES + 1):
            try:
                return await self._execute_call(
                    system_prompt,
                    user_prompt,
                    resolved,
                )
            except (RateLimitError, APIError) as err:
                last_error = err
                if not self._is_retryable(err) or attempt == MAX_RETRIES:
                    raise
                delay = _BASE_DELAY * (2**attempt) + random.uniform(0, 1)
                logger.warning(
                    "LLM call failed (attempt %d/%d), retrying in %.1fs: %s",
                    attempt + 1,
                    MAX_RETRIES + 1,
                    delay,
                    str(err),
                    extra={"arxiv_id": "llm"},
                )
                await asyncio.sleep(delay)

        raise last_error  # type: ignore[misc]

    async def _execute_call(
        self,
        system_prompt: str,
        user_prompt: str,
        thinking: bool = True,
    ) -> LLMResponse:
        """Execute a single LLM API call."""
        kwargs: dict = {
            "model": self._model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "response_format": {"type": "json_object"},
        }

        if thinking:
            kwargs["extra_body"] = {"thinking": {"type": "enabled"}}

        response = await self._client.chat.completions.create(**kwargs)

        return LLMResponse(
            content=response.choices[0].message.content,
            input_tokens=response.usage.prompt_tokens,
            output_tokens=response.usage.completion_tokens,
            model=response.model,
        )

    def _is_retryable(self, err: APIError) -> bool:
        """Check if an API error warrants a retry.

        @param err The API error to inspect
        @returns True if the error is retryable
        """
        if isinstance(err, RateLimitError):
            return True
        status = getattr(err, "status_code", None)
        if status is None:
            resp = getattr(err, "response", None)
            status = getattr(resp, "status_code", None)
        return status in _RETRYABLE_CODES
