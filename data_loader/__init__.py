"""
@file __init__.py
@description Theo-Fish ETL Data Loader — ingests ArXiv papers into structured JSON.
"""

from data_loader.errors import LoaderError
from data_loader.models import BatchResult, PaperDocument, PaperResult
from data_loader.sdk import is_processed, load_paper, load_papers

__all__ = [
    "load_paper",
    "load_papers",
    "is_processed",
    "PaperResult",
    "BatchResult",
    "PaperDocument",
    "LoaderError",
]
