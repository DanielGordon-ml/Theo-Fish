"""
@file main.py
@description CLI entry point for the Theo-Fish ETL extraction pipeline.
Processes single papers or CSV batches through the full pipeline.
"""

import argparse
import asyncio
import logging
import sys
from pathlib import Path

from data_cleaner.pipeline import run_pipeline as clean_paper
from data_loader.config import PROCESSED_DIR, sanitize_arxiv_id
from data_loader.input_reader import read_csv
from data_loader.sdk import load_papers
from graph_builder.config.config import (
    CLEANED_DIR,
    DEFAULT_CONCURRENCY,
    SCHEMA_PATH,
    VAULT_DIR,
)
from graph_builder.config.schema_loader import load_schema
from graph_builder.graph.graph_reader import GraphReader
from graph_builder.graph.neo4j_client import Neo4jClient
from graph_builder.llm.claude_client import ClaudeClient
from graph_builder.llm.llm_client import DeepSeekClient
from graph_builder.orchestrator.orchestrator import PipelineOptions, process_paper
from graph_builder.vault.obsidian_exporter import export_vault

logger = logging.getLogger("graph_builder")

_CSV_HEADER = "arxiv_id"


def _parse_arxiv_ids(
    arxiv_id: str | None,
    csv_path: str | None,
) -> list[str]:
    """Parse paper IDs from CLI arguments.

    @param arxiv_id Single paper ID from positional arg
    @param csv_path Path to CSV or plain text file
    @returns List of arxiv IDs
    @raises SystemExit if no input provided
    """
    if arxiv_id:
        return [arxiv_id]
    if csv_path is None:
        print("Error: provide an arxiv_id or --csv file", file=sys.stderr)
        raise SystemExit(1)
    return _read_id_file(csv_path)


def _read_id_file(path: str) -> list[str]:
    """Read arxiv IDs from a CSV or plain text file.

    Supports two formats:
    - Multi-column CSV with paper_name,file_path,file_type (same as data_loader)
    - Single-column text file with one arxiv ID per line

    @param path Path to the input file
    @returns List of arxiv IDs with blanks stripped
    """
    file_path = Path(path)
    first_line = file_path.read_text(encoding="utf-8").split("\n", 1)[0].strip()

    if "file_path" in first_line:
        papers = read_csv(file_path)
        return [p.arxiv_id for p in papers]

    lines = file_path.read_text(encoding="utf-8").strip().splitlines()
    if not lines:
        return []
    if lines[0].strip() == _CSV_HEADER:
        lines = lines[1:]
    return [line.strip() for line in lines if line.strip()]


def _build_arg_parser() -> argparse.ArgumentParser:
    """Build the CLI argument parser."""
    parser = argparse.ArgumentParser(
        description="Theo-Fish ETL: extract mathematical knowledge from papers",
    )
    parser.add_argument(
        "arxiv_id",
        nargs="?",
        default=None,
        help="ArXiv ID or paper name to process",
    )
    parser.add_argument(
        "--csv",
        dest="csv_path",
        default=None,
        help="Path to CSV or text file with paper IDs",
    )
    parser.add_argument(
        "--from",
        dest="from_stage",
        default="load",
        choices=["load", "clean", "process"],
        help="Start pipeline from this stage (default: load)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-extract even if paper already built",
    )
    parser.add_argument(
        "--concurrency",
        type=int,
        default=DEFAULT_CONCURRENCY,
        help=f"Max parallel LLM calls (default: {DEFAULT_CONCURRENCY})",
    )
    parser.add_argument(
        "--no-export",
        action="store_true",
        help="Skip vault export after processing",
    )
    return parser


async def _load_stage(
    arxiv_id: str | None,
    csv_path: str | None,
    force: bool,
) -> None:
    """Stage 1: Download and convert papers to JSON.

    Non-fatal — failures here don't abort the pipeline.

    @param arxiv_id Single paper ID (positional arg)
    @param csv_path Path to CSV file with paper IDs
    @param force Reprocess even if JSON already exists
    """
    try:
        if csv_path:
            result = await load_papers(
                arxiv_ids=[],
                csv_path=Path(csv_path),
                force=force,
            )
        else:
            result = await load_papers(
                arxiv_ids=[arxiv_id] if arxiv_id else [],
                force=force,
            )
        logger.info(
            "Load: %d processed, %d skipped, %d failed",
            result.processed,
            result.skipped,
            result.failed,
        )
    except Exception:
        logger.exception("Load stage failed — continuing")


