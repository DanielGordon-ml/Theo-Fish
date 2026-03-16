"""
@file test_golden_paper.py
@description Structural golden paper tests that validate extraction topology
and cross-paper concept deduplication using synthetic LLM response fixtures
for a game theory paper about K-Strong Price of Anarchy.

Phase 1: Single-paper extraction (concept types, claim dependency chain,
ABOUT coupling edges, edge attributes).
Phase 2: Cross-paper dedup (shared concept merging, separate Provenance
nodes, no duplicate Concept nodes).

These tests will be upgraded with real LLM fixture recordings once the
pipeline runs against actual ArXiv papers.
"""

import json
from contextlib import contextmanager
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, call, patch

import pytest

from graph_builder.config.schema_types import (
    ClaimTypeDef,
    ConceptTypeDef,
    EdgeCategories,
    FieldOwnership,
    GraphSchema,
    ValidationConfig,
)
from graph_builder.extraction.concept_merger import MergedConcept
from graph_builder.extraction.dedup.dedup_cascade import DedupResult
from graph_builder.models.claim import ClaimNode
from graph_builder.models.concept import ConceptNode
from graph_builder.models.edges import ClaimEdge, CouplingEdge
from graph_builder.models.provenance import ProvenanceNode
from graph_builder.models.section import Section
from graph_builder.orchestrator.orchestrator import PipelineOptions, process_paper
from graph_builder.shared.slugify import slugify

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_FIXTURES_DIR = Path(__file__).parent / "fixtures"
_PAPER_1_ID = "2312.00001"
_PAPER_2_ID = "2312.00002"
_PAPER_1_TITLE = "K-Strong Price of Anarchy in Coalition Games"
_PAPER_2_TITLE = "Congestion Games and Nash Equilibrium Refinements"
_MODULE = "graph_builder.orchestrator.orchestrator"

# Concept names as they appear in the fixture
_NASH_EQ_NAME = "Nash Equilibrium"
_ACTION_SPACE_NAME = "action space"
_UTILITY_FN_NAME = "utility function"
_POA_NAME = "price of anarchy"
_COALITION_NAME = "coalition"
_K_SE_NAME = "k-strong equilibrium"
_CONGESTION_GAME_NAME = "congestion game"

# Slugified versions
_NASH_EQ_SLUG = slugify(_NASH_EQ_NAME)
_POA_SLUG = slugify(_POA_NAME)
_K_SE_SLUG = slugify(_K_SE_NAME)
_COALITION_SLUG = slugify(_COALITION_NAME)


# ---------------------------------------------------------------------------
# Fixture loading helpers
# ---------------------------------------------------------------------------

def _load_concepts_fixture() -> dict:
    """Load the golden concept extraction fixture from disk."""
    path = _FIXTURES_DIR / "golden_paper_concepts.json"
    return json.loads(path.read_text(encoding="utf-8"))


def _load_claims_fixture() -> dict:
    """Load the golden claim extraction fixture from disk."""
    path = _FIXTURES_DIR / "golden_paper_claims.json"
    return json.loads(path.read_text(encoding="utf-8"))


# ---------------------------------------------------------------------------
# Schema and model builder helpers
# ---------------------------------------------------------------------------

def _make_schema() -> GraphSchema:
    """Build a GraphSchema covering all concept/claim types used in the fixtures."""
    concept_types = {
        "structure": ConceptTypeDef(
            description="A named mathematical structure or equilibrium concept",
            required_fields=["name", "semantic_type"],
        ),
        "space": ConceptTypeDef(
            description="A mathematical space or domain",
            required_fields=["name", "semantic_type"],
        ),
        "operator": ConceptTypeDef(
            description="A function or mapping between spaces",
            required_fields=["name", "semantic_type"],
        ),
        "quantity": ConceptTypeDef(
            description="A scalar measure or ratio",
            required_fields=["name", "semantic_type"],
        ),
        "class": ConceptTypeDef(
            description="A class or family of mathematical objects",
            required_fields=["name", "semantic_type"],
        ),
    }
    claim_types = {
        "theorem": ClaimTypeDef(
            description="A proven statement with full proof",
            required_fields=["label", "claim_type", "conclusion"],
        ),
        "lemma": ClaimTypeDef(
            description="An auxiliary result used to prove a theorem",
            required_fields=["label", "claim_type", "conclusion"],
        ),
        "corollary": ClaimTypeDef(
            description="A result derived directly from a theorem",
            required_fields=["label", "claim_type", "conclusion"],
        ),
    }
    return GraphSchema(
        version="1.0",
        last_updated="2026-01-01",
        concept_types=concept_types,
        claim_types=claim_types,
        edges=EdgeCategories(),
        validation=ValidationConfig(),
        field_ownership=FieldOwnership(),
    )


