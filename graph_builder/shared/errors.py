"""
@file errors.py
@description Custom exceptions for the dual-graph knowledge graph builder.
"""


class GraphBuilderError(Exception):
    """Raised when graph building fails for a single paper."""

    def __init__(self, arxiv_id: str, reason: str):
        super().__init__(f"[{arxiv_id}] {reason}")
        self.arxiv_id = arxiv_id
        self.reason = reason


class ValidationError(Exception):
    """Raised when schema validation detects an issue."""

    def __init__(self, rule: str, severity: str, message: str):
        super().__init__(f"[{severity}] {rule}: {message}")
        self.rule = rule
        self.severity = severity


class DedupConflictError(Exception):
    """Raised when concept dedup finds an ambiguous match."""

    def __init__(
        self, new_slug: str, existing_slug: str, similarity: float,
    ):
        super().__init__(
            f"Ambiguous match: '{new_slug}' \u2194 '{existing_slug}' "
            f"(similarity={similarity:.2f})"
        )
        self.new_slug = new_slug
        self.existing_slug = existing_slug
        self.similarity = similarity
