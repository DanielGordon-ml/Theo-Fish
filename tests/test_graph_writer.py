"""
@file test_graph_writer.py
@description Unit tests for GraphWriter — all Neo4j calls are mocked.
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

from graph_builder.graph.graph_writer import GraphWriter
from graph_builder.models.claim import ClaimNode
from graph_builder.models.concept import ConceptNode
from graph_builder.models.edges import ClaimEdge, ConceptEdge, CouplingEdge
from graph_builder.models.provenance import FormulationEdge, ProvenanceNode
from graph_builder.models.source import SourceNode


def _make_mock_client() -> MagicMock:
    """Build a mock Neo4jClient with async write/read methods."""
    client = MagicMock()
    client.execute_write = AsyncMock(return_value=[])
    client.execute_read = AsyncMock(return_value=[])
    client.execute_write_tx = AsyncMock(return_value=None)
    return client


class TestWriteConcept:
    """Tests for GraphWriter.write_concept()."""

    @pytest.mark.asyncio
    async def test_it_should_merge_concept_by_slug(self):
        """MERGE uses slug as the key and sets pipeline-owned fields."""
        mock_client = _make_mock_client()
        writer = GraphWriter(mock_client)

        concept = ConceptNode(
            name="Banach Space",
            semantic_type="space",
            formal_spec="(V, ||·||)",
            aliases=["B-space"],
            status="canonical",
        )
        await writer.write_concept(concept)

        mock_client.execute_write.assert_awaited_once()
        cypher, kwargs = _extract_call(mock_client.execute_write)
        assert "MERGE" in cypher
        assert kwargs["slug"] == "banach-space"
        assert kwargs["semantic_type"] == "space"
        assert kwargs["formal_spec"] == "(V, ||·||)"

    @pytest.mark.asyncio
    async def test_it_should_preserve_human_owned_fields_on_merge(self):
        """Human-owned fields use COALESCE so existing values survive."""
        mock_client = _make_mock_client()
        writer = GraphWriter(mock_client)

        concept = ConceptNode(
            name="Hilbert Space",
            semantic_type="space",
            canonical_definition="A complete inner product space.",
        )
        await writer.write_concept(concept)

        cypher, _ = _extract_call(mock_client.execute_write)
        # ON MATCH should use COALESCE for human-owned fields
        assert "COALESCE(c.name, $name)" in cypher
        assert "COALESCE(c.canonical_definition, $canonical_definition)" in cypher
        assert "COALESCE(c.human_notes, $human_notes)" in cypher


class TestWriteClaim:
    """Tests for GraphWriter.write_claim()."""

    @pytest.mark.asyncio
    async def test_it_should_create_claim_with_sourced_from_edge(self):
        """CREATE claim node plus SOURCED_FROM edge to source."""
        mock_client = _make_mock_client()
        writer = GraphWriter(mock_client)

        claim = ClaimNode(
            source_paper_slug="2301-00001",
            label="Theorem 3.1",
            claim_type="theorem",
            statement="Every Banach space is complete.",
        )
        await writer.write_claim(claim, source_arxiv_id="2301.00001")

        mock_client.execute_write.assert_awaited_once()
        cypher, kwargs = _extract_call(mock_client.execute_write)
        assert "CREATE" in cypher
        assert "SOURCED_FROM" in cypher
        assert kwargs["source_arxiv_id"] == "2301.00001"
        assert kwargs["slug"] == claim.slug
        assert kwargs["claim_type"] == "theorem"


class TestWriteProvenance:
    """Tests for GraphWriter.write_provenance()."""

    @pytest.mark.asyncio
    async def test_it_should_create_provenance_with_edges(self):
        """CREATE provenance + FORMULATION_OF to concept + SOURCED_FROM to source."""
        mock_client = _make_mock_client()
        writer = GraphWriter(mock_client)

        prov = ProvenanceNode(
            concept_slug="banach-space",
            source_arxiv_id="2301.00001",
            formulation="A Banach space is ...",
            extraction_confidence=0.95,
        )
        form_edge = FormulationEdge(
            match_method="embedding",
            match_confidence=0.92,
        )
        await writer.write_provenance(prov, form_edge)

        mock_client.execute_write.assert_awaited_once()
        cypher, kwargs = _extract_call(mock_client.execute_write)
        assert "FORMULATION_OF" in cypher
        assert "SOURCED_FROM" in cypher
        assert kwargs["match_method"] == "embedding"
        assert kwargs["match_confidence"] == 0.92
        assert kwargs["concept_slug"] == "banach-space"
        assert kwargs["source_arxiv_id"] == "2301.00001"


class TestWriteEdgesBatch:
    """Tests for batched edge writing."""

    @pytest.mark.asyncio
    async def test_it_should_write_concept_edges_in_single_tx(self):
        """Multiple concept edges execute inside one transaction."""
        mock_client = _make_mock_client()
        writer = GraphWriter(mock_client)

        edges = [
            ConceptEdge(
                source_slug="banach-space",
                target_slug="normed-space",
                edge_type="SPECIALIZES",
            ),
            ConceptEdge(
                source_slug="hilbert-space",
                target_slug="banach-space",
                edge_type="SPECIALIZES",
            ),
        ]
        await writer.write_concept_edges(edges)

        mock_client.execute_write_tx.assert_awaited_once()
        tx_func = mock_client.execute_write_tx.call_args[0][0]
        # Verify tx_func is callable (it will be called with a tx)
        assert callable(tx_func)

    @pytest.mark.asyncio
    async def test_it_should_write_claim_edges_in_single_tx(self):
        """Multiple claim edges execute inside one transaction."""
        mock_client = _make_mock_client()
        writer = GraphWriter(mock_client)

        edges = [
            ClaimEdge(
                source_slug="paper--thm-1",
                target_slug="paper--lemma-1",
                edge_type="DEPENDS_ON",
            ),
        ]
        await writer.write_claim_edges(edges)

        mock_client.execute_write_tx.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_it_should_write_coupling_edges_in_single_tx(self):
        """Coupling (ABOUT) edges execute inside one transaction."""
        mock_client = _make_mock_client()
        writer = GraphWriter(mock_client)

        edges = [
            CouplingEdge(
                claim_slug="paper--thm-1",
                concept_slug="banach-space",
                role="primary",
            ),
        ]
        await writer.write_coupling_edges(edges)

        mock_client.execute_write_tx.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_it_should_issue_cypher_for_each_edge_in_tx(self):
        """The tx function runs tx.run once per edge."""
        mock_client = _make_mock_client()
        writer = GraphWriter(mock_client)

        edges = [
            ConceptEdge(
                source_slug="a",
                target_slug="b",
                edge_type="RELATES_TO",
            ),
            ConceptEdge(
                source_slug="c",
                target_slug="d",
                edge_type="SPECIALIZES",
            ),
        ]

        # Capture the tx_func and run it with a mock tx
        captured_func = None

        async def capture_tx(func):
            nonlocal captured_func
            captured_func = func

        mock_client.execute_write_tx = capture_tx
        await writer.write_concept_edges(edges)

        mock_tx = AsyncMock()
        mock_result = AsyncMock()
        mock_result.consume = AsyncMock()
        mock_tx.run = AsyncMock(return_value=mock_result)
        await captured_func(mock_tx)

        assert mock_tx.run.call_count == 2


class TestWriteSource:
    """Tests for GraphWriter.write_source()."""

    @pytest.mark.asyncio
    async def test_it_should_merge_source_by_arxiv_id(self):
        """MERGE source node by arxiv_id."""
        mock_client = _make_mock_client()
        writer = GraphWriter(mock_client)

        source = SourceNode(
            arxiv_id="2301.00001",
            title="A Paper",
            authors=["Author A"],
            date_published="2023-01-01",
        )
        await writer.write_source(source)

        mock_client.execute_write.assert_awaited_once()
        cypher, kwargs = _extract_call(mock_client.execute_write)
        assert "MERGE" in cypher
        assert kwargs["arxiv_id"] == "2301.00001"
        assert kwargs["title"] == "A Paper"


class TestClearMethods:
    """Tests for GraphWriter clear_paper_claims / clear_paper_provenances."""

    @pytest.mark.asyncio
    async def test_it_should_clear_paper_claims(self):
        """It should execute DETACH DELETE for claims of a given paper."""
        client = _make_mock_client()
        writer = GraphWriter(client)
        await writer.clear_paper_claims("my-paper-slug")
        client.execute_write.assert_called_once()
        cypher = client.execute_write.call_args[0][0]
        assert "DETACH DELETE" in cypher
        assert "source_paper_slug" in cypher

    @pytest.mark.asyncio
    async def test_it_should_clear_paper_provenances(self):
        """It should execute DETACH DELETE for provenances of a given paper."""
        client = _make_mock_client()
        writer = GraphWriter(client)
        await writer.clear_paper_provenances("arxiv-123")
        client.execute_write.assert_called_once()
        cypher = client.execute_write.call_args[0][0]
        assert "DETACH DELETE" in cypher
        assert "source_arxiv_id" in cypher


class TestCreateSchemaConstraints:
    """Tests for GraphWriter.create_schema_constraints()."""

    @pytest.mark.asyncio
    async def test_it_should_run_all_constraint_statements(self):
        """create_schema_constraints issues multiple Cypher DDL calls."""
        mock_client = _make_mock_client()
        writer = GraphWriter(mock_client)

        await writer.create_schema_constraints()

        # Should have been called multiple times for constraints/indexes
        assert mock_client.execute_write.await_count >= 4

    @pytest.mark.asyncio
    async def test_it_should_include_concept_uniqueness_constraint(self):
        """At least one constraint ensures Concept slug uniqueness."""
        mock_client = _make_mock_client()
        writer = GraphWriter(mock_client)

        await writer.create_schema_constraints()

        all_cypher = _collect_all_cypher(mock_client.execute_write)
        # Verify there's a uniqueness constraint on Concept.slug
        concept_constraint = [
            c
            for c in all_cypher
            if "Concept" in c and "slug" in c and "UNIQUE" in c.upper()
        ]
        assert len(concept_constraint) >= 1


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _extract_call(mock_method: AsyncMock) -> tuple[str, dict]:
    """Extract the Cypher string and kwargs from the first call to a mock.

    @returns Tuple of (cypher_query, keyword_params)
    """
    args, kwargs = mock_method.call_args
    return args[0], kwargs


def _collect_all_cypher(mock_method: AsyncMock) -> list[str]:
    """Collect all Cypher strings across all calls to a mock.

    @returns List of Cypher query strings
    """
    return [c[0][0] for c in mock_method.call_args_list]
