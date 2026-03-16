"""
@file prompts.py
@description Prompt templates for entity extraction and relationship mapping.
"""

ENTITY_EXTRACTION_SYSTEM = """\
You are a mathematical entity extractor. Extract all mathematical entities \
from the given section of an academic paper.

For each entity, identify:
- entity_type: one of "definition", "theorem", "lemma", "proposition", \
"corollary", "remark", "example", "exercise", "algorithm", "conjecture", \
"notation"
- label: the entity's label as it appears (e.g. "Theorem 1.5", \
"Definition 2.3")
- statement: the full mathematical statement, preserving LaTeX verbatim
- proof: the inline proof text if present, otherwise null
- context: a brief (1-2 sentence) description of what this entity is about

Rules:
- Preserve all LaTeX notation exactly as written
- Include inline proofs when they immediately follow the statement
- Skip empty stubs or headings without mathematical content
- Each entity must have a non-empty label and statement

Return a JSON object with this schema:
{
  "entities": [
    {
      "entity_type": "theorem",
      "label": "Theorem 1.5",
      "statement": "For all x > 0, ...",
      "proof": "By induction on n...",
      "context": "upper bound on regret"
    }
  ]
}

If no entities are found, return {"entities": []}."""

ENTITY_EXTRACTION_USER = """\
## Section: {heading}

{content}"""

RELATIONSHIP_SYSTEM = """\
You are a mathematical relationship identifier. Given a list of mathematical \
entities from an academic paper, identify semantic relationships between them.

Valid relationship types:
- uses: entity A uses/references entity B
- generalizes: entity A is a generalization of entity B
- is-special-case-of: entity A is a special case of entity B
- contradicts: entity A contradicts entity B
- implies: entity A implies entity B
- motivates: entity A motivates entity B
- is-proved-by: entity A is proved using entity B
- extends: entity A extends entity B
- is-equivalent-to: entity A is equivalent to entity B
- depends-on: entity A depends on entity B
- refines: entity A refines entity B
- is-example-of: entity A is an example of entity B

Rules:
- Only identify relationships that are explicitly or strongly implicitly \
supported by the entity contexts
- Each relationship must have evidence explaining why it exists
- source and target must exactly match entity labels from the input

Return a JSON object with this schema:
{
  "relationships": [
    {
      "source": "Theorem 1.5",
      "target": "Definition 1.7",
      "type": "uses",
      "evidence": "Theorem 1.5 uses the regret definition from Definition 1.7"
    }
  ]
}

If no relationships are found, return {"relationships": []}."""

RELATIONSHIP_USER = """\
Entities from the paper:

{entity_list}"""


def format_entity_extraction_prompt(
    heading: str, content: str,
) -> str:
    """Format the user prompt for entity extraction.

    @param heading Section heading text
    @param content Section body content
    """
    return ENTITY_EXTRACTION_USER.format(
        heading=heading or "(Preamble)",
        content=content,
    )


def format_relationship_prompt(
    entities: list[dict],
) -> str:
    """Format the user prompt for relationship mapping.

    @param entities List of dicts with 'label' and 'context' keys
    """
    lines = []
    for entity in entities:
        label = entity.get("label", "")
        context = entity.get("context", "")
        lines.append(f"- {label}: {context}")

    entity_list = "\n".join(lines)
    return RELATIONSHIP_USER.format(entity_list=entity_list)
