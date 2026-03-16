"""
@file test_fuzzy_matcher.py
@description Tests for fuzzy string normalization and similarity matching.
"""

import pytest

from graph_builder.extraction.dedup.fuzzy_matcher import (
    classify_match,
    compute_similarity,
    normalize_name,
)


class TestNormalizeName:
    """Tests for normalize_name()."""

    def test_it_should_expand_mdp_abbreviation(self):
        """It should expand 'MDP' to 'markov decision process'."""
        result = normalize_name("MDP")
        assert result == "markov decision process"

    def test_it_should_lowercase_input(self):
        """It should lowercase the input string."""
        result = normalize_name("Banach Space")
        assert result == result.lower()

    def test_it_should_strip_leading_article_the(self):
        """It should strip leading 'the' article."""
        result = normalize_name("the Markov Chain")
        assert not result.startswith("the ")

    def test_it_should_strip_leading_article_a(self):
        """It should strip leading 'a' article."""
        result = normalize_name("a neural network")
        assert not result.startswith("a ")

    def test_it_should_strip_leading_article_an(self):
        """It should strip leading 'an' article."""
        result = normalize_name("an estimator")
        assert not result.startswith("an ")

    def test_it_should_handle_rl_abbreviation(self):
        """It should expand 'RL' to 'reinforcement learning'."""
        result = normalize_name("RL")
        assert result == "reinforcement learning"

    def test_it_should_handle_mixed_case_abbreviation(self):
        """It should expand abbreviations regardless of case."""
        result = normalize_name("Ucb")
        assert result == "upper confidence bound"

    def test_it_should_leave_non_abbreviated_text_intact(self):
        """It should leave non-abbreviated text in lowercase."""
        result = normalize_name("Gaussian Process")
        assert result == "gaussian process"


class TestComputeSimilarity:
    """Tests for compute_similarity()."""

    def test_it_should_return_one_for_identical_names(self):
        """It should return similarity 1.0 for identical names."""
        score = compute_similarity("markov chain", "markov chain")
        assert score == pytest.approx(1.0)

    def test_it_should_return_float_between_zero_and_one(self):
        """It should return a float in [0.0, 1.0]."""
        score = compute_similarity("neural network", "bayesian inference")
        assert 0.0 <= score <= 1.0

    def test_it_should_return_high_score_for_near_duplicates(self):
        """It should return a high score for near-duplicate strings."""
        score = compute_similarity("markov chain", "markov chains")
        assert score > 0.85

    def test_it_should_return_low_score_for_unrelated_names(self):
        """It should return a low score for unrelated concept names."""
        score = compute_similarity("banach space", "gradient descent")
        assert score < 0.60


class TestClassifyMatch:
    """Tests for classify_match()."""

    def test_it_should_classify_high_similarity_as_auto_resolve(self):
        """It should return 'auto_resolve' for similarity > 0.85."""
        result = classify_match(0.90)
        assert result == "auto_resolve"

    def test_it_should_classify_boundary_auto_resolve(self):
        """It should return 'auto_resolve' for similarity exactly at 0.85."""
        result = classify_match(0.85)
        assert result == "auto_resolve"

    def test_it_should_classify_moderate_similarity_as_flag(self):
        """It should return 'flag' for similarity in [0.60, 0.85)."""
        result = classify_match(0.70)
        assert result == "flag"

    def test_it_should_classify_lower_boundary_flag(self):
        """It should return 'flag' for similarity exactly at 0.60."""
        result = classify_match(0.60)
        assert result == "flag"

    def test_it_should_classify_low_similarity_as_new(self):
        """It should return 'new' for similarity < 0.60."""
        result = classify_match(0.40)
        assert result == "new"

    def test_it_should_classify_zero_as_new(self):
        """It should return 'new' for similarity of 0.0."""
        result = classify_match(0.0)
        assert result == "new"
