"""
@file errors.py
@description Custom exceptions for the data cleaner.
"""


class CleanerError(Exception):
    """Raised when cleaning a single paper fails."""

    def __init__(self, arxiv_id: str, reason: str):
        super().__init__(f"[{arxiv_id}] {reason}")
        self.arxiv_id = arxiv_id
        self.reason = reason
