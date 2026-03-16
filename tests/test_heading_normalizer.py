"""
@file test_heading_normalizer.py
@description Tests for Stage 3: heading hierarchy normalizer.
"""

from data_cleaner.stages.heading_normalizer import normalize_headings


class TestMineruDemotion:
    def test_should_demote_roman_numeral_sections_to_h2(self):
        """It should demote numbered sections with Roman numerals to h2."""
        text = "# Paper Title\n\n# I. Introduction\n\nSome text.\n\n# II. Methods\n"
        result, stage = normalize_headings(text, converter="mineru")
        assert "## I. Introduction" in result
        assert "## II. Methods" in result
        # Title stays h1
        assert result.startswith("# Paper Title")
        assert stage.changes_made > 0

    def test_should_demote_letter_subsections_to_h3(self):
        """It should demote letter subsections (A., B.) to h3."""
        text = "# Title\n\n# I. Main\n\n# A. Sub One\n\n# B. Sub Two\n"
        result, stage = normalize_headings(text, converter="mineru")
        assert "### A. Sub One" in result
        assert "### B. Sub Two" in result

    def test_should_demote_abstract_and_references_to_h2(self):
        """It should demote Abstract, References, Appendix to h2."""
        text = "# Title\n\n# Abstract\n\nText.\n\n# References\n"
        result, stage = normalize_headings(text, converter="mineru")
        assert "## Abstract" in result
        assert "## References" in result

    def test_should_keep_first_h1_as_title(self):
        """It should preserve the first heading as h1 (paper title)."""
        text = "# My Paper Title\n\n# I. Intro\n"
        result, _ = normalize_headings(text, converter="mineru")
        assert result.startswith("# My Paper Title")


class TestArxiv2mdPromotion:
    def test_should_promote_headings_to_fill_from_h1(self):
        """It should promote h3-h6 range so the minimum becomes h1."""
        text = "### Paper Title\n\n#### Section One\n\n##### Subsection\n"
        result, stage = normalize_headings(text, converter="arxiv2md")
        assert result.startswith("# Paper Title")
        assert "## Section One" in result
        assert "### Subsection" in result
        assert stage.changes_made > 0

    def test_should_not_change_already_correct_hierarchy(self):
        """It should skip when headings already start at h1."""
        text = "# Title\n\n## Section\n\n### Sub\n"
        result, stage = normalize_headings(text, converter="arxiv2md")
        assert result == text
        assert stage.changes_made == 0

    def test_should_handle_h4_minimum(self):
        """It should promote h4 minimum to h1 (shift by 3)."""
        text = "#### Title\n\n##### Section\n\n###### Detail\n"
        result, _ = normalize_headings(text, converter="arxiv2md")
        assert "# Title" in result
        assert "## Section" in result
        assert "### Detail" in result


class TestDuplicateTitleRemoval:
    def test_should_remove_duplicate_title(self):
        """It should remove a second heading that matches the first."""
        text = "# My Paper\n\n# My Paper\n\nContent."
        result, stage = normalize_headings(text, converter="mineru")
        assert result.count("# My Paper") == 1
        assert stage.details.get("duplicate_titles", 0) == 1


class TestCodeBlockProtection:
    def test_should_not_modify_headings_in_code_blocks(self):
        """It should skip headings inside fenced code blocks."""
        text = "# Title\n\n```\n### Not a heading\n```\n\n## Real\n"
        result, _ = normalize_headings(text, converter="arxiv2md")
        assert "### Not a heading" in result


class TestStageMetadata:
    def test_should_return_correct_stage_name(self):
        """It should return 'heading_normalizer' as stage_name."""
        _, stage = normalize_headings("plain text", converter="mineru")
        assert stage.stage_name == "heading_normalizer"

    def test_should_default_to_mineru_converter(self):
        """It should work with default converter parameter."""
        text = "# Title\n\n# Abstract\n\nText."
        result, _ = normalize_headings(text)
        assert "## Abstract" in result
