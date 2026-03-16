"""
@file pipeline_writer.py
@description Neo4j write helpers for the orchestrator pipeline. Handles
granular per-concept transactions, claim writes, and batched edge writes.
"""

import logging
from datetime import datetime

from graph_builder.extraction.concept_merger import MergedConcept
from graph_builder.graph.graph_writer import GraphWriter
from graph_builder.models.claim import ClaimNode
from graph_builder.models.edges import ClaimEdge, CouplingEdge
from graph_builder.models.provenance import FormulationEdge
from graph_builder.models.source import SourceNode

logger = logging.getLogger("graph_builder")


def build_source_node(arxiv_id: str, title: str) -> SourceNode:
    """Build a SourceNode for the paper.

    @param arxiv_id ArXiv identifier
    @param title Paper title
    @returns Populated SourceNode
    """
    return SourceNode(
        arxiv_id=arxiv_id,
        title=title,
        date_extracted=datetime.now().isoformat(),
    )


async def write_to_neo4j(
    writer: GraphWriter,
    source: SourceNode,
    merged: list[MergedConcept],
    claims: list[ClaimNode],
    claim_edges: list[ClaimEdge],
    coupling_edges: list[CouplingEdge],
) -> dict[str, int]:
    """Write all extracted data to Neo4j with granular transactions.

    Each concept is its own transaction. Edges are batched per type.

    @param writer GraphWriter instance
    @param source SourceNode to write first
    @param merged All merged concepts with provenance
    @param claims All claim nodes
    @param claim_edges All claim-to-claim edges
    @param coupling_edges All claim-to-concept edges
    @returns Dict with concepts, claims, edges counts
    """
    await writer.write_source(source)

    concept_count = await _write_concepts(writer, merged)
    claim_count = await _write_claims(writer, claims, source.arxiv_id)
    edge_count = await _write_edges(writer, claim_edges, coupling_edges)

    return {
        "concepts": concept_count,
        "claims": claim_count,
        "edges": edge_count,
    }


async def _write_concepts(
    writer: GraphWriter,
    merged: list[MergedConcept],
) -> int:
    """Write each concept in its own transaction.

    @param writer GraphWriter instance
    @param merged Merged concepts with provenance
    @returns Number of concepts written
    """
    count = 0
    for m in merged:
        try:
            await writer.write_concept(m.concept)
            form_edge = FormulationEdge(
                match_method=m.dedup_result.match_method,
                match_confidence=m.dedup_result.match_confidence,
            )
            await writer.write_provenance(m.provenance, form_edge)
            count += 1
        except Exception as err:
            logger.error(
                "Failed to write concept '%s': %s", m.concept.slug, err,
            )
    return count


async def _write_claims(
    writer: GraphWriter,
    claims: list[ClaimNode],
    arxiv_id: str,
) -> int:
    """Write each claim node.

    @param writer GraphWriter instance
    @param claims Claim nodes to write
    @param arxiv_id ArXiv ID for SOURCED_FROM edges
    @returns Number of claims written
    """
    count = 0
    for claim in claims:
        try:
            await writer.write_claim(claim, arxiv_id)
            count += 1
        except Exception as err:
            logger.error(
                "Failed to write claim '%s': %s", claim.slug, err,
            )
    return count


async def _write_edges(
    writer: GraphWriter,
    claim_edges: list[ClaimEdge],
    coupling_edges: list[CouplingEdge],
) -> int:
    """Batch-write all edges.

    @param writer GraphWriter instance
    @param claim_edges Claim-to-claim edges
    @param coupling_edges Claim-to-concept ABOUT edges
    @returns Total edge count
    """
    count = 0
    try:
        await writer.write_claim_edges(claim_edges)
        count += len(claim_edges)
    except Exception as err:
        logger.error("Failed to write claim edges: %s", err)

    try:
        await writer.write_coupling_edges(coupling_edges)
        count += len(coupling_edges)
    except Exception as err:
        logger.error("Failed to write coupling edges: %s", err)

    return count
