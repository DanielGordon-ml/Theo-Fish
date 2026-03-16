"""
@file graph_writer.py
@description Write operations for the dual-graph knowledge graph in Neo4j.
"""

from graph_builder.graph.neo4j_client import Neo4jClient
from graph_builder.models.claim import ClaimNode
from graph_builder.models.concept import ConceptNode
from graph_builder.models.edges import ClaimEdge, ConceptEdge, CouplingEdge
from graph_builder.models.provenance import FormulationEdge, ProvenanceNode
from graph_builder.models.source import SourceNode

# Cypher for MERGE-ing a Concept with field-ownership semantics.
# Pipeline-owned fields are always overwritten.
# Human-owned fields (name, canonical_definition, human_notes) use COALESCE
# so that existing human edits are never clobbered by the pipeline.
_MERGE_CONCEPT_CYPHER = """
MERGE (c:Concept {slug: $slug})
ON CREATE SET
    c.name = $name,
    c.canonical_definition = $canonical_definition,
    c.human_notes = $human_notes,
    c.semantic_type = $semantic_type,
    c.rhetorical_origin = $rhetorical_origin,
    c.formal_spec = $formal_spec,
    c.components = $components,
    c.ts_domain = $ts_domain,
    c.ts_codomain = $ts_codomain,
    c.ts_applies_to = $ts_applies_to,
    c.ts_member_type = $ts_member_type,
    c.ts_objective = $ts_objective,
    c.aliases = $aliases,
    c.status = $status,
    c.embedding = $embedding
ON MATCH SET
    c.semantic_type = $semantic_type,
    c.rhetorical_origin = $rhetorical_origin,
    c.formal_spec = $formal_spec,
    c.components = $components,
    c.ts_domain = $ts_domain,
    c.ts_codomain = $ts_codomain,
    c.ts_applies_to = $ts_applies_to,
    c.ts_member_type = $ts_member_type,
    c.ts_objective = $ts_objective,
    c.aliases = $aliases,
    c.status = $status,
    c.embedding = $embedding,
    c.name = COALESCE(c.name, $name),
    c.canonical_definition = COALESCE(c.canonical_definition, $canonical_definition),
    c.human_notes = COALESCE(c.human_notes, $human_notes)
SET c.date_modified = datetime()
"""

_CREATE_CLAIM_CYPHER = """
MATCH (s:Source {arxiv_id: $source_arxiv_id})
CREATE (cl:Claim {
    slug: $slug,
    source_paper_slug: $source_paper_slug,
    label: $label,
    name: $name,
    claim_type: $claim_type,
    assumptions: $assumptions,
    conclusion: $conclusion,
    proof_technique: $proof_technique,
    strength: $strength,
    statement: $statement,
    proof: $proof,
    section: $section,
    status: $status,
    human_notes: $human_notes,
    date_modified: datetime()
})
CREATE (cl)-[:SOURCED_FROM]->(s)
"""

_CREATE_PROVENANCE_CYPHER = """
MATCH (c:Concept {slug: $concept_slug})
MATCH (s:Source {arxiv_id: $source_arxiv_id})
CREATE (p:Provenance {
    concept_slug: $concept_slug,
    source_arxiv_id: $source_arxiv_id,
    formulation: $formulation,
    formal_spec: $formal_spec,
    section: $section,
    extraction_confidence: $extraction_confidence
})
CREATE (p)-[:FORMULATION_OF {
    match_method: $match_method,
    match_confidence: $match_confidence
}]->(c)
CREATE (p)-[:SOURCED_FROM]->(s)
"""

_MERGE_SOURCE_CYPHER = """
MERGE (s:Source {arxiv_id: $arxiv_id})
ON CREATE SET
    s.title = $title,
    s.authors = $authors,
    s.date_published = $date_published,
    s.date_extracted = $date_extracted,
    s.human_notes = $human_notes
ON MATCH SET
    s.title = $title,
    s.authors = $authors,
    s.date_published = $date_published,
    s.date_extracted = $date_extracted
SET s.date_modified = datetime()
"""

_CONCEPT_EDGE_CYPHER = """
MATCH (a:Concept {slug: $source_slug})
MATCH (b:Concept {slug: $target_slug})
CREATE (a)-[r:CONCEPT_REL {edge_type: $edge_type}]->(b)
SET r += $attributes
"""

_CLAIM_EDGE_CYPHER = """
MATCH (a:Claim {slug: $source_slug})
MATCH (b:Claim {slug: $target_slug})
CREATE (a)-[r:CLAIM_REL {edge_type: $edge_type}]->(b)
SET r += $attributes
"""

_COUPLING_EDGE_CYPHER = """
MATCH (cl:Claim {slug: $claim_slug})
MATCH (c:Concept {slug: $concept_slug})
CREATE (cl)-[:ABOUT {role: $role, aspect: $aspect}]->(c)
"""

