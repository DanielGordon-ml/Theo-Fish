"""
@file test_claim_model.py
@description Tests for ClaimNode model.
"""

from graph_builder.models.claim import ClaimNode


class TestClaimNode:
    def test_slug_composition(self):
        """It should compose slug from paper_slug + claim label."""
        node = ClaimNode(
            source_paper_slug="intro-bandits",
            label="Theorem 4.1",
            claim_type="theorem",
        )
        assert node.slug == "intro-bandits--theorem-4-1"

    def test_name_defaults_to_label(self):
        """It should default name to label."""
        node = ClaimNode(
            source_paper_slug="paper",
            label="Lemma 2.3",
            claim_type="lemma",
        )
        assert node.name == "Lemma 2.3"

    def test_strength_stored(self):
        """It should store strength value."""
        node = ClaimNode(
            source_paper_slug="p",
            label="T1",
            claim_type="theorem",
            strength="asymptotic",
        )
        assert node.strength == "asymptotic"

    def test_assumptions_ordered_list(self):
        """It should preserve assumption ordering."""
        node = ClaimNode(
            source_paper_slug="p",
            label="T1",
            claim_type="theorem",
            assumptions=["finite action space", "bounded rewards"],
        )
        assert node.assumptions == ["finite action space", "bounded rewards"]
