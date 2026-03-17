"""
@file config.py
@description Default paths and constants for the data loader.
"""

from pathlib import Path

# Paths relative to project root for portability
PROJECT_ROOT = Path(__file__).resolve().parents[1]  # ETL/
DATA_DIR = PROJECT_ROOT.parent / "Data"  # Theo-Fish/Data/
PAPERS_DIR = DATA_DIR / "papers"
PROCESSED_DIR = DATA_DIR / "processed"
FOR_PROCESS_DIR = DATA_DIR / "for_process"
LOG_DIR = PROJECT_ROOT / "logs"


def sanitize_arxiv_id(arxiv_id: str) -> str:
    """Convert an ArXiv ID to a safe filename component."""
    return arxiv_id.replace("/", "_")


# Concurrency
DEFAULT_CONCURRENCY = 5

# ArXiv API
ARXIV_API_URL = "https://export.arxiv.org/api/query"
ARXIV_API_DELAY = 3.0  # seconds between API batches
ARXIV_API_BATCH_SIZE = 20
