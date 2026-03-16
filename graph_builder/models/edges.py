"""
@file edges.py
@description Typed edge models for concept, claim, and coupling relationships.
"""

from typing import Any

from pydantic import BaseModel


class ConceptEdge(BaseModel):
    """Edge between two concepts in Graph A."""

    source_slug: str
    target_slug: str
    edge_type: str
    attributes: dict[str, Any] = {}


class ClaimEdge(BaseModel):
    """Edge between two claims in Graph B."""

    source_slug: str
    target_slug: str
    edge_type: str
    attributes: dict[str, Any] = {}


class CouplingEdge(BaseModel):
    """ABOUT edge from a claim to a concept."""

    claim_slug: str
    concept_slug: str
    role: str = "primary"
    aspect: str = ""


class SourcedFromEdge(BaseModel):
    """SOURCED_FROM edge linking a node to its paper."""

    node_slug: str
    source_arxiv_id: str
    section: str = ""
    page: str = ""
    confidence: float = 0.0
