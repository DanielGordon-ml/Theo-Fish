"""
@file paper_converter.py
@description Convert ArXiv papers to markdown using arxiv2md (primary) and MinerU (fallback).
"""

import asyncio
import logging
import tempfile
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import httpx

from data_loader.models import ConversionResult

logger = logging.getLogger("data_loader")

# Process pool for CPU-bound MinerU calls
_executor = ProcessPoolExecutor(max_workers=2)


async def _call_arxiv2md(paper_id: str) -> object:
    """Call arxiv2md's ingest_paper. Thin wrapper for monkeypatching."""
    from arxiv2md.ingestion import ingest_paper
    return await ingest_paper(paper_id)


async def convert_with_arxiv2md(arxiv_id: str) -> ConversionResult | None:
    """Try converting a paper using arxiv2md (HTML-based).

    Returns None if conversion fails.
    """
    try:
        result = await _call_arxiv2md(arxiv_id)
        markdown = result.markdown if hasattr(result, "markdown") else str(result)
        return ConversionResult(
            arxiv_id=arxiv_id,
            markdown_content=markdown,
            converter_used="arxiv2md",
            conversion_warnings=[],
        )
    except Exception as e:
        logger.warning(
            "arxiv2md failed: %s, falling back to MinerU",
            str(e),
            extra={"arxiv_id": arxiv_id},
        )
        return None


def _run_mineru(pdf_path: str, output_dir: str) -> str:
    """Run MinerU in a separate process (CPU-bound).

    This function is called via ProcessPoolExecutor, so it must be
    a top-level function (picklable) and import MinerU inside.
    """
    from pathlib import Path
    # NOTE: mineru.cli.common is an internal API path — may change between MinerU versions.
    # If this import breaks after a MinerU update, check their docs for the new entry point.
    from mineru.cli.common import parse_doc

    parse_doc(
        path_list=[Path(pdf_path)],
        output_dir=output_dir,
        backend="pipeline",
        method="auto",
        lang="en",
    )

    # MinerU writes output to output_dir/<filename>/<filename>.md
    stem = Path(pdf_path).stem
    md_path = Path(output_dir) / stem / f"{stem}.md"
    if md_path.exists():
        return md_path.read_text(encoding="utf-8")
    # Try alternate output patterns
    for md_file in Path(output_dir).rglob("*.md"):
        return md_file.read_text(encoding="utf-8")
    raise FileNotFoundError(f"MinerU produced no markdown output for {pdf_path}")


async def _download_pdf(arxiv_id: str, papers_dir: Path) -> Path | None:
    """Download a PDF from ArXiv to the cache directory.

    Returns the path to the cached PDF, or None on failure.
    Skips download if the file already exists.
    """
    from data_loader.config import sanitize_arxiv_id
    pdf_path = papers_dir / f"{sanitize_arxiv_id(arxiv_id)}.pdf"
    if pdf_path.exists():
        return pdf_path

    papers_dir.mkdir(parents=True, exist_ok=True)
    url = f"https://arxiv.org/pdf/{arxiv_id}"

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, follow_redirects=True, timeout=60.0)
            response.raise_for_status()
            pdf_path.write_bytes(response.content)
            return pdf_path
    except (httpx.HTTPError, httpx.TimeoutException) as e:
        logger.error(
            "PDF download failed: %s",
            str(e),
            extra={"arxiv_id": arxiv_id},
        )
        return None


async def convert_with_mineru(
    arxiv_id: str,
    papers_dir: Path,
) -> ConversionResult | None:
    """Try converting a paper using MinerU (PDF-based fallback).

    Downloads the PDF if not cached, then runs MinerU via ProcessPoolExecutor.
    Returns None if conversion fails.
    """
    pdf_path = await _download_pdf(arxiv_id, papers_dir)
    if pdf_path is None:
        return None

    loop = asyncio.get_running_loop()
    with tempfile.TemporaryDirectory() as tmp_out:
        try:
            markdown = await loop.run_in_executor(
                _executor,
                _run_mineru,
                str(pdf_path),
                tmp_out,
            )
            return ConversionResult(
                arxiv_id=arxiv_id,
                markdown_content=markdown,
                converter_used="mineru",
                conversion_warnings=[],
            )
        except Exception as e:
            logger.error(
                "MinerU conversion failed: %s",
                str(e),
                extra={"arxiv_id": arxiv_id},
            )
            return None


async def convert_paper(
    arxiv_id: str,
    papers_dir: Path,
) -> ConversionResult | None:
    """Convert a paper using arxiv2md, falling back to MinerU.

    Returns None if both converters fail.
    """
    result = await convert_with_arxiv2md(arxiv_id)
    if result is not None:
        return result

    result = await convert_with_mineru(arxiv_id, papers_dir)
    if result is not None:
        return result

    logger.error(
        "Both converters failed — skipping paper",
        extra={"arxiv_id": arxiv_id},
    )
    return None
