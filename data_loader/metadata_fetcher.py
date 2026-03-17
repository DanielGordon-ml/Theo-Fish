"""
@file metadata_fetcher.py
@description Fetch paper metadata from ArXiv API with frontmatter fallback.
"""

import asyncio
import logging
import re
from typing import Any

import feedparser
import httpx

from data_loader.config import ARXIV_API_URL, ARXIV_API_DELAY, ARXIV_API_BATCH_SIZE
from data_loader.models import PaperInput, PaperMetadata

logger = logging.getLogger("data_loader")

# Full mapping of math.* ArXiv categories to human-readable names
MATH_SUBJECTS: dict[str, str] = {
    "math.AC": "Commutative Algebra",
    "math.AG": "Algebraic Geometry",
    "math.AP": "Analysis of PDEs",
    "math.AT": "Algebraic Topology",
    "math.CA": "Classical Analysis and ODEs",
    "math.CO": "Combinatorics",
    "math.CT": "Category Theory",
    "math.CV": "Complex Variables",
    "math.DG": "Differential Geometry",
    "math.DS": "Dynamical Systems",
    "math.FA": "Functional Analysis",
    "math.GM": "General Mathematics",
    "math.GN": "General Topology",
    "math.GR": "Group Theory",
    "math.GT": "Geometric Topology",
    "math.HO": "History and Overview",
    "math.IT": "Information Theory",
    "math.KT": "K-Theory and Homology",
    "math.LO": "Logic",
    "math.MG": "Metric Geometry",
    "math.MP": "Mathematical Physics",
    "math.NA": "Numerical Analysis",
    "math.NT": "Number Theory",
    "math.OA": "Operator Algebras",
    "math.OC": "Optimization and Control",
    "math.PR": "Probability",
    "math.QA": "Quantum Algebra",
    "math.RA": "Rings and Algebras",
    "math.RT": "Representation Theory",
    "math.SG": "Symplectic Geometry",
    "math.SP": "Spectral Theory",
    "math.ST": "Statistics Theory",
    "math-ph": "Mathematical Physics",
}


def build_local_metadata(paper: PaperInput) -> PaperMetadata:
    """Build minimal metadata for a local PDF paper.

    Uses paper_name as title, falling back to arxiv_id (filename stem).
    """
    return PaperMetadata(
        arxiv_id=paper.arxiv_id,
        title=paper.paper_name or paper.arxiv_id,
        source="local",
    )


def get_math_subject(primary_category: str) -> str:
    """Resolve a category code to a human-readable math subject name.

    Returns the raw category code if not in the math mapping.
    """
    return MATH_SUBJECTS.get(primary_category, primary_category)


def parse_arxiv_entry(entry: Any) -> PaperMetadata:
    """Parse a single feedparser entry into PaperMetadata."""
    # Extract ArXiv ID from the entry URL
    raw_id = entry.id  # e.g. "http://arxiv.org/abs/2706.03762v1"
    arxiv_id = re.search(r"abs/(.+?)(?:v\d+)?$", raw_id)
    arxiv_id = arxiv_id.group(1) if arxiv_id else raw_id

    authors = [a.get("name", "") for a in entry.get("authors", [])]
    categories = [t["term"] for t in entry.get("tags", [])]

    primary_category = ""
    if hasattr(entry, "arxiv_primary_category"):
        primary_category = entry.arxiv_primary_category.get("term", "")
    elif categories:
        primary_category = categories[0]

    publication_date = entry.get("published", "")[
        :10
    ]  # "2017-06-12T..." -> "2017-06-12"

    return PaperMetadata(
        arxiv_id=arxiv_id,
        title=entry.get("title", "").replace("\n", " ").strip(),
        authors=authors,
        abstract=entry.get("summary", "").strip(),
        publication_date=publication_date,
        categories=categories,
        primary_category=primary_category,
        math_subject=get_math_subject(primary_category),
        source="arxiv_api",
    )


