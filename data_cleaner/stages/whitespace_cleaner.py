"""
@file whitespace_cleaner.py
@description Stage 4: Collapse excessive whitespace, normalize line endings.
"""

import re

from data_cleaner.models import StageResult

STAGE_NAME = "whitespace_cleaner"

# Fenced code block boundaries
_CODE_FENCE = re.compile(r"^```", re.MULTILINE)

# 3+ consecutive newlines
_EXCESS_NEWLINES = re.compile(r"\n{3,}")

# Trailing whitespace on a line (spaces/tabs before newline)
_TRAILING_WS = re.compile(r"[ \t]+$", re.MULTILINE)


def _split_code_blocks(text: str) -> list[tuple[str, bool]]:
    """Split text into (segment, is_code) pairs."""
    fences = [m.start() for m in _CODE_FENCE.finditer(text)]
    if not fences:
        return [(text, False)]

    parts: list[tuple[str, bool]] = []
    prev = 0
    in_code = False

    for pos in fences:
        line_end = text.find("\n", pos)
        if line_end == -1:
            line_end = len(text)
        else:
            line_end += 1

        if not in_code:
            if pos > prev:
                parts.append((text[prev:pos], False))
            parts.append((text[pos:line_end], True))
            prev = line_end
            in_code = True
        else:
            parts.append((text[prev:line_end], True))
            prev = line_end
            in_code = False

    if prev < len(text):
        parts.append((text[prev:], in_code))

    return parts


def _normalize_line_endings(text: str) -> tuple[str, int]:
    """Convert \\r\\n and \\r to \\n. Returns text and count."""
    crlf_count = text.count("\r\n")
    text = text.replace("\r\n", "\n")

    cr_count = text.count("\r")
    text = text.replace("\r", "\n")

    total = crlf_count + cr_count
    return text, total


def _strip_trailing_ws(text: str) -> tuple[str, int]:
    """Remove trailing whitespace per line. Returns text and count."""
    count = len(_TRAILING_WS.findall(text))
    if count == 0:
        return text, 0
    return _TRAILING_WS.sub("", text), count


def _collapse_newlines_segment(text: str) -> tuple[str, int]:
    """Collapse 3+ newlines to 2 in a non-code segment."""
    count = len(_EXCESS_NEWLINES.findall(text))
    if count == 0:
        return text, 0
    return _EXCESS_NEWLINES.sub("\n\n", text), count


def clean_whitespace(text: str) -> tuple[str, StageResult]:
    """Run Stage 4: normalize whitespace.

    - Normalize line endings (\\r\\n, \\r → \\n)
    - Strip trailing whitespace per line
    - Collapse 3+ newlines to 2 (outside code blocks)
    - Trim document and ensure single trailing newline

    @returns Tuple of (cleaned text, StageResult).
    """
    details: dict[str, int] = {}
    total_changes = 0

    # Normalize line endings first (applies everywhere)
    text, n = _normalize_line_endings(text)
    if n:
        details["crlf_normalized"] = n
        total_changes += n

    # Strip trailing whitespace (applies everywhere)
    text, n = _strip_trailing_ws(text)
    if n:
        details["trailing_whitespace"] = n
        total_changes += n

    # Collapse excessive newlines — protect code blocks
    segments = _split_code_blocks(text)
    result_parts: list[str] = []
    collapse_count = 0

    for segment, is_code in segments:
        if is_code:
            result_parts.append(segment)
        else:
            cleaned, c = _collapse_newlines_segment(segment)
            result_parts.append(cleaned)
            collapse_count += c

    text = "".join(result_parts)
    if collapse_count:
        details["collapsed_newlines"] = collapse_count
        total_changes += collapse_count

    # Trim and ensure single trailing newline
    trimmed = text.strip()
    if trimmed:
        text = trimmed + "\n"
    # Count trimming as a change only if it actually modified the text
    if text != "".join(result_parts):
        was_different = True
    else:
        was_different = False

    if was_different and "trimmed" not in details:
        pass  # Trimming is cosmetic, don't inflate change count

    return text, StageResult(
        stage_name=STAGE_NAME,
        changes_made=total_changes,
        details=details,
    )
