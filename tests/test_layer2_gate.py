"""
@file test_layer2_gate.py
@description Layer 2 integration gate — validates models + graph agree on Neo4j schema.
Must pass before building Layer 3.
"""

import pytest

from graph_builder.graph.graph_reader import GraphReader
from graph_builder.graph.graph_writer import GraphWriter
from graph_builder.models.claim import ClaimNode
from graph_builder.models.concept import ConceptNode
from graph_builder.models.edges import ClaimEdge, ConceptEdge, CouplingEdge
from graph_builder.models.provenance import FormulationEdge, ProvenanceNode
from graph_builder.models.source import SourceNode

pytestmark = [pytest.mark.integration, pytest.mark.asyncio]


class TestLayer2Gate:
    """End-to-end write-read tests for all node types and edge types."""

    async def test_concept_write_read_roundtrip(self, neo4j_client):
        """It should write a Concept and read it back with all fields."""
        writer = GraphWriter(neo4j_client)
        reader = GraphReader(neo4j_client)

        await writer.create_schema_constraints()

        concept = ConceptNode(
            name="Markov Decision Process",
            semantic_type="structure",
            formal_spec="(S, A, P, R, γ)",
            components=["state_space", "action_space"],
            embedding=[0.1] * 10,
        )
        await writer.write_concept(concept)

        result = await reader.get_existing_concept("markov-decision-process")
        assert result is not None
        assert result.semantic_type == "structure"
        assert result.formal_spec == "(S, A, P, R, γ)"

    async def test_claim_write_with_about_edge(self, neo4j_client):
        """It should write a Claim with ABOUT -> Concept coupling edge."""
        writer = GraphWriter(neo4j_client)
        await writer.create_schema_constraints()

        concept = ConceptNode(name="regret", semantic_type="quantity")
        await writer.write_concept(concept)

        source = SourceNode(arxiv_id="1904.07272", title="Intro Bandits")
        await writer.write_source(source)

        claim = ClaimNode(
            source_paper_slug="intro-bandits",
            label="Theorem 1.1",
            claim_type="theorem",
            conclusion="R_T <= sqrt(KT ln T)",
        )
        await writer.write_claim(claim, "1904.07272")

        coupling = CouplingEdge(
            claim_slug=claim.slug,
            concept_slug="regret",
            role="primary",
        )
        await writer.write_coupling_edges([coupling])

        result = await neo4j_client.execute_read(
            "MATCH (cl:Claim)-[r:ABOUT]->(c:Concept) "
            "RETURN cl.slug AS claim_slug, c.slug AS concept_slug, r.role AS role"
        )
        assert len(result) == 1
        assert result[0]["role"] == "primary"

    async def test_source_and_provenance(self, neo4j_client):
        """It should write Source + Provenance with FORMULATION_OF + SOURCED_FROM."""
        writer = GraphWriter(neo4j_client)
        await writer.create_schema_constraints()

        concept = ConceptNode(name="Nash Equilibrium", semantic_type="structure")
        await writer.write_concept(concept)

        source = SourceNode(arxiv_id="2103.04523", title="Game Theory")
        await writer.write_source(source)

        prov = ProvenanceNode(
            concept_slug="nash-equilibrium",
            source_arxiv_id="2103.04523",
            formulation="A strategy profile from which no player deviates",
            extraction_confidence=0.92,
        )
        form_edge = FormulationEdge(
            match_method="embedding+llm",
            match_confidence=0.87,
        )
        await writer.write_provenance(prov, form_edge)

        result = await neo4j_client.execute_read(
            "MATCH (p:Provenance)-[r:FORMULATION_OF]->(c:Concept) "
            "RETURN r.match_method AS match_method, r.match_confidence AS match_confidence"
        )
        assert len(result) == 1
        assert result[0]["match_method"] == "embedding+llm"

    async def test_all_concept_edge_types(self, neo4j_client):
        """It should write a CONCEPT_REL edge with edge_type and attributes."""
        writer = GraphWriter(neo4j_client)
        await writer.create_schema_constraints()

        c1 = ConceptNode(name="POMDP", semantic_type="structure")
        c2 = ConceptNode(name="MDP", semantic_type="structure")
        await writer.write_concept(c1)
        await writer.write_concept(c2)

        edges = [
            ConceptEdge(
                source_slug="pomdp",
                target_slug="mdp",
                edge_type="generalizes",
                attributes={"condition": "full observability"},
            ),
        ]
        await writer.write_concept_edges(edges)

        result = await neo4j_client.execute_read(
            "MATCH (a:Concept)-[r:CONCEPT_REL]->(b:Concept) "
            "RETURN a.slug AS source, b.slug AS target, "
            "r.edge_type AS edge_type, r.condition AS condition"
        )
        assert len(result) == 1
        assert result[0]["edge_type"] == "generalizes"
        assert result[0]["condition"] == "full observability"

    async def test_all_claim_edge_types(self, neo4j_client):
        """It should write a CLAIM_REL edge with edge_type and role attribute."""
        writer = GraphWriter(neo4j_client)
        await writer.create_schema_constraints()

        source = SourceNode(arxiv_id="1904.07272", title="Paper")
        await writer.write_source(source)

        c1 = ClaimNode(
            source_paper_slug="paper",
            label="Theorem 1",
            claim_type="theorem",
        )
        c2 = ClaimNode(
            source_paper_slug="paper",
            label="Lemma 1",
            claim_type="lemma",
        )
        await writer.write_claim(c1, "1904.07272")
        await writer.write_claim(c2, "1904.07272")

        edges = [
            ClaimEdge(
                source_slug=c1.slug,
                target_slug=c2.slug,
                edge_type="depends_on",
                attributes={"role": "bound"},
            ),
        ]
        await writer.write_claim_edges(edges)

        result = await neo4j_client.execute_read(
            "MATCH (a:Claim)-[r:CLAIM_REL]->(b:Claim) "
            "RETURN r.edge_type AS edge_type, r.role AS role"
        )
        assert len(result) == 1
        assert result[0]["edge_type"] == "depends_on"
        assert result[0]["role"] == "bound"

    async def test_field_ownership_on_merge(self, neo4j_client):
        """It should preserve human-owned fields when MERGEing same concept."""
        writer = GraphWriter(neo4j_client)
        await writer.create_schema_constraints()

        c1 = ConceptNode(
            name="Nash Equilibrium",
            semantic_type="structure",
            formal_spec="original spec",
        )
        await writer.write_concept(c1)

        # Simulate a human edit by directly setting human_notes
        await neo4j_client.execute_write(
            "MATCH (c:Concept {slug: 'nash-equilibrium'}) "
            "SET c.human_notes = 'manually curated'"
        )

        # Second write (re-extraction) — human_notes should survive
        c2 = ConceptNode(
            name="Nash Equilibrium",
            semantic_type="structure",
            formal_spec="updated spec",
            human_notes="should be ignored",
        )
        await writer.write_concept(c2)

        result = await neo4j_client.execute_read(
            "MATCH (c:Concept {slug: 'nash-equilibrium'}) "
            "RETURN c.human_notes AS human_notes, c.formal_spec AS formal_spec"
        )
        assert result[0]["human_notes"] == "manually curated"
        assert result[0]["formal_spec"] == "updated spec"

    async def test_is_paper_built(self, neo4j_client):
        """It should detect whether a paper's Source node exists."""
        writer = GraphWriter(neo4j_client)
        reader = GraphReader(neo4j_client)
        await writer.create_schema_constraints()

        assert await reader.is_paper_built("9999.99999") is False

        source = SourceNode(arxiv_id="9999.99999", title="Test")
        await writer.write_source(source)

        assert await reader.is_paper_built("9999.99999") is True
