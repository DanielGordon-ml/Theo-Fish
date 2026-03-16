"""
@file validator.py
@description Schema-driven validation of extracted graph data.

Errors block writes; warnings are logged only.
Rule codes match schema.yaml severity lists.
"""

from graph_builder.config.schema_types import EdgeCategories, GraphSchema
from graph_builder.models.claim import ClaimNode
from graph_builder.models.concept import ConceptNode
from graph_builder.models.edges import ClaimEdge, ConceptEdge, CouplingEdge
from graph_builder.models.provenance import ProvenanceNode
from graph_builder.models.results import ValidationResult
from graph_builder.validation.cycle_detector import detect_depends_on_cycles

COROLLARY = "corollary"
DEPENDS_ON = "depends_on"


def validate_paper(
    concepts: list[ConceptNode],
    claims: list[ClaimNode],
    concept_edges: list[ConceptEdge],
    claim_edges: list[ClaimEdge],
    coupling_edges: list[CouplingEdge],
    provenances: list[ProvenanceNode],
    schema: GraphSchema,
) -> ValidationResult:
    """Validate extracted data against schema rules.

    Runs all validation checks in a single pass and collects every issue.
    Returns a ValidationResult where is_valid is False only when errors exist;
    warnings are accumulated but do not block writes.

    @raises nothing — all issues are captured in the result.
    """
    errors: list[str] = []
    warnings: list[str] = []

    _check_missing_about(claims, coupling_edges, errors)
    _check_missing_provenance(concepts, provenances, errors)
    _check_corollary_depends_on(claims, claim_edges, warnings)
    _check_unknown_edge_types(concept_edges, claim_edges, schema.edges, errors)
    _check_unknown_attributes(concept_edges, claim_edges, schema.edges, warnings)
    _check_depends_on_cycles(claim_edges, warnings)
    _check_inconsistent_inverses(concept_edges, schema.edges, errors)

    return ValidationResult(
        is_valid=len(errors) == 0,
        errors=errors,
        warnings=warnings,
    )


# ---------------------------------------------------------------------------
# Individual rule checkers
# ---------------------------------------------------------------------------

def _check_missing_about(
    claims: list[ClaimNode],
    coupling_edges: list[CouplingEdge],
    errors: list[str],
) -> None:
    """Error: every claim must have at least one ABOUT (coupling) edge."""
    claimed_slugs = {e.claim_slug for e in coupling_edges}
    for claim in claims:
        if claim.slug not in claimed_slugs:
            errors.append(f"missing_about: claim '{claim.slug}' has no ABOUT edge")


def _check_missing_provenance(
    concepts: list[ConceptNode],
    provenances: list[ProvenanceNode],
    errors: list[str],
) -> None:
    """Error: every concept must have at least one ProvenanceNode."""
    covered = {p.concept_slug for p in provenances}
    for concept in concepts:
        if concept.slug not in covered:
            errors.append(
                f"missing_provenance: concept '{concept.slug}' has no provenance node"
            )


def _check_corollary_depends_on(
    claims: list[ClaimNode],
    claim_edges: list[ClaimEdge],
    warnings: list[str],
) -> None:
    """Warning: corollary claims should have at least one DEPENDS_ON edge."""
    sources_with_depends_on = {
        e.source_slug for e in claim_edges if e.edge_type == DEPENDS_ON
    }
    for claim in claims:
        if claim.claim_type == COROLLARY and claim.slug not in sources_with_depends_on:
            warnings.append(
                f"corollary_without_depends_on: corollary '{claim.slug}' has no DEPENDS_ON edge"
            )


def _check_unknown_edge_types(
    concept_edges: list[ConceptEdge],
    claim_edges: list[ClaimEdge],
    edge_categories: EdgeCategories,
    errors: list[str],
) -> None:
    """Error: every edge_type must exist in the schema."""
    known_concept = set(edge_categories.concept_edges)
    known_claim = set(edge_categories.claim_edges)

    for edge in concept_edges:
        if edge.edge_type not in known_concept:
            errors.append(
                f"unknown_edge_type: concept edge '{edge.edge_type}' "
                f"({edge.source_slug} -> {edge.target_slug}) not in schema"
            )
    for edge in claim_edges:
        if edge.edge_type not in known_claim:
            errors.append(
                f"unknown_edge_type: claim edge '{edge.edge_type}' "
                f"({edge.source_slug} -> {edge.target_slug}) not in schema"
            )


def _check_unknown_attributes(
    concept_edges: list[ConceptEdge],
    claim_edges: list[ClaimEdge],
    edge_categories: EdgeCategories,
    warnings: list[str],
) -> None:
    """Warning: every attribute on an edge must be listed in the schema."""
    for edge in concept_edges:
        defn = edge_categories.concept_edges.get(edge.edge_type)
        if defn is None:
            continue
        _audit_attributes(edge.attributes, defn.attributes, edge.edge_type, warnings)

    for edge in claim_edges:
        defn = edge_categories.claim_edges.get(edge.edge_type)
        if defn is None:
            continue
        _audit_attributes(edge.attributes, defn.attributes, edge.edge_type, warnings)


def _audit_attributes(
    used: dict,
    allowed: list[str],
    edge_type: str,
    warnings: list[str],
) -> None:
    """Append a warning for each attribute key not listed in allowed."""
    for key in used:
        if key not in allowed:
            warnings.append(
                f"unknown_attribute: attribute '{key}' on edge type '{edge_type}' not in schema"
            )


def _check_depends_on_cycles(
    claim_edges: list[ClaimEdge],
    warnings: list[str],
) -> None:
    """Warning: DEPENDS_ON edges must not form cycles."""
    cycles = detect_depends_on_cycles(claim_edges)
    for cycle in cycles:
        path_str = " -> ".join(cycle)
        warnings.append(f"cycle_in_depends_on: cycle detected [{path_str}]")


def _check_inconsistent_inverses(
    concept_edges: list[ConceptEdge],
    edge_categories: EdgeCategories,
    errors: list[str],
) -> None:
    """Error: if A generalizes B then B must not also generalizes A (inverse consistency)."""
    edge_pairs: set[tuple[str, str, str]] = {
        (e.source_slug, e.target_slug, e.edge_type) for e in concept_edges
    }

    for edge in concept_edges:
        defn = edge_categories.concept_edges.get(edge.edge_type)
        if defn is None or defn.inverse is None:
            continue
        inverse_exists = (edge.target_slug, edge.source_slug, edge.edge_type) in edge_pairs
        if inverse_exists:
            errors.append(
                f"inconsistent_inverse: '{edge.source_slug}' {edge.edge_type} '{edge.target_slug}' "
                f"but reverse also uses '{edge.edge_type}' (expected '{defn.inverse}')"
            )
