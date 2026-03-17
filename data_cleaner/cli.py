"""
@file cli.py
@description CLI interface for the data cleaner pipeline.
"""

import argparse
import sys
from pathlib import Path

from data_loader.config import sanitize_arxiv_id

from data_cleaner.config import CLEANED_DIR, DEFAULT_CONCURRENCY
from data_cleaner.logger import setup_logger
from data_cleaner.pipeline import run_batch, run_pipeline


def build_parser() -> argparse.ArgumentParser:
    """Build the argument parser for the data cleaner CLI."""
    parser = argparse.ArgumentParser(
        prog="data_cleaner",
        description="Clean and normalize processed paper documents.",
    )
    parser.add_argument(
        "--input",
        default=None,
        help="Input directory (default: Data/processed)",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Output directory (default: Data/cleaned)",
    )
    parser.add_argument(
        "--paper",
        default=None,
        help="Clean a single paper by ArXiv ID",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-clean even if output exists",
    )
    parser.add_argument(
        "--concurrency",
        type=int,
        default=DEFAULT_CONCURRENCY,
        help=f"Max parallel workers (default: {DEFAULT_CONCURRENCY})",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """Run the data cleaner CLI.

    @returns Exit code: 0 on success, 1 on failure.
    """
    setup_logger()
    parser = build_parser()
    args = parser.parse_args(argv)

    # Resolve directories
    from data_loader.config import DATA_DIR

    input_dir = Path(args.input) if args.input else DATA_DIR / "processed"
    output_dir = Path(args.output) if args.output else CLEANED_DIR

    if args.paper:
        # Single-paper mode
        filename = f"{sanitize_arxiv_id(args.paper)}.json"
        input_path = input_dir / filename
        if not input_path.exists():
            print(f"Error: {input_path} not found", file=sys.stderr)
            return 1

        report = run_pipeline(input_path, output_dir, force=args.force)
        print(f"[{report.status}] {report.arxiv_id} — {report.total_changes} changes")
        return 0

    # Batch mode
    if not input_dir.exists():
        print(f"Error: {input_dir} not found", file=sys.stderr)
        return 1

    batch = run_batch(
        input_dir,
        output_dir,
        force=args.force,
        concurrency=args.concurrency,
    )

    print(
        f"Cleaned: {batch.cleaned}  Skipped: {batch.skipped}  Failed: {batch.failed}  Total: {batch.total}"
    )

    for report in batch.reports:
        status_char = {"cleaned": "+", "skipped": "~", "failed": "!"}
        char = status_char.get(report.status, "?")
        print(f"  [{char}] {report.arxiv_id} — {report.total_changes} changes")

    return 1 if batch.failed > 0 else 0
