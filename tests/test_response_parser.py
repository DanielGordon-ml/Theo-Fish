"""
@file test_response_parser.py
@description Tests for the LLM response parser: concept, claim, and edge parsing.
"""

import json
import logging


from graph_builder.config.schema_types import (
    ClaimTypeDef,
    ConceptTypeDef,
    EdgeCategories,
    EdgeDef,
    FieldOwnership,
    GraphSchema,
    ValidationConfig,
    ValidationSeverity,
)
from graph_builder.llm.response_parser import parse_claims, parse_concepts, parse_edges
from graph_builder.models.claim import ClaimNode
from graph_builder.models.concept import ConceptNode
from graph_builder.models.edges import ClaimEdge, ConceptEdge, CouplingEdge


# ---------------------------------------------------------------------------
# Minimal schema fixture
# ---------------------------------------------------------------------------

def _make_schema(concept_types: dict | None = None, claim_types: dict | None = None) -> GraphSchema:
    """Build a minimal GraphSchema for use in parser tests."""
    concept_types = concept_types or {
        "structure": ConceptTypeDef(
            description="A mathematical structure",
            required_fields=["name", "semantic_type"],
        ),
        "operator": ConceptTypeDef(
            description="A mathematical operator",
            required_fields=["name", "semantic_type"],
        ),
    }
    claim_types = claim_types or {
        "theorem": ClaimTypeDef(
            description="A proven theorem",
            required_fields=["label", "claim_type", "conclusion"],
        ),
        "definition": ClaimTypeDef(
            description="A formal definition",
            required_fields=["label", "claim_type", "conclusion"],
        ),
    }
    return GraphSchema(
        version="1.0",
        last_updated="2025-01-01",
        concept_types=concept_types,
        claim_types=claim_types,
        edges=EdgeCategories(
            concept_edges={
                "GENERALIZES": EdgeDef(description="A generalizes B"),
            },
            claim_edges={
                "IMPLIES": EdgeDef(description="A implies B"),
            },
            coupling_edges={
                "ABOUT": EdgeDef(description="Claim is about concept"),
            },
            provenance_edges={},
        ),
        validation=ValidationConfig(rules=[], severity=ValidationSeverity()),
        field_ownership=FieldOwnership(),
    )


SCHEMA = _make_schema()

PAPER_SLUG = "test-paper-2024"

_VALID_CLAIM = {
    "label": "Theorem 4.1",
    "claim_type": "theorem",
    "conclusion": "Policy converges under mild assumptions.",
    "assumptions": ["MDP is finite"],
}


# ---------------------------------------------------------------------------
# parse_concepts tests
# ---------------------------------------------------------------------------

class TestParseConcepts:
    """Tests for parse_concepts()."""

    def test_it_should_parse_valid_concept_json_into_concept_nodes(self):
        """Valid JSON with 'concepts' key returns list of ConceptNode."""
        payload = json.dumps({
            "concepts": [
                {
                    "name": "MDP",
                    "semantic_type": "structure",
                    "formal_spec": "(S,A,P,R,γ)",
                    "canonical_definition": "Markov Decision Process",
                },
            ],
        })

        result = parse_concepts(payload, SCHEMA)

        assert len(result) == 1
        assert isinstance(result[0], ConceptNode)
        assert result[0].name == "MDP"
        assert result[0].semantic_type == "structure"
        assert result[0].formal_spec == "(S,A,P,R,γ)"

    def test_it_should_parse_multiple_concepts(self):
        """Multiple concepts in JSON all produce ConceptNode objects."""
        payload = json.dumps({
            "concepts": [
                {"name": "MDP", "semantic_type": "structure"},
                {"name": "Bellman Operator", "semantic_type": "operator"},
            ],
        })

        result = parse_concepts(payload, SCHEMA)

        assert len(result) == 2
        assert result[0].name == "MDP"
        assert result[1].name == "Bellman Operator"

    def test_it_should_skip_malformed_entries_and_log_warning(self, caplog):
        """Entries missing required fields are skipped with a warning logged."""
        payload = json.dumps({
            "concepts": [
                {"name": "Valid Concept", "semantic_type": "structure"},
                {"semantic_type": "structure"},  # missing 'name'
            ],
        })

        with caplog.at_level(logging.WARNING):
            result = parse_concepts(payload, SCHEMA)

        assert len(result) == 1
        assert result[0].name == "Valid Concept"
        assert any("skipping" in r.message.lower() or "malformed" in r.message.lower() or "invalid" in r.message.lower() for r in caplog.records)

    def test_it_should_return_empty_list_for_completely_invalid_json(self, caplog):
        """Non-JSON input returns empty list and logs a warning."""
        with caplog.at_level(logging.WARNING):
            result = parse_concepts("not valid json at all {{{{", SCHEMA)

        assert result == []
        assert len(caplog.records) >= 1

    def test_it_should_return_empty_list_for_missing_concepts_key(self, caplog):
        """JSON without 'concepts' key returns empty list."""
        payload = json.dumps({"something_else": []})

        with caplog.at_level(logging.WARNING):
            result = parse_concepts(payload, SCHEMA)

        assert result == []

    def test_it_should_validate_semantic_type_against_schema_concept_types(self, caplog):
        """Entries with unknown semantic_type are skipped with a warning."""
        payload = json.dumps({
            "concepts": [
                {"name": "Valid", "semantic_type": "structure"},
                {"name": "Invalid", "semantic_type": "nonexistent_type"},
            ],
        })

        with caplog.at_level(logging.WARNING):
            result = parse_concepts(payload, SCHEMA)

        assert len(result) == 1
        assert result[0].name == "Valid"
        assert any("nonexistent_type" in r.message or "semantic_type" in r.message for r in caplog.records)

    def test_it_should_auto_derive_slug_from_name(self):
        """ConceptNode.slug is derived from name if not provided."""
        payload = json.dumps({
            "concepts": [{"name": "Markov Decision Process", "semantic_type": "structure"}],
        })

        result = parse_concepts(payload, SCHEMA)

        assert result[0].slug == "markov-decision-process"


