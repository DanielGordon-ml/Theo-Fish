"""
@file fuzzy_matcher.py
@description String normalization and similarity scoring for concept deduplication.
"""

import re
from difflib import SequenceMatcher

from graph_builder.config.config import DEDUP_AUTO_THRESHOLD, DEDUP_FLAG_THRESHOLD
from graph_builder.extraction.dedup.abbreviations import MATH_ABBREVIATIONS

# Articles stripped from the start of normalized names
_LEADING_ARTICLES = re.compile(r"^(the|an|a)\s+")


def normalize_name(name: str) -> str:
    """Lowercase, expand known abbreviations, and strip leading articles.

    @param name Raw concept name
    @returns Normalized string for fuzzy comparison
    """
    lowered = name.lower().strip()
    expanded = MATH_ABBREVIATIONS.get(lowered, lowered)
    return _LEADING_ARTICLES.sub("", expanded)


def compute_similarity(name_a: str, name_b: str) -> float:
    """Compute normalized Levenshtein-style similarity between two names.

    Both inputs are normalized before comparison.

    @param name_a First concept name
    @param name_b Second concept name
    @returns Similarity score in [0.0, 1.0]
    """
    norm_a = normalize_name(name_a)
    norm_b = normalize_name(name_b)
    return SequenceMatcher(None, norm_a, norm_b).ratio()


def classify_match(similarity: float) -> str:
    """Map a similarity score to a match category.

    @param similarity Score in [0.0, 1.0]
    @returns "auto_resolve" if >= AUTO threshold,
             "flag" if >= FLAG threshold,
             "new" otherwise
    """
    if similarity >= DEDUP_AUTO_THRESHOLD:
        return "auto_resolve"
    if similarity >= DEDUP_FLAG_THRESHOLD:
        return "flag"
    return "new"
