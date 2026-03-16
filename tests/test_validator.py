"""
@file test_validator.py
@description Tests for graph validation rules: errors, warnings, cycles, and inverse consistency.
"""

import pytest

from graph_builder.config.schema_types import (
    EdgeCategories,
    EdgeDef,
    GraphSchema,
    ValidationConfig,
    ValidationSeverity,
    ConceptTypeDef,
    ClaimTypeDef,
    FieldOwnership,
)
from graph_builder.models.claim import ClaimNode
from graph_builder.models.concept import ConceptNode
from graph_builder.models.edges import ClaimEdge, ConceptEdge, CouplingEdge
from graph_builder.models.provenance import ProvenanceNode
from graph_builder.models.results import ValidationResult
from graph_builder.validation.cycle_detector import detect_depends_on_cycles
from graph_builder.validation.validator import validate_paper


# ---------------------------------------------------------------------------
# Helpers / fixtures
# ---------------------------------------------------------------------------

def _make_schema() -> GraphSchema:
    """Return a minimal GraphSchema mirroring the real schema.yaml structure."""
    return GraphSchema(
        version="2.1",
        last_updated="2026-03-16",
        concept_types={
            "structure": ConceptTypeDef(
                description="Named mathematical objects",
                required_fields=["name", "formal_spec"],
            )
        },
        claim_types={
            "theorem": ClaimTypeDef(
                description="Major proven result",
                required_fields=["name", "assumptions", "conclusion"],
            ),
            "corollary": ClaimTypeDef(
                description="Direct consequence",
                required_fields=["name", "conclusion"],
            ),
        },
        edges=EdgeCategories(
            concept_edges={
                "generalizes": EdgeDef(
                    description="Source generalizes target",
                    attributes=["condition"],
                    inverse="specializes",
                ),
                "specializes": EdgeDef(
                    description="Source specializes target",
                    attributes=["restriction"],
                    inverse="generalizes",
                ),
            },
            claim_edges={
                "depends_on": EdgeDef(
                    description="Source depends on target",
                    attributes=["role", "applied_to"],
                ),
                "enables": EdgeDef(
                    description="Source enables target",
                    attributes=["nature"],
                ),
            },
            coupling_edges={
                "about": EdgeDef(
                    description="Claim concerns concept",
                    attributes=["role", "aspect"],
                )
            },
            provenance_edges={},
        ),
        validation=ValidationConfig(
            rules=[],
            severity=ValidationSeverity(
                error=["missing_about", "missing_provenance", "unknown_edge_type", "inconsistent_inverse"],
                warning=["cycle_in_depends_on", "unknown_attribute", "corollary_without_depends_on"],
            ),
        ),
        field_ownership=FieldOwnership(),
    )


def _concept(name: str = "MDP") -> ConceptNode:
    return ConceptNode(name=name, semantic_type="structure")


def _claim(label: str = "Theorem 1", claim_type: str = "theorem") -> ClaimNode:
    return ClaimNode(
        source_paper_slug="paper-2401",
        label=label,
        claim_type=claim_type,
    )


def _provenance(concept_slug: str) -> ProvenanceNode:
    return ProvenanceNode(concept_slug=concept_slug, source_arxiv_id="2401.00001")


def _about(claim_slug: str, concept_slug: str) -> CouplingEdge:
    return CouplingEdge(claim_slug=claim_slug, concept_slug=concept_slug)


# ---------------------------------------------------------------------------
# Happy path
# ---------------------------------------------------------------------------

class TestValidatePaperHappyPath:
    def test_should_pass_when_all_rules_satisfied(self):
        """It should return is_valid=True with no errors or warnings when data is clean."""
        concept = _concept("MDP")
        claim = _claim("Theorem 1", "theorem")
        coupling = _about(claim.slug, concept.slug)
        provenance = _provenance(concept.slug)
        schema = _make_schema()

        result = validate_paper(
            concepts=[concept],
            claims=[claim],
            concept_edges=[],
            claim_edges=[],
            coupling_edges=[coupling],
            provenances=[provenance],
            schema=schema,
        )

        assert result.is_valid is True
        assert result.errors == []
        assert result.warnings == []


# ---------------------------------------------------------------------------
# Error rules
# ---------------------------------------------------------------------------

