"""
@file test_whitespace_cleaner.py
@description Tests for Stage 4: whitespace cleaner.
"""

from data_cleaner.stages.whitespace_cleaner import clean_whitespace


class TestNewlineCollapsing:
    def test_should_collapse_triple_newlines(self):
        """It should collapse 3+ consecutive newlines to 2."""
        text = "Para one.\n\n\n\nPara two."
        result, stage = clean_whitespace(text)
        assert result == "Para one.\n\nPara two.\n"
        assert stage.details["collapsed_newlines"] > 0

    def test_should_keep_double_newlines(self):
        """It should preserve exactly 2 consecutive newlines."""
        text = "Para one.\n\nPara two.\n"
        result, stage = clean_whitespace(text)
        assert result == text

    def test_should_collapse_many_newlines(self):
        """It should handle 5+ consecutive newlines."""
        text = "A\n\n\n\n\n\nB"
        result, _ = clean_whitespace(text)
        assert result == "A\n\nB\n"


class TestTrailingWhitespace:
    def test_should_strip_trailing_spaces(self):
        """It should remove trailing spaces from each line."""
        text = "Line one   \nLine two  \n"
        result, stage = clean_whitespace(text)
        assert "Line one\n" in result
        assert "Line two\n" in result
        assert stage.details["trailing_whitespace"] > 0

    def test_should_strip_trailing_tabs(self):
        """It should remove trailing tabs from each line."""
        text = "Line one\t\nLine two\n"
        result, _ = clean_whitespace(text)
        assert "Line one\n" in result


class TestLineEndingNormalization:
    def test_should_normalize_crlf(self):
        """It should convert \\r\\n to \\n."""
        text = "Line one\r\nLine two\r\n"
        result, stage = clean_whitespace(text)
        assert "\r" not in result
        assert stage.details["crlf_normalized"] > 0

    def test_should_normalize_cr(self):
        """It should convert bare \\r to \\n."""
        text = "Line one\rLine two\r"
        result, _ = clean_whitespace(text)
        assert "\r" not in result


class TestDocumentTrimming:
    def test_should_ensure_single_trailing_newline(self):
        """It should end the document with exactly one newline."""
        text = "Content here"
        result, _ = clean_whitespace(text)
        assert result == "Content here\n"

    def test_should_trim_leading_whitespace(self):
        """It should remove leading blank lines."""
        text = "\n\n\nContent here\n"
        result, _ = clean_whitespace(text)
        assert result == "Content here\n"

    def test_should_trim_trailing_excess_newlines(self):
        """It should trim excess trailing newlines to exactly one."""
        text = "Content here\n\n\n\n"
        result, _ = clean_whitespace(text)
        assert result == "Content here\n"


class TestCodeBlockProtection:
    def test_should_preserve_whitespace_in_code_blocks(self):
        """It should not collapse newlines inside fenced code blocks."""
        text = "Text\n\n```\n\n\n\ncode\n\n\n\n```\n\nMore text\n"
        result, _ = clean_whitespace(text)
        # Code block internals should keep their newlines
        assert "\n\n\n\ncode\n\n\n\n" in result


class TestStageMetadata:
    def test_should_return_correct_stage_name(self):
        """It should return 'whitespace_cleaner' as stage_name."""
        _, stage = clean_whitespace("text\n")
        assert stage.stage_name == "whitespace_cleaner"

    def test_should_report_zero_for_clean_input(self):
        """It should report no changes for already-clean input."""
        _, stage = clean_whitespace("Clean text.\n")
        assert stage.changes_made == 0
