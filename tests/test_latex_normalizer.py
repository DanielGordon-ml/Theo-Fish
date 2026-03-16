"""
@file test_latex_normalizer.py
@description Tests for Stage 1: LaTeX delimiter normalizer.
"""

from data_cleaner.stages.latex_normalizer import normalize_latex


class TestInlineDelimiters:
    def test_should_convert_paren_delimiters_to_dollar(self):
        """It should convert \\(...\\) to $...$."""
        text = r"The value \(x + y\) is positive."
        result, stage = normalize_latex(text)
        assert result == "The value $x + y$ is positive."
        assert stage.details["inline_converted"] == 1

    def test_should_handle_multiple_inline(self):
        """It should convert multiple inline delimiters."""
        text = r"Given \(a\) and \(b\), we have \(a + b\)."
        result, stage = normalize_latex(text)
        assert result == "Given $a$ and $b$, we have $a + b$."
        assert stage.details["inline_converted"] == 3

    def test_should_not_touch_existing_dollar_delimiters(self):
        """It should leave existing $...$ delimiters unchanged."""
        text = "The value $x + y$ is positive."
        result, stage = normalize_latex(text)
        assert result == text
        assert stage.details.get("inline_converted", 0) == 0


class TestDisplayDelimiters:
    def test_should_convert_bracket_delimiters_to_double_dollar(self):
        """It should convert \\[...\\] to $$...$$."""
        text = "We know that\n\\[x^2 + y^2 = z^2\\]\nis true."
        result, stage = normalize_latex(text)
        assert result == "We know that\n$$x^2 + y^2 = z^2$$\nis true."
        assert stage.details["display_converted"] == 1

    def test_should_handle_multiline_display(self):
        """It should convert display math spanning multiple lines."""
        text = "Equation:\n\\[\na + b\n= c\n\\]\nEnd."
        result, stage = normalize_latex(text)
        assert result == "Equation:\n$$\na + b\n= c\n$$\nEnd."
        assert stage.details["display_converted"] == 1


class TestCodeBlockProtection:
    def test_should_not_convert_inside_code_blocks(self):
        """It should skip LaTeX delimiters inside fenced code blocks."""
        text = "Text \\(x\\) here.\n```\n\\(y\\)\n```\nMore \\(z\\)."
        result, stage = normalize_latex(text)
        assert "```\n\\(y\\)\n```" in result
        assert result.startswith("Text $x$ here.")
        assert result.endswith("More $z$.")

    def test_should_not_convert_inside_inline_code(self):
        """It should skip delimiters inside inline code spans."""
        text = r"Use `\(x\)` for inline math."
        result, stage = normalize_latex(text)
        assert result == text


class TestSkipLogic:
    def test_should_skip_when_no_paren_or_bracket_delimiters(self):
        """It should skip when text only uses dollar delimiters."""
        text = "We have $x$ and $$y = 1$$."
        result, stage = normalize_latex(text)
        assert result == text
        assert stage.changes_made == 0

    def test_should_return_correct_stage_name(self):
        """It should return 'latex_normalizer' as stage_name."""
        _, stage = normalize_latex("plain text")
        assert stage.stage_name == "latex_normalizer"
