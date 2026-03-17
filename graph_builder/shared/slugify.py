"""
@file slugify.py
@description Deterministic slug generation from canonical names.

The slugify algorithm is FROZEN after first production run.
Any changes require a migration script for all existing Neo4j slugs,
vault filenames, and wikilink references.
"""

import re
import unicodedata

# LaTeX command patterns to strip
_LATEX_CMD_RE = re.compile(r"\\[a-zA-Z]+\{([^}]*)\}")
_LATEX_DOLLAR_RE = re.compile(r"\$([^$]*)\$")
_LATEX_BACKSLASH_RE = re.compile(r"\\([a-zA-Z]+)")

# Greek letter map for LaTeX command names (common in math)
_GREEK_MAP = {
    "alpha": "a",
    "beta": "b",
    "gamma": "g",
    "delta": "d",
    "epsilon": "epsilon",
    "zeta": "z",
    "eta": "eta",
    "theta": "theta",
    "lambda": "lambda",
    "mu": "mu",
    "pi": "pi",
    "sigma": "sigma",
    "tau": "tau",
    "phi": "phi",
    "omega": "omega",
}

# Unicode Greek character -> ASCII replacement (applied before NFKD)
_UNICODE_GREEK_MAP = {
    "α": "a",
    "β": "b",
    "γ": "g",
    "δ": "d",
    "ε": "epsilon",
    "ζ": "z",
    "η": "eta",
    "θ": "theta",
    "λ": "lambda",
    "μ": "mu",
    "π": "pi",
    "σ": "sigma",
    "τ": "tau",
    "φ": "phi",
    "ω": "omega",
    "Α": "a",
    "Β": "b",
    "Γ": "g",
    "Δ": "d",
    "Ε": "epsilon",
    "Ζ": "z",
    "Η": "eta",
    "Θ": "theta",
    "Λ": "lambda",
    "Μ": "mu",
    "Π": "pi",
    "Σ": "sigma",
    "Τ": "tau",
    "Φ": "phi",
    "Ω": "omega",
}


def slugify(name: str) -> str:
    """Convert a canonical name to a deterministic slug.

    Algorithm (frozen — do not modify without migration script):
    1. Strip LaTeX commands
    2. Unicode NFKD normalization, strip combining marks
    3. Lowercase
    4. Replace non-alphanumeric with hyphens
    5. Collapse consecutive hyphens
    6. Strip leading/trailing hyphens
    """
    if not name:
        return ""

    text = name
    # Substitute Unicode Greek letters before normalization strips them
    for greek_char, ascii_equiv in _UNICODE_GREEK_MAP.items():
        text = text.replace(greek_char, ascii_equiv)

    # Strip LaTeX: $\epsilon$ -> epsilon
    text = _LATEX_DOLLAR_RE.sub(r"\1", text)
    text = _LATEX_CMD_RE.sub(r"\1", text)
    for cmd, replacement in _GREEK_MAP.items():
        text = text.replace(f"\\{cmd}", replacement)
    text = _LATEX_BACKSLASH_RE.sub(r"\1", text)

    # Unicode NFKD normalization
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))

    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-{2,}", "-", text)
    text = text.strip("-")

    return text
