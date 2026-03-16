# Dual-Graph Knowledge Graph Builder — Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebuild the graph_builder module as a dual-graph architecture backed by Neo4j, replacing the star-graph v1 with a Concept Ontology (Graph A) + Reasoning Graph (Graph B) coupled by ABOUT edges, with an Obsidian vault exporter.

**Architecture:** Neo4j 5.26-community (Docker) is the source of truth. A schema-driven two-pass extraction pipeline (concepts → claims) writes to Neo4j with typed, attributed edges. An Obsidian exporter generates a browsable vault mirror with scoped sync-back for human curation. Implementation follows a 4-layer build order with a Layer 2 integration gate.

**Tech Stack:** Python 3.10+, Neo4j 5.26-community (Docker), DeepSeek V3.2 (OpenAI SDK), OpenAI text-embedding-3-small (1536d), pydantic, pytest, pytest-asyncio, neo4j (async driver), PyYAML, uv (package manager)

**Spec:** `docs/superpowers/specs/2026-03-16-dual-graph-kg-builder-design.md`

**Convention:** Every sub-module's `__init__.py` must export its public API after its implementation files are complete. Wire exports in the commit step of each task. Follow the pattern shown in Task 4 Step 6 (models/__init__.py).

---

## Chunk 1: Project Setup + Layer 1 (Config, Models, Shared)

### Task 1: Project Setup — Dependencies & Directory Scaffolding

**Files:**
- Modify: `pyproject.toml`
- Modify: `tests/conftest.py`
- Create: `docker-compose.yml`
- Create: `graph_builder/config/__init__.py`
- Create: `graph_builder/models/__init__.py`
- Create: `graph_builder/extraction/__init__.py`
- Create: `graph_builder/extraction/dedup/__init__.py`
- Create: `graph_builder/validation/__init__.py`
- Create: `graph_builder/graph/__init__.py`
- Create: `graph_builder/vault/__init__.py`
- Create: `graph_builder/llm/__init__.py`
- Create: `graph_builder/orchestrator/__init__.py`
- Create: `graph_builder/shared/__init__.py`
- Create: `data_vault/_meta/schema.yaml`
- Rename: `graph_builder/` → `graph_builder_v1/` (preserve v1)
- Create: new `graph_builder/` (v2 module root)

- [ ] **Step 1: Preserve v1 as graph_builder_v1**

```bash
cd C:/python_projects/bamf/Theo-Fish/ETL
cp -r graph_builder graph_builder_v1
```

- [ ] **Step 2: Clear graph_builder/ for v2 — keep only reusable files**

Remove all v1 files from `graph_builder/` except those being reused. Keep:
- `section_splitter.py` (reuse as-is)
- `logger.py` (reuse as-is)

Delete everything else from `graph_builder/`:
```bash
cd C:/python_projects/bamf/Theo-Fish/ETL/graph_builder
rm -f __init__.py __main__.py cli.py config.py entity_extractor.py errors.py llm_client.py models.py orchestrator.py prompts.py relationship_mapper.py sdk.py vault_scanner.py vault_writer.py
```

- [ ] **Step 3: Create sub-module directories**

```bash
cd C:/python_projects/bamf/Theo-Fish/ETL/graph_builder
mkdir -p config models extraction/dedup validation graph vault llm orchestrator shared
touch config/__init__.py models/__init__.py extraction/__init__.py extraction/dedup/__init__.py validation/__init__.py graph/__init__.py vault/__init__.py llm/__init__.py orchestrator/__init__.py shared/__init__.py
touch __init__.py __main__.py
```

- [ ] **Step 4: Add new dependencies to pyproject.toml**

Add to `[project] dependencies`:
```toml
"neo4j>=5.0",
"numpy>=1.24",
```

Add to `[project.optional-dependencies] dev`:
```toml
"testcontainers[neo4j]>=4.0",
```

Update `[tool.hatch.build.targets.wheel] packages` to include `graph_builder_v1`:
```toml
packages = ["data_loader", "data_cleaner", "graph_builder", "graph_builder_v1"]
```

Also add pytest markers to `pyproject.toml`:
```toml
[tool.pytest.ini_options]
markers = [
    "unit: no external dependencies",
    "integration: requires Neo4j Docker",
    "e2e: full pipeline smoke test",
    "slow: tests taking >10s",
]
asyncio_mode = "auto"
```

Run: `uv sync --all-extras`

- [ ] **Step 5a: Create docker-compose.yml for local Neo4j**

```yaml
version: "3.8"
services:
  neo4j:
    image: neo4j:5.26-community
    ports:
      - "7687:7687"  # Bolt
      - "7474:7474"  # Browser
    environment:
      NEO4J_AUTH: neo4j/password
      NEO4J_PLUGINS: '[]'
    volumes:
      - neo4j_data:/data

volumes:
  neo4j_data:
```

Start with: `docker compose up -d neo4j`

- [ ] **Step 5b: Write conftest.py Neo4j testcontainer fixture**

Add to `tests/conftest.py`:

```python
import asyncio
import pytest
from neo4j import AsyncGraphDatabase


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

    container = Neo4jContainer("neo4j:5.26-community")
    container.start()
    bolt_url = container.get_connection_url()
    yield {"url": bolt_url, "user": "neo4j", "password": "test"}
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
```

Create `data_vault/_meta/schema.yaml` with the full schema from spec Section 4. This is the pipeline-driving config file.

