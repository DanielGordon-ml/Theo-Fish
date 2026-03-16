"""
@file test_e2e_smoke.py
@description End-to-end smoke test for the full dual-graph pipeline.

Exercises the complete flow — paper loading, section splitting (real),
concept extraction (mocked LLM), claim extraction (mocked LLM), edge
enrichment (mocked LLM), validation (real), Neo4j write (mocked),
vault export (real filesystem), and sync-back (real filesystem + mocked
Neo4j).  All tests are unit-level: no live services required.
"""

import json
import os
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
import yaml

from graph_builder.config.schema_types import (
    ClaimTypeDef,
    ConceptTypeDef,
    EdgeCategories,
    FieldOwnership,
    GraphSchema,
    ValidationConfig,
    ValidationSeverity,
)
from graph_builder.llm.llm_client import LLMResponse
from graph_builder.models.claim import ClaimNode
from graph_builder.models.concept import ConceptNode
from graph_builder.models.edges import (
    ClaimEdge,
    ConceptEdge,
    CouplingEdge,
    SourcedFromEdge,
)
from graph_builder.models.provenance import ProvenanceNode
from graph_builder.models.source import SourceNode
from graph_builder.orchestrator.orchestrator import PipelineOptions, process_paper
from graph_builder.vault.obsidian_exporter import export_vault
from graph_builder.vault.sync_back import sync_back

pytestmark = [pytest.mark.asyncio, pytest.mark.e2e]

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_ARXIV_ID = "2301.00001"
_PAPER_TITLE = "Spectral Theory of Compact Operators"
_PAPER_SLUG = "spectral-theory-of-compact-operators"
_SANITIZED_ID = "2301-00001"

_CONCEPT_JSON = json.dumps({
    "concepts": [
        {
            "name": "Compact Operator",
            "semantic_type": "operator",
            "canonical_definition": "A bounded linear map sending bounded sets to precompact sets.",
            "formal_spec": "T: X -> X, T(B) relatively compact",
            "aliases": ["compact linear map"],
        }
    ]
})

_CLAIM_JSON = json.dumps({
    "claims": [
        {
            "label": "Theorem 1",
            "claim_type": "theorem",
            "statement": "Every compact operator on a Hilbert space has a spectral decomposition.",
            "conclusion": "Spectral decomposition exists.",
            "strength": "proved",
            "status": "unverified",
        }
    ]
})

_EDGE_JSON = json.dumps({
    "claim_edges": [],
    "coupling_edges": [
        {
            "claim_slug": f"{_PAPER_SLUG}--theorem-1",
            "concept_slug": "compact-operator",
            "role": "primary",
            "aspect": "",
        }
    ],
})

_CROSS_SECTION_JSON = json.dumps({
    "edges": []
})


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


def _build_minimal_schema() -> GraphSchema:
    """Construct a minimal GraphSchema sufficient for smoke testing."""
    return GraphSchema(
        version="1.0",
        last_updated="2026-03-16",
        concept_types={
            "operator": ConceptTypeDef(
                description="A linear map between spaces.",
                required_fields=["name", "semantic_type"],
            ),
        },
        claim_types={
            "theorem": ClaimTypeDef(
                description="A proven mathematical statement.",
                required_fields=["label", "claim_type"],
                strength_values=["proved", "partial"],
                status_values=["unverified", "verified"],
            ),
        },
        edges=EdgeCategories(),
        validation=ValidationConfig(
            rules=[],
            severity=ValidationSeverity(),
        ),
        field_ownership=FieldOwnership(
            pipeline_owned=["semantic_type", "formal_spec"],
            human_owned=["name", "canonical_definition", "human_notes"],
            shared=["aliases", "status"],
        ),
    )


def _make_llm_response(content: str) -> LLMResponse:
    """Wrap a JSON string in an LLMResponse."""
    return LLMResponse(
        content=content,
        input_tokens=10,
        output_tokens=10,
        model="deepseek-chat",
    )


def _build_mock_llm(
    concept_json: str = _CONCEPT_JSON,
    claim_json: str = _CLAIM_JSON,
    edge_json: str = _EDGE_JSON,
    cross_json: str = _CROSS_SECTION_JSON,
) -> MagicMock:
    """Build a mock LLM client that routes responses by system prompt keyword.

    Uses the distinctive opening line of each pass's system prompt so the
    routing is stable regardless of how many sections the paper has.

    Routing table (first-match):
      "concept extractor"  -> concept_json
      "claim extractor"    -> claim_json
      "relationship extractor" -> edge_json
      "gap-fill extractor" -> cross_json
    """
    async def _call(system_prompt: str, user_prompt: str) -> LLMResponse:
        prompt_lower = system_prompt.lower()
        if "concept extractor" in prompt_lower:
            return _make_llm_response(concept_json)
        if "claim extractor" in prompt_lower:
            return _make_llm_response(claim_json)
        if "relationship extractor" in prompt_lower:
            return _make_llm_response(edge_json)
        # gap-fill / cross-section pass
        return _make_llm_response(cross_json)

    llm = MagicMock()
    llm.call = AsyncMock(side_effect=_call)
    return llm


