"""
@file protocol.py
@description LLMClient protocol shared by DeepSeek and Claude clients.
"""

from typing import Protocol, runtime_checkable

from graph_builder.llm.llm_client import LLMResponse


@runtime_checkable
class LLMClient(Protocol):
    """Structural protocol for LLM clients used in extraction passes.

    Both DeepSeekClient and ClaudeClient satisfy this protocol.
    """

    async def call(
        self,
        system_prompt: str,
        user_prompt: str,
        thinking: bool | None = None,
    ) -> LLMResponse:
        """Send a chat completion request and return the response.

        @param system_prompt System message content
        @param user_prompt User message content
        @param thinking Optional thinking mode toggle
        @returns LLMResponse with content and token counts
        """
        ...
