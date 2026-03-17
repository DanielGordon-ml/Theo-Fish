"""
@file test_provenance_model.py
@description Tests for ProvenanceNode and FormulationEdge models.
"""

from graph_builder.models.provenance import ProvenanceNode, FormulationEdge


class TestProvenanceNode:
    def test_concept_slug_and_source_arxiv(self):
        """It should store uniqueness keys."""
        node = ProvenanceNode(
            concept_slug="markov-decision-process",
            source_arxiv_id="1904.07272",
            formulation="A tuple (S,A,P,R,γ)",
        )
        assert node.concept_slug == "markov-decision-process"
        assert node.source_arxiv_id == "1904.07272"


class TestFormulationEdge:
    def test_match_metadata(self):
        """It should carry match method and confidence."""
        edge = FormulationEdge(match_method="embedding+llm", match_confidence=0.87)
        assert edge.match_method == "embedding+llm"
        assert edge.match_confidence == 0.87
