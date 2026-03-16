"""
@file entity_extractor.py
@description Per-section LLM extraction with deduplication and proof attachment.
"""

import asyncio
import json
import logging
import re

from graph_builder.config import SECTION_TIMEOUT_SECONDS
from graph_builder.llm_client import DeepSeekClient, LLMResponse
from graph_builder.logger import log_progress
from graph_builder.models import EntityType, ExtractedEntity, Section
from graph_builder.prompts import (
    ENTITY_EXTRACTION_SYSTEM,
    format_entity_extraction_prompt,
)

logger = logging.getLogger("graph_builder")

# Matches headings like "Proof of Theorem 2.1"
_PROOF_HEADING_RE = re.compile(
    r"^Proof\s+of\s+(.+)$", re.IGNORECASE,
)


def parse_entities_response(
    response: LLMResponse, section: Section,
) -> list[ExtractedEntity]:
    """Parse LLM JSON response into ExtractedEntity objects.

    @param response LLM response with JSON content
    @param section The source section for metadata
    """
    try:
        data = json.loads(response.content)
    except (json.JSONDecodeError, TypeError):
        logger.warning(
            "Malformed JSON from LLM: %s", response.content[:200],
            extra={"arxiv_id": "parse"},
        )
        return []

    raw_entities = data.get("entities", [])
    entities: list[ExtractedEntity] = []

    for raw in raw_entities:
        try:
            entity = _build_entity(raw, section)
            entities.append(entity)
        except (KeyError, ValueError):
            continue

    return entities


def _build_entity(raw: dict, section: Section) -> ExtractedEntity:
    """Build an ExtractedEntity from a raw dict and section metadata."""
    return ExtractedEntity(
        entity_type=EntityType(raw["entity_type"]),
        label=raw["label"],
        statement=raw["statement"],
        proof=raw.get("proof"),
        section=section.heading,
        section_index=section.index,
        context=raw.get("context", ""),
    )


def deduplicate_entities(
    entities: list[ExtractedEntity],
) -> list[ExtractedEntity]:
    """Remove duplicate entities, keeping the one with the longest statement.

    Deduplicates by (entity_type, label) key.
    """
    best: dict[tuple, ExtractedEntity] = {}

    for entity in entities:
        key = (entity.entity_type, entity.label)
        existing = best.get(key)
        if existing is None or len(entity.statement) > len(existing.statement):
            best[key] = entity

    return list(best.values())


def attach_orphan_proofs(
    entities: list[ExtractedEntity],
    sections: list[Section],
) -> list[ExtractedEntity]:
    """Attach orphan proof sections to their matching entities.

    Looks for sections with headings like 'Proof of Theorem X.Y' and
    attaches the content to the matching entity if it has no proof.
    """
    # Build label lookup
    label_map: dict[str, int] = {}
    for i, entity in enumerate(entities):
        label_map[entity.label.lower()] = i

    for section in sections:
        match = _PROOF_HEADING_RE.match(section.heading)
        if match is None:
            continue

        target_label = match.group(1).strip().lower()
        idx = label_map.get(target_label)
        if idx is None:
            continue

        # Only attach if entity has no existing proof
        if entities[idx].proof is not None:
            continue

        entities[idx] = entities[idx].model_copy(
            update={"proof": section.content},
        )

    return entities


async def _extract_section(
    client: DeepSeekClient, section: Section,
) -> tuple[list[ExtractedEntity], int, int]:
    """Extract entities from a single section via LLM."""
    user_prompt = format_entity_extraction_prompt(
        heading=section.heading, content=section.content,
    )
    response = await asyncio.wait_for(
        client.call(ENTITY_EXTRACTION_SYSTEM, user_prompt),
        timeout=SECTION_TIMEOUT_SECONDS,
    )
    entities = parse_entities_response(response, section)
    return entities, response.input_tokens, response.output_tokens


async def extract_entities(
    client: DeepSeekClient, sections: list[Section],
) -> tuple[list[ExtractedEntity], dict[str, int]]:
    """Extract entities from all sections with dedup and proof attachment.

    @param client DeepSeek LLM client
    @param sections Sections to process
    @returns Tuple of (deduplicated entities, token usage dict)
    """
    if not sections:
        return [], {"input": 0, "output": 0}

    tasks = [_extract_section(client, s) for s in sections]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    all_entities: list[ExtractedEntity] = []
    total_input = 0
    total_output = 0

    for i, result in enumerate(results):
        if isinstance(result, Exception):
            logger.warning(
                "Section extraction failed: %s", str(result),
                extra={"arxiv_id": "extract"},
            )
            continue
        entities, inp, out = result
        all_entities.extend(entities)
        total_input += inp
        total_output += out
        log_progress(f"    Section {i + 1}/{len(sections)} done")

    deduped = deduplicate_entities(all_entities)
    deduped = attach_orphan_proofs(deduped, sections)

    return deduped, {"input": total_input, "output": total_output}
