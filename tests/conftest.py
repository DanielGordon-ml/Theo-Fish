"""
@file conftest.py
@description Shared test fixtures.
"""

import pytest
from pathlib import Path


@pytest.fixture
def tmp_data_dir(tmp_path):
    """Create a temporary data directory structure."""
    papers_dir = tmp_path / "papers"
    processed_dir = tmp_path / "processed"
    papers_dir.mkdir()
    processed_dir.mkdir()
    return tmp_path


@pytest.fixture
def sample_csv(tmp_path):
    """Create a sample CSV input file."""
    csv_content = (
        'paper_name,file_path,file_type\n'
        '"Attention Is All You Need",2706.03762,pdf\n'
        '"BERT",1810.04805,html\n'
    )
    csv_file = tmp_path / "papers.csv"
    csv_file.write_text(csv_content)
    return csv_file