```yaml
# ═══════════════════════════════════════════
# Knowledge Graph Schema — Source of Truth
# ═══════════════════════════════════════════
# This file drives extraction prompts, validation, and vault export.
# To add a new edge type or node type, add it here. Pipeline picks it up.

version: "2.1"
last_updated: "2026-03-16"

concept_types:
  structure:
    description: "Named mathematical objects and constructions"
    examples: ["Markov Decision Process", "Nash Equilibrium", "policy"]
    required_fields: [name, formal_spec]
    optional_fields: [components, notation, parametrization]
  space:
    description: "Sets, domains, manifolds, topological spaces"
    examples: ["policy space", "state space", "simplex"]
    required_fields: [name, formal_spec]
    optional_fields: [dimensionality, topology, base_field]
  operator:
    description: "Functions, maps, transformations between spaces"
    examples: ["Bellman operator", "policy gradient", "projection"]
    required_fields: [name, domain, codomain]
    optional_fields: [formal_spec, linearity, continuity]
  property:
    description: "Attributes that structures or spaces can possess"
    examples: ["ergodicity", "convexity", "Lipschitz continuity"]
    required_fields: [name, applies_to]
    optional_fields: [formal_spec, negation]
  quantity:
    description: "Measurable or computable scalar/vector values"
    examples: ["expected return", "regret", "KL divergence"]
    required_fields: [name, formal_spec]
    optional_fields: [range, unit, computability]
  relation:
    description: "Named binary or n-ary relationships"
    examples: ["dominance", "Pareto optimality", "equivalence"]
    required_fields: [name, arity, formal_spec]
    optional_fields: [symmetry, transitivity, reflexivity]
  class:
    description: "Families or categories of structures"
    examples: ["potential games", "linear MDPs", "extensive-form games"]
    required_fields: [name, member_type]
    optional_fields: [formal_spec, defining_property]
  problem:
    description: "Named problems or tasks to be solved"
    examples: ["multi-armed bandit problem", "optimal stopping problem"]
    required_fields: [name, input_spec, objective]
    optional_fields: [formal_spec, hardness, known_solutions]
  criterion:
    description: "Objective functions, loss functions, optimality conditions"
    examples: ["expected regret minimization", "Nash social welfare"]
    required_fields: [name, formal_spec]
    optional_fields: [direction, domain, convexity]

claim_types:
  theorem:
    description: "Major proven result"
    required_fields: [name, assumptions, conclusion, proof_technique]
    optional_fields: [strength, tightness]
    strength_values: [exact, asymptotic, approximate, existential]
  lemma:
    description: "Supporting proven result used by other claims"
    required_fields: [name, assumptions, conclusion]
    optional_fields: [proof_technique, used_by]
  proposition:
    description: "Intermediate result, standalone but not central"
    required_fields: [name, assumptions, conclusion]
    optional_fields: [proof_technique]
  corollary:
    description: "Direct consequence of a theorem or proposition"
    required_fields: [name, conclusion, derived_from]
    optional_fields: [assumptions]
  conjecture:
    description: "Unproven claim"
    required_fields: [name, statement]
    optional_fields: [evidence_for, evidence_against, status]
    status_values: [open, partially_resolved, resolved, disproven]
  algorithm:
    description: "Procedural claim — this method achieves specified behavior"
    required_fields: [name, input_spec, output_spec, guarantee]
    optional_fields: [complexity, convergence_rate, assumptions]

edges:
  concept_edges:
    generalizes:
      inverse: specializes
      description: "Source is a more general form of target"
      attributes: [condition]
    specializes:
      inverse: generalizes
      description: "Source is a special case of target"
      attributes: [restriction]
    has_component:
      inverse: component_of
      description: "Target is a named part of source's definition"
      attributes: []
    instance_of:
      inverse: has_instance
      description: "Source is a concrete example of target"
      attributes: [parameters]
    dual_of:
      inverse: dual_of
      description: "Source and target are dual constructions"
      attributes: [duality_type]
    equipped_with:
      description: "Source space/structure carries target as additional structure"
      attributes: [compatibility_condition]
  claim_edges:
    depends_on:
      description: "Source claim's proof uses target claim"
      attributes: [role, applied_to]
      role_values: [existence_guarantee, bound, construction, base_case, inductive_step]
    enables:
      description: "Source claim makes target claim possible"
      attributes: [nature]
      nature_values: [constructive, existential, computational, relaxation]
    strengthens:
      inverse: weakens
      description: "Source tightens the bound or relaxes assumptions of target"
      attributes: [dimension]
      dimension_values: [tighter_bound, weaker_assumptions, broader_scope]
    weakens:
      inverse: strengthens
      description: "Source is a weaker version of target"
      attributes: [dimension]
    contradicts:
      description: "Source and target cannot both hold"
      attributes: [resolution]
    equivalent_to:
      description: "Source and target are logically equivalent"
      attributes: [under_assumptions]
  coupling_edges:
    about:
      description: "Claim concerns this concept"
      attributes: [role, aspect]
      role_values: [primary, scope, mechanism, bound_target, construction_input]
  provenance_edges:
    sourced_from:
      description: "Entity was extracted from this source"
      attributes: [section, page, confidence]
    formulation_of:
      description: "Provenance node records a per-paper formulation of a concept"
      attributes: [match_method, match_confidence]

validation:
  rules:
    - "every Claim node must have at least one 'about' edge"
    - "every Concept node must have at least one Provenance node linked via 'formulation_of'"
    - "'corollary' claims must have at least one 'depends_on' edge"
    - "'depends_on' edges must not form cycles"
    - "'generalizes' and 'specializes' must be consistent inverses"
    - "every edge type used must exist in this schema"
    - "every attribute used on an edge must be listed in that edge's attributes"
  severity:
    error: [missing_about, missing_provenance, unknown_edge_type, inconsistent_inverse]
    warning: [cycle_in_depends_on, missing_proof_technique, unknown_attribute, corollary_without_depends_on]
    info: [concept_with_single_source, claim_without_enables]

field_ownership:
  pipeline_owned:
    - slug
    - semantic_type
    - rhetorical_origin
    - formal_spec
    - components
    - ts_domain
    - ts_codomain
    - ts_applies_to
    - ts_member_type
    - ts_objective
    - type_specific_fields
    - source_paper_slug
    - label
    - claim_type
    - assumptions
    - conclusion
    - proof_technique
    - strength
    - statement
    - proof
    - section
    - embedding
    - arxiv_id
    - title
    - authors
    - date_published
    - date_extracted
    - date_modified
    - formulation
    - extraction_confidence
    - concept_slug
    - source_arxiv_id
  human_owned:
    - name  # on Concept only; on Claim it is pipeline-owned (same as label)
    - canonical_definition
    - human_notes
    - status  # on Claim only (verified/unverified/disputed)
  shared:
    - aliases
    - status  # on Concept only (canonical/review_needed/deprecated)
```

- [ ] **Step 6: Commit setup**

```bash
git add -A
git commit -m "chore(graph-builder): scaffold v2 dual-graph module structure

Preserve v1 as graph_builder_v1, create new module layout with
config/, models/, extraction/, dedup/, validation/, graph/, vault/,
llm/, orchestrator/, shared/ sub-modules. Add schema.yaml, neo4j
and testcontainers dependencies."
```

---

### Task 2: Shared Utilities — slugify.py + errors.py

**Files:**
- Create: `graph_builder/shared/slugify.py`
- Create: `graph_builder/shared/errors.py`
- Create: `tests/test_slugify.py`
- Create: `tests/test_graph_builder_v2_errors.py`

- [ ] **Step 1: Write test_slugify.py**

```python
"""
@file test_slugify.py
@description Tests for deterministic slug generation.
"""

import pytest

from graph_builder.shared.slugify import slugify


class TestSlugify:
    """Tests for the slugify function."""

    def test_basic_name(self):
        """It should convert a simple name to lowercase hyphenated slug."""
        assert slugify("Markov Decision Process") == "markov-decision-process"

    def test_latex_stripping(self):
        """It should strip LaTeX commands and convert to readable text."""
        assert slugify("$\\epsilon$-greedy") == "epsilon-greedy"

    def test_parenthetical_content(self):
        """It should handle parenthetical content."""
        assert slugify("KL Divergence (D_KL)") == "kl-divergence-d-kl"

    def test_consecutive_hyphens_collapsed(self):
        """It should collapse consecutive hyphens to single hyphen."""
        assert slugify("foo  --  bar") == "foo-bar"

    def test_leading_trailing_hyphens_stripped(self):
        """It should strip leading and trailing hyphens."""
        assert slugify(" -hello world- ") == "hello-world"

    def test_unicode_normalization(self):
        """It should normalize unicode characters."""
        assert slugify("Hölder continuity") == "holder-continuity"

    def test_deterministic(self):
        """It should produce the same slug for the same input every time."""
        name = "Nash Equilibrium"
        assert slugify(name) == slugify(name)

    def test_special_math_chars(self):
        """It should handle common math notation."""
        assert slugify("Q-function") == "q-function"
        assert slugify("α-regret") == "a-regret"

    def test_empty_string(self):
        """It should handle empty input."""
        assert slugify("") == ""

    def test_numbers_preserved(self):
        """It should preserve digits."""
        assert slugify("Theorem 4.1") == "theorem-4-1"
```

- [ ] **Step 2: Run test — verify it fails**

```bash
cd C:/python_projects/bamf/Theo-Fish/ETL
uv run pytest tests/test_slugify.py -v
```
Expected: FAIL — `ModuleNotFoundError: No module named 'graph_builder.shared.slugify'`

- [ ] **Step 3: Implement slugify.py**

```python
"""
@file slugify.py
@description Deterministic slug generation from canonical names.

The slugify algorithm is FROZEN after first production run.
Any changes require a migration script for all existing Neo4j slugs,
vault filenames, and wikilink references.
"""

import re
import unicodedata

# LaTeX command patterns to strip
_LATEX_CMD_RE = re.compile(r"\\[a-zA-Z]+\{([^}]*)\}")
_LATEX_DOLLAR_RE = re.compile(r"\$([^$]*)\$")
_LATEX_BACKSLASH_RE = re.compile(r"\\([a-zA-Z]+)")

# Greek letter map (common in math)
_GREEK_MAP = {
    "alpha": "a", "beta": "b", "gamma": "g", "delta": "d",
    "epsilon": "epsilon", "zeta": "z", "eta": "eta", "theta": "theta",
    "lambda": "lambda", "mu": "mu", "pi": "pi", "sigma": "sigma",
    "tau": "tau", "phi": "phi", "omega": "omega",
}


def slugify(name: str) -> str:
    """Convert a canonical name to a deterministic slug.

    Algorithm (frozen — do not modify without migration script):
    1. Strip LaTeX commands
    2. Unicode NFKD normalization, strip combining marks
    3. Lowercase
    4. Replace non-alphanumeric with hyphens
    5. Collapse consecutive hyphens
    6. Strip leading/trailing hyphens
    """
    if not name:
        return ""

    text = name
    # Strip LaTeX: $\epsilon$ -> epsilon
    text = _LATEX_DOLLAR_RE.sub(r"\1", text)
    text = _LATEX_CMD_RE.sub(r"\1", text)
    for cmd, replacement in _GREEK_MAP.items():
        text = text.replace(f"\\{cmd}", replacement)
    text = _LATEX_BACKSLASH_RE.sub(r"\1", text)

    # Unicode NFKD normalization
    text = unicodedata.normalize("NFKD", text)
    text = "".join(
        c for c in text if not unicodedata.combining(c)
    )

    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-{2,}", "-", text)
    text = text.strip("-")

    return text
```

- [ ] **Step 4: Run test — verify it passes**

```bash
uv run pytest tests/test_slugify.py -v
```
Expected: All 10 tests PASS

- [ ] **Step 5: Write test_graph_builder_v2_errors.py**

