"""
@file logger.py
@description Logging setup — WARNING and ERROR only to file.
"""

import logging
from pathlib import Path

from data_cleaner.config import LOG_DIR


def setup_logger(log_dir: Path | None = None) -> logging.Logger:
    """Configure and return the data cleaner logger.

    Writes WARNING+ to logs/cleaner.log. Creates log directory if needed.
    """
    log_dir = log_dir or LOG_DIR
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "cleaner.log"

    logger = logging.getLogger("data_cleaner")
    logger.setLevel(logging.WARNING)

    if not logger.handlers:
        handler = logging.FileHandler(log_file, mode="a", encoding="utf-8")
        handler.setLevel(logging.WARNING)
        formatter = logging.Formatter(
            "%(asctime)s %(levelname)-7s [%(arxiv_id)s] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


def get_logger() -> logging.Logger:
    """Get the data_cleaner logger (must call setup_logger first)."""
    return logging.getLogger("data_cleaner")
