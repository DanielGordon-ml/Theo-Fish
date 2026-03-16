"""
@file cli.py
@description CLI entry point for the v2 dual-graph knowledge graph builder.
Supports single-paper processing, batch directory processing, vault export,
and vault sync-back operations.
"""

import argparse
import asyncio
import logging
import sys
from pathlib import Path

from graph_builder.config.config import (
    CLEANED_DIR,
    DEFAULT_CONCURRENCY,
    DEEPSEEK_API_KEY,
    LLM_THINKING,
    NEO4J_AUTH_PASS,
    NEO4J_AUTH_USER,
    NEO4J_BOLT_URI,
    SCHEMA_PATH,
    VAULT_DIR,
)
from graph_builder.config.schema_loader import load_schema

logger = logging.getLogger("graph_builder")


# ---------------------------------------------------------------------------
# Parser
# ---------------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    """Build the CLI argument parser for the v2 graph builder.

    @returns Configured ArgumentParser instance
    """
    parser = argparse.ArgumentParser(
        prog="graph_builder",
        description="v2 dual-graph knowledge graph builder for ArXiv math papers.",
    )

    # Action flags (mutually exclusive in practice, enforced post-parse)
    action = parser.add_argument_group("actions (at least one required)")
    action.add_argument(
        "--paper",
        metavar="ARXIV_ID",
        help="Process a single paper by ArXiv ID.",
    )
    action.add_argument(
        "--input-dir",
        dest="input_dir",
        type=Path,
        metavar="DIR",
        help="Process all papers in DIR (batch mode).",
    )
    action.add_argument(
        "--export",
        action="store_true",
        default=False,
        help="Export the full Neo4j graph to the Obsidian vault.",
    )
    action.add_argument(
        "--sync-back",
        dest="sync_back",
        action="store_true",
        default=False,
        help="Sync human-edited vault fields back to Neo4j.",
    )

    # Modifier flags
    parser.add_argument(
        "--force",
        action="store_true",
        default=False,
        help="Re-process papers that are already built.",
    )
    parser.add_argument(
        "--concurrency",
        type=int,
        default=DEFAULT_CONCURRENCY,
        metavar="N",
        help=f"Max parallel LLM calls (default: {DEFAULT_CONCURRENCY}).",
    )
    parser.add_argument(
        "--no-thinking",
        dest="no_thinking",
        action="store_true",
        default=False,
        help="Disable chain-of-thought thinking in the LLM.",
    )
    parser.add_argument(
        "--dry-run",
        dest="dry_run",
        action="store_true",
        default=False,
        help="Preview sync-back changes without writing to Neo4j.",
    )

    return parser


def _validate_args(
    parser: argparse.ArgumentParser,
    args: argparse.Namespace,
) -> None:
    """Error out if no action flag was provided.

    @param parser ArgumentParser to call error() on
    @param args Parsed namespace to inspect
    """
    has_action = bool(args.paper or args.input_dir or args.export or args.sync_back)
    if not has_action:
        parser.error(
            "Provide at least one action flag: "
            "--paper, --input-dir, --export, or --sync-back."
        )


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main() -> None:
    """CLI entry point for the v2 graph builder.

    Parses arguments, validates them, then dispatches to the appropriate
    async action via asyncio.run().
    """
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    parser = build_parser()
    args = parser.parse_args()
    _validate_args(parser, args)
    asyncio.run(_run(args))


async def _run(args: argparse.Namespace) -> None:
    """Execute the requested action based on parsed CLI arguments.

    Dispatches to --paper, --input-dir, --export, or --sync-back handlers.
    Actions may be combined (e.g. --input-dir + --export).

    @param args Parsed argument namespace from build_parser()
    """
    schema = load_schema(SCHEMA_PATH)

    if args.paper:
        await _run_paper(args, schema)
    elif args.input_dir:
        await _run_batch(args, schema)

    if args.export:
        await _run_export(args)

    if args.sync_back:
        await _run_sync_back(args)


async def _run_paper(
    args: argparse.Namespace,
    schema,
) -> None:
    """Process a single paper by ArXiv ID.

    @param args Parsed CLI arguments
    @param schema Loaded graph schema
    """
    from graph_builder.graph.neo4j_client import Neo4jClient
    from graph_builder.llm.llm_client import DeepSeekClient
    from graph_builder.orchestrator.orchestrator import PipelineOptions, process_paper

    thinking = LLM_THINKING and not args.no_thinking
    options = PipelineOptions(
        schema=schema,
        concurrency=args.concurrency,
        force=args.force,
        thinking=thinking,
    )

    async with Neo4jClient(NEO4J_BOLT_URI, NEO4J_AUTH_USER, NEO4J_AUTH_PASS) as neo4j:
        llm = DeepSeekClient(api_key=DEEPSEEK_API_KEY, thinking=thinking)
        result = await process_paper(args.paper, options, llm, neo4j)

    _log_result(result)


async def _run_batch(
    args: argparse.Namespace,
    schema,
) -> None:
    """Process all papers found in the specified input directory.

    @param args Parsed CLI arguments
    @param schema Loaded graph schema
    """
    from graph_builder.graph.neo4j_client import Neo4jClient
    from graph_builder.llm.llm_client import DeepSeekClient
    from graph_builder.orchestrator.batch_processor import process_batch
    from graph_builder.orchestrator.orchestrator import PipelineOptions

    thinking = LLM_THINKING and not args.no_thinking
    options = PipelineOptions(
        schema=schema,
        concurrency=args.concurrency,
        force=args.force,
        thinking=thinking,
    )

    async with Neo4jClient(NEO4J_BOLT_URI, NEO4J_AUTH_USER, NEO4J_AUTH_PASS) as neo4j:
        llm = DeepSeekClient(api_key=DEEPSEEK_API_KEY, thinking=thinking)
        batch_result = await process_batch(args.input_dir, options, llm, neo4j)

    logger.info(
        "Batch complete — built: %d, skipped: %d, failed: %d",
        batch_result.built,
        batch_result.skipped,
        batch_result.failed,
    )


async def _run_export(args: argparse.Namespace) -> None:
    """Export the full Neo4j graph to the Obsidian vault.

    @param args Parsed CLI arguments
    """
    from graph_builder.graph.graph_reader import GraphReader
    from graph_builder.graph.neo4j_client import Neo4jClient
    from graph_builder.vault.obsidian_exporter import export_vault

    async with Neo4jClient(NEO4J_BOLT_URI, NEO4J_AUTH_USER, NEO4J_AUTH_PASS) as neo4j:
        reader = GraphReader(neo4j)
        stats = await export_vault(VAULT_DIR, reader, neo4j)

    logger.info("Export complete: %s", stats)


async def _run_sync_back(args: argparse.Namespace) -> None:
    """Sync human-edited vault fields back to Neo4j.

    @param args Parsed CLI arguments (dry_run controls write behaviour)
    """
    from graph_builder.graph.neo4j_client import Neo4jClient
    from graph_builder.vault.sync_back import sync_back

    async with Neo4jClient(NEO4J_BOLT_URI, NEO4J_AUTH_USER, NEO4J_AUTH_PASS) as neo4j:
        changes = await sync_back(VAULT_DIR, neo4j, dry_run=args.dry_run)

    prefix = "[dry-run] " if args.dry_run else ""
    logger.info("%sSynced %d field changes.", prefix, len(changes))
    for change in changes:
        logger.info(
            "%s  %s.%s: %r -> %r",
            prefix, change.node_type, change.field, change.old_value, change.new_value,
        )


# ---------------------------------------------------------------------------
# Result logging helper
# ---------------------------------------------------------------------------


def _log_result(result) -> None:
    """Log the outcome of a single-paper build.

    @param result BuildResult from process_paper()
    """
    if result.status == "built":
        logger.info(
            "Built %s — concepts: %d, claims: %d, edges: %d",
            result.arxiv_id,
            result.concept_count,
            result.claim_count,
            result.edge_count,
        )
    elif result.status == "skipped":
        logger.info("Skipped %s (already built; use --force to rebuild).", result.arxiv_id)
    else:
        logger.error("Failed %s: %s", result.arxiv_id, result.error)