```python
"""
@file test_graph_builder_v2_errors.py
@description Tests for v2 error classes.
"""

from graph_builder.shared.errors import (
    GraphBuilderError,
    ValidationError,
    DedupConflictError,
)


class TestGraphBuilderError:
    def test_includes_arxiv_id_and_reason(self):
        err = GraphBuilderError("1904.07272", "extraction failed")
        assert "1904.07272" in str(err)
        assert "extraction failed" in str(err)
        assert err.arxiv_id == "1904.07272"

class TestValidationError:
    def test_includes_severity_and_rule(self):
        err = ValidationError("missing_about", "error", "Claim X has no ABOUT edge")
        assert err.rule == "missing_about"
        assert err.severity == "error"

class TestDedupConflictError:
    def test_includes_slugs(self):
        err = DedupConflictError("mdp", "markov-decision-process", 0.72)
        assert err.new_slug == "mdp"
        assert err.existing_slug == "markov-decision-process"
        assert err.similarity == 0.72
```

- [ ] **Step 6: Implement errors.py**

```python
"""
@file errors.py
@description Custom exceptions for the dual-graph knowledge graph builder.
"""


class GraphBuilderError(Exception):
    """Raised when graph building fails for a single paper."""

    def __init__(self, arxiv_id: str, reason: str):
        super().__init__(f"[{arxiv_id}] {reason}")
        self.arxiv_id = arxiv_id
        self.reason = reason


class ValidationError(Exception):
    """Raised when schema validation detects an issue."""

    def __init__(self, rule: str, severity: str, message: str):
        super().__init__(f"[{severity}] {rule}: {message}")
        self.rule = rule
        self.severity = severity


class DedupConflictError(Exception):
    """Raised when concept dedup finds an ambiguous match."""

    def __init__(
        self, new_slug: str, existing_slug: str, similarity: float,
    ):
        super().__init__(
            f"Ambiguous match: '{new_slug}' ↔ '{existing_slug}' "
            f"(similarity={similarity:.2f})"
        )
        self.new_slug = new_slug
        self.existing_slug = existing_slug
        self.similarity = similarity
```

- [ ] **Step 7: Run tests — verify passes**

```bash
uv run pytest tests/test_slugify.py tests/test_graph_builder_v2_errors.py -v
```
Expected: All PASS

- [ ] **Step 8: Commit**

```bash
git add graph_builder/shared/slugify.py graph_builder/shared/errors.py tests/test_slugify.py tests/test_graph_builder_v2_errors.py
git commit -m "feat(shared): add slugify and error classes for v2 dual-graph builder"
```

---

### Task 3: Schema Loader — config/schema_loader.py

**Files:**
- Create: `tests/test_schema_loader.py`
- Create: `graph_builder/config/schema_types.py`
- Create: `graph_builder/config/schema_loader.py`
- Create: `graph_builder/config/config.py`

- [ ] **Step 1: Write test_schema_loader.py**

```python
"""
@file test_schema_loader.py
@description Tests for YAML schema loading and validation.
"""

import pytest
from pathlib import Path

from graph_builder.config.schema_loader import load_schema
from graph_builder.config.schema_types import (
    GraphSchema,
    ConceptTypeDef,
    ClaimTypeDef,
    EdgeDef,
)


SCHEMA_PATH = Path("data_vault/_meta/schema.yaml")


class TestLoadSchema:
    def test_loads_real_schema(self):
        """It should parse the real schema.yaml into a GraphSchema."""
        schema = load_schema(SCHEMA_PATH)
        assert isinstance(schema, GraphSchema)
        assert schema.version == "2.1"

    def test_concept_types_loaded(self):
        """It should load all 9 concept types."""
        schema = load_schema(SCHEMA_PATH)
        expected = {
            "structure", "space", "operator", "property",
            "quantity", "relation", "class", "problem", "criterion",
        }
        assert set(schema.concept_types.keys()) == expected

    def test_claim_types_loaded(self):
        """It should load all 6 claim types."""
        schema = load_schema(SCHEMA_PATH)
        expected = {
            "theorem", "lemma", "proposition",
            "corollary", "conjecture", "algorithm",
        }
        assert set(schema.claim_types.keys()) == expected

    def test_concept_type_has_required_fields(self):
        """It should parse required and optional fields per type."""
        schema = load_schema(SCHEMA_PATH)
        structure = schema.concept_types["structure"]
        assert "name" in structure.required_fields
        assert "formal_spec" in structure.required_fields
        assert "components" in structure.optional_fields

    def test_edge_types_loaded(self):
        """It should load concept, claim, coupling, and provenance edges."""
        schema = load_schema(SCHEMA_PATH)
        assert "generalizes" in schema.edges.concept_edges
        assert "depends_on" in schema.edges.claim_edges
        assert "about" in schema.edges.coupling_edges
        assert "sourced_from" in schema.edges.provenance_edges

    def test_inverse_symmetry(self):
        """It should have symmetric inverse declarations."""
        schema = load_schema(SCHEMA_PATH)
        gen = schema.edges.concept_edges["generalizes"]
        spec = schema.edges.concept_edges["specializes"]
        assert gen.inverse == "specializes"
        assert spec.inverse == "generalizes"

    def test_edge_has_attributes(self):
        """It should parse edge attribute lists."""
        schema = load_schema(SCHEMA_PATH)
        depends = schema.edges.claim_edges["depends_on"]
        assert "role" in depends.attributes
        assert "applied_to" in depends.attributes

    def test_validation_rules_loaded(self):
        """It should load validation rules with severity levels."""
        schema = load_schema(SCHEMA_PATH)
        assert "missing_about" in schema.validation.severity["error"]
        assert "cycle_in_depends_on" in schema.validation.severity["warning"]

    def test_field_ownership_loaded(self):
        """It should load field ownership categories."""
        schema = load_schema(SCHEMA_PATH)
        assert "slug" in schema.field_ownership.pipeline_owned
        assert "human_notes" in schema.field_ownership.human_owned
        assert "aliases" in schema.field_ownership.shared

    def test_rejects_unknown_yaml_key(self, tmp_path):
        """It should raise on unrecognized top-level keys."""
        bad = tmp_path / "bad.yaml"
        bad.write_text("version: '1.0'\nunknown_key: true\n")
        with pytest.raises(ValueError, match="unknown_key"):
            load_schema(bad)
```

- [ ] **Step 2: Run test — verify it fails**

```bash
uv run pytest tests/test_schema_loader.py -v
```
Expected: FAIL — `ModuleNotFoundError`

- [ ] **Step 3: Implement schema_types.py — dataclasses for the parsed schema**

```python
"""
@file schema_types.py
@description Typed dataclass definitions for the parsed schema.yaml.
"""

from dataclasses import dataclass, field


@dataclass
class ConceptTypeDef:
    """Definition of a concept type from schema.yaml."""
    description: str
    required_fields: list[str]
    optional_fields: list[str] = field(default_factory=list)
    examples: list[str] = field(default_factory=list)


@dataclass
class ClaimTypeDef:
    """Definition of a claim type from schema.yaml."""
    description: str
    required_fields: list[str]
    optional_fields: list[str] = field(default_factory=list)
    strength_values: list[str] = field(default_factory=list)
    status_values: list[str] = field(default_factory=list)


@dataclass
class EdgeDef:
    """Definition of an edge type from schema.yaml."""
    description: str
    attributes: list[str] = field(default_factory=list)
    inverse: str | None = None
    role_values: list[str] = field(default_factory=list)
    nature_values: list[str] = field(default_factory=list)
    dimension_values: list[str] = field(default_factory=list)


@dataclass
class EdgeCategories:
    """All edge types grouped by category."""
    concept_edges: dict[str, EdgeDef] = field(default_factory=dict)
    claim_edges: dict[str, EdgeDef] = field(default_factory=dict)
    coupling_edges: dict[str, EdgeDef] = field(default_factory=dict)
    provenance_edges: dict[str, EdgeDef] = field(default_factory=dict)


@dataclass
class ValidationSeverity:
    """Validation rule severity classifications."""
    error: list[str] = field(default_factory=list)
    warning: list[str] = field(default_factory=list)
    info: list[str] = field(default_factory=list)


@dataclass
class ValidationConfig:
    """Validation rules and severity levels."""
    rules: list[str] = field(default_factory=list)
    severity: ValidationSeverity = field(default_factory=ValidationSeverity)


@dataclass
class FieldOwnership:
    """Field ownership categories for export/sync-back."""
    pipeline_owned: list[str] = field(default_factory=list)
    human_owned: list[str] = field(default_factory=list)
    shared: list[str] = field(default_factory=list)


@dataclass
class GraphSchema:
    """Complete parsed schema.yaml."""
    version: str
    last_updated: str
    concept_types: dict[str, ConceptTypeDef]
    claim_types: dict[str, ClaimTypeDef]
    edges: EdgeCategories
    validation: ValidationConfig
    field_ownership: FieldOwnership
```

