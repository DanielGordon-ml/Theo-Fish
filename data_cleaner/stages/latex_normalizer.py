"""
@file latex_normalizer.py
@description Stage 1: Standardize LaTeX delimiters to $...$ and $$...$$.
"""

import re

from data_cleaner.models import StageResult

STAGE_NAME = "latex_normalizer"

# Fenced code block boundaries
_CODE_FENCE = re.compile(r"^```", re.MULTILINE)

# Inline code spans — match `...` but not ``...``
_INLINE_CODE = re.compile(r"`[^`]+`")

# \(...\) → $...$  (non-greedy, single-line)
_INLINE_PAREN = re.compile(r"\\\((.+?)\\\)")

# \[...\] → $$...$$ (non-greedy, may span lines)
_DISPLAY_BRACKET = re.compile(r"\\\[(.*?)\\\]", re.DOTALL)


def _split_code_blocks(text: str) -> list[tuple[str, bool]]:
    """Split text into segments, marking code blocks.

    Returns list of (segment, is_code) tuples.
    """
    parts: list[tuple[str, bool]] = []
    fence_positions = [m.start() for m in _CODE_FENCE.finditer(text)]

    if not fence_positions:
        return [(text, False)]

    prev = 0
    in_code = False
    for pos in fence_positions:
        # Find end of the ``` line
        line_end = text.find("\n", pos)
        if line_end == -1:
            line_end = len(text)
        else:
            line_end += 1  # include the newline

        if not in_code:
            # Text before the opening fence
            if pos > prev:
                parts.append((text[prev:pos], False))
            # The fence line itself
            parts.append((text[pos:line_end], True))
            prev = line_end
            in_code = True
        else:
            # Everything from prev to end of closing fence
            parts.append((text[prev:line_end], True))
            prev = line_end
            in_code = False

    # Remaining text after last fence
    if prev < len(text):
        parts.append((text[prev:], in_code))

    return parts


def _protect_inline_code(segment: str) -> tuple[str, list[str]]:
    """Replace inline code spans with placeholders.

    Returns the modified text and list of original spans.
    """
    spans: list[str] = []

    def _replace(m: re.Match) -> str:
        spans.append(m.group(0))
        return f"\x00ICODE{len(spans) - 1}\x00"

    return _INLINE_CODE.sub(_replace, segment), spans


def _restore_inline_code(text: str, spans: list[str]) -> str:
    """Restore inline code placeholders."""
    for i, span in enumerate(spans):
        text = text.replace(f"\x00ICODE{i}\x00", span)
    return text


def _convert_segment(text: str) -> tuple[str, int, int]:
    """Convert LaTeX delimiters in a non-code segment.

    Returns (converted text, inline_count, display_count).
    """
    # Protect inline code spans
    text, code_spans = _protect_inline_code(text)

    inline_count = len(_INLINE_PAREN.findall(text))
    text = _INLINE_PAREN.sub(r"$\1$", text)

    display_count = len(_DISPLAY_BRACKET.findall(text))
    text = _DISPLAY_BRACKET.sub(r"$$\1$$", text)

    text = _restore_inline_code(text, code_spans)
    return text, inline_count, display_count


def normalize_latex(text: str) -> tuple[str, StageResult]:
    """Run Stage 1: standardize LaTeX delimiters.

    Converts \\(...\\) to $...$ and \\[...\\] to $$...$$.
    Protects code blocks and inline code from transformation.

    @returns Tuple of (cleaned text, StageResult).
    """
    segments = _split_code_blocks(text)
    total_inline = 0
    total_display = 0
    result_parts: list[str] = []

    for segment, is_code in segments:
        if is_code:
            result_parts.append(segment)
        else:
            converted, ic, dc = _convert_segment(segment)
            result_parts.append(converted)
            total_inline += ic
            total_display += dc

    details: dict[str, int] = {}
    total_changes = total_inline + total_display
    if total_inline:
        details["inline_converted"] = total_inline
    if total_display:
        details["display_converted"] = total_display

    return "".join(result_parts), StageResult(
        stage_name=STAGE_NAME,
        changes_made=total_changes,
        details=details,
    )
