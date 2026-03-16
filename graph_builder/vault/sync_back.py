"""
@file sync_back.py
@description Sync human-owned fields from the Obsidian vault back to Neo4j.

Sync-back is MANUAL only — never triggered automatically by the pipeline.
It is invoked via the --sync-back CLI flag.

Field-ownership contract:
  Concepts — human-owned  : name, canonical_definition, human_notes
           — shared       : aliases (union-merge), status
           — pipeline     : IGNORED (semantic_type, formal_spec, embedding, …)
  Claims   — human-owned  : human_notes, status
           — pipeline     : IGNORED (statement, proof, strength, …)

Only files modified after the last export timestamp are processed, unless no
manifest exists in which case all files are processed.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

import yaml

from graph_builder.graph.neo4j_client import Neo4jClient
from graph_builder.vault.manifest import read_manifest

# ---------------------------------------------------------------------------
# Cypher — targeted single-field MERGE updates
# ---------------------------------------------------------------------------

_UPDATE_CONCEPT_CYPHER = """
MATCH (c:Concept {slug: $slug})
SET c[$field] = $value, c.date_modified = datetime()
"""

_UPDATE_CLAIM_CYPHER = """
MATCH (cl:Claim {slug: $slug})
SET cl[$field] = $value, cl.date_modified = datetime()
"""

_GET_CONCEPT_CYPHER = """
MATCH (c:Concept {slug: $slug})
RETURN c {.*} AS props
"""

_GET_CLAIM_CYPHER = """
MATCH (cl:Claim {slug: $slug})
RETURN cl {.*} AS props
"""

# ---------------------------------------------------------------------------
# Field ownership tables
# ---------------------------------------------------------------------------

# Human-owned concept fields: always sync if changed in Obsidian
_CONCEPT_HUMAN_FIELDS = ("name", "canonical_definition", "human_notes")

# Shared concept fields: union-merge (never subtract)
_CONCEPT_SHARED_FIELDS = ("aliases",)

# Shared concept scalar fields: sync like human-owned (last-write wins)
_CONCEPT_SHARED_SCALAR = ("status",)

# Human-owned claim fields
_CLAIM_HUMAN_FIELDS = ("human_notes", "status")


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


@dataclass
class SyncChange:
    """A single field change to sync back to Neo4j."""

    node_type: str  # "concept" or "claim"
    slug: str
    field: str
    old_value: object
    new_value: object


async def sync_back(
    vault_dir: Path,
    neo4j_client: Neo4jClient,
    dry_run: bool = False,
) -> list[SyncChange]:
    """Sync human-owned fields from Obsidian vault back to Neo4j.

    Returns the list of changes made (or that would be made in dry-run).
    Changes are only applied when dry_run is False.

    @param vault_dir Root directory of the Obsidian vault
    @param neo4j_client Connected Neo4jClient for reads and writes
    @param dry_run When True, return changes without writing to Neo4j
    @returns List of SyncChange objects describing each field change
    """
    cutoff = _load_cutoff(vault_dir)
    changes: list[SyncChange] = []

    concept_changes = await _sync_concepts(vault_dir, neo4j_client, cutoff)
    claim_changes = await _sync_claims(vault_dir, neo4j_client, cutoff)
    changes.extend(concept_changes)
    changes.extend(claim_changes)

    if not dry_run:
        await _apply_changes(changes, neo4j_client)

    return changes


# ---------------------------------------------------------------------------
# Internal — manifest timestamp
# ---------------------------------------------------------------------------


def _load_cutoff(vault_dir: Path) -> datetime | None:
    """Return the export cutoff datetime, or None to process all files.

    @param vault_dir Root directory of the Obsidian vault
    @returns UTC-aware datetime from manifest, or None when missing
    """
    manifest = read_manifest(vault_dir)
    if manifest is None:
        return None
    raw = manifest.get("exported_at")
    if not raw:
        return None
    return _parse_ts(raw)


def _parse_ts(raw: str) -> datetime:
    """Parse an ISO-8601 timestamp string into a UTC-aware datetime.

    @param raw ISO timestamp string, with or without timezone info
    @returns UTC-aware datetime
    """
    dt = datetime.fromisoformat(raw)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt


# ---------------------------------------------------------------------------
# Internal — concept sync
# ---------------------------------------------------------------------------


async def _sync_concepts(
    vault_dir: Path,
    client: Neo4jClient,
    cutoff: datetime | None,
) -> list[SyncChange]:
    """Scan concepts/ and return SyncChange list for modified files.

    @param vault_dir Root directory of the Obsidian vault
    @param client Connected Neo4jClient
    @param cutoff Only process files modified after this timestamp (or all)
    @returns List of SyncChange objects for changed concept fields
    """
    concepts_dir = vault_dir / "concepts"
    if not concepts_dir.exists():
        return []

    changes: list[SyncChange] = []
    for path in concepts_dir.glob("*.md"):
        if not _is_modified_after(path, cutoff):
            continue
        fm = _parse_frontmatter(path)
        slug = fm.get("slug") or path.stem
        neo4j_props = await _fetch_concept(client, slug)
        if neo4j_props is None:
            continue
        changes.extend(_diff_concept(slug, fm, neo4j_props))

    return changes


def _diff_concept(
    slug: str,
    fm: dict,
    neo4j: dict,
) -> list[SyncChange]:
    """Compute SyncChange list for a single concept.

    @param slug Concept slug
    @param fm Parsed YAML frontmatter from vault file
    @param neo4j Current Neo4j property dict for this concept
    @returns List of changes for differing human-owned / shared fields
    """
    changes: list[SyncChange] = []

    for field in _CONCEPT_HUMAN_FIELDS:
        change = _diff_scalar(slug, "concept", field, fm, neo4j)
        if change:
            changes.append(change)

    for field in _CONCEPT_SHARED_SCALAR:
        change = _diff_scalar(slug, "concept", field, fm, neo4j)
        if change:
            changes.append(change)

    alias_change = _diff_aliases(slug, fm, neo4j)
    if alias_change:
        changes.append(alias_change)

    return changes


def _diff_scalar(
    slug: str,
    node_type: str,
    field: str,
    fm: dict,
    neo4j: dict,
) -> SyncChange | None:
    """Return a SyncChange if a scalar field value differs.

    @param slug Node slug
    @param node_type "concept" or "claim"
    @param field Field name to compare
    @param fm Vault frontmatter dict
    @param neo4j Neo4j property dict
    @returns SyncChange if different, None otherwise
    """
    vault_val = fm.get(field, "")
    neo4j_val = neo4j.get(field, "")
    if vault_val != neo4j_val:
        return SyncChange(
            node_type=node_type,
            slug=slug,
            field=field,
            old_value=neo4j_val,
            new_value=vault_val,
        )
    return None


def _diff_aliases(
    slug: str,
    fm: dict,
    neo4j: dict,
) -> SyncChange | None:
    """Return a SyncChange if the union of aliases is larger than current Neo4j.

    Union-merge: aliases are never subtracted — only new ones are added.

    @param slug Concept slug
    @param fm Vault frontmatter dict
    @param neo4j Neo4j property dict
    @returns SyncChange if new aliases found, None otherwise
    """
    vault_aliases = set(fm.get("aliases") or [])
    neo4j_aliases = set(neo4j.get("aliases") or [])
    merged = sorted(vault_aliases | neo4j_aliases)
    current = sorted(neo4j_aliases)

    if merged != current:
        return SyncChange(
            node_type="concept",
            slug=slug,
            field="aliases",
            old_value=current,
            new_value=merged,
        )
    return None


async def _fetch_concept(client: Neo4jClient, slug: str) -> dict | None:
    """Fetch a concept's current properties from Neo4j.

    @param client Connected Neo4jClient
    @param slug Concept slug to look up
    @returns Property dict, or None if not found
    """
    rows = await client.execute_read(_GET_CONCEPT_CYPHER, slug=slug)
    if not rows:
        return None
    return rows[0].get("props", rows[0])


# ---------------------------------------------------------------------------
# Internal — claim sync
# ---------------------------------------------------------------------------


async def _sync_claims(
    vault_dir: Path,
    client: Neo4jClient,
    cutoff: datetime | None,
) -> list[SyncChange]:
    """Scan claims/ and return SyncChange list for modified files.

    @param vault_dir Root directory of the Obsidian vault
    @param client Connected Neo4jClient
    @param cutoff Only process files modified after this timestamp (or all)
    @returns List of SyncChange objects for changed claim fields
    """
    claims_dir = vault_dir / "claims"
    if not claims_dir.exists():
        return []

    changes: list[SyncChange] = []
    for path in claims_dir.glob("*.md"):
        if not _is_modified_after(path, cutoff):
            continue
        fm = _parse_frontmatter(path)
        slug = fm.get("slug") or path.stem
        neo4j_props = await _fetch_claim(client, slug)
        if neo4j_props is None:
            continue
        changes.extend(_diff_claim(slug, fm, neo4j_props))

    return changes


def _diff_claim(
    slug: str,
    fm: dict,
    neo4j: dict,
) -> list[SyncChange]:
    """Compute SyncChange list for a single claim.

    @param slug Claim slug
    @param fm Parsed YAML frontmatter from vault file
    @param neo4j Current Neo4j property dict for this claim
    @returns List of changes for differing human-owned fields
    """
    changes: list[SyncChange] = []
    for field in _CLAIM_HUMAN_FIELDS:
        change = _diff_scalar(slug, "claim", field, fm, neo4j)
        if change:
            changes.append(change)
    return changes


async def _fetch_claim(client: Neo4jClient, slug: str) -> dict | None:
    """Fetch a claim's current properties from Neo4j.

    @param client Connected Neo4jClient
    @param slug Claim slug to look up
    @returns Property dict, or None if not found
    """
    rows = await client.execute_read(_GET_CLAIM_CYPHER, slug=slug)
    if not rows:
        return None
    return rows[0].get("props", rows[0])


# ---------------------------------------------------------------------------
# Internal — write changes
# ---------------------------------------------------------------------------


async def _apply_changes(
    changes: list[SyncChange],
    client: Neo4jClient,
) -> None:
    """Write each SyncChange to Neo4j using targeted SET queries.

    @param changes List of SyncChange to apply
    @param client Connected Neo4jClient
    """
    for change in changes:
        cypher = (
            _UPDATE_CONCEPT_CYPHER
            if change.node_type == "concept"
            else _UPDATE_CLAIM_CYPHER
        )
        await client.execute_write(
            cypher,
            slug=change.slug,
            field=change.field,
            value=change.new_value,
        )


# ---------------------------------------------------------------------------
# Internal — file helpers
# ---------------------------------------------------------------------------


def _is_modified_after(path: Path, cutoff: datetime | None) -> bool:
    """Return True if the file's mtime is strictly after the cutoff.

    When cutoff is None, all files are considered modified (no gate).

    @param path File path to check
    @param cutoff UTC-aware datetime to compare mtime against, or None
    @returns True if file should be processed
    """
    if cutoff is None:
        return True
    mtime = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
    return mtime > cutoff


def _parse_frontmatter(path: Path) -> dict:
    """Parse YAML frontmatter from a markdown file.

    Expects the file to start with '---', with frontmatter ending at the
    next '---' line.  Returns empty dict on parse failure.

    @param path Path to the markdown file
    @returns Dict of frontmatter key/value pairs
    """
    content = path.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return {}
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}
    try:
        return yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        return {}
