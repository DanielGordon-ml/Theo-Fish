"""
@file vault_scanner.py
@description Scan existing vault frontmatter into searchable index.
"""

import logging
from dataclasses import dataclass, field
from pathlib import Path

import yaml

logger = logging.getLogger("graph_builder")


@dataclass
class VaultEntry:
    """A single entity found in the existing vault."""

    paper_title: str
    arxiv_id: str
    label: str
    entity_type: str
    paper_folder: str


@dataclass
class VaultIndex:
    """Searchable index of vault entity files."""

    label_index: dict[str, list[VaultEntry]] = field(default_factory=dict)
    tag_index: dict[str, list[VaultEntry]] = field(default_factory=dict)

    def get_by_label(self, label: str) -> list[VaultEntry]:
        """Look up vault entries by entity label (case-insensitive).

        @param label Entity label to search for
        """
        return self.label_index.get(label.lower(), [])

    def get_labels_map(self) -> dict[str, list[tuple[str, str]]]:
        """Return label -> [(paper_title, arxiv_id)] for cross-paper linking."""
        result: dict[str, list[tuple[str, str]]] = {}
        for label, entries in self.label_index.items():
            result[label] = [
                (e.paper_title, e.arxiv_id) for e in entries
            ]
        return result


def scan_vault(vault_dir: Path) -> VaultIndex:
    """Walk the vault directory and build a searchable index.

    @param vault_dir Path to the data_vault directory
    """
    index = VaultIndex()

    if not vault_dir.exists():
        return index

    for paper_folder in vault_dir.iterdir():
        if not paper_folder.is_dir():
            continue
        _scan_paper_folder(paper_folder, index)

    return index


def _scan_paper_folder(folder: Path, index: VaultIndex) -> None:
    """Scan a single paper folder for entity files."""
    for md_file in folder.glob("*.md"):
        if md_file.name == "index.md":
            continue
        _index_entity_file(md_file, folder.name, index)


def _index_entity_file(
    file_path: Path, paper_folder: str, index: VaultIndex,
) -> None:
    """Parse frontmatter from an entity file and add to index."""
    try:
        frontmatter = _parse_frontmatter(file_path)
    except Exception:
        logger.warning(
            "Failed to parse frontmatter: %s", str(file_path),
            extra={"arxiv_id": "scan"},
        )
        return

    if not frontmatter:
        return

    label = frontmatter.get("label", "")
    if not label:
        return

    entry = VaultEntry(
        paper_title=frontmatter.get("paper", ""),
        arxiv_id=frontmatter.get("arxiv_id", ""),
        label=label,
        entity_type=frontmatter.get("type", ""),
        paper_folder=paper_folder,
    )

    normalized_label = label.lower()
    index.label_index.setdefault(normalized_label, []).append(entry)

    for tag in frontmatter.get("tags", []):
        index.tag_index.setdefault(tag, []).append(entry)


def _parse_frontmatter(file_path: Path) -> dict:
    """Extract YAML frontmatter from a markdown file."""
    content = file_path.read_text(encoding="utf-8")

    if not content.startswith("---"):
        return {}

    end_idx = content.index("---", 3)
    yaml_str = content[3:end_idx].strip()
    return yaml.safe_load(yaml_str) or {}
