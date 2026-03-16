"""
@file test_sync_back.py
@description Tests for sync_back — syncs human-owned fields from Obsidian vault
back to Neo4j. Only human-owned and shared fields are ever written; pipeline-owned
fields are ignored regardless of what appears in the vault file.
"""

import os
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock

import pytest
import yaml

from graph_builder.vault.manifest import write_manifest
from graph_builder.vault.sync_back import SyncChange, sync_back

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_EXPORT_TS = datetime(2026, 1, 1, 12, 0, 0, tzinfo=timezone.utc).isoformat()

_CONCEPT_PIPELINE_FIELDS = {
    "semantic_type": "space",
    "formal_spec": "(V, ||·||)",
    "rhetorical_origin": "",
    "components": [],
    "ts_domain": "",
    "ts_codomain": "",
    "ts_applies_to": "",
    "ts_member_type": "",
    "ts_objective": "",
    "embedding": [],
}

_CLAIM_PIPELINE_FIELDS = {
    "assumptions": [],
    "conclusion": "",
    "proof_technique": "",
    "strength": "",
    "statement": "",
    "proof": "",
    "section": "",
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _write_manifest(vault_dir: Path, exported_at: str) -> None:
    """Write a minimal export manifest via write_manifest()."""
    vault_dir.mkdir(parents=True, exist_ok=True)
    write_manifest(vault_dir, {"exported_at": exported_at})


def _write_concept_file(
    vault_dir: Path,
    slug: str,
    frontmatter: dict,
    mtime: float | None = None,
) -> Path:
    """Write a concept vault file with YAML frontmatter."""
    concepts_dir = vault_dir / "concepts"
    concepts_dir.mkdir(parents=True, exist_ok=True)
    path = concepts_dir / f"{slug}.md"
    path.write_text(f"---\n{yaml.dump(frontmatter)}---\n\n# {slug}\n", encoding="utf-8")
    if mtime is not None:
        os.utime(path, (mtime, mtime))
    return path


def _write_claim_file(
    vault_dir: Path,
    slug: str,
    frontmatter: dict,
    mtime: float | None = None,
) -> Path:
    """Write a claim vault file with YAML frontmatter."""
    claims_dir = vault_dir / "claims"
    claims_dir.mkdir(parents=True, exist_ok=True)
    path = claims_dir / f"{slug}.md"
    path.write_text(f"---\n{yaml.dump(frontmatter)}---\n\n# {slug}\n", encoding="utf-8")
    if mtime is not None:
        os.utime(path, (mtime, mtime))
    return path


def _concept_neo4j_row(slug: str, **overrides) -> dict:
    """Build a minimal Neo4j concept row with sensible defaults."""
    props = {
        "slug": slug,
        "name": slug.replace("-", " ").title(),
        "canonical_definition": "",
        "human_notes": "",
        "aliases": [],
        "status": "canonical",
        **_CONCEPT_PIPELINE_FIELDS,
        **overrides,
    }
    return {"props": props}


def _claim_neo4j_row(slug: str, source_paper_slug: str, **overrides) -> dict:
    """Build a minimal Neo4j claim row with sensible defaults."""
    props = {
        "slug": slug,
        "source_paper_slug": source_paper_slug,
        "label": slug.split("--")[-1].replace("-", " ").title(),
        "name": slug.split("--")[-1].replace("-", " ").title(),
        "claim_type": "lemma",
        "status": "unverified",
        "human_notes": "",
        **_CLAIM_PIPELINE_FIELDS,
        **overrides,
    }
    return {"props": props}


def _make_mock_client(
    concept_rows: list[dict] | None = None,
    claim_rows: list[dict] | None = None,
) -> MagicMock:
    """Build a mock Neo4jClient that returns controlled concept/claim rows."""
    client = MagicMock()
    concept_data = concept_rows or []
    claim_data = claim_rows or []

    async def _execute_read(query: str, **kwargs):
        if "Concept" in query:
            return concept_data
        if "Claim" in query:
            return claim_data
        return []

    client.execute_read = AsyncMock(side_effect=_execute_read)
    client.execute_write = AsyncMock(return_value=[])
    return client


# ---------------------------------------------------------------------------
# Test: human-owned concept fields are synced to Neo4j
# ---------------------------------------------------------------------------


class TestConceptHumanFields:
    """Human-owned concept fields are written back to Neo4j when changed."""

    @pytest.mark.asyncio
    async def test_it_should_read_human_owned_fields_from_concept_file(
        self, tmp_path
    ):
        """sync_back returns SyncChange for each human-owned field that differs."""
        vault_dir = tmp_path / "vault"
        _write_manifest(vault_dir, _EXPORT_TS)
        _write_concept_file(
            vault_dir, "banach-space",
            {
                "slug": "banach-space",
                "name": "Banach Space (corrected)",
                "canonical_definition": "A complete normed vector space.",
                "human_notes": "Key concept for functional analysis.",
                "aliases": ["B-space"],
                "status": "canonical",
                "semantic_type": "space",  # pipeline-owned — must be ignored
            },
        )
        mock_client = _make_mock_client(
            concept_rows=[_concept_neo4j_row("banach-space", name="Banach Space")]
        )

        changes = await sync_back(vault_dir, mock_client)

        field_names = {c.field for c in changes}
        assert "name" in field_names
        assert "canonical_definition" in field_names
        assert "human_notes" in field_names

    @pytest.mark.asyncio
    async def test_it_should_produce_sync_change_with_correct_metadata(
        self, tmp_path
    ):
        """Each SyncChange has correct node_type, slug, old_value, new_value."""
        vault_dir = tmp_path / "vault"
        _write_manifest(vault_dir, _EXPORT_TS)
        _write_concept_file(
            vault_dir, "banach-space",
            {
                "slug": "banach-space",
                "name": "Banach Space",
                "canonical_definition": "",
                "human_notes": "Updated note.",
                "aliases": [],
                "status": "canonical",
            },
        )
        mock_client = _make_mock_client(
            concept_rows=[_concept_neo4j_row("banach-space", name="Banach Space")]
        )

        changes = await sync_back(vault_dir, mock_client)

        change = next((c for c in changes if c.field == "human_notes"), None)
        assert change is not None
        assert change.node_type == "concept"
        assert change.slug == "banach-space"
        assert change.old_value == ""
        assert change.new_value == "Updated note."


# ---------------------------------------------------------------------------
# Test: pipeline-owned concept fields are ignored
# ---------------------------------------------------------------------------


class TestPipelineFieldsIgnored:
    """Pipeline-owned fields in vault files are never written to Neo4j."""

    @pytest.mark.asyncio
    async def test_it_should_ignore_pipeline_owned_fields_in_vault_files(
        self, tmp_path
    ):
        """semantic_type, formal_spec, embedding etc. are not synced back."""
        vault_dir = tmp_path / "vault"
        _write_manifest(vault_dir, _EXPORT_TS)
        _write_concept_file(
            vault_dir, "banach-space",
            {
                "slug": "banach-space",
                "name": "Banach Space",
                "canonical_definition": "",
                "human_notes": "",
                "aliases": [],
                "status": "canonical",
                "semantic_type": "HACKED_VALUE",
                "formal_spec": "HACKED_SPEC",
                "rhetorical_origin": "HACKED",
                "components": ["hacked"],
            },
        )
        mock_client = _make_mock_client(
            concept_rows=[_concept_neo4j_row("banach-space", name="Banach Space")]
        )

        changes = await sync_back(vault_dir, mock_client)

        pipeline_fields = {"semantic_type", "formal_spec", "rhetorical_origin",
                           "components", "embedding"}
        synced_fields = {c.field for c in changes}
        assert synced_fields.isdisjoint(pipeline_fields), (
            f"Pipeline fields were synced: {synced_fields & pipeline_fields}"
        )


# ---------------------------------------------------------------------------
# Test: alias union merge
# ---------------------------------------------------------------------------


class TestAliasUnionMerge:
    """Aliases are union-merged — never subtracted, always combined."""

    @pytest.mark.asyncio
    async def test_it_should_union_merge_aliases(self, tmp_path):
        """Union of Obsidian aliases + Neo4j aliases, never subtracting."""
        vault_dir = tmp_path / "vault"
        _write_manifest(vault_dir, _EXPORT_TS)
        _write_concept_file(
            vault_dir, "banach-space",
            {
                "slug": "banach-space",
                "name": "Banach Space",
                "canonical_definition": "",
                "human_notes": "",
                "aliases": ["B-space", "complete-normed-space"],
                "status": "canonical",
            },
        )
        mock_client = _make_mock_client(
            concept_rows=[_concept_neo4j_row(
                "banach-space",
                name="Banach Space",
                aliases=["B-space", "Banach-space-legacy"],
            )]
        )

        changes = await sync_back(vault_dir, mock_client)

        alias_change = next((c for c in changes if c.field == "aliases"), None)
        assert alias_change is not None
        merged = alias_change.new_value
        assert "B-space" in merged
        assert "complete-normed-space" in merged
        assert "Banach-space-legacy" in merged

    @pytest.mark.asyncio
    async def test_it_should_not_subtract_aliases_absent_from_obsidian(
        self, tmp_path
    ):
        """Neo4j-only aliases are preserved even if absent from vault file."""
        vault_dir = tmp_path / "vault"
        _write_manifest(vault_dir, _EXPORT_TS)
        _write_concept_file(
            vault_dir, "hilbert-space",
            {
                "slug": "hilbert-space",
                "name": "Hilbert Space",
                "canonical_definition": "",
                "human_notes": "",
                "aliases": [],  # Human cleared them in Obsidian
                "status": "canonical",
            },
        )
        mock_client = _make_mock_client(
            concept_rows=[_concept_neo4j_row(
                "hilbert-space",
                name="Hilbert Space",
                aliases=["H-space", "inner-product-space"],
            )]
        )

        changes = await sync_back(vault_dir, mock_client)

        alias_change = next((c for c in changes if c.field == "aliases"), None)
        # Union keeps Neo4j-only aliases; no subtraction allowed
        if alias_change is not None:
            assert "H-space" in alias_change.new_value
            assert "inner-product-space" in alias_change.new_value


# ---------------------------------------------------------------------------
# Test: dry-run mode
# ---------------------------------------------------------------------------


class TestDryRun:
    """In dry-run mode, changes are returned but Neo4j is not written."""

    @pytest.mark.asyncio
    async def test_it_should_support_dry_run_mode(self, tmp_path):
        """dry_run=True returns changes without calling execute_write."""
        vault_dir = tmp_path / "vault"
        _write_manifest(vault_dir, _EXPORT_TS)
        _write_concept_file(
            vault_dir, "banach-space",
            {
                "slug": "banach-space",
                "name": "Banach Space",
                "canonical_definition": "A complete normed space.",
                "human_notes": "New note.",
                "aliases": [],
                "status": "canonical",
            },
        )
        mock_client = _make_mock_client(
            concept_rows=[_concept_neo4j_row("banach-space", name="Banach Space")]
        )

        changes = await sync_back(vault_dir, mock_client, dry_run=True)

        assert len(changes) > 0
        mock_client.execute_write.assert_not_awaited()

    @pytest.mark.asyncio
    async def test_it_should_write_to_neo4j_when_not_dry_run(self, tmp_path):
        """dry_run=False (default) triggers execute_write for changed fields."""
        vault_dir = tmp_path / "vault"
        _write_manifest(vault_dir, _EXPORT_TS)
        _write_concept_file(
            vault_dir, "banach-space",
            {
                "slug": "banach-space",
                "name": "Banach Space",
                "canonical_definition": "A complete normed space.",
                "human_notes": "New note.",
                "aliases": [],
                "status": "canonical",
            },
        )
        mock_client = _make_mock_client(
            concept_rows=[_concept_neo4j_row("banach-space", name="Banach Space")]
        )

        changes = await sync_back(vault_dir, mock_client, dry_run=False)

        assert len(changes) > 0
        mock_client.execute_write.assert_awaited()


# ---------------------------------------------------------------------------
# Test: timestamp filtering
# ---------------------------------------------------------------------------


class TestTimestampFiltering:
    """Only files modified after the last export timestamp are processed."""

    @pytest.mark.asyncio
    async def test_it_should_only_process_files_modified_after_manifest_timestamp(
        self, tmp_path
    ):
        """Files with mtime <= export timestamp are skipped."""
        vault_dir = tmp_path / "vault"
        export_ts = datetime(2026, 3, 1, 12, 0, 0, tzinfo=timezone.utc)
        _write_manifest(vault_dir, export_ts.isoformat())

        old_mtime = export_ts.timestamp() - 3600
        _write_concept_file(
            vault_dir, "old-concept",
            {
                "slug": "old-concept",
                "name": "Old Concept",
                "canonical_definition": "Changed after export.",
                "human_notes": "Changed note.",
                "aliases": [],
                "status": "canonical",
            },
            mtime=old_mtime,
        )
        mock_client = _make_mock_client()

        changes = await sync_back(vault_dir, mock_client)

        assert "old-concept" not in {c.slug for c in changes}

    @pytest.mark.asyncio
    async def test_it_should_process_files_modified_after_manifest_timestamp(
        self, tmp_path
    ):
        """Files with mtime > export timestamp are processed."""
        vault_dir = tmp_path / "vault"
        export_ts = datetime(2026, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
        _write_manifest(vault_dir, export_ts.isoformat())

        new_mtime = export_ts.timestamp() + 3600
        _write_concept_file(
            vault_dir, "new-concept",
            {
                "slug": "new-concept",
                "name": "New Concept (edited)",
                "canonical_definition": "Edited definition.",
                "human_notes": "Edited note.",
                "aliases": [],
                "status": "canonical",
            },
            mtime=new_mtime,
        )
        mock_client = _make_mock_client(
            concept_rows=[_concept_neo4j_row("new-concept", name="New Concept")]
        )

        changes = await sync_back(vault_dir, mock_client)

        assert "new-concept" in {c.slug for c in changes}


# ---------------------------------------------------------------------------
# Test: claim files
# ---------------------------------------------------------------------------


class TestClaimFiles:
    """Claim-specific human-owned fields (status, human_notes) are synced."""

    @pytest.mark.asyncio
    async def test_it_should_read_claim_status_and_human_notes_from_claim_files(
        self, tmp_path
    ):
        """status and human_notes are synced from claim vault files."""
        vault_dir = tmp_path / "vault"
        _write_manifest(vault_dir, _EXPORT_TS)
        claim_slug = "paper-slug--lemma-1"
        _write_claim_file(
            vault_dir, claim_slug,
            {
                "slug": claim_slug,
                "label": "Lemma 1",
                "claim_type": "lemma",
                "status": "verified",
                "human_notes": "Checked against Rudin, page 42.",
                "statement": "For all x in X...",  # pipeline — must be ignored
            },
        )
        mock_client = _make_mock_client(
            claim_rows=[_claim_neo4j_row(claim_slug, "paper-slug")]
        )

        changes = await sync_back(vault_dir, mock_client)

        field_names = {c.field for c in changes}
        assert "status" in field_names
        assert "human_notes" in field_names

        status_change = next(c for c in changes if c.field == "status")
        assert status_change.node_type == "claim"
        assert status_change.slug == claim_slug
        assert status_change.old_value == "unverified"
        assert status_change.new_value == "verified"

    @pytest.mark.asyncio
    async def test_it_should_ignore_pipeline_owned_claim_fields(
        self, tmp_path
    ):
        """statement, proof, strength etc. are never synced from claim files."""
        vault_dir = tmp_path / "vault"
        _write_manifest(vault_dir, _EXPORT_TS)
        claim_slug = "paper-slug--theorem-2"
        _write_claim_file(
            vault_dir, claim_slug,
            {
                "slug": claim_slug,
                "label": "Theorem 2",
                "claim_type": "theorem",
                "status": "unverified",
                "human_notes": "",
                "statement": "HACKED_STATEMENT",
                "proof": "HACKED_PROOF",
                "strength": "HACKED",
                "proof_technique": "HACKED_TECHNIQUE",
            },
        )
        mock_client = _make_mock_client(
            claim_rows=[_claim_neo4j_row(claim_slug, "paper-slug")]
        )

        changes = await sync_back(vault_dir, mock_client)

        pipeline_fields = {"statement", "proof", "strength", "proof_technique"}
        synced_fields = {c.field for c in changes}
        assert synced_fields.isdisjoint(pipeline_fields), (
            f"Pipeline claim fields were synced: {synced_fields & pipeline_fields}"
        )


# ---------------------------------------------------------------------------
# Test: missing manifest
# ---------------------------------------------------------------------------


class TestMissingManifest:
    """When no manifest exists, all files are processed (no timestamp gate)."""

    @pytest.mark.asyncio
    async def test_it_should_handle_missing_manifest_gracefully(
        self, tmp_path
    ):
        """If no manifest file exists, process all vault files."""
        vault_dir = tmp_path / "vault"
        # Deliberately do NOT write a manifest
        _write_concept_file(
            vault_dir, "orphan-concept",
            {
                "slug": "orphan-concept",
                "name": "Orphan Concept",
                "canonical_definition": "Defined without prior export.",
                "human_notes": "Created fresh.",
                "aliases": [],
                "status": "canonical",
            },
        )
        mock_client = _make_mock_client(
            concept_rows=[_concept_neo4j_row("orphan-concept", name="Orphan Concept")]
        )

        changes = await sync_back(vault_dir, mock_client)

        assert "orphan-concept" in {c.slug for c in changes}

    @pytest.mark.asyncio
    async def test_it_should_not_raise_when_vault_dirs_are_empty(
        self, tmp_path
    ):
        """Empty concepts/ and claims/ dirs produce an empty change list."""
        vault_dir = tmp_path / "vault"
        (vault_dir / "concepts").mkdir(parents=True)
        (vault_dir / "claims").mkdir(parents=True)
        mock_client = _make_mock_client()

        changes = await sync_back(vault_dir, mock_client)

        assert changes == []
