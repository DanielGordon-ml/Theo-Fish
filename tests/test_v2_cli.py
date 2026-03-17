"""
@file test_v2_cli.py
@description Unit tests for the v2 CLI argument parser. Tests argument
parsing only — no actual execution of pipeline actions.
"""

from pathlib import Path

import pytest

from graph_builder.orchestrator.cli import build_parser


class TestBuildParser:
    """Tests for build_parser() argument definitions."""

    def test_it_should_parse_paper_flag(self):
        """--paper flag captures the ArXiv ID string."""
        parser = build_parser()
        args = parser.parse_args(["--paper", "1904.07272"])
        assert args.paper == "1904.07272"

    def test_it_should_parse_input_dir_flag(self):
        """--input-dir flag captures the path as a Path object."""
        parser = build_parser()
        args = parser.parse_args(["--input-dir", "Data/cleaned/"])
        assert args.input_dir == Path("Data/cleaned")

    def test_it_should_parse_export_flag(self):
        """--export flag is stored as True when present."""
        parser = build_parser()
        args = parser.parse_args(["--export"])
        assert args.export is True

    def test_it_should_default_export_flag_to_false(self):
        """--export flag defaults to False when not provided."""
        parser = build_parser()
        args = parser.parse_args(["--paper", "1904.07272"])
        assert args.export is False

    def test_it_should_parse_sync_back_flag(self):
        """--sync-back flag is stored as True when present."""
        parser = build_parser()
        args = parser.parse_args(["--sync-back"])
        assert args.sync_back is True

    def test_it_should_default_sync_back_to_false(self):
        """--sync-back flag defaults to False when not provided."""
        parser = build_parser()
        args = parser.parse_args(["--paper", "1904.07272"])
        assert args.sync_back is False

    def test_it_should_parse_dry_run_with_sync_back(self):
        """--dry-run flag is accepted alongside --sync-back."""
        parser = build_parser()
        args = parser.parse_args(["--sync-back", "--dry-run"])
        assert args.sync_back is True
        assert args.dry_run is True

    def test_it_should_default_dry_run_to_false(self):
        """--dry-run flag defaults to False when not provided."""
        parser = build_parser()
        args = parser.parse_args(["--sync-back"])
        assert args.dry_run is False

    def test_it_should_parse_force_flag(self):
        """--force flag defaults to False, True when explicitly set."""
        parser = build_parser()
        args_default = parser.parse_args(["--paper", "1904.07272"])
        assert args_default.force is False

        args_force = parser.parse_args(["--paper", "1904.07272", "--force"])
        assert args_force.force is True

    def test_it_should_parse_concurrency_flag(self):
        """--concurrency flag captures the integer value."""
        parser = build_parser()
        args = parser.parse_args(["--paper", "1904.07272", "--concurrency", "5"])
        assert args.concurrency == 5

    def test_it_should_parse_no_thinking_flag(self):
        """--no-thinking flag defaults to False, True when set."""
        parser = build_parser()
        args_default = parser.parse_args(["--paper", "1904.07272"])
        assert args_default.no_thinking is False

        args_no_think = parser.parse_args(["--paper", "1904.07272", "--no-thinking"])
        assert args_no_think.no_thinking is True

    def test_it_should_combine_concurrency_no_thinking_and_paper(self):
        """--concurrency, --no-thinking, and --paper can be used together."""
        parser = build_parser()
        args = parser.parse_args([
            "--concurrency", "5", "--no-thinking", "--paper", "1904.07272",
        ])
        assert args.concurrency == 5
        assert args.no_thinking is True
        assert args.paper == "1904.07272"

    def test_it_should_error_when_no_action_flag_provided(self, capsys):
        """Parser raises SystemExit when no action flag (--paper, --input-dir,
        --export, --sync-back) is given."""
        parser = build_parser()
        with pytest.raises(SystemExit) as exc_info:
            # parse_args alone won't error — main() enforces this via a
            # post-parse check. We test the _validate_args helper directly.
            from graph_builder.orchestrator.cli import _validate_args
            _validate_args(parser, parser.parse_args([]))

        assert exc_info.value.code != 0