# ---------------------------------------------------------------------------
# parse_claims tests
# ---------------------------------------------------------------------------

class TestParseClaims:
    """Tests for parse_claims()."""

    def test_it_should_parse_valid_claim_json_into_claim_nodes(self):
        """Valid JSON with 'claims' key returns list of ClaimNode."""
        payload = json.dumps({
            "claims": [
                {
                    "label": "Theorem 4.1",
                    "claim_type": "theorem",
                    "conclusion": "Policy converges under mild assumptions.",
                    "assumptions": ["MDP is finite"],
                },
            ],
        })

        result = parse_claims(payload, PAPER_SLUG, SCHEMA)

        assert len(result) == 1
        assert isinstance(result[0], ClaimNode)
        assert result[0].label == "Theorem 4.1"
        assert result[0].claim_type == "theorem"
        assert result[0].source_paper_slug == PAPER_SLUG

    def test_it_should_compose_slug_from_paper_slug_and_label(self):
        """ClaimNode slug is paper_slug--label_slug."""
        payload = json.dumps({
            "claims": [
                {"label": "Lemma 2.3", "claim_type": "theorem", "conclusion": "foo"},
            ],
        })

        result = parse_claims(payload, PAPER_SLUG, SCHEMA)

        assert result[0].slug == f"{PAPER_SLUG}--lemma-2-3"

    def test_it_should_skip_malformed_claim_entries_and_log_warning(self, caplog):
        """Claims missing required fields are skipped with a warning."""
        payload = json.dumps({
            "claims": [
                {"label": "Theorem 1.0", "claim_type": "theorem", "conclusion": "valid"},
                {"claim_type": "theorem"},  # missing 'label'
            ],
        })

        with caplog.at_level(logging.WARNING):
            result = parse_claims(payload, PAPER_SLUG, SCHEMA)

        assert len(result) == 1
        assert result[0].label == "Theorem 1.0"
        assert any(r.levelno >= logging.WARNING for r in caplog.records)

    def test_it_should_return_empty_list_for_completely_invalid_json(self, caplog):
        """Non-JSON input returns empty list and logs a warning."""
        with caplog.at_level(logging.WARNING):
            result = parse_claims("garbage_input[]]]", PAPER_SLUG, SCHEMA)

        assert result == []

    def test_it_should_validate_claim_type_against_schema_claim_types(self, caplog):
        """Claims with unknown claim_type are skipped."""
        payload = json.dumps({
            "claims": [
                {"label": "Theorem 1", "claim_type": "theorem", "conclusion": "valid"},
                {"label": "Unknown 2", "claim_type": "nonsense_type", "conclusion": "x"},
            ],
        })

        with caplog.at_level(logging.WARNING):
            result = parse_claims(payload, PAPER_SLUG, SCHEMA)

        assert len(result) == 1
        assert result[0].label == "Theorem 1"

    def test_it_should_parse_proof_field(self):
        """It should populate ClaimNode.proof from LLM response."""
        schema = _make_schema()
        claim_data = {**_VALID_CLAIM, "proof": "By induction on n."}
        json_str = json.dumps({"claims": [claim_data]})
        claims = parse_claims(json_str, PAPER_SLUG, schema)
        assert claims[0].proof == "By induction on n."

    def test_it_should_parse_proof_technique_field(self):
        """It should populate ClaimNode.proof_technique from LLM response."""
        schema = _make_schema()
        claim_data = {**_VALID_CLAIM, "proof_technique": "induction"}
        json_str = json.dumps({"claims": [claim_data]})
        claims = parse_claims(json_str, PAPER_SLUG, schema)
        assert claims[0].proof_technique == "induction"

    def test_it_should_parse_strength_field(self):
        """It should populate ClaimNode.strength from LLM response."""
        schema = _make_schema()
        claim_data = {**_VALID_CLAIM, "strength": "exact"}
        json_str = json.dumps({"claims": [claim_data]})
        claims = parse_claims(json_str, PAPER_SLUG, schema)
        assert claims[0].strength == "exact"

    def test_it_should_parse_confidence_field(self):
        """It should populate ClaimNode.confidence from LLM response."""
        schema = _make_schema()
        claim_data = {**_VALID_CLAIM, "confidence": 0.85}
        json_str = json.dumps({"claims": [claim_data]})
        claims = parse_claims(json_str, PAPER_SLUG, schema)
        assert claims[0].confidence == 0.85

    def test_it_should_ignore_about_concepts_in_claim_construction(self):
        """It should not pass about_concepts to ClaimNode constructor."""
        schema = _make_schema()
        claim_data = {**_VALID_CLAIM, "about_concepts": ["slug1", "slug2"]}
        json_str = json.dumps({"claims": [claim_data]})
        claims = parse_claims(json_str, PAPER_SLUG, schema)
        assert len(claims) == 1  # Should not raise validation error


