"""
@file test_round_trip_invariance.py
@description Round-trip invariance: export → sync-back with no edits = zero diff.

Validates that the exporter writes fields in a format that sync-back reads
correctly, and that sync-back correctly classifies all pipeline-owned fields
as unchanged.  A second test confirms that a genuine human edit IS detected.
"""

import os
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock

import pytest
import yaml

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
from graph_builder.vault.manifest import write_manifest
from graph_builder.vault.obsidian_exporter import export_vault
from graph_builder.vault.sync_back import SyncChange, sync_back

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_ARXIV_ID = "2101.00001"
_PAPER_SLUG = "2101-00001"

# A timestamp far in the past so all exported files are treated as "new" by
# the manifest cutoff gate inside sync-back.
_PAST_TS = datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc).isoformat()


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture()
def concept() -> ConceptNode:
    """A canonical concept node with all syncable fields populated."""
    return ConceptNode(
        name="Hilbert Space",
        semantic_type="mathematical_object",
        canonical_definition="A complete inner product space.",
        aliases=["H-space"],
        status="canonical",
        human_notes="",
    )


@pytest.fixture()
def claim(concept: ConceptNode) -> ClaimNode:
    """A theorem claim linked to the concept fixture."""
    return ClaimNode(
        source_paper_slug=_PAPER_SLUG,
        label="Theorem 2.1",
        claim_type="theorem",
        statement="Every Hilbert space has an orthonormal basis.",
        status="unverified",
        human_notes="",
    )


@pytest.fixture()
def source() -> SourceNode:
    """A source node for the fixture paper."""
    return SourceNode(
        arxiv_id=_ARXIV_ID,
        title="Functional Analysis Primer",
        authors=["Conway, J."],
        date_published="2021-01-01",
    )


@pytest.fixture()
def provenance(concept: ConceptNode) -> ProvenanceNode:
    """A provenance record linking the concept to the source paper."""
    return ProvenanceNode(
        concept_slug=concept.slug,
        source_arxiv_id=_ARXIV_ID,
        formulation="A separable complete inner product space.",
        section="Section 1",
        extraction_confidence=0.9,
    )


# ---------------------------------------------------------------------------
# Helper factories
# ---------------------------------------------------------------------------


def _make_reader(
    concepts: list[ConceptNode],
    claims: list[ClaimNode],
    sources: list[SourceNode],
    provenances: list[ProvenanceNode] | None = None,
    concept_edges: list[ConceptEdge] | None = None,
    claim_edges: list[ClaimEdge] | None = None,
    coupling_edges: list[CouplingEdge] | None = None,
    sourced_from: list[SourcedFromEdge] | None = None,
) -> MagicMock:
    """Build a mock GraphReader returning the provided fixture data."""
    reader = MagicMock()
    reader.get_all_concepts = AsyncMock(return_value=concepts)
    reader.get_all_claims = AsyncMock(return_value=claims)
    reader.get_all_sources = AsyncMock(return_value=sources)
    reader.get_all_concept_edges = AsyncMock(return_value=concept_edges or [])
    reader.get_all_claim_edges = AsyncMock(return_value=claim_edges or [])
    reader.get_all_coupling_edges = AsyncMock(return_value=coupling_edges or [])
    reader.get_all_sourced_from_edges = AsyncMock(return_value=sourced_from or [])
    reader.get_all_provenances = AsyncMock(return_value=provenances or [])
    return reader


def _make_neo4j_client() -> MagicMock:
    """Return a no-op mock Neo4jClient."""
    return MagicMock()


def _neo4j_concept_props(concept: ConceptNode) -> dict:
    """Build a Neo4j-style props dict mirroring the exported concept fields.

    Only includes fields that sync-back compares: human-owned and shared
    scalars (name, canonical_definition, human_notes, status, aliases).
    """
    return {
        "slug": concept.slug,
        "name": concept.name,
        "canonical_definition": concept.canonical_definition,
        "human_notes": concept.human_notes,
        "aliases": list(concept.aliases),
        "status": concept.status,
    }


def _neo4j_claim_props(claim: ClaimNode) -> dict:
    """Build a Neo4j-style props dict mirroring the exported claim fields.

    Only includes fields that sync-back compares: human-owned (status,
    human_notes).
    """
    return {
        "slug": claim.slug,
        "status": claim.status,
        "human_notes": claim.human_notes,
    }


def _make_sync_client(
    concept: ConceptNode,
    claim: ClaimNode,
) -> MagicMock:
    """Build a mock Neo4jClient whose execute_read returns original Neo4j props.

    The returned props exactly mirror the node state before any human edit,
    allowing sync-back to detect real differences.
    """
    client = MagicMock()
    concept_row = {"props": _neo4j_concept_props(concept)}
    claim_row = {"props": _neo4j_claim_props(claim)}

    async def _execute_read(query: str, **kwargs):
        if "Concept" in query:
            return [concept_row]
        if "Claim" in query:
            return [claim_row]
        return []

    client.execute_read = AsyncMock(side_effect=_execute_read)
    client.execute_write = AsyncMock(return_value=[])
    return client


