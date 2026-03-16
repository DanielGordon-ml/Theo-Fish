"""
@file batch_processor.py
@description Batch processor that discovers all cleaned-paper JSON files in an
input directory and processes them in parallel, bounded by a semaphore derived
from PipelineOptions.concurrency. One paper failing never blocks the others.
"""

import asyncio
import logging
from pathlib import Path

from graph_builder.extraction.dedup.embedding_client import EmbeddingClient
from graph_builder.graph.neo4j_client import Neo4jClient
from graph_builder.llm.llm_client import DeepSeekClient
from graph_builder.models.results import BatchBuildResult, BuildResult
from graph_builder.orchestrator.orchestrator import PipelineOptions, process_paper

logger = logging.getLogger("graph_builder")


async def process_batch(
    input_dir: Path,
    options: PipelineOptions,
    llm_client: DeepSeekClient,
    neo4j_client: Neo4jClient,
    embedding_client: EmbeddingClient | None = None,
) -> BatchBuildResult:
    """Process all papers in input directory in parallel.

    Discovers every *.json file in input_dir, derives the arxiv_id from the
    filename stem, and calls process_paper for each one under a semaphore
    bounded by options.concurrency. Uses asyncio.gather with
    return_exceptions=True so a single failure never blocks other papers.

    @param input_dir Directory containing cleaned paper JSON files
    @param options Pipeline configuration (concurrency, schema, force, thinking)
    @param llm_client LLM client for extraction calls
    @param neo4j_client Neo4j connection for reads and writes
    @param embedding_client Optional embedding client for dedup cascade
    @returns BatchBuildResult with total/built/skipped/failed counts and
             individual BuildResult for every paper
    """
    paper_files = sorted(input_dir.glob("*.json"))
    if not paper_files:
        return _empty_batch()

    semaphore = asyncio.Semaphore(options.concurrency)
    tasks = [
        _process_guarded(f.stem, options, llm_client, neo4j_client, embedding_client, semaphore)
        for f in paper_files
    ]
    raw = await asyncio.gather(*tasks, return_exceptions=True)
    results = _coerce_results(raw, [f.stem for f in paper_files])
    return _aggregate(results)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

async def _process_guarded(
    arxiv_id: str,
    options: PipelineOptions,
    llm_client: DeepSeekClient,
    neo4j_client: Neo4jClient,
    embedding_client: EmbeddingClient | None,
    semaphore: asyncio.Semaphore,
) -> BuildResult:
    """Run process_paper inside a semaphore; never raises.

    @param arxiv_id ArXiv identifier derived from filename stem
    @param options Pipeline configuration
    @param llm_client LLM client
    @param neo4j_client Neo4j client
    @param embedding_client Optional embedding client
    @param semaphore Concurrency limiter
    @returns BuildResult with status 'built', 'skipped', or 'failed'
    """
    async with semaphore:
        return await process_paper(
            arxiv_id, options, llm_client, neo4j_client, embedding_client,
        )


def _coerce_results(
    raw: list,
    arxiv_ids: list[str],
) -> list[BuildResult]:
    """Convert gather results (including bare exceptions) to BuildResults.

    asyncio.gather with return_exceptions=True can return Exception objects
    alongside normal results. Those are wrapped into failed BuildResults so
    the aggregation logic only ever sees BuildResult instances.

    @param raw Raw output list from asyncio.gather
    @param arxiv_ids IDs in the same order as raw
    @returns List of BuildResult, one per paper
    """
    results: list[BuildResult] = []
    for item, arxiv_id in zip(raw, arxiv_ids):
        if isinstance(item, Exception):
            logger.error("Unhandled exception for %s: %s", arxiv_id, item)
            results.append(BuildResult(
                arxiv_id=arxiv_id,
                status="failed",
                error=str(item),
            ))
        else:
            results.append(item)
    return results


def _aggregate(results: list[BuildResult]) -> BatchBuildResult:
    """Tally built/skipped/failed counts from a list of BuildResults.

    @param results Individual build results
    @returns BatchBuildResult with aggregated counts
    """
    built = sum(1 for r in results if r.status == "built")
    skipped = sum(1 for r in results if r.status == "skipped")
    failed = sum(1 for r in results if r.status == "failed")
    return BatchBuildResult(
        total=len(results),
        built=built,
        skipped=skipped,
        failed=failed,
        results=results,
    )


def _empty_batch() -> BatchBuildResult:
    """Return a zero-count BatchBuildResult for an empty input directory.

    @returns BatchBuildResult with all counts at zero
    """
    return BatchBuildResult(total=0, built=0, skipped=0, failed=0, results=[])
