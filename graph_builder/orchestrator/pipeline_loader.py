"""
@file pipeline_loader.py
@description Paper loading and JSON parsing helpers for the orchestrator pipeline.
"""

import json
import logging
from pathlib import Path

from graph_builder.config.config import CLEANED_DIR
from graph_builder.graph.graph_reader import GraphReader
from graph_builder.graph.neo4j_client import Neo4jClient
from graph_builder.models.section import Section

logger = logging.getLogger("graph_builder")


async def load_paper(arxiv_id: str) -> tuple[str, list[Section], str]:
    """Load cleaned JSON and split into sections.

    @param arxiv_id ArXiv identifier
    @returns Tuple of (title, sections, full_text)
    @raises FileNotFoundError if cleaned JSON does not exist
    """
    from graph_builder.extraction.section_splitter import split_into_sections

    json_path = _find_json_path(arxiv_id)
    paper_data = _read_json(json_path)
    title = paper_data.get("title", arxiv_id)
    markdown = paper_data.get("extracted_text_markdown", "")
    sections = split_into_sections(markdown)
    return title, sections, markdown


def _find_json_path(arxiv_id: str) -> Path:
    """Locate the cleaned JSON file for the given ArXiv ID.

    @param arxiv_id ArXiv identifier
    @returns Path to the cleaned JSON file
    @raises FileNotFoundError if not found
    """
    from data_loader.config import sanitize_arxiv_id

    candidates = [
        CLEANED_DIR / f"{arxiv_id}.json",
        CLEANED_DIR / f"{sanitize_arxiv_id(arxiv_id)}.json",
    ]
    for path in candidates:
        if path.exists():
            return path
    raise FileNotFoundError(
        f"No cleaned JSON found for {arxiv_id} in {CLEANED_DIR}",
    )


def _read_json(path: Path) -> dict:
    """Read and parse a JSON file.

    @param path Path to the JSON file
    @returns Parsed dict
    """
    content = path.read_text(encoding="utf-8")
    return json.loads(content)


async def check_already_built(
    arxiv_id: str,
    neo4j_client: Neo4jClient,
) -> bool:
    """Check whether the paper has already been ingested.

    @param arxiv_id ArXiv identifier
    @param neo4j_client Neo4j connection
    @returns True if paper already exists
    """
    reader = GraphReader(neo4j_client)
    return await reader.is_paper_built(arxiv_id)
