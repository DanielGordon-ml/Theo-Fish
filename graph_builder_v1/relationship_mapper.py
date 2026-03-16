"""
@file relationship_mapper.py
@description Intra-paper relationship mapping and cross-paper label matching.
"""

import json
import logging

from graph_builder.llm_client import DeepSeekClient, LLMResponse
from graph_builder.models import (
    CrossPaperLink,
    ExtractedEntity,
    Relationship,
    RelationshipType,
)
from graph_builder.prompts import (
    RELATIONSHIP_SYSTEM,
    format_relationship_prompt,
)

logger = logging.getLogger("graph_builder")


def parse_relationships_response(
    response: LLMResponse,
) -> list[Relationship]:
    """Parse LLM JSON response into Relationship objects.

    @param response LLM response with JSON content
    """
    try:
        data = json.loads(response.content)
    except (json.JSONDecodeError, TypeError):
        logger.warning(
            "Malformed relationship JSON: %s", response.content[:200],
            extra={"arxiv_id": "parse"},
        )
        return []

    raw_rels = data.get("relationships", [])
    relationships: list[Relationship] = []

    for raw in raw_rels:
        try:
            rel = _build_relationship(raw)
            relationships.append(rel)
        except (KeyError, ValueError):
            continue

    return relationships


def _build_relationship(raw: dict) -> Relationship:
    """Build a Relationship from a raw dict."""
    return Relationship(
        source_label=raw["source"],
        target_label=raw["target"],
        relationship_type=RelationshipType(raw["type"]),
        evidence=raw.get("evidence", ""),
    )


def validate_relationships(
    relationships: list[Relationship],
    entities: list[ExtractedEntity],
) -> list[Relationship]:
    """Remove relationships that reference non-existent entity labels.

    @param relationships Relationships to validate
    @param entities Known entities to validate against
    """
    valid_labels = {e.label for e in entities}
    return [
        r for r in relationships
        if r.source_label in valid_labels and r.target_label in valid_labels
    ]


def find_cross_paper_links(
    entities: list[ExtractedEntity],
    current_arxiv_id: str,
    vault_labels: dict[str, list[tuple[str, str]]],
) -> list[CrossPaperLink]:
    """Find cross-paper links by matching entity labels against vault index.

    @param entities Entities from the current paper
    @param current_arxiv_id ArXiv ID of the current paper
    @param vault_labels Normalized label -> [(paper_title, arxiv_id)] map
    """
    links: list[CrossPaperLink] = []

    for entity in entities:
        normalized = entity.label.lower()
        matches = vault_labels.get(normalized, [])

        for paper_title, arxiv_id in matches:
            # Skip self-references
            if arxiv_id == current_arxiv_id:
                continue
            links.append(CrossPaperLink(
                source_paper=current_arxiv_id,
                source_entity=entity.label,
                target_paper=arxiv_id,
                target_entity=entity.label,
                confidence=1.0,
            ))

    return links


async def map_relationships(
    client: DeepSeekClient,
    entities: list[ExtractedEntity],
) -> tuple[list[Relationship], dict[str, int]]:
    """Identify relationships between entities via LLM.

    @param client DeepSeek LLM client
    @param entities Extracted entities to find relationships between
    @returns Tuple of (validated relationships, token usage dict)
    """
    if not entities:
        return [], {"input": 0, "output": 0}

    entity_summaries = [
        {"label": e.label, "context": e.context}
        for e in entities
    ]
    user_prompt = format_relationship_prompt(entity_summaries)
    response = await client.call(RELATIONSHIP_SYSTEM, user_prompt)

    relationships = parse_relationships_response(response)
    validated = validate_relationships(relationships, entities)

    tokens = {
        "input": response.input_tokens,
        "output": response.output_tokens,
    }
    return validated, tokens
