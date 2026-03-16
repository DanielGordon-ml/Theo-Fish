"""
@file test_newline_normalizer.py
@description Tests for Stage 0: newline normalizer.
"""

from data_cleaner.stages.newline_normalizer import normalize_newlines


class TestLiteralNewlineReplacement:
    def test_should_replace_literal_backslash_n(self):
        """It should replace literal two-char \\n with real newlines."""
        # Simulates arxiv2md output: no real newlines, only literal \n
        text = "Line one\\nLine two\\nLine three"
        result, stage = normalize_newlines(text)
        assert result == "Line one\nLine two\nLine three"
        assert stage.changes_made > 0
        assert stage.details["literal_newlines"] == 2

    def test_should_skip_when_real_newlines_exist(self):
        """It should skip literal replacement when text has real newlines."""
        text = "Line one\nLine two\nLine three"
        result, stage = normalize_newlines(text)
        assert result == text
        assert stage.details.get("literal_newlines", 0) == 0

    def test_should_not_touch_escaped_newlines_in_latex(self):
        """It should preserve double-backslash followed by n (e.g. \\\\n in LaTeX)."""
        # Text with real newlines but also \\n (double backslash + n) in LaTeX
        text = "Real line\nSome math \\\\neq 0\nEnd"
        result, stage = normalize_newlines(text)
        assert "\\\\neq" in result or "\\neq" in result


class TestMetadataPrefixStripping:
    def test_should_strip_arxiv2md_summary_prefix(self):
        """It should strip the summary='...' sections_tree='...' prefix."""
        prefix = "summary='Title: Test Paper\\nArXiv: 1234' sections_tree='Sections:\\nIntro'"
        body = "\n# Test Paper\n\nContent here."
        text = prefix + body
        result, stage = normalize_newlines(text)
        assert not result.startswith("summary=")
        assert "# Test Paper" in result
        assert stage.details["prefix_stripped"] == 1

    def test_should_not_strip_when_no_prefix(self):
        """It should leave text unchanged when no metadata prefix exists."""
        text = "# Test Paper\n\nContent here."
        result, stage = normalize_newlines(text)
        assert result == text
        assert stage.details.get("prefix_stripped", 0) == 0


class TestStageMetadata:
    def test_should_return_correct_stage_name(self):
        """It should return 'newline_normalizer' as stage_name."""
        _, stage = normalize_newlines("Hello")
        assert stage.stage_name == "newline_normalizer"

    def test_should_report_skipped_for_clean_input(self):
        """It should report skipped when no changes are needed."""
        _, stage = normalize_newlines("Already clean\ntext here.")
        assert stage.changes_made == 0
