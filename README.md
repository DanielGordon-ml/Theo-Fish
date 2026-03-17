# Theo-Fish ETL Pipeline

A three-stage pipeline that converts ArXiv math papers into a Neo4j-backed dual-graph knowledge graph, exported as an Obsidian vault with full round-trip editing support.

## Architecture

```
                         Stage 1              Stage 2              Stage 3
ArXiv papers ──► Data Loader ──► Data Cleaner ──► Graph Builder ──► Neo4j
                  (ingest)        (normalize)      (extract)          │
                                                                     ▼
                 CSV / ArXiv ID   6-stage          Multi-pass LLM  Obsidian
                 ──► JSON         cleaning         extraction       Vault
                                                                     │
                 Data/papers/     Data/processed/   Data/cleaned/   data_vault/
                                                                     │
                                                         ◄───────────┘
                                                       sync-back
                                                    (human edits)
```

**Dual-graph model:**

- **Graph A (Concept Ontology)** — Mathematical objects and vocabulary (`:Concept` nodes with 9 semantic types)
- **Graph B (Reasoning Graph)** — Claims about concepts (`:Claim` nodes with 6 claim types)
- **Coupling** — `ABOUT` edges connect claims to the concepts they reference
- **Provenance** — `:Source` and `:Provenance` nodes track paper origins and per-paper formulations

## Quick Start

```bash
# 1. Clone and install
git clone <repo-url> && cd Theo-Fish/ETL
uv sync

# 2. Configure environment
cp ../.env.example ../.env   # then fill in API keys

# 3. Start Neo4j
docker compose up -d

# 4. Run the full pipeline on a paper
python -m data_loader --paper 2502.00425
python -m data_cleaner --paper 2502.00425
python -m graph_builder --paper 2502.00425

# Or use the unified CLI (runs all 3 stages automatically)
python main.py 2502.00425

# 5. Export to Obsidian vault
python -m graph_builder --export

# 6. Open data_vault/ in Obsidian
```

## Prerequisites

