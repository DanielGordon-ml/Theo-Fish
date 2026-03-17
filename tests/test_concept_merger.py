"""
@file test_concept_merger.py
@description Tests for the concept merger — intra-paper dedup and cross-vault cascade.
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

from graph_builder.extraction.concept_merger import MergedConcept, merge_concepts
from graph_builder.extraction.dedup.dedup_cascade import DedupResult
from graph_builder.extraction.dedup.embedding_client import EmbeddingClient
from graph_builder.models.concept import ConceptNode
from graph_builder.models.provenance import ProvenanceNode


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _make_concept(
    name: str,
    formal_spec: str = "",
    components: list[str] | None = None,
    semantic_type: str = "structure",
) -> ConceptNode:
    """Build a ConceptNode for testing."""
    return ConceptNode(
        name=name,
        semantic_type=semantic_type,
        formal_spec=formal_spec,
        components=components or [],
    )


def _make_graph_reader() -> MagicMock:
    """Build a mock GraphReader that returns an empty vault."""
    reader = MagicMock()
    reader.get_all_concept_slugs = AsyncMock(return_value=[])
    reader.get_existing_concept = AsyncMock(return_value=None)
    reader.vector_similarity_search = AsyncMock(return_value=[])
    return reader


def _make_embedding_client() -> EmbeddingClient:
    """Build a mock EmbeddingClient returning a fixed vector."""
    client = MagicMock(spec=EmbeddingClient)
    client.embed_single = AsyncMock(return_value=[0.1] * 1536)
    return client


def _dedup_new(slug: str) -> DedupResult:
    """Build a DedupResult representing a brand-new concept."""
    return DedupResult(
        slug=slug,
        is_new=True,
        match_method="new",
        match_confidence=0.0,
        existing_slug=None,
    )


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


class TestMergeConceptsDedup:
    """Tests for intra-paper deduplication by concept name/slug."""

    @pytest.mark.asyncio
    async def test_it_should_deduplicate_same_name_across_sections(self):
        """It should produce one entry when the same concept appears in two sections."""
        section_a = [
            _make_concept(
                "Hilbert Space", formal_spec="H is a complete inner-product space"
            )
        ]
        section_b = [_make_concept("Hilbert Space", formal_spec="H")]
        reader = _make_graph_reader()
        embedding_client = _make_embedding_client()

        result = await merge_concepts(
            [section_a, section_b],
            reader,
            embedding_client,
            source_arxiv_id="1234.5678",
        )

        names = [mc.concept.name for mc in result]
        assert names.count("Hilbert Space") == 1

    @pytest.mark.asyncio
    async def test_it_should_keep_richest_formal_spec_when_deduplicating(self):
        """It should retain the longest formal_spec among duplicates."""
        short_spec = "H"
        long_spec = "H is a complete inner-product space over the reals"
        section_a = [_make_concept("Hilbert Space", formal_spec=long_spec)]
        section_b = [_make_concept("Hilbert Space", formal_spec=short_spec)]
        reader = _make_graph_reader()
        embedding_client = _make_embedding_client()

        result = await merge_concepts(
            [section_a, section_b],
            reader,
            embedding_client,
            source_arxiv_id="1234.5678",
        )

        merged = next(mc for mc in result if mc.concept.name == "Hilbert Space")
        assert merged.concept.formal_spec == long_spec

    @pytest.mark.asyncio
    async def test_it_should_merge_components_lists_across_sections(self):
        """It should union components when the same concept appears in multiple sections."""
        section_a = [_make_concept("MDP", components=["states", "actions"])]
        section_b = [_make_concept("MDP", components=["rewards", "transitions"])]
        reader = _make_graph_reader()
        embedding_client = _make_embedding_client()

        result = await merge_concepts(
            [section_a, section_b],
            reader,
            embedding_client,
            source_arxiv_id="1234.5678",
        )

        merged = next(mc for mc in result if mc.concept.name == "MDP")
        assert set(merged.concept.components) == {
            "states",
            "actions",
            "rewards",
            "transitions",
        }


class TestMergeConceptsDedupCascade:
    """Tests for cross-vault dedup cascade integration."""

    @pytest.mark.asyncio
    async def test_it_should_run_dedup_cascade_for_each_unique_concept(self):
        """It should call run_dedup_cascade once per unique concept slug."""
        sections = [
            [_make_concept("Banach Space"), _make_concept("Norm")],
        ]
        reader = _make_graph_reader()
        embedding_client = _make_embedding_client()

        with pytest.MonkeyPatch().context() as mp:
            calls: list[str] = []

            async def _fake_cascade(concept, graph_reader, emb_client, llm_client=None):
                calls.append(concept.slug)
                return _dedup_new(concept.slug)

            mp.setattr(
                "graph_builder.extraction.concept_merger.run_dedup_cascade",
                _fake_cascade,
            )

            result = await merge_concepts(
                sections,
                reader,
                embedding_client,
                source_arxiv_id="1234.5678",
            )

        assert len(calls) == 2
        assert len(result) == 2

    @pytest.mark.asyncio
    async def test_it_should_return_dedup_result_per_merged_concept(self):
        """Each MergedConcept should carry the DedupResult from the cascade."""
        sections = [[_make_concept("Lebesgue Space")]]
        reader = _make_graph_reader()
        embedding_client = _make_embedding_client()

        result = await merge_concepts(
            sections,
            reader,
            embedding_client,
            source_arxiv_id="2345.6789",
        )

        assert len(result) == 1
        assert isinstance(result[0], MergedConcept)
        assert isinstance(result[0].dedup_result, DedupResult)


class TestMergeConceptsProvenance:
    """Tests for provenance metadata attached to merged concepts."""

    @pytest.mark.asyncio
    async def test_it_should_attach_provenance_with_correct_arxiv_id(self):
        """Each MergedConcept should have provenance linked to source_arxiv_id."""
        sections = [[_make_concept("Sobolev Space", formal_spec="W^{k,p}")]]
        reader = _make_graph_reader()
        embedding_client = _make_embedding_client()

        result = await merge_concepts(
            sections,
            reader,
            embedding_client,
            source_arxiv_id="9876.5432",
        )

        prov = result[0].provenance
        assert isinstance(prov, ProvenanceNode)
        assert prov.source_arxiv_id == "9876.5432"

    @pytest.mark.asyncio
    async def test_it_should_set_provenance_concept_slug(self):
        """Provenance concept_slug should match the concept slug."""
        sections = [[_make_concept("Cauchy Sequence")]]
        reader = _make_graph_reader()
        embedding_client = _make_embedding_client()

        result = await merge_concepts(
            sections,
            reader,
            embedding_client,
            source_arxiv_id="1111.2222",
        )

        mc = result[0]
        assert mc.provenance.concept_slug == mc.concept.slug

    @pytest.mark.asyncio
    async def test_it_should_set_provenance_formal_spec_from_concept(self):
        """Provenance formal_spec should carry the concept's formal specification."""
        formal = "A sequence {x_n} where d(x_m, x_n) -> 0"
        sections = [[_make_concept("Cauchy Sequence", formal_spec=formal)]]
        reader = _make_graph_reader()
        embedding_client = _make_embedding_client()

        result = await merge_concepts(
            sections,
            reader,
            embedding_client,
            source_arxiv_id="1111.2222",
        )

        assert result[0].provenance.formal_spec == formal


