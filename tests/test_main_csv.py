"""
@file test_main_csv.py
@description Tests for _read_id_file multi-column CSV parsing support.
"""



class TestReadIdFileMultiColumnCsv:
    """Tests for _read_id_file() with multi-column CSV format."""

    def test_it_should_parse_multi_column_csv_with_local_pdfs(self, tmp_path):
        """It should extract PDF stems as IDs from a multi-column CSV."""
        from main import _read_id_file

        csv_file = tmp_path / "papers.csv"
        csv_file.write_text(
            "paper_name,file_path,file_type\n"
            "K-Strong Price of Anarchy,k_strong_price_of_anarchy.pdf,PDF\n"
            "Some Other Paper,some_other_paper.pdf,PDF\n"
        )
        result = _read_id_file(str(csv_file))
        assert result == [
            "k_strong_price_of_anarchy",
            "some_other_paper",
        ]

    def test_it_should_parse_multi_column_csv_with_arxiv_ids(self, tmp_path):
        """It should normalize arxiv IDs from the file_path column."""
        from main import _read_id_file

        csv_file = tmp_path / "papers.csv"
        csv_file.write_text(
            "paper_name,file_path,file_type\n"
            "A Paper,2301.12345,HTML\n"
            "Another,math-ph/0101023,HTML\n"
        )
        result = _read_id_file(str(csv_file))
        assert result == ["2301.12345", "math-ph/0101023"]

    def test_it_should_parse_single_column_plain_text(self, tmp_path):
        """It should read one ID per line from a plain text file."""
        from main import _read_id_file

        txt_file = tmp_path / "papers.txt"
        txt_file.write_text("1904.07272\n1011.4748\n")
        result = _read_id_file(str(txt_file))
        assert result == ["1904.07272", "1011.4748"]

    def test_it_should_skip_header_in_single_column_format(self, tmp_path):
        """It should skip the arxiv_id header row in single-column format."""
        from main import _read_id_file

        csv_file = tmp_path / "papers.csv"
        csv_file.write_text("arxiv_id\n1904.07272\n1011.4748\n")
        result = _read_id_file(str(csv_file))
        assert result == ["1904.07272", "1011.4748"]

    def test_it_should_return_empty_list_for_empty_file(self, tmp_path):
        """It should return an empty list for an empty file."""
        from main import _read_id_file

        txt_file = tmp_path / "empty.txt"
        txt_file.write_text("")
        result = _read_id_file(str(txt_file))
        assert result == []