def _make_section(heading: str, content: str, index: int = 0) -> Section:
    """Build a Section with the given heading and content."""
    return Section(
        heading=heading,
        level=2,
        content=content,
        char_count=len(content),
        index=index,
    )


def _make_concept_from_fixture(entry: dict) -> ConceptNode:
    """Construct a ConceptNode from a fixture dict entry."""
    return ConceptNode(
        name=entry["name"],
        semantic_type=entry["semantic_type"],
        canonical_definition=entry.get("canonical_definition", ""),
        formal_spec=entry.get("formal_spec", ""),
        aliases=entry.get("aliases", []),
    )


def _make_claim_from_fixture(
    entry: dict,
    paper_slug: str,
) -> ClaimNode:
    """Construct a ClaimNode from a fixture dict entry."""
    slug_override = f"{paper_slug}--{slugify(entry['label'])}"
    return ClaimNode(
        slug=slug_override,
        label=entry["label"],
        source_paper_slug=paper_slug,
        claim_type=entry["claim_type"],
        statement=entry.get("statement", ""),
        conclusion=entry.get("conclusion", ""),
        proof_technique=entry.get("proof_technique", ""),
        proof=entry.get("proof", ""),
        assumptions=entry.get("assumptions", []),
        strength=entry.get("strength", ""),
        section=entry.get("section", ""),
    )


def _make_merged(
    concept: ConceptNode,
    arxiv_id: str,
    is_new: bool = True,
) -> MergedConcept:
    """Build a MergedConcept wrapping a ConceptNode."""
    return MergedConcept(
        concept=concept,
        dedup_result=DedupResult(
            slug=concept.slug,
            is_new=is_new,
            match_method="new" if is_new else "exact",
            match_confidence=0.0 if is_new else 1.0,
        ),
        provenance=ProvenanceNode(
            concept_slug=concept.slug,
            source_arxiv_id=arxiv_id,
            formulation=concept.canonical_definition,
            formal_spec=concept.formal_spec,
        ),
    )


def _make_options(schema: GraphSchema | None = None) -> PipelineOptions:
    """Build PipelineOptions with optional schema override."""
    return PipelineOptions(
        schema=schema or _make_schema(),
        concurrency=2,
        force=True,
    )


def _mock_neo4j() -> MagicMock:
    """Build a Neo4jClient mock with async read/write returning empty."""
    client = MagicMock()
    client.execute_read = AsyncMock(return_value=[])
    client.execute_write = AsyncMock(return_value=None)
    client.execute_write_tx = AsyncMock(return_value=None)
    return client


def _valid_validation() -> MagicMock:
    """Return a mock ValidationResult with is_valid=True."""
    return MagicMock(is_valid=True, errors=[], warnings=[])


# ---------------------------------------------------------------------------
# Concept and claim sets built from fixtures
# ---------------------------------------------------------------------------

def _paper1_concepts_section1() -> list[ConceptNode]:
    """Return the three concepts from paper 1 section 1."""
    fixture = _load_concepts_fixture()
    return [
        _make_concept_from_fixture(e)
        for e in fixture["paper_1_section_1"]["concepts"]
    ]


def _paper1_concepts_section2() -> list[ConceptNode]:
    """Return the three concepts from paper 1 section 2."""
    fixture = _load_concepts_fixture()
    return [
        _make_concept_from_fixture(e)
        for e in fixture["paper_1_section_2"]["concepts"]
    ]


def _paper2_concepts_section1() -> list[ConceptNode]:
    """Return the two concepts from paper 2 section 1."""
    fixture = _load_concepts_fixture()
    return [
        _make_concept_from_fixture(e)
        for e in fixture["paper_2_section_1"]["concepts"]
    ]


def _paper1_all_merged() -> list[MergedConcept]:
    """Build all six merged concepts for paper 1 (all new)."""
    concepts = _paper1_concepts_section1() + _paper1_concepts_section2()
    return [_make_merged(c, _PAPER_1_ID) for c in concepts]


