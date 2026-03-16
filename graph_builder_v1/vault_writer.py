"""
@file vault_writer.py
@description Obsidian markdown generation with YAML frontmatter and wikilinks.
"""

import re
from datetime import datetime, timezone
from pathlib import Path

import yaml

from graph_builder.config import MAX_TITLE_LENGTH
from graph_builder.models import (
    CrossPaperLink,
    ExtractedEntity,
    PaperGraph,
    Relationship,
)

# Characters invalid in file/folder names
_UNSAFE_CHARS_RE = re.compile(r'[<>:"/\\|?*]')

# Characters invalid in filenames (broader set for entity labels with LaTeX)
_UNSAFE_FILENAME_RE = re.compile(r'[<>:"/\\|?*{}$^]')


def sanitize_filename(label: str) -> str:
    """Sanitize an entity label for use as a filename.

    Removes LaTeX special chars and other unsafe characters while
    preserving readability.

    @param label Entity label (may contain LaTeX like \\mathcal{A})
    """
    cleaned = _UNSAFE_FILENAME_RE.sub("", label).strip()
    # Collapse multiple spaces/underscores
    cleaned = re.sub(r"\s+", " ", cleaned)
    if not cleaned:
        cleaned = "entity"
    return cleaned


def sanitize_title(
    title: str, fallback: str = "untitled",
) -> str:
    """Sanitize a paper title for use as a folder name.

    @param title Paper title to sanitize
    @param fallback Fallback if title is empty after sanitization
    """
    cleaned = _UNSAFE_CHARS_RE.sub("", title).strip()
    cleaned = cleaned.replace(" ", "-")

    if not cleaned:
        return fallback.replace("/", "_")

    if len(cleaned) > MAX_TITLE_LENGTH:
        cleaned = cleaned[:MAX_TITLE_LENGTH]

    return cleaned


def build_index_md(graph: PaperGraph) -> str:
    """Build the index.md content for a paper folder.

    @param graph Extracted paper graph with entities and relationships
    """
    lines = [
        f"# {graph.title}",
        "",
        f"**ArXiv ID:** {graph.arxiv_id}",
        "",
        "## Entities",
        "",
    ]

    for entity in graph.entities:
        lines.append(
            f"- **{entity.entity_type.value}:** [[{entity.label}]]",
        )

    lines.append("")
    lines.append(f"*Extracted: {_now_iso()}*")
    return "\n".join(lines) + "\n"


def build_entity_md(
    entity: ExtractedEntity,
    graph: PaperGraph,
    relationships: list[Relationship],
    cross_links: list[CrossPaperLink],
    cross_paper_folders: dict[str, str] | None = None,
) -> str:
    """Build the markdown content for a single entity file.

    @param entity The entity to render
    @param graph Parent paper graph for metadata
    @param relationships Relationships involving this entity
    @param cross_links Cross-paper links for this entity
    @param cross_paper_folders ArXiv ID -> folder name mapping
    """
    folders = cross_paper_folders or {}

    # Build frontmatter
    related = _build_related_list(entity, relationships)
    frontmatter = _build_frontmatter(entity, graph, related)
    fm_yaml = yaml.dump(
        frontmatter, default_flow_style=False, allow_unicode=True,
        sort_keys=False,
    ).rstrip()

    # Build body
    body_parts = [
        f"# {entity.label}",
        "",
        entity.statement,
    ]

    if entity.proof:
        body_parts.extend(["", "## Proof", "", entity.proof])

    # Relationship section
    rel_lines = _build_relationship_lines(entity, relationships)
    cross_lines = _build_cross_paper_lines(entity, cross_links, folders)

    if rel_lines or cross_lines:
        body_parts.extend(["", "## Relationships", ""])
        body_parts.extend(rel_lines)
        body_parts.extend(cross_lines)

    # References section
    body_parts.extend([
        "",
        "## References",
        "",
        f"- Paper: [[index|{graph.title}]]",
        f"- Section: {entity.section}",
    ])

    body = "\n".join(body_parts) + "\n"
    return f"---\n{fm_yaml}\n---\n\n{body}"


