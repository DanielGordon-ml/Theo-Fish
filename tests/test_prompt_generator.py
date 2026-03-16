"""
@file test_prompt_generator.py
@description Tests for the schema-driven prompt generator for all extraction passes.
"""

import pytest
from pathlib import Path

from graph_builder.config.schema_loader import load_schema
from graph_builder.config.schema_types import (
    GraphSchema,
    ConceptTypeDef,
    ClaimTypeDef,
    EdgeDef,
    EdgeCategories,
    ValidationConfig,
    FieldOwnership,
)
from graph_builder.extraction.prompt_generator import (
    build_concept_prompt,
    build_claim_prompt,
    build_edge_enrichment_prompt,
    build_gap_fill_prompt,
)

SCHEMA_PATH = Path("data_vault/_meta/schema.yaml")

ALL_CONCEPT_TYPES = {
    "structure", "space", "operator", "property",
    "quantity", "relation", "class", "problem", "criterion",
}

ALL_CLAIM_TYPES = {
    "theorem", "lemma", "proposition",
    "corollary", "conjecture", "algorithm",
}


@pytest.fixture(scope="module")
def schema() -> GraphSchema:
    """Load the real schema for use across tests."""
    return load_schema(SCHEMA_PATH)


@pytest.fixture
def minimal_schema() -> GraphSchema:
    """Build a minimal in-memory schema for mutation tests."""
    return GraphSchema(
        version="1.0",
        last_updated="2026-01-01",
        concept_types={
            "structure": ConceptTypeDef(
                description="Named mathematical objects",
                required_fields=["name", "formal_spec"],
                optional_fields=["components"],
            ),
        },
        claim_types={
            "theorem": ClaimTypeDef(
                description="Major proven result",
                required_fields=["name", "assumptions", "conclusion"],
                optional_fields=["strength"],
            ),
        },
        edges=EdgeCategories(
            claim_edges={
                "depends_on": EdgeDef(
                    description="Source uses target",
                    attributes=["role", "applied_to"],
                ),
            },
            coupling_edges={
                "about": EdgeDef(
                    description="Claim concerns concept",
                    attributes=["role", "aspect"],
                ),
            },
        ),
        validation=ValidationConfig(),
        field_ownership=FieldOwnership(),
    )


class TestBuildConceptPrompt:
    """Tests for build_concept_prompt."""

    def test_it_should_contain_all_nine_concept_types(self, schema):
        """It should generate a concept extraction prompt containing all 9 concept types."""
        prompt = build_concept_prompt(schema)
        for concept_type in ALL_CONCEPT_TYPES:
            assert concept_type in prompt, f"Missing concept type: {concept_type}"

    def test_it_should_include_required_fields_per_type(self, schema):
        """It should include required fields for each concept type."""
        prompt = build_concept_prompt(schema)
        # structure requires name and formal_spec
        assert "formal_spec" in prompt
        # operator requires domain and codomain
        assert "domain" in prompt
        assert "codomain" in prompt

    def test_it_should_include_optional_fields_per_type(self, schema):
        """It should include optional fields for each concept type."""
        prompt = build_concept_prompt(schema)
        # structure has optional: components, notation, parametrization
        assert "components" in prompt
        assert "notation" in prompt

    def test_it_should_instruct_json_output_with_concepts_key(self, schema):
        """It should instruct the LLM to output JSON with a 'concepts' key."""
        prompt = build_concept_prompt(schema)
        assert '"concepts"' in prompt or "'concepts'" in prompt or "concepts" in prompt

    def test_it_should_instruct_to_extract_objects_not_claims(self, schema):
        """It should explicitly instruct to extract objects, not claims."""
        prompt = build_concept_prompt(schema)
        lower = prompt.lower()
        assert "object" in lower or "concept" in lower

    def test_it_should_include_concept_type_descriptions(self, schema):
        """It should include descriptions for concept types."""
        prompt = build_concept_prompt(schema)
        # Check a known description fragment is present
        assert "manifold" in prompt or "domain" in prompt or "sets" in prompt.lower()


