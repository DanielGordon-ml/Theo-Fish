"""
@file config.py
@description Paths and constants for the data cleaner.
"""

from data_loader.config import DATA_DIR, PROJECT_ROOT, sanitize_arxiv_id

CLEANED_DIR = DATA_DIR / "cleaned"
LOG_DIR = PROJECT_ROOT / "logs"

DEFAULT_CONCURRENCY = 8

__all__ = [
    "CLEANED_DIR",
    "DATA_DIR",
    "DEFAULT_CONCURRENCY",
    "LOG_DIR",
    "PROJECT_ROOT",
    "sanitize_arxiv_id",
]
