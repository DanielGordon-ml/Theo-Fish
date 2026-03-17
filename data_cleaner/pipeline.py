"""
@file pipeline.py
@description Orchestration for the cleaning pipeline — single-paper and batch.
"""

import logging
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

from data_loader.config import sanitize_arxiv_id
from data_loader.models import PaperDocument

from data_cleaner.config import CLEANED_DIR, DEFAULT_CONCURRENCY
from data_cleaner.models import CleaningBatchReport, CleaningReport, StageResult
from data_cleaner.stages.newline_normalizer import normalize_newlines
from data_cleaner.stages.latex_normalizer import normalize_latex
from data_cleaner.stages.artifact_remover import remove_artifacts
from data_cleaner.stages.heading_normalizer import normalize_headings
from data_cleaner.stages.whitespace_cleaner import clean_whitespace
from data_cleaner.metadata_repairer import repair_metadata

logger = logging.getLogger("data_cleaner")


def _should_skip(arxiv_id: str, output_dir: Path, force: bool) -> bool:
    """Check if cleaned output already exists."""
    if force:
        return False
    json_file = output_dir / f"{sanitize_arxiv_id(arxiv_id)}.json"
    return json_file.exists()


def _run_text_stage(
    text: str,
    stage_fn,
    **kwargs,
) -> tuple[str, StageResult]:
    """Run a text-transforming stage with error isolation."""
    try:
        return stage_fn(text, **kwargs)
    except Exception as e:
        return text, StageResult(
            stage_name=stage_fn.__module__.rsplit(".", 1)[-1],
            changes_made=0,
            details={},
            error=str(e),
        )


def _write_output(doc: PaperDocument, output_dir: Path) -> Path:
    """Write cleaned PaperDocument to JSON."""
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / f"{sanitize_arxiv_id(doc.arxiv_id)}.json"
    output_file.write_text(
        doc.model_dump_json(indent=2), encoding="utf-8",
    )
    return output_file


def run_pipeline(
    input_path: Path,
    output_dir: Path | None = None,
    force: bool = False,
) -> CleaningReport:
    """Clean a single paper through all 6 stages.

    Reads a PaperDocument JSON, runs stages 0-5, writes cleaned output.

    @returns CleaningReport with per-stage results.
    """
    output_dir = output_dir or CLEANED_DIR
    now = datetime.now(timezone.utc).isoformat()

    # Load input document
    raw = Path(input_path).read_text(encoding="utf-8")
    doc = PaperDocument.model_validate_json(raw)

    # Skip check
    if _should_skip(doc.arxiv_id, output_dir, force):
        return CleaningReport(
            arxiv_id=doc.arxiv_id,
            input_path=str(input_path),
            output_path=str(output_dir / f"{sanitize_arxiv_id(doc.arxiv_id)}.json"),
            stages=[],
            total_changes=0,
            cleaned_at=now,
            status="skipped",
        )

    stages: list[StageResult] = []
    text = doc.extracted_text_markdown

    # Stage 0: Newline normalizer
    text, sr = _run_text_stage(text, normalize_newlines)
    stages.append(sr)

    # Stage 1: LaTeX normalizer
    text, sr = _run_text_stage(text, normalize_latex)
    stages.append(sr)

    # Stage 2: Artifact remover
    text, sr = _run_text_stage(text, remove_artifacts)
    stages.append(sr)

    # Stage 3: Heading normalizer
    text, sr = _run_text_stage(
        text, normalize_headings, converter=doc.converter_used,
    )
    stages.append(sr)

    # Stage 4: Whitespace cleaner
    text, sr = _run_text_stage(text, clean_whitespace)
    stages.append(sr)

    # Update document with cleaned text
    doc = doc.model_copy(update={"extracted_text_markdown": text})

    # Stage 5: Metadata repairer (operates on full document)
    try:
        doc, sr = repair_metadata(doc)
    except Exception as e:
        sr = StageResult(
            stage_name="metadata_repairer",
            changes_made=0,
            details={},
            error=str(e),
        )
    stages.append(sr)

    # Write output
    total_changes = sum(s.changes_made for s in stages)
    output_path = _write_output(doc, output_dir)

    return CleaningReport(
        arxiv_id=doc.arxiv_id,
        input_path=str(input_path),
        output_path=str(output_path),
        stages=stages,
        total_changes=total_changes,
        cleaned_at=now,
        status="cleaned",
    )


def run_batch(
    input_dir: Path,
    output_dir: Path | None = None,
    force: bool = False,
    concurrency: int = DEFAULT_CONCURRENCY,
) -> CleaningBatchReport:
    """Clean all papers in a directory.

    @returns CleaningBatchReport with aggregate statistics.
    """
    output_dir = output_dir or CLEANED_DIR
    input_files = sorted(input_dir.glob("*.json"))

    reports: list[CleaningReport] = []
    cleaned = 0
    skipped = 0
    failed = 0

    def _process_one(path: Path) -> CleaningReport:
        try:
            return run_pipeline(path, output_dir, force=force)
        except Exception as e:
            logger.error(
                "Pipeline failed: %s", str(e),
                extra={"arxiv_id": path.stem},
            )
            return CleaningReport(
                arxiv_id=path.stem,
                input_path=str(path),
                output_path="",
                stages=[],
                total_changes=0,
                cleaned_at=datetime.now(timezone.utc).isoformat(),
                status="failed",
            )

    with ThreadPoolExecutor(max_workers=concurrency) as pool:
        results = pool.map(_process_one, input_files)

    for report in results:
        reports.append(report)
        if report.status == "cleaned":
            cleaned += 1
        elif report.status == "skipped":
            skipped += 1
        else:
            failed += 1

    return CleaningBatchReport(
        total=len(input_files),
        cleaned=cleaned,
        skipped=skipped,
        failed=failed,
        reports=reports,
    )
