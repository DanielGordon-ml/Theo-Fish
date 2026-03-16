"""
@file input_reader.py
@description Read and normalize paper inputs from CSV files and CLI arguments.
"""

import csv
import re
import logging
from pathlib import Path

from data_loader.models import PaperInput

logger = logging.getLogger("data_loader")

# Matches new-style ArXiv IDs: YYMM.NNNNN (with optional version)
_NEW_ID_RE = re.compile(r"^(\d{4}\.\d{4,5})(v\d+)?$")
# Matches legacy ArXiv IDs: category/NNNNNNN (with optional version)
_LEGACY_ID_RE = re.compile(r"^([a-z-]+/\d{7})(v\d+)?$")
# Extracts ID from ArXiv URLs
_URL_RE = re.compile(r"arxiv\.org/(?:abs|pdf|html)/([a-z-]*/?\d+\.?\d*)(v\d+)?")


def normalize_arxiv_id(raw: str) -> str | None:
    """Normalize an ArXiv identifier to its canonical form (no version suffix).

    Accepts: raw IDs, versioned IDs, full URLs, arxiv:-prefixed IDs.
    Returns None if the input cannot be parsed.
    """
    raw = raw.strip()
    if not raw:
        return None

    # Strip arxiv: prefix
    if raw.lower().startswith("arxiv:"):
        raw = raw[6:]

    # Try URL extraction
    url_match = _URL_RE.search(raw)
    if url_match:
        return url_match.group(1)

    # Try new-style ID
    new_match = _NEW_ID_RE.match(raw)
    if new_match:
        return new_match.group(1)

    # Try legacy ID
    legacy_match = _LEGACY_ID_RE.match(raw)
    if legacy_match:
        return legacy_match.group(1)

    return None


def read_csv(csv_path: Path) -> list[PaperInput]:
    """Read papers from a CSV file with columns: paper_name, file_path, file_type.

    Normalizes ArXiv IDs. Skips rows with invalid IDs (logs warning).
    """
    papers = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            file_path = row["file_path"].strip()

            # Detect local PDF by .pdf extension
            if file_path.lower().endswith(".pdf"):
                stem = Path(file_path).stem
                papers.append(PaperInput(
                    arxiv_id=stem,
                    paper_name=row.get("paper_name") or None,
                    file_type="pdf",
                    is_local=True,
                    local_filename=file_path,
                ))
                continue

            arxiv_id = normalize_arxiv_id(file_path)
            if arxiv_id is None:
                logger.warning(
                    "Skipping invalid ArXiv ID in CSV: %s",
                    file_path,
                    extra={"arxiv_id": file_path},
                )
                continue
            papers.append(PaperInput(
                arxiv_id=arxiv_id,
                paper_name=row.get("paper_name") or None,
                file_type=row.get("file_type") or None,
            ))
    return papers


def read_cli_papers(paper_ids: list[str]) -> list[PaperInput]:
    """Create PaperInput list from CLI --paper arguments.

    Normalizes IDs. Skips invalid ones (logs warning).
    """
    papers = []
    for raw_id in paper_ids:
        arxiv_id = normalize_arxiv_id(raw_id)
        if arxiv_id is None:
            logger.warning(
                "Skipping invalid ArXiv ID from CLI: %s",
                raw_id,
                extra={"arxiv_id": raw_id},
            )
            continue
        papers.append(PaperInput(arxiv_id=arxiv_id))
    return papers


def merge_inputs(
    csv_papers: list[PaperInput],
    cli_papers: list[PaperInput],
) -> list[PaperInput]:
    """Merge CSV and CLI inputs, deduplicating by ArXiv ID.

    CSV entries take priority (they have paper_name and file_type).
    """
    seen: dict[str, PaperInput] = {}
    for paper in csv_papers:
        seen[paper.arxiv_id] = paper
    for paper in cli_papers:
        if paper.arxiv_id not in seen:
            seen[paper.arxiv_id] = paper
    return list(seen.values())