- [ ] **Step 4: Implement schema_loader.py**

```python
"""
@file schema_loader.py
@description Reads _meta/schema.yaml into typed dataclasses.
"""

from pathlib import Path

import yaml

from graph_builder.config.schema_types import (
    ClaimTypeDef,
    ConceptTypeDef,
    EdgeCategories,
    EdgeDef,
    FieldOwnership,
    GraphSchema,
    ValidationConfig,
    ValidationSeverity,
)

_VALID_TOP_KEYS = {
    "version", "last_updated", "concept_types", "claim_types",
    "edges", "validation", "field_ownership",
}


def load_schema(path: Path) -> GraphSchema:
    """Load and validate schema.yaml into a GraphSchema dataclass.

    @param path Path to schema.yaml
    @raises ValueError on unknown keys or malformed YAML
    """
    with open(path, "r", encoding="utf-8") as f:
        raw = yaml.safe_load(f)

    _check_unknown_keys(raw)

    return GraphSchema(
        version=str(raw["version"]),
        last_updated=str(raw.get("last_updated", "")),
        concept_types=_parse_concept_types(raw.get("concept_types", {})),
        claim_types=_parse_claim_types(raw.get("claim_types", {})),
        edges=_parse_edges(raw.get("edges", {})),
        validation=_parse_validation(raw.get("validation", {})),
        field_ownership=_parse_field_ownership(raw.get("field_ownership", {})),
    )


def _check_unknown_keys(raw: dict) -> None:
    """Reject unrecognized top-level keys."""
    unknown = set(raw.keys()) - _VALID_TOP_KEYS
    if unknown:
        raise ValueError(
            f"Unknown top-level keys in schema.yaml: {unknown}"
        )


def _parse_concept_types(raw: dict) -> dict[str, ConceptTypeDef]:
    return {
        name: ConceptTypeDef(
            description=defn.get("description", ""),
            required_fields=defn.get("required_fields", []),
            optional_fields=defn.get("optional_fields", []),
            examples=defn.get("examples", []),
        )
        for name, defn in raw.items()
    }


def _parse_claim_types(raw: dict) -> dict[str, ClaimTypeDef]:
    return {
        name: ClaimTypeDef(
            description=defn.get("description", ""),
            required_fields=defn.get("required_fields", []),
            optional_fields=defn.get("optional_fields", []),
            strength_values=defn.get("strength_values", []),
            status_values=defn.get("status_values", []),
        )
        for name, defn in raw.items()
    }


def _parse_edges(raw: dict) -> EdgeCategories:
    return EdgeCategories(
        concept_edges=_parse_edge_group(raw.get("concept_edges", {})),
        claim_edges=_parse_edge_group(raw.get("claim_edges", {})),
        coupling_edges=_parse_edge_group(raw.get("coupling_edges", {})),
        provenance_edges=_parse_edge_group(raw.get("provenance_edges", {})),
    )


def _parse_edge_group(raw: dict) -> dict[str, EdgeDef]:
    return {
        name: EdgeDef(
            description=defn.get("description", ""),
            attributes=defn.get("attributes", []),
            inverse=defn.get("inverse"),
            role_values=defn.get("role_values", []),
            nature_values=defn.get("nature_values", []),
            dimension_values=defn.get("dimension_values", []),
        )
        for name, defn in raw.items()
        if isinstance(defn, dict)  # skip YAML comments
    }


def _parse_validation(raw: dict) -> ValidationConfig:
    sev = raw.get("severity", {})
    return ValidationConfig(
        rules=raw.get("rules", []),
        severity=ValidationSeverity(
            error=sev.get("error", []),
            warning=sev.get("warning", []),
            info=sev.get("info", []),
        ),
    )


def _parse_field_ownership(raw: dict) -> FieldOwnership:
    return FieldOwnership(
        pipeline_owned=raw.get("pipeline_owned", []),
        human_owned=raw.get("human_owned", []),
        shared=raw.get("shared", []),
    )
```

- [ ] **Step 5: Run tests — verify passes**

```bash
uv run pytest tests/test_schema_loader.py -v
```
Expected: All 10 tests PASS

- [ ] **Step 6: Implement config.py**

```python
"""
@file config.py
@description Paths, constants, and connection configuration for the v2 graph builder.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

from data_loader.config import DATA_DIR, PROJECT_ROOT, sanitize_arxiv_id

# Load .env from Theo-Fish root
load_dotenv(PROJECT_ROOT.parent / ".env")

# Directories
CLEANED_DIR = DATA_DIR / "cleaned"
VAULT_DIR = PROJECT_ROOT / "data_vault"
LOG_DIR = PROJECT_ROOT / "logs"
SCHEMA_PATH = VAULT_DIR / "_meta" / "schema.yaml"

# DeepSeek LLM
DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY")
DEEPSEEK_MODEL = "deepseek-chat"
DEEPSEEK_BASE_URL = "https://api.deepseek.com"
LLM_THINKING = os.environ.get("LLM_THINKING", "True").lower() == "true"

# Embedding
EMBEDDING_MODEL = os.environ.get("EMBEDDING_MODEL", "text-embedding-3-small")
EMBEDDING_DIMENSIONS = int(os.environ.get("EMBEDDING_DIMENSIONS", "1536"))
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Neo4j
NEO4J_BOLT_URI = os.environ.get("NEO4J_BOLT_URI", "bolt://localhost:7687")
NEO4J_AUTH_USER = os.environ.get("NEO4J_AUTH_USER", "neo4j")
NEO4J_AUTH_PASS = os.environ.get("NEO4J_AUTH_PASS", "password")

# Processing limits
DEFAULT_CONCURRENCY = 10
MAX_SECTION_CHARS = 30_000
MIN_SECTION_CHARS = 50
MAX_RETRIES = 3
SECTION_TIMEOUT_SECONDS = 300
MAX_TITLE_LENGTH = 80

# Dedup thresholds
DEDUP_AUTO_THRESHOLD = 0.85
DEDUP_FLAG_THRESHOLD = 0.60
DEDUP_SHORTLIST_SIZE = 20

# Failure abort threshold
LLM_FAILURE_ABORT_RATIO = 0.50
```

- [ ] **Step 7: Commit**

```bash
git add graph_builder/config/ tests/test_schema_loader.py
git commit -m "feat(config): add schema loader, types, and v2 config with Neo4j/embedding params"
```

---

### Task 4: Models — ConceptNode, ClaimNode, SourceNode, ProvenanceNode, Edges, Section

**Files:**
- Create: `tests/test_concept_model.py`
- Create: `tests/test_claim_model.py`
- Create: `tests/test_source_model.py`
- Create: `tests/test_provenance_model.py`
- Create: `tests/test_edges_model.py`
- Create: `graph_builder/models/concept.py`
- Create: `graph_builder/models/claim.py`
- Create: `graph_builder/models/source.py`
- Create: `graph_builder/models/provenance.py`
- Create: `graph_builder/models/edges.py`
- Create: `graph_builder/models/section.py`
- Create: `graph_builder/models/results.py`

- [ ] **Step 1: Write test_concept_model.py**

```python
"""
@file test_concept_model.py
@description Tests for ConceptNode model.
"""

from graph_builder.models.concept import ConceptNode
from graph_builder.shared.slugify import slugify


class TestConceptNode:
    def test_slug_derived_from_name(self):
        """It should derive slug deterministically from name."""
        node = ConceptNode(
            name="Markov Decision Process",
            semantic_type="structure",
            formal_spec="(S, A, P, R, γ)",
        )
        assert node.slug == "markov-decision-process"

    def test_aliases_deduplicated_and_sorted(self):
        """It should deduplicate and sort aliases."""
        node = ConceptNode(
            name="MDP",
            semantic_type="structure",
            aliases=["finite MDP", "MDP", "finite MDP"],
        )
        assert node.aliases == ["MDP", "finite MDP"]

    def test_status_default_canonical(self):
        """It should default status to canonical."""
        node = ConceptNode(name="X", semantic_type="structure")
        assert node.status == "canonical"

    def test_promoted_fields(self):
        """It should accept promoted type-specific fields."""
        node = ConceptNode(
            name="Bellman operator",
            semantic_type="operator",
            ts_domain="state-value space",
            ts_codomain="state-value space",
        )
        assert node.ts_domain == "state-value space"
```

- [ ] **Step 1b: Write test_claim_model.py**

