"""
@file proof_linker.py
@description Regex-based proof-location mapper. Scans full paper text for
proof markers and builds a mapping from claim labels to proof text.
"""

import re

# Matches "Proof of Theorem III.3:" or "Proof of Theorem III.3."
_DEFERRED_PROOF_RE = re.compile(
    r"Proof\s+of\s+"
    r"((?:Theorem|Lemma|Proposition|Corollary)\s+[\w\.\-]+)"
    r"\s*[:\.]",
    re.IGNORECASE,
)

# Matches "Proof." or "Proof:" at the start of a line or after blank line
_INLINE_PROOF_RE = re.compile(
    r"(?:^|\n\n)\s*Proof\s*[\.:]",
    re.IGNORECASE,
)

# Matches claim labels like "Theorem 1.", "Lemma III.3."
_CLAIM_LABEL_RE = re.compile(
    r"((?:Theorem|Lemma|Proposition|Corollary)\s+[\w\.\-]+)\s*[\.:]",
    re.IGNORECASE,
)

# QED markers that terminate a proof
_QED_RE = re.compile(
    r"(?:\$\\square\$|\$\\blacksquare\$|∎|□)",
)

# Heading that terminates a proof
_HEADING_RE = re.compile(r"^#{1,6}\s+", re.MULTILINE)

# Minimum chars to skip before searching for the next marker
_MIN_PROOF_CHARS = 20


def build_proof_map(full_text: str) -> dict[str, str]:
    """Build a mapping from claim labels to their proof text.

    @param full_text Full markdown text of the paper.
    @returns Dict mapping claim labels to proof text.
    """
    proof_map: dict[str, str] = {}
    _find_deferred_proofs(full_text, proof_map)
    _find_inline_proofs(full_text, proof_map)
    return proof_map


def _find_deferred_proofs(
    text: str,
    proof_map: dict[str, str],
) -> None:
    """Find 'Proof of X:' patterns and extract proof text.

    @param text Full paper text to scan.
    @param proof_map Dict to populate with label -> proof text mappings.
    """
    for match in _DEFERRED_PROOF_RE.finditer(text):
        label = _normalize_label(match.group(1))
        proof_text = _extract_proof_text(text, match.end())
        if proof_text.strip():
            proof_map[label] = proof_text.strip()


def _find_inline_proofs(
    text: str,
    proof_map: dict[str, str],
) -> None:
    """Find 'Proof.' patterns and link to the preceding claim.

    @param text Full paper text to scan.
    @param proof_map Dict to populate (skips already-mapped labels).
    """
    for match in _INLINE_PROOF_RE.finditer(text):
        claim_label = _find_preceding_claim(text[: match.start()])
        if not claim_label or claim_label in proof_map:
            continue
        proof_text = _extract_proof_text(text, match.end())
        if proof_text.strip():
            proof_map[claim_label] = proof_text.strip()


def _find_preceding_claim(text: str) -> str | None:
    """Find the last claim label before a given position.

    @param text Text preceding the proof marker.
    @returns Normalized claim label, or None if not found.
    """
    matches = list(_CLAIM_LABEL_RE.finditer(text))
    if not matches:
        return None
    return _normalize_label(matches[-1].group(1))


def _extract_proof_text(text: str, start: int) -> str:
    """Extract proof text from start until a terminator.

    Terminators: QED symbol, heading, or next proof/claim marker.

    @param text Full paper text.
    @param start Character offset where proof body begins.
    @returns Extracted proof text (untrimmed).
    """
    remaining = text[start:]
    end = len(remaining)
    end = _clamp_at_qed(remaining, end)
    end = _clamp_at_heading(remaining, end)
    end = _clamp_at_next_marker(remaining, end)
    return remaining[:end]


def _clamp_at_qed(text: str, end: int) -> int:
    """Reduce end to include QED marker but nothing after.

    @param text Remaining text after proof start.
    @param end Current end boundary.
    @returns Adjusted end boundary.
    """
    qed = _QED_RE.search(text)
    if qed:
        return min(end, qed.end())
    return end


def _clamp_at_heading(text: str, end: int) -> int:
    """Reduce end to stop before the next heading.

    @param text Remaining text after proof start.
    @param end Current end boundary.
    @returns Adjusted end boundary.
    """
    heading = _HEADING_RE.search(text)
    if heading:
        return min(end, heading.start())
    return end


def _clamp_at_next_marker(text: str, end: int) -> int:
    """Reduce end to stop before the next proof or claim marker.

    Skips the first few characters to avoid matching the current marker.

    @param text Remaining text after proof start.
    @param end Current end boundary.
    @returns Adjusted end boundary.
    """
    search_start = min(_MIN_PROOF_CHARS, len(text))
    for pattern in [_DEFERRED_PROOF_RE, _CLAIM_LABEL_RE]:
        match = pattern.search(text, search_start)
        if match:
            end = min(end, match.start())
    return end


def _normalize_label(label: str) -> str:
    """Normalize a claim label by collapsing whitespace.

    @param label Raw label string from regex match.
    @returns Cleaned label with single spaces.
    """
    return re.sub(r"\s+", " ", label).strip()
