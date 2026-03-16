"""
@file test_graph_builder_v2_errors.py
@description Tests for v2 error classes.
"""

from graph_builder.shared.errors import (
    GraphBuilderError,
    ValidationError,
    DedupConflictError,
)


class TestGraphBuilderError:
    def test_includes_arxiv_id_and_reason(self):
        """It should include arxiv_id and reason in message."""
        err = GraphBuilderError("1904.07272", "extraction failed")
        assert "1904.07272" in str(err)
        assert "extraction failed" in str(err)
        assert err.arxiv_id == "1904.07272"


class TestValidationError:
    def test_includes_severity_and_rule(self):
        """It should include severity and rule in the error."""
        err = ValidationError("missing_about", "error", "Claim X has no ABOUT edge")
        assert err.rule == "missing_about"
        assert err.severity == "error"


class TestDedupConflictError:
    def test_includes_slugs(self):
        """It should include both slugs and similarity score."""
        err = DedupConflictError("mdp", "markov-decision-process", 0.72)
        assert err.new_slug == "mdp"
        assert err.existing_slug == "markov-decision-process"
        assert err.similarity == 0.72
