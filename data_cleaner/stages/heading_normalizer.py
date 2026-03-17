"""
@file heading_normalizer.py
@description Stage 3: Normalize heading hierarchy per converter type.
"""

import re

from data_cleaner.models import StageResult

STAGE_NAME = "heading_normalizer"

# Heading at start of line: # ... ## ... etc.
_HEADING = re.compile(r"^(#{1,6})\s+(.+)$", re.MULTILINE)

# Fenced code block boundaries
_CODE_FENCE = re.compile(r"^```", re.MULTILINE)

# Roman numeral section: "I.", "II.", "III.", "IV.", "V.", etc.
_ROMAN_SECTION = re.compile(r"^[IVXLC]+\.\s")

# Letter subsection: "A.", "B.", "C." etc.
_LETTER_SUBSECTION = re.compile(r"^[A-Z]\.\s")

# Numbered subsection: "1.", "2.", "3." etc.
_NUMBERED_SUBSECTION = re.compile(r"^\d+\.\s")

# Special sections that should be h2 in MinerU output
SPECIAL_SECTIONS = {
    "abstract",
    "references",
    "bibliography",
    "appendix",
    "acknowledgments",
    "acknowledgements",
    "conclusion",
    "conclusions",
}


def _find_code_ranges(text: str) -> list[tuple[int, int]]:
    """Find character ranges of fenced code blocks."""
    ranges: list[tuple[int, int]] = []
    fences = list(_CODE_FENCE.finditer(text))

    i = 0
    while i + 1 < len(fences):
        ranges.append((fences[i].start(), fences[i + 1].end()))
        i += 2

    return ranges


def _in_code_block(pos: int, ranges: list[tuple[int, int]]) -> bool:
    """Check if a position falls within any code block range."""
    return any(start <= pos <= end for start, end in ranges)


def _classify_mineru_heading(title_text: str) -> int:
    """Determine target heading level for a MinerU all-h1 heading.

    Returns target level: 1 for title, 2 for major sections, 3 for sub.
    """
    stripped = title_text.strip()
    lower = stripped.lower()

    if lower in SPECIAL_SECTIONS:
        return 2
    if _ROMAN_SECTION.match(stripped):
        return 2
    if _LETTER_SUBSECTION.match(stripped):
        return 3
    if _NUMBERED_SUBSECTION.match(stripped):
        return 3

    return 1


def _normalize_mineru(
    text: str, code_ranges: list[tuple[int, int]]
) -> tuple[str, dict[str, int]]:
    """Normalize MinerU output: demote all-h1 headings based on patterns."""
    changes = 0
    duplicate_titles = 0
    first_title: str | None = None

    def _replace_heading(m: re.Match) -> str:
        nonlocal changes, first_title, duplicate_titles

        if _in_code_block(m.start(), code_ranges):
            return m.group(0)

        hashes = m.group(1)
        title_text = m.group(2)

        # Only process h1 headings for MinerU
        if len(hashes) != 1:
            return m.group(0)

        # First h1 stays as title
        if first_title is None:
            first_title = title_text.strip()
            return m.group(0)

        # Duplicate title removal
        if title_text.strip() == first_title:
            duplicate_titles += 1
            return ""

        target = _classify_mineru_heading(title_text)
        if target == 1:
            return m.group(0)

        new_hashes = "#" * target
        changes += 1
        return f"{new_hashes} {title_text}"

    result = _HEADING.sub(_replace_heading, text)
    details: dict[str, int] = {"headings_demoted": changes}
    if duplicate_titles:
        details["duplicate_titles"] = duplicate_titles
        changes += duplicate_titles

    return result, details


def _normalize_arxiv2md(
    text: str, code_ranges: list[tuple[int, int]]
) -> tuple[str, dict[str, int]]:
    """Normalize arxiv2md output: promote headings to fill from h1."""
    # Find minimum heading level outside code blocks
    min_level = 7
    for m in _HEADING.finditer(text):
        if _in_code_block(m.start(), code_ranges):
            continue
        level = len(m.group(1))
        if level < min_level:
            min_level = level

    if min_level <= 1 or min_level == 7:
        return text, {"headings_promoted": 0}

    shift = min_level - 1
    changes = 0

    def _promote(m: re.Match) -> str:
        nonlocal changes
        if _in_code_block(m.start(), code_ranges):
            return m.group(0)

        level = len(m.group(1))
        new_level = max(1, level - shift)
        if new_level == level:
            return m.group(0)

        changes += 1
        return f"{'#' * new_level} {m.group(2)}"

    result = _HEADING.sub(_promote, text)
    return result, {"headings_promoted": changes}


def normalize_headings(
    text: str,
    converter: str = "mineru",
) -> tuple[str, StageResult]:
    """Run Stage 3: normalize heading hierarchy.

    For MinerU: demote all-h1 headings based on section numbering.
    For arxiv2md: promote headings so minimum level becomes h1.

    @returns Tuple of (cleaned text, StageResult).
    """
    code_ranges = _find_code_ranges(text)

    if converter == "arxiv2md":
        result, details = _normalize_arxiv2md(text, code_ranges)
    else:
        result, details = _normalize_mineru(text, code_ranges)

    total = sum(details.values())

    return result, StageResult(
        stage_name=STAGE_NAME,
        changes_made=total,
        details=details,
    )
