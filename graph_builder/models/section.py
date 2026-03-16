"""
@file section.py
@description Section model for chunked paper content. Moved from v1.
"""

from pydantic import BaseModel


class Section(BaseModel):
    """A chunked section of a paper for LLM processing."""

    heading: str
    level: int
    content: str
    char_count: int
    index: int
