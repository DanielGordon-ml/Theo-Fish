"""
@file test_edges_model.py
@description Tests for edge dataclasses.
"""

from graph_builder.models.edges import (
    ConceptEdge, ClaimEdge, CouplingEdge, SourcedFromEdge,
)


class TestCouplingEdge:
    def test_about_requires_role(self):
        """It should store role on ABOUT edge."""
        edge = CouplingEdge(
            claim_slug="paper--theorem-1",
            concept_slug="nash-equilibrium",
            role="primary",
            aspect="existence proof",
        )
        assert edge.role == "primary"

class TestClaimEdge:
    def test_attributes_typed(self):
        """It should store typed attributes dict."""
        edge = ClaimEdge(
            source_slug="t1", target_slug="l1",
            edge_type="depends_on",
            attributes={"role": "bound", "applied_to": "concentration step"},
        )
        assert edge.attributes["role"] == "bound"

class TestConceptEdge:
    def test_basic_creation(self):
        """It should create concept edge with type."""
        edge = ConceptEdge(
            source_slug="mdp", target_slug="pomdp",
            edge_type="generalizes",
            attributes={"condition": "full observability"},
        )
        assert edge.edge_type == "generalizes"

class TestSourcedFromEdge:
    def test_stores_confidence(self):
        """It should store confidence score."""
        edge = SourcedFromEdge(
            node_slug="theorem-1", source_arxiv_id="1904.07272",
            section="Chapter 1", confidence=0.95,
        )
        assert edge.confidence == 0.95
