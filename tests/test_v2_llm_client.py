"""
@file test_v2_llm_client.py
@description Tests for v2 DeepSeek LLM client with rate limiting and retries.
"""

import asyncio
from unittest.mock import AsyncMock, MagicMock

import pytest

from graph_builder.llm.llm_client import DeepSeekClient, LLMResponse


def _make_mock_response(
    content: str = "{}", prompt_tokens: int = 10, completion_tokens: int = 5
) -> MagicMock:
    """Build a minimal mock OpenAI chat completion response."""
    mock_response = MagicMock()
    mock_response.choices = [MagicMock()]
    mock_response.choices[0].message.content = content
    mock_response.usage.prompt_tokens = prompt_tokens
    mock_response.usage.completion_tokens = completion_tokens
    mock_response.model = "deepseek-chat"
    return mock_response


def _make_mock_http_response(status_code: int) -> MagicMock:
    """Build a minimal mock HTTP response for error construction."""
    mock_http = MagicMock()
    mock_http.status_code = status_code
    mock_http.headers = {}
    return mock_http


class TestDeepSeekClientInit:
    """Tests for DeepSeekClient initialization."""

    def test_it_should_raise_without_api_key(self):
        """Missing API key raises ValueError."""
        with pytest.raises(ValueError, match="DEEPSEEK_API_KEY"):
            DeepSeekClient(api_key=None)

    def test_it_should_accept_explicit_api_key(self):
        """Client initializes successfully with an explicit API key."""
        client = DeepSeekClient(api_key="test-key")
        assert client is not None

    def test_it_should_respect_concurrency_limit(self):
        """Semaphore is created with the given concurrency value."""
        client = DeepSeekClient(api_key="test-key", concurrency=3)
        assert client._semaphore._value == 3


class TestDeepSeekClientCall:
    """Tests for DeepSeekClient.call()."""

    @pytest.mark.asyncio
    async def test_it_should_return_llm_response(self):
        """Successful call returns LLMResponse with content and token counts."""
        client = DeepSeekClient(api_key="test-key")
        mock_response = _make_mock_response(
            content='{"entities": []}',
            prompt_tokens=100,
            completion_tokens=50,
        )
        client._client.chat.completions.create = AsyncMock(return_value=mock_response)

        result = await client.call(
            system_prompt="Extract entities",
            user_prompt="Section content here",
        )

        assert isinstance(result, LLMResponse)
        assert result.content == '{"entities": []}'
        assert result.input_tokens == 100
        assert result.output_tokens == 50
        assert result.model == "deepseek-chat"

    @pytest.mark.asyncio
    async def test_it_should_track_input_and_output_tokens(self):
        """Token counts from API usage are stored in LLMResponse."""
        client = DeepSeekClient(api_key="test-key")
        mock_response = _make_mock_response(prompt_tokens=250, completion_tokens=75)
        client._client.chat.completions.create = AsyncMock(return_value=mock_response)

        result = await client.call("sys", "usr")

        assert result.input_tokens == 250
        assert result.output_tokens == 75

    @pytest.mark.asyncio
    async def test_it_should_use_json_mode(self):
        """Call includes response_format: json_object for JSON mode."""
        client = DeepSeekClient(api_key="test-key")
        mock_response = _make_mock_response()
        create_mock = AsyncMock(return_value=mock_response)
        client._client.chat.completions.create = create_mock

        await client.call("system", "user")

        call_kwargs = create_mock.call_args.kwargs
        assert call_kwargs["response_format"] == {"type": "json_object"}

    @pytest.mark.asyncio
    async def test_it_should_respect_semaphore_concurrency_limit(self):
        """Concurrent calls are throttled by the semaphore."""
        client = DeepSeekClient(api_key="test-key", concurrency=1)
        max_concurrent = 0
        current_concurrent = 0

        async def tracked_create(**kwargs):
            nonlocal max_concurrent, current_concurrent
            current_concurrent += 1
            max_concurrent = max(max_concurrent, current_concurrent)
            await asyncio.sleep(0.05)
            current_concurrent -= 1
            return _make_mock_response()

        client._client.chat.completions.create = AsyncMock(side_effect=tracked_create)

        await asyncio.gather(
            client.call("s", "u"),
            client.call("s", "u"),
            client.call("s", "u"),
        )

        assert max_concurrent == 1

    @pytest.mark.asyncio
    async def test_it_should_retry_on_rate_limit_error(self):
        """429 RateLimitError triggers retry, succeeds on second attempt."""
        import unittest.mock
        from openai import RateLimitError

        client = DeepSeekClient(api_key="test-key")
        mock_response = _make_mock_response(content='{"ok": true}')

        rate_limit_err = RateLimitError(
            message="rate limited",
            response=_make_mock_http_response(429),
            body=None,
        )

        # Patch asyncio.sleep to avoid real delays in the retry backoff
        with unittest.mock.patch("asyncio.sleep", new_callable=AsyncMock):
            create_mock = AsyncMock(side_effect=[rate_limit_err, mock_response])
            client._client.chat.completions.create = create_mock
            result = await client.call("system", "user")

        assert result.content == '{"ok": true}'
        assert create_mock.call_count == 2

    @pytest.mark.asyncio
    async def test_it_should_raise_after_exhausting_retries(self):
        """Persistent API errors raise after MAX_RETRIES attempts."""
        from openai import APIError

        client = DeepSeekClient(api_key="test-key")
        api_err = APIError(
            message="server error",
            request=MagicMock(),
            body=None,
        )
        client._client.chat.completions.create = AsyncMock(side_effect=api_err)

        import unittest.mock

        with unittest.mock.patch("asyncio.sleep", new_callable=AsyncMock):
            with pytest.raises(APIError):
                await client.call("system", "user")


