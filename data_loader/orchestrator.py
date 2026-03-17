"""
@file orchestrator.py
@description Async batch orchestrator for the data loader pipeline.
"""

import asyncio
import logging
from pathlib import Path

import httpx

from data_loader.config import FOR_PROCESS_DIR
from data_loader.json_writer import assemble_document, should_skip, write_document
from data_loader.metadata_fetcher import (
    build_local_metadata,
    fetch_all_metadata,
    parse_frontmatter_metadata,
)
from data_loader.models import PaperInput, PaperResult, BatchResult
from data_loader.paper_converter import convert_local_pdf, convert_paper

logger = logging.getLogger("data_loader")


async def _process_one(
    paper: PaperInput,
    metadata_cache: dict,
    semaphore: asyncio.Semaphore,
    processed_dir: Path,
    papers_dir: Path,
    force: bool,
) -> PaperResult:
    """Process a single paper. Returns a PaperResult with status info."""
    arxiv_id = paper.arxiv_id

    # Skip check
    if should_skip(arxiv_id, processed_dir, force):
        return PaperResult(arxiv_id=arxiv_id, status="skipped")

    # Branch on local vs ArXiv
    if paper.is_local:
        metadata = build_local_metadata(paper)
        async with semaphore:
            conversion = await convert_local_pdf(paper, FOR_PROCESS_DIR)
    else:
        # Check metadata — try API cache first, then frontmatter fallback
        metadata = metadata_cache.get(arxiv_id)
        if metadata is None:
            logger.warning(
                "No API metadata, trying frontmatter fallback",
                extra={"arxiv_id": arxiv_id},
            )
            metadata = await parse_frontmatter_metadata(arxiv_id)
        if metadata is None:
            logger.error(
                "Both API and frontmatter metadata failed — skipping",
                extra={"arxiv_id": arxiv_id},
            )
            return PaperResult(
                arxiv_id=arxiv_id,
                status="failed",
                error="no metadata",
            )

        # Convert (with concurrency limit)
        async with semaphore:
            conversion = await convert_paper(arxiv_id, papers_dir)

    if conversion is None:
        return PaperResult(
            arxiv_id=arxiv_id,
            status="failed",
            error="conversion failed",
        )

    # Assemble and write
    try:
        doc = assemble_document(paper, metadata, conversion)
        output_path = write_document(doc, processed_dir)
        return PaperResult(
            arxiv_id=arxiv_id,
            status="processed",
            converter=conversion.converter_used,
            output_path=str(output_path),
        )
    except Exception as e:
        logger.error(
            "Failed to write document: %s",
            str(e),
            extra={"arxiv_id": arxiv_id},
        )
        return PaperResult(
            arxiv_id=arxiv_id,
            status="failed",
            error=str(e),
        )


async def process_batch(
    papers: list[PaperInput],
    processed_dir: Path,
    papers_dir: Path,
    concurrency: int = 5,
    force: bool = False,
) -> BatchResult:
    """Process a batch of papers concurrently.

    Returns a BatchResult with counts and per-paper results.
    """
    semaphore = asyncio.Semaphore(concurrency)

    # Step 1: Fetch metadata for ArXiv papers only (local papers skip API)
    arxiv_papers = [p for p in papers if not p.is_local]
    async with httpx.AsyncClient(follow_redirects=True) as client:
        metadata_cache = await fetch_all_metadata(arxiv_papers, client)

    # Step 2: Process papers concurrently
    tasks = [
        _process_one(paper, metadata_cache, semaphore, processed_dir, papers_dir, force)
        for paper in papers
    ]
    raw_results = await asyncio.gather(*tasks, return_exceptions=True)

    # Step 3: Build BatchResult
    paper_results: list[PaperResult] = []
    counts = {
        "processed": 0,
        "skipped": 0,
        "failed": 0,
        "arxiv2md": 0,
        "mineru": 0,
    }

    for r in raw_results:
        if isinstance(r, Exception):
            counts["failed"] += 1
            paper_results.append(
                PaperResult(
                    arxiv_id="unknown",
                    status="failed",
                    error=str(r),
                )
            )
            continue

        paper_results.append(r)
        if r.status == "processed":
            counts["processed"] += 1
            if r.converter == "arxiv2md":
                counts["arxiv2md"] += 1
            elif r.converter == "mineru":
                counts["mineru"] += 1
        elif r.status == "skipped":
            counts["skipped"] += 1
        elif r.status == "failed":
            counts["failed"] += 1

    return BatchResult(
        total=len(papers),
        results=paper_results,
        **counts,
    )


def print_summary(batch_result: BatchResult) -> None:
    """Print a human-readable processing summary to stdout."""
    print(f"\nProcessed: {batch_result.processed}/{batch_result.total}")
    if batch_result.arxiv2md:
        print(f"  - arxiv2md: {batch_result.arxiv2md}")
    if batch_result.mineru:
        print(f"  - mineru:   {batch_result.mineru}")
    if batch_result.skipped:
        print(f"Skipped (already exists): {batch_result.skipped}")
    if batch_result.failed:
        print(f"Failed: {batch_result.failed} (see logs/loader.log for details)")
