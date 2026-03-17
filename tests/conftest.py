"""
@file conftest.py
@description Shared test fixtures.
"""

import asyncio

import pytest


@pytest.fixture
def tmp_data_dir(tmp_path):
    """Create a temporary data directory structure."""
    papers_dir = tmp_path / "papers"
    processed_dir = tmp_path / "processed"
    papers_dir.mkdir()
    processed_dir.mkdir()
    return tmp_path


@pytest.fixture
def sample_csv(tmp_path):
    """Create a sample CSV input file."""
    csv_content = (
        'paper_name,file_path,file_type\n'
        '"Attention Is All You Need",2706.03762,pdf\n'
        '"BERT",1810.04805,html\n'
    )
    csv_file = tmp_path / "papers.csv"
    csv_file.write_text(csv_content)
    return csv_file


@pytest.fixture(scope="session")
def event_loop():
    """Create a single event loop for the entire test session."""
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def neo4j_container():
    """Start a Neo4j testcontainer for integration tests."""
    from testcontainers.neo4j import Neo4jContainer

    container = Neo4jContainer(
        "neo4j:5.26-community",
        username="neo4j",
        password="testpassword123",
    )
    container.start()
    bolt_url = container.get_connection_url()
    yield {"url": bolt_url, "user": "neo4j", "password": "testpassword123"}
    container.stop()


@pytest.fixture
async def neo4j_client(neo4j_container):
    """Provide a Neo4j client that cleans the DB between tests."""
    from graph_builder.graph.neo4j_client import Neo4jClient

    client = Neo4jClient(
        uri=neo4j_container["url"],
        user=neo4j_container["user"],
        password=neo4j_container["password"],
    )
    yield client
    # Clean DB between tests
    async with client._driver.session() as session:
        await session.run("MATCH (n) DETACH DELETE n")
    await client.close()