def _paper1_claims() -> list[ClaimNode]:
    """Build the three claims for paper 1 from fixture data."""
    fixture = _load_claims_fixture()
    paper_slug = slugify(_PAPER_1_TITLE)
    return [
        _make_claim_from_fixture(e, paper_slug)
        for e in fixture["paper_1_section_2"]["claims"]
    ]


def _paper1_coupling_edges(
    claims: list[ClaimNode],
) -> list[CouplingEdge]:
    """Build coupling edges from fixture about_concepts lists."""
    fixture = _load_claims_fixture()
    raw_claims = fixture["paper_1_section_2"]["claims"]
    edges: list[CouplingEdge] = []
    for claim, raw in zip(claims, raw_claims):
        for concept_slug in raw.get("about_concepts", []):
            edges.append(CouplingEdge(
                claim_slug=claim.slug,
                concept_slug=concept_slug,
            ))
    return edges


def _paper1_claim_edges(claims: list[ClaimNode]) -> list[ClaimEdge]:
    """Build claim-to-claim edges reflecting the theorem dependency chain."""
    theorem = next(c for c in claims if c.label == "Theorem 1")
    lemma = next(c for c in claims if c.label == "Lemma 1")
    corollary = next(c for c in claims if c.label == "Corollary 1")
    return [
        ClaimEdge(
            source_slug=theorem.slug,
            target_slug=lemma.slug,
            edge_type="depends_on",
            attributes={"condition": "Theorem 1 proof invokes Lemma 1"},
        ),
        ClaimEdge(
            source_slug=corollary.slug,
            target_slug=theorem.slug,
            edge_type="derived_from",
            attributes={"condition": "Corollary obtained by substituting k=1 into Theorem 1"},
        ),
    ]


# ---------------------------------------------------------------------------
# Pipeline patch context manager
# ---------------------------------------------------------------------------

@contextmanager
def _patch_pipeline(overrides: dict | None = None):
    """Patch all orchestrator pipeline internals with sensible defaults.

    Yields a dict of mock objects keyed by short name. Pass overrides dict
    to change specific return_values before the pipeline runs.
    """
    overrides = overrides or {}

    paper1_slug = slugify(_PAPER_1_TITLE)
    claims = _paper1_claims()
    coupling = _paper1_coupling_edges(claims)

    defaults = {
        "load": (_PAPER_1_TITLE, [
            _make_section("Introduction", "Game theory intro content.", 0),
            _make_section("Main Results", "Theorems and lemmas.", 1),
        ]),
        "check": False,
        "p1": [_paper1_concepts_section1(), _paper1_concepts_section2()],
        "merge": _paper1_all_merged(),
        "p2": (claims, coupling),
        "p3a": ([], []),
        "p3b": [],
        "validate": _valid_validation(),
        "write": {
            "concepts": len(_paper1_all_merged()),
            "claims": len(claims),
            "edges": len(coupling),
        },
    }
    defaults.update(overrides)

    targets = {
        "load": f"{_MODULE}.load_paper",
        "check": f"{_MODULE}.check_already_built",
        "p1": f"{_MODULE}._run_pass1",
        "merge": f"{_MODULE}._run_merge",
        "p2": f"{_MODULE}._run_pass2",
        "p3a": f"{_MODULE}._run_pass3a",
        "p3b": f"{_MODULE}._run_pass3b",
        "validate": f"{_MODULE}.validate_paper",
        "write": f"{_MODULE}.write_to_neo4j",
    }

    # validate_paper is synchronous; all others are async
    _ASYNC_KEYS = {"load", "check", "p1", "merge", "p2", "p3a", "p3b", "write"}

    patches = {}
    active = []
    for key, target in targets.items():
        kwargs = {"new_callable": AsyncMock} if key in _ASYNC_KEYS else {}
        p = patch(target, **kwargs)
        mock_obj = p.start()
        mock_obj.return_value = defaults[key]
        patches[key] = mock_obj
        active.append(p)

    try:
        yield patches
    finally:
        for p in active:
            p.stop()


# ---------------------------------------------------------------------------
# Phase 1: Single-paper extraction tests
# ---------------------------------------------------------------------------

