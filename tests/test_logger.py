"""
@file test_logger.py
@description Tests for logger setup and formatting.
"""

import logging
import pytest
from data_loader.logger import setup_logger


@pytest.fixture(autouse=True)
def _reset_logger():
    """Clear logger handlers before each test for isolation."""
    log = logging.getLogger("data_loader")
    log.handlers.clear()
    yield
    log.handlers.clear()


class TestSetupLogger:
    def test_creates_log_file(self, tmp_path):
        """It should create a log file and write warnings."""
        logger = setup_logger(log_dir=tmp_path)
        log_file = tmp_path / "loader.log"
        logger.warning("test warning", extra={"arxiv_id": "2706.03762"})
        assert log_file.exists()
        content = log_file.read_text()
        assert "WARNING" in content
        assert "2706.03762" in content

    def test_writes_error(self, tmp_path):
        """It should write error messages to log file."""
        logger = setup_logger(log_dir=tmp_path)
        logger.error("test error", extra={"arxiv_id": "9999.99999"})
        content = (tmp_path / "loader.log").read_text()
        assert "ERROR" in content
        assert "9999.99999" in content

    def test_ignores_info(self, tmp_path):
        """It should ignore INFO-level messages."""
        logger = setup_logger(log_dir=tmp_path)
        logger.info("should not appear", extra={"arxiv_id": "0000.00000"})
        content = (tmp_path / "loader.log").read_text()
        assert "should not appear" not in content

    def test_appends_across_calls(self, tmp_path):
        """It should append logs across multiple setup calls."""
        # Reset logger handlers for clean test
        log = logging.getLogger("data_loader")
        log.handlers.clear()
        logger = setup_logger(log_dir=tmp_path)
        logger.warning("first", extra={"arxiv_id": "1111.11111"})
        # Simulate a second run (clear and re-setup)
        log.handlers.clear()
        logger = setup_logger(log_dir=tmp_path)
        logger.warning("second", extra={"arxiv_id": "2222.22222"})
        content = (tmp_path / "loader.log").read_text()
        assert "first" in content
        assert "second" in content
