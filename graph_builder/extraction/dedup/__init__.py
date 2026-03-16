"""
@file __init__.py
@description Public exports for dedup cascade.
"""

from graph_builder.extraction.dedup.dedup_cascade import run_dedup_cascade, DedupResult
from graph_builder.extraction.dedup.fuzzy_matcher import normalize_name, compute_similarity
from graph_builder.extraction.dedup.embedding_client import EmbeddingClient

__all__ = [
    "run_dedup_cascade",
    "DedupResult",
    "normalize_name",
    "compute_similarity",
    "EmbeddingClient",
]
