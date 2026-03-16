"""
@file test_frontmatter_builder.py
@description Tests for the frontmatter builder that produces YAML dicts for
Obsidian vault files, covering flat wikilink keys and companion _meta keys.
"""

import pytest

from graph_builder.models.claim import ClaimNode
from graph_builder.models.concept import ConceptNode
from graph_builder.models.edges import (
    ClaimEdge,
    ConceptEdge,
    CouplingEdge,
    SourcedFromEdge,
)
from graph_builder.models.source import SourceNode
from graph_builder.vault.frontmatter_builder import (
    build_claim_frontmatter,
    build_concept_frontmatter,
    build_source_frontmatter,
)

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture()
def brouwer() -> ConceptNode:
    """A concept node representing Brouwer's fixed point theorem."""
    return ConceptNode(
        name="Brouwer Fixed Point Theorem",
        semantic_type="theorem",
        canonical_definition="Every continuous map on a compact convex set has a fixed point.",
        aliases=["Brouwer's theorem"],
    )


@pytest.fixture()
def sperner() -> ConceptNode:
    """A concept node representing Sperner's lemma."""
    return ConceptNode(
        name="Sperner Lemma",
        semantic_type="lemma",
    )


@pytest.fixture()
def simplex() -> ConceptNode:
    """A concept node representing the simplex."""
    return ConceptNode(
        name="Simplex",
        semantic_type="structure",
    )


@pytest.fixture()
def source_node() -> SourceNode:
    """A source node representing a paper."""
    return SourceNode(
        arxiv_id="1904.07272",
        title="Introduction to Topology",
        authors=["Alice Smith", "Bob Jones"],
        date_published="2019-04-15",
    )


@pytest.fixture()
def claim_node() -> ClaimNode:
    """A claim node."""
    return ClaimNode(
        source_paper_slug="intro-topology",
        label="Lemma 2.3",
        claim_type="lemma",
        statement="Every open cover of a compact set has a finite sub-cover.",
    )


# ---------------------------------------------------------------------------
# ConceptNode frontmatter
# ---------------------------------------------------------------------------


