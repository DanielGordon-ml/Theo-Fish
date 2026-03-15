# Data Loader Design Spec

## Overview

The Data Loader is the first component of the Theo-Fish ETL pipeline. It ingests academic papers from ArXiv, extracts their content as markdown with inline LaTeX math, fetches structured metadata, and outputs one JSON file per paper for downstream processing by the Data Cleaner, Structurer, and Enricher stages.

## Scope

This spec covers **only the Data Loader** — not the full ETL pipeline. The Cleaner, Structurer, and Enricher will be designed and built in subsequent iterations.

**Deviation from parent spec (`data_module.md`):**
- The parent spec's JSON schema uses `extracted_text_latex` for the full text field. This spec uses `extracted_text_markdown` instead, because both arxiv2md and MinerU output markdown with inline LaTeX math — not pure LaTeX source. The field name reflects the actual content.
- The parent spec requires an `extracted_math` array with individually cataloged equations. This is deferred to the Data Structurer stage, which will parse math expressions from the markdown. Extracting them during loading would duplicate work.

## Extraction Strategy: Two-Tier with Automatic Fallback

1. **Primary — arxiv2md**: Async, HTML-based conversion. Fast, excellent math quality (pulls original LaTeX from HTML annotations). Installed via `pip install arxiv2markdown`.
2. **Fallback — MinerU**: PDF-based conversion with dedicated formula detection model. Triggers automatically when arxiv2md fails (no HTML version available). Installed via `uv pip install -U "mineru[all]"`.

## Architecture

Modular pipeline with async orchestrator (Approach B).

### Module Structure

```
ETL/
├── data_loader/
│   ├── __init__.py
│   ├── cli.py              # CLI entry point (argparse)
│   ├── input_reader.py     # CSV parsing + CLI arg merging
│   ├── metadata_fetcher.py # ArXiv API with frontmatter fallback
│   ├── paper_converter.py  # arxiv2md + MinerU fallback
│   ├── json_writer.py      # JSON assembly and file writing
│   ├── orchestrator.py     # async batch orchestrator
│   ├── logger.py           # warning/error-only log file setup
│   ├── models.py           # Pydantic models for paper data
│   └── config.py           # default paths and constants
├── data_vault/             # (existing Obsidian vault)
├── logs/
│   └── loader.log
├── data_module.md
└── pyproject.toml
```

### Data Flow

```
Input (CSV + CLI)
  → Input Reader: normalize ArXiv IDs, deduplicate
  → Metadata Fetcher: ArXiv API (batch) → frontmatter fallback
  → Paper Converter: arxiv2md → MinerU fallback
  → JSON Writer: assemble PaperDocument, write to disk
  → Summary: print results, log warnings/errors
```

## Component Details

### 1. Input Reader (`input_reader.py`)

**CSV format:**
```csv
paper_name,file_path,file_type
"Attention Is All You Need",2706.03762,pdf
"BERT",1810.04805,html
```

- `paper_name`: human-readable label
- `file_path`: ArXiv ID or full URL
- `file_type`: `pdf` or `html` (hint, not hard constraint)

**CLI interface:**
```bash
# Process from CSV
python -m data_loader --csv path/to/papers.csv

# Process single paper(s)
python -m data_loader --paper 2706.03762 --paper 1810.04805

# Both
python -m data_loader --csv papers.csv --paper 2706.03762

# Control output and concurrency
python -m data_loader --csv papers.csv --output ./output --concurrency 10

# Force reprocess existing
python -m data_loader --csv papers.csv --force
```

**Input normalization:**
- Accepts raw IDs (`2706.03762`), versioned IDs (`2706.03762v1`), full URLs (`https://arxiv.org/abs/2706.03762`), `arxiv:`-prefixed IDs
- All normalized to canonical ArXiv ID
- Duplicates across CSV + CLI merged (same ID = processed once)
- Malformed IDs logged as warnings and skipped
- For papers provided via `--paper` CLI flag without a CSV entry, `paper_name` defaults to the paper's title (from metadata) or the ArXiv ID if metadata fetch fails

### 2. Metadata Fetcher (`metadata_fetcher.py`)

**Primary: ArXiv API** (`http://export.arxiv.org/api/query`)

Fetches per paper: title, authors, abstract, publication_date, categories, primary_category.

