"""
@file test_input_reader.py
@description Tests for input reading, normalization, and deduplication.
"""

from data_loader.input_reader import (
    normalize_arxiv_id,
    read_csv,
    read_cli_papers,
    merge_inputs,
)
from data_loader.models import PaperInput


class TestNormalizeArxivId:
    def test_raw_id(self):
        """It should pass through a raw ArXiv ID unchanged."""
        assert normalize_arxiv_id("2706.03762") == "2706.03762"

    def test_versioned_id(self):
        """It should strip version suffix."""
        assert normalize_arxiv_id("2706.03762v1") == "2706.03762"

    def test_abs_url(self):
        """It should extract ID from abs URL."""
        assert normalize_arxiv_id("https://arxiv.org/abs/2706.03762") == "2706.03762"

    def test_abs_url_versioned(self):
        """It should extract ID from versioned abs URL."""
        assert normalize_arxiv_id("https://arxiv.org/abs/2706.03762v2") == "2706.03762"

    def test_pdf_url(self):
        """It should extract ID from pdf URL."""
        assert normalize_arxiv_id("https://arxiv.org/pdf/2706.03762") == "2706.03762"

    def test_arxiv_prefix(self):
        """It should strip arxiv: prefix."""
        assert normalize_arxiv_id("arxiv:2706.03762") == "2706.03762"

    def test_legacy_id(self):
        """It should handle legacy category/number IDs."""
        assert normalize_arxiv_id("cs/0512078v2") == "cs/0512078"

    def test_invalid_returns_none(self):
        """It should return None for unrecognized input."""
        assert normalize_arxiv_id("not-an-id") is None

    def test_empty_string_returns_none(self):
        """It should return None for empty string."""
        assert normalize_arxiv_id("") is None


class TestReadCsv:
    def test_reads_valid_csv(self, sample_csv):
        """It should parse all valid rows from CSV."""
        papers = read_csv(sample_csv)
        assert len(papers) == 2
        assert papers[0].arxiv_id == "2706.03762"
        assert papers[0].paper_name == "Attention Is All You Need"
        assert papers[0].file_type == "pdf"
        assert papers[1].arxiv_id == "1810.04805"

    def test_skips_invalid_ids(self, tmp_path):
        """It should skip rows with invalid ArXiv IDs."""
        csv_file = tmp_path / "bad.csv"
        csv_file.write_text(
            "paper_name,file_path,file_type\n"
            '"Good Paper",2706.03762,pdf\n'
            '"Bad Paper",not-a-valid-id,pdf\n'
        )
        papers = read_csv(csv_file)
        assert len(papers) == 1
        assert papers[0].arxiv_id == "2706.03762"

    def test_empty_csv(self, tmp_path):
        """It should return empty list for header-only CSV."""
        csv_file = tmp_path / "empty.csv"
        csv_file.write_text("paper_name,file_path,file_type\n")
        papers = read_csv(csv_file)
        assert papers == []

    def test_detects_local_pdf(self, tmp_path):
        """It should detect .pdf extension and create local PaperInput."""
        csv_file = tmp_path / "local.csv"
        csv_file.write_text(
            'paper_name,file_path,file_type\n"My Local Paper",my_paper.pdf,PDF\n'
        )
        papers = read_csv(csv_file)
        assert len(papers) == 1
        assert papers[0].is_local is True
        assert papers[0].arxiv_id == "my_paper"
        assert papers[0].local_filename == "my_paper.pdf"
        assert papers[0].paper_name == "My Local Paper"
        assert papers[0].file_type == "pdf"

    def test_mixed_csv_arxiv_and_local(self, tmp_path):
        """It should handle CSV with both ArXiv IDs and local PDFs."""
        csv_file = tmp_path / "mixed.csv"
        csv_file.write_text(
            "paper_name,file_path,file_type\n"
            '"ArXiv Paper",2706.03762,pdf\n'
            '"Local Paper",achieving_pareto.pdf,PDF\n'
        )
        papers = read_csv(csv_file)
        assert len(papers) == 2
        # First is ArXiv
        assert papers[0].is_local is False
        assert papers[0].arxiv_id == "2706.03762"
        # Second is local PDF
        assert papers[1].is_local is True
        assert papers[1].arxiv_id == "achieving_pareto"
        assert papers[1].local_filename == "achieving_pareto.pdf"

    def test_pdf_extension_case_insensitive(self, tmp_path):
        """It should detect .PDF extension regardless of case."""
        csv_file = tmp_path / "case.csv"
        csv_file.write_text(
            'paper_name,file_path,file_type\n"Paper",my_paper.PDF,pdf\n'
        )
        papers = read_csv(csv_file)
        assert len(papers) == 1
        assert papers[0].is_local is True


class TestReadCliPapers:
    def test_reads_cli_papers(self):
        """It should create PaperInput list from CLI IDs."""
        papers = read_cli_papers(["2706.03762", "1810.04805"])
        assert len(papers) == 2
        assert papers[0].arxiv_id == "2706.03762"
        assert papers[0].paper_name is None

    def test_skips_invalid_cli(self):
        """It should skip invalid IDs from CLI."""
        papers = read_cli_papers(["2706.03762", "garbage"])
        assert len(papers) == 1


class TestMergeInputs:
    def test_deduplicates(self):
        """It should deduplicate by ArXiv ID, CSV taking priority."""
        csv_papers = [PaperInput(arxiv_id="2706.03762", paper_name="From CSV")]
        cli_papers = [PaperInput(arxiv_id="2706.03762")]
        merged = merge_inputs(csv_papers, cli_papers)
        assert len(merged) == 1
        assert merged[0].paper_name == "From CSV"  # CSV entry takes priority

    def test_merges_unique(self):
        """It should keep all unique papers from both sources."""
        csv_papers = [PaperInput(arxiv_id="2706.03762", paper_name="Paper A")]
        cli_papers = [PaperInput(arxiv_id="1810.04805")]
        merged = merge_inputs(csv_papers, cli_papers)
        assert len(merged) == 2