class TestMissingAbout:
    def test_should_error_when_claim_has_no_about_edge(self):
        """It should report missing_about error for claims with no ABOUT coupling."""
        concept = _concept()
        claim = _claim("Theorem 1")
        provenance = _provenance(concept.slug)
        schema = _make_schema()

        result = validate_paper(
            concepts=[concept],
            claims=[claim],
            concept_edges=[],
            claim_edges=[],
            coupling_edges=[],         # no ABOUT edges at all
            provenances=[provenance],
            schema=schema,
        )

        assert result.is_valid is False
        assert any("missing_about" in e for e in result.errors)
        assert claim.slug in " ".join(result.errors)


class TestMissingProvenance:
    def test_should_error_when_concept_has_no_provenance(self):
        """It should report missing_provenance error for concepts with no ProvenanceNode."""
        concept = _concept("Bellman Operator")
        claim = _claim("Theorem 2")
        coupling = _about(claim.slug, concept.slug)
        schema = _make_schema()

        result = validate_paper(
            concepts=[concept],
            claims=[claim],
            concept_edges=[],
            claim_edges=[],
            coupling_edges=[coupling],
            provenances=[],            # no provenance nodes
            schema=schema,
        )

        assert result.is_valid is False
        assert any("missing_provenance" in e for e in result.errors)
        assert concept.slug in " ".join(result.errors)


class TestUnknownEdgeType:
    def test_should_error_on_unknown_claim_edge_type(self):
        """It should report unknown_edge_type error when edge_type is not in schema."""
        concept = _concept()
        claim_a = _claim("Theorem A")
        claim_b = _claim("Theorem B")
        coupling_a = _about(claim_a.slug, concept.slug)
        coupling_b = _about(claim_b.slug, concept.slug)
        provenance = _provenance(concept.slug)
        schema = _make_schema()

        bad_edge = ClaimEdge(
            source_slug=claim_a.slug,
            target_slug=claim_b.slug,
            edge_type="invented_type",
        )

        result = validate_paper(
            concepts=[concept],
            claims=[claim_a, claim_b],
            concept_edges=[],
            claim_edges=[bad_edge],
            coupling_edges=[coupling_a, coupling_b],
            provenances=[provenance],
            schema=schema,
        )

        assert result.is_valid is False
        assert any("unknown_edge_type" in e for e in result.errors)

    def test_should_error_on_unknown_concept_edge_type(self):
        """It should report unknown_edge_type error for concept edges not in schema."""
        concept_a = _concept("MDP")
        concept_b = _concept("POMDP")
        claim = _claim("Theorem 1")
        coupling = _about(claim.slug, concept_a.slug)
        prov_a = _provenance(concept_a.slug)
        prov_b = _provenance(concept_b.slug)
        schema = _make_schema()

        bad_edge = ConceptEdge(
            source_slug=concept_a.slug,
            target_slug=concept_b.slug,
            edge_type="mystery_relation",
        )

        result = validate_paper(
            concepts=[concept_a, concept_b],
            claims=[claim],
            concept_edges=[bad_edge],
            claim_edges=[],
            coupling_edges=[coupling],
            provenances=[prov_a, prov_b],
            schema=schema,
        )

        assert result.is_valid is False
        assert any("unknown_edge_type" in e for e in result.errors)


class TestInconsistentInverse:
    def test_should_error_on_inconsistent_inverse_generalizes(self):
        """It should error when A generalizes B and B generalizes A simultaneously."""
        concept_a = _concept("MDP")
        concept_b = _concept("POMDP")
        claim = _claim("Theorem 1")
        coupling = _about(claim.slug, concept_a.slug)
        prov_a = _provenance(concept_a.slug)
        prov_b = _provenance(concept_b.slug)
        schema = _make_schema()

        edge_ab = ConceptEdge(
            source_slug=concept_a.slug,
            target_slug=concept_b.slug,
            edge_type="generalizes",
        )
        # inconsistent: B also generalizes A (should be specializes)
        edge_ba = ConceptEdge(
            source_slug=concept_b.slug,
            target_slug=concept_a.slug,
            edge_type="generalizes",
        )

        result = validate_paper(
            concepts=[concept_a, concept_b],
            claims=[claim],
            concept_edges=[edge_ab, edge_ba],
            claim_edges=[],
            coupling_edges=[coupling],
            provenances=[prov_a, prov_b],
            schema=schema,
        )

        assert result.is_valid is False
        assert any("inconsistent_inverse" in e for e in result.errors)


