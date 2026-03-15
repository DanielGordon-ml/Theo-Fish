"""
@file test_errors.py
@description Tests for LoaderError exception.
"""

from data_loader.errors import LoaderError


class TestLoaderError:
    def test_message_format(self):
        """It should format message as [arxiv_id] reason."""
        err = LoaderError(arxiv_id="2706.03762", reason="Both converters failed")
        assert str(err) == "[2706.03762] Both converters failed"

    def test_attributes(self):
        """It should store arxiv_id and reason as attributes."""
        err = LoaderError(arxiv_id="1810.04805", reason="no metadata")
        assert err.arxiv_id == "1810.04805"
        assert err.reason == "no metadata"

    def test_is_exception(self):
        """It should be a proper Exception subclass."""
        err = LoaderError(arxiv_id="2706.03762", reason="test")
        assert isinstance(err, Exception)