class TestBuildClaimPrompt:
    """Tests for build_claim_prompt."""

    def test_it_should_contain_all_six_claim_types(self, schema):
        """It should generate a claim extraction prompt containing all 6 claim types."""
        prompt = build_claim_prompt(schema)
        for claim_type in ALL_CLAIM_TYPES:
            assert claim_type in prompt, f"Missing claim type: {claim_type}"

    def test_it_should_instruct_json_output_with_claims_key(self, schema):
        """It should instruct the LLM to output JSON with a 'claims' key."""
        prompt = build_claim_prompt(schema)
        assert "claims" in prompt

    def test_it_should_inject_concept_list_when_provided(self, schema):
        """It should inject concept names/slugs/types into prompt when concept_list provided."""
        concepts = [
            {"name": "Bellman operator", "slug": "bellman-operator", "type": "operator"},
            {"name": "policy space", "slug": "policy-space", "type": "space"},
        ]
        prompt = build_claim_prompt(schema, concept_list=concepts)
        assert "Bellman operator" in prompt
        assert "policy-space" in prompt
        assert "policy space" in prompt

    def test_it_should_not_include_concept_list_when_not_provided(self, schema):
        """It should not include concept grounding section when concept_list is None."""
        prompt_without = build_claim_prompt(schema, concept_list=None)
        prompt_with = build_claim_prompt(schema, concept_list=[
            {"name": "Markov chain", "slug": "markov-chain", "type": "structure"},
        ])
        # The prompt with concepts should be longer
        assert len(prompt_with) > len(prompt_without)

    def test_it_should_include_claim_type_descriptions(self, schema):
        """It should include descriptions for each claim type."""
        prompt = build_claim_prompt(schema)
        # Known description fragments from schema
        assert "proven" in prompt.lower() or "proof" in prompt.lower() or "result" in prompt.lower()

    def test_it_should_instruct_to_extract_assertions(self, schema):
        """It should instruct to extract assertions/claims, not objects."""
        prompt = build_claim_prompt(schema)
        lower = prompt.lower()
        assert "assertion" in lower or "claim" in lower or "statement" in lower


class TestBuildEdgeEnrichmentPrompt:
    """Tests for build_edge_enrichment_prompt."""

    def test_it_should_include_claim_edge_types(self, schema):
        """It should include all claim edge types in the edge enrichment prompt."""
        prompt = build_edge_enrichment_prompt(schema)
        claim_edges = schema.edges.claim_edges
        for edge_name in claim_edges:
            assert edge_name in prompt, f"Missing claim edge: {edge_name}"

    def test_it_should_include_coupling_edges(self, schema):
        """It should include coupling edge types (e.g. 'about')."""
        prompt = build_edge_enrichment_prompt(schema)
        coupling_edges = schema.edges.coupling_edges
        for edge_name in coupling_edges:
            assert edge_name in prompt, f"Missing coupling edge: {edge_name}"

    def test_it_should_include_edge_attributes(self, schema):
        """It should list attributes for edges that have them."""
        prompt = build_edge_enrichment_prompt(schema)
        # depends_on has attributes: role, applied_to
        assert "role" in prompt
        assert "applied_to" in prompt

    def test_it_should_instruct_conditional_attribute_extraction(self, schema):
        """It should instruct the LLM to extract edges with conditional attributes."""
        prompt = build_edge_enrichment_prompt(schema)
        lower = prompt.lower()
        assert "edge" in lower or "attribute" in lower


class TestBuildGapFillPrompt:
    """Tests for build_gap_fill_prompt."""

    def test_it_should_return_a_non_empty_prompt(self, schema):
        """It should return a non-empty string prompt."""
        prompt = build_gap_fill_prompt(schema)
        assert isinstance(prompt, str)
        assert len(prompt) > 50

    def test_it_should_instruct_cross_section_dependency_finding(self, schema):
        """It should instruct to find cross-section implicit dependencies."""
        prompt = build_gap_fill_prompt(schema)
        lower = prompt.lower()
        assert "cross" in lower or "section" in lower or "implicit" in lower

    def test_it_should_mention_gap_or_missing(self, schema):
        """It should reference gap-filling or missing connections."""
        prompt = build_gap_fill_prompt(schema)
        lower = prompt.lower()
        assert "gap" in lower or "missing" in lower or "implicit" in lower or "cross" in lower


class TestSchemaReflection:
    """Tests for dynamic schema-reflection behavior."""

    def test_it_should_reflect_added_concept_type_in_concept_prompt(self, minimal_schema):
        """It should include a newly added concept type in the concept prompt."""
        prompt_before = build_concept_prompt(minimal_schema)
        assert "category" not in prompt_before

        minimal_schema.concept_types["category"] = ConceptTypeDef(
            description="A named categorical structure",
            required_fields=["name", "objects", "morphisms"],
            optional_fields=["functors"],
        )

        prompt_after = build_concept_prompt(minimal_schema)
        assert "category" in prompt_after
        assert "morphisms" in prompt_after

    def test_it_should_reflect_added_claim_type_in_claim_prompt(self, minimal_schema):
        """It should include a newly added claim type in the claim prompt."""
        prompt_before = build_claim_prompt(minimal_schema)
        assert "observation" not in prompt_before

        minimal_schema.claim_types["observation"] = ClaimTypeDef(
            description="An informal observed pattern",
            required_fields=["name", "statement"],
            optional_fields=["evidence"],
        )

        prompt_after = build_claim_prompt(minimal_schema)
        assert "observation" in prompt_after
        assert "evidence" in prompt_after

    def test_it_should_reflect_added_edge_in_enrichment_prompt(self, minimal_schema):
        """It should include a newly added edge type in the enrichment prompt."""
        prompt_before = build_edge_enrichment_prompt(minimal_schema)
        assert "refines" not in prompt_before

        minimal_schema.edges.claim_edges["refines"] = EdgeDef(
            description="Source is a tighter version of target",
            attributes=["aspect"],
        )

        prompt_after = build_edge_enrichment_prompt(minimal_schema)
        assert "refines" in prompt_after
        assert "aspect" in prompt_after
