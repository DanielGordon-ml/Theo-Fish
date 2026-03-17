"""
@file test_main_cli.py
@description Tests for the CLI entry point argument parsing and file detection.
"""

import pytest


class TestParseArxivIds:
    """Tests for _parse_arxiv_ids()."""

    def test_it_should_return_single_id_from_positional_arg(self):
        """It should wrap a single arxiv_id in a list."""
        from main import _parse_arxiv_ids

        result = _parse_arxiv_ids("k_strong_price_of_anarchy", None)
        assert result == ["k_strong_price_of_anarchy"]

    def test_it_should_read_ids_from_csv_with_header(self, tmp_path):
        """It should read arxiv_ids from a CSV file with header."""
        from main import _parse_arxiv_ids

        csv_file = tmp_path / "papers.csv"
        csv_file.write_text("arxiv_id\n1904.07272\n1011.4748\n")
        result = _parse_arxiv_ids(None, str(csv_file))
        assert result == ["1904.07272", "1011.4748"]

    def test_it_should_read_ids_from_plain_text_file(self, tmp_path):
        """It should read one ID per line from a plain text file."""
        from main import _parse_arxiv_ids

        txt_file = tmp_path / "papers.txt"
        txt_file.write_text("1904.07272\n1011.4748\n")
        result = _parse_arxiv_ids(None, str(txt_file))
        assert result == ["1904.07272", "1011.4748"]

    def test_it_should_skip_empty_lines(self, tmp_path):
        """It should ignore blank lines in the input file."""
        from main import _parse_arxiv_ids

        txt_file = tmp_path / "papers.txt"
        txt_file.write_text("1904.07272\n\n1011.4748\n\n")
        result = _parse_arxiv_ids(None, str(txt_file))
        assert result == ["1904.07272", "1011.4748"]

    def test_it_should_raise_when_no_input_provided(self):
        """It should raise SystemExit when no arxiv_id or csv is given."""
        from main import _parse_arxiv_ids

        with pytest.raises(SystemExit):
            _parse_arxiv_ids(None, None)
