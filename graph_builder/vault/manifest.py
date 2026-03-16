"""
@file manifest.py
@description Read and write the export-manifest.json file stored in _meta/.

The manifest captures file counts and export metadata so downstream tools
can detect stale exports without scanning the full vault tree.
"""

import json
from pathlib import Path

_META_DIR = "_meta"
_MANIFEST_FILENAME = "export-manifest.json"


def _manifest_path(vault_dir: Path) -> Path:
    """Return the absolute path for the manifest file.

    @param vault_dir Root vault directory.
    @returns Path to _meta/export-manifest.json.
    """
    return vault_dir / _META_DIR / _MANIFEST_FILENAME


def write_manifest(vault_dir: Path, data: dict) -> None:
    """Write export-manifest.json to _meta/.

    Creates the _meta/ directory if it does not already exist.
    Overwrites any existing manifest on repeated calls.

    @param vault_dir Root directory of the Obsidian vault.
    @param data Dict of counts and metadata to serialise as JSON.
    """
    meta_dir = vault_dir / _META_DIR
    meta_dir.mkdir(parents=True, exist_ok=True)
    manifest = _manifest_path(vault_dir)
    manifest.write_text(json.dumps(data, indent=2, ensure_ascii=False))


def read_manifest(vault_dir: Path) -> dict | None:
    """Read export-manifest.json, returns None if not found.

    @param vault_dir Root directory of the Obsidian vault.
    @returns Parsed manifest dict, or None if the file does not exist.
    """
    manifest = _manifest_path(vault_dir)
    if not manifest.exists():
        return None
    return json.loads(manifest.read_text())
