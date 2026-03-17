"""
@file test_artifact_remover.py
@description Tests for Stage 2: HTML and artifact remover.
"""

from data_cleaner.stages.artifact_remover import remove_artifacts


class TestHtmlTableConversion:
    def test_should_convert_simple_table(self):
        """It should convert an HTML table to markdown pipe table."""
        html = (
            "<table><tr><th>A</th><th>B</th></tr><tr><td>1</td><td>2</td></tr></table>"
        )
        result, stage = remove_artifacts(html)
        assert "| A | B |" in result
        assert "| 1 | 2 |" in result
        assert "<table>" not in result
        assert stage.details["tables_converted"] == 1

    def test_should_handle_table_with_no_header(self):
        """It should convert a table that has no th elements."""
        html = "<table><tr><td>X</td><td>Y</td></tr></table>"
        result, _ = remove_artifacts(html)
        assert "| X | Y |" in result
        assert "<table>" not in result


class TestBrTagReplacement:
    def test_should_replace_br_tags(self):
        """It should replace <br> and <br/> with newlines."""
        text = "Line one<br>Line two<br/>Line three"
        result, stage = remove_artifacts(text)
        assert result == "Line one\nLine two\nLine three"
        assert stage.details["br_tags"] == 2


class TestTagUnwrapping:
    def test_should_unwrap_span_tags(self):
        """It should remove span tags but keep their content."""
        text = "The <span>important</span> result."
        result, stage = remove_artifacts(text)
        assert result == "The important result."
        assert stage.details["tags_unwrapped"] >= 1

    def test_should_unwrap_div_tags(self):
        """It should remove div tags but keep their content."""
        text = "<div>Content here</div>"
        result, _ = remove_artifacts(text)
        assert result == "Content here"


class TestArxivLinkSimplification:
    def test_should_simplify_arxiv_cross_refs(self):
        """It should replace ArXiv HTML links with just the text."""
        text = "See [Theorem 1](https://arxiv.org/html/1234.5678v1#S2) for details."
        result, stage = remove_artifacts(text)
        assert result == "See Theorem 1 for details."
        assert stage.details["arxiv_links"] == 1

    def test_should_not_touch_non_arxiv_links(self):
        """It should leave non-ArXiv links untouched."""
        text = "See [docs](https://example.com) for info."
        result, _ = remove_artifacts(text)
        assert result == text


class TestBrokenReferences:
    def test_should_remove_question_mark_refs(self):
        """It should remove [?] broken references."""
        text = "As shown in [?] and proven in [?], we have."
        result, stage = remove_artifacts(text)
        assert "[?]" not in result
        assert stage.details["broken_refs"] == 2

    def test_should_replace_nbsp(self):
        """It should replace non-breaking spaces with regular spaces."""
        text = "word\xa0word"
        result, stage = remove_artifacts(text)
        assert result == "word word"
        assert stage.details["nbsp"] == 1


class TestStageMetadata:
    def test_should_return_correct_stage_name(self):
        """It should return 'artifact_remover' as stage_name."""
        _, stage = remove_artifacts("clean text")
        assert stage.stage_name == "artifact_remover"

    def test_should_report_zero_changes_for_clean_input(self):
        """It should report no changes for text without artifacts."""
        _, stage = remove_artifacts("Just plain text.")
        assert stage.changes_made == 0