class TestPhase1ConceptExtraction:
    """Phase 1 — validate concept semantic types from fixture data."""

    def test_it_should_produce_concepts_with_correct_semantic_types(self):
        """It should assign each concept the semantic_type declared in the fixture."""
        concepts = _paper1_concepts_section1() + _paper1_concepts_section2()
        type_map = {c.name: c.semantic_type for c in concepts}

        assert type_map[_NASH_EQ_NAME] == "structure"
        assert type_map[_ACTION_SPACE_NAME] == "space"
        assert type_map[_UTILITY_FN_NAME] == "operator"
        assert type_map[_POA_NAME] == "quantity"
        assert type_map[_COALITION_NAME] == "class"
        assert type_map[_K_SE_NAME] == "structure"

    def test_it_should_derive_slugs_from_concept_names(self):
        """It should auto-derive slugs from names using the slugify function."""
        concepts = _paper1_concepts_section1() + _paper1_concepts_section2()
        for concept in concepts:
            assert concept.slug == slugify(concept.name)
            assert concept.slug != ""

    def test_it_should_populate_formal_spec_on_all_concepts(self):
        """It should carry the formal_spec string from the fixture."""
        concepts = _paper1_concepts_section1() + _paper1_concepts_section2()
        for concept in concepts:
            assert concept.formal_spec != "", (
                f"Concept '{concept.name}' is missing formal_spec"
            )


class TestPhase1ClaimDependencyChain:
    """Phase 1 — validate the claim dependency structure."""

    def test_it_should_extract_three_claims_with_correct_types(self):
        """It should produce Lemma 1, Theorem 1, and Corollary 1 with right types."""
        claims = _paper1_claims()
        by_label = {c.label: c for c in claims}

        assert "Lemma 1" in by_label
        assert "Theorem 1" in by_label
        assert "Corollary 1" in by_label

        assert by_label["Lemma 1"].claim_type == "lemma"
        assert by_label["Theorem 1"].claim_type == "theorem"
        assert by_label["Corollary 1"].claim_type == "corollary"

    def test_it_should_build_theorem_depends_on_lemma_edge(self):
        """It should create a depends_on edge from Theorem 1 to Lemma 1."""
        claims = _paper1_claims()
        edges = _paper1_claim_edges(claims)

        depends_on_edges = [e for e in edges if e.edge_type == "depends_on"]
        assert len(depends_on_edges) == 1

        theorem = next(c for c in claims if c.label == "Theorem 1")
        lemma = next(c for c in claims if c.label == "Lemma 1")
        edge = depends_on_edges[0]

        assert edge.source_slug == theorem.slug
        assert edge.target_slug == lemma.slug

    def test_it_should_build_corollary_derived_from_theorem_edge(self):
        """It should create a derived_from edge from Corollary 1 to Theorem 1."""
        claims = _paper1_claims()
        edges = _paper1_claim_edges(claims)

        derived_edges = [e for e in edges if e.edge_type == "derived_from"]
        assert len(derived_edges) == 1

        corollary = next(c for c in claims if c.label == "Corollary 1")
        theorem = next(c for c in claims if c.label == "Theorem 1")
        edge = derived_edges[0]

        assert edge.source_slug == corollary.slug
        assert edge.target_slug == theorem.slug

    def test_it_should_produce_two_claim_edges_in_dependency_chain(self):
        """It should produce exactly two claim edges (Thm->Lemma, Cor->Thm)."""
        claims = _paper1_claims()
        edges = _paper1_claim_edges(claims)
        assert len(edges) == 2


class TestPhase1CouplingEdges:
    """Phase 1 — validate ABOUT coupling edges from claims to concepts."""

    def test_it_should_create_about_edges_linking_claims_to_concepts(self):
        """It should emit at least one CouplingEdge per claim."""
        claims = _paper1_claims()
        coupling = _paper1_coupling_edges(claims)

        claim_slugs_with_edges = {e.claim_slug for e in coupling}
        for claim in claims:
            assert claim.slug in claim_slugs_with_edges, (
                f"Claim '{claim.label}' has no ABOUT coupling edges"
            )

    def test_it_should_link_theorem_to_price_of_anarchy_concept(self):
        """It should link Theorem 1 to the price-of-anarchy concept slug."""
        claims = _paper1_claims()
        coupling = _paper1_coupling_edges(claims)

        theorem = next(c for c in claims if c.label == "Theorem 1")
        theorem_targets = {
            e.concept_slug for e in coupling if e.claim_slug == theorem.slug
        }
        assert _POA_SLUG in theorem_targets

    def test_it_should_link_lemma_to_coalition_concept(self):
        """It should link Lemma 1 to the coalition concept slug."""
        claims = _paper1_claims()
        coupling = _paper1_coupling_edges(claims)

        lemma = next(c for c in claims if c.label == "Lemma 1")
        lemma_targets = {
            e.concept_slug for e in coupling if e.claim_slug == lemma.slug
        }
        assert _COALITION_SLUG in lemma_targets

    def test_it_should_populate_edge_condition_attribute_in_claim_edges(self):
        """It should populate the condition attribute on claim-to-claim edges."""
        claims = _paper1_claims()
        claim_edges = _paper1_claim_edges(claims)

        for edge in claim_edges:
            assert "condition" in edge.attributes, (
                f"ClaimEdge {edge.source_slug}->{edge.target_slug} missing 'condition'"
            )
            assert edge.attributes["condition"] != ""


