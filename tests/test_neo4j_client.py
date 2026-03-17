"""
@file test_neo4j_client.py
@description Unit tests for the async Neo4j client — driver mocked throughout.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from graph_builder.graph.neo4j_client import Neo4jClient


class TestNeo4jClientInit:
    """Tests for Neo4jClient driver construction."""

    def test_it_should_create_driver_with_correct_uri_and_auth(self):
        """Driver is created with the given URI and (user, password) tuple."""
        with patch("graph_builder.graph.neo4j_client.AsyncGraphDatabase") as mock_gdb:
            mock_gdb.driver.return_value = MagicMock()

            client = Neo4jClient(
                uri="bolt://test-host:7687",
                user="testuser",
                password="testpass",
            )

            mock_gdb.driver.assert_called_once_with(
                "bolt://test-host:7687",
                auth=("testuser", "testpass"),
            )
            assert client._driver is mock_gdb.driver.return_value


class TestNeo4jClientClose:
    """Tests for Neo4jClient.close()."""

    @pytest.mark.asyncio
    async def test_it_should_close_the_driver(self):
        """close() awaits driver.close() exactly once."""
        with patch("graph_builder.graph.neo4j_client.AsyncGraphDatabase") as mock_gdb:
            mock_driver = AsyncMock()
            mock_gdb.driver.return_value = mock_driver

            client = Neo4jClient(uri="bolt://localhost:7687", user="u", password="p")
            await client.close()

            mock_driver.close.assert_awaited_once()


class TestNeo4jClientExecuteRead:
    """Tests for Neo4jClient.execute_read()."""

    @pytest.mark.asyncio
    async def test_it_should_execute_read_query_through_session(self):
        """execute_read routes through session.execute_read with a tx function."""
        with patch("graph_builder.graph.neo4j_client.AsyncGraphDatabase") as mock_gdb:
            expected_rows = [{"id": 1, "name": "Alpha"}]

            # Build a minimal async-context-manager session mock
            mock_session = _make_session_mock(
                read_return=expected_rows,
            )
            mock_driver = MagicMock()
            mock_driver.session.return_value = mock_session
            mock_gdb.driver.return_value = mock_driver

            client = Neo4jClient(uri="bolt://localhost:7687", user="u", password="p")
            result = await client.execute_read("MATCH (n) RETURN n")

            assert result == expected_rows
            mock_session.__aenter__.assert_called_once()
            mock_session.execute_read.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_it_should_pass_params_to_read_tx(self):
        """Keyword params are forwarded to tx.run inside the read transaction."""
        with patch("graph_builder.graph.neo4j_client.AsyncGraphDatabase") as mock_gdb:
            captured: dict = {}

            async def fake_execute_read(tx_func):
                mock_tx = AsyncMock()

                # Capture what tx.run was called with
                async def capturing_run(query, **params):
                    captured["query"] = query
                    captured["params"] = params
                    mock_result = AsyncMock()
                    mock_result.__aiter__ = lambda s: aiter_from([])
                    return mock_result

                mock_tx.run = capturing_run
                return await tx_func(mock_tx)

            mock_session = _make_session_mock()
            mock_session.execute_read = fake_execute_read
            mock_driver = MagicMock()
            mock_driver.session.return_value = mock_session
            mock_gdb.driver.return_value = mock_driver

            client = Neo4jClient(uri="bolt://localhost:7687", user="u", password="p")
            await client.execute_read("MATCH (n {id: $node_id}) RETURN n", node_id=42)

            assert captured["query"] == "MATCH (n {id: $node_id}) RETURN n"
            assert captured["params"] == {"node_id": 42}


class TestNeo4jClientExecuteWrite:
    """Tests for Neo4jClient.execute_write()."""

    @pytest.mark.asyncio
    async def test_it_should_execute_write_in_managed_transaction(self):
        """execute_write uses session.execute_write, not session.run directly."""
        with patch("graph_builder.graph.neo4j_client.AsyncGraphDatabase") as mock_gdb:
            expected_rows = [{"created": True}]

            mock_session = _make_session_mock(write_return=expected_rows)
            mock_driver = MagicMock()
            mock_driver.session.return_value = mock_session
            mock_gdb.driver.return_value = mock_driver

            client = Neo4jClient(uri="bolt://localhost:7687", user="u", password="p")
            result = await client.execute_write(
                "CREATE (n:Node {id: $node_id}) RETURN n",
                node_id=99,
            )

            assert result == expected_rows
            mock_session.execute_write.assert_awaited_once()
            # session.run must NOT be called — writes go through managed tx only
            mock_session.run.assert_not_called()

    @pytest.mark.asyncio
    async def test_it_should_not_use_auto_commit_for_writes(self):
        """session.run is never called for write queries."""
        with patch("graph_builder.graph.neo4j_client.AsyncGraphDatabase") as mock_gdb:
            mock_session = _make_session_mock(write_return=[])
            mock_driver = MagicMock()
            mock_driver.session.return_value = mock_session
            mock_gdb.driver.return_value = mock_driver

            client = Neo4jClient(uri="bolt://localhost:7687", user="u", password="p")
            await client.execute_write("CREATE (n:Thing)")

            mock_session.run.assert_not_called()


class TestNeo4jClientExecuteWriteTx:
    """Tests for Neo4jClient.execute_write_tx()."""

    @pytest.mark.asyncio
    async def test_it_should_pass_tx_func_to_execute_write(self):
        """execute_write_tx delegates the caller's tx_func to session.execute_write."""
        with patch("graph_builder.graph.neo4j_client.AsyncGraphDatabase") as mock_gdb:
            user_tx_func = AsyncMock(return_value={"ok": True})

            mock_session = _make_session_mock()
            mock_session.execute_write = AsyncMock(return_value={"ok": True})
            mock_driver = MagicMock()
            mock_driver.session.return_value = mock_session
            mock_gdb.driver.return_value = mock_driver

            client = Neo4jClient(uri="bolt://localhost:7687", user="u", password="p")
            result = await client.execute_write_tx(user_tx_func)

            mock_session.execute_write.assert_awaited_once_with(user_tx_func)
            assert result == {"ok": True}

    @pytest.mark.asyncio
    async def test_it_should_return_tx_func_result(self):
        """execute_write_tx returns whatever session.execute_write resolves to."""
        with patch("graph_builder.graph.neo4j_client.AsyncGraphDatabase") as mock_gdb:
            mock_session = _make_session_mock()
            mock_session.execute_write = AsyncMock(return_value=[1, 2, 3])
            mock_driver = MagicMock()
            mock_driver.session.return_value = mock_session
            mock_gdb.driver.return_value = mock_driver

            client = Neo4jClient(uri="bolt://localhost:7687", user="u", password="p")
            result = await client.execute_write_tx(AsyncMock())

            assert result == [1, 2, 3]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _make_session_mock(
    read_return=None,
    write_return=None,
):
    """Build an async-context-manager session mock with pre-wired results.

    @param read_return Value returned by execute_read
    @param write_return Value returned by execute_write
    """
    mock_session = MagicMock()
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=False)
    mock_session.execute_read = AsyncMock(return_value=read_return or [])
    mock_session.execute_write = AsyncMock(return_value=write_return or [])
    mock_session.run = AsyncMock()
    return mock_session


async def aiter_from(items):
    """Yield items as an async iterator (for mocking async for loops)."""
    for item in items:
        yield item