_CLEAR_CLAIMS_CYPHER = """
MATCH (cl:Claim {source_paper_slug: $paper_slug})
DETACH DELETE cl
"""

_CLEAR_PROVENANCES_CYPHER = """
MATCH (p:Provenance {source_arxiv_id: $arxiv_id})
DETACH DELETE p
"""

# Schema DDL — uniqueness constraints and indexes
_SCHEMA_STATEMENTS = [
    "CREATE CONSTRAINT concept_slug_unique IF NOT EXISTS FOR (c:Concept) REQUIRE c.slug IS UNIQUE",
    "CREATE CONSTRAINT claim_slug_unique IF NOT EXISTS FOR (cl:Claim) REQUIRE cl.slug IS UNIQUE",
    "CREATE CONSTRAINT source_arxiv_unique IF NOT EXISTS FOR (s:Source) REQUIRE s.arxiv_id IS UNIQUE",
    "CREATE INDEX concept_semantic_type_idx IF NOT EXISTS FOR (c:Concept) ON (c.semantic_type)",
    "CREATE INDEX claim_type_idx IF NOT EXISTS FOR (cl:Claim) ON (cl.claim_type)",
    "CREATE INDEX claim_source_paper_idx IF NOT EXISTS FOR (cl:Claim) ON (cl.source_paper_slug)",
]


class GraphWriter:
    """Writes nodes and edges to the dual-graph knowledge graph in Neo4j.

    Enforces field-ownership semantics: pipeline-owned fields are always
    overwritten, human-owned fields are preserved via COALESCE.
    """

    def __init__(self, client: Neo4jClient):
        """Initialize with a Neo4jClient.

        @param client Connected Neo4jClient instance
        """
        self._client = client

    async def write_concept(self, concept: ConceptNode) -> None:
        """MERGE a concept node by slug with field-ownership semantics.

        Pipeline-owned fields (semantic_type, formal_spec, etc.) are always
        overwritten. Human-owned fields (name, canonical_definition,
        human_notes) use COALESCE to preserve existing values.

        @param concept ConceptNode to merge
        """
        await self._client.execute_write(
            _MERGE_CONCEPT_CYPHER,
            **_concept_params(concept),
        )

    async def write_claim(
        self,
        claim: ClaimNode,
        source_arxiv_id: str,
    ) -> None:
        """CREATE a claim node with a SOURCED_FROM edge to its source.

        @param claim ClaimNode to create
        @param source_arxiv_id ArXiv ID of the source paper
        """
        await self._client.execute_write(
            _CREATE_CLAIM_CYPHER,
            **_claim_params(claim, source_arxiv_id),
        )

    async def write_provenance(
        self,
        prov: ProvenanceNode,
        form_edge: FormulationEdge,
    ) -> None:
        """CREATE a provenance node with FORMULATION_OF and SOURCED_FROM edges.

        @param prov ProvenanceNode to create
        @param form_edge FormulationEdge with match metadata
        """
        await self._client.execute_write(
            _CREATE_PROVENANCE_CYPHER,
            **_provenance_params(prov, form_edge),
        )

    async def write_source(self, source: SourceNode) -> None:
        """MERGE a source node by arxiv_id.

        @param source SourceNode to merge
        """
        await self._client.execute_write(
            _MERGE_SOURCE_CYPHER,
            **_source_params(source),
        )

    async def write_concept_edges(
        self,
        edges: list[ConceptEdge],
    ) -> None:
        """Batch-write concept-to-concept edges in a single transaction.

        @param edges List of ConceptEdge to write
        """
        await self._write_edges_batch(
            edges,
            _CONCEPT_EDGE_CYPHER,
            _concept_edge_params,
        )

    async def write_claim_edges(
        self,
        edges: list[ClaimEdge],
    ) -> None:
        """Batch-write claim-to-claim edges in a single transaction.

        @param edges List of ClaimEdge to write
        """
        await self._write_edges_batch(
            edges,
            _CLAIM_EDGE_CYPHER,
            _claim_edge_params,
        )

    async def write_coupling_edges(
        self,
        edges: list[CouplingEdge],
    ) -> None:
        """Batch-write ABOUT edges from claims to concepts in a single transaction.

        @param edges List of CouplingEdge to write
        """
        await self._write_edges_batch(
            edges,
            _COUPLING_EDGE_CYPHER,
            _coupling_edge_params,
        )

    async def clear_paper_claims(self, paper_slug: str) -> None:
        """Delete all claim nodes and their edges for a given paper.

        @param paper_slug Source paper slug to match
        """
        await self._client.execute_write(
            _CLEAR_CLAIMS_CYPHER, paper_slug=paper_slug,
        )

    async def clear_paper_provenances(self, arxiv_id: str) -> None:
        """Delete all provenance nodes and their edges for a given paper.

        @param arxiv_id ArXiv ID of the source paper
        """
        await self._client.execute_write(
            _CLEAR_PROVENANCES_CYPHER, arxiv_id=arxiv_id,
        )

    async def create_schema_constraints(self) -> None:
        """Run all CREATE CONSTRAINT and CREATE INDEX statements.

        Safe to call repeatedly — uses IF NOT EXISTS.
        """
        for stmt in _SCHEMA_STATEMENTS:
            await self._client.execute_write(stmt)

    async def _write_edges_batch(self, edges, cypher, param_fn) -> None:
        """Execute one Cypher statement per edge inside a single tx.

        @param edges List of edge models
        @param cypher Cypher template for the edge type
        @param param_fn Callable that converts an edge to a param dict
        """

        async def _tx(tx):
            for edge in edges:
                result = await tx.run(cypher, **param_fn(edge))
                await result.consume()

        await self._client.execute_write_tx(_tx)


