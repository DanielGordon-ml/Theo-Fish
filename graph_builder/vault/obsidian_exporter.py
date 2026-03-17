"""
@file obsidian_exporter.py
@description Export the full Neo4j knowledge graph to an Obsidian markdown vault.

Writes all concepts, claims, and sources as .md files with YAML frontmatter
and markdown body.  Files are staged in a temporary directory first; each
is moved atomically to its final location to avoid partial writes.

Human-owned frontmatter fields (human_notes, canonical_definition, status,
name) are read from existing files before staging so they survive re-export.
"""

import shutil
from pathlib import Path

import yaml

from graph_builder.graph.graph_reader import GraphReader
from graph_builder.graph.neo4j_client import Neo4jClient
from graph_builder.models.claim import ClaimNode
from graph_builder.models.concept import ConceptNode
from graph_builder.vault.body_renderer import (
    render_claim_body,
    render_concept_body,
    render_source_body,
)
from graph_builder.vault.frontmatter_builder import (
    build_claim_frontmatter,
    build_concept_frontmatter,
    build_source_frontmatter,
)
from graph_builder.vault.manifest import write_manifest

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_STAGING_DIR = ".staging"
_REVIEW_NEEDED = "review_needed"

# Human-owned keys whose values must survive re-export if already edited.
_CONCEPT_HUMAN_KEYS = ("name", "canonical_definition", "human_notes")
_CLAIM_HUMAN_KEYS = ("status", "human_notes")
_SOURCE_HUMAN_KEYS = ("human_notes",)

# Maps claim_type -> subfolder name (pluralised)
_CLAIM_TYPE_DIRS: dict[str, str] = {
    "theorem": "theorems",
    "lemma": "lemmas",
    "proposition": "propositions",
    "corollary": "corollaries",
    "conjecture": "conjectures",
    "algorithm": "algorithms",
}
_DEFAULT_CLAIM_SUBDIR = "other"


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


async def export_vault(
    vault_dir: Path,
    graph_reader: GraphReader,
    neo4j_client: Neo4jClient,
) -> dict:
    """Export full Neo4j graph to Obsidian vault.

    Writes to staging dir first, then atomic move per file.
    Preserves human-owned fields from existing files.
    Returns manifest dict with counts.

    @param vault_dir Destination vault root directory.
    @param graph_reader Reader providing graph data (may be mocked).
    @param neo4j_client Neo4j client (passed for interface compatibility).
    @returns Manifest dict with keys: concepts, claims, sources.
    """
    data = await _fetch_graph_data(graph_reader)
    _ensure_vault_dirs(vault_dir, data["claims"])

    staging = vault_dir / _STAGING_DIR
    staging.mkdir(parents=True, exist_ok=True)

    counts = await _write_all_files(vault_dir, staging, data)

    _cleanup_staging(staging)

    manifest = {**counts, "exported_at": _utc_now()}
    write_manifest(vault_dir, manifest)
    return manifest


# ---------------------------------------------------------------------------
# Graph data fetching
# ---------------------------------------------------------------------------


async def _fetch_graph_data(reader: GraphReader) -> dict:
    """Query all nodes and edges from the graph reader.

    @param reader GraphReader (real or mock).
    @returns Dict with lists for each entity type.
    """
    return {
        "concepts": await reader.get_all_concepts(),
        "claims": await reader.get_all_claims(),
        "sources": await reader.get_all_sources(),
        "concept_edges": await reader.get_all_concept_edges(),
        "claim_edges": await reader.get_all_claim_edges(),
        "coupling_edges": await reader.get_all_coupling_edges(),
        "sourced_from": await reader.get_all_sourced_from_edges(),
        "provenances": await reader.get_all_provenances(),
    }


# ---------------------------------------------------------------------------
# Directory creation
# ---------------------------------------------------------------------------


def _ensure_vault_dirs(vault_dir: Path, claims: list[ClaimNode]) -> None:
    """Create all required vault subdirectories.

    @param vault_dir Root vault directory.
    @param claims Claims list used to determine claim type subdirs needed.
    """
    for name in ["concepts", "sources", "_review/concepts", "_review/claims", "_meta"]:
        (vault_dir / name).mkdir(parents=True, exist_ok=True)
    _ensure_claim_type_dirs(vault_dir, claims)


def _ensure_claim_type_dirs(vault_dir: Path, claims: list[ClaimNode]) -> None:
    """Create claims/{type}/ subdirs for all claim types present.

    @param vault_dir Root vault directory.
    @param claims Claims to inspect for type diversity.
    """
    seen: set[str] = set()
    for claim in claims:
        subdir = _claim_subdir(claim.claim_type)
        if subdir not in seen:
            (vault_dir / "claims" / subdir).mkdir(parents=True, exist_ok=True)
            seen.add(subdir)


