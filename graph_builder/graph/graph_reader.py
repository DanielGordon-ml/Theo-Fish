"""
@file graph_reader.py
@description Read operations for the dual-graph knowledge graph in Neo4j.
"""

from graph_builder.graph.neo4j_client import Neo4jClient
from graph_builder.models.concept import ConceptNode

_ALL_SLUGS_CYPHER = "MATCH (c:Concept) RETURN c.slug AS slug"

_GET_CONCEPT_CYPHER = """
MATCH (c:Concept {slug: $slug})
RETURN c {.*} AS props
"""

_NEIGHBORS_CYPHER = """
MATCH (c:Concept)-[:CONCEPT_REL]-(neighbor:Concept)
WHERE c.slug IN $slugs
RETURN DISTINCT neighbor {.*} AS props
"""

_VECTOR_SEARCH_CYPHER = """
CALL db.index.vector.queryNodes('concept_embedding_idx', $top_k, $embedding)
YIELD node, score
RETURN node.slug AS slug, score
"""

_IS_PAPER_BUILT_CYPHER = """
MATCH (s:Source {arxiv_id: $arxiv_id})
RETURN count(s) AS count
"""


class GraphReader:
    """Read-only queries against the dual-graph knowledge graph.

    All methods use read transactions for safe follower routing.
    """

    def __init__(self, client: Neo4jClient):
        """Initialize with a Neo4jClient.

        @param client Connected Neo4jClient instance
        """
        self._client = client

    async def get_all_concept_slugs(self) -> list[str]:
        """Return every concept slug in the graph.

        @returns List of slug strings, empty if no concepts exist
        """
        rows = await self._client.execute_read(_ALL_SLUGS_CYPHER)
        return [row["slug"] for row in rows]

    async def get_existing_concept(self, slug: str) -> ConceptNode | None:
        """Look up a single concept by slug.

        @param slug Concept slug to look up
        @returns ConceptNode if found, None otherwise
        """
        rows = await self._client.execute_read(
            _GET_CONCEPT_CYPHER,
            slug=slug,
        )
        if not rows:
            return None
        return _row_to_concept(rows[0])

    async def get_concept_neighbors(
        self,
        slugs: list[str],
    ) -> list[ConceptNode]:
        """Find immediate Graph A neighbors of the given concepts.

        @param slugs List of concept slugs to find neighbors for
        @returns List of neighboring ConceptNodes
        """
        rows = await self._client.execute_read(
            _NEIGHBORS_CYPHER,
            slugs=slugs,
        )
        return [_row_to_concept(row) for row in rows]

    async def vector_similarity_search(
        self,
        embedding: list[float],
        top_k: int = 20,
    ) -> list[tuple[str, float]]:
        """Query the vector index for similar concepts.

        @param embedding Query embedding vector
        @param top_k Number of nearest neighbors to return (default 20)
        @returns List of (slug, score) tuples ordered by similarity
        """
        rows = await self._client.execute_read(
            _VECTOR_SEARCH_CYPHER,
            embedding=embedding,
            top_k=top_k,
        )
        return [(row["slug"], row["score"]) for row in rows]

    async def is_paper_built(self, arxiv_id: str) -> bool:
        """Check whether a Source node exists for the given arxiv_id.

        @param arxiv_id ArXiv paper identifier
        @returns True if the paper has already been ingested
        """
        rows = await self._client.execute_read(
            _IS_PAPER_BUILT_CYPHER,
            arxiv_id=arxiv_id,
        )
        return rows[0]["count"] > 0 if rows else False


def _row_to_concept(row: dict) -> ConceptNode:
    """Convert a Neo4j record dict into a ConceptNode.

    Handles both raw property dicts and nested {props: ...} records.

    @param row Dict from Neo4j query result
    @returns Hydrated ConceptNode
    """
    props = row.get("props", row)
    return ConceptNode(**_filter_concept_fields(props))


def _filter_concept_fields(props: dict) -> dict:
    """Keep only fields that ConceptNode accepts, dropping Neo4j internals.

    Converts Neo4j native types (DateTime, etc.) to strings.

    @param props Raw property dict from Neo4j
    @returns Filtered dict safe for ConceptNode construction
    """
    allowed = ConceptNode.model_fields.keys()
    result = {}
    for k, v in props.items():
        if k not in allowed:
            continue
        result[k] = _coerce_neo4j_type(v)
    return result


def _coerce_neo4j_type(value):
    """Convert Neo4j native types to Python primitives.

    @param value Value from Neo4j record
    @returns Python-native equivalent
    """
    if hasattr(value, "iso_format"):
        return value.iso_format()
    return value
