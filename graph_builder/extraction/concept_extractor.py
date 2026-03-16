"""
@file concept_extractor.py
@description Per-section concept extractor: builds prompts, calls the LLM,
parses the response, and stamps section provenance onto each ConceptNode.
"""

import logging

from graph_builder.config.schema_types import GraphSchema
from graph_builder.extraction.prompt_generator import build_concept_prompt
from graph_builder.llm.protocol import LLMClient
from graph_builder.llm.response_parser import parse_concepts
from graph_builder.models.concept import ConceptNode
from graph_builder.models.section import Section

logger = logging.getLogger("graph_builder")

# Header text prefixed to the existing-concept shortlist block
_KNOWN_CONCEPTS_HEADER = (
    "Known concepts (use exact names if this concept matches):"
)


async def extract_concepts_from_section(
    section: Section,
    schema: GraphSchema,
    llm_client: LLMClient,
    existing_concepts: list[dict] | None = None,
) -> list[ConceptNode]:
    """Extract concept nodes from a single paper section via the LLM.

    Builds a schema-driven system prompt and a user prompt embedding the
    section content. If existing_concepts is provided, a shortlist of known
    slugs and types is appended to the user prompt to improve grounding.
    Each returned ConceptNode has its rhetorical_origin set to the section
    heading.

    @param section The paper section to process.
    @param schema The GraphSchema used to build prompts and validate output.
    @param llm_client Async LLM client for the extraction call.
    @param existing_concepts Optional list of known concept dicts with
        ``slug`` and ``semantic_type`` keys.
    @returns List of validated ConceptNode objects, empty on LLM failure.
    """
    system_prompt = build_concept_prompt(schema)
    user_prompt = _build_user_prompt(section, existing_concepts)

    try:
        response = await llm_client.call(system_prompt, user_prompt)
    except Exception as err:
        logger.error(
            "LLM call failed for section '%s': %s",
            section.heading,
            err,
        )
        return []

    concepts = parse_concepts(response.content, schema)
    return _stamp_provenance(concepts, section.heading)


def _build_user_prompt(
    section: Section,
    existing_concepts: list[dict] | None,
) -> str:
    """Compose the user-facing extraction prompt for one section.

    @param section The section whose content to embed.
    @param existing_concepts Optional known-concept shortlist for grounding.
    @returns A formatted user prompt string.
    """
    parts = [section.content]
    if existing_concepts:
        parts.append("")
        parts.append(_KNOWN_CONCEPTS_HEADER)
        parts.extend(_format_concept_shortlist(existing_concepts))
    return "\n".join(parts)


def _format_concept_shortlist(concepts: list[dict]) -> list[str]:
    """Format each known concept as a bullet line for prompt injection.

    @param concepts List of dicts with ``slug`` and ``semantic_type`` keys.
    @returns List of formatted bullet strings.
    """
    lines = []
    for c in concepts:
        slug = c.get("slug", "")
        sem_type = c.get("semantic_type", "")
        lines.append(f"- {slug} ({sem_type})")
    return lines


def _stamp_provenance(
    concepts: list[ConceptNode],
    heading: str,
) -> list[ConceptNode]:
    """Set rhetorical_origin to the section heading on each ConceptNode.

    @param concepts Parsed ConceptNode list.
    @param heading The section heading used as provenance.
    @returns The same list with rhetorical_origin mutated in place.
    """
    for concept in concepts:
        concept.rhetorical_origin = heading
    return concepts
