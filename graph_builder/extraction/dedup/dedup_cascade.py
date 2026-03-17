"""
@file dedup_cascade.py
@description Orchestrates the full concept deduplication cascade:
alias match -> embedding similarity -> LLM confirmation.
"""

import json
import logging
from dataclasses import dataclass, field

from graph_builder.config.config import (
    DEDUP_AUTO_THRESHOLD,
    DEDUP_FLAG_THRESHOLD,
    DEDUP_SHORTLIST_SIZE,
)
from graph_builder.extraction.dedup.embedding_client import EmbeddingClient
from graph_builder.graph.graph_reader import GraphReader
from graph_builder.llm.llm_client import DeepSeekClient
from graph_builder.models.concept import ConceptNode

logger = logging.getLogger("graph_builder")

_LLM_SYSTEM_PROMPT = (
    "You are a mathematics ontology expert. "
    "Determine whether two concept names refer to the same mathematical concept. "
    'Reply only with JSON: {"is_same_concept": true} or {"is_same_concept": false}.'
)


@dataclass
class DedupResult:
    """Result of deduplicating a single concept."""

    slug: str
    is_new: bool
    match_method: str  # "new" | "alias" | "embedding" | "embedding+llm"
    match_confidence: float
    existing_slug: str | None = field(default=None)


async def run_dedup_cascade(
    concept: ConceptNode,
    graph_reader: GraphReader,
    embedding_client: EmbeddingClient,
    llm_client: DeepSeekClient | None = None,
) -> DedupResult:
    """Run the full dedup cascade for a single concept.

    Steps:
    1. Exact alias match against existing concept slugs
    2. Embedding vector similarity search
    3. LLM confirmation for moderate similarity scores

    @param concept The new concept to deduplicate
    @param graph_reader Read access to the graph
    @param embedding_client Embedding API wrapper
    @param llm_client Optional LLM for ambiguous cases
    @returns DedupResult describing how the concept was resolved
    """
    existing_slugs = await graph_reader.get_all_concept_slugs()

    alias_result = await _check_alias_match(concept, existing_slugs, graph_reader)
    if alias_result is not None:
        return alias_result

    return await _run_embedding_cascade(
        concept,
        graph_reader,
        embedding_client,
        llm_client,
    )


async def _check_alias_match(
    concept: ConceptNode,
    existing_slugs: list[str],
    graph_reader: GraphReader,
) -> DedupResult | None:
    """Check if the concept slug matches any alias of an existing concept.

    @param concept Incoming concept
    @param existing_slugs All slugs currently in the graph
    @param graph_reader Graph read access
    @returns DedupResult if alias match found, None otherwise
    """
    for slug in existing_slugs:
        existing = await graph_reader.get_existing_concept(slug)
        if existing is None:
            continue
        if concept.slug in existing.aliases:
            return DedupResult(
                slug=concept.slug,
                is_new=False,
                match_method="alias",
                match_confidence=1.0,
                existing_slug=slug,
            )
    return None


async def _run_embedding_cascade(
    concept: ConceptNode,
    graph_reader: GraphReader,
    embedding_client: EmbeddingClient,
    llm_client: DeepSeekClient | None,
) -> DedupResult:
    """Run embedding search and optional LLM confirmation.

    @param concept Incoming concept
    @param graph_reader Graph read access
    @param embedding_client Embedding API wrapper
    @param llm_client Optional LLM for confirmation
    @returns DedupResult from embedding or LLM step
    """
    embedding = await embedding_client.embed_single(concept.name)
    matches = await graph_reader.vector_similarity_search(
        embedding,
        top_k=DEDUP_SHORTLIST_SIZE,
    )

    if not matches:
        return _new_result(concept)

    best_slug, best_score = matches[0]

    if best_score >= DEDUP_AUTO_THRESHOLD:
        return DedupResult(
            slug=concept.slug,
            is_new=False,
            match_method="embedding",
            match_confidence=best_score,
            existing_slug=best_slug,
        )

    if best_score >= DEDUP_FLAG_THRESHOLD:
        return await _confirm_with_llm(concept, best_slug, best_score, llm_client)

    return _new_result(concept)


async def _confirm_with_llm(
    concept: ConceptNode,
    candidate_slug: str,
    score: float,
    llm_client: DeepSeekClient | None,
) -> DedupResult:
    """Ask the LLM to confirm whether two concepts are the same.

    Falls back to a new concept if llm_client is None or raises.

    @param concept Incoming concept
    @param candidate_slug Slug of the candidate existing concept
    @param score Embedding similarity score
    @param llm_client Optional LLM client
    @returns DedupResult with method "embedding+llm" or "new"
    """
    if llm_client is None:
        return _new_result(concept)

    user_prompt = (
        f'Concept A: "{concept.name}"\n'
        f'Concept B slug: "{candidate_slug}"\n'
        "Are these the same mathematical concept?"
    )

    try:
        response = await llm_client.call(_LLM_SYSTEM_PROMPT, user_prompt)
        parsed = json.loads(response.content)
        is_same = bool(parsed.get("is_same_concept", False))
    except Exception as exc:
        logger.warning(
            "LLM dedup confirmation failed for '%s' vs '%s': %s",
            concept.slug,
            candidate_slug,
            exc,
        )
        return _new_result(concept)

    if is_same:
        return DedupResult(
            slug=concept.slug,
            is_new=False,
            match_method="embedding+llm",
            match_confidence=score,
            existing_slug=candidate_slug,
        )
    return _new_result(concept)


def _new_result(concept: ConceptNode) -> DedupResult:
    """Build a DedupResult representing a brand-new concept.

    @param concept The concept being registered as new
    @returns DedupResult with is_new=True
    """
    return DedupResult(
        slug=concept.slug,
        is_new=True,
        match_method="new",
        match_confidence=0.0,
        existing_slug=None,
    )
