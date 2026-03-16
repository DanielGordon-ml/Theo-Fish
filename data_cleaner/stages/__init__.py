"""
@file stages/__init__.py
@description Re-exports all cleaning stage functions.
"""

from data_cleaner.stages.newline_normalizer import normalize_newlines
from data_cleaner.stages.latex_normalizer import normalize_latex
from data_cleaner.stages.artifact_remover import remove_artifacts
from data_cleaner.stages.heading_normalizer import normalize_headings
from data_cleaner.stages.whitespace_cleaner import clean_whitespace

__all__ = [
    "normalize_newlines",
    "normalize_latex",
    "remove_artifacts",
    "normalize_headings",
    "clean_whitespace",
]
