"""
@file artifact_remover.py
@description Stage 2: Strip HTML tags, broken refs, and footnote markers.
"""

import re

from data_cleaner.models import StageResult

STAGE_NAME = "artifact_remover"

# HTML table block: <table>...</table>
_TABLE_BLOCK = re.compile(r"<table[^>]*>.*?</table>", re.DOTALL | re.IGNORECASE)
_TABLE_ROW = re.compile(r"<tr[^>]*>(.*?)</tr>", re.DOTALL | re.IGNORECASE)
_TABLE_HEADER = re.compile(r"<th[^>]*>(.*?)</th>", re.DOTALL | re.IGNORECASE)
_TABLE_CELL = re.compile(r"<td[^>]*>(.*?)</td>", re.DOTALL | re.IGNORECASE)

# <br> and <br/> variants
_BR_TAG = re.compile(r"<br\s*/?>", re.IGNORECASE)

# Tags to unwrap (keep content, remove tags)
_UNWRAP_TAGS = re.compile(
    r"</?(?:span|div|font|em|strong|b|i|u|sup|sub)[^>]*>", re.IGNORECASE
)

# ArXiv cross-reference links
_ARXIV_LINK = re.compile(r"\[([^\]]*)\]\(https?://arxiv\.org/html/[^)]+\)")

# Broken reference markers
_BROKEN_REF = re.compile(r"\[\?\]")

# Non-breaking space
_NBSP = "\xa0"


def _html_table_to_markdown(match: re.Match) -> str:
    """Convert a single HTML table match to markdown pipe table."""
    table_html = match.group(0)
    rows = _TABLE_ROW.findall(table_html)
    if not rows:
        return ""

    md_rows: list[str] = []
    has_header = False

    for i, row_html in enumerate(rows):
        headers = _TABLE_HEADER.findall(row_html)
        cells = _TABLE_CELL.findall(row_html)

        if headers:
            has_header = True
            values = [h.strip() for h in headers]
        else:
            values = [c.strip() for c in cells]

        md_rows.append("| " + " | ".join(values) + " |")

        # Add separator after header row
        if headers and i == 0:
            md_rows.append("| " + " | ".join("---" for _ in values) + " |")

    # If no th elements, add separator after first row
    if not has_header and md_rows:
        first_row = md_rows[0]
        col_count = first_row.count("|") - 1
        md_rows.insert(1, "| " + " | ".join("---" for _ in range(col_count)) + " |")

    return "\n".join(md_rows)


def _convert_tables(text: str) -> tuple[str, int]:
    """Convert all HTML tables to markdown. Returns text and count."""
    count = len(_TABLE_BLOCK.findall(text))
    if count == 0:
        return text, 0
    return _TABLE_BLOCK.sub(_html_table_to_markdown, text), count


def _replace_br_tags(text: str) -> tuple[str, int]:
    """Replace <br> tags with newlines. Returns text and count."""
    count = len(_BR_TAG.findall(text))
    if count == 0:
        return text, 0
    return _BR_TAG.sub("\n", text), count


def _unwrap_tags(text: str) -> tuple[str, int]:
    """Remove HTML wrapper tags, keeping content. Returns text and count."""
    count = len(_UNWRAP_TAGS.findall(text))
    if count == 0:
        return text, 0
    return _UNWRAP_TAGS.sub("", text), count


def _simplify_arxiv_links(text: str) -> tuple[str, int]:
    """Replace ArXiv HTML cross-ref links with just the text."""
    count = len(_ARXIV_LINK.findall(text))
    if count == 0:
        return text, 0
    return _ARXIV_LINK.sub(r"\1", text), count


def _remove_broken_refs(text: str) -> tuple[str, int]:
    """Remove [?] broken reference markers."""
    count = len(_BROKEN_REF.findall(text))
    if count == 0:
        return text, 0
    return _BROKEN_REF.sub("", text), count


def _replace_nbsp(text: str) -> tuple[str, int]:
    """Replace non-breaking spaces with regular spaces."""
    count = text.count(_NBSP)
    if count == 0:
        return text, 0
    return text.replace(_NBSP, " "), count


def remove_artifacts(text: str) -> tuple[str, StageResult]:
    """Run Stage 2: remove HTML artifacts and broken references.

    @returns Tuple of (cleaned text, StageResult).
    """
    details: dict[str, int] = {}
    total_changes = 0

    text, n = _convert_tables(text)
    if n:
        details["tables_converted"] = n
        total_changes += n

    text, n = _replace_br_tags(text)
    if n:
        details["br_tags"] = n
        total_changes += n

    text, n = _unwrap_tags(text)
    if n:
        details["tags_unwrapped"] = n
        total_changes += n

    text, n = _simplify_arxiv_links(text)
    if n:
        details["arxiv_links"] = n
        total_changes += n

    text, n = _remove_broken_refs(text)
    if n:
        details["broken_refs"] = n
        total_changes += n

    text, n = _replace_nbsp(text)
    if n:
        details["nbsp"] = n
        total_changes += n

    return text, StageResult(
        stage_name=STAGE_NAME,
        changes_made=total_changes,
        details=details,
    )