**Fallback: arxiv2md frontmatter** — if API fails (timeout, rate limit, not found), extract metadata from arxiv2md's `--frontmatter` output.

**Implementation:**
- `httpx.AsyncClient` for async HTTP
- Batch queries: up to 20 IDs per request via `id_list` parameter
- ArXiv API returns Atom XML; responses are parsed using `feedparser`
- Rate limiting: 3-second delay between API batches (ArXiv policy)
- Results cached in dict keyed by ArXiv ID
- **Double failure handling:** If both ArXiv API and frontmatter fallback fail for a paper, log error and skip the paper (do not proceed with empty metadata)

**Model:**
```python
class PaperMetadata(BaseModel):
    arxiv_id: str
    title: str
    authors: list[str]
    abstract: str
    publication_date: str           # ISO format
    categories: list[str]           # e.g. ["math.AG", "math.AT"]
    primary_category: str           # e.g. "math.AG"
    math_subject: str               # e.g. "Algebraic Geometry"
    source: str                     # "arxiv_api" or "frontmatter_fallback"
```

**Math subject lookup:** Mapping from ArXiv category codes to human-readable names:
```python
MATH_SUBJECTS = {
    "math.AG": "Algebraic Geometry",
    "math.AT": "Algebraic Topology",
    "math.AP": "Analysis of PDEs",
    "math.DG": "Differential Geometry",
    "math.NT": "Number Theory",
    # ... full mapping for all math.* categories
}
```

Falls back to raw category code for non-math papers.

### 3. Paper Converter (`paper_converter.py`)

**Tier 1 — arxiv2md:**
- Calls async `ingest_paper()` with ArXiv ID
- Enables frontmatter extraction (metadata fallback)
- Returns markdown with inline LaTeX (`$...$` / `$$...$$`)

**Tier 2 — MinerU:**
- Triggers when arxiv2md fails
- Downloads PDF from `https://arxiv.org/pdf/{arxiv_id}` to cache (`Data/papers/{arxiv_id}.pdf`). If download fails (HTTP error, timeout, corrupt file), log error and skip paper.
- Calls `parse_doc()` with `backend="pipeline"` (CPU-compatible)
- **Async wrapping:** MinerU's `parse_doc()` is synchronous and CPU-bound. Must be offloaded via `asyncio.loop.run_in_executor()` with a `ProcessPoolExecutor` to avoid blocking the event loop. The semaphore is acquired *before* the executor call to control total concurrency.
- Returns markdown with LaTeX from formula detection

**Flow per paper:**
```
try arxiv2md(arxiv_id)
  → success: return markdown, source="arxiv2md"
  → failure: log warning
    → download PDF to cache (Data/papers/{arxiv_id}.pdf)
      → download failure: log error, return None (paper skipped)
    → try mineru(pdf_path) via run_in_executor
      → success: return markdown, source="mineru"
      → failure: log error, return None (paper skipped)
```

**Model:**
```python
class ConversionResult(BaseModel):
    arxiv_id: str
    markdown_content: str
    converter_used: str              # "arxiv2md" or "mineru"
    conversion_warnings: list[str]
```

**PDF caching:** Downloaded PDFs stored in `Data/papers/` for reuse. Skip re-download if file exists locally.

### 4. JSON Writer (`json_writer.py`)

**Assembles metadata + converted content into final JSON.**

**Model:**
```python
class PaperDocument(BaseModel):
    paper_name: str
    arxiv_id: str
    title: str
    authors: list[str]
    abstract: str
    publication_date: str
    categories: list[str]
    primary_category: str
    math_subject: str
    extracted_text_markdown: str     # full markdown with inline LaTeX
    metadata_source: str             # "arxiv_api" or "frontmatter_fallback"
    converter_used: str              # "arxiv2md" or "mineru"
    conversion_warnings: list[str]
    processed_at: str                # ISO timestamp
```

**Output structure:**
```
Theo-Fish/Data/                      # DATA_DIR (relative to project)
├── papers.csv                       # input CSV
├── papers/                          # cached PDFs
│   ├── 2706.03762.pdf
│   └── 1810.04805.pdf
└── processed/                       # output JSON files
    ├── 2706.03762.json
    └── 1810.04805.json
```

**File naming:** `{arxiv_id}.json` — guarantees uniqueness.