async def _call_arxiv2md_frontmatter(paper_id: str) -> object:
    """Call arxiv2md for frontmatter extraction. Thin wrapper for monkeypatching."""
    from arxiv2md.ingestion import ingest_paper

    html_url = f"https://arxiv.org/html/{paper_id}"
    result, _metadata = await ingest_paper(
        arxiv_id=paper_id,
        version=None,
        html_url=html_url,
        remove_refs=True,
        remove_toc=False,
        section_filter_mode="include",
        sections=[],
        include_frontmatter=True,
    )
    return result


async def parse_frontmatter_metadata(arxiv_id: str) -> PaperMetadata | None:
    """Extract metadata from arxiv2md's frontmatter as a fallback.

    Calls arxiv2md with frontmatter enabled and parses the YAML header.
    Returns None if extraction fails.
    """
    try:
        result = await _call_arxiv2md_frontmatter(arxiv_id)
        markdown = result.markdown if hasattr(result, "markdown") else str(result)

        # Parse YAML frontmatter if present (between --- delimiters)
        title, authors = "", []
        if markdown.startswith("---"):
            end = markdown.find("---", 3)
            if end != -1:
                frontmatter = markdown[3:end]
                for line in frontmatter.strip().split("\n"):
                    if line.startswith("title:"):
                        title = line[6:].strip().strip('"').strip("'")
                    elif line.startswith("authors:"):
                        # Simple comma-separated parsing
                        authors_str = line[8:].strip().strip("[]")
                        authors = [
                            a.strip().strip('"').strip("'")
                            for a in authors_str.split(",")
                            if a.strip()
                        ]

        return PaperMetadata(
            arxiv_id=arxiv_id,
            title=title,
            authors=authors,
            abstract="",
            publication_date="",
            categories=[],
            primary_category="",
            math_subject="",
            source="frontmatter_fallback",
        )
    except Exception as e:
        logger.warning(
            "Frontmatter metadata extraction failed: %s",
            str(e),
            extra={"arxiv_id": arxiv_id},
        )
        return None


async def _fetch_batch(
    arxiv_ids: list[str],
    client: httpx.AsyncClient,
) -> dict[str, PaperMetadata]:
    """Fetch metadata for a batch of ArXiv IDs (max 20)."""
    id_list = ",".join(arxiv_ids)
    url = f"{ARXIV_API_URL}?id_list={id_list}&max_results={len(arxiv_ids)}"

    try:
        response = await client.get(url, timeout=30.0)
        response.raise_for_status()
    except (httpx.HTTPError, httpx.TimeoutException) as e:
        for aid in arxiv_ids:
            logger.error(
                "ArXiv API request failed: %s",
                str(e),
                extra={"arxiv_id": aid},
            )
        return {}

    feed = feedparser.parse(response.text)
    results: dict[str, PaperMetadata] = {}

    for entry in feed.entries:
        try:
            metadata = parse_arxiv_entry(entry)
            results[metadata.arxiv_id] = metadata
        except Exception as e:
            logger.warning(
                "Failed to parse ArXiv entry: %s",
                str(e),
                extra={"arxiv_id": "unknown"},
            )

    return results


async def fetch_all_metadata(
    papers: list[PaperInput],
    client: httpx.AsyncClient,
) -> dict[str, PaperMetadata]:
    """Fetch metadata for all papers in batches, respecting rate limits.

    Returns a dict mapping arxiv_id -> PaperMetadata.
    Papers not found via the API are omitted from the dict.
    """
    # Only fetch metadata for ArXiv papers, not local PDFs
    arxiv_papers = [p for p in papers if not p.is_local]
    arxiv_ids = [p.arxiv_id for p in arxiv_papers]
    all_metadata: dict[str, PaperMetadata] = {}

    for i in range(0, len(arxiv_ids), ARXIV_API_BATCH_SIZE):
        batch = arxiv_ids[i : i + ARXIV_API_BATCH_SIZE]
        batch_result = await _fetch_batch(batch, client)
        all_metadata.update(batch_result)

        # Rate limit: wait between batches (skip after last batch)
        if i + ARXIV_API_BATCH_SIZE < len(arxiv_ids):
            await asyncio.sleep(ARXIV_API_DELAY)

    return all_metadata
