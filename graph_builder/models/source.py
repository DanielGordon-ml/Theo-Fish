"""
@file source.py
@description SourceNode dataclass for paper provenance.
"""

from pydantic import BaseModel


class SourceNode(BaseModel):
    """Paper provenance as a first-class node."""

    arxiv_id: str
    title: str = ""
    authors: list[str] = []
    date_published: str = ""
    date_extracted: str = ""
    human_notes: str = ""