class TestMergeConceptsEdgeCases:
    """Edge-case tests for merge_concepts."""

    @pytest.mark.asyncio
    async def test_it_should_handle_empty_input(self):
        """It should return an empty list when given no sections."""
        reader = _make_graph_reader()
        embedding_client = _make_embedding_client()

        result = await merge_concepts(
            [],
            reader,
            embedding_client,
            source_arxiv_id="0000.0000",
        )

        assert result == []

    @pytest.mark.asyncio
    async def test_it_should_handle_sections_with_no_concepts(self):
        """It should return an empty list when all sections are empty."""
        reader = _make_graph_reader()
        embedding_client = _make_embedding_client()

        result = await merge_concepts(
            [[], []],
            reader,
            embedding_client,
            source_arxiv_id="0000.0000",
        )

        assert result == []

    @pytest.mark.asyncio
    async def test_it_should_preserve_distinct_concepts_from_multiple_sections(self):
        """It should keep all distinct concepts when no duplicates exist."""
        sections = [
            [_make_concept("Metric Space")],
            [_make_concept("Topological Space")],
            [_make_concept("Normed Space")],
        ]
        reader = _make_graph_reader()
        embedding_client = _make_embedding_client()

        result = await merge_concepts(
            sections,
            reader,
            embedding_client,
            source_arxiv_id="3333.4444",
        )

        assert len(result) == 3
        names = {mc.concept.name for mc in result}
        assert names == {"Metric Space", "Topological Space", "Normed Space"}