**Skip logic:** If `processed/{arxiv_id}.json` exists, skip unless `--force` flag provided. Makes re-runs idempotent.

### 5. Orchestrator (`orchestrator.py`)

```python
async def process_batch(papers: list[PaperInput], output_dir: Path, force: bool = False):
    semaphore = asyncio.Semaphore(5)  # max 5 concurrent papers

    async with httpx.AsyncClient() as client:
        # Step 1: Batch fetch metadata (respecting ArXiv 3s rate limit)
        metadata = await fetch_all_metadata(papers, client)

        # Step 2: Convert papers concurrently (with semaphore)
        tasks = [process_one(paper, metadata, semaphore, output_dir, force)
                 for paper in papers]
        results = await asyncio.gather(*tasks, return_exceptions=True)

    # Step 3: Print summary
    print_summary(results)
```

**Concurrency:**
- `Semaphore(5)` default — at most 5 concurrent conversions
- Configurable via `--concurrency` CLI flag
- ArXiv API: batched queries (20 IDs each), 3-second delay between batches
- All exceptions caught per-paper — never crashes the batch

**CLI summary output:**
```
Processed: 45/50
  - arxiv2md: 38
  - mineru:    7
Skipped (already exists): 3
Failed: 2 (see logs/loader.log for details)
```

### 6. Logger (`logger.py`)

**Log file:** `ETL/logs/loader.log`
- Level: `WARNING` and above only
- Console: brief progress via print (not logger)
- Python built-in `logging` module

**Format:**
```
2026-03-15 14:30:22 WARNING [2706.03762] arxiv2md failed: no HTML version, falling back to MinerU
2026-03-15 14:30:45 WARNING [2706.03762] MinerU: 3 formulas may have extraction errors
2026-03-15 14:31:02 ERROR   [9901.12345] Both converters failed: ConnectionTimeout
2026-03-15 14:31:02 ERROR   [9901.12345] Skipping paper: "Some Paper Title"
```

**What gets logged:**
- `WARNING`: converter fallbacks, metadata fallbacks, conversion quality issues, malformed inputs skipped
- `ERROR`: both converters failed, PDF download failures, JSON write failures

No log rotation in v1.

## Dependencies

**`pyproject.toml`:**
```toml
[project]
name = "theo-fish-etl"
version = "0.1.0"
requires-python = ">=3.10"
dependencies = [
    "arxiv2markdown",
    "mineru[all]",
    "httpx",
    "pydantic>=2.0",
    "feedparser",
]
```

**Package manager:** `uv`
- Install: `uv pip install -e .`
- No separate `requirements.txt` — `pyproject.toml` is the single source of truth

## Configuration (`config.py`)

Hardcoded defaults, overridable via CLI:

```python
# Paths relative to project root for portability
PROJECT_ROOT = Path(__file__).resolve().parents[1]  # ETL/
DATA_DIR = PROJECT_ROOT.parent / "Data"             # Theo-Fish/Data/
PAPERS_DIR = DATA_DIR / "papers"
PROCESSED_DIR = DATA_DIR / "processed"
LOG_DIR = PROJECT_ROOT / "logs"
DEFAULT_CONCURRENCY = 5
ARXIV_API_DELAY = 3.0          # seconds between API batches
ARXIV_API_BATCH_SIZE = 20
```

## Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Primary converter | arxiv2md | Best math quality — pulls original LaTeX from HTML |
| PDF fallback | MinerU | Built for scientific papers, best out-of-the-box formula detection |
| Concurrency model | asyncio with semaphore + ProcessPoolExecutor | arxiv2md is natively async; MinerU offloaded via run_in_executor |
| Metadata source | ArXiv API with frontmatter fallback | API is more reliable and structured |
| Output format | One JSON per paper | Simple, idempotent, easy to inspect |
| Math extraction | Inline in markdown, not separate array | Avoids duplication; Structurer stage parses math later |
| Package manager | uv | Fast, modern Python package management |
| Skip logic | Check for existing JSON | Idempotent re-runs without `--force` |

## Out of Scope (Future Stages)

- Data Cleaner (deduplication, error correction)
- Data Structurer (graph extraction: definitions, theorems, lemmas)
- Data Enricher (citations, missing proof steps, examples)
- Neo4j vs Obsidian decision for final storage
- PDF fallback for non-ArXiv papers
