"""
@file sdk.py
@description High-level Python API for the knowledge graph builder.
"""

from pathlib import Path

from graph_builder.config import CLEANED_DIR, DEFAULT_CONCURRENCY, VAULT_DIR
from graph_builder.errors import GraphBuilderError
from graph_builder.logger import setup_logger
from graph_builder.models import BatchBuildResult, BuildResult
from graph_builder.orchestrator import process_batch

_logger_initialized = False


def _ensure_logger() -> None:
    """Initialize the logger once on first SDK call."""
    global _logger_initialized
    if not _logger_initialized:
        setup_logger()
        _logger_initialized = True


async def build_graph(
    arxiv_id: str,
    input_dir: Path | None = None,
    vault_dir: Path | None = None,
    force: bool = False,
    thinking: bool | None = None,
) -> BuildResult:
    """Build a knowledge graph for a single paper.

    @param arxiv_id ArXiv ID of the paper
    @param input_dir Directory with cleaned JSON files
    @param vault_dir Output vault directory
    @param force Reprocess even if vault folder exists
    @param thinking Enable LLM thinking mode (None uses config default)
    @raises GraphBuilderError if building fails
    """
    _ensure_logger()

    result = await process_batch(
        arxiv_ids=[arxiv_id],
        input_dir=input_dir or CLEANED_DIR,
        vault_dir=vault_dir or VAULT_DIR,
        concurrency=1,
        force=force,
        thinking=thinking,
    )

    paper_result = result.results[0]
    if paper_result.status == "failed":
        raise GraphBuilderError(
            arxiv_id=arxiv_id,
            reason=paper_result.error or "unknown error",
        )

    return paper_result


async def build_graphs(
    arxiv_ids: list[str] | None = None,
    input_dir: Path | None = None,
    vault_dir: Path | None = None,
    concurrency: int = DEFAULT_CONCURRENCY,
    force: bool = False,
    thinking: bool | None = None,
) -> BatchBuildResult:
    """Build knowledge graphs for multiple papers.

    Never raises — failures are captured in BatchBuildResult.

    @param arxiv_ids List of ArXiv IDs (None = discover from input_dir)
    @param input_dir Directory with cleaned JSON files
    @param vault_dir Output vault directory
    @param concurrency Max concurrent LLM calls
    @param force Reprocess even if vault folders exist
    @param thinking Enable LLM thinking mode (None uses config default)
    """
    _ensure_logger()

    return await process_batch(
        arxiv_ids=arxiv_ids,
        input_dir=input_dir or CLEANED_DIR,
        vault_dir=vault_dir or VAULT_DIR,
        concurrency=concurrency,
        force=force,
        thinking=thinking,
    )


def is_built(arxiv_id: str, vault_dir: Path | None = None) -> bool:
    """Check if a paper's vault folder already exists.

    @param arxiv_id ArXiv ID of the paper
    @param vault_dir Vault directory to check
    """
    vault = vault_dir or VAULT_DIR
    # Check if any subfolder contains an index.md with this arxiv_id
    if not vault.exists():
        return False

    for paper_dir in vault.iterdir():
        if not paper_dir.is_dir():
            continue
        index_file = paper_dir / "index.md"
        if index_file.exists():
            content = index_file.read_text(encoding="utf-8")
            if arxiv_id in content:
                return True

    return False