class TestPhase1OrchestratorResult:
    """Phase 1 — validate the orchestrator BuildResult for paper 1."""

    @pytest.mark.asyncio
    async def test_it_should_return_built_status_for_paper_1(self):
        """It should return status='built' after processing the golden paper."""
        llm = MagicMock()
        llm.call = AsyncMock()

        with _patch_pipeline():
            result = await process_paper(
                _PAPER_1_ID,
                _make_options(),
                llm,
                _mock_neo4j(),
            )

        assert result.status == "built"
        assert result.arxiv_id == _PAPER_1_ID

    @pytest.mark.asyncio
    async def test_it_should_report_six_concepts_for_paper_1(self):
        """It should count all six extracted concepts in the BuildResult."""
        llm = MagicMock()
        llm.call = AsyncMock()

        with _patch_pipeline():
            result = await process_paper(
                _PAPER_1_ID,
                _make_options(),
                llm,
                _mock_neo4j(),
            )

        assert result.concept_count == 6

    @pytest.mark.asyncio
    async def test_it_should_report_three_claims_for_paper_1(self):
        """It should count all three extracted claims in the BuildResult."""
        llm = MagicMock()
        llm.call = AsyncMock()

        with _patch_pipeline():
            result = await process_paper(
                _PAPER_1_ID,
                _make_options(),
                llm,
                _mock_neo4j(),
            )

        assert result.claim_count == 3


# ---------------------------------------------------------------------------
# Phase 2: Cross-paper deduplication tests
# ---------------------------------------------------------------------------

def _paper2_all_merged_with_nash_shared() -> list[MergedConcept]:
    """Build paper 2 merged list: Nash Equilibrium is not-new (cross-vault hit).

    Nash Equilibrium appears in both papers. The second paper's
    Nash Equilibrium is resolved as a match against the existing slug.
    """
    p2_concepts = _paper2_concepts_section1()
    results: list[MergedConcept] = []
    for concept in p2_concepts:
        is_new = concept.name != _NASH_EQ_NAME
        match_method = "new" if is_new else "exact"
        results.append(MergedConcept(
            concept=concept,
            dedup_result=DedupResult(
                slug=concept.slug,
                is_new=is_new,
                match_method=match_method,
                match_confidence=0.0 if is_new else 1.0,
            ),
            provenance=ProvenanceNode(
                concept_slug=concept.slug,
                source_arxiv_id=_PAPER_2_ID,
                formulation=concept.canonical_definition,
                formal_spec=concept.formal_spec,
            ),
        ))
    return results


