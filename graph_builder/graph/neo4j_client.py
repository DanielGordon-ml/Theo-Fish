"""
@file neo4j_client.py
@description Async Neo4j driver wrapper with connection pool.
"""

from neo4j import AsyncDriver, AsyncGraphDatabase

from graph_builder.config.config import (
    NEO4J_AUTH_PASS,
    NEO4J_AUTH_USER,
    NEO4J_BOLT_URI,
)


class Neo4jClient:
    """Async Neo4j connection manager."""

    def __init__(
        self,
        uri: str = NEO4J_BOLT_URI,
        user: str = NEO4J_AUTH_USER,
        password: str = NEO4J_AUTH_PASS,
    ):
        """Initialize Neo4j async driver.

        @param uri Bolt connection URI
        @param user Neo4j username
        @param password Neo4j password
        """
        self._driver: AsyncDriver = AsyncGraphDatabase.driver(
            uri,
            auth=(user, password),
        )

    async def __aenter__(self):
        """Support async context manager protocol."""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Close driver on context exit."""
        await self.close()

    async def close(self) -> None:
        """Close the driver and release connection pool resources."""
        await self._driver.close()

    async def execute_read(self, query: str, **params):
        """Execute a read query and return results as a list of dicts.

        Uses a managed read transaction — safe for follower routing.

        @param query Cypher query string
        @param params Keyword parameters forwarded to tx.run
        @raises neo4j.exceptions.Neo4jError on query failure
        """

        async def _tx(tx):
            result = await tx.run(query, **params)
            return [record.data() async for record in result]

        async with self._driver.session() as session:
            return await session.execute_read(_tx)

    async def execute_write(self, query: str, **params):
        """Execute a single write query in a managed transaction.

        Uses session.execute_write — never auto-commit via session.run.

        @param query Cypher query string
        @param params Keyword parameters forwarded to tx.run
        @raises neo4j.exceptions.Neo4jError on query failure
        """

        async def _tx(tx):
            result = await tx.run(query, **params)
            return [record.data() async for record in result]

        async with self._driver.session() as session:
            return await session.execute_write(_tx)

    async def execute_write_tx(self, tx_func) -> None:
        """Execute a multi-statement write transaction via a caller-supplied function.

        Passes a live transaction object to tx_func so the caller can issue
        multiple Cypher statements atomically.

        @param tx_func Async callable receiving a Neo4j transaction object
        @raises neo4j.exceptions.Neo4jError on query failure
        """
        async with self._driver.session() as session:
            return await session.execute_write(tx_func)
