"""
@file errors.py
@description Custom exceptions for the knowledge graph builder.
"""


class GraphBuilderError(Exception):
    """Raised when graph building fails for a single paper."""

    def __init__(self, arxiv_id: str, reason: str):
        super().__init__(f"[{arxiv_id}] {reason}")
        self.arxiv_id = arxiv_id
        self.reason = reason
