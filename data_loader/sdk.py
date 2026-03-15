"""
@file sdk.py
@description High-level Python API for the data loader.
"""

from pathlib import Path

from data_loader.config import (
    DEFAULT_CONCURRENCY,
    PAPERS_DIR,
    PROCESSED_DIR,
    sanitize_arxiv_id,
)
from data_loader.errors import LoaderError
from data_loader.input_reader import normalize_arxiv_id, read_csv, merge_inputs
from data_loader.logger import setup_logger
from data_loader.models import BatchResult, PaperInput, PaperResult
from data_loader.orchestrator import process_batch

_logger_initialized = False


def _ensure_logger() -> None:
    """Initialize the logger once on first SDK call."""
    global _logger_initialized
    if not _logger_initialized:
        setup_logger()
        _logger_initialized = True


async def load_paper(
    arxiv_id: str,
    output_dir: Path | None = None,
    papers_dir: Path | None = None,
    force: bool = False,
) -> PaperResult:
    """Load a single paper. Raises LoaderError on failure.

    @param arxiv_id ArXiv ID, URL, or arxiv:-prefixed ID
    @param output_dir Directory for output JSON (default: Data/processed)
    @param papers_dir Directory for cached PDFs (default: Data/papers)
    @param force Reprocess even if JSON already exists
    @raises LoaderError if normalization or processing fails
    """
    _ensure_logger()

    normalized = normalize_arxiv_id(arxiv_id)
    if normalized is None:
        raise LoaderError(arxiv_id=arxiv_id, reason="invalid ArXiv ID")

    papers = [PaperInput(arxiv_id=normalized)]
    result = await process_batch(
        papers=papers,
        processed_dir=output_dir or PROCESSED_DIR,
        papers_dir=papers_dir or PAPERS_DIR,
        concurrency=1,
        force=force,
    )

    paper_result = result.results[0]
    if paper_result.status == "failed":
        raise LoaderError(
            arxiv_id=normalized,
            reason=paper_result.error or "unknown error",
        )

    return paper_result


async def load_papers(
    arxiv_ids: list[str],
    csv_path: Path | None = None,
    output_dir: Path | None = None,
    papers_dir: Path | None = None,
    concurrency: int = DEFAULT_CONCURRENCY,
    force: bool = False,
) -> BatchResult:
    """Load multiple papers. Never raises — failures captured in BatchResult.

    @param arxiv_ids List of ArXiv IDs, URLs, or arxiv:-prefixed IDs
    @param csv_path Optional CSV file with paper_name, file_path, file_type
    @param output_dir Directory for output JSON (default: Data/processed)
    @param papers_dir Directory for cached PDFs (default: Data/papers)
    @param concurrency Max concurrent paper conversions
    @param force Reprocess even if JSON already exists
    """
    _ensure_logger()

    # Build paper list from IDs
    cli_papers = []
    for raw_id in arxiv_ids:
        normalized = normalize_arxiv_id(raw_id)
        if normalized is not None:
            cli_papers.append(PaperInput(arxiv_id=normalized))

    # Optionally merge with CSV
    csv_papers = read_csv(csv_path) if csv_path else []
    papers = merge_inputs(csv_papers, cli_papers)

    return await process_batch(
        papers=papers,
        processed_dir=output_dir or PROCESSED_DIR,
        papers_dir=papers_dir or PAPERS_DIR,
        concurrency=concurrency,
        force=force,
    )


def is_processed(arxiv_id: str, output_dir: Path | None = None) -> bool:
    """Check if a paper's JSON already exists on disk.

    @param arxiv_id The canonical ArXiv ID
    @param output_dir Directory to check (default: Data/processed)
    """
    processed_dir = output_dir or PROCESSED_DIR
    json_file = processed_dir / f"{sanitize_arxiv_id(arxiv_id)}.json"
    return json_file.exists()
