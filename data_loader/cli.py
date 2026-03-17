"""
@file cli.py
@description CLI entry point for the data loader.
"""

import argparse
import asyncio
import sys
from pathlib import Path

from data_loader.config import PROCESSED_DIR, PAPERS_DIR, DEFAULT_CONCURRENCY
from data_loader.orchestrator import print_summary
from data_loader.sdk import load_papers


def build_parser() -> argparse.ArgumentParser:
    """Build the argument parser for the data loader CLI."""
    parser = argparse.ArgumentParser(
        prog="data_loader",
        description="Load ArXiv papers into structured JSON.",
    )
    parser.add_argument(
        "--csv",
        type=Path,
        help="Path to CSV file with paper_name, file_path, file_type columns",
    )
    parser.add_argument(
        "--paper",
        action="append",
        default=[],
        help="ArXiv ID or URL to process (can be repeated)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=PROCESSED_DIR,
        help=f"Output directory for JSON files (default: {PROCESSED_DIR})",
    )
    parser.add_argument(
        "--papers-dir",
        type=Path,
        default=PAPERS_DIR,
        help=f"Directory for cached PDFs (default: {PAPERS_DIR})",
    )
    parser.add_argument(
        "--concurrency",
        type=int,
        default=DEFAULT_CONCURRENCY,
        help=f"Max concurrent paper conversions (default: {DEFAULT_CONCURRENCY})",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Reprocess papers even if JSON already exists",
    )
    return parser


def main() -> None:
    """Run the data loader CLI."""
    parser = build_parser()
    args = parser.parse_args()

    if not args.csv and not args.paper:
        parser.error("Provide at least one of --csv or --paper")

    print("Processing paper(s)...")

    # Run pipeline via SDK
    batch_result = asyncio.run(
        load_papers(
            arxiv_ids=args.paper,
            csv_path=args.csv,
            output_dir=args.output,
            papers_dir=args.papers_dir,
            concurrency=args.concurrency,
            force=args.force,
        )
    )

    print_summary(batch_result)

    # Exit with error code if any failures
    if batch_result.failed > 0:
        sys.exit(1)