class TestDeepSeekClientThinking:
    """Tests for configurable thinking mode."""

    @pytest.mark.asyncio
    async def test_it_should_omit_extra_body_when_thinking_disabled(self):
        """Thinking=False omits extra_body from the API call."""
        client = DeepSeekClient(api_key="test-key", thinking=False)
        mock_response = _make_mock_response()
        create_mock = AsyncMock(return_value=mock_response)
        client._client.chat.completions.create = create_mock

        await client.call("system", "user")

        call_kwargs = create_mock.call_args.kwargs
        assert "extra_body" not in call_kwargs

    @pytest.mark.asyncio
    async def test_it_should_include_extra_body_when_thinking_enabled(self):
        """Thinking=True adds extra_body with thinking config."""
        client = DeepSeekClient(api_key="test-key", thinking=True)
        mock_response = _make_mock_response()
        create_mock = AsyncMock(return_value=mock_response)
        client._client.chat.completions.create = create_mock

        await client.call("system", "user")

        call_kwargs = create_mock.call_args.kwargs
        assert call_kwargs["extra_body"] == {"thinking": {"type": "enabled"}}

    @pytest.mark.asyncio
    async def test_it_should_override_thinking_per_call(self):
        """Per-call thinking=True overrides instance default of False."""
        client = DeepSeekClient(api_key="test-key", thinking=False)
        mock_response = _make_mock_response()
        create_mock = AsyncMock(return_value=mock_response)
        client._client.chat.completions.create = create_mock

        await client.call("system", "user", thinking=True)

        call_kwargs = create_mock.call_args.kwargs
        assert call_kwargs["extra_body"] == {"thinking": {"type": "enabled"}}


class TestLLMResponse:
    """Tests for LLMResponse model."""

    def test_it_should_store_all_fields(self):
        """LLMResponse stores content, token counts, and model name."""
        resp = LLMResponse(
            content='{"entities": []}',
            input_tokens=500,
            output_tokens=200,
            model="deepseek-chat",
        )
        assert resp.content == '{"entities": []}'
        assert resp.input_tokens == 500
        assert resp.output_tokens == 200
        assert resp.model == "deepseek-chat"