# ---------------------------------------------------------------------------
# Parameter extraction helpers — keep Cypher params close to model fields
# ---------------------------------------------------------------------------


def _concept_params(c: ConceptNode) -> dict:
    """Extract Cypher parameters from a ConceptNode.

    @param c ConceptNode to extract from
    @returns Dict of Cypher parameters
    """
    return {
        "slug": c.slug,
        "name": c.name,
        "semantic_type": c.semantic_type,
        "rhetorical_origin": c.rhetorical_origin,
        "canonical_definition": c.canonical_definition,
        "formal_spec": c.formal_spec,
        "components": c.components,
        "ts_domain": c.ts_domain,
        "ts_codomain": c.ts_codomain,
        "ts_applies_to": c.ts_applies_to,
        "ts_member_type": c.ts_member_type,
        "ts_objective": c.ts_objective,
        "aliases": c.aliases,
        "status": c.status,
        "embedding": c.embedding,
        "human_notes": c.human_notes,
    }


def _claim_params(cl: ClaimNode, source_arxiv_id: str) -> dict:
    """Extract Cypher parameters from a ClaimNode.

    @param cl ClaimNode to extract from
    @param source_arxiv_id ArXiv ID for the SOURCED_FROM edge
    @returns Dict of Cypher parameters
    """
    return {
        "slug": cl.slug,
        "source_paper_slug": cl.source_paper_slug,
        "label": cl.label,
        "name": cl.name,
        "claim_type": cl.claim_type,
        "assumptions": cl.assumptions,
        "conclusion": cl.conclusion,
        "proof_technique": cl.proof_technique,
        "strength": cl.strength,
        "statement": cl.statement,
        "proof": cl.proof,
        "section": cl.section,
        "status": cl.status,
        "human_notes": cl.human_notes,
        "source_arxiv_id": source_arxiv_id,
    }


def _provenance_params(p: ProvenanceNode, fe: FormulationEdge) -> dict:
    """Extract Cypher parameters from a ProvenanceNode and FormulationEdge.

    @param p ProvenanceNode to extract from
    @param fe FormulationEdge with match metadata
    @returns Dict of Cypher parameters
    """
    return {
        "concept_slug": p.concept_slug,
        "source_arxiv_id": p.source_arxiv_id,
        "formulation": p.formulation,
        "formal_spec": p.formal_spec,
        "section": p.section,
        "extraction_confidence": p.extraction_confidence,
        "match_method": fe.match_method,
        "match_confidence": fe.match_confidence,
    }


def _source_params(s: SourceNode) -> dict:
    """Extract Cypher parameters from a SourceNode.

    @param s SourceNode to extract from
    @returns Dict of Cypher parameters
    """
    return {
        "arxiv_id": s.arxiv_id,
        "title": s.title,
        "authors": s.authors,
        "date_published": s.date_published,
        "date_extracted": s.date_extracted,
        "human_notes": s.human_notes,
    }


def _concept_edge_params(e: ConceptEdge) -> dict:
    """Extract Cypher parameters from a ConceptEdge.

    @param e ConceptEdge to extract from
    @returns Dict of Cypher parameters
    """
    return {
        "source_slug": e.source_slug,
        "target_slug": e.target_slug,
        "edge_type": e.edge_type,
        "attributes": e.attributes,
    }


def _claim_edge_params(e: ClaimEdge) -> dict:
    """Extract Cypher parameters from a ClaimEdge.

    @param e ClaimEdge to extract from
    @returns Dict of Cypher parameters
    """
    return {
        "source_slug": e.source_slug,
        "target_slug": e.target_slug,
        "edge_type": e.edge_type,
        "attributes": e.attributes,
    }


def _coupling_edge_params(e: CouplingEdge) -> dict:
    """Extract Cypher parameters from a CouplingEdge.

    @param e CouplingEdge to extract from
    @returns Dict of Cypher parameters
    """
    return {
        "claim_slug": e.claim_slug,
        "concept_slug": e.concept_slug,
        "role": e.role,
        "aspect": e.aspect,
    }
