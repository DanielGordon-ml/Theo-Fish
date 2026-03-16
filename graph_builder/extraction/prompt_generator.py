"""
@file prompt_generator.py
@description Schema-driven system prompt builder for all extraction passes.
Reads a GraphSchema and dynamically constructs structured prompts for concept
extraction, claim extraction, edge enrichment, and gap-fill passes.
"""

from graph_builder.config.schema_types import GraphSchema, ConceptTypeDef, ClaimTypeDef

_JSON_FENCE = "```json"
_FENCE_END = "```"


def build_concept_prompt(schema: GraphSchema) -> str:
    """Build a system prompt for Pass 1: concept extraction.

    Lists all concept types with descriptions and required/optional fields.
    Instructs the model to extract mathematical objects, not claims.
    Output: JSON {"concepts": [...]}.

    @param schema The loaded GraphSchema.
    @return A structured system prompt string.
    """
    lines = [
        "You are a mathematical concept extractor for research papers.",
        "Extract OBJECTS (concepts, structures, spaces) — not claims or theorems.",
        "",
        "## Concept Types",
        "",
    ]
    for name, defn in schema.concept_types.items():
        lines.extend(_format_concept_type(name, defn))

    lines.extend(_concept_output_format())
    return "\n".join(lines)


def _format_concept_type(name: str, defn: ConceptTypeDef) -> list[str]:
    """Format a single concept type block for the prompt."""
    block = [
        f"### {name}",
        f"Description: {defn.description}",
        f"Required fields: {', '.join(defn.required_fields)}",
    ]
    if defn.optional_fields:
        block.append(f"Optional fields: {', '.join(defn.optional_fields)}")
    block.append("")
    return block


def _concept_output_format() -> list[str]:
    """Return the output format instructions for concept extraction."""
    return [
        "## Output Format",
        "Return ONLY valid JSON:",
        _JSON_FENCE,
        '{"concepts": [{"semantic_type": "<one of the types above>", "name": "<name>", '
        '"formal_spec": "<spec>", "...other fields": "..."}]}',
        _FENCE_END,
        "",
        "Rules:",
        "- Only extract types listed above.",
        "- Do NOT extract theorems, lemmas, or proofs.",
        "- Include all required fields. Omit optional fields if absent.",
    ]


def build_claim_prompt(
    schema: GraphSchema,
    concept_list: list[dict] | None = None,
) -> str:
    """Build a system prompt for Pass 2: claim extraction.

    Lists all claim types with required/optional fields. If concept_list is
    provided, injects concept names, slugs, and types for grounding.
    Output: JSON {"claims": [...]}.

    @param schema The loaded GraphSchema.
    @param concept_list Optional list of concept dicts with name/slug/type keys.
    @return A structured system prompt string.
    """
    lines = [
        "You are a mathematical claim extractor for research papers.",
        "Extract ASSERTIONS (theorems, lemmas, proofs) — not objects or definitions.",
        "",
        "## Claim Types",
        "",
    ]
    for name, defn in schema.claim_types.items():
        lines.extend(_format_claim_type(name, defn))

    if concept_list:
        lines.extend(_format_concept_grounding(concept_list))

    lines.extend(_claim_output_format())
    return "\n".join(lines)


def _format_claim_type(name: str, defn: ClaimTypeDef) -> list[str]:
    """Format a single claim type block for the prompt."""
    block = [
        f"### {name}",
        f"Description: {defn.description}",
        f"Required fields: {', '.join(defn.required_fields)}",
    ]
    if defn.optional_fields:
        block.append(f"Optional fields: {', '.join(defn.optional_fields)}")
    block.append("")
    return block


def _format_concept_grounding(concept_list: list[dict]) -> list[str]:
    """Format a grounding section listing known concepts for reference."""
    lines = [
        "## Known Concepts (for grounding)",
        "When referencing concepts, use these slugs:",
        "",
    ]
    for c in concept_list:
        lines.append(f"- {c.get('name', '')} (slug: {c.get('slug', '')}, type: {c.get('type', '')})")
    lines.append("")
    return lines