def write_paper_vault(
    graph: PaperGraph,
    vault_dir: Path,
    relationships: list[Relationship],
    cross_links: list[CrossPaperLink],
    cross_paper_folders: dict[str, str] | None = None,
) -> Path:
    """Write all vault files for a single paper.

    @param graph Extracted paper graph
    @param vault_dir Root vault directory
    @param relationships Validated relationships
    @param cross_links Cross-paper links
    @param cross_paper_folders ArXiv ID -> folder name mapping
    @returns Path to the created paper folder
    """
    folder_name = sanitize_title(graph.title, fallback=graph.arxiv_id)
    paper_dir = vault_dir / folder_name
    paper_dir.mkdir(parents=True, exist_ok=True)

    # Write index.md
    index_content = build_index_md(graph)
    (paper_dir / "index.md").write_text(index_content, encoding="utf-8")

    # Write entity files
    for entity in graph.entities:
        entity_rels = _filter_relationships(entity, relationships)
        entity_cross = _filter_cross_links(entity, cross_links)
        content = build_entity_md(
            entity, graph, entity_rels, entity_cross, cross_paper_folders,
        )
        filename = f"{sanitize_filename(entity.label)}.md"
        (paper_dir / filename).write_text(content, encoding="utf-8")

    return paper_dir


def _build_frontmatter(
    entity: ExtractedEntity,
    graph: PaperGraph,
    related: list[str],
) -> dict:
    """Build YAML frontmatter dict for an entity file."""
    return {
        "type": entity.entity_type.value,
        "label": entity.label,
        "paper": graph.title,
        "arxiv_id": graph.arxiv_id,
        "section": entity.section,
        "related_entities": related,
        "date_extracted": _now_iso(),
    }


def _build_related_list(
    entity: ExtractedEntity,
    relationships: list[Relationship],
) -> list[str]:
    """Build list of related entity wikilinks."""
    related: list[str] = []
    for rel in relationships:
        if rel.source_label == entity.label:
            related.append(f"[[{rel.target_label}]]")
        elif rel.target_label == entity.label:
            related.append(f"[[{rel.source_label}]]")
    return related


def _build_relationship_lines(
    entity: ExtractedEntity,
    relationships: list[Relationship],
) -> list[str]:
    """Build markdown lines for intra-paper relationships."""
    lines: list[str] = []
    for rel in relationships:
        if rel.source_label == entity.label:
            label = rel.relationship_type.value.replace("-", " ").title()
            lines.append(f"- **{label}:** [[{rel.target_label}]]")
        elif rel.target_label == entity.label:
            label = rel.relationship_type.value.replace("-", " ").title()
            lines.append(f"- **{label} (inverse):** [[{rel.source_label}]]")
    return lines


def _build_cross_paper_lines(
    entity: ExtractedEntity,
    cross_links: list[CrossPaperLink],
    folders: dict[str, str],
) -> list[str]:
    """Build markdown lines for cross-paper links."""
    lines: list[str] = []
    for link in cross_links:
        folder = folders.get(link.target_paper, link.target_paper)
        display = f"{link.target_entity} ({folder})"
        lines.append(
            f"- **Cross-paper:** [[{folder}/{link.target_entity}|{display}]]",
        )
    return lines


def _filter_relationships(
    entity: ExtractedEntity,
    relationships: list[Relationship],
) -> list[Relationship]:
    """Filter relationships to those involving this entity."""
    return [
        r for r in relationships
        if r.source_label == entity.label or r.target_label == entity.label
    ]


def _filter_cross_links(
    entity: ExtractedEntity,
    cross_links: list[CrossPaperLink],
) -> list[CrossPaperLink]:
    """Filter cross-paper links to those involving this entity."""
    return [
        cl for cl in cross_links
        if cl.source_entity == entity.label
    ]


def _now_iso() -> str:
    """Return the current UTC time as ISO 8601 string."""
    return datetime.now(timezone.utc).isoformat()
