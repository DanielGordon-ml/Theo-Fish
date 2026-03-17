"""
@file test_section_splitter.py
@description Tests for section splitter with TOC stripping and stub detection.
"""

from graph_builder.extraction.section_splitter import (
    is_stub_section,
    split_into_sections,
    strip_toc,
)


class TestStripToc:
    """Tests for strip_toc()."""

    def test_it_should_remove_contents_heading_with_bullet_list(self):
        """Strip a TOC block starting with # Contents."""
        text = (
            "# Contents\n\n"
            "- [Introduction](#introduction)\n"
            "- [Methods](#methods)\n\n"
            "# Introduction\n\n"
            "This is the intro."
        )
        result = strip_toc(text)
        assert "# Contents" not in result
        assert "# Introduction" in result
        assert "This is the intro." in result

    def test_it_should_handle_no_toc(self):
        """Text without a TOC is returned unchanged."""
        text = "# Introduction\n\nSome content here."
        result = strip_toc(text)
        assert result == text

    def test_it_should_handle_numbered_toc_items(self):
        """Strip TOC with numbered list items."""
        text = "# Contents\n\n1. Introduction\n2. Methods\n\n# Introduction\n\nContent."
        result = strip_toc(text)
        assert "# Contents" not in result
        assert "# Introduction" in result

    def test_it_should_handle_table_of_contents_heading(self):
        """Strip TOC with 'Table of Contents' heading variant."""
        text = "# Table of Contents\n\n- Intro\n- Methods\n\n# Intro\n\nContent."
        result = strip_toc(text)
        assert "Table of Contents" not in result
        assert "# Intro" in result


class TestSplitIntoSections:
    """Tests for split_into_sections()."""

    def test_it_should_split_on_h1_headings(self):
        """H1 headings create section boundaries."""
        filler = "This is enough content to exceed the stub threshold easily."
        text = f"# Section One\n\n{filler}\n\n# Section Two\n\n{filler}"
        sections = split_into_sections(text)
        assert len(sections) == 2
        assert sections[0].heading == "Section One"
        assert sections[1].heading == "Section Two"

    def test_it_should_split_on_h2_headings(self):
        """H2 headings also create section boundaries."""
        filler = "This is enough content to exceed the stub threshold easily."
        text = f"# Main Title\n\n{filler}\n\n## Sub Section\n\n{filler}"
        sections = split_into_sections(text)
        assert len(sections) == 2
        assert sections[1].heading == "Sub Section"

    def test_it_should_track_heading_level(self):
        """Section level matches the heading depth."""
        filler = "This is enough content to exceed the stub threshold easily."
        text = f"# H1 Title\n\n{filler}\n\n## H2 Title\n\n{filler}"
        sections = split_into_sections(text)
        assert sections[0].level == 1
        assert sections[1].level == 2

    def test_it_should_assign_sequential_indices(self):
        """Sections get sequential zero-based indices."""
        filler = "This is enough content to exceed the stub threshold easily."
        text = f"# A\n\n{filler}\n\n# B\n\n{filler}\n\n# C\n\n{filler}"
        sections = split_into_sections(text)
        assert [s.index for s in sections] == [0, 1, 2]

    def test_it_should_calculate_char_count(self):
        """char_count reflects the content length."""
        filler = "This is enough content to exceed the stub threshold easily."
        text = f"# Title\n\n{filler}"
        sections = split_into_sections(text)
        assert sections[0].char_count == len(sections[0].content)

    def test_it_should_filter_stub_sections(self):
        """Sections with <50 chars of non-heading content are excluded."""
        text = (
            "# Real Section\n\n"
            "This section has enough content to pass the filter.\n\n"
            "# Stub\n\n"
            "tiny\n\n"
            "# Another Real\n\n"
            "This also has enough content to pass the stub filter."
        )
        sections = split_into_sections(text)
        headings = [s.heading for s in sections]
        assert "Stub" not in headings
        assert "Real Section" in headings
        assert "Another Real" in headings

    def test_it_should_handle_text_before_first_heading(self):
        """Content before the first heading is captured as a section."""
        filler = "This is enough content to exceed the stub threshold easily."
        text = (
            "Some preamble content that is long enough.\n"
            "It has multiple lines to pass the stub filter.\n\n"
            f"# First Heading\n\n{filler}"
        )
        sections = split_into_sections(text)
        assert len(sections) == 2
        assert sections[0].heading == ""

    def test_it_should_subsplit_oversized_sections(self):
        """Sections exceeding MAX_SECTION_CHARS are sub-split on H3."""
        # Build content large enough to trigger sub-splitting
        large_block = "x" * 16_000
        text = (
            "# Big Section\n\n"
            f"{large_block}\n\n"
            "### Sub A\n\n"
            f"{large_block}\n\n"
            "### Sub B\n\n"
            "More content that is long enough to pass filter."
        )
        sections = split_into_sections(text)
        # Should be split into sub-sections
        assert len(sections) >= 2


class TestIsStubSection:
    """Tests for is_stub_section()."""

    def test_it_should_detect_short_content(self):
        """Content under 50 chars is a stub."""
        assert is_stub_section("tiny") is True

    def test_it_should_accept_long_content(self):
        """Content over 50 chars is not a stub."""
        content = "x" * 51
        assert is_stub_section(content) is False

    def test_it_should_detect_whitespace_only_as_stub(self):
        """Whitespace-only content is a stub."""
        assert is_stub_section("   \n\n  ") is True

    def test_it_should_detect_empty_as_stub(self):
        """Empty string is a stub."""
        assert is_stub_section("") is True