def _claim_subdir(claim_type: str) -> str:
    """Map a claim_type string to its vault subdirectory name.

    @param claim_type Raw claim_type from ClaimNode.
    @returns Subfolder name under claims/.
    """
    return _CLAIM_TYPE_DIRS.get(claim_type, _DEFAULT_CLAIM_SUBDIR)


# ---------------------------------------------------------------------------
# Write orchestration
# ---------------------------------------------------------------------------


async def _write_all_files(
    vault_dir: Path,
    staging: Path,
    data: dict,
) -> dict:
    """Stage and move all vault files; return counts.

    @param vault_dir Final destination root.
    @param staging Temporary staging directory.
    @param data Dict returned by _fetch_graph_data.
    @returns Dict with keys concepts, claims, sources.
    """
    source_titles = {s.arxiv_id: s.title for s in data["sources"]}

    n_concepts = _write_concepts(vault_dir, staging, data, source_titles)
    n_claims = _write_claims(vault_dir, staging, data, source_titles)
    n_sources = _write_sources(vault_dir, staging, data)

    return {"concepts": n_concepts, "claims": n_claims, "sources": n_sources}


# ---------------------------------------------------------------------------
# Concept writing
# ---------------------------------------------------------------------------


def _write_concepts(
    vault_dir: Path,
    staging: Path,
    data: dict,
    source_titles: dict[str, str],
) -> int:
    """Write all concept files and return the count.

    @param vault_dir Final vault root.
    @param staging Staging directory.
    @param data Full graph data dict.
    @param source_titles Map of arxiv_id -> title.
    @returns Number of concept files written.
    """
    edges_by_source = _index_by(data["concept_edges"], "source_slug")
    sourced_by_node = _index_by(data["sourced_from"], "node_slug")
    provs_by_concept = _index_by(data["provenances"], "concept_slug")

    for concept in data["concepts"]:
        _write_concept_file(
            vault_dir, staging, concept,
            edges_by_source.get(concept.slug, []),
            sourced_by_node.get(concept.slug, []),
            provs_by_concept.get(concept.slug, []),
            source_titles,
        )
    return len(data["concepts"])


def _write_concept_file(
    vault_dir: Path,
    staging: Path,
    concept: ConceptNode,
    edges: list,
    sourced_from: list,
    provenances: list,
    source_titles: dict,
) -> None:
    """Build, stage, and atomically move a single concept file.

    @param vault_dir Final vault root.
    @param staging Staging directory.
    @param concept ConceptNode to render.
    @param edges Outbound ConceptEdge list for this concept.
    @param sourced_from SourcedFromEdge list for this concept.
    @param provenances ProvenanceNode list for this concept.
    @param source_titles Map of arxiv_id -> title.
    """
    fm = build_concept_frontmatter(
        concept, edges, sourced_from, source_titles=source_titles
    )
    final = vault_dir / "concepts" / f"{concept.slug}.md"
    _apply_human_overrides(fm, final, _CONCEPT_HUMAN_KEYS)

    body = render_concept_body(concept, provenances)
    content = _assemble(fm, body)

    _stage_and_move(staging / "concepts" / f"{concept.slug}.md", final, content)

    if concept.status == _REVIEW_NEEDED:
        review = vault_dir / "_review" / "concepts" / f"{concept.slug}.md"
        _stage_and_move(
            staging / "_review_c" / f"{concept.slug}.md", review, content
        )


# ---------------------------------------------------------------------------
# Claim writing
# ---------------------------------------------------------------------------


def _write_claims(
    vault_dir: Path,
    staging: Path,
    data: dict,
    source_titles: dict[str, str],
) -> int:
    """Write all claim files and return the count.

    @param vault_dir Final vault root.
    @param staging Staging directory.
    @param data Full graph data dict.
    @param source_titles Map of arxiv_id -> title.
    @returns Number of claim files written.
    """
    claim_edges_by = _index_by(data["claim_edges"], "source_slug")
    coupling_by = _index_by(data["coupling_edges"], "claim_slug")
    sourced_by = _index_by(data["sourced_from"], "node_slug")

    for claim in data["claims"]:
        _write_claim_file(
            vault_dir, staging, claim,
            claim_edges_by.get(claim.slug, []),
            coupling_by.get(claim.slug, []),
            sourced_by.get(claim.slug, []),
            source_titles,
        )
    return len(data["claims"])


