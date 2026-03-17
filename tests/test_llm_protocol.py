"""
@file test_llm_protocol.py
@description Tests that the LLMClient protocol is satisfied by objects with async call method.
"""

from unittest.mock import AsyncMock, MagicMock


from graph_builder.llm.protocol import LLMClient
from graph_builder.llm.llm_client import LLMResponse


class TestLLMClientProtocol:
    """Tests for the LLMClient protocol."""

    def test_it_should_accept_any_object_with_async_call_method(self):
        """It should be satisfied by any object with the right call signature."""
        mock = MagicMock()
        mock.call = AsyncMock(
            return_value=LLMResponse(
                content="{}",
                input_tokens=0,
                output_tokens=0,
                model="test",
            )
        )
        assert isinstance(mock, LLMClient)

    def test_it_should_reject_objects_without_call_method(self):
        """It should not be satisfied by objects missing a call method."""
        mock = MagicMock(spec=[])
        assert not isinstance(mock, LLMClient)
