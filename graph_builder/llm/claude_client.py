"""
@file claude_client.py
@description Claude Opus 4.6 async client via Anthropic SDK with rate limiting and retries.
"""

import asyncio
import json
import logging
import random
import re

from anthropic import AsyncAnthropic, APIError, RateLimitError

from graph_builder.config.config import (
    ANTHROPIC_API_KEY,
    CLAUDE_MODEL,
    DEFAULT_CONCURRENCY,
    MAX_RETRIES,
)
from graph_builder.llm.llm_client import LLMResponse

logger = logging.getLogger("graph_builder")

# HTTP status codes that warrant a retry
_RETRYABLE_CODES = {429, 500, 502, 503}

# Base delay in seconds for exponential backoff
_BASE_DELAY = 1.0

# Regex to extract JSON from Markdown fenced code blocks
_JSON_FENCE_RE = re.compile(r"```json\s*\n(.*?)\n\s*```", re.DOTALL)


def extract_json_content(raw: str) -> str:
    """Extract JSON from raw LLM response, handling code fences.

    Tries three strategies in order:
    (a) raw string is already valid JSON -- return as-is,
    (b) extract from ```json ... ``` fences,
    (c) return raw unchanged.

    @param raw Raw response text from Claude
    @returns Extracted JSON string or original text
    """
    try:
        json.loads(raw)
        return raw
    except (json.JSONDecodeError, ValueError):
        pass

    match = _JSON_FENCE_RE.search(raw)
    if match:
        return match.group(1).strip()

    return raw


class ClaudeClient:
    """Async client for Claude Opus 4.6 with rate limiting and retries."""

    def __init__(
        self,
        api_key: str | None = ANTHROPIC_API_KEY,
        concurrency: int = DEFAULT_CONCURRENCY,
    ):
        """Initialize the Claude client.

        @param api_key Anthropic API key
        @param concurrency Max concurrent LLM calls
        @raises ValueError if api_key is not set
        """
        if not api_key:
            raise ValueError(
                "ANTHROPIC_API_KEY is required. "
                "Set it in Theo-Fish/.env or pass explicitly.",
            )

        self._client = AsyncAnthropic(api_key=api_key)
        self._semaphore = asyncio.Semaphore(concurrency)
        self._model = CLAUDE_MODEL

    async def call(
        self,
        system_prompt: str,
        user_prompt: str,
        thinking: bool | None = None,
    ) -> LLMResponse:
        """Send a message to Claude and return the response.

        @param system_prompt System message content
        @param user_prompt User message content
        @param thinking Unused (kept for protocol compatibility)
        @raises APIError after exhausting retries
        """
        async with self._semaphore:
            return await self._call_with_retries(
                system_prompt, user_prompt,
            )

    async def _call_with_retries(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> LLMResponse:
        """Execute the call with exponential backoff retries."""
        last_error: Exception | None = None

        for attempt in range(MAX_RETRIES + 1):
            try:
                return await self._execute_call(
                    system_prompt, user_prompt,
                )
            except (RateLimitError, APIError) as err:
                last_error = err
                if not _is_retryable(err) or attempt == MAX_RETRIES:
                    raise
                delay = _compute_backoff_delay(attempt)
                logger.warning(
                    "Claude call failed (attempt %d/%d), retrying in %.1fs: %s",
                    attempt + 1, MAX_RETRIES + 1, delay, str(err),
                )
                await asyncio.sleep(delay)

        raise last_error  # type: ignore[misc]

    async def _execute_call(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> LLMResponse:
        """Execute a single Anthropic API call."""
        response = await self._client.messages.create(
            model=self._model,
            max_tokens=16384,
            system=system_prompt,
            messages=[{"role": "user", "content": user_prompt}],
        )

        raw_content = response.content[0].text
        content = extract_json_content(raw_content)

        return LLMResponse(
            content=content,
            input_tokens=response.usage.input_tokens,
            output_tokens=response.usage.output_tokens,
            model=response.model,
        )


def _is_retryable(err: APIError) -> bool:
    """Check if an API error warrants a retry.

    @param err The API error to inspect
    @returns True if the error is retryable
    """
    if isinstance(err, RateLimitError):
        return True
    status = getattr(err, "status_code", None)
    return status in _RETRYABLE_CODES


def _compute_backoff_delay(attempt: int) -> float:
    """Calculate exponential backoff delay with jitter.

    @param attempt Zero-based attempt number
    @returns Delay in seconds
    """
    return _BASE_DELAY * (2 ** attempt) + random.uniform(0, 1)
