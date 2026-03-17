"""
@file json_writer.py
@description Assemble and write PaperDocument JSON files.
"""

import logging
from datetime import datetime, timezone
from pathlib import Path

from data_loader.config import sanitize_arxiv_id
from data_loader.models import (
    PaperInput,
    PaperMetadata,
    ConversionResult,
    PaperDocument,
)

logger = logging.getLogger("data_loader")


def assemble_document(
    paper_input: PaperInput,
    metadata: PaperMetadata,
    conversion: ConversionResult,
) -> PaperDocument:
    """Combine input, metadata, and conversion into a PaperDocument."""
    # Resolve paper_name: CSV name > title > arxiv_id
    paper_name = paper_input.paper_name or metadata.title or paper_input.arxiv_id

    return PaperDocument(
        paper_name=paper_name,
        arxiv_id=metadata.arxiv_id,
        title=metadata.title,
        authors=metadata.authors,
        abstract=metadata.abstract,
        publication_date=metadata.publication_date,
        categories=metadata.categories,
        primary_category=metadata.primary_category,
        math_subject=metadata.math_subject,
        extracted_text_markdown=conversion.markdown_content,
        metadata_source=metadata.source,
        converter_used=conversion.converter_used,
        conversion_warnings=conversion.conversion_warnings,
        processed_at=datetime.now(timezone.utc).isoformat(),
    )


def should_skip(arxiv_id: str, processed_dir: Path, force: bool) -> bool:
    """Check if a paper has already been processed."""
    if force:
        return False
    json_file = processed_dir / f"{sanitize_arxiv_id(arxiv_id)}.json"
    return json_file.exists()


def write_document(doc: PaperDocument, processed_dir: Path) -> Path:
    """Write a PaperDocument to a JSON file. Returns the output path."""
    processed_dir.mkdir(parents=True, exist_ok=True)
    json_file = processed_dir / f"{sanitize_arxiv_id(doc.arxiv_id)}.json"

    try:
        json_file.write_text(doc.model_dump_json(indent=2), encoding="utf-8")
    except Exception as e:
        logger.error(
            "Failed to write JSON: %s",
            str(e),
            extra={"arxiv_id": doc.arxiv_id},
        )
        raise

    return json_file
