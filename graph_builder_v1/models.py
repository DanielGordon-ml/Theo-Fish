"""
@file models.py
@description Pydantic models for the knowledge graph builder pipeline.
"""

from enum import Enum

from pydantic import BaseModel


class EntityType(str, Enum):
    """Mathematical entity types extracted from papers."""

    DEFINITION = "definition"
    THEOREM = "theorem"
    LEMMA = "lemma"
    PROPOSITION = "proposition"
    COROLLARY = "corollary"
    REMARK = "remark"
    EXAMPLE = "example"
    EXERCISE = "exercise"
    ALGORITHM = "algorithm"
    CONJECTURE = "conjecture"
    NOTATION = "notation"


class RelationshipType(str, Enum):
    """Semantic relationship types between entities."""

    USES = "uses"
    GENERALIZES = "generalizes"
    IS_SPECIAL_CASE_OF = "is-special-case-of"
    CONTRADICTS = "contradicts"
    IMPLIES = "implies"
    MOTIVATES = "motivates"
    IS_PROVED_BY = "is-proved-by"
    EXTENDS = "extends"
    IS_EQUIVALENT_TO = "is-equivalent-to"
    DEPENDS_ON = "depends-on"
    REFINES = "refines"
    IS_EXAMPLE_OF = "is-example-of"


class Section(BaseModel):
    """A chunked section of a paper for LLM processing."""

    heading: str
    level: int
    content: str
    char_count: int
    index: int


class ExtractedEntity(BaseModel):
    """A single mathematical entity extracted from a paper section."""

    entity_type: EntityType
    label: str
    statement: str
    proof: str | None = None
    section: str
    section_index: int
    context: str


class Relationship(BaseModel):
    """A directed semantic edge between two entities."""

    source_label: str
    target_label: str
    relationship_type: RelationshipType
    evidence: str


class PaperGraph(BaseModel):
    """Full extraction result for a single paper."""

    arxiv_id: str
    title: str
    entities: list[ExtractedEntity]
    relationships: list[Relationship]
    total_input_tokens: int
    total_output_tokens: int


class VaultFile(BaseModel):
    """An Obsidian markdown file to write."""

    relative_path: str
    frontmatter: dict
    body: str


class CrossPaperLink(BaseModel):
    """A link connecting entities across different papers."""

    source_paper: str
    source_entity: str
    target_paper: str
    target_entity: str
    confidence: float


class BuildResult(BaseModel):
    """Result of building a knowledge graph for a single paper."""

    arxiv_id: str
    status: str  # "built", "skipped", "failed"
    entity_count: int = 0
    relationship_count: int = 0
    error: str | None = None


class BatchBuildResult(BaseModel):
    """Aggregate result of building graphs for a batch of papers."""

    total: int
    built: int
    skipped: int
    failed: int
    results: list[BuildResult]
