"""
@file orchestrator.py
@description Async pipeline orchestrator with batch processing.
"""

import asyncio
import json
import logging
from pathlib import Path

from graph_builder.config import (
    CLEANED_DIR,
    DEFAULT_CONCURRENCY,
    VAULT_DIR,
    sanitize_arxiv_id,
)
from graph_builder.entity_extractor import extract_entities
from graph_builder.llm_client import DeepSeekClient
from graph_builder.logger import log_progress
from graph_builder.models import (
    BatchBuildResult,
    BuildResult,
    PaperGraph,
)
from graph_builder.relationship_mapper import (
    find_cross_paper_links,
    map_relationships,
)
from graph_builder.section_splitter import split_into_sections
from graph_builder.vault_scanner import VaultIndex, scan_vault
from graph_builder.vault_writer import sanitize_title, write_paper_vault

logger = logging.getLogger("graph_builder")


async def _process_one(
    arxiv_id: str,
    input_dir: Path,
    vault_dir: Path,
    client: DeepSeekClient,
    force: bool,
    vault_index: VaultIndex | None = None,
) -> BuildResult:
    """Process a single paper through the full pipeline.

    @param arxiv_id ArXiv ID of the paper
    @param input_dir Directory containing cleaned JSON files
    @param vault_dir Output vault directory
    @param client DeepSeek LLM client
    @param force Reprocess even if vault folder exists
    @param vault_index Pre-scanned vault index for cross-paper links
    """
    # Load cleaned JSON
    json_path = _find_json_file(arxiv_id, input_dir)
    if json_path is None:
        return BuildResult(
            arxiv_id=arxiv_id, status="failed",
            error=f"No cleaned JSON found for {arxiv_id}",
        )

    paper_data = _load_paper_json(json_path)
    if paper_data is None:
        return BuildResult(
            arxiv_id=arxiv_id, status="failed",
            error="Failed to parse cleaned JSON",
        )

    title = paper_data.get("title", arxiv_id)

    # Skip check
    if not force and _is_built(title, arxiv_id, vault_dir):
        return BuildResult(arxiv_id=arxiv_id, status="skipped")

    log_progress(f"  [{arxiv_id}] Starting pipeline...")

    try:
        return await _run_pipeline(
            arxiv_id, title, paper_data, client, vault_dir,
            vault_index or VaultIndex(),
        )
    except Exception as err:
        logger.error(
            "Pipeline failed: %s", str(err),
            extra={"arxiv_id": arxiv_id},
        )
        return BuildResult(
            arxiv_id=arxiv_id, status="failed", error=str(err),
        )


async def _run_pipeline(
    arxiv_id: str,
    title: str,
    paper_data: dict,
    client: DeepSeekClient,
    vault_dir: Path,
    vault_index: VaultIndex,
) -> BuildResult:
    """Run the extraction pipeline for a single paper."""
    markdown = paper_data.get("extracted_text_markdown", "")
    sections = split_into_sections(markdown)

    # Extract entities
    entities, entity_tokens = await extract_entities(client, sections)

    # Map relationships
    relationships, rel_tokens = await map_relationships(client, entities)

    # Build paper graph
    graph = PaperGraph(
        arxiv_id=arxiv_id,
        title=title,
        entities=entities,
        relationships=relationships,
        total_input_tokens=entity_tokens["input"] + rel_tokens["input"],
        total_output_tokens=entity_tokens["output"] + rel_tokens["output"],
    )

    # Use pre-scanned vault index for cross-paper links
    vault_labels = vault_index.get_labels_map()
    cross_links = find_cross_paper_links(entities, arxiv_id, vault_labels)

    # Build cross-paper folder mapping
    cross_folders: dict[str, str] = {}
    for entry_list in vault_index.label_index.values():
        for entry in entry_list:
            cross_folders[entry.arxiv_id] = entry.paper_folder

    # Write vault files
    write_paper_vault(
        graph, vault_dir, relationships, cross_links, cross_folders,
    )

    log_progress(
        f"  [{arxiv_id}] Done: {len(entities)} entities, "
        f"{len(relationships)} relationships",
    )

    return BuildResult(
        arxiv_id=arxiv_id,
        status="built",
        entity_count=len(entities),
        relationship_count=len(relationships),
    )