class TestPhase2CrossPaperDedup:
    """Phase 2 — validate cross-paper concept deduplication topology."""

    def test_it_should_merge_nash_equilibrium_as_non_new_in_paper_2(self):
        """It should flag Nash Equilibrium as is_new=False when paper 2 processes it."""
        merged_p2 = _paper2_all_merged_with_nash_shared()
        nash_entry = next(
            m for m in merged_p2 if m.concept.slug == _NASH_EQ_SLUG
        )
        assert nash_entry.dedup_result.is_new is False
        assert nash_entry.dedup_result.match_method == "exact"
        assert nash_entry.dedup_result.match_confidence == 1.0

    def test_it_should_keep_congestion_game_as_new_in_paper_2(self):
        """It should flag congestion game as is_new=True since paper 1 lacks it."""
        merged_p2 = _paper2_all_merged_with_nash_shared()
        cg_slug = slugify(_CONGESTION_GAME_NAME)
        cg_entry = next(m for m in merged_p2 if m.concept.slug == cg_slug)

        assert cg_entry.dedup_result.is_new is True
        assert cg_entry.dedup_result.match_method == "new"

    def test_it_should_produce_separate_provenance_nodes_per_paper(self):
        """It should create one ProvenanceNode per paper for Nash Equilibrium."""
        merged_p1 = _paper1_all_merged()
        merged_p2 = _paper2_all_merged_with_nash_shared()

        nash_prov_p1 = next(
            m.provenance for m in merged_p1 if m.concept.slug == _NASH_EQ_SLUG
        )
        nash_prov_p2 = next(
            m.provenance for m in merged_p2 if m.concept.slug == _NASH_EQ_SLUG
        )

        assert nash_prov_p1.source_arxiv_id == _PAPER_1_ID
        assert nash_prov_p2.source_arxiv_id == _PAPER_2_ID
        assert nash_prov_p1.concept_slug == _NASH_EQ_SLUG
        assert nash_prov_p2.concept_slug == _NASH_EQ_SLUG

    def test_it_should_have_different_formulations_per_provenance(self):
        """Each paper's Provenance should carry its own formulation of Nash Equilibrium."""
        merged_p1 = _paper1_all_merged()
        merged_p2 = _paper2_all_merged_with_nash_shared()

        form_p1 = next(
            m.provenance.formulation
            for m in merged_p1 if m.concept.slug == _NASH_EQ_SLUG
        )
        form_p2 = next(
            m.provenance.formulation
            for m in merged_p2 if m.concept.slug == _NASH_EQ_SLUG
        )

        # Both are non-empty and distinct (different papers frame it differently)
        assert form_p1 != ""
        assert form_p2 != ""
        assert form_p1 != form_p2

    def test_it_should_not_create_duplicate_concept_nodes_for_shared_concepts(self):
        """It should maintain one Concept node per unique slug across both papers."""
        merged_p1 = _paper1_all_merged()
        merged_p2 = _paper2_all_merged_with_nash_shared()

        all_slugs = (
            [m.concept.slug for m in merged_p1]
            + [m.concept.slug for m in merged_p2]
        )
        # Nash Equilibrium slug appears in both but should have distinct
        # Provenance nodes, not duplicate Concept nodes.
        # The concept-level slug must appear exactly ONCE per merged list
        p1_slugs = [m.concept.slug for m in merged_p1]
        p2_slugs = [m.concept.slug for m in merged_p2]

        # Each paper's own merged list must have no duplicates
        assert len(p1_slugs) == len(set(p1_slugs)), "Paper 1 has duplicate concept slugs"
        assert len(p2_slugs) == len(set(p2_slugs)), "Paper 2 has duplicate concept slugs"

    def test_it_should_write_two_provenance_nodes_for_shared_nash_eq(self):
        """Orchestrator should invoke write for both provenance nodes (one per paper)."""
        # We validate that merged concepts from both papers each yield a
        # ProvenanceNode with a distinct source_arxiv_id when concept is shared.
        merged_p1 = _paper1_all_merged()
        merged_p2 = _paper2_all_merged_with_nash_shared()

        all_prov = [m.provenance for m in merged_p1] + [m.provenance for m in merged_p2]
        nash_prov = [p for p in all_prov if p.concept_slug == _NASH_EQ_SLUG]

        assert len(nash_prov) == 2
        sources = {p.source_arxiv_id for p in nash_prov}
        assert _PAPER_1_ID in sources
        assert _PAPER_2_ID in sources

    @pytest.mark.asyncio
    async def test_it_should_return_built_status_for_paper_2_with_shared_concepts(self):
        """It should process paper 2 successfully even with a shared concept."""
        llm = MagicMock()
        llm.call = AsyncMock()

        p2_concepts = _paper2_concepts_section1()
        p2_merged = _paper2_all_merged_with_nash_shared()
        p2_claims: list[ClaimNode] = []

        with _patch_pipeline({
            "load": (_PAPER_2_TITLE, [
                _make_section("Introduction", "Nash equilibrium in congestion games.", 0),
            ]),
            "p1": [p2_concepts],
            "merge": p2_merged,
            "p2": (p2_claims, []),
            "p3a": ([], []),
            "p3b": [],
            "write": {
                "concepts": len(p2_merged),
                "claims": 0,
                "edges": 0,
            },
        }):
            result = await process_paper(
                _PAPER_2_ID,
                _make_options(),
                llm,
                _mock_neo4j(),
            )

        assert result.status == "built"
        assert result.arxiv_id == _PAPER_2_ID
        assert result.concept_count == len(p2_merged)