def _claim_output_format() -> list[str]:
    """Return the output format instructions for claim extraction."""
    return [
        "## Output Format",
        "Return ONLY valid JSON:",
        _JSON_FENCE,
        '{"claims": [{"claim_type": "<one of the types above>", "label": "<e.g. Theorem 1.1>", '
        '"statement": "<full statement>", "assumptions": ["..."], "conclusion": "<...>", '
        '"about_concepts": ["<concept_slug_1>", "<concept_slug_2>"]}]}',
        _FENCE_END,
        "",
        "Rules:",
        "- Only extract types listed above.",
        "- Do NOT extract concept definitions or structures.",
        "- Every claim must reference at least one concept by slug.",
    ]


def build_edge_enrichment_prompt(schema: GraphSchema) -> str:
    """Build a system prompt for Pass 3a: section-batched edge enrichment.

    Lists claim edge types and coupling edges with their attributes.
    Instructs the model to extract edges with conditional attributes.
    Output: JSON {"edges": [...]}.

    @param schema The loaded GraphSchema.
    @return A structured system prompt string.
    """
    lines = [
        "You are a mathematical relationship extractor.",
        "Extract edges between claims and concepts with their attributes.",
        "",
        "## Claim-to-Claim Edge Types",
        "",
    ]
    for name, defn in schema.edges.claim_edges.items():
        lines.extend(_format_edge_type(name, defn))

    lines += [
        "## Coupling Edge Types (Claim → Concept)",
        "",
    ]
    for name, defn in schema.edges.coupling_edges.items():
        lines.extend(_format_edge_type(name, defn))

    lines.extend(_edge_output_format())
    return "\n".join(lines)


def _format_edge_type(name: str, defn) -> list[str]:
    """Format a single edge type block for the prompt."""
    block = [
        f"### {name}",
        f"Description: {defn.description}",
    ]
    if defn.attributes:
        block.append(f"Attributes: {', '.join(defn.attributes)}")
    block.append("")
    return block


def _edge_output_format() -> list[str]:
    """Return the output format instructions for edge enrichment."""
    return [
        "## Output Format",
        "Return ONLY valid JSON:",
        _JSON_FENCE,
        '{"edges": [{"type": "<edge_type>", "source": "<slug>", '
        '"target": "<slug>", "attributes": {"<attr>": "<value>"}}]}',
        _FENCE_END,
        "",
        "Rules:",
        "- Only use edge types listed above.",
        "- Include conditional attributes only when evidence exists.",
        "- Use slugs (not names) for source and target.",
    ]


def build_gap_fill_prompt(schema: GraphSchema) -> str:
    """Build a system prompt for Pass 3b: cross-section gap-fill.

    Instructs the model to find only cross-section implicit dependencies
    that were not captured within individual section passes.
    Output: JSON {"edges": [...]}.

    @param schema The loaded GraphSchema.
    @return A structured system prompt string.
    """
    claim_edge_names = ", ".join(schema.edges.claim_edges.keys())
    lines = [
        "You are a mathematical gap-fill extractor.",
        "Your task: find ONLY cross-section implicit dependencies.",
        "Do NOT re-extract edges already found within individual sections.",
        "",
        "## What to Look For",
        "- Claims in one section that implicitly depend on claims in another section.",
        "- Missing 'depends_on', 'enables', or 'equivalent_to' edges across sections.",
        "- Implicit logical dependencies not stated explicitly in any single section.",
        "",
        f"## Allowed Edge Types (gap-fill only): {claim_edge_names}",
        "",
        "## Output Format",
        "Return ONLY valid JSON:",
        _JSON_FENCE,
        '{"edges": [{"type": "<edge_type>", "source": "<slug>", '
        '"target": "<slug>", "cross_section": true, '
        '"evidence": "<quote or reasoning>"}]}',
        _FENCE_END,
        "",
        "Rules:",
        "- Only add edges where source and target are in DIFFERENT sections.",
        "- Only include edges with clear textual or logical evidence.",
        "- Skip edges already present in the per-section edge graph.",
    ]
    return "\n".join(lines)