def _result_from_exception(arxiv_id: str, exc: Exception) -> BuildResult:
    """Wrap an unhandled exception into a failed BuildResult.

    @param arxiv_id ArXiv ID of the paper that failed
    @param exc The exception that was raised
    """
    return BuildResult(
        arxiv_id=arxiv_id, status="failed", error=str(exc),
    )


async def process_batch(
    arxiv_ids: list[str] | None = None,
    input_dir: Path | None = None,
    vault_dir: Path | None = None,
    concurrency: int = DEFAULT_CONCURRENCY,
    force: bool = False,
    thinking: bool | None = None,
) -> BatchBuildResult:
    """Process a batch of papers concurrently.

    @param arxiv_ids List of ArXiv IDs to process
    @param input_dir Directory with cleaned JSON files
    @param vault_dir Output vault directory
    @param concurrency Max concurrent LLM calls
    @param force Reprocess even if vault folders exist
    @param thinking Enable LLM thinking mode (None uses config default)
    """
    input_dir = input_dir or CLEANED_DIR
    vault_dir = vault_dir or VAULT_DIR

    # Discover papers to process
    ids = arxiv_ids or _discover_papers(input_dir)

    log_progress(f"Processing {len(ids)} paper(s)...")

    # Scan vault once before parallel processing
    vault_index = scan_vault(vault_dir)

    client = DeepSeekClient(concurrency=concurrency, thinking=thinking)

    # Process papers in parallel — semaphore gates LLM concurrency
    tasks = [
        _process_one(
            arxiv_id, input_dir, vault_dir, client, force, vault_index,
        )
        for arxiv_id in ids
    ]
    raw_results = await asyncio.gather(*tasks, return_exceptions=True)

    # Convert any unhandled exceptions to failed BuildResults
    results: list[BuildResult] = []
    for i, raw in enumerate(raw_results):
        if isinstance(raw, Exception):
            results.append(_result_from_exception(ids[i], raw))
        else:
            results.append(raw)

    counts = _count_results(results)
    return BatchBuildResult(
        total=len(ids), results=results, **counts,
    )


def print_summary(batch_result: BatchBuildResult) -> None:
    """Print a human-readable processing summary to stdout."""
    print(f"\nBuilt: {batch_result.built}/{batch_result.total}")
    if batch_result.skipped:
        print(f"Skipped (already exists): {batch_result.skipped}")
    if batch_result.failed:
        print(
            f"Failed: {batch_result.failed} "
            "(see logs/graph_builder.log for details)",
        )

    for r in batch_result.results:
        if r.status == "built":
            print(
                f"  + {r.arxiv_id}: {r.entity_count} entities, "
                f"{r.relationship_count} relationships",
            )
        elif r.status == "failed":
            print(f"  x {r.arxiv_id}: {r.error}")


def _find_json_file(arxiv_id: str, input_dir: Path) -> Path | None:
    """Locate the cleaned JSON file for a given ArXiv ID."""
    sanitized = sanitize_arxiv_id(arxiv_id)
    candidates = [
        input_dir / f"{arxiv_id}.json",
        input_dir / f"{sanitized}.json",
    ]
    for path in candidates:
        if path.exists():
            return path
    return None


def _load_paper_json(json_path: Path) -> dict | None:
    """Load and parse a cleaned JSON file."""
    try:
        content = json_path.read_text(encoding="utf-8")
        return json.loads(content)
    except (json.JSONDecodeError, OSError) as err:
        logger.warning(
            "Failed to load JSON: %s", str(err),
            extra={"arxiv_id": "load"},
        )
        return None


def _is_built(title: str, arxiv_id: str, vault_dir: Path) -> bool:
    """Check if a paper's vault folder already exists."""
    folder_name = sanitize_title(title, fallback=arxiv_id)
    paper_dir = vault_dir / folder_name
    return paper_dir.exists() and (paper_dir / "index.md").exists()


def _discover_papers(input_dir: Path) -> list[str]:
    """Discover ArXiv IDs from JSON filenames in the input directory."""
    ids: list[str] = []
    for json_file in sorted(input_dir.glob("*.json")):
        # Use the filename stem as the ArXiv ID
        ids.append(json_file.stem)
    return ids


def _count_results(results: list[BuildResult]) -> dict[str, int]:
    """Count built/skipped/failed from results list."""
    counts = {"built": 0, "skipped": 0, "failed": 0}
    for r in results:
        if r.status in counts:
            counts[r.status] += 1
    return counts