class TestBuildConceptFrontmatter:
    """Tests for build_concept_frontmatter()."""

    def test_it_should_include_all_pipeline_owned_fields(self, brouwer):
        """Pipeline-owned fields are present with their model values."""
        fm = build_concept_frontmatter(brouwer, [], [])

        assert fm["slug"] == "brouwer-fixed-point-theorem"
        assert fm["name"] == "Brouwer Fixed Point Theorem"
        assert fm["semantic_type"] == "theorem"
        assert fm["canonical_definition"] == (
            "Every continuous map on a compact convex set has a fixed point."
        )
        assert fm["aliases"] == ["Brouwer's theorem"]
        assert fm["status"] == "canonical"

    def test_it_should_set_human_owned_fields_to_empty_string_on_new_file(
        self, brouwer
    ):
        """Human-owned fields default to empty string so Obsidian shows them."""
        fm = build_concept_frontmatter(brouwer, [], [])

        assert fm["human_notes"] == ""

    def test_it_should_produce_empty_edge_lists_when_no_edges(self, brouwer):
        """With no edges, all wikilink and _meta lists are empty."""
        fm = build_concept_frontmatter(brouwer, [], [])

        assert fm["generalizes"] == []
        assert fm["generalizes_meta"] == []
        assert fm["has_component"] == []
        assert fm["has_component_meta"] == []
        assert fm["sourced_from"] == []
        assert fm["sourced_from_meta"] == []

    def test_it_should_generate_flat_wikilink_keys_for_concept_edges(
        self, brouwer, sperner
    ):
        """Each edge type key holds a list of wikilinks to target concepts."""
        edge = ConceptEdge(
            source_slug=brouwer.slug,
            target_slug=sperner.slug,
            edge_type="generalizes",
            attributes={"condition": "triangulation"},
        )
        fm = build_concept_frontmatter(brouwer, [edge], [])

        assert "[[concepts/sperner-lemma]]" in fm["generalizes"]

    def test_it_should_generate_companion_meta_keys_with_attributes(
        self, brouwer, sperner
    ):
        """The _meta companion key contains the edge attributes dict."""
        edge = ConceptEdge(
            source_slug=brouwer.slug,
            target_slug=sperner.slug,
            edge_type="generalizes",
            attributes={"condition": "triangulation", "direction": "forward"},
        )
        fm = build_concept_frontmatter(brouwer, [edge], [])

        meta_list = fm["generalizes_meta"]
        assert len(meta_list) == 1
        assert meta_list[0]["target"] == "[[concepts/sperner-lemma]]"
        assert meta_list[0]["condition"] == "triangulation"
        assert meta_list[0]["direction"] == "forward"

    def test_it_should_group_edges_by_type(
        self, brouwer, sperner, simplex
    ):
        """Multiple edges of different types appear in separate lists."""
        generalizes_edge = ConceptEdge(
            source_slug=brouwer.slug,
            target_slug=sperner.slug,
            edge_type="generalizes",
        )
        component_edge = ConceptEdge(
            source_slug=brouwer.slug,
            target_slug=simplex.slug,
            edge_type="has_component",
        )
        fm = build_concept_frontmatter(
            brouwer, [generalizes_edge, component_edge], []
        )

        assert "[[concepts/sperner-lemma]]" in fm["generalizes"]
        assert "[[concepts/simplex]]" in fm["has_component"]
        assert "[[concepts/simplex]]" not in fm["generalizes"]

    def test_it_should_generate_sourced_from_wikilinks_for_concepts(
        self, brouwer, source_node
    ):
        """sourced_from holds wikilinks pointing to the sources/ folder."""
        edge = SourcedFromEdge(
            node_slug=brouwer.slug,
            source_arxiv_id=source_node.arxiv_id,
            confidence=0.9,
        )
        titles = {source_node.arxiv_id: source_node.title}
        fm = build_concept_frontmatter(brouwer, [], [edge], source_titles=titles)

        assert "[[sources/1904.07272|Introduction to Topology]]" in fm["sourced_from"]

    def test_it_should_include_sourced_from_meta_with_attributes(
        self, brouwer, source_node
    ):
        """sourced_from_meta includes section, page, and confidence."""
        edge = SourcedFromEdge(
            node_slug=brouwer.slug,
            source_arxiv_id=source_node.arxiv_id,
            section="Section 3",
            page="42",
            confidence=0.9,
        )
        titles = {source_node.arxiv_id: source_node.title}
        fm = build_concept_frontmatter(brouwer, [], [edge], source_titles=titles)

        meta = fm["sourced_from_meta"]
        assert len(meta) == 1
        assert meta[0]["target"] == "[[sources/1904.07272|Introduction to Topology]]"
        assert meta[0]["section"] == "Section 3"
        assert meta[0]["confidence"] == 0.9


# ---------------------------------------------------------------------------
# ClaimNode frontmatter
# ---------------------------------------------------------------------------


