"""
@file test_schema_loader.py
@description Tests for YAML schema loading and validation.
"""

import pytest
from pathlib import Path

from graph_builder.config.schema_loader import load_schema
from graph_builder.config.schema_types import (
    GraphSchema,
)


SCHEMA_PATH = Path("data_vault/_meta/schema.yaml")


class TestLoadSchema:
    def test_loads_real_schema(self):
        """It should parse the real schema.yaml into a GraphSchema."""
        schema = load_schema(SCHEMA_PATH)
        assert isinstance(schema, GraphSchema)
        assert schema.version == "2.1"

    def test_concept_types_loaded(self):
        """It should load all 9 concept types."""
        schema = load_schema(SCHEMA_PATH)
        expected = {
            "structure", "space", "operator", "property",
            "quantity", "relation", "class", "problem", "criterion",
        }
        assert set(schema.concept_types.keys()) == expected

    def test_claim_types_loaded(self):
        """It should load all 6 claim types."""
        schema = load_schema(SCHEMA_PATH)
        expected = {
            "theorem", "lemma", "proposition",
            "corollary", "conjecture", "algorithm",
        }
        assert set(schema.claim_types.keys()) == expected

    def test_concept_type_has_required_fields(self):
        """It should parse required and optional fields per type."""
        schema = load_schema(SCHEMA_PATH)
        structure = schema.concept_types["structure"]
        assert "name" in structure.required_fields
        assert "formal_spec" in structure.required_fields
        assert "components" in structure.optional_fields

    def test_edge_types_loaded(self):
        """It should load concept, claim, coupling, and provenance edges."""
        schema = load_schema(SCHEMA_PATH)
        assert "generalizes" in schema.edges.concept_edges
        assert "depends_on" in schema.edges.claim_edges
        assert "about" in schema.edges.coupling_edges
        assert "sourced_from" in schema.edges.provenance_edges

    def test_inverse_symmetry(self):
        """It should have symmetric inverse declarations."""
        schema = load_schema(SCHEMA_PATH)
        gen = schema.edges.concept_edges["generalizes"]
        spec = schema.edges.concept_edges["specializes"]
        assert gen.inverse == "specializes"
        assert spec.inverse == "generalizes"

    def test_edge_has_attributes(self):
        """It should parse edge attribute lists."""
        schema = load_schema(SCHEMA_PATH)
        depends = schema.edges.claim_edges["depends_on"]
        assert "role" in depends.attributes
        assert "applied_to" in depends.attributes

    def test_validation_rules_loaded(self):
        """It should load validation rules with severity levels."""
        schema = load_schema(SCHEMA_PATH)
        assert "missing_about" in schema.validation.severity["error"]
        assert "cycle_in_depends_on" in schema.validation.severity["warning"]

    def test_field_ownership_loaded(self):
        """It should load field ownership categories."""
        schema = load_schema(SCHEMA_PATH)
        assert "slug" in schema.field_ownership.pipeline_owned
        assert "human_notes" in schema.field_ownership.human_owned
        assert "aliases" in schema.field_ownership.shared

    def test_rejects_unknown_yaml_key(self, tmp_path):
        """It should raise on unrecognized top-level keys."""
        bad = tmp_path / "bad.yaml"
        bad.write_text("version: '1.0'\nunknown_key: true\n")
        with pytest.raises(ValueError, match="unknown_key"):
            load_schema(bad)
