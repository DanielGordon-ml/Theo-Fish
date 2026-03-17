"""
@file newline_normalizer.py
@description Stage 0: Fix literal \\n characters and strip arxiv2md metadata prefix.
"""

import re

from data_cleaner.models import StageResult

STAGE_NAME = "newline_normalizer"

# Matches the arxiv2md metadata prefix:
# summary='...' sections_tree='...' content='...<actual markdown>...'
_PREFIX_PATTERN = re.compile(
    r"^summary='.*?'\s*sections_tree='.*?'\s*(?:content=')?",
    re.DOTALL,
)

# Trailing quote from content='...' wrapper
_CONTENT_SUFFIX = re.compile(r"'\s*$")


def _has_real_newlines(text: str) -> bool:
    """Check if text contains real newline characters."""
    return "\n" in text


def _replace_literal_newlines(text: str) -> tuple[str, int]:
    """Replace literal two-char backslash-n with real newlines.

    Only runs when text has zero real newlines (arxiv2md output).
    Returns the cleaned text and count of replacements.
    """
    if _has_real_newlines(text):
        return text, 0

    count = text.count("\\n")
    if count == 0:
        return text, 0

    return text.replace("\\n", "\n"), count


def _strip_metadata_prefix(text: str) -> tuple[str, int]:
    """Remove the summary/sections_tree prefix from arxiv2md output.

    Returns the cleaned text and 1 if stripped, 0 otherwise.
    """
    match = _PREFIX_PATTERN.match(text)
    if not match:
        return text, 0

    text = text[match.end() :]
    # Strip trailing ' from content='...' wrapper
    text = _CONTENT_SUFFIX.sub("", text)
    return text.lstrip(), 1


def normalize_newlines(text: str) -> tuple[str, StageResult]:
    """Run Stage 0: normalize newlines and strip metadata prefix.

    @returns Tuple of (cleaned text, StageResult).
    """
    details: dict[str, int] = {}
    total_changes = 0

    text, literal_count = _replace_literal_newlines(text)
    if literal_count:
        details["literal_newlines"] = literal_count
        total_changes += literal_count

    text, prefix_count = _strip_metadata_prefix(text)
    if prefix_count:
        details["prefix_stripped"] = prefix_count
        total_changes += prefix_count

    return text, StageResult(
        stage_name=STAGE_NAME,
        changes_made=total_changes,
        details=details,
    )
