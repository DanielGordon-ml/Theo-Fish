# Data Loader SDK & API Design Spec

## Overview

The Data Loader SDK and API extend the core data loader pipeline with two additional interfaces beyond the CLI:

1. **SDK** — High-level Python API for notebooks and downstream pipeline stages
2. **FastAPI Service** — HTTP endpoints with async job queue for remote triggering

All three interfaces (CLI, SDK, API) funnel through the same core modules via the SDK layer.

## Architecture

```
CLI  ──→  SDK  ──→  Orchestrator  ──→  Core Modules
API  ──→  SDK  ──→  Orchestrator  ──→  Core Modules
              ↘ Job Store
```

The SDK is the central programmatic interface. The CLI calls SDK functions. The API wraps SDK functions with HTTP endpoints and an async job queue.

## SDK (`data_loader/sdk.py`)

### Public Functions

```python
async def load_paper(arxiv_id: str, **kwargs) -> PaperResult:
    """Load a single paper. Raises LoaderError on failure."""

async def load_papers(
    arxiv_ids: list[str],
    csv_path: Path | None = None,
    output_dir: Path | None = None,
    papers_dir: Path | None = None,
    concurrency: int = DEFAULT_CONCURRENCY,
    force: bool = False,
) -> BatchResult:
    """Load multiple papers. Never raises — failures captured in BatchResult."""

def is_processed(arxiv_id: str, output_dir: Path | None = None) -> bool:
    """Check if a paper's JSON already exists on disk."""
```

### Behavior

- `load_paper()` normalizes the ID, creates a single-item batch, calls the orchestrator, and returns a `PaperResult`. Raises `LoaderError` if the paper fails.
- `load_papers()` normalizes all IDs, optionally reads a CSV, merges and deduplicates inputs, calls the orchestrator, and returns a `BatchResult`. Never raises — individual failures are captured in the result.
- `is_processed()` checks whether `{output_dir}/{arxiv_id}.json` exists on disk.
- All SDK functions call `setup_logger()` internally on first use.

## Models

### PaperResult

```python
class PaperResult(BaseModel):
    arxiv_id: str
    status: str           # "processed", "skipped", "failed"
    converter: str | None = None
    error: str | None = None
    output_path: str | None = None
```

### BatchResult

```python
class BatchResult(BaseModel):
    total: int
    processed: int
    skipped: int
    failed: int
    arxiv2md: int
    mineru: int
    results: list[PaperResult]
```

### LoaderError

```python
class LoaderError(Exception):
    """Raised by SDK when a single-paper load fails."""
    def __init__(self, arxiv_id: str, reason: str):
        super().__init__(f"[{arxiv_id}] {reason}")
        self.arxiv_id = arxiv_id
        self.reason = reason
```

## FastAPI Service (`data_loader/api.py`)

### Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/papers` | Submit single paper for processing |
| `POST` | `/papers/batch` | Submit batch of papers |
| `GET` | `/jobs/{job_id}` | Poll job status |
| `GET` | `/papers/{arxiv_id}` | Read processed JSON from disk |
| `GET` | `/health` | Health check |

### Request/Response Models

**POST /papers**
```json
// Request
{"arxiv_id": "1706.03762", "force": false}

// Response (202 Accepted)
{"job_id": "uuid4", "status": "pending"}
```

**POST /papers/batch**
```json
// Request
{"arxiv_ids": ["1706.03762", "1810.04805"], "force": false}

// Response (202 Accepted)
{"job_id": "uuid4", "status": "pending"}
```

**GET /jobs/{job_id}**
```json
// Response
{
  "job_id": "uuid4",
  "status": "completed",  // "pending", "running", "completed", "failed"
  "result": { ... },       // PaperResult or BatchResult when complete
  "error": null,
  "created_at": "ISO timestamp",
  "completed_at": "ISO timestamp"
}
```

**GET /papers/{arxiv_id}**
```json
// Response: the full PaperDocument JSON from disk
```

**GET /health**
```json
{"status": "ok"}
```

### Async Job Queue

- Jobs submitted via POST are processed using `asyncio.create_task()`.
- Job state is tracked in an in-memory `JobStore` (dict-based).
- Jobs are lost on server restart — JSON files on disk are the durable record.

## Job Store (`data_loader/job_store.py`)

```python
class JobStore:
    """In-memory job tracking."""

    def create(self, job_type: str) -> str:
        """Create a new job, return UUID4 job_id."""

    def get(self, job_id: str) -> dict | None:
        """Get job status. Returns None if not found."""

    def update(self, job_id: str, **kwargs) -> None:
        """Update job fields: status, result, error, completed_at."""
```

## Design Decisions

| Decision | Choice | Why |
|----------|--------|-----|
| SDK as central layer | CLI + API both call SDK | Single source of truth, no logic duplication |
| High-level SDK only | `load_paper()` / `load_papers()` | Simple, opinionated — users don't need internals |
| Async job queue | `asyncio.create_task()` + in-memory store | On-demand usage, no infrastructure needed |
| In-memory jobs | Dict-based, lost on restart | JSON files on disk are the durable record |
| `BatchResult` model | Replaces plain dict from orchestrator | Typed, serializable, usable across all interfaces |
| `LoaderError` exception | SDK raises for single-paper failures | Clean error handling — batch never raises |

## Package Exports (`data_loader/__init__.py`)

```python
from data_loader.sdk import load_paper, load_papers, is_processed
from data_loader.models import PaperResult, BatchResult, PaperDocument
from data_loader.errors import LoaderError
```

## Dependencies

Added to `pyproject.toml`:
- `fastapi>=0.115`
- `uvicorn[standard]`

Dev dependencies:
- `httpx` (for FastAPI TestClient)
