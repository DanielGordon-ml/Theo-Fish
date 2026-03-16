"""
@file test_concept_model.py
@description Tests for ConceptNode model.
"""

from graph_builder.models.concept import ConceptNode


class TestConceptNode:
    def test_slug_derived_from_name(self):
        """It should derive slug deterministically from name."""
        node = ConceptNode(
            name="Markov Decision Process",
            semantic_type="structure",
            formal_spec="(S, A, P, R, γ)",
        )
        assert node.slug == "markov-decision-process"

    def test_aliases_deduplicated_and_sorted(self):
        """It should deduplicate and sort aliases."""
        node = ConceptNode(
            name="MDP",
            semantic_type="structure",
            aliases=["finite MDP", "MDP", "finite MDP"],
        )
        assert node.aliases == ["MDP", "finite MDP"]

    def test_status_default_canonical(self):
        """It should default status to canonical."""
        node = ConceptNode(name="X", semantic_type="structure")
        assert node.status == "canonical"

    def test_promoted_fields(self):
        """It should accept promoted type-specific fields."""
        node = ConceptNode(
            name="Bellman operator",
            semantic_type="operator",
            ts_domain="state-value space",
            ts_codomain="state-value space",
        )
        assert node.ts_domain == "state-value space"
