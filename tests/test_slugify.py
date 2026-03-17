"""
@file test_slugify.py
@description Tests for deterministic slug generation.
"""

from graph_builder.shared.slugify import slugify


class TestSlugify:
    """Tests for the slugify function."""

    def test_basic_name(self):
        """It should convert a simple name to lowercase hyphenated slug."""
        assert slugify("Markov Decision Process") == "markov-decision-process"

    def test_latex_stripping(self):
        """It should strip LaTeX commands and convert to readable text."""
        assert slugify("$\\epsilon$-greedy") == "epsilon-greedy"

    def test_parenthetical_content(self):
        """It should handle parenthetical content."""
        assert slugify("KL Divergence (D_KL)") == "kl-divergence-d-kl"

    def test_consecutive_hyphens_collapsed(self):
        """It should collapse consecutive hyphens to single hyphen."""
        assert slugify("foo  --  bar") == "foo-bar"

    def test_leading_trailing_hyphens_stripped(self):
        """It should strip leading and trailing hyphens."""
        assert slugify(" -hello world- ") == "hello-world"

    def test_unicode_normalization(self):
        """It should normalize unicode characters."""
        assert slugify("Hölder continuity") == "holder-continuity"

    def test_deterministic(self):
        """It should produce the same slug for the same input every time."""
        name = "Nash Equilibrium"
        assert slugify(name) == slugify(name)

    def test_special_math_chars(self):
        """It should handle common math notation."""
        assert slugify("Q-function") == "q-function"
        assert slugify("α-regret") == "a-regret"

    def test_empty_string(self):
        """It should handle empty input."""
        assert slugify("") == ""

    def test_numbers_preserved(self):
        """It should preserve digits."""
        assert slugify("Theorem 4.1") == "theorem-4-1"