def _write_claim_file(
    vault_dir: Path,
    staging: Path,
    claim: ClaimNode,
    claim_edges: list,
    coupling_edges: list,
    sourced_from: list,
    source_titles: dict,
) -> None:
    """Build, stage, and atomically move a single claim file.

    @param vault_dir Final vault root.
    @param staging Staging directory.
    @param claim ClaimNode to render.
    @param claim_edges Outbound ClaimEdge list for this claim.
    @param coupling_edges CouplingEdge list for this claim.
    @param sourced_from SourcedFromEdge list for this claim.
    @param source_titles Map of arxiv_id -> title.
    """
    fm = build_claim_frontmatter(
        claim, claim_edges, coupling_edges, sourced_from,
        source_titles=source_titles,
    )
    subdir = _claim_subdir(claim.claim_type)
    final = vault_dir / "claims" / subdir / f"{claim.slug}.md"
    _apply_human_overrides(fm, final, _CLAIM_HUMAN_KEYS)

    body = render_claim_body(claim)
    content = _assemble(fm, body)

    _stage_and_move(
        staging / "claims" / subdir / f"{claim.slug}.md", final, content
    )

    if claim.status == _REVIEW_NEEDED:
        review = vault_dir / "_review" / "claims" / f"{claim.slug}.md"
        _stage_and_move(
            staging / "_review_cl" / f"{claim.slug}.md", review, content
        )


# ---------------------------------------------------------------------------
# Source writing
# ---------------------------------------------------------------------------


def _write_sources(vault_dir: Path, staging: Path, data: dict) -> int:
    """Write all source files and return the count.

    @param vault_dir Final vault root.
    @param staging Staging directory.
    @param data Full graph data dict.
    @returns Number of source files written.
    """
    sourced_by = _index_by(data["sourced_from"], "source_arxiv_id")

    for source in data["sources"]:
        linked = sourced_by.get(source.arxiv_id, [])
        concept_slugs = [e.node_slug for e in linked if not _is_claim_slug(e.node_slug)]
        claim_slugs = [e.node_slug for e in linked if _is_claim_slug(e.node_slug)]

        fm = build_source_frontmatter(source)
        final = vault_dir / "sources" / f"{source.arxiv_id}.md"
        _apply_human_overrides(fm, final, _SOURCE_HUMAN_KEYS)

        body = render_source_body(source, concept_slugs, claim_slugs)
        content = _assemble(fm, body)
        _stage_and_move(staging / "sources" / f"{source.arxiv_id}.md", final, content)

    return len(data["sources"])


def _is_claim_slug(slug: str) -> bool:
    """Return True if the slug looks like a claim (contains '--').

    @param slug Node slug string.
    @returns True when '--' separator is present.
    """
    return "--" in slug


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _index_by(items: list, key: str) -> dict[str, list]:
    """Group a list of objects by a string attribute value.

    @param items List of Pydantic model instances or dicts.
    @param key Attribute name to group by.
    @returns Dict mapping attribute value -> list of items.
    """
    result: dict[str, list] = {}
    for item in items:
        val = getattr(item, key, None)
        if val is None:
            continue
        result.setdefault(val, []).append(item)
    return result


def _assemble(frontmatter: dict, body: str) -> str:
    """Combine a frontmatter dict and body string into a markdown file.

    @param frontmatter Dict to serialise as YAML between --- delimiters.
    @param body Markdown body text.
    @returns Complete file content string.
    """
    fm_yaml = yaml.dump(
        frontmatter, default_flow_style=False, allow_unicode=True, sort_keys=False
    )
    return f"---\n{fm_yaml}---\n\n{body}"


def _stage_and_move(staging_path: Path, final_path: Path, content: str) -> None:
    """Write content to a staging path, then move it to the final path.

    @param staging_path Temporary file location inside .staging/.
    @param final_path Destination file location in the vault.
    @param content File text to write.
    """
    staging_path.parent.mkdir(parents=True, exist_ok=True)
    final_path.parent.mkdir(parents=True, exist_ok=True)
    staging_path.write_text(content, encoding="utf-8")
    shutil.move(str(staging_path), str(final_path))


def _read_existing_frontmatter(path: Path) -> dict:
    """Parse YAML frontmatter from an existing vault file.

    Returns an empty dict when the file does not exist or has no frontmatter.

    @param path Path to an existing .md file.
    @returns Parsed frontmatter dict, or {} if absent/unparseable.
    """
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    try:
        return yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        return {}


def _apply_human_overrides(
    fm: dict,
    existing_path: Path,
    human_keys: tuple[str, ...],
) -> None:
    """Overwrite pipeline values with existing human-edited values in-place.

    Reads the existing file's frontmatter and copies any non-empty human
    values back into the outgoing frontmatter dict before staging.

    @param fm Frontmatter dict being prepared for writing (mutated in-place).
    @param existing_path Path to the current file on disk (may not exist).
    @param human_keys Tuple of key names considered human-owned.
    """
    existing = _read_existing_frontmatter(existing_path)
    for key in human_keys:
        if key in existing and existing[key]:
            fm[key] = existing[key]


def _cleanup_staging(staging: Path) -> None:
    """Remove the staging directory tree after all moves complete.

    @param staging Path to the .staging directory.
    """
    if staging.exists():
        shutil.rmtree(staging)


def _utc_now() -> str:
    """Return an ISO-8601 UTC timestamp string for the manifest.

    @returns Timestamp string like '2026-03-16T00:00:00'.
    """
    from datetime import datetime, timezone
    return datetime.now(tz=timezone.utc).isoformat(timespec="seconds")
