"""
@file provenance.py
@description ProvenanceNode for per-paper concept formulations.
"""

from pydantic import BaseModel


class ProvenanceNode(BaseModel):
    """Per-paper formulation of a concept. Append-only."""

    concept_slug: str
    source_arxiv_id: str
    formulation: str = ""
    formal_spec: str = ""
    section: str = ""
    extraction_confidence: float = 0.0


class FormulationEdge(BaseModel):
    """Edge from Provenance to Concept with match metadata."""

    match_method: str = "new"
    match_confidence: float = 1.0