```python
"""
@file test_claim_model.py
@description Tests for ClaimNode model.
"""

from graph_builder.models.claim import ClaimNode


class TestClaimNode:
    def test_slug_composition(self):
        """It should compose slug from paper_slug + claim label."""
        node = ClaimNode(
            source_paper_slug="intro-bandits",
            label="Theorem 4.1",
            claim_type="theorem",
        )
        assert node.slug == "intro-bandits--theorem-4-1"

    def test_name_defaults_to_label(self):
        """It should default name to label."""
        node = ClaimNode(
            source_paper_slug="paper",
            label="Lemma 2.3",
            claim_type="lemma",
        )
        assert node.name == "Lemma 2.3"

    def test_strength_stored(self):
        """It should store strength value."""
        node = ClaimNode(
            source_paper_slug="p",
            label="T1",
            claim_type="theorem",
            strength="asymptotic",
        )
        assert node.strength == "asymptotic"

    def test_assumptions_ordered_list(self):
        """It should preserve assumption ordering."""
        node = ClaimNode(
            source_paper_slug="p",
            label="T1",
            claim_type="theorem",
            assumptions=["finite action space", "bounded rewards"],
        )
        assert node.assumptions == ["finite action space", "bounded rewards"]
```

- [ ] **Step 1c: Write test_source_model.py, test_provenance_model.py, test_edges_model.py**

```python
# tests/test_source_model.py
"""
@file test_source_model.py
@description Tests for SourceNode model.
"""

from graph_builder.models.source import SourceNode


class TestSourceNode:
    def test_creation_with_arxiv_id(self):
        """It should create with arxiv_id."""
        node = SourceNode(arxiv_id="1904.07272", title="Intro to Bandits")
        assert node.arxiv_id == "1904.07272"

    def test_authors_list(self):
        """It should store authors as list."""
        node = SourceNode(arxiv_id="1904.07272", authors=["A. Slivkins"])
        assert node.authors == ["A. Slivkins"]
```

```python
# tests/test_provenance_model.py
"""
@file test_provenance_model.py
@description Tests for ProvenanceNode and FormulationEdge models.
"""

from graph_builder.models.provenance import ProvenanceNode, FormulationEdge


class TestProvenanceNode:
    def test_concept_slug_and_source_arxiv(self):
        """It should store uniqueness keys."""
        node = ProvenanceNode(
            concept_slug="markov-decision-process",
            source_arxiv_id="1904.07272",
            formulation="A tuple (S,A,P,R,γ)",
        )
        assert node.concept_slug == "markov-decision-process"
        assert node.source_arxiv_id == "1904.07272"

class TestFormulationEdge:
    def test_match_metadata(self):
        """It should carry match method and confidence."""
        edge = FormulationEdge(match_method="embedding+llm", match_confidence=0.87)
        assert edge.match_method == "embedding+llm"
        assert edge.match_confidence == 0.87
```

```python
# tests/test_edges_model.py
"""
@file test_edges_model.py
@description Tests for edge dataclasses.
"""

from graph_builder.models.edges import (
    ConceptEdge, ClaimEdge, CouplingEdge, SourcedFromEdge,
)


class TestCouplingEdge:
    def test_about_requires_role(self):
        """It should store role on ABOUT edge."""
        edge = CouplingEdge(
            claim_slug="paper--theorem-1",
            concept_slug="nash-equilibrium",
            role="primary",
            aspect="existence proof",
        )
        assert edge.role == "primary"

class TestClaimEdge:
    def test_attributes_typed(self):
        """It should store typed attributes dict."""
        edge = ClaimEdge(
            source_slug="t1", target_slug="l1",
            edge_type="depends_on",
            attributes={"role": "bound", "applied_to": "concentration step"},
        )
        assert edge.attributes["role"] == "bound"
```

- [ ] **Step 2: Run tests — verify fails**

```bash
uv run pytest tests/test_concept_model.py tests/test_claim_model.py tests/test_source_model.py tests/test_provenance_model.py tests/test_edges_model.py -v
```
Expected: FAIL

- [ ] **Step 3: Implement concept.py**

```python
"""
@file concept.py
@description ConceptNode dataclass for Graph A.
"""

from typing import Any

from pydantic import BaseModel, field_validator, model_validator

from graph_builder.shared.slugify import slugify


class ConceptNode(BaseModel):
    """A mathematical concept in Graph A (Concept Ontology)."""

    slug: str = ""
    name: str
    semantic_type: str
    rhetorical_origin: str = ""
    canonical_definition: str = ""
    formal_spec: str = ""
    components: list[str] = []
    ts_domain: str = ""
    ts_codomain: str = ""
    ts_applies_to: str = ""
    ts_member_type: str = ""
    ts_objective: str = ""
    type_specific_fields: dict[str, Any] = {}
    aliases: list[str] = []
    status: str = "canonical"
    embedding: list[float] = []
    human_notes: str = ""
    date_modified: str = ""

    @model_validator(mode="after")
    def _derive_slug(self):
        if not self.slug:
            self.slug = slugify(self.name)
        return self

    @field_validator("aliases", mode="after")
    @classmethod
    def _dedup_sort_aliases(cls, v):
        return sorted(set(v))
```

- [ ] **Step 4: Implement claim.py, source.py, provenance.py, edges.py, section.py, results.py**

`graph_builder/models/section.py` (moved from v1 — the section_splitter depends on this):
```python
"""
@file section.py
@description Section model for chunked paper content.
"""

from pydantic import BaseModel


class Section(BaseModel):
    """A chunked section of a paper for LLM processing."""

    heading: str
    level: int
    content: str
    char_count: int
    index: int
```

`graph_builder/models/claim.py`:
```python
"""
@file claim.py
@description ClaimNode dataclass for Graph B.
"""

from pydantic import BaseModel, model_validator

from graph_builder.shared.slugify import slugify


class ClaimNode(BaseModel):
    """An assertion in Graph B (Reasoning Graph)."""

    slug: str = ""
    source_paper_slug: str
    label: str
    name: str = ""
    claim_type: str
    assumptions: list[str] = []
    conclusion: str = ""
    proof_technique: str = ""
    strength: str = ""
    statement: str = ""
    proof: str = ""
    section: str = ""
    status: str = "unverified"
    human_notes: str = ""
    date_modified: str = ""

    @model_validator(mode="after")
    def _derive_fields(self):
        if not self.name:
            self.name = self.label
        if not self.slug:
            label_slug = slugify(self.label)
            self.slug = f"{self.source_paper_slug}--{label_slug}"
        return self
```

`graph_builder/models/source.py`:
```python
"""
@file source.py
@description SourceNode dataclass for paper provenance.
"""

from pydantic import BaseModel


class SourceNode(BaseModel):
    """Paper provenance as a first-class node."""

    arxiv_id: str
    title: str = ""
    authors: list[str] = []
    date_published: str = ""
    date_extracted: str = ""
    human_notes: str = ""
```

`graph_builder/models/provenance.py`:
```python
"""
@file provenance.py
@description ProvenanceNode for per-paper concept formulations.
"""

from pydantic import BaseModel


class ProvenanceNode(BaseModel):
    """Per-paper formulation of a concept. Append-only."""

    concept_slug: str
    source_arxiv_id: str
    formulation: str = ""
    formal_spec: str = ""
    section: str = ""
    extraction_confidence: float = 0.0


class FormulationEdge(BaseModel):
    """Edge from Provenance to Concept with match metadata."""

    match_method: str = "new"  # new | alias | embedding | embedding+llm
    match_confidence: float = 1.0
```

`graph_builder/models/edges.py`:
```python
"""
@file edges.py
@description Typed edge models for concept, claim, and coupling relationships.
"""

from typing import Any

from pydantic import BaseModel


class ConceptEdge(BaseModel):
    """Edge between two concepts in Graph A."""

    source_slug: str
    target_slug: str
    edge_type: str  # e.g., "generalizes", "has_component"
    attributes: dict[str, Any] = {}


class ClaimEdge(BaseModel):
    """Edge between two claims in Graph B."""

    source_slug: str
    target_slug: str
    edge_type: str  # e.g., "depends_on", "enables"
    attributes: dict[str, Any] = {}


class CouplingEdge(BaseModel):
    """ABOUT edge from a claim to a concept."""

    claim_slug: str
    concept_slug: str
    role: str = "primary"
    aspect: str = ""


class SourcedFromEdge(BaseModel):
    """SOURCED_FROM edge linking a node to its paper."""

    node_slug: str
    source_arxiv_id: str
    section: str = ""
    page: str = ""
    confidence: float = 0.0
```

`graph_builder/models/results.py`:
```python
"""
@file results.py
@description Pipeline result models.
"""

from pydantic import BaseModel


class ValidationResult(BaseModel):
    """Result of schema validation for a single paper."""

    is_valid: bool
    errors: list[str] = []
    warnings: list[str] = []


class BuildResult(BaseModel):
    """Result of building a knowledge graph for a single paper."""

    arxiv_id: str
    status: str  # "built", "skipped", "failed"
    concept_count: int = 0
    claim_count: int = 0
    edge_count: int = 0
    error: str | None = None


class BatchBuildResult(BaseModel):
    """Aggregate result of building graphs for a batch of papers."""

    total: int
    built: int
    skipped: int
    failed: int
    results: list[BuildResult]
```