# ---------------------------------------------------------------------------
# Warning rules
# ---------------------------------------------------------------------------

class TestCorollaryWithoutDependsOn:
    def test_should_warn_when_corollary_has_no_depends_on_edge(self):
        """It should warn (not error) when a corollary claim has no DEPENDS_ON edge."""
        concept = _concept()
        corollary = _claim("Corollary 1", "corollary")
        coupling = _about(corollary.slug, concept.slug)
        provenance = _provenance(concept.slug)
        schema = _make_schema()

        result = validate_paper(
            concepts=[concept],
            claims=[corollary],
            concept_edges=[],
            claim_edges=[],            # no depends_on edges
            coupling_edges=[coupling],
            provenances=[provenance],
            schema=schema,
        )

        assert result.is_valid is True   # warnings do not block
        assert any("corollary_without_depends_on" in w for w in result.warnings)
        assert corollary.slug in " ".join(result.warnings)


class TestUnknownAttribute:
    def test_should_warn_on_unknown_attribute_on_edge(self):
        """It should warn when an edge carries an attribute not listed in the schema."""
        concept = _concept()
        claim_a = _claim("Theorem A")
        claim_b = _claim("Theorem B")
        coupling_a = _about(claim_a.slug, concept.slug)
        coupling_b = _about(claim_b.slug, concept.slug)
        provenance = _provenance(concept.slug)
        schema = _make_schema()

        edge_with_extra = ClaimEdge(
            source_slug=claim_a.slug,
            target_slug=claim_b.slug,
            edge_type="depends_on",
            attributes={"role": "bound", "ghost_field": "unexpected"},
        )

        result = validate_paper(
            concepts=[concept],
            claims=[claim_a, claim_b],
            concept_edges=[],
            claim_edges=[edge_with_extra],
            coupling_edges=[coupling_a, coupling_b],
            provenances=[provenance],
            schema=schema,
        )

        assert result.is_valid is True
        assert any("unknown_attribute" in w for w in result.warnings)


class TestDependsOnCycleWarning:
    def test_should_warn_on_depends_on_cycle(self):
        """It should warn (not error) when DEPENDS_ON edges form a cycle."""
        concept = _concept()
        claim_a = _claim("Theorem A")
        claim_b = _claim("Theorem B")
        claim_c = _claim("Theorem C")
        for c in [claim_a, claim_b, claim_c]:
            _ = _about(c.slug, concept.slug)
        couplings = [
            _about(claim_a.slug, concept.slug),
            _about(claim_b.slug, concept.slug),
            _about(claim_c.slug, concept.slug),
        ]
        provenance = _provenance(concept.slug)
        schema = _make_schema()

        # A -> B -> C -> A cycle
        cycle_edges = [
            ClaimEdge(source_slug=claim_a.slug, target_slug=claim_b.slug, edge_type="depends_on"),
            ClaimEdge(source_slug=claim_b.slug, target_slug=claim_c.slug, edge_type="depends_on"),
            ClaimEdge(source_slug=claim_c.slug, target_slug=claim_a.slug, edge_type="depends_on"),
        ]

        result = validate_paper(
            concepts=[concept],
            claims=[claim_a, claim_b, claim_c],
            concept_edges=[],
            claim_edges=cycle_edges,
            coupling_edges=couplings,
            provenances=[provenance],
            schema=schema,
        )

        assert result.is_valid is True          # cycle is a warning, not an error
        assert any("cycle_in_depends_on" in w for w in result.warnings)


# ---------------------------------------------------------------------------
# Multi-issue and validity semantics
# ---------------------------------------------------------------------------

