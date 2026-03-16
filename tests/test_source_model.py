"""
@file test_source_model.py
@description Tests for SourceNode model.
"""

from graph_builder.models.source import SourceNode


class TestSourceNode:
    def test_creation_with_arxiv_id(self):
        """It should create with arxiv_id."""
        node = SourceNode(arxiv_id="1904.07272", title="Intro to Bandits")
        assert node.arxiv_id == "1904.07272"

    def test_authors_list(self):
        """It should store authors as list."""
        node = SourceNode(arxiv_id="1904.07272", authors=["A. Slivkins"])
        assert node.authors == ["A. Slivkins"]