- [ ] **Step 5: Run all model tests**

```bash
uv run pytest tests/test_concept_model.py tests/test_claim_model.py tests/test_source_model.py tests/test_provenance_model.py tests/test_edges_model.py -v
```
Expected: All PASS

- [ ] **Step 6: Wire up models/__init__.py exports**

```python
"""
@file __init__.py
@description Public exports for graph_builder.models.
"""

from graph_builder.models.concept import ConceptNode
from graph_builder.models.claim import ClaimNode
from graph_builder.models.source import SourceNode
from graph_builder.models.provenance import ProvenanceNode, FormulationEdge
from graph_builder.models.edges import (
    ConceptEdge, ClaimEdge, CouplingEdge, SourcedFromEdge,
)
from graph_builder.models.section import Section
from graph_builder.models.results import (
    BuildResult, BatchBuildResult, ValidationResult,
)
```

- [ ] **Step 7: Commit**

```bash
git add graph_builder/models/ tests/test_concept_model.py tests/test_claim_model.py tests/test_source_model.py tests/test_provenance_model.py tests/test_edges_model.py
git commit -m "feat(models): add dual-graph node and edge models

ConceptNode (Graph A), ClaimNode (Graph B), SourceNode, ProvenanceNode,
typed edges (ConceptEdge, ClaimEdge, CouplingEdge, SourcedFromEdge),
and pipeline result models."
```

---

## Chunk 2: Layer 2 (LLM, Neo4j Graph Client) + Layer 2 Gate

### Task 5: LLM Client — Adapt v1 for v2

**Files:**
- Create: `tests/test_v2_llm_client.py`
- Create: `graph_builder/llm/llm_client.py`
- Create: `graph_builder/llm/response_parser.py`
- Create: `tests/test_response_parser.py`

- [ ] **Step 1: Write test_v2_llm_client.py** — covers retry, semaphore, token tracking (all mocked)

- [ ] **Step 2: Run test — verify fails**

- [ ] **Step 3: Implement llm_client.py** — adapt v1's `DeepSeekClient` into `graph_builder/llm/llm_client.py`, importing from v2 config. Keep the same retry/semaphore/token tracking logic.

- [ ] **Step 4: Write test_response_parser.py** — covers JSON parsing of concept/claim extraction responses, malformed entry handling, schema enum validation

- [ ] **Step 5: Implement response_parser.py** — parses LLM JSON responses into ConceptNode/ClaimNode lists, validates field values against schema enums, gracefully skips malformed entries

- [ ] **Step 6: Run all tests — verify passes**

```bash
uv run pytest tests/test_v2_llm_client.py tests/test_response_parser.py -v
```

- [ ] **Step 7: Commit**

```bash
git commit -m "feat(llm): add v2 LLM client and response parser with schema validation"
```

---

### Task 6: Neo4j Client — graph/neo4j_client.py

**Files:**
- Create: `tests/test_neo4j_client.py`
- Create: `graph_builder/graph/neo4j_client.py`

- [ ] **Step 1: Write test_neo4j_client.py** — unit tests for connection config, query builder helpers (mocked driver)

- [ ] **Step 2: Implement neo4j_client.py** — async Neo4j driver wrapper with connection pool, parameterized URI/auth from config

```python
"""
@file neo4j_client.py
@description Async Neo4j driver wrapper with connection pool.
"""

from neo4j import AsyncGraphDatabase, AsyncDriver

from graph_builder.config.config import (
    NEO4J_BOLT_URI,
    NEO4J_AUTH_USER,
    NEO4J_AUTH_PASS,
)


class Neo4jClient:
    """Async Neo4j connection manager."""

    def __init__(
        self,
        uri: str = NEO4J_BOLT_URI,
        user: str = NEO4J_AUTH_USER,
        password: str = NEO4J_AUTH_PASS,
    ):
        self._driver: AsyncDriver = AsyncGraphDatabase.driver(
            uri, auth=(user, password),
        )

    async def close(self) -> None:
        await self._driver.close()

    async def execute_read(self, query: str, **params):
        async with self._driver.session() as session:
            result = await session.run(query, **params)
            return [record.data() async for record in result]

    async def execute_write(self, query: str, **params):
        """Execute a single write query in a managed transaction."""
        async def _tx(tx):
            result = await tx.run(query, **params)
            return [record.data() async for record in result]
        async with self._driver.session() as session:
            return await session.execute_write(_tx)

    async def execute_write_tx(self, tx_func):
        """Execute a write transaction function for multi-statement transactions."""
        async with self._driver.session() as session:
            return await session.execute_write(tx_func)
```

- [ ] **Step 3: Run tests, commit**

---

### Task 7: Graph Writer — graph/graph_writer.py

**Files:**
- Create: `tests/test_graph_writer.py` (integration — requires Neo4j Docker)
- Create: `graph_builder/graph/graph_writer.py`