# ---------------------------------------------------------------------------
# parse_edges tests
# ---------------------------------------------------------------------------

class TestParseEdges:
    """Tests for parse_edges()."""

    def test_it_should_parse_valid_concept_edges(self):
        """Valid concept edges produce ConceptEdge objects."""
        payload = json.dumps({
            "concept_edges": [
                {
                    "source_slug": "mdp",
                    "target_slug": "pomdp",
                    "edge_type": "GENERALIZES",
                },
            ],
            "claim_edges": [],
            "coupling_edges": [],
        })

        concept_edges, claim_edges, coupling_edges = parse_edges(payload, SCHEMA)

        assert len(concept_edges) == 1
        assert isinstance(concept_edges[0], ConceptEdge)
        assert concept_edges[0].source_slug == "mdp"
        assert concept_edges[0].edge_type == "GENERALIZES"

    def test_it_should_parse_valid_claim_edges(self):
        """Valid claim edges produce ClaimEdge objects."""
        payload = json.dumps({
            "concept_edges": [],
            "claim_edges": [
                {
                    "source_slug": "paper--theorem-1",
                    "target_slug": "paper--theorem-2",
                    "edge_type": "IMPLIES",
                },
            ],
            "coupling_edges": [],
        })

        concept_edges, claim_edges, coupling_edges = parse_edges(payload, SCHEMA)

        assert len(claim_edges) == 1
        assert isinstance(claim_edges[0], ClaimEdge)

    def test_it_should_parse_valid_coupling_edges(self):
        """Valid coupling edges produce CouplingEdge objects."""
        payload = json.dumps({
            "concept_edges": [],
            "claim_edges": [],
            "coupling_edges": [
                {"claim_slug": "paper--theorem-1", "concept_slug": "mdp"},
            ],
        })

        concept_edges, claim_edges, coupling_edges = parse_edges(payload, SCHEMA)

        assert len(coupling_edges) == 1
        assert isinstance(coupling_edges[0], CouplingEdge)
        assert coupling_edges[0].claim_slug == "paper--theorem-1"

    def test_it_should_return_empty_lists_for_invalid_json(self, caplog):
        """Completely invalid JSON returns three empty lists and logs a warning."""
        with caplog.at_level(logging.WARNING):
            concept_edges, claim_edges, coupling_edges = parse_edges("not json", SCHEMA)

        assert concept_edges == []
        assert claim_edges == []
        assert coupling_edges == []

    def test_it_should_skip_malformed_edge_entries_and_log_warning(self, caplog):
        """Edge entries missing required fields are skipped."""
        payload = json.dumps({
            "concept_edges": [
                {"source_slug": "a", "target_slug": "b", "edge_type": "GENERALIZES"},
                {"source_slug": "c"},  # missing target_slug and edge_type
            ],
            "claim_edges": [],
            "coupling_edges": [],
        })

        with caplog.at_level(logging.WARNING):
            concept_edges, claim_edges, coupling_edges = parse_edges(payload, SCHEMA)

        assert len(concept_edges) == 1
        assert any(r.levelno >= logging.WARNING for r in caplog.records)
