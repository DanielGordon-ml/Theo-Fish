"""
@file __init__.py
@description Knowledge Graph Builder — extracts mathematical entities and
relationships from cleaned ArXiv papers and outputs an Obsidian vault.
"""

from graph_builder.errors import GraphBuilderError
from graph_builder.models import BatchBuildResult, BuildResult
from graph_builder.sdk import build_graph, build_graphs, is_built

__all__ = [
    "build_graph",
    "build_graphs",
    "is_built",
    "BuildResult",
    "BatchBuildResult",
    "GraphBuilderError",
]
