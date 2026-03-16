"""
@file test_claim_verifier.py
@description Tests for the Pass 4 claim verification and auto-fix logic.
"""

import json
from unittest.mock import AsyncMock, MagicMock

import pytest

from graph_builder.extraction.claim_verifier import (
    verify_section_claims,
    apply_corrections,
    apply_flags,
    build_missing_claims,
)
from graph_builder.llm.llm_client import LLMResponse
from graph_builder.models.claim import ClaimNode
from graph_builder.models.edges import CouplingEdge


def _make_claim(
    slug: str = "paper--theorem-1",
    label: str = "Theorem 1",
    claim_type: str = "theorem",
    statement: str = "The bound holds.",
) -> ClaimNode:
    """Build a minimal ClaimNode for testing."""
    return ClaimNode(
        slug=slug, source_paper_slug="paper",
        label=label, claim_type=claim_type, statement=statement,
    )


def _make_mock_client(response_data: dict) -> MagicMock:
    """Return a mock LLM client returning the given verification JSON."""
    client = MagicMock()
    client.call = AsyncMock(return_value=LLMResponse(
        content=json.dumps(response_data),
        input_tokens=100, output_tokens=50, model="claude-opus-4-6",
    ))
    return client


class TestApplyCorrections:
    """Tests for apply_corrections()."""

    def test_it_should_update_statement_field(self):
        """It should overwrite a claim's statement when corrected."""
        claim = _make_claim()
        corrections = [{"claim_slug": "paper--theorem-1", "field": "statement",
                        "issue": "paraphrased", "corrected_value": "The exact bound is 2."}]
        apply_corrections([claim], corrections)
        assert claim.statement == "The exact bound is 2."

    def test_it_should_reject_label_corrections(self):
        """It should skip corrections that target the label field."""
        claim = _make_claim(label="Theorem 1")
        corrections = [{"claim_slug": "paper--theorem-1", "field": "label",
                        "issue": "wrong label", "corrected_value": "Theorem 2"}]
        apply_corrections([claim], corrections)
        assert claim.label == "Theorem 1"

    def test_it_should_skip_unknown_slugs(self):
        """It should silently skip corrections for non-existent claims."""
        claim = _make_claim()
        corrections = [{"claim_slug": "paper--nonexistent", "field": "statement",
                        "issue": "wrong", "corrected_value": "new value"}]
        apply_corrections([claim], corrections)
        assert claim.statement == "The bound holds."


class TestApplyFlags:
    """Tests for apply_flags()."""

    def test_it_should_set_review_needed_for_low_confidence(self):
        """It should set status to review_needed when confidence < 0.7."""
        claim = _make_claim()
        flags = [{"claim_slug": "paper--theorem-1", "issue": "proof truncated", "confidence": 0.4}]
        apply_flags([claim], flags)
        assert claim.status == "review_needed"

    def test_it_should_not_flag_high_confidence(self):
        """It should not modify status when confidence >= 0.7."""
        claim = _make_claim()
        flags = [{"claim_slug": "paper--theorem-1", "issue": "minor", "confidence": 0.8}]
        apply_flags([claim], flags)
        assert claim.status == "unverified"


class TestBuildMissingClaims:
    """Tests for build_missing_claims()."""

    def test_it_should_create_claim_nodes_from_missing_entries(self):
        """It should construct ClaimNodes from missing_claims data."""
        missing = [{"label": "Lemma 3", "claim_type": "lemma",
                     "statement": "The auxiliary bound holds.", "about_concepts": ["regret"]}]
        claims, edges = build_missing_claims(missing, "paper", "Section III")
        assert len(claims) == 1
        assert claims[0].label == "Lemma 3"
        assert claims[0].source_paper_slug == "paper"
        assert claims[0].section == "Section III"
        assert len(edges) == 1
        assert edges[0].concept_slug == "regret"

    def test_it_should_skip_entries_without_label(self):
        """It should skip missing entries that have no label."""
        missing = [{"label": "", "claim_type": "lemma", "statement": "Something."}]
        claims, edges = build_missing_claims(missing, "paper", "Section I")
        assert claims == []
        assert edges == []

    def test_it_should_create_multiple_coupling_edges(self):
        """It should create one coupling edge per about_concepts entry."""
        missing = [{"label": "Theorem 5", "claim_type": "theorem",
                     "statement": "Result.", "about_concepts": ["regret", "loss"]}]
        claims, edges = build_missing_claims(missing, "paper", "Section II")
        assert len(claims) == 1
        assert len(edges) == 2
        concept_slugs = {e.concept_slug for e in edges}
        assert concept_slugs == {"regret", "loss"}


class TestVerifySectionClaims:
    """Tests for verify_section_claims()."""

    @pytest.mark.asyncio
    async def test_it_should_return_empty_results_on_no_issues(self):
        """It should return empty lists when verification finds no problems."""
        client = _make_mock_client({"missing_claims": [], "corrections": [], "flags": []})
        claims = [_make_claim()]
        new_claims, new_edges = await verify_section_claims(
            "section text", {}, claims, None, client, "paper", "Section I",
        )
        assert new_claims == []
        assert new_edges == []

    @pytest.mark.asyncio
    async def test_it_should_apply_corrections_in_place(self):
        """It should mutate existing claims based on corrections."""
        client = _make_mock_client({
            "missing_claims": [],
            "corrections": [{"claim_slug": "paper--theorem-1", "field": "proof_technique",
                             "issue": "missing", "corrected_value": "induction"}],
            "flags": [],
        })
        claims = [_make_claim()]
        await verify_section_claims("section text", {}, claims, None, client, "paper", "Section I")
        assert claims[0].proof_technique == "induction"

    @pytest.mark.asyncio
    async def test_it_should_handle_llm_failure_gracefully(self):
        """It should return empty results when the LLM call fails."""
        client = MagicMock()
        client.call = AsyncMock(side_effect=RuntimeError("LLM down"))
        claims = [_make_claim()]
        new_claims, new_edges = await verify_section_claims(
            "section text", {}, claims, None, client, "paper", "Section I",
        )
        assert new_claims == []
        assert new_edges == []

    @pytest.mark.asyncio
    async def test_it_should_return_empty_when_no_claims(self):
        """It should return empty results when claims list is empty."""
        client = _make_mock_client({"missing_claims": [], "corrections": [], "flags": []})
        new_claims, new_edges = await verify_section_claims(
            "section text", {}, [], None, client, "paper", "Section I",
        )
        assert new_claims == []
        assert new_edges == []
        # LLM should not be called when there are no claims
        client.call.assert_not_called()

    @pytest.mark.asyncio
    async def test_it_should_handle_invalid_json_response(self):
        """It should return empty results when LLM returns invalid JSON."""
        client = MagicMock()
        client.call = AsyncMock(return_value=LLMResponse(
            content="not valid json {{{",
            input_tokens=100, output_tokens=50, model="claude-opus-4-6",
        ))
        claims = [_make_claim()]
        new_claims, new_edges = await verify_section_claims(
            "section text", {}, claims, None, client, "paper", "Section I",
        )
        assert new_claims == []
        assert new_edges == []