class TestMultipleIssues:
    def test_should_collect_multiple_errors_and_warnings_in_one_pass(self):
        """It should accumulate all errors and warnings rather than stopping at first."""
        concept_a = _concept("MDP")
        concept_b = _concept("Policy")
        # concept_a has provenance, concept_b does not
        claim_no_about = _claim("Theorem No About")
        claim_with_about = _claim("Corollary With About", "corollary")
        coupling = _about(claim_with_about.slug, concept_a.slug)
        provenance = _provenance(concept_a.slug)
        schema = _make_schema()

        result = validate_paper(
            concepts=[concept_a, concept_b],
            claims=[claim_no_about, claim_with_about],
            concept_edges=[],
            claim_edges=[],
            coupling_edges=[coupling],
            provenances=[provenance],
            schema=schema,
        )

        # missing_about for claim_no_about AND missing_provenance for concept_b
        error_text = " ".join(result.errors)
        assert any("missing_about" in e for e in result.errors)
        assert any("missing_provenance" in e for e in result.errors)
        # corollary_without_depends_on for claim_with_about
        assert any("corollary_without_depends_on" in w for w in result.warnings)
        assert result.is_valid is False


class TestValiditySemantics:
    def test_should_return_is_valid_true_when_only_warnings_exist(self):
        """It should return is_valid=True when there are warnings but no errors."""
        concept = _concept()
        corollary = _claim("Corollary 1", "corollary")
        coupling = _about(corollary.slug, concept.slug)
        provenance = _provenance(concept.slug)
        schema = _make_schema()

        result = validate_paper(
            concepts=[concept],
            claims=[corollary],
            concept_edges=[],
            claim_edges=[],
            coupling_edges=[coupling],
            provenances=[provenance],
            schema=schema,
        )

        assert result.is_valid is True
        assert len(result.warnings) > 0
        assert result.errors == []

    def test_should_return_is_valid_false_when_errors_exist(self):
        """It should return is_valid=False when at least one error is present."""
        concept = _concept()
        claim = _claim("Theorem 1")
        # no ABOUT edge -> missing_about error
        provenance = _provenance(concept.slug)
        schema = _make_schema()

        result = validate_paper(
            concepts=[concept],
            claims=[claim],
            concept_edges=[],
            claim_edges=[],
            coupling_edges=[],
            provenances=[provenance],
            schema=schema,
        )

        assert result.is_valid is False
        assert len(result.errors) > 0


# ---------------------------------------------------------------------------
# cycle_detector unit tests
# ---------------------------------------------------------------------------

class TestDetectDependsOnCycles:
    def test_should_return_empty_when_no_edges(self):
        """It should return no cycles for an empty edge list."""
        assert detect_depends_on_cycles([]) == []

    def test_should_return_empty_for_acyclic_chain(self):
        """It should return no cycles for a linear depends_on chain."""
        edges = [
            ClaimEdge(source_slug="a", target_slug="b", edge_type="depends_on"),
            ClaimEdge(source_slug="b", target_slug="c", edge_type="depends_on"),
        ]
        assert detect_depends_on_cycles(edges) == []

    def test_should_detect_simple_two_node_cycle(self):
        """It should detect a cycle between two nodes."""
        edges = [
            ClaimEdge(source_slug="a", target_slug="b", edge_type="depends_on"),
            ClaimEdge(source_slug="b", target_slug="a", edge_type="depends_on"),
        ]
        cycles = detect_depends_on_cycles(edges)
        assert len(cycles) >= 1
        # each cycle path contains both nodes
        cycle_nodes = {n for path in cycles for n in path}
        assert "a" in cycle_nodes
        assert "b" in cycle_nodes

    def test_should_detect_three_node_cycle(self):
        """It should detect a three-node cycle A->B->C->A."""
        edges = [
            ClaimEdge(source_slug="a", target_slug="b", edge_type="depends_on"),
            ClaimEdge(source_slug="b", target_slug="c", edge_type="depends_on"),
            ClaimEdge(source_slug="c", target_slug="a", edge_type="depends_on"),
        ]
        cycles = detect_depends_on_cycles(edges)
        assert len(cycles) >= 1

    def test_should_ignore_non_depends_on_edges(self):
        """It should only consider depends_on edge_type when detecting cycles."""
        edges = [
            ClaimEdge(source_slug="a", target_slug="b", edge_type="enables"),
            ClaimEdge(source_slug="b", target_slug="a", edge_type="enables"),
        ]
        assert detect_depends_on_cycles(edges) == []
