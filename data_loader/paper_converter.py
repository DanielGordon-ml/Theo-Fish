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

from data_loader.models import PaperInput, ConversionResult

logger = logging.getLogger("data_loader")

# Process pool for CPU-bound MinerU calls
_executor = ProcessPoolExecutor(max_workers=2)


async def _call_arxiv2md(paper_id: str) -> object:
    """Call arxiv2md's ingest_paper. Thin wrapper for monkeypatching."""
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
        include_frontmatter=False,
    )
    return result


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
    from mineru.cli.common import do_parse

    pdf_bytes = Path(pdf_path).read_bytes()
    do_parse(
        output_dir=output_dir,
        pdf_file_names=[Path(pdf_path).name],
        pdf_bytes_list=[pdf_bytes],
        p_lang_list=["en"],
        parse_method="auto",
        f_dump_md=True,
        f_dump_middle_json=False,
        f_dump_model_output=False,
        f_dump_orig_pdf=False,
        f_dump_content_list=False,
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


async def convert_local_pdf(
    paper: PaperInput,
    for_process_dir: Path,
) -> ConversionResult | None:
    """Convert a local PDF file using MinerU directly.

    Reads the PDF from for_process_dir and runs MinerU.
    Returns None if the file is missing or conversion fails.
    """
    pdf_path = for_process_dir / paper.local_filename
    if not pdf_path.exists():
        logger.error(
            "Local PDF not found: %s",
            pdf_path,
            extra={"arxiv_id": paper.arxiv_id},
        )
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
                arxiv_id=paper.arxiv_id,
                markdown_content=markdown,
                converter_used="mineru",
                conversion_warnings=[],
            )
        except Exception as e:
            logger.error(
                "MinerU failed for local PDF %s: %s",
                paper.local_filename,
                str(e),
                extra={"arxiv_id": paper.arxiv_id},
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