class TestBuildClaimFrontmatter:
    """Tests for build_claim_frontmatter()."""

    def test_it_should_include_all_pipeline_owned_fields(self, claim_node):
        """Pipeline-owned claim fields appear in frontmatter."""
        fm = build_claim_frontmatter(claim_node, [], [], [])

        assert fm["slug"] == claim_node.slug
        assert fm["claim_type"] == "lemma"
        assert fm["label"] == "Lemma 2.3"
        assert fm["statement"] == "Every open cover of a compact set has a finite sub-cover."
        assert fm["status"] == "unverified"

    def test_it_should_set_human_owned_fields_to_empty_string_on_new_file(
        self, claim_node
    ):
        """Human-owned fields default to empty string."""
        fm = build_claim_frontmatter(claim_node, [], [], [])

        assert fm["human_notes"] == ""

    def test_it_should_build_about_wikilinks_from_coupling_edges(
        self, claim_node, brouwer
    ):
        """ABOUT edges produce wikilinks in the about key."""
        coupling = CouplingEdge(
            claim_slug=claim_node.slug,
            concept_slug=brouwer.slug,
            role="primary",
        )
        fm = build_claim_frontmatter(claim_node, [], [coupling], [])

        assert "[[concepts/brouwer-fixed-point-theorem]]" in fm["about"]

    def test_it_should_include_about_meta_with_role_and_aspect(
        self, claim_node, brouwer
    ):
        """about_meta includes role and aspect from CouplingEdge."""
        coupling = CouplingEdge(
            claim_slug=claim_node.slug,
            concept_slug=brouwer.slug,
            role="primary",
            aspect="existence",
        )
        fm = build_claim_frontmatter(claim_node, [], [coupling], [])

        meta = fm["about_meta"]
        assert len(meta) == 1
        assert meta[0]["target"] == "[[concepts/brouwer-fixed-point-theorem]]"
        assert meta[0]["role"] == "primary"
        assert meta[0]["aspect"] == "existence"

    def test_it_should_build_depends_on_wikilinks_from_claim_edges(
        self, claim_node
    ):
        """depends_on edges produce wikilinks pointing to claims/ folder."""
        edge = ClaimEdge(
            source_slug=claim_node.slug,
            target_slug="other-paper--lemma-1-1",
            edge_type="depends_on",
            attributes={"role": "key step"},
        )
        fm = build_claim_frontmatter(claim_node, [edge], [], [])

        assert "[[claims/other-paper--lemma-1-1]]" in fm["depends_on"]

    def test_it_should_include_depends_on_meta_with_attributes(
        self, claim_node
    ):
        """depends_on_meta includes the edge attributes and target wikilink."""
        edge = ClaimEdge(
            source_slug=claim_node.slug,
            target_slug="other-paper--lemma-1-1",
            edge_type="depends_on",
            attributes={"role": "key step"},
        )
        fm = build_claim_frontmatter(claim_node, [edge], [], [])

        meta = fm["depends_on_meta"]
        assert len(meta) == 1
        assert meta[0]["target"] == "[[claims/other-paper--lemma-1-1]]"
        assert meta[0]["role"] == "key step"

    def test_it_should_generate_sourced_from_wikilinks_for_claims(
        self, claim_node, source_node
    ):
        """sourced_from wikilinks point to the sources/ folder."""
        edge = SourcedFromEdge(
            node_slug=claim_node.slug,
            source_arxiv_id=source_node.arxiv_id,
            confidence=0.85,
        )
        titles = {source_node.arxiv_id: source_node.title}
        fm = build_claim_frontmatter(claim_node, [], [], [edge], source_titles=titles)

        assert "[[sources/1904.07272|Introduction to Topology]]" in fm["sourced_from"]

    def test_it_should_produce_empty_lists_when_no_edges(self, claim_node):
        """With no edges, all list fields are empty."""
        fm = build_claim_frontmatter(claim_node, [], [], [])

        assert fm["about"] == []
        assert fm["about_meta"] == []
        assert fm["depends_on"] == []
        assert fm["depends_on_meta"] == []
        assert fm["sourced_from"] == []
        assert fm["sourced_from_meta"] == []


# ---------------------------------------------------------------------------
# SourceNode frontmatter
# ---------------------------------------------------------------------------


class TestBuildSourceFrontmatter:
    """Tests for build_source_frontmatter()."""

    def test_it_should_include_all_pipeline_owned_fields(self, source_node):
        """All SourceNode fields appear in frontmatter."""
        fm = build_source_frontmatter(source_node)

        assert fm["arxiv_id"] == "1904.07272"
        assert fm["title"] == "Introduction to Topology"
        assert fm["authors"] == ["Alice Smith", "Bob Jones"]
        assert fm["date_published"] == "2019-04-15"

    def test_it_should_set_human_owned_fields_to_empty_string(
        self, source_node
    ):
        """human_notes defaults to empty string."""
        fm = build_source_frontmatter(source_node)

        assert fm["human_notes"] == ""

    def test_it_should_handle_minimal_source_with_only_arxiv_id(self):
        """SourceNode with only arxiv_id produces valid frontmatter."""
        source = SourceNode(arxiv_id="2301.99999")
        fm = build_source_frontmatter(source)

        assert fm["arxiv_id"] == "2301.99999"
        assert fm["title"] == ""
        assert fm["authors"] == []