def _clean_stage(arxiv_ids: list[str], force: bool) -> None:
    """Stage 2: Clean each paper's processed JSON.

    Skips papers without processed JSON. Non-fatal per paper.

    @param arxiv_ids List of paper identifiers
    @param force Re-clean even if cleaned JSON exists
    """
    for paper_id in arxiv_ids:
        input_path = PROCESSED_DIR / f"{sanitize_arxiv_id(paper_id)}.json"
        if not input_path.exists():
            logger.warning("Clean skip: no processed JSON for %s", paper_id)
            continue
        try:
            report = clean_paper(input_path, CLEANED_DIR, force=force)
            logger.info("Clean %s: %s", paper_id, report.status)
        except Exception:
            logger.exception("Clean failed: %s", paper_id)


async def _process_stage(
    arxiv_ids: list[str],
    args: argparse.Namespace,
) -> tuple[int, int, int]:
    """Stage 3: Build knowledge graph from cleaned JSON.

    @param arxiv_ids List of paper identifiers
    @param args Parsed CLI arguments
    @returns Tuple of (built, skipped, failed) counts
    """
    schema = load_schema(SCHEMA_PATH)
    options = _build_options(schema, args)

    deepseek = DeepSeekClient(concurrency=args.concurrency)
    claude = ClaudeClient(concurrency=args.concurrency)
    neo4j = Neo4jClient()

    try:
        counts = await _process_all(
            arxiv_ids,
            options,
            deepseek,
            claude,
            neo4j,
        )
        if not args.no_export:
            await _export(neo4j)
    finally:
        await neo4j.close()

    return counts


async def _run(args: argparse.Namespace) -> int:
    """Execute the pipeline for all papers and return exit code.

    @param args Parsed CLI arguments
    @returns 0 on success, 1 if any paper failed
    """
    arxiv_ids = _parse_arxiv_ids(args.arxiv_id, args.csv_path)

    # Stage 1: Load
    if args.from_stage == "load":
        await _load_stage(
            arxiv_id=args.arxiv_id,
            csv_path=args.csv_path,
            force=args.force,
        )

    # Stage 2: Clean
    if args.from_stage in ("load", "clean"):
        _clean_stage(arxiv_ids, force=args.force)

    # Stage 3: Build graph
    counts = await _process_stage(arxiv_ids, args)

    _print_summary(counts)
    return 1 if counts[2] > 0 else 0


def _build_options(
    schema,
    args: argparse.Namespace,
) -> PipelineOptions:
    """Construct PipelineOptions from schema and CLI args.

    @param schema Loaded GraphSchema
    @param args Parsed CLI arguments
    @returns Configured PipelineOptions
    """
    return PipelineOptions(
        schema=schema,
        concurrency=args.concurrency,
        force=args.force,
    )


async def _process_all(
    arxiv_ids: list[str],
    options: PipelineOptions,
    deepseek: DeepSeekClient,
    claude: ClaudeClient,
    neo4j: Neo4jClient,
) -> tuple[int, int, int]:
    """Process every paper and return (built, skipped, failed) counts.

    @param arxiv_ids List of paper identifiers
    @param options Pipeline configuration
    @param deepseek DeepSeek LLM client
    @param claude Claude LLM client for claim passes
    @param neo4j Neo4j connection
    @returns Tuple of (built, skipped, failed) counts
    """
    built, skipped, failed = 0, 0, 0
    for paper_id in arxiv_ids:
        logger.info("Processing: %s", paper_id)
        result = await process_paper(
            paper_id,
            options,
            deepseek,
            neo4j,
            claim_llm_client=claude,
        )
        built, skipped, failed = _tally(
            result,
            built,
            skipped,
            failed,
        )
    return built, skipped, failed


async def _export(neo4j: Neo4jClient) -> None:
    """Export the vault after all papers are processed.

    @param neo4j Neo4j client for graph reading
    """
    reader = GraphReader(neo4j)
    await export_vault(VAULT_DIR, reader, neo4j)
    logger.info("Vault exported to %s", VAULT_DIR)


def _tally(
    result,
    built: int,
    skipped: int,
    failed: int,
) -> tuple[int, int, int]:
    """Update counters based on a BuildResult.

    @param result BuildResult from process_paper
    @param built Current built count
    @param skipped Current skipped count
    @param failed Current failed count
    @returns Updated (built, skipped, failed) tuple
    """
    if result.status == "built":
        logger.info("Built: %s", result.arxiv_id)
        return built + 1, skipped, failed
    if result.status == "skipped":
        logger.info("Skipped: %s", result.arxiv_id)
        return built, skipped + 1, failed
    logger.error("Failed: %s — %s", result.arxiv_id, result.error)
    return built, skipped, failed + 1


def _print_summary(counts: tuple[int, int, int]) -> None:
    """Print a one-line summary of pipeline results.

    @param counts Tuple of (built, skipped, failed) counts
    """
    built, skipped, failed = counts
    print(
        f"\nSummary: {built} built, {skipped} skipped, {failed} failed",
    )


def main():
    """CLI entry point."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    parser = _build_arg_parser()
    args = parser.parse_args()
    exit_code = asyncio.run(_run(args))
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
