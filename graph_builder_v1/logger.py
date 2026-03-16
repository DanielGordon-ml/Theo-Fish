"""
@file logger.py
@description Logging setup — WARNING and ERROR only to file.
"""

import logging
from pathlib import Path

from graph_builder.config import LOG_DIR


def setup_logger(log_dir: Path | None = None) -> logging.Logger:
    """Configure and return the graph builder logger.

    Writes WARNING+ to logs/graph_builder.log. Creates log directory if needed.
    """
    log_dir = log_dir or LOG_DIR
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "graph_builder.log"

    logger = logging.getLogger("graph_builder")
    logger.setLevel(logging.WARNING)

    # Remove stale handlers when reconfiguring with a new log_dir
    for h in logger.handlers[:]:
        h.close()
        logger.removeHandler(h)

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
    """Get the graph_builder logger (must call setup_logger first)."""
    return logging.getLogger("graph_builder")


def log_progress(message: str) -> None:
    """Print a progress message to stderr with flush.

    @param message Progress message to display
    """
    import sys
    print(message, file=sys.stderr, flush=True)
