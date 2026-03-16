"""
@file test_body_renderer.py
@description Tests for body_renderer: markdown body generation for concept,
claim, and source vault files.
"""

import pytest

from graph_builder.models.concept import ConceptNode
from graph_builder.models.claim import ClaimNode
from graph_builder.models.source import SourceNode
from graph_builder.models.provenance import ProvenanceNode
from graph_builder.vault.body_renderer import (
    render_concept_body,
    render_claim_body,
    render_source_body,
)

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture()
def concept() -> ConceptNode:
    """A minimal ConceptNode for testing."""
    return ConceptNode(
        name="Markov Decision Process",
        semantic_type="mathematical_object",
        canonical_definition=(
            "A Markov Decision Process is a tuple $(S, A, P, R, \\gamma)$ where..."
        ),
    )


@pytest.fixture()
def provenance(concept: ConceptNode) -> ProvenanceNode:
    """A ProvenanceNode linked to the concept fixture."""
    return ProvenanceNode(
        concept_slug=concept.slug,
        source_arxiv_id="1904-07272",
        formulation="(S, A, P, R, γ)",
        section="Ch. 1",
        extraction_confidence=0.95,
    )


@pytest.fixture()
def claim() -> ClaimNode:
    """A ClaimNode with statement and proof."""
    return ClaimNode(
        source_paper_slug="1904-07272",
        label="Theorem 1.1",
        claim_type="theorem",
        statement="Let $K = |A|$ be the number of actions...",
        proof="By applying Lemma 1.3 to the UCB index...",
    )


@pytest.fixture()
def source() -> SourceNode:
    """A SourceNode representing a paper."""
    return SourceNode(
        arxiv_id="1904.07272",
        title="Intro MAB",
        authors=["Slivkins, A."],
        date_published="2019-04-15",
    )


# ---------------------------------------------------------------------------
# render_concept_body
# ---------------------------------------------------------------------------

class TestRenderConceptBody:
    """Tests for render_concept_body()."""

    def test_it_should_render_concept_body_with_canonical_definition(
        self, concept: ConceptNode,
    ):
        """Body opens with a heading and the canonical definition."""
        body = render_concept_body(concept, [])
        assert "# Markov Decision Process" in body
        assert concept.canonical_definition in body

    def test_it_should_preserve_latex_in_body_text(self, concept: ConceptNode):
        """LaTeX expressions survive verbatim in the rendered body."""
        body = render_concept_body(concept, [])
        assert "$(S, A, P, R, \\gamma)$" in body

    def test_it_should_render_provenance_table_for_concepts(
        self,
        concept: ConceptNode,
        provenance: ProvenanceNode,
    ):
        """A provenance table with four columns is present when data exists."""
        body = render_concept_body(concept, [provenance])
        assert "## Provenance" in body
        assert "| Source | Section | Formulation | Confidence |" in body
        assert "| [[sources/1904-07272" in body
        assert "Ch. 1" in body
        assert "(S, A, P, R, γ)" in body
        assert "0.95" in body

    def test_it_should_handle_concept_with_no_provenance(
        self, concept: ConceptNode,
    ):
        """When provenance list is empty, no provenance table is rendered."""
        body = render_concept_body(concept, [])
        assert "## Provenance" not in body


# ---------------------------------------------------------------------------
# render_claim_body
# ---------------------------------------------------------------------------

class TestRenderClaimBody:
    """Tests for render_claim_body()."""

    def test_it_should_render_claim_body_with_statement_and_proof_sections(
        self, claim: ClaimNode,
    ):
        """Body contains heading, statement text, and proof section."""
        body = render_claim_body(claim)
        assert "# Theorem 1.1" in body
        assert claim.statement in body
        assert "## Proof" in body
        assert claim.proof in body

    def test_it_should_handle_missing_proof_no_proof_section(self):
        """When proof is empty, the ## Proof section is omitted."""
        claim_no_proof = ClaimNode(
            source_paper_slug="1904-07272",
            label="Lemma 2.3",
            claim_type="lemma",
            statement="All rewards are bounded in $[0, 1]$.",
            proof="",
        )
        body = render_claim_body(claim_no_proof)
        assert "# Lemma 2.3" in body
        assert claim_no_proof.statement in body
        assert "## Proof" not in body


# ---------------------------------------------------------------------------
# render_source_body
# ---------------------------------------------------------------------------

class TestRenderSourceBody:
    """Tests for render_source_body()."""

    def test_it_should_render_source_body_with_paper_metadata_and_entity_lists(
        self, source: SourceNode,
    ):
        """Body contains heading, arxiv_id, authors, and entity wikilinks."""
        concept_slugs = ["markov-decision-process", "ucb-index"]
        claim_slugs = ["1904-07272--theorem-1-1"]

        body = render_source_body(source, concept_slugs, claim_slugs)

        assert "# Intro MAB" in body
        assert source.arxiv_id in body
        assert "Slivkins, A." in body
        assert "[[concepts/markov-decision-process" in body
        assert "[[concepts/ucb-index" in body
        assert "[[claims/1904-07272--theorem-1-1" in body