| Requirement | Version | Purpose |
|---|---|---|
| Python | >= 3.10 | Runtime |
| [uv](https://github.com/astral-sh/uv) | latest | Package management |
| Docker | latest | Neo4j container |
| DeepSeek API key | — | LLM extraction (Graph Builder) |
| Anthropic API key | — | Claude Opus 4.6 for claim extraction + verification |
| OpenAI API key | — | Embeddings for dedup (optional, uses `text-embedding-3-small`) |

## Installation

```bash
# Install all dependencies (including dev)
uv sync

# Or install without dev dependencies
uv sync --no-dev
```

Create a `.env` file at `Theo-Fish/.env`:

```env
DEEPSEEK_API_KEY=<your-deepseek-key>
OPENAI_API_KEY=<your-openai-key>        # optional, for embedding dedup
LLM_THINKING=True                        # enable chain-of-thought
ANTHROPIC_API_KEY=<your-anthropic-key>   # for claim extraction + verification
```

## Pipeline Stages

### Stage 1: Data Loader

Ingests ArXiv papers by ID or URL and converts them to structured JSON. Supports two conversion backends: **arxiv2md** (lightweight Markdown) and **MinerU** (high-fidelity PDF extraction).

```bash
# Load a single paper by ArXiv ID
python -m data_loader --paper 2502.00425

# Load multiple papers
python -m data_loader --paper 2502.00425 --paper 1904.07272

# Load from a CSV file
python -m data_loader --csv papers.csv

# Custom output directory and concurrency
python -m data_loader --paper 2502.00425 --output Data/processed --concurrency 5

# Force reprocess even if JSON exists
python -m data_loader --paper 2502.00425 --force
```

**CSV format:** Columns `paper_name`, `file_path`, `file_type`.

**Input:** ArXiv IDs or URLs | **Output:** `Data/processed/*.json`

| Flag | Default | Description |
|---|---|---|
| `--csv` | — | Path to CSV file |
| `--paper` | — | ArXiv ID or URL (repeatable) |
| `--output` | `Data/processed` | Output directory |
| `--papers-dir` | `Data/papers` | Directory for cached PDFs |
| `--concurrency` | `5` | Max concurrent conversions |
| `--force` | `false` | Reprocess existing papers |

### Stage 2: Data Cleaner

Normalizes raw paper text through six sequential cleaning stages:

1. **Newline normalization** — Standardize line endings and paragraph breaks
2. **LaTeX normalization** — Fix broken LaTeX commands, normalize delimiters
3. **Artifact removal** — Strip OCR/conversion artifacts
4. **Heading normalization** — Standardize section heading formats
5. **Whitespace cleaning** — Remove excess whitespace, normalize indentation
6. **Metadata repair** — Fix and validate paper metadata fields

```bash
# Clean a single paper
python -m data_cleaner --paper 2502.00425

# Clean all papers in a directory
python -m data_cleaner --input Data/processed --output Data/cleaned

# Force re-clean with higher concurrency
python -m data_cleaner --force --concurrency 16
```

**Input:** `Data/processed/*.json` | **Output:** `Data/cleaned/*.json`

| Flag | Default | Description |
|---|---|---|
| `--input` | `Data/processed` | Input directory |
| `--output` | `Data/cleaned` | Output directory |
| `--paper` | — | Clean a single paper by ArXiv ID |
| `--concurrency` | `8` | Max parallel workers |
| `--force` | `false` | Re-clean existing papers |

### Stage 3: Graph Builder

Uses DeepSeek V3 for concept extraction and Claude Opus 4.6 for claim/proof extraction via a schema-driven, multi-pass extraction process, then writes to Neo4j and exports to an Obsidian vault.

```bash
# Build graph for a single paper
python -m graph_builder --paper 2502.00425

# Batch process all cleaned papers
python -m graph_builder --input-dir Data/cleaned

# Export Neo4j graph to Obsidian vault
python -m graph_builder --export

# Sync human edits from vault back to Neo4j
python -m graph_builder --sync-back

# Preview sync-back changes without writing
python -m graph_builder --sync-back --dry-run

# Combine: process batch then export
python -m graph_builder --input-dir Data/cleaned --export

# Force reprocess with custom concurrency, no thinking
python -m graph_builder --paper 2502.00425 --force --concurrency 20 --no-thinking
```

**Input:** `Data/cleaned/*.json` | **Output:** Neo4j graph + `data_vault/`

| Flag | Default | Description |
|---|---|---|
| `--paper` | — | Process a single paper by ArXiv ID |
| `--input-dir` | — | Process all papers in directory |
| `--export` | `false` | Export Neo4j graph to Obsidian vault |
| `--sync-back` | `false` | Sync human-edited vault fields back to Neo4j |
| `--force` | `false` | Re-process already-built papers |
| `--concurrency` | `10` | Max parallel LLM calls |
| `--no-thinking` | `false` | Disable chain-of-thought in LLM |
| `--dry-run` | `false` | Preview sync-back changes without writing |

#### Unified CLI

A single entry point that runs the full pipeline (load → clean → build) for one or more papers.
By default all three stages run, each auto-skipping already-completed work.

```bash
# Single paper — full pipeline
python main.py 2502.00425

# CSV batch — full pipeline
python main.py --csv papers.csv

# Resume from a specific stage (skip earlier stages)
python main.py --csv papers.csv --from clean    # skip load
python main.py --csv papers.csv --from process  # skip load+clean

# Force re-run everything
python main.py --csv papers.csv --force

# Force re-run from clean stage only
python main.py --csv papers.csv --from clean --force
```

| Flag | Default | Description |
|---|---|---|
| `arxiv_id` | — | Positional: paper ID to process |
| `--csv` | — | Path to CSV or text file with paper IDs |
| `--from` | `load` | Start pipeline from this stage: `load`, `clean`, or `process` |
| `--force` | `false` | Re-run all active stages from scratch |
| `--concurrency` | `10` | Max parallel LLM calls |
| `--no-export` | `false` | Skip vault export |

#### Multi-Pass Extraction

1. **Pass 1 — Concept Extraction** (DeepSeek, per-section parallel): Extracts mathematical concepts with semantic types from each section. Includes top-k embedding-similar existing concepts for cross-paper reuse.
2. **Concept Merge & Dedup** (paper-wide): Hybrid dedup cascade — embedding similarity > 0.85 auto-merges, 0.6–0.85 triggers LLM confirmation, < 0.6 creates new concept.
3. **Proof Linker** — Maps deferred proofs to their theorems (regex, no LLM).
4. **Pass 2 — Claim + Proof Extraction** (Claude, per-section parallel): Extracts theorems, lemmas, propositions, etc. grounded against merged concepts, with injected deferred proofs.
5. **Pass 3a — Edge Enrichment** (DeepSeek, per-section): Per-section enrichment for typed edges with attributes + coupling edge dedup.
6. **Pass 3b — Cross-section Gap-fill** (DeepSeek, single call): Paper-wide gap-fill for cross-section dependencies.
7. **Pass 4 — Verification** (Claude, per-section): Auto-fix + review routing for extracted entities.
8. **Validate & Write** to Neo4j (with clear-on-force): Schema validation, then granular Neo4j transactions (one per entity, partial failure safe).

**LLM call budget:** ~2N DeepSeek + N Claude + S DeepSeek + 1 DeepSeek + N Claude verification calls per paper (N = sections, S = sections with claims).

## Neo4j Setup

```bash
# Start Neo4j (5.26-community) 
docker compose up -d

# Stop Neo4j (data persists in volume)
docker compose down
```

| Property | Value |
|---|---|
| Bolt URL | `bolt://localhost:7687` |
| Browser URL | `http://localhost:7474` See also [Neo4j Browser](http://127.0.0.1:7474) |
| Username | `neo4j` |
| Password | `password` |

The graph builder auto-creates all required constraints and indexes on first run:
- Uniqueness constraints on concept `slug`, claim `slug`, source `arxiv_id`
- Composite index on claim `source_paper_slug` + `label`
- Full-text index on concept `name` + `formal_spec` + `aliases`
- Vector index on concept `embedding` (1536 dims, cosine similarity)

## Vault Structure

```
data_vault/
├── concepts/                    # Graph A — shared mathematical vocabulary
│   ├── markov-decision-process.md
│   ├── nash-equilibrium.md
│   └── ...
├── claims/                      # Graph B — organized by claim type
│   ├── theorems/
│   ├── lemmas/
│   ├── propositions/
│   ├── corollaries/
│   ├── conjectures/
│   └── algorithms/
├── sources/                     # Paper provenance
│   └── k-strong-price-of-anarchy.md
├── _meta/
│   ├── schema.yaml              # Single source of truth for types and edges
│   └── export-manifest.json     # Audit trail for export runs
└── _review/                     # Human curation queue
    ├── concepts/                # Concepts with status: review_needed
    └── claims/                  # Claims with validation warnings
```

Each markdown file has YAML frontmatter with typed fields and `[[wikilinks]]` for Obsidian graph navigation.

## Schema-Driven Extraction

All extraction is driven by `data_vault/_meta/schema.yaml` (v2.1). The schema defines:

### Concept Types (9)

| Type | Description | Example |
|---|---|---|
| `structure` | Mathematical objects | Markov Decision Process, Nash Equilibrium |
| `space` | Sets, domains, manifolds | Policy space, state space, simplex |
| `operator` | Functions, maps, transformations | Bellman operator, projection |
| `property` | Attributes of objects | Ergodicity, convexity, Lipschitz continuity |
| `quantity` | Measurable values | Expected return, regret, KL divergence |
| `relation` | Binary/n-ary relationships | Dominance, Pareto optimality |
| `class` | Families or categories | Potential games, linear MDPs |
| `problem` | Named problems | Multi-armed bandit, optimal stopping |
| `criterion` | Objectives or loss functions | Regret minimization, Nash social welfare |

### Claim Types (6)

| Type | Description | Required Fields |
|---|---|---|
| `theorem` | Major proven result | name, assumptions, conclusion, proof_technique |
| `lemma` | Supporting proven result | name, assumptions, conclusion |
| `proposition` | Intermediate result | name, assumptions, conclusion |
| `corollary` | Direct consequence | name, conclusion, derived_from |
| `conjecture` | Unproven claim | name, statement |
| `algorithm` | Procedural claim | name, input_spec, output_spec, guarantee |

### Edge Types

**Concept ↔ Concept:** `generalizes`/`specializes`, `has_component`/`component_of`, `instance_of`/`has_instance`, `dual_of`, `equipped_with`

**Claim ↔ Claim:** `depends_on`, `enables`, `strengthens`/`weakens`, `contradicts`, `equivalent_to`

**Coupling:** `about` (claim → concept, with role: primary, scope, mechanism, bound_target, construction_input)

**Provenance:** `sourced_from`, `formulation_of`

## Obsidian Export & Sync-Back

### Export (Neo4j → Vault)

```bash
python -m graph_builder --export
```

- Queries all nodes from Neo4j and writes markdown files to `data_vault/`
- Pipeline-owned fields are always overwritten
- Human-owned fields are preserved from existing files
- Shared fields (e.g., `aliases`) are union-merged
- Writes to staging directory first, then atomic-moves per file

### Sync-Back (Vault → Neo4j)

```bash
python -m graph_builder --sync-back           # apply changes
python -m graph_builder --sync-back --dry-run  # preview only
```

Only syncs human-owned and shared fields — pipeline-owned fields are ignored.

| Field | Ownership | Sync Behavior |
|---|---|---|
| `name` (Concept) | Human | Vault overwrites Neo4j |
| `canonical_definition` | Human | Vault overwrites Neo4j |
| `human_notes` | Human | Vault overwrites Neo4j |
| `status` (Claim) | Human | Vault overwrites Neo4j |
| `aliases` | Shared | Union merge (never subtracts) |
| `status` (Concept) | Shared | Human can resolve `review_needed` → `canonical` |
| `slug`, `formal_spec`, ... | Pipeline | Ignored during sync-back |

**Round-trip invariance:** Export → sync-back with no human edits = zero diff.

## Running the Full Pipeline

End-to-end example using the K-Strong Price of Anarchy paper:

```bash
# Start Neo4j
docker compose up -d

# Stage 1: Ingest the paper
python -m data_loader --paper 2502.00425

# Stage 2: Clean the paper
python -m data_cleaner --paper 2502.00425

# Stage 3: Build the knowledge graph
python -m graph_builder --paper 2502.00425

# Export to Obsidian vault
python -m graph_builder --export

# Open data_vault/ in Obsidian and explore the graph
```

## Testing

```bash
# Run all tests
uv run pytest tests/ -v

# Run only unit tests (no external dependencies)
uv run pytest tests/ -v -m unit

# Run integration tests (requires Neo4j Docker)
uv run pytest tests/ -v -m integration

# Run end-to-end smoke tests
uv run pytest tests/ -v -m e2e

# Run a single test file
uv run pytest tests/test_concept_extractor.py -v
```

**Test markers** (defined in `pyproject.toml`):

| Marker | Description |
|---|---|
| `unit` | No external dependencies |
| `integration` | Requires Neo4j Docker (via testcontainers) |
| `e2e` | Full pipeline smoke test |
| `slow` | Tests taking > 10s |

Dev dependencies include `pytest`, `pytest-asyncio`, and `testcontainers[neo4j]`.

## Environment Variables

| Variable | Default | Required | Description |
|---|---|---|---|
| `DEEPSEEK_API_KEY` | — | Yes | DeepSeek API key for LLM extraction |
| `OPENAI_API_KEY` | — | No | OpenAI key for embedding-based dedup |
| `ANTHROPIC_API_KEY` | — | Yes | Anthropic API key for claim extraction and verification |
| `CLAIM_LLM` | `claude` | No | LLM backend for claim extraction (claude or deepseek) |
| `CLAUDE_MODEL` | `claude-opus-4-6` | No | Claude model name |
| `LLM_THINKING` | `True` | No | Enable chain-of-thought in DeepSeek |
| `DEEPSEEK_MODEL` | `deepseek-chat` | No | DeepSeek model name |
| `DEEPSEEK_BASE_URL` | `https://api.deepseek.com` | No | DeepSeek API base URL |
| `EMBEDDING_MODEL` | `text-embedding-3-small` | No | OpenAI embedding model |
| `EMBEDDING_DIMENSIONS` | `1536` | No | Embedding vector dimensions |
| `NEO4J_BOLT_URI` | `bolt://localhost:7687` | No | Neo4j Bolt connection URI |
| `NEO4J_AUTH_USER` | `neo4j` | No | Neo4j username |
| `NEO4J_AUTH_PASS` | `password` | No | Neo4j password |

## Project Structure

```
ETL/
├── data_loader/                # Stage 1: ArXiv paper ingestion
│   ├── cli.py                  #   CLI interface
│   ├── orchestrator.py         #   Workflow coordination
│   ├── paper_converter.py      #   PDF → JSON conversion
│   ├── metadata_fetcher.py     #   ArXiv API metadata
│   ├── input_reader.py         #   CSV parsing
│   ├── models.py               #   Pydantic models
│   ├── sdk.py                  #   High-level SDK
│   └── config.py               #   Configuration
│
├── data_cleaner/               # Stage 2: Text normalization
│   ├── cli.py                  #   CLI interface
│   ├── pipeline.py             #   6-stage orchestrator
│   ├── metadata_repairer.py    #   Stage 6
│   └── stages/                 #   Stages 1-5
│       ├── newline_normalizer.py
│       ├── latex_normalizer.py
│       ├── artifact_remover.py
│       ├── heading_normalizer.py
│       └── whitespace_cleaner.py
│
├── graph_builder/              # Stage 3: Knowledge graph extraction
│   ├── config/                 #   Configuration & schema
│   │   ├── config.py
│   │   ├── schema_loader.py
│   │   └── schema_types.py
│   ├── extraction/             #   Entity & relationship extraction
│   │   ├── concept_extractor.py
│   │   ├── claim_extractor.py
│   │   ├── claim_verifier.py     #   Pass 4 verification
│   │   ├── proof_linker.py       #   Proof location mapper
│   │   ├── concept_merger.py
│   │   ├── cross_section_linker.py
│   │   ├── edge_enricher.py
│   │   ├── prompt_generator.py
│   │   ├── section_splitter.py
│   │   └── dedup/              #   Deduplication cascade
│   │       ├── dedup_cascade.py
│   │       ├── embedding_client.py
│   │       └── fuzzy_matcher.py
│   ├── llm/                    #   LLM interaction layer
│   │   ├── llm_client.py
│   │   ├── claude_client.py      #   Claude async client
│   │   ├── protocol.py           #   LLMClient protocol
│   │   └── response_parser.py
│   ├── graph/                  #   Neo4j read/write
│   │   ├── neo4j_client.py
│   │   ├── graph_writer.py
│   │   └── graph_reader.py
│   ├── vault/                  #   Obsidian vault generation
│   │   ├── obsidian_exporter.py
│   │   ├── sync_back.py
│   │   ├── frontmatter_builder.py
│   │   ├── body_renderer.py
│   │   └── manifest.py
│   ├── validation/             #   Graph validation
│   │   ├── validator.py
│   │   └── cycle_detector.py
│   ├── models/                 #   Data models
│   │   ├── concept.py
│   │   ├── claim.py
│   │   ├── edges.py
│   │   ├── source.py
│   │   └── provenance.py
│   └── orchestrator/           #   Pipeline orchestration
│       ├── cli.py
│       ├── orchestrator.py
│       ├── pass_helpers.py       #   Extracted pass helper functions
│       └── batch_processor.py
│
├── data_vault/                 # Output: Obsidian vault
│   ├── concepts/
│   ├── claims/{type}/
│   ├── sources/
│   ├── _meta/schema.yaml
│   └── _review/
│
├── tests/                      # Test suite (540+ tests)
│   ├── conftest.py
│   ├── fixtures/
│   └── test_*.py
│
├── docs/                       # Design documents
│   └── superpowers/specs/
│
├── main.py                    # Unified CLI entry point
├── docker-compose.yml
├── pyproject.toml
└── CLAUDE.md
```

## Design Documents

- [Data Loader Design](docs/superpowers/specs/2026-03-15-data-loader-design.md) — Stage 1 architecture
- [Data Loader SDK/API Design](docs/superpowers/specs/2026-03-15-data-loader-sdk-api-design.md) — Programmatic interface
- [Knowledge Graph Builder Design](docs/superpowers/specs/2026-03-15-knowledge-graph-builder-design.md) — Original v1 design
- [Dual-Graph KG Builder Design](docs/superpowers/specs/2026-03-16-dual-graph-kg-builder-design.md) — Current v2 dual-graph architecture
- [Extraction Quality Overhaul](docs/superpowers/specs/2026-03-16-extraction-quality-overhaul-design.md) — Claude upgrade, proof extraction, verification pass
