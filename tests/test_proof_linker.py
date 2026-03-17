"""
@file test_proof_linker.py
@description Tests for the proof-linking pre-pass that maps claim labels to proof text.
"""


from graph_builder.extraction.proof_linker import build_proof_map


class TestBuildProofMap:
    """Tests for build_proof_map()."""

    def test_it_should_find_deferred_proofs_with_colon(self):
        """It should match 'Proof of Theorem X:' patterns."""
        text = (
            "# Main Results\n\n"
            "Theorem III.3. The bound is tight.\n\n"
            "# Appendix\n\n"
            "Proof of Theorem III.3: We proceed by induction. "
            "Base case holds. Inductive step follows.\n\n"
            "# References\n"
        )
        proof_map = build_proof_map(text)
        assert "Theorem III.3" in proof_map
        assert "induction" in proof_map["Theorem III.3"]

    def test_it_should_find_deferred_proofs_with_period(self):
        """It should match 'Proof of Proposition II.1.' patterns."""
        text = (
            "Proposition II.1. Existence is guaranteed.\n\n"
            "Proof of Proposition II.1. We observe that "
            "the optimal is a fixed point.\n\n"
            "## Next Section\n"
        )
        proof_map = build_proof_map(text)
        assert "Proposition II.1" in proof_map
        assert "fixed point" in proof_map["Proposition II.1"]

    def test_it_should_find_inline_proofs(self):
        """It should match 'Proof.' appearing after a claim."""
        text = (
            "Theorem 1. The regret is O(sqrt(T)).\n\n"
            "Proof. By Hoeffding's inequality, we have the bound.\n\n"
            "Theorem 2. Convergence is guaranteed.\n"
        )
        proof_map = build_proof_map(text)
        assert "Theorem 1" in proof_map
        assert "Hoeffding" in proof_map["Theorem 1"]

    def test_it_should_stop_at_qed_symbols(self):
        """It should stop proof text at QED markers."""
        text = (
            "Proof of Theorem 1: By construction. "
            "This completes the proof. $\\square$\n\n"
            "Some other text after QED.\n"
        )
        proof_map = build_proof_map(text)
        assert "Theorem 1" in proof_map
        assert "other text after" not in proof_map["Theorem 1"]

    def test_it_should_return_empty_dict_when_no_proofs(self):
        """It should return {} when the text has no proof markers."""
        text = "# Introduction\n\nThis paper studies games.\n"
        proof_map = build_proof_map(text)
        assert proof_map == {}

    def test_it_should_handle_multiple_proofs(self):
        """It should map multiple claims to their respective proofs."""
        text = (
            "Proof of Theorem 1: First proof text.\n\n"
            "Proof of Lemma 2: Second proof text.\n\n"
            "# End\n"
        )
        proof_map = build_proof_map(text)
        assert len(proof_map) == 2
        assert "First proof" in proof_map["Theorem 1"]
        assert "Second proof" in proof_map["Lemma 2"]

    def test_it_should_handle_corollary_proofs(self):
        """It should match proofs of corollaries."""
        text = (
            "Proof of Corollary 1: This follows immediately "
            "from Theorem 2.\n\n"
            "# Next\n"
        )
        proof_map = build_proof_map(text)
        assert "Corollary 1" in proof_map