def _stamp_files_as_new(vault_dir: Path, exported_at_ts: str) -> None:
    """Set mtime of all vault .md files to 1 second after the manifest ts.

    This ensures the sync-back timestamp gate processes them even if the OS
    wrote the files at or before the manifest's exported_at.

    @param vault_dir Root vault directory.
    @param exported_at_ts ISO-8601 string from the manifest.
    """
    cutoff_dt = datetime.fromisoformat(exported_at_ts)
    if cutoff_dt.tzinfo is None:
        cutoff_dt = cutoff_dt.replace(tzinfo=timezone.utc)
    future_mtime = cutoff_dt.timestamp() + 1.0

    for md_file in vault_dir.rglob("*.md"):
        os.utime(md_file, (future_mtime, future_mtime))


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
class TestRoundTripInvariance:
    """Validates export and sync-back are true inverses for pipeline/shared fields."""

    async def test_no_edits_produces_zero_changes(
        self,
        tmp_path: Path,
        concept: ConceptNode,
        claim: ClaimNode,
        source: SourceNode,
        provenance: ProvenanceNode,
    ) -> None:
        """It should produce zero changes when syncing back an unedited export.

        Exports a concept and a claim to a tmp vault, then immediately runs
        sync-back with a mock client whose Neo4j state matches the original
        nodes.  No changes should be detected because the vault files are
        identical to the Neo4j state.
        """
        vault_dir = tmp_path / "vault"
        reader = _make_reader(
            [concept], [claim], [source], provenances=[provenance]
        )
        export_client = _make_neo4j_client()

        manifest = await export_vault(vault_dir, reader, export_client)

        # Overwrite manifest with a past timestamp so the timestamp gate
        # does not skip the freshly exported files.
        write_manifest(vault_dir, {**manifest, "exported_at": _PAST_TS})

        sync_client = _make_sync_client(concept, claim)
        changes = await sync_back(vault_dir, sync_client, dry_run=True)

        assert changes == [], (
            f"Expected zero changes on unedited export but got: {changes}"
        )

    async def test_human_edit_detected_on_sync_back(
        self,
        tmp_path: Path,
        concept: ConceptNode,
        claim: ClaimNode,
        source: SourceNode,
        provenance: ProvenanceNode,
    ) -> None:
        """It should detect a human edit after export and produce exactly one SyncChange.

        Exports to vault, manually rewrites the human_notes field in the
        concept file, then runs sync-back.  Exactly one SyncChange for the
        human_notes field must be returned.
        """
        vault_dir = tmp_path / "vault"
        reader = _make_reader(
            [concept], [claim], [source], provenances=[provenance]
        )
        export_client = _make_neo4j_client()

        manifest = await export_vault(vault_dir, reader, export_client)

        # Simulate a human edit: change human_notes in the concept file.
        concept_file = vault_dir / "concepts" / f"{concept.slug}.md"
        _inject_human_notes(concept_file, "My important annotation.")

        # Overwrite manifest with past ts so the modified file passes the gate.
        write_manifest(vault_dir, {**manifest, "exported_at": _PAST_TS})

        sync_client = _make_sync_client(concept, claim)
        changes = await sync_back(vault_dir, sync_client, dry_run=True)

        human_notes_changes = [c for c in changes if c.field == "human_notes"]
        assert len(human_notes_changes) == 1, (
            f"Expected exactly one human_notes change; got {changes}"
        )
        change = human_notes_changes[0]
        assert change.node_type == "concept"
        assert change.slug == concept.slug
        assert change.old_value == ""
        assert change.new_value == "My important annotation."


# ---------------------------------------------------------------------------
# File-editing helper
# ---------------------------------------------------------------------------


def _inject_human_notes(path: Path, value: str) -> None:
    """Rewrite the human_notes field in a vault markdown file's frontmatter.

    Reads the existing file, parses its YAML frontmatter, sets human_notes,
    and rewrites the file so the change is visible to sync-back.

    @param path Path to the .md file to modify.
    @param value New value for the human_notes field.
    """
    content = path.read_text(encoding="utf-8")
    parts = content.split("---", 2)
    if len(parts) < 3:
        raise ValueError(f"No frontmatter found in {path}")

    fm = yaml.safe_load(parts[1]) or {}
    fm["human_notes"] = value
    new_fm = yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)
    path.write_text(f"---\n{new_fm}---\n{parts[2]}", encoding="utf-8")
