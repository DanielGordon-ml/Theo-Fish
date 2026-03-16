"""
@file test_manifest.py
@description Tests for manifest.py: write and read export-manifest.json.
"""

import pytest

from graph_builder.vault.manifest import read_manifest, write_manifest

# ---------------------------------------------------------------------------
# write_manifest
# ---------------------------------------------------------------------------


class TestWriteManifest:
    """Tests for write_manifest()."""

    def test_it_should_create_meta_dir_and_write_json(self, tmp_path):
        """write_manifest creates _meta/ and writes valid JSON."""
        data = {"concepts": 5, "claims": 10, "sources": 2}
        write_manifest(tmp_path, data)

        meta_file = tmp_path / "_meta" / "export-manifest.json"
        assert meta_file.exists()

    def test_it_should_persist_all_provided_keys(self, tmp_path):
        """All keys in the data dict are written to the manifest file."""
        data = {"concepts": 3, "claims": 7, "sources": 1, "exported_at": "2026-03-16"}
        write_manifest(tmp_path, data)

        result = read_manifest(tmp_path)
        assert result["concepts"] == 3
        assert result["claims"] == 7
        assert result["sources"] == 1
        assert result["exported_at"] == "2026-03-16"

    def test_it_should_overwrite_existing_manifest(self, tmp_path):
        """A second write replaces the previous manifest content."""
        write_manifest(tmp_path, {"concepts": 1})
        write_manifest(tmp_path, {"concepts": 99})

        result = read_manifest(tmp_path)
        assert result["concepts"] == 99

    def test_it_should_write_empty_dict(self, tmp_path):
        """An empty dict produces a valid JSON file."""
        write_manifest(tmp_path, {})

        result = read_manifest(tmp_path)
        assert result == {}


# ---------------------------------------------------------------------------
# read_manifest
# ---------------------------------------------------------------------------


class TestReadManifest:
    """Tests for read_manifest()."""

    def test_it_should_return_none_when_file_missing(self, tmp_path):
        """Returns None when no manifest exists yet."""
        result = read_manifest(tmp_path)
        assert result is None

    def test_it_should_return_none_when_meta_dir_missing(self, tmp_path):
        """Returns None when the _meta directory does not exist."""
        vault = tmp_path / "empty_vault"
        vault.mkdir()

        result = read_manifest(vault)
        assert result is None

    def test_it_should_round_trip_nested_data(self, tmp_path):
        """Nested dicts and lists survive a write/read cycle intact."""
        data = {
            "counts": {"concepts": 2, "claims": 4},
            "files": ["a.md", "b.md"],
        }
        write_manifest(tmp_path, data)

        result = read_manifest(tmp_path)
        assert result["counts"]["concepts"] == 2
        assert result["files"] == ["a.md", "b.md"]
