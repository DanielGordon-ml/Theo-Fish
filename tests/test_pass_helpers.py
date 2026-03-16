"""
@file test_pass_helpers.py
@description Tests for orchestrator pass helper functions: flatten utilities,
concept list building, claims-by-section grouping, and fallback merge.
"""

import pytest

from graph_builder.extraction.concept_merger import MergedConcept
from graph_builder.extraction.dedup.dedup_cascade import DedupResult
from graph_builder.models.claim import ClaimNode
from graph_builder.models.concept import ConceptNode
from graph_builder.models.edges import ClaimEdge, CouplingEdge
from graph_builder.models.provenance import ProvenanceNode
from graph_builder.models.section import Section
from graph_builder.orchestrator.pass_helpers import (
    build_concept_list,
    fallback_merge,
    flatten_claim_results,
    flatten_edge_results,
    group_claims_by_section,
)


def _make_concept(name: str) -> ConceptNode:
    """Build a ConceptNode with the given name."""
    return ConceptNode(name=name, semantic_type="structure")


def _make_claim(label: str, section: str) -> ClaimNode:
    """Build a ClaimNode with the given label and section."""
    return ClaimNode(
        label=label, source_paper_slug="test-paper",
        claim_type="theorem", section=section,
    )


def _make_section(heading: str, index: int) -> Section:
    """Build a Section with the given heading."""
    return Section(
        heading=heading, level=2, content="content",
        char_count=7, index=index,
    )


def _make_merged(name: str, arxiv_id: str) -> MergedConcept:
    """Build a MergedConcept with a new-concept DedupResult."""
    concept = _make_concept(name)
    return MergedConcept(
        concept=concept,
        dedup_result=DedupResult(
            slug=concept.slug, is_new=True,
            match_method="new", match_confidence=0.0,
        ),
        provenance=ProvenanceNode(
            concept_slug=concept.slug, source_arxiv_id=arxiv_id,
            formulation="def", formal_spec="spec",
        ),
    )


class TestFlattenClaimResults:
    """Tests for flattening per-section claim results."""

    def test_it_should_merge_claims_and_couplings(self):
        """It should concatenate all claims and coupling edges."""
        c1 = _make_claim("T1", "s1")
        c2 = _make_claim("T2", "s2")
        e1 = CouplingEdge(claim_slug="c1", concept_slug="x")
        results = [([c1], [e1]), ([c2], [])]
        claims, couplings = flatten_claim_results(results)
        assert len(claims) == 2
        assert len(couplings) == 1


class TestFlattenEdgeResults:
    """Tests for flattening per-section edge results."""

    def test_it_should_merge_claim_edges_and_couplings(self):
        """It should concatenate claim edges and coupling edges."""
        ce = ClaimEdge(source_slug="a", target_slug="b", edge_type="depends_on")
        co = CouplingEdge(claim_slug="c1", concept_slug="x")
        results = [([ce], [co]), ([], [])]
        claim_edges, couplings = flatten_edge_results(results)
        assert len(claim_edges) == 1
        assert len(couplings) == 1


class TestBuildConceptList:
    """Tests for building concept grounding list from merged concepts."""

    def test_it_should_extract_name_slug_type(self):
        """It should return dicts with name, slug, type keys."""
        merged = [_make_merged("Hilbert Space", "2401.00001")]
        result = build_concept_list(merged)
        assert len(result) == 1
        assert result[0]["name"] == "Hilbert Space"
        assert "slug" in result[0]
        assert result[0]["type"] == "structure"


class TestGroupClaimsBySection:
    """Tests for grouping claims by their section heading."""

    def test_it_should_group_by_section_field(self):
        """It should create a dict mapping heading to claims."""
        sections = [_make_section("Intro", 0), _make_section("Main", 1)]
        claims = [_make_claim("T1", "Intro"), _make_claim("T2", "Main")]
        groups = group_claims_by_section(claims, sections)
        assert len(groups["Intro"]) == 1
        assert len(groups["Main"]) == 1


class TestFallbackMerge:
    """Tests for slug-based fallback merge."""

    def test_it_should_dedup_by_slug(self):
        """It should keep only one concept per unique slug."""
        c1 = _make_concept("Space")
        c2 = _make_concept("Space")
        result = fallback_merge([[c1], [c2]], "2401.00001")
        assert len(result) == 1
        assert result[0].concept.slug == c1.slug