def _build_mock_neo4j() -> MagicMock:
    """Build a mock Neo4jClient that accepts all write/read calls."""
    client = MagicMock()
    client.execute_write = AsyncMock(return_value=[])
    client.execute_write_tx = AsyncMock(return_value=None)

    async def _read(query: str, **kwargs):
        # is_paper_built check → return count 0 so pipeline doesn't skip.
        if "count" in query.lower():
            return [{"count": 0}]
        # get_all_concept_slugs → empty (no existing concepts)
        if "Concept" in query and "slug" in query:
            return []
        return []

    client.execute_read = AsyncMock(side_effect=_read)
    return client


def _build_mock_graph_reader(
    concepts: list[ConceptNode] | None = None,
    claims: list[ClaimNode] | None = None,
    sources: list[SourceNode] | None = None,
    provenances: list[ProvenanceNode] | None = None,
) -> MagicMock:
    """Build a mock GraphReader for export_vault calls."""
    reader = MagicMock()
    reader.get_all_concepts = AsyncMock(return_value=concepts or [])
    reader.get_all_claims = AsyncMock(return_value=claims or [])
    reader.get_all_sources = AsyncMock(return_value=sources or [])
    reader.get_all_concept_edges = AsyncMock(return_value=[])
    reader.get_all_claim_edges = AsyncMock(return_value=[])
    reader.get_all_coupling_edges = AsyncMock(return_value=[])
    reader.get_all_sourced_from_edges = AsyncMock(return_value=[])
    reader.get_all_provenances = AsyncMock(return_value=provenances or [])
    return reader


def _write_cleaned_paper(directory: Path, arxiv_id: str, title: str) -> Path:
    """Write a minimal cleaned paper JSON to the given directory."""
    paper = {
        "title": title,
        "extracted_text_markdown": (
            "# Introduction\n\n"
            "Compact operators appear throughout functional analysis. "
            "They play a central role in spectral theory and arise naturally "
            "in the study of integral equations on Hilbert spaces.  "
            "Their spectral properties are well understood.\n\n"
            "# Spectral Theorem\n\n"
            "Every compact self-adjoint operator admits an orthonormal basis "
            "of eigenvectors with eigenvalues converging to zero. "
            "This is the cornerstone result that links compact operators to "
            "the classical finite-dimensional spectral theory."
        ),
    }
    path = directory / f"{arxiv_id}.json"
    path.write_text(json.dumps(paper), encoding="utf-8")
    return path


# ---------------------------------------------------------------------------
# Test class
# ---------------------------------------------------------------------------


