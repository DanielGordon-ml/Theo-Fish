"""
@file models.py
@description Pydantic models for the data loader pipeline.
"""

from pydantic import BaseModel


class PaperInput(BaseModel):
    """A paper to process — from CSV or CLI input."""

    arxiv_id: str
    paper_name: str | None = None
    file_type: str | None = None  # "pdf" or "html" hint
    is_local: bool = False  # True = local PDF, False = ArXiv paper
    local_filename: str | None = None  # Original PDF filename for local papers


class PaperMetadata(BaseModel):
    """Metadata fetched from ArXiv API, frontmatter fallback, or local defaults."""

    arxiv_id: str
    title: str = ""
    authors: list[str] = []
    abstract: str = ""
    publication_date: str = ""
    categories: list[str] = []
    primary_category: str = ""
    math_subject: str = ""
    source: str = "local"  # "arxiv_api", "frontmatter_fallback", or "local"


class ConversionResult(BaseModel):
    """Result of converting a paper to markdown."""

    arxiv_id: str
    markdown_content: str
    converter_used: str  # "arxiv2md" or "mineru"
    conversion_warnings: list[str]


class PaperDocument(BaseModel):
    """Final output document — one per paper, written as JSON."""

    paper_name: str
    arxiv_id: str
    title: str
    authors: list[str]
    abstract: str
    publication_date: str
    categories: list[str]
    primary_category: str
    math_subject: str
    extracted_text_markdown: str
    metadata_source: str
    converter_used: str
    conversion_warnings: list[str]
    processed_at: str


class PaperResult(BaseModel):
    """Result of processing a single paper — used by SDK and API."""

    arxiv_id: str
    status: str  # "processed", "skipped", "failed"
    converter: str | None = None
    error: str | None = None
    output_path: str | None = None


class BatchResult(BaseModel):
    """Aggregate result of processing a batch of papers."""

    total: int
    processed: int
    skipped: int
    failed: int
    arxiv2md: int
    mineru: int
    results: list[PaperResult]
