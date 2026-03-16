"""
@file __init__.py
@description Public API for the v2 dual-graph knowledge graph builder.
"""

from graph_builder.graph.graph_reader import GraphReader
from graph_builder.orchestrator.orchestrator import PipelineOptions, process_paper
from graph_builder.vault.obsidian_exporter import export_vault
from graph_builder.vault.sync_back import sync_back

try:
    # batch_processor is added in Task 24; import is optional until then.
    from graph_builder.orchestrator.batch_processor import process_batch
except ImportError:
    process_batch = None  # type: ignore[assignment]

__all__ = [
    "process_paper",
    "process_batch",
    "PipelineOptions",
    "export_vault",
    "sync_back",
    "GraphReader",
]
