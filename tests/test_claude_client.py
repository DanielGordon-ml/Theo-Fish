"""
@file test_claude_client.py
@description Tests for the Claude Opus 4.6 async client with mocked Anthropic SDK.
"""

import json
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from graph_builder.llm.llm_client import LLMResponse
from graph_builder.llm.protocol import LLMClient


class TestClaudeClient:
    """Tests for ClaudeClient."""

    @pytest.mark.asyncio
    async def test_it_should_return_llm_response_on_success(self):
        """It should parse the Anthropic response into an LLMResponse."""
        from graph_builder.llm.claude_client import ClaudeClient

        mock_response = MagicMock()
        mock_response.content = [MagicMock(text='{"claims": []}')]
        mock_response.usage.input_tokens = 100
        mock_response.usage.output_tokens = 50
        mock_response.model = "claude-opus-4-6"

        with patch("graph_builder.llm.claude_client.AsyncAnthropic") as MockAnthropic:
            mock_client = AsyncMock()
            mock_client.messages.create = AsyncMock(return_value=mock_response)
            MockAnthropic.return_value = mock_client

            client = ClaudeClient(api_key="test-key", concurrency=5)
            result = await client.call("system prompt", "user prompt")

        assert isinstance(result, LLMResponse)
        assert result.content == '{"claims": []}'
        assert result.input_tokens == 100
        assert result.output_tokens == 50

    @pytest.mark.asyncio
    async def test_it_should_extract_json_from_fenced_code_block(self):
        """It should fall back to extracting JSON from code fences."""
        from graph_builder.llm.claude_client import extract_json_content

        raw = 'Here is the result:\n```json\n{"key": "value"}\n```\nDone.'
        result = extract_json_content(raw)
        assert result == '{"key": "value"}'

    @pytest.mark.asyncio
    async def test_it_should_return_raw_content_when_valid_json(self):
        """It should return raw content directly when it is valid JSON."""
        from graph_builder.llm.claude_client import extract_json_content

        raw = '{"key": "value"}'
        result = extract_json_content(raw)
        assert result == '{"key": "value"}'

    @pytest.mark.asyncio
    async def test_it_should_return_raw_content_when_no_json_found(self):
        """It should return raw content when no JSON is extractable."""
        from graph_builder.llm.claude_client import extract_json_content

        raw = "This is not JSON at all."
        result = extract_json_content(raw)
        assert result == raw

    def test_it_should_satisfy_llm_client_protocol(self):
        """It should be recognized as an LLMClient."""
        from graph_builder.llm.claude_client import ClaudeClient

        with patch("graph_builder.llm.claude_client.AsyncAnthropic"):
            client = ClaudeClient(api_key="test-key")
        assert isinstance(client, LLMClient)

    def test_it_should_raise_on_missing_api_key(self):
        """It should raise ValueError when no API key is provided."""
        from graph_builder.llm.claude_client import ClaudeClient

        with pytest.raises(ValueError, match="ANTHROPIC_API_KEY"):
            ClaudeClient(api_key=None)
