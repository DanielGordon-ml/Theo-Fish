"""
@file section_splitter.py
@description TOC stripping, heading-based splitting, and stub detection.
"""

import re

from graph_builder.config.config import MAX_SECTION_CHARS, MIN_SECTION_CHARS
from graph_builder.models.section import Section

# Matches TOC headings like "# Contents" or "# Table of Contents"
_TOC_HEADING_RE = re.compile(
    r"^#\s+(Contents|Table of Contents)\s*$",
    re.MULTILINE | re.IGNORECASE,
)

# Matches any markdown heading (H1-H6)
_HEADING_RE = re.compile(r"^(#{1,6})\s+(.+)$", re.MULTILINE)

# Matches H1 or H2 headings only
_H1_H2_RE = re.compile(r"^(#{1,2})\s+(.+)$", re.MULTILINE)

# Matches H3 headings
_H3_RE = re.compile(r"^(###)\s+(.+)$", re.MULTILINE)


def strip_toc(text: str) -> str:
    """Remove Table of Contents block from markdown text.

    Detects a heading like '# Contents' followed by list items, and strips
    everything up to the next non-TOC heading.
    """
    match = _TOC_HEADING_RE.search(text)
    if match is None:
        return text

    toc_start = match.start()
    # Find the next heading after the TOC
    rest = text[match.end() :]
    next_heading = _HEADING_RE.search(rest)
    if next_heading is None:
        return text[:toc_start].rstrip()

    toc_end = match.end() + next_heading.start()
    return (text[:toc_start].rstrip() + "\n\n" + text[toc_end:]).strip()


def is_stub_section(content: str) -> bool:
    """Return True if content has fewer than MIN_SECTION_CHARS non-whitespace chars."""
    return len(content.strip()) < MIN_SECTION_CHARS


def _split_on_pattern(text: str, pattern: re.Pattern) -> list[Section]:
    """Split text into sections based on a heading regex pattern."""
    matches = list(pattern.finditer(text))
    if not matches:
        return _make_single_section(text)

    sections: list[Section] = []
    # Content before the first heading
    preamble = text[: matches[0].start()].strip()
    if preamble and not is_stub_section(preamble):
        sections.append(_build_section("", 0, preamble, len(sections)))

    for i, match in enumerate(matches):
        level = len(match.group(1))
        heading = match.group(2).strip()
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        content = text[start:end].strip()

        if is_stub_section(content):
            continue
        sections.append(_build_section(heading, level, content, len(sections)))

    return sections


def _make_single_section(text: str) -> list[Section]:
    """Wrap entire text as a single section if no headings found."""
    content = text.strip()
    if is_stub_section(content):
        return []
    return [_build_section("", 0, content, 0)]


def _build_section(
    heading: str,
    level: int,
    content: str,
    index: int,
) -> Section:
    """Construct a Section model from components."""
    return Section(
        heading=heading,
        level=level,
        content=content,
        char_count=len(content),
        index=index,
    )


def _subsplit_large_section(section: Section) -> list[Section]:
    """Split an oversized section on H3 boundaries, then paragraphs."""
    h3_sections = _split_on_pattern(section.content, _H3_RE)
    if len(h3_sections) > 1:
        return h3_sections

    # Fallback: split on double-newline paragraph boundaries
    return _split_on_paragraphs(section)


def _split_on_paragraphs(section: Section) -> list[Section]:
    """Split a section into paragraph-based chunks under the size limit."""
    paragraphs = re.split(r"\n{2,}", section.content)
    chunks: list[Section] = []
    current_parts: list[str] = []
    current_len = 0

    for para in paragraphs:
        para_len = len(para)
        if current_len + para_len > MAX_SECTION_CHARS and current_parts:
            content = "\n\n".join(current_parts)
            chunks.append(
                _build_section(
                    section.heading,
                    section.level,
                    content,
                    len(chunks),
                )
            )
            current_parts = []
            current_len = 0
        current_parts.append(para)
        current_len += para_len

    if current_parts:
        content = "\n\n".join(current_parts)
        if not is_stub_section(content):
            chunks.append(
                _build_section(
                    section.heading,
                    section.level,
                    content,
                    len(chunks),
                )
            )

    return chunks if chunks else [section]


def split_into_sections(text: str) -> list[Section]:
    """Split markdown text into sections on H1/H2 boundaries.

    Strips TOC, filters stubs, and sub-splits oversized sections.
    """
    cleaned = strip_toc(text)
    sections = _split_on_pattern(cleaned, _H1_H2_RE)

    # Sub-split oversized sections
    result: list[Section] = []
    for section in sections:
        if section.char_count > MAX_SECTION_CHARS:
            result.extend(_subsplit_large_section(section))
        else:
            result.append(section)

    # Re-index after splitting
    for i, section in enumerate(result):
        result[i] = _build_section(
            section.heading,
            section.level,
            section.content,
            i,
        )

    return result
