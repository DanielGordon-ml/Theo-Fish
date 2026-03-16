# Knowledge Graph Builder — Design Spec

## Context

The Theo-Fish ETL pipeline has two completed modules: **Data Loader** (ingests ArXiv papers → JSON) and **Data Cleaner** (normalizes text → cleaned JSON). The **Knowledge Graph Builder** is the third module. It reads cleaned JSON from `Data/cleaned/`, uses LLM-powered extraction (DeepSeek V3.2) to identify mathematical entities and their relationships, and outputs an Obsidian markdown vault in `ETL/data_vault/`.

**Why:** Academic math papers contain rich, interconnected mathematical concepts (definitions, theorems, lemmas, proofs) that are difficult to navigate in linear form. By extracting these into a knowledge graph viewable in Obsidian, researchers can visually explore relationships between concepts, trace proof dependencies, and discover connections across papers.

## Architecture

### Module: `graph_builder/` (15 source files)

```
graph_builder/
  __init__.py                 # Public API: build_graph, build_graphs, is_built
  __main__.py                 # python -m graph_builder entry point
  cli.py                      # argparse CLI
  config.py                   # Paths, constants, DeepSeek config, .env loading
  errors.py                   # GraphBuilderError
  logger.py                   # WARNING+ to logs/graph_builder.log
  models.py                   # Pydantic: EntityType, ExtractedEntity, Relationship, PaperGraph, BuildResult
  section_splitter.py         # TOC stripping, heading-based splitting, stub detection
  llm_client.py               # DeepSeek V3.2 via OpenAI SDK, rate limiting, retries, token tracking
  prompts.py                  # Entity extraction + relationship mapping prompt templates
  entity_extractor.py         # Per-section LLM extraction, dedup, proof attachment
  relationship_mapper.py      # Intra-paper relationships + cross-paper label matching
  vault_scanner.py            # Scan existing vault frontmatter into searchable index
  vault_writer.py             # Obsidian .md generation with YAML frontmatter + wikilinks
  orchestrator.py             # Async pipeline, batch processing
```

### Data Flow

```
Data/cleaned/*.json
  → Section Splitter (strip TOC, split on H1/H2, filter stubs)
  → Entity Extractor (1 DeepSeek call per section, JSON mode)
  → Deduplicate entities by (type, label)
  → Relationship Mapper (1 consolidation LLM call per paper)
  → Vault Scanner (scan existing vault for cross-paper matches)
  → Vault Writer (Obsidian .md with frontmatter + wikilinks)
  → data_vault/{sanitized_paper_title}/*.md
```

### Dependencies

```toml
"openai>=1.0",              # DeepSeek V3.2 via OpenAI SDK
"python-dotenv>=1.0",       # Load .env from Theo-Fish/.env
"pyyaml>=6.0",              # YAML frontmatter generation
```

### Environment Configuration

`.env` at `Theo-Fish/.env`:
- `DEEPSEEK_API_KEY` — API key for DeepSeek
- `LLM_THINKING=True` — enables thinking parameter

## Data Models

### EntityType (enum)
`definition`, `theorem`, `lemma`, `proposition`, `corollary`, `remark`, `example`, `exercise`, `algorithm`, `conjecture`, `notation`

### RelationshipType (enum)
`uses`, `generalizes`, `is-special-case-of`, `contradicts`, `implies`, `motivates`, `is-proved-by`, `extends`, `is-equivalent-to`, `depends-on`, `refines`, `is-example-of`

### Key Models

| Model | Fields | Purpose |
|-------|--------|---------|
| `Section` | heading, level, content, char_count, index | Chunked section for LLM |
| `ExtractedEntity` | entity_type, label, statement, proof?, section, section_index, context | Single extracted entity |
| `Relationship` | source_label, target_label, relationship_type, evidence | Directed edge |
| `PaperGraph` | arxiv_id, title, entities[], relationships[], token stats | Full extraction result |
| `VaultFile` | relative_path, frontmatter, body | File to write |
| `CrossPaperLink` | source/target paper+entity, confidence | Cross-paper match |
| `BuildResult` | arxiv_id, status, counts, error? | Per-paper result |
| `BatchBuildResult` | total, built, skipped, failed, results[] | Batch result |

## Component Details

### Section Splitter
1. Strip TOC — detect `# Contents` heading followed by bullet list, remove everything up to next non-TOC heading
2. Split on H1/H2 — each heading starts a new section
3. Sub-split oversized sections — if section > 30K chars, split on H3, then paragraph boundaries
4. Filter stubs — sections with <50 chars of non-heading content are TOC artifacts

### LLM Client
- Client: `openai.AsyncOpenAI(base_url=DEEPSEEK_BASE_URL, api_key=DEEPSEEK_API_KEY)`
- Model: `deepseek-chat` (DeepSeek V3.2)
- JSON mode: `response_format={"type": "json_object"}`
- Thinking: `extra_body={"thinking": {"type": "enabled"}}` when `LLM_THINKING=True`
- Rate limiting: `asyncio.Semaphore` (default 10 concurrent calls)
- Retries: Exponential backoff with jitter, 3 retries for 429/500/502/503

### Entity Extractor
1. Load cleaned JSON → split into sections → filter stubs
2. Dispatch concurrent LLM calls (1 per section, semaphore-limited)
3. Parse JSON responses into ExtractedEntity objects
4. Deduplicate by (entity_type, label) — keep longest statement
5. Attach orphan proofs ("Proof of Theorem X.Y" → attach to Theorem X.Y)

### Relationship Mapper
- Phase 1: Intra-paper — LLM identifies relationships between entities
- Phase 2: Cross-paper — label/tag matching against existing vault

### Vault Writer
Output structure: `data_vault/{sanitized_paper_title}/*.md`
Entity files include YAML frontmatter with type, label, paper, arxiv_id, section, related_entities, tags, date_extracted.
Wikilinks for intra-paper (`[[Theorem 1.5]]`) and cross-paper (`[[Paper Title/Theorem 1.5|Theorem 1.5 (Paper Title)]]`).

### CLI
```bash
python -m graph_builder --paper 1904.07272
python -m graph_builder --input-dir Data/cleaned/
python -m graph_builder --input-dir Data/cleaned/ --force
```

## Verification
1. Unit tests: all test files pass
2. Smoke test: creates vault files for real papers
3. Obsidian verification: graph view shows entities and relationships
4. Batch test: process all cleaned papers
5. Cross-paper links: wikilinks across paper folders resolve