- [ ] **Step 1: Write test_graph_writer.py** — integration tests with real Neo4j testcontainer:
  - MERGE :Concept respects field ownership
  - CREATE :Claim with SOURCED_FROM + ABOUT edges
  - CREATE :Provenance with match_method + match_confidence
  - Node-level transaction isolation (failed claim doesn't roll back concept)
  - Edge batch rollback on dangling reference

- [ ] **Step 2: Implement graph_writer.py** — MERGE/CREATE operations with field ownership rules per spec Section 3:
  - `write_concept()` — MERGE by slug, SET pipeline-owned, skip human-owned if exists
  - `write_claim()` — CREATE with SOURCED_FROM edge
  - `write_provenance()` — CREATE with FORMULATION_OF + SOURCED_FROM edges
  - `write_edges_batch()` — batch all edges for a paper in single transaction
  - `create_schema_constraints()` — creates all uniqueness constraints and indexes from spec Section 2.6

- [ ] **Step 3: Run integration tests**

```bash
uv run pytest tests/test_graph_writer.py -v -m integration
```

- [ ] **Step 4: Commit**

---

### Task 8: Graph Reader — graph/graph_reader.py

**Files:**
- Create: `tests/test_graph_reader.py` (integration)
- Create: `graph_builder/graph/graph_reader.py`

- [ ] **Step 1: Write test_graph_reader.py** — queries against real Neo4j:
  - Get all concept slugs
  - Vector similarity search for embeddings
  - Full-text search on name/formal_spec/aliases
  - Get concept neighbors (for Pass 2 context injection)

- [ ] **Step 2: Implement graph_reader.py**:
  - `get_all_concept_slugs()` → list[str]
  - `get_concept_embeddings()` → dict[slug, embedding]
  - `vector_similarity_search(embedding, top_k)` → list[(slug, score)]
  - `get_concept_neighbors(slugs)` → list[ConceptNode] (immediate Graph A neighbors)
  - `get_existing_concept(slug)` → ConceptNode | None

- [ ] **Step 3: Run integration tests, commit**

---

### Task 9: Layer 2 Gate — Integration Test Milestone

**Files:**
- Create: `tests/test_layer2_gate.py`

- [ ] **Step 1: Write test_layer2_gate.py**

This is the critical gate test. It validates that models/ and graph/ agree on the Neo4j schema before building Layer 3.

```python
"""
@file test_layer2_gate.py
@description Layer 2 integration gate — validates models + graph agree on Neo4j schema.
Must pass before building Layer 3.
"""

import pytest

# Mark entire module as integration
pytestmark = pytest.mark.integration


class TestLayer2Gate:
    """End-to-end write-read with fixture data for all node types and edge types."""

    async def test_concept_write_read_roundtrip(self, neo4j_client):
        """It should write a Concept and read it back with all fields intact."""

    async def test_claim_write_with_about_edge(self, neo4j_client):
        """It should write a Claim with ABOUT -> Concept edge."""

    async def test_source_and_provenance(self, neo4j_client):
        """It should write Source + Provenance with FORMULATION_OF + SOURCED_FROM."""

    async def test_all_concept_edge_types(self, neo4j_client):
        """It should write GENERALIZES, HAS_COMPONENT, INSTANCE_OF, etc. with attributes."""

    async def test_all_claim_edge_types(self, neo4j_client):
        """It should write DEPENDS_ON, ENABLES, STRENGTHENS, etc. with attributes."""

    async def test_field_ownership_on_merge(self, neo4j_client):
        """It should preserve human-owned fields when MERGEing same concept."""

    async def test_vector_similarity_search(self, neo4j_client):
        """It should find a concept by embedding similarity."""

    async def test_node_transaction_isolation(self, neo4j_client):
        """It should write valid concept even when claim fails."""

    async def test_provenance_uniqueness_constraint(self, neo4j_client):
        """It should reject duplicate (concept_slug, source_arxiv_id) pairs."""
```

- [ ] **Step 2: Run gate test**

```bash
uv run pytest tests/test_layer2_gate.py -v -m integration
```
Expected: All 9 tests PASS

- [ ] **Step 3: Commit**

```bash
git commit -m "test(gate): Layer 2 integration gate — all node/edge types validated against Neo4j"
```

**MILESTONE: Layer 2 gate passes. Proceed to Layer 3.**

---

## Chunk 3: Layer 3A — Extraction Pipeline + Dedup

### Task 10: Prompt Generator — extraction/prompt_generator.py

**Files:**
- Create: `tests/test_prompt_generator.py`
- Create: `graph_builder/extraction/prompt_generator.py`

- [ ] **Step 1: Write test** — verify prompts are generated from schema, include all concept/claim types, respond to schema changes

- [ ] **Step 2: Implement** — reads GraphSchema, outputs formatted system prompts for:
  - `build_concept_prompt(schema)` — Pass 1 system prompt
  - `build_claim_prompt(schema, concept_list)` — Pass 2 system prompt
  - `build_edge_enrichment_prompt(schema)` — Pass 3a system prompt
  - `build_gap_fill_prompt(schema)` — Pass 3b system prompt

- [ ] **Step 3: Tests pass, commit**

---

### Task 11: Concept Extractor — extraction/concept_extractor.py

**Files:**
- Create: `tests/test_concept_extractor.py`
- Create: `graph_builder/extraction/concept_extractor.py`

- [ ] **Step 1: Write test** — mocked LLM, verifies:
  - Per-section extraction returns ConceptNode list
  - Empty sections return empty list
  - Existing concept shortlist injected into prompt
  - Malformed LLM response handled gracefully

- [ ] **Step 2: Implement** — `extract_concepts(section, schema, existing_concepts, llm_client)` → list[ConceptNode]

- [ ] **Step 3: Tests pass, commit**

---

### Task 12: Dedup Cascade — extraction/dedup/

**Files:**
- Create: `tests/test_fuzzy_matcher.py`
- Create: `tests/test_dedup_cascade.py`
- Create: `graph_builder/extraction/dedup/abbreviations.py`
- Create: `graph_builder/extraction/dedup/fuzzy_matcher.py`
- Create: `graph_builder/extraction/dedup/embedding_client.py`
- Create: `graph_builder/extraction/dedup/dedup_cascade.py`

- [ ] **Step 1: Write test_fuzzy_matcher.py** — abbreviation expansion, similarity thresholds, normalization

- [ ] **Step 2: Implement abbreviations.py + fuzzy_matcher.py**

- [ ] **Step 3: Write test_embedding_client.py** — batch computation (mocked API), dimensionality matches Neo4j config

- [ ] **Step 4: Implement embedding_client.py** — batch embedding computation via OpenAI API (mocked in tests)

- [ ] **Step 5: Write test_dedup_cascade.py** — full cascade flow, confidence propagation

- [ ] **Step 6: Implement dedup_cascade.py** — orchestrates: embedding → fuzzy → LLM confirm. Returns resolved concept list with slug mappings + match_method/match_confidence.

- [ ] **Step 7: Tests pass, commit**

---

### Task 13: Concept Merger — extraction/concept_merger.py

**Files:**
- Create: `tests/test_concept_merger.py`
- Create: `graph_builder/extraction/concept_merger.py`

- [ ] **Step 1: Write test** — intra-paper dedup (keeps richest formulation), cross-vault cascade integration

- [ ] **Step 2: Implement** — `merge_concepts(per_section_concepts, graph_reader, dedup_cascade)` → resolved concept list with provenance metadata

- [ ] **Step 3: Tests pass, commit**

---

### Task 14: Claim Extractor — extraction/claim_extractor.py

**Files:**
- Create: `tests/test_claim_extractor.py`
- Create: `graph_builder/extraction/claim_extractor.py`

- [ ] **Step 1: Write test** — mocked LLM, verifies:
  - Per-section extraction with section-local concepts + neighbors in prompt
  - Claims reference concept slugs from provided list
  - ABOUT edges generated per claim

- [ ] **Step 2: Implement** — `extract_claims(section, schema, concept_list, llm_client)` → (list[ClaimNode], list[CouplingEdge])

- [ ] **Step 3: Tests pass, commit**

---

### Task 15: Edge Enricher + Cross-Section Linker

**Files:**
- Create: `tests/test_edge_enricher.py`
- Create: `tests/test_cross_section_linker.py`
- Create: `graph_builder/extraction/edge_enricher.py`
- Create: `graph_builder/extraction/cross_section_linker.py`

- [ ] **Step 1: Write test_edge_enricher.py** — per-section claim enrichment, conditional attributes, schema enum validation

- [ ] **Step 2: Implement edge_enricher.py** — `enrich_section_edges(section_claims, section_text, concepts, schema, llm_client)` → list[ClaimEdge]

Batches claims by section (not per-claim) per spec feedback.

- [ ] **Step 3: Write test_cross_section_linker.py** — detects implicit cross-section deps, no duplication

- [ ] **Step 4: Implement cross_section_linker.py** — `find_cross_section_edges(all_claims, all_concepts, existing_edges, schema, llm_client)` → list[ClaimEdge]

Uses claim conclusions + concept formal_specs (not full text) per spec feedback.

- [ ] **Step 5: Tests pass, commit**

---

### Task 16: Section Splitter — Move v1 to v2 namespace

**Files:**
- Modify: `graph_builder/extraction/section_splitter.py` (copy from v1, update imports)

- [ ] **Step 1: Copy section_splitter.py to extraction/**

Update two imports:
- `from graph_builder.config import MAX_SECTION_CHARS, MIN_SECTION_CHARS` → `from graph_builder.config.config import MAX_SECTION_CHARS, MIN_SECTION_CHARS`
- `from graph_builder.models import Section` → `from graph_builder.models.section import Section`

The `Section` model now lives at `graph_builder/models/section.py` (created in Task 4).

- [ ] **Step 2: Verify existing section splitter tests still pass**

```bash
uv run pytest tests/test_section_splitter.py -v
```

- [ ] **Step 3: Commit**

---

## Chunk 4: Layer 3B — Validation + Vault

### Task 17: Validator — validation/validator.py

**Files:**
- Create: `tests/test_validator.py`
- Create: `graph_builder/validation/validator.py`
- Create: `graph_builder/validation/cycle_detector.py`

- [ ] **Step 1: Write test_validator.py** — tests all validation rules:
  - Every claim has ≥1 ABOUT (error)
  - Every concept has ≥1 Provenance via FORMULATION_OF (error)
  - Corollary has ≥1 DEPENDS_ON (warning)
  - No unknown edge types (error)
  - Unknown attributes (warning)
  - DEPENDS_ON cycle detection (warning)
  - Inverse consistency (error)
  - Severity levels respected

- [ ] **Step 2: Implement cycle_detector.py** — DFS-based cycle detection on DEPENDS_ON edges

- [ ] **Step 3: Implement validator.py** — `validate_paper(concepts, claims, edges, schema)` → ValidationResult

- [ ] **Step 4: Tests pass, commit**

---

### Task 18: Frontmatter Builder — vault/frontmatter_builder.py

**Files:**
- Create: `tests/test_frontmatter_builder.py`
- Create: `graph_builder/vault/frontmatter_builder.py`

- [ ] **Step 1: Write test** — generates flat wikilink keys + _meta companion keys, field ownership defaults

- [ ] **Step 2: Implement** — builds YAML frontmatter dicts from Neo4j node data, respecting field ownership. Generates both `depends_on: ["[[...]]"]` and `depends_on_meta: [...]` keys atomically.

- [ ] **Step 3: Tests pass, commit**

---

### Task 19: Body Renderer — vault/body_renderer.py

**Files:**
- Create: `tests/test_body_renderer.py`
- Create: `graph_builder/vault/body_renderer.py`

- [ ] **Step 1: Write test** — LaTeX preserved, prose wikilinks correct, provenance table for concepts

- [ ] **Step 2: Implement** — renders markdown body from node data. Concept files get provenance table. Claim files get proof section. Source files get concept/claim lists.

- [ ] **Step 3: Tests pass, commit**

---

### Task 20: Obsidian Exporter — vault/obsidian_exporter.py

**Files:**
- Create: `tests/test_obsidian_exporter.py`
- Create: `graph_builder/vault/obsidian_exporter.py`
- Create: `graph_builder/vault/manifest.py`

- [ ] **Step 1: Write test_obsidian_exporter.py** — integration:
  - Full export creates correct folder structure (concepts/, claims/{type}/, sources/, _review/, _meta/)
  - Human-owned fields preserved on re-export
  - Dirty git check aborts with warning
  - Export-manifest.json written with correct counts
  - Claim files use {paper-slug}--{claim-slug}.md naming

- [ ] **Step 2: Implement manifest.py** — reads/writes `_meta/export-manifest.json`

- [ ] **Step 3: Implement obsidian_exporter.py** — queries Neo4j, writes to staging dir, atomic move per file. Preserves human-owned fields by reading existing files before write. Populates `_review/` for flagged items.

- [ ] **Step 4: Tests pass, commit**

---

### Task 21: Sync-Back — vault/sync_back.py

**Files:**
- Create: `tests/test_sync_back.py`
- Create: `graph_builder/vault/sync_back.py`

- [ ] **Step 1: Write test** — integration:
  - Reads human-owned fields from vault → writes to Neo4j
  - Ignores pipeline-owned fields
  - Union-merges shared fields (aliases)
  - Dry-run mode shows diff without writing
  - Only processes files modified after last manifest timestamp

- [ ] **Step 2: Implement** — `sync_back(vault_dir, neo4j_client, dry_run=False)`

- [ ] **Step 3: Tests pass, commit**

---

### Task 22: Round-Trip Invariance Test

**Files:**
- Create: `tests/test_round_trip_invariance.py`

- [ ] **Step 1: Write test** — scheduled integration:
  - Populate Neo4j with fixture data
  - Export to vault
  - Sync-back with no human edits
  - Compare Neo4j state: zero diff

- [ ] **Step 2: Run and verify**

```bash
uv run pytest tests/test_round_trip_invariance.py -v -m integration
```

- [ ] **Step 3: Commit**

---

## Chunk 5: Layer 4 — Orchestrator + End-to-End Tests

### Task 23: Orchestrator — orchestrator/orchestrator.py

**Files:**
- Create: `tests/test_v2_orchestrator.py`
- Create: `graph_builder/orchestrator/orchestrator.py`

- [ ] **Step 1: Write test** — integration (mocked LLM, real Neo4j):
  - Single paper through full pipeline: load → P1 → merge → P2 → P3a → P3b → validate → write
  - Correct pass ordering verified
  - Partial validation failure: valid nodes written, invalid skipped + logged
  - Skip-if-already-built logic
  - LLM failure >50% aborts paper

- [ ] **Step 2: Implement orchestrator.py** — `process_paper(arxiv_id, schema, llm_client, neo4j_client)` → BuildResult

The orchestrator coordinates all pipeline stages:
1. Load cleaned JSON
2. Split into sections
3. Pass 1: parallel concept extraction per section
4. Concept merge + dedup cascade
5. Pass 2: parallel claim extraction per section (grounded)
6. Pass 3a: section-batched edge enrichment
7. Pass 3b: paper-wide gap-fill
8. Validate against schema
9. Write to Neo4j (granular transactions)

- [ ] **Step 3: Tests pass, commit**

---

### Task 24: Batch Processor — orchestrator/batch_processor.py

**Files:**
- Create: `tests/test_batch_processor.py`
- Create: `graph_builder/orchestrator/batch_processor.py`

- [ ] **Step 1: Write test** — multi-paper parallel, one failure doesn't block others, BatchBuildResult aggregation

- [ ] **Step 2: Implement** — discovers papers from input dir, processes in parallel (semaphore), returns BatchBuildResult

- [ ] **Step 3: Tests pass, commit**

---

### Task 25: CLI — orchestrator/cli.py

**Files:**
- Create: `tests/test_v2_cli.py`
- Create: `graph_builder/orchestrator/cli.py`
- Modify: `graph_builder/__main__.py`
- Modify: `graph_builder/__init__.py`

- [ ] **Step 1: Write test** — flag parsing: --paper, --input-dir, --export, --sync-back, --force, --dry-run, --concurrency, --no-thinking

- [ ] **Step 2: Implement cli.py** — argparse with all flags, dispatches to orchestrator/exporter/sync-back

- [ ] **Step 3: Wire __main__.py and __init__.py** — public API: `build_graph`, `build_graphs`, `is_built`, `export_vault`, `sync_back`

- [ ] **Step 4: Tests pass, commit**

---

### Task 26: Golden Paper Test (Two-Paper Cross-Dedup)

**Files:**
- Create: `tests/test_golden_paper.py`
- Create: `tests/fixtures/llm/k_strong_price_of_anarchy/` (recorded fixtures)
- Create: `tests/fixtures/llm/overlap_game_theory/` (recorded fixtures)

- [ ] **Step 1: Generate LLM fixtures** — run the pipeline against the K-Strong Price of Anarchy paper with real DeepSeek, record all LLM request/response pairs as JSON fixtures

- [ ] **Step 2: Generate overlap paper fixtures** — run against a second game theory paper that shares 5-10 concepts

- [ ] **Step 3: Write test_golden_paper.py**

Phase 1 — Single-paper extraction:
- Concept extraction produces expected semantic types
- Claim extraction identifies theorems/lemmas with dependency structure
- ABOUT coupling edges link claims to correct concepts
- Edge attributes populated

Phase 2 — Cross-paper dedup:
- Shared concepts merged (e.g., "Nash Equilibrium")
- Separate :Provenance nodes for each paper's formulation
- match_method and match_confidence populated on FORMULATION_OF edges
- No duplicate :Concept nodes

- [ ] **Step 4: Run golden test**

```bash
uv run pytest tests/test_golden_paper.py -v -m integration
```

- [ ] **Step 5: Commit**

```bash
git commit -m "test(golden): two-paper golden test validates cross-paper dedup"
```

---

### Task 27: End-to-End Smoke Test

**Files:**
- Create: `tests/test_e2e_smoke.py`

- [ ] **Step 1: Write test_e2e_smoke.py** — the acceptance test:
  1. Load real cleaned paper JSON
  2. Run full pipeline (mocked LLM with recorded fixtures, real Neo4j)
  3. Query Neo4j: confirm :Concept, :Claim, :Source, :Provenance nodes exist
  4. Confirm all edge types present with correct attributes
  5. Run export → confirm vault files in correct folders
  6. Edit a human-owned field in vault → run sync-back → confirm Neo4j updated
  7. Re-export → confirm human edit preserved

- [ ] **Step 2: Run**

```bash
uv run pytest tests/test_e2e_smoke.py -v -m e2e
```

- [ ] **Step 3: Commit**

```bash
git commit -m "test(e2e): full pipeline smoke test — extraction, Neo4j, export, sync-back"
```

---

### Task 28: Cleanup — Remove v1 After Validation

- [ ] **Step 1: Verify all new tests pass**

```bash
uv run pytest tests/ -v --ignore=tests/test_entity_extractor.py --ignore=tests/test_relationship_mapper.py --ignore=tests/test_vault_scanner.py --ignore=tests/test_vault_writer.py --ignore=tests/test_prompts.py --ignore=tests/test_graph_builder_models.py --ignore=tests/test_graph_builder_orchestrator.py --ignore=tests/test_graph_builder_sdk.py --ignore=tests/test_graph_builder_cli.py
```

- [ ] **Step 2: Remove graph_builder_v1/ and old test files**

```bash
rm -rf graph_builder_v1
rm tests/test_entity_extractor.py tests/test_relationship_mapper.py tests/test_vault_scanner.py tests/test_vault_writer.py tests/test_prompts.py tests/test_graph_builder_models.py tests/test_graph_builder_orchestrator.py tests/test_graph_builder_sdk.py tests/test_graph_builder_cli.py
```

- [ ] **Step 3: Update pyproject.toml** — remove `graph_builder_v1` from packages

- [ ] **Step 4: Final test run**

```bash
uv run pytest tests/ -v
```

- [ ] **Step 5: Commit**

```bash
git commit -m "chore: remove graph_builder v1 after successful v2 validation"
```

---

## Summary: File Count & Build Order

| Layer | Tasks | New Files | Test Files |
|---|---|---|---|
| Setup | 1 | schema.yaml + scaffolding | — |
| Layer 1 | 2-4 | 11 source files | 4 test files |
| Layer 2 | 5-9 | 5 source files | 5 test files + gate |
| Layer 3A | 10-16 | 10 source files | 7 test files |
| Layer 3B | 17-22 | 7 source files | 6 test files + roundtrip |
| Layer 4 | 23-28 | 4 source files | 5 test files + golden + e2e |
| **Total** | **28 tasks** | **~37 source files** | **~27 test files** |