class TestE2ESmoke:
    """Full pipeline smoke test — extraction, Neo4j write, export, sync-back."""

    async def test_full_pipeline_flow(self, tmp_path: Path) -> None:
        """It should run the full pipeline: load → extract → write → export → sync-back."""
        # 1. Create cleaned paper JSON that load_paper can read.
        cleaned_dir = tmp_path / "cleaned"
        cleaned_dir.mkdir()
        _write_cleaned_paper(cleaned_dir, _ARXIV_ID, _PAPER_TITLE)

        schema = _build_minimal_schema()
        options = PipelineOptions(schema=schema, concurrency=1, force=True)
        mock_llm = _build_mock_llm()
        mock_neo4j = _build_mock_neo4j()

        # 2-6. Patch CLEANED_DIR and run process_paper.
        with patch(
            "graph_builder.orchestrator.pipeline_loader.CLEANED_DIR",
            cleaned_dir,
        ):
            result = await process_paper(
                arxiv_id=_ARXIV_ID,
                options=options,
                llm_client=mock_llm,
                neo4j_client=mock_neo4j,
            )

        # 5. Verify BuildResult has the expected shape.
        assert result.status == "built", f"Expected 'built', got: {result.status!r} ({result.error})"
        assert result.arxiv_id == _ARXIV_ID
        assert result.concept_count >= 1
        assert result.claim_count >= 1

        # 6-7. Export vault to tmp_path using mock graph reader.
        vault_dir = tmp_path / "vault"
        vault_dir.mkdir()

        concept = ConceptNode(
            name="Compact Operator",
            semantic_type="operator",
            canonical_definition="A bounded linear map.",
        )
        claim = ClaimNode(
            source_paper_slug=_SANITIZED_ID,
            label="Theorem 1",
            claim_type="theorem",
            statement="Every compact operator has a spectral decomposition.",
        )
        source = SourceNode(arxiv_id=_ARXIV_ID, title=_PAPER_TITLE)
        prov = ProvenanceNode(
            concept_slug=concept.slug,
            source_arxiv_id=_ARXIV_ID,
            formulation="T: X -> X compact",
        )

        reader = _build_mock_graph_reader(
            concepts=[concept],
            claims=[claim],
            sources=[source],
            provenances=[prov],
        )
        mock_neo4j_for_export = MagicMock()

        manifest = await export_vault(vault_dir, reader, mock_neo4j_for_export)

        # 7. Verify vault files exist in correct structure.
        assert (vault_dir / "concepts").is_dir()
        assert (vault_dir / "claims").is_dir()
        assert (vault_dir / "sources").is_dir()
        assert (vault_dir / "_meta").is_dir()
        assert (vault_dir / "concepts" / f"{concept.slug}.md").exists()
        assert (vault_dir / "sources" / f"{_ARXIV_ID}.md").exists()
        assert manifest["concepts"] == 1
        assert manifest["claims"] == 1
        assert manifest["sources"] == 1

        # 8. Edit a human-owned field in a concept vault file.
        concept_file = vault_dir / "concepts" / f"{concept.slug}.md"
        content = concept_file.read_text(encoding="utf-8")
        # Replace empty human_notes with a human annotation.
        updated = content.replace("human_notes: ''", "human_notes: 'Reviewed by hand.'")
        updated = updated.replace('human_notes: ""', 'human_notes: "Reviewed by hand."')
        concept_file.write_text(updated, encoding="utf-8")

        # 9. Call sync_back with a mocked Neo4j client.
        async def _sync_read(query: str, **kwargs):
            if "Concept" in query:
                return [{"props": {
                    "slug": concept.slug,
                    "name": concept.name,
                    "canonical_definition": concept.canonical_definition,
                    "human_notes": "",
                    "aliases": [],
                    "status": "canonical",
                    "semantic_type": "operator",
                    "formal_spec": "",
                    "rhetorical_origin": "",
                    "components": [],
                    "ts_domain": "",
                    "ts_codomain": "",
                    "ts_applies_to": "",
                    "ts_member_type": "",
                    "ts_objective": "",
                    "embedding": [],
                }}]
            return []

        sync_client = MagicMock()
        sync_client.execute_read = AsyncMock(side_effect=_sync_read)
        sync_client.execute_write = AsyncMock(return_value=[])

        changes = await sync_back(vault_dir, sync_client)

        # 10. Verify the sync detected the human_notes edit.
        human_notes_change = next(
            (c for c in changes if c.field == "human_notes"), None
        )
        assert human_notes_change is not None, (
            f"Expected a human_notes SyncChange; got fields: {[c.field for c in changes]}"
        )
        assert human_notes_change.new_value == "Reviewed by hand."
        assert human_notes_change.slug == concept.slug

    async def test_export_creates_correct_structure(self, tmp_path: Path) -> None:
        """It should create concepts/, claims/, sources/, _meta/ directories."""
        vault_dir = tmp_path / "vault"
        vault_dir.mkdir()

        concept = ConceptNode(
            name="Hilbert Space",
            semantic_type="operator",
        )
        claim = ClaimNode(
            source_paper_slug="test-paper",
            label="Lemma 2",
            claim_type="theorem",
        )
        source = SourceNode(arxiv_id="1234.56789", title="Test Paper")

        reader = _build_mock_graph_reader(
            concepts=[concept],
            claims=[claim],
            sources=[source],
        )
        mock_neo4j = MagicMock()

        manifest = await export_vault(vault_dir, reader, mock_neo4j)

        assert (vault_dir / "concepts").is_dir()
        assert (vault_dir / "claims").is_dir()
        assert (vault_dir / "sources").is_dir()
        assert (vault_dir / "_meta").is_dir()
        assert (vault_dir / "_meta" / "export-manifest.json").exists()
        assert manifest["concepts"] == 1
        assert manifest["claims"] == 1
        assert manifest["sources"] == 1

    async def test_human_edit_survives_reexport(self, tmp_path: Path) -> None:
        """It should preserve human edits through export → edit → re-export cycle."""
        vault_dir = tmp_path / "vault"
        vault_dir.mkdir()

        concept = ConceptNode(
            name="Banach Space",
            semantic_type="operator",
            canonical_definition="A complete normed vector space.",
        )
        source = SourceNode(arxiv_id="9999.00001", title="Functional Analysis")

        reader = _build_mock_graph_reader(concepts=[concept], sources=[source])
        mock_neo4j = MagicMock()

        # First export.
        await export_vault(vault_dir, reader, mock_neo4j)

        concept_file = vault_dir / "concepts" / f"{concept.slug}.md"
        assert concept_file.exists()

        # Human edits human_notes.
        content = concept_file.read_text(encoding="utf-8")
        content = content.replace("human_notes: ''", "human_notes: 'My curated note.'")
        content = content.replace('human_notes: ""', 'human_notes: "My curated note."')
        concept_file.write_text(content, encoding="utf-8")

        # Re-export — same reader, same concept.
        await export_vault(vault_dir, reader, mock_neo4j)

        re_exported = concept_file.read_text(encoding="utf-8")
        assert "My curated note." in re_exported, (
            "human_notes edit was lost during re-export"
        )
