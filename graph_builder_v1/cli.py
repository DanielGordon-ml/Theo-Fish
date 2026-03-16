"""
@file cli.py
@description CLI entry point for the knowledge graph builder.
"""

import argparse
import asyncio
import sys
from pathlib import Path

from graph_builder.config import CLEANED_DIR, DEFAULT_CONCURRENCY, VAULT_DIR
from graph_builder.orchestrator import print_summary
from graph_builder.sdk import build_graph, build_graphs


def build_parser() -> argparse.ArgumentParser:
    """Build the argument parser for the graph builder CLI."""
    parser = argparse.ArgumentParser(
        prog="graph_builder",
        description="Build knowledge graphs from cleaned ArXiv papers.",
    )
    parser.add_argument(
        "--paper",
        type=str,
        help="ArXiv ID of a single paper to process",
    )
    parser.add_argument(
        "--input-dir",
        type=Path,
        default=CLEANED_DIR,
        help=f"Input directory with cleaned JSON files (default: {CLEANED_DIR})",
    )
    parser.add_argument(
        "--vault-dir",
        type=Path,
        default=VAULT_DIR,
        help=f"Output vault directory (default: {VAULT_DIR})",
    )
    parser.add_argument(
        "--concurrency",
        type=int,
        default=DEFAULT_CONCURRENCY,
        help=f"Max concurrent LLM calls (default: {DEFAULT_CONCURRENCY})",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Reprocess papers even if vault folder exists",
    )
    parser.add_argument(
        "--no-thinking",
        action="store_true",
        help="Disable LLM thinking mode for faster processing",
    )
    return parser


def main() -> None:
    """Run the graph builder CLI."""
    parser = build_parser()
    args = parser.parse_args()

    if not args.paper and args.input_dir == CLEANED_DIR:
        # Process all papers in the default cleaned directory
        pass
    elif not args.paper and not args.input_dir.exists():
        parser.error(f"Input directory does not exist: {args.input_dir}")

    print("Building knowledge graphs...")

    if args.paper:
        # Single paper mode
        thinking = not args.no_thinking

        try:
            result = asyncio.run(build_graph(
                arxiv_id=args.paper,
                input_dir=args.input_dir,
                vault_dir=args.vault_dir,
                force=args.force,
                thinking=thinking,
            ))
            print(
                f"\n{args.paper}: {result.entity_count} entities, "
                f"{result.relationship_count} relationships",
            )
        except Exception as err:
            print(f"\nFailed: {err}", file=sys.stderr)
            sys.exit(1)
    else:
        # Batch mode
        thinking = not args.no_thinking

        batch_result = asyncio.run(build_graphs(
            input_dir=args.input_dir,
            vault_dir=args.vault_dir,
            concurrency=args.concurrency,
            force=args.force,
            thinking=thinking,
        ))
        print_summary(batch_result)
        if batch_result.failed > 0:
            sys.exit(1)
