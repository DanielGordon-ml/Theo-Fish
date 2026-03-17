"""
@file metadata_repairer.py
@description Stage 5: Extract missing metadata (title, authors, abstract, date) from markdown text.
"""

import re

from data_loader.models import PaperDocument

from data_cleaner.models import StageResult

STAGE_NAME = "metadata_repairer"

# First h1 or h2 heading
_FIRST_HEADING = re.compile(r"^#{1,2}\s+(.+)$", re.MULTILINE)

# Abstract section: ## Abstract followed by text until next ##
_ABSTRACT_SECTION = re.compile(
    r"^##?\s+Abstract\s*\n+(.*?)(?=^##?\s|\Z)",
    re.MULTILINE | re.DOTALL,
)

# 4-digit year in range 1900-2099
_YEAR_PATTERN = re.compile(r"\b(19|20)\d{2}\b")

# Common author separators
_AND_SEPARATOR = re.compile(r"\s+and\s+", re.IGNORECASE)


def _is_populated(value: str | list) -> bool:
    """Check if a metadata field has a non-empty value."""
    if isinstance(value, list):
        return len(value) > 0
    return bool(value and value.strip())


def _extract_title(md: str) -> str | None:
    """Extract title from first heading."""
    m = _FIRST_HEADING.search(md)
    if m:
        return m.group(1).strip()
    return None


def _extract_authors(md: str) -> list[str] | None:
    """Extract authors from text between title and Abstract heading.

    Looks for the first non-empty line(s) after the title heading
    and before ## Abstract. Splits on commas and 'and'.
    """
    # Find title heading end
    title_match = _FIRST_HEADING.search(md)
    if not title_match:
        return None

    after_title = md[title_match.end() :]

    # Find Abstract heading
    abstract_match = re.search(r"^##?\s+Abstract", after_title, re.MULTILINE)
    if not abstract_match:
        return None

    between = after_title[: abstract_match.start()].strip()
    if not between:
        return None

    # Take the first non-empty paragraph (may be multi-line)
    first_para = between.split("\n\n")[0].strip()
    if not first_para:
        return None

    # Join multi-line into single line
    first_para = " ".join(first_para.split("\n"))

    # Split on "and" first, then commas
    parts = _AND_SEPARATOR.split(first_para)
    authors: list[str] = []
    for part in parts:
        for name in part.split(","):
            name = name.strip()
            if name:
                authors.append(name)

    # Sanity: skip if any "author" is too long (likely not an author line)
    MAX_AUTHOR_NAME_LEN = 80
    if any(len(a) > MAX_AUTHOR_NAME_LEN for a in authors):
        return None

    return authors if authors else None


def _extract_abstract(md: str) -> str | None:
    """Extract abstract text from ## Abstract section."""
    m = _ABSTRACT_SECTION.search(md)
    if m:
        text = m.group(1).strip()
        return text if text else None
    return None


def _extract_date(md: str) -> str | None:
    """Extract a year from the first 2000 chars of markdown."""
    head = md[:2000]
    m = _YEAR_PATTERN.search(head)
    if m:
        return m.group(0)
    return None


def repair_metadata(doc: PaperDocument) -> tuple[PaperDocument, StageResult]:
    """Run Stage 5: extract missing metadata from markdown text.

    Fills in title, authors, abstract, and publication_date when empty.
    Returns a new PaperDocument (original is not mutated).

    @returns Tuple of (updated PaperDocument, StageResult).
    """
    md = doc.extracted_text_markdown
    details: dict[str, int] = {}
    total_changes = 0

    has_title = _is_populated(doc.title)
    has_authors = _is_populated(doc.authors)
    has_abstract = _is_populated(doc.abstract)
    has_date = _is_populated(doc.publication_date)

    if has_title and has_authors and has_abstract and has_date:
        return doc, StageResult(
            stage_name=STAGE_NAME,
            changes_made=0,
            details={},
            skipped=True,
        )

    updates: dict[str, object] = {}

    if not has_title:
        title = _extract_title(md)
        if title:
            updates["title"] = title
            details["title_extracted"] = 1
            total_changes += 1

    if not has_authors:
        authors = _extract_authors(md)
        if authors:
            updates["authors"] = authors
            details["authors_extracted"] = 1
            total_changes += 1

    if not has_abstract:
        abstract = _extract_abstract(md)
        if abstract:
            updates["abstract"] = abstract
            details["abstract_extracted"] = 1
            total_changes += 1

    if not has_date:
        date = _extract_date(md)
        if date:
            updates["publication_date"] = date
            details["date_extracted"] = 1
            total_changes += 1

    if updates:
        doc = doc.model_copy(update=updates)

    return doc, StageResult(
        stage_name=STAGE_NAME,
        changes_made=total_changes,
        details=details,
    )
