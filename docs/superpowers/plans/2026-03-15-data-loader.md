# Data Loader Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a Data Loader that ingests ArXiv papers, extracts content as markdown with inline LaTeX, fetches metadata, and outputs one JSON file per paper.

**Architecture:** Modular async pipeline — Input Reader, Metadata Fetcher, Paper Converter (arxiv2md primary + MinerU PDF fallback), JSON Writer — coordinated by an async orchestrator with semaphore-based concurrency control.

**Tech Stack:** Python 3.10+, uv, asyncio, httpx, pydantic, feedparser, arxiv2markdown, mineru

**Spec:** `docs/superpowers/specs/2026-03-15-data-loader-design.md`

---

## File Map

| File | Responsibility |
|------|---------------|
| `pyproject.toml` | Project config, dependencies |
| `data_loader/__init__.py` | Package marker |
| `data_loader/__main__.py` | `python -m data_loader` entry point |
| `data_loader/config.py` | Default paths and constants |
| `data_loader/logger.py` | Warning/error log file setup |
| `data_loader/models.py` | Pydantic models: PaperInput, PaperMetadata, ConversionResult, PaperDocument |
| `data_loader/input_reader.py` | CSV parsing, CLI arg merging, ArXiv ID normalization, deduplication |
| `data_loader/metadata_fetcher.py` | ArXiv API batch queries, frontmatter fallback, math subject lookup |
| `data_loader/paper_converter.py` | arxiv2md async conversion, MinerU fallback via ProcessPoolExecutor, PDF caching |
| `data_loader/json_writer.py` | PaperDocument assembly, JSON file writing, skip logic |
| `data_loader/orchestrator.py` | Async batch processing, semaphore concurrency, summary output |
| `data_loader/cli.py` | argparse CLI definition |
| `tests/test_models.py` | Model validation tests |
| `tests/test_input_reader.py` | CSV/CLI/normalization tests |
| `tests/test_metadata_fetcher.py` | API parsing and fallback tests |
| `tests/test_paper_converter.py` | Converter fallback logic tests |
| `tests/test_json_writer.py` | JSON assembly and skip logic tests |
| `tests/test_orchestrator.py` | End-to-end batch processing tests |
| `tests/__init__.py` | Test package marker |
| `tests/conftest.py` | Shared fixtures (tmp dirs, sample data) |
| `tests/test_logger.py` | Logger setup and format tests |

---

## Chunk 1: Project Setup and Foundation

### Task 1: Project Scaffolding

**Files:**
- Create: `pyproject.toml`
- Create: `data_loader/__init__.py`
- Create: `data_loader/__main__.py`
- Create: `.gitignore`

- [ ] **Step 1: Create `pyproject.toml`**

```toml
[project]
name = "theo-fish-etl"
version = "0.1.0"
description = "ETL pipeline for ingesting ArXiv academic papers"
requires-python = ">=3.10"
dependencies = [
    "arxiv2markdown",
    "mineru[all]",
    "httpx",
    "pydantic>=2.0",
    "feedparser",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0",
    "pytest-asyncio>=0.23",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

- [ ] **Step 2: Create `.gitignore`**

```gitignore
__pycache__/
*.pyc
.venv/
*.egg-info/
dist/
logs/*.log
```

- [ ] **Step 3: Create `data_loader/__init__.py`**

```python
"""Theo-Fish ETL Data Loader — ingests ArXiv papers into structured JSON."""
```

- [ ] **Step 4: Create `data_loader/__main__.py`**

Placeholder that will call CLI later:

```python
"""Entry point for `python -m data_loader`."""

from data_loader.cli import main

if __name__ == "__main__":
    main()
```

- [ ] **Step 5: Create `tests/__init__.py`**

```python
```

- [ ] **Step 6: Install the project**

Run: `uv venv && uv pip install -e ".[dev]"`
Expected: installs successfully, all dependencies resolved.

Note: `mineru[all]` is a large install (~20GB of models downloaded on first use). This step may take several minutes. If the install fails due to platform-specific issues with MinerU (e.g., PyTorch version conflicts), try `uv pip install -e ".[dev]" --exclude mineru` first to unblock development, then resolve MinerU installation separately.

- [ ] **Step 7: Commit**

```bash
git init
git add pyproject.toml .gitignore data_loader/__init__.py data_loader/__main__.py tests/__init__.py
git commit -m "feat: scaffold data_loader project with dependencies"
```

---

### Task 2: Config Module

**Files:**
- Create: `data_loader/config.py`
- Create: `tests/conftest.py`

- [ ] **Step 1: Create `data_loader/config.py`**

```python
"""Default paths and constants for the data loader."""

from pathlib import Path

# Paths relative to project root for portability
PROJECT_ROOT = Path(__file__).resolve().parents[1]  # ETL/
DATA_DIR = PROJECT_ROOT.parent / "Data"             # Theo-Fish/Data/
PAPERS_DIR = DATA_DIR / "papers"
PROCESSED_DIR = DATA_DIR / "processed"
LOG_DIR = PROJECT_ROOT / "logs"

# Filename sanitization: legacy ArXiv IDs contain slashes (e.g., cs/0512078)
def sanitize_arxiv_id(arxiv_id: str) -> str:
    """Convert an ArXiv ID to a safe filename component."""
    return arxiv_id.replace("/", "_")

# Concurrency
DEFAULT_CONCURRENCY = 5

# ArXiv API
ARXIV_API_URL = "http://export.arxiv.org/api/query"
ARXIV_API_DELAY = 3.0          # seconds between API batches
ARXIV_API_BATCH_SIZE = 20
```

- [ ] **Step 2: Create `tests/conftest.py`**

```python
"""Shared test fixtures."""

import pytest
from pathlib import Path


@pytest.fixture
def tmp_data_dir(tmp_path):
    """Create a temporary data directory structure."""
    papers_dir = tmp_path / "papers"
    processed_dir = tmp_path / "processed"
    papers_dir.mkdir()
    processed_dir.mkdir()
    return tmp_path


@pytest.fixture
def sample_csv(tmp_path):
    """Create a sample CSV input file."""
    csv_content = (
        'paper_name,file_path,file_type\n'
        '"Attention Is All You Need",2706.03762,pdf\n'
        '"BERT",1810.04805,html\n'
    )
    csv_file = tmp_path / "papers.csv"
    csv_file.write_text(csv_content)
    return csv_file
```

- [ ] **Step 3: Verify config paths resolve correctly**

Run: `python -c "from data_loader.config import PROJECT_ROOT, DATA_DIR; print(PROJECT_ROOT); print(DATA_DIR)"`
Expected: prints the ETL directory and the Data directory paths.

- [ ] **Step 4: Commit**

```bash
git add data_loader/config.py tests/conftest.py
git commit -m "feat: add config module with default paths and test fixtures"
```

---

### Task 3: Logger Module

**Files:**
- Create: `data_loader/logger.py`

- [ ] **Step 1: Create `data_loader/logger.py`**

```python
"""Logging setup — WARNING and ERROR only to file."""

import logging
from pathlib import Path

from data_loader.config import LOG_DIR


def setup_logger(log_dir: Path | None = None) -> logging.Logger:
    """Configure and return the data loader logger.

    Writes WARNING+ to logs/loader.log. Creates log directory if needed.
    """
    log_dir = log_dir or LOG_DIR
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "loader.log"

    logger = logging.getLogger("data_loader")
    logger.setLevel(logging.WARNING)

    # Avoid duplicate handlers on repeated calls
    if not logger.handlers:
        handler = logging.FileHandler(log_file, mode="a", encoding="utf-8")
        handler.setLevel(logging.WARNING)
        formatter = logging.Formatter(
            "%(asctime)s %(levelname)-7s [%(arxiv_id)s] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


def get_logger() -> logging.Logger:
    """Get the data_loader logger (must call setup_logger first)."""
    return logging.getLogger("data_loader")
```

- [ ] **Step 2: Write failing tests for logger**

Create `tests/test_logger.py`:

```python
"""Tests for logger setup and formatting."""

import logging
from data_loader.logger import setup_logger


class TestSetupLogger:
    def test_creates_log_file(self, tmp_path):
        logger = setup_logger(log_dir=tmp_path)
        log_file = tmp_path / "loader.log"
        logger.warning("test warning", extra={"arxiv_id": "2706.03762"})
        assert log_file.exists()
        content = log_file.read_text()
        assert "WARNING" in content
        assert "2706.03762" in content

    def test_writes_error(self, tmp_path):
        logger = setup_logger(log_dir=tmp_path)
        logger.error("test error", extra={"arxiv_id": "9999.99999"})
        content = (tmp_path / "loader.log").read_text()
        assert "ERROR" in content
        assert "9999.99999" in content

    def test_ignores_info(self, tmp_path):
        logger = setup_logger(log_dir=tmp_path)
        logger.info("should not appear", extra={"arxiv_id": "0000.00000"})
        content = (tmp_path / "loader.log").read_text()
        assert "should not appear" not in content

    def test_appends_across_calls(self, tmp_path):
        # Reset logger handlers for clean test
        log = logging.getLogger("data_loader")
        log.handlers.clear()
        logger = setup_logger(log_dir=tmp_path)
        logger.warning("first", extra={"arxiv_id": "1111.11111"})
        # Simulate a second run (clear and re-setup)
        log.handlers.clear()
        logger = setup_logger(log_dir=tmp_path)
        logger.warning("second", extra={"arxiv_id": "2222.22222"})
        content = (tmp_path / "loader.log").read_text()
        assert "first" in content
        assert "second" in content
```

- [ ] **Step 3: Run logger tests to verify they fail**

Run: `uv run pytest tests/test_logger.py -v`
Expected: FAIL — `ImportError`

- [ ] **Step 4: Run logger tests to verify they pass** (after creating logger.py in step 1)

Run: `uv run pytest tests/test_logger.py -v`
Expected: all 4 tests PASS.

- [ ] **Step 5: Commit**

```bash
git add data_loader/logger.py tests/test_logger.py
git commit -m "feat: add logger module — WARNING/ERROR only to file, append mode"
```

---

### Task 4: Pydantic Models

**Files:**
- Create: `data_loader/models.py`
- Create: `tests/test_models.py`

- [ ] **Step 1: Write failing tests for models**

Create `tests/test_models.py`:

```python
"""Tests for Pydantic data models."""

from data_loader.models import PaperInput, PaperMetadata, ConversionResult, PaperDocument


class TestPaperInput:
    def test_create_with_all_fields(self):
        p = PaperInput(
            paper_name="Test Paper",
            arxiv_id="2706.03762",
            file_type="pdf",
        )
        assert p.paper_name == "Test Paper"
        assert p.arxiv_id == "2706.03762"
        assert p.file_type == "pdf"

    def test_create_minimal(self):
        p = PaperInput(arxiv_id="2706.03762")
        assert p.paper_name is None
        assert p.file_type is None


class TestPaperMetadata:
    def test_create_full(self):
        m = PaperMetadata(
            arxiv_id="2706.03762",
            title="Attention Is All You Need",
            authors=["Vaswani", "Shazeer"],
            abstract="The dominant sequence...",
            publication_date="2017-06-12",
            categories=["cs.CL", "cs.LG"],
            primary_category="cs.CL",
            math_subject="cs.CL",
            source="arxiv_api",
        )
        assert m.title == "Attention Is All You Need"
        assert len(m.authors) == 2
        assert m.source == "arxiv_api"


class TestConversionResult:
    def test_create(self):
        c = ConversionResult(
            arxiv_id="2706.03762",
            markdown_content="# Title\nSome content with $E=mc^2$",
            converter_used="arxiv2md",
            conversion_warnings=[],
        )
        assert c.converter_used == "arxiv2md"
        assert "$E=mc^2$" in c.markdown_content


class TestPaperDocument:
    def test_create_full(self):
        d = PaperDocument(
            paper_name="Attention Is All You Need",
            arxiv_id="2706.03762",
            title="Attention Is All You Need",
            authors=["Vaswani", "Shazeer"],
            abstract="The dominant sequence...",
            publication_date="2017-06-12",
            categories=["cs.CL", "cs.LG"],
            primary_category="cs.CL",
            math_subject="cs.CL",
            extracted_text_markdown="# Full paper markdown",
            metadata_source="arxiv_api",
            converter_used="arxiv2md",
            conversion_warnings=[],
            processed_at="2026-03-15T14:30:00",
        )
        assert d.paper_name == "Attention Is All You Need"
        assert d.processed_at == "2026-03-15T14:30:00"

    def test_json_roundtrip(self):
        d = PaperDocument(
            paper_name="Test",
            arxiv_id="2706.03762",
            title="Test",
            authors=["A"],
            abstract="abs",
            publication_date="2017-06-12",
            categories=["math.AG"],
            primary_category="math.AG",
            math_subject="Algebraic Geometry",
            extracted_text_markdown="# Content",
            metadata_source="arxiv_api",
            converter_used="arxiv2md",
            conversion_warnings=["minor issue"],
            processed_at="2026-03-15T14:30:00",
        )
        json_str = d.model_dump_json(indent=2)
        d2 = PaperDocument.model_validate_json(json_str)
        assert d == d2
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `uv run pytest tests/test_models.py -v`
Expected: FAIL — `ImportError: cannot import name 'PaperInput' from 'data_loader.models'`

- [ ] **Step 3: Implement models**

Create `data_loader/models.py`:

```python
"""Pydantic models for the data loader pipeline."""

from pydantic import BaseModel


class PaperInput(BaseModel):
    """A paper to process — from CSV or CLI input."""

    arxiv_id: str
    paper_name: str | None = None
    file_type: str | None = None  # "pdf" or "html" hint


class PaperMetadata(BaseModel):
    """Metadata fetched from ArXiv API or frontmatter fallback."""

    arxiv_id: str
    title: str
    authors: list[str]
    abstract: str
    publication_date: str
    categories: list[str]
    primary_category: str
    math_subject: str
    source: str  # "arxiv_api" or "frontmatter_fallback"


class ConversionResult(BaseModel):
    """Result of converting a paper to markdown."""

    arxiv_id: str
    markdown_content: str
    converter_used: str  # "arxiv2md" or "mineru"
    conversion_warnings: list[str]


class PaperDocument(BaseModel):
    """Final output document — one per paper, written as JSON."""

    paper_name: str
    arxiv_id: str
    title: str
    authors: list[str]
    abstract: str
    publication_date: str
    categories: list[str]
    primary_category: str
    math_subject: str
    extracted_text_markdown: str
    metadata_source: str
    converter_used: str
    conversion_warnings: list[str]
    processed_at: str
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `uv run pytest tests/test_models.py -v`
Expected: all 5 tests PASS.

- [ ] **Step 5: Commit**

```bash
git add data_loader/models.py tests/test_models.py
git commit -m "feat: add Pydantic models — PaperInput, PaperMetadata, ConversionResult, PaperDocument"
```

---

## Chunk 2: Input Reader

### Task 5: ArXiv ID Normalization

**Files:**
- Create: `data_loader/input_reader.py`
- Create: `tests/test_input_reader.py`

- [ ] **Step 1: Write failing tests for ArXiv ID normalization**

Create `tests/test_input_reader.py`:

```python
"""Tests for input reading, normalization, and deduplication."""

import pytest
from data_loader.input_reader import normalize_arxiv_id, read_csv, read_cli_papers, merge_inputs


class TestNormalizeArxivId:
    def test_raw_id(self):
        assert normalize_arxiv_id("2706.03762") == "2706.03762"

    def test_versioned_id(self):
        assert normalize_arxiv_id("2706.03762v1") == "2706.03762"

    def test_abs_url(self):
        assert normalize_arxiv_id("https://arxiv.org/abs/2706.03762") == "2706.03762"

    def test_abs_url_versioned(self):
        assert normalize_arxiv_id("https://arxiv.org/abs/2706.03762v2") == "2706.03762"

    def test_pdf_url(self):
        assert normalize_arxiv_id("https://arxiv.org/pdf/2706.03762") == "2706.03762"

    def test_arxiv_prefix(self):
        assert normalize_arxiv_id("arxiv:2706.03762") == "2706.03762"

    def test_legacy_id(self):
        assert normalize_arxiv_id("cs/0512078v2") == "cs/0512078"

    def test_invalid_returns_none(self):
        assert normalize_arxiv_id("not-an-id") is None

    def test_empty_string_returns_none(self):
        assert normalize_arxiv_id("") is None
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `uv run pytest tests/test_input_reader.py::TestNormalizeArxivId -v`
Expected: FAIL — `ImportError`

- [ ] **Step 3: Implement normalization**

Create `data_loader/input_reader.py`:

```python
"""Read and normalize paper inputs from CSV files and CLI arguments."""

import csv
import re
import logging
from pathlib import Path

from data_loader.models import PaperInput

logger = logging.getLogger("data_loader")

# Matches new-style ArXiv IDs: YYMM.NNNNN (with optional version)
_NEW_ID_RE = re.compile(r"^(\d{4}\.\d{4,5})(v\d+)?$")
# Matches legacy ArXiv IDs: category/NNNNNNN (with optional version)
_LEGACY_ID_RE = re.compile(r"^([a-z-]+/\d{7})(v\d+)?$")
# Extracts ID from ArXiv URLs
_URL_RE = re.compile(r"arxiv\.org/(?:abs|pdf|html)/([a-z-]*/?\d+\.?\d*)(v\d+)?")


def normalize_arxiv_id(raw: str) -> str | None:
    """Normalize an ArXiv identifier to its canonical form (no version suffix).

    Accepts: raw IDs, versioned IDs, full URLs, arxiv:-prefixed IDs.
    Returns None if the input cannot be parsed.
    """
    raw = raw.strip()
    if not raw:
        return None

    # Strip arxiv: prefix
    if raw.lower().startswith("arxiv:"):
        raw = raw[6:]

    # Try URL extraction
    url_match = _URL_RE.search(raw)
    if url_match:
        return url_match.group(1)

    # Try new-style ID
    new_match = _NEW_ID_RE.match(raw)
    if new_match:
        return new_match.group(1)

    # Try legacy ID
    legacy_match = _LEGACY_ID_RE.match(raw)
    if legacy_match:
        return legacy_match.group(1)

    return None
```

- [ ] **Step 4: Run normalization tests**

Run: `uv run pytest tests/test_input_reader.py::TestNormalizeArxivId -v`
Expected: all 9 tests PASS.

- [ ] **Step 5: Commit**

```bash
git add data_loader/input_reader.py tests/test_input_reader.py
git commit -m "feat: add ArXiv ID normalization with URL/version/prefix handling"
```

---

### Task 6: CSV Reading and Input Merging

**Files:**
- Modify: `data_loader/input_reader.py`
- Modify: `tests/test_input_reader.py`

- [ ] **Step 1: Write failing tests for CSV reading and merging**

Append to `tests/test_input_reader.py`:

```python
class TestReadCsv:
    def test_reads_valid_csv(self, sample_csv):
        papers = read_csv(sample_csv)
        assert len(papers) == 2
        assert papers[0].arxiv_id == "2706.03762"
        assert papers[0].paper_name == "Attention Is All You Need"
        assert papers[0].file_type == "pdf"
        assert papers[1].arxiv_id == "1810.04805"

    def test_skips_invalid_ids(self, tmp_path):
        csv_file = tmp_path / "bad.csv"
        csv_file.write_text(
            'paper_name,file_path,file_type\n'
            '"Good Paper",2706.03762,pdf\n'
            '"Bad Paper",not-a-valid-id,pdf\n'
        )
        papers = read_csv(csv_file)
        assert len(papers) == 1
        assert papers[0].arxiv_id == "2706.03762"

    def test_empty_csv(self, tmp_path):
        csv_file = tmp_path / "empty.csv"
        csv_file.write_text('paper_name,file_path,file_type\n')
        papers = read_csv(csv_file)
        assert papers == []


class TestReadCliPapers:
    def test_reads_cli_papers(self):
        papers = read_cli_papers(["2706.03762", "1810.04805"])
        assert len(papers) == 2
        assert papers[0].arxiv_id == "2706.03762"
        assert papers[0].paper_name is None

    def test_skips_invalid_cli(self):
        papers = read_cli_papers(["2706.03762", "garbage"])
        assert len(papers) == 1


class TestMergeInputs:
    def test_deduplicates(self):
        csv_papers = [PaperInput(arxiv_id="2706.03762", paper_name="From CSV")]
        cli_papers = [PaperInput(arxiv_id="2706.03762")]
        merged = merge_inputs(csv_papers, cli_papers)
        assert len(merged) == 1
        assert merged[0].paper_name == "From CSV"  # CSV entry takes priority

    def test_merges_unique(self):
        csv_papers = [PaperInput(arxiv_id="2706.03762", paper_name="Paper A")]
        cli_papers = [PaperInput(arxiv_id="1810.04805")]
        merged = merge_inputs(csv_papers, cli_papers)
        assert len(merged) == 2
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `uv run pytest tests/test_input_reader.py -v -k "not TestNormalize"`
Expected: FAIL — `ImportError: cannot import name 'read_csv'`

- [ ] **Step 3: Implement CSV reading and merging**

Add to `data_loader/input_reader.py`:

```python
def read_csv(csv_path: Path) -> list[PaperInput]:
    """Read papers from a CSV file with columns: paper_name, file_path, file_type.

    Normalizes ArXiv IDs. Skips rows with invalid IDs (logs warning).
    """
    papers = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            arxiv_id = normalize_arxiv_id(row["file_path"])
            if arxiv_id is None:
                logger.warning(
                    "Skipping invalid ArXiv ID in CSV: %s",
                    row["file_path"],
                    extra={"arxiv_id": row["file_path"]},
                )
                continue
            papers.append(PaperInput(
                arxiv_id=arxiv_id,
                paper_name=row.get("paper_name") or None,
                file_type=row.get("file_type") or None,
            ))
    return papers


def read_cli_papers(paper_ids: list[str]) -> list[PaperInput]:
    """Create PaperInput list from CLI --paper arguments.

    Normalizes IDs. Skips invalid ones (logs warning).
    """
    papers = []
    for raw_id in paper_ids:
        arxiv_id = normalize_arxiv_id(raw_id)
        if arxiv_id is None:
            logger.warning(
                "Skipping invalid ArXiv ID from CLI: %s",
                raw_id,
                extra={"arxiv_id": raw_id},
            )
            continue
        papers.append(PaperInput(arxiv_id=arxiv_id))
    return papers


def merge_inputs(
    csv_papers: list[PaperInput],
    cli_papers: list[PaperInput],
) -> list[PaperInput]:
    """Merge CSV and CLI inputs, deduplicating by ArXiv ID.

    CSV entries take priority (they have paper_name and file_type).
    """
    seen: dict[str, PaperInput] = {}
    for paper in csv_papers:
        seen[paper.arxiv_id] = paper
    for paper in cli_papers:
        if paper.arxiv_id not in seen:
            seen[paper.arxiv_id] = paper
    return list(seen.values())
```

- [ ] **Step 4: Run all input reader tests**

Run: `uv run pytest tests/test_input_reader.py -v`
Expected: all 14 tests PASS.

- [ ] **Step 5: Commit**

```bash
git add data_loader/input_reader.py tests/test_input_reader.py
git commit -m "feat: add CSV reading, CLI parsing, and input merging with dedup"
```

---

## Chunk 3: Metadata Fetcher

### Task 7: Math Subject Lookup and ArXiv API Parsing

**Files:**
- Create: `data_loader/metadata_fetcher.py`
- Create: `tests/test_metadata_fetcher.py`

- [ ] **Step 1: Write failing tests for math subject lookup and API response parsing**

Create `tests/test_metadata_fetcher.py`:

```python
"""Tests for ArXiv metadata fetching."""

import pytest
from data_loader.metadata_fetcher import (
    get_math_subject,
    parse_arxiv_entry,
    parse_frontmatter_metadata,
)
from data_loader.models import PaperMetadata


class TestGetMathSubject:
    def test_known_category(self):
        assert get_math_subject("math.AG") == "Algebraic Geometry"

    def test_unknown_math_category(self):
        # Should return the raw code if not in mapping
        result = get_math_subject("math.ZZ")
        assert result == "math.ZZ"

    def test_non_math_category(self):
        assert get_math_subject("cs.CL") == "cs.CL"

    def test_physics_category(self):
        assert get_math_subject("hep-th") == "hep-th"


# Sample Atom XML entry as returned by ArXiv API
SAMPLE_ENTRY_XML = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:arxiv="http://arxiv.org/schemas/atom">
  <entry>
    <id>http://arxiv.org/abs/2706.03762v1</id>
    <title>Attention Is All You Need</title>
    <summary>The dominant sequence transduction models...</summary>
    <published>2017-06-12T17:57:34Z</published>
    <author><name>Ashish Vaswani</name></author>
    <author><name>Noam Shazeer</name></author>
    <arxiv:primary_category term="cs.CL" />
    <category term="cs.CL" />
    <category term="cs.LG" />
  </entry>
</feed>"""


class TestParseArxivEntry:
    def test_parses_entry(self):
        import feedparser
        feed = feedparser.parse(SAMPLE_ENTRY_XML)
        entry = feed.entries[0]
        metadata = parse_arxiv_entry(entry)
        assert metadata.arxiv_id == "2706.03762"
        assert metadata.title == "Attention Is All You Need"
        assert metadata.authors == ["Ashish Vaswani", "Noam Shazeer"]
        assert metadata.publication_date == "2017-06-12"
        assert metadata.categories == ["cs.CL", "cs.LG"]
        assert metadata.primary_category == "cs.CL"
        assert metadata.source == "arxiv_api"
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `uv run pytest tests/test_metadata_fetcher.py -v`
Expected: FAIL — `ImportError`

- [ ] **Step 3: Implement math subject lookup and entry parsing**

Create `data_loader/metadata_fetcher.py`:

```python
"""Fetch paper metadata from ArXiv API with frontmatter fallback."""

import asyncio
import logging
import re
from typing import Any

import feedparser
import httpx

from data_loader.config import ARXIV_API_URL, ARXIV_API_DELAY, ARXIV_API_BATCH_SIZE
from data_loader.models import PaperInput, PaperMetadata

logger = logging.getLogger("data_loader")

# Full mapping of math.* ArXiv categories to human-readable names
MATH_SUBJECTS: dict[str, str] = {
    "math.AC": "Commutative Algebra",
    "math.AG": "Algebraic Geometry",
    "math.AP": "Analysis of PDEs",
    "math.AT": "Algebraic Topology",
    "math.CA": "Classical Analysis and ODEs",
    "math.CO": "Combinatorics",
    "math.CT": "Category Theory",
    "math.CV": "Complex Variables",
    "math.DG": "Differential Geometry",
    "math.DS": "Dynamical Systems",
    "math.FA": "Functional Analysis",
    "math.GM": "General Mathematics",
    "math.GN": "General Topology",
    "math.GR": "Group Theory",
    "math.GT": "Geometric Topology",
    "math.HO": "History and Overview",
    "math.IT": "Information Theory",
    "math.KT": "K-Theory and Homology",
    "math.LO": "Logic",
    "math.MG": "Metric Geometry",
    "math.MP": "Mathematical Physics",
    "math.NA": "Numerical Analysis",
    "math.NT": "Number Theory",
    "math.OA": "Operator Algebras",
    "math.OC": "Optimization and Control",
    "math.PR": "Probability",
    "math.QA": "Quantum Algebra",
    "math.RA": "Rings and Algebras",
    "math.RT": "Representation Theory",
    "math.SG": "Symplectic Geometry",
    "math.SP": "Spectral Theory",
    "math.ST": "Statistics Theory",
    "math-ph": "Mathematical Physics",
}


def get_math_subject(primary_category: str) -> str:
    """Resolve a category code to a human-readable math subject name.

    Returns the raw category code if not in the math mapping.
    """
    return MATH_SUBJECTS.get(primary_category, primary_category)


def parse_arxiv_entry(entry: Any) -> PaperMetadata:
    """Parse a single feedparser entry into PaperMetadata."""
    # Extract ArXiv ID from the entry URL
    raw_id = entry.id  # e.g. "http://arxiv.org/abs/2706.03762v1"
    arxiv_id = re.search(r"abs/(.+?)(?:v\d+)?$", raw_id)
    arxiv_id = arxiv_id.group(1) if arxiv_id else raw_id

    authors = [a.get("name", "") for a in entry.get("authors", [])]
    categories = [t["term"] for t in entry.get("tags", [])]

    primary_category = ""
    if hasattr(entry, "arxiv_primary_category"):
        primary_category = entry.arxiv_primary_category.get("term", "")
    elif categories:
        primary_category = categories[0]

    publication_date = entry.get("published", "")[:10]  # "2017-06-12T..." → "2017-06-12"

    return PaperMetadata(
        arxiv_id=arxiv_id,
        title=entry.get("title", "").replace("\n", " ").strip(),
        authors=authors,
        abstract=entry.get("summary", "").strip(),
        publication_date=publication_date,
        categories=categories,
        primary_category=primary_category,
        math_subject=get_math_subject(primary_category),
        source="arxiv_api",
    )
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `uv run pytest tests/test_metadata_fetcher.py -v`
Expected: all 5 tests PASS.

- [ ] **Step 5: Commit**

```bash
git add data_loader/metadata_fetcher.py tests/test_metadata_fetcher.py
git commit -m "feat: add math subject lookup and ArXiv API entry parsing"
```

---

### Task 8: Async Batch Metadata Fetching

**Files:**
- Modify: `data_loader/metadata_fetcher.py`
- Modify: `tests/test_metadata_fetcher.py`

- [ ] **Step 1: Write failing test for batch fetching**

Append to `tests/test_metadata_fetcher.py`:

```python
@pytest.mark.asyncio
class TestParseFrontmatterMetadata:
    async def test_extracts_frontmatter(self, monkeypatch):
        """Should parse YAML frontmatter from arxiv2md output."""
        from data_loader.metadata_fetcher import parse_frontmatter_metadata

        async def mock_ingest(paper_id, **kwargs):
            class MockResult:
                markdown = '---\ntitle: "Test Paper"\nauthors: ["Author A", "Author B"]\nurl: https://arxiv.org/abs/2706.03762\n---\n# Content'
            return MockResult()

        monkeypatch.setattr("data_loader.metadata_fetcher.ingest_paper", mock_ingest)
        # Also need to patch at module level for the import inside the function
        import data_loader.metadata_fetcher as mf
        original = mf.parse_frontmatter_metadata

        async def patched_frontmatter(arxiv_id):
            # Monkey-patch the ingest_paper import
            import arxiv2md.ingestion
            monkeypatch.setattr(arxiv2md.ingestion, "ingest_paper", mock_ingest)
            return await original(arxiv_id)

        result = await patched_frontmatter("2706.03762")
        assert result is not None
        assert result.source == "frontmatter_fallback"

    async def test_returns_none_on_failure(self, monkeypatch):
        """Should return None when arxiv2md fails."""
        from data_loader.metadata_fetcher import parse_frontmatter_metadata

        async def mock_ingest(paper_id, **kwargs):
            raise RuntimeError("No HTML version")

        monkeypatch.setattr(
            "arxiv2md.ingestion.ingest_paper",
            mock_ingest,
        )
        result = await parse_frontmatter_metadata("9999.99999")
        assert result is None


@pytest.mark.asyncio
class TestFetchAllMetadata:
    async def test_fetches_batch(self, monkeypatch):
        """Test batch fetching with a mocked HTTP response."""
        from data_loader.metadata_fetcher import fetch_all_metadata
        from data_loader.models import PaperInput

        # Mock httpx response with sample Atom XML
        async def mock_get(self, url, **kwargs):
            class MockResponse:
                status_code = 200
                text = SAMPLE_ENTRY_XML
            return MockResponse()

        monkeypatch.setattr(httpx.AsyncClient, "get", mock_get)

        papers = [PaperInput(arxiv_id="2706.03762")]
        async with httpx.AsyncClient() as client:
            result = await fetch_all_metadata(papers, client)

        assert "2706.03762" in result
        assert result["2706.03762"].title == "Attention Is All You Need"

    async def test_handles_timeout(self, monkeypatch):
        """API timeout should return empty dict, not crash."""
        from data_loader.metadata_fetcher import fetch_all_metadata
        from data_loader.models import PaperInput

        async def mock_get(self, url, **kwargs):
            raise httpx.TimeoutException("Connection timed out")

        monkeypatch.setattr(httpx.AsyncClient, "get", mock_get)

        papers = [PaperInput(arxiv_id="2706.03762")]
        async with httpx.AsyncClient() as client:
            result = await fetch_all_metadata(papers, client)

        assert result == {}

    async def test_returns_empty_for_missing(self, monkeypatch):
        """Papers not in API response are not in the result dict."""
        from data_loader.metadata_fetcher import fetch_all_metadata
        from data_loader.models import PaperInput

        async def mock_get(self, url, **kwargs):
            class MockResponse:
                status_code = 200
                text = SAMPLE_ENTRY_XML  # Only has 2706.03762
            return MockResponse()

        monkeypatch.setattr(httpx.AsyncClient, "get", mock_get)

        papers = [
            PaperInput(arxiv_id="2706.03762"),
            PaperInput(arxiv_id="9999.99999"),
        ]
        async with httpx.AsyncClient() as client:
            result = await fetch_all_metadata(papers, client)

        assert "2706.03762" in result
        assert "9999.99999" not in result
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `uv run pytest tests/test_metadata_fetcher.py::TestFetchAllMetadata -v`
Expected: FAIL — `ImportError: cannot import name 'fetch_all_metadata'`

- [ ] **Step 3: Implement batch fetching**

Add to `data_loader/metadata_fetcher.py`:

```python
async def parse_frontmatter_metadata(arxiv_id: str) -> PaperMetadata | None:
    """Extract metadata from arxiv2md's frontmatter as a fallback.

    Calls arxiv2md with frontmatter enabled and parses the YAML header.
    Returns None if extraction fails.
    """
    try:
        from arxiv2md.ingestion import ingest_paper
        result = await ingest_paper(arxiv_id)
        markdown = result.markdown if hasattr(result, "markdown") else str(result)

        # Parse YAML frontmatter if present (between --- delimiters)
        title, authors = "", []
        if markdown.startswith("---"):
            end = markdown.find("---", 3)
            if end != -1:
                frontmatter = markdown[3:end]
                for line in frontmatter.strip().split("\n"):
                    if line.startswith("title:"):
                        title = line[6:].strip().strip('"').strip("'")
                    elif line.startswith("authors:"):
                        # Simple comma-separated parsing
                        authors_str = line[8:].strip().strip("[]")
                        authors = [a.strip().strip('"').strip("'") for a in authors_str.split(",") if a.strip()]

        return PaperMetadata(
            arxiv_id=arxiv_id,
            title=title,
            authors=authors,
            abstract="",
            publication_date="",
            categories=[],
            primary_category="",
            math_subject="",
            source="frontmatter_fallback",
        )
    except Exception as e:
        logger.warning(
            "Frontmatter metadata extraction failed: %s", str(e),
            extra={"arxiv_id": arxiv_id},
        )
        return None


async def _fetch_batch(
    arxiv_ids: list[str],
    client: httpx.AsyncClient,
) -> dict[str, PaperMetadata]:
    """Fetch metadata for a batch of ArXiv IDs (max 20)."""
    id_list = ",".join(arxiv_ids)
    url = f"{ARXIV_API_URL}?id_list={id_list}&max_results={len(arxiv_ids)}"

    try:
        response = await client.get(url, timeout=30.0)
        response.raise_for_status()
    except (httpx.HTTPError, httpx.TimeoutException) as e:
        for aid in arxiv_ids:
            logger.error(
                "ArXiv API request failed: %s", str(e),
                extra={"arxiv_id": aid},
            )
        return {}

    feed = feedparser.parse(response.text)
    results: dict[str, PaperMetadata] = {}

    for entry in feed.entries:
        try:
            metadata = parse_arxiv_entry(entry)
            results[metadata.arxiv_id] = metadata
        except Exception as e:
            logger.warning(
                "Failed to parse ArXiv entry: %s", str(e),
                extra={"arxiv_id": "unknown"},
            )

    return results


async def fetch_all_metadata(
    papers: list[PaperInput],
    client: httpx.AsyncClient,
) -> dict[str, PaperMetadata]:
    """Fetch metadata for all papers in batches, respecting rate limits.

    Returns a dict mapping arxiv_id → PaperMetadata.
    Papers not found via the API are omitted from the dict.
    """
    arxiv_ids = [p.arxiv_id for p in papers]
    all_metadata: dict[str, PaperMetadata] = {}

    for i in range(0, len(arxiv_ids), ARXIV_API_BATCH_SIZE):
        batch = arxiv_ids[i : i + ARXIV_API_BATCH_SIZE]
        batch_result = await _fetch_batch(batch, client)
        all_metadata.update(batch_result)

        # Rate limit: wait between batches (skip after last batch)
        if i + ARXIV_API_BATCH_SIZE < len(arxiv_ids):
            await asyncio.sleep(ARXIV_API_DELAY)

    return all_metadata
```

- [ ] **Step 4: Run all metadata fetcher tests**

Run: `uv run pytest tests/test_metadata_fetcher.py -v`
Expected: all 10 tests PASS.

- [ ] **Step 5: Commit**

```bash
git add data_loader/metadata_fetcher.py tests/test_metadata_fetcher.py
git commit -m "feat: add async batch metadata fetching with rate limiting"
```

---

## Chunk 4: Paper Converter

### Task 9: arxiv2md Integration

**Files:**
- Create: `data_loader/paper_converter.py`
- Create: `tests/test_paper_converter.py`

- [ ] **Step 1: Write failing tests for arxiv2md conversion**

Create `tests/test_paper_converter.py`:

```python
"""Tests for paper conversion with arxiv2md and MinerU fallback."""

import pytest
from pathlib import Path
from data_loader.paper_converter import convert_with_arxiv2md, convert_with_mineru, convert_paper
from data_loader.models import ConversionResult


@pytest.mark.asyncio
class TestConvertWithArxiv2md:
    async def test_success(self, monkeypatch):
        """Mock arxiv2md to return markdown content."""
        async def mock_ingest(paper_id, **kwargs):
            class MockResult:
                markdown = "# Test Paper\n\nContent with $E=mc^2$"
            return MockResult()

        monkeypatch.setattr(
            "data_loader.paper_converter._call_arxiv2md",
            mock_ingest,
        )
        result = await convert_with_arxiv2md("2706.03762")
        assert result is not None
        assert result.converter_used == "arxiv2md"
        assert "$E=mc^2$" in result.markdown_content

    async def test_failure_returns_none(self, monkeypatch):
        """When arxiv2md raises, return None."""
        async def mock_ingest(paper_id, **kwargs):
            raise RuntimeError("No HTML version available")

        monkeypatch.setattr(
            "data_loader.paper_converter._call_arxiv2md",
            mock_ingest,
        )
        result = await convert_with_arxiv2md("2706.03762")
        assert result is None


@pytest.mark.asyncio
class TestConvertPaper:
    async def test_uses_arxiv2md_when_available(self, monkeypatch):
        """Should use arxiv2md as primary."""
        async def mock_arxiv2md(arxiv_id):
            return ConversionResult(
                arxiv_id=arxiv_id,
                markdown_content="# From arxiv2md",
                converter_used="arxiv2md",
                conversion_warnings=[],
            )

        monkeypatch.setattr(
            "data_loader.paper_converter.convert_with_arxiv2md",
            mock_arxiv2md,
        )
        result = await convert_paper("2706.03762", papers_dir=Path("/tmp"))
        assert result is not None
        assert result.converter_used == "arxiv2md"

    async def test_falls_back_to_mineru(self, monkeypatch):
        """When arxiv2md fails, should fall back to MinerU."""
        async def mock_arxiv2md(arxiv_id):
            return None

        async def mock_mineru(arxiv_id, papers_dir):
            return ConversionResult(
                arxiv_id=arxiv_id,
                markdown_content="# From MinerU",
                converter_used="mineru",
                conversion_warnings=[],
            )

        monkeypatch.setattr(
            "data_loader.paper_converter.convert_with_arxiv2md",
            mock_arxiv2md,
        )
        monkeypatch.setattr(
            "data_loader.paper_converter.convert_with_mineru",
            mock_mineru,
        )
        result = await convert_paper("2706.03762", papers_dir=Path("/tmp"))
        assert result is not None
        assert result.converter_used == "mineru"

    async def test_both_fail_returns_none(self, monkeypatch):
        """When both converters fail, return None."""
        async def mock_arxiv2md(arxiv_id):
            return None

        async def mock_mineru(arxiv_id, papers_dir):
            return None

        monkeypatch.setattr(
            "data_loader.paper_converter.convert_with_arxiv2md",
            mock_arxiv2md,
        )
        monkeypatch.setattr(
            "data_loader.paper_converter.convert_with_mineru",
            mock_mineru,
        )
        result = await convert_paper("2706.03762", papers_dir=Path("/tmp"))
        assert result is None
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `uv run pytest tests/test_paper_converter.py -v`
Expected: FAIL — `ImportError`

- [ ] **Step 3: Implement paper converter**

Create `data_loader/paper_converter.py`:

```python
"""Convert ArXiv papers to markdown using arxiv2md (primary) and MinerU (fallback)."""

import asyncio
import logging
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import httpx

from data_loader.models import ConversionResult

logger = logging.getLogger("data_loader")

# Process pool for CPU-bound MinerU calls
_executor = ProcessPoolExecutor(max_workers=2)


async def _call_arxiv2md(paper_id: str) -> object:
    """Call arxiv2md's ingest_paper. Thin wrapper for monkeypatching."""
    from arxiv2md.ingestion import ingest_paper
    return await ingest_paper(paper_id)


async def convert_with_arxiv2md(arxiv_id: str) -> ConversionResult | None:
    """Try converting a paper using arxiv2md (HTML-based).

    Returns None if conversion fails.
    """
    try:
        result = await _call_arxiv2md(arxiv_id)
        markdown = result.markdown if hasattr(result, "markdown") else str(result)
        return ConversionResult(
            arxiv_id=arxiv_id,
            markdown_content=markdown,
            converter_used="arxiv2md",
            conversion_warnings=[],
        )
    except Exception as e:
        logger.warning(
            "arxiv2md failed: %s, falling back to MinerU",
            str(e),
            extra={"arxiv_id": arxiv_id},
        )
        return None


def _run_mineru(pdf_path: str, output_dir: str) -> str:
    """Run MinerU in a separate process (CPU-bound).

    This function is called via ProcessPoolExecutor, so it must be
    a top-level function (picklable) and import MinerU inside.
    """
    from pathlib import Path
    # NOTE: mineru.cli.common is an internal API path — may change between MinerU versions.
    # If this import breaks after a MinerU update, check their docs for the new entry point.
    from mineru.cli.common import parse_doc

    parse_doc(
        path_list=[Path(pdf_path)],
        output_dir=output_dir,
        backend="pipeline",
        method="auto",
        lang="en",
    )

    # MinerU writes output to output_dir/<filename>/<filename>.md
    stem = Path(pdf_path).stem
    md_path = Path(output_dir) / stem / f"{stem}.md"
    if md_path.exists():
        return md_path.read_text(encoding="utf-8")
    # Try alternate output patterns
    for md_file in Path(output_dir).rglob("*.md"):
        return md_file.read_text(encoding="utf-8")
    raise FileNotFoundError(f"MinerU produced no markdown output for {pdf_path}")


async def _download_pdf(arxiv_id: str, papers_dir: Path) -> Path | None:
    """Download a PDF from ArXiv to the cache directory.

    Returns the path to the cached PDF, or None on failure.
    Skips download if the file already exists.
    """
    from data_loader.config import sanitize_arxiv_id
    pdf_path = papers_dir / f"{sanitize_arxiv_id(arxiv_id)}.pdf"
    if pdf_path.exists():
        return pdf_path

    papers_dir.mkdir(parents=True, exist_ok=True)
    url = f"https://arxiv.org/pdf/{arxiv_id}"

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, follow_redirects=True, timeout=60.0)
            response.raise_for_status()
            pdf_path.write_bytes(response.content)
            return pdf_path
    except (httpx.HTTPError, httpx.TimeoutException) as e:
        logger.error(
            "PDF download failed: %s",
            str(e),
            extra={"arxiv_id": arxiv_id},
        )
        return None


async def convert_with_mineru(
    arxiv_id: str,
    papers_dir: Path,
) -> ConversionResult | None:
    """Try converting a paper using MinerU (PDF-based fallback).

    Downloads the PDF if not cached, then runs MinerU via ProcessPoolExecutor.
    Returns None if conversion fails.
    """
    pdf_path = await _download_pdf(arxiv_id, papers_dir)
    if pdf_path is None:
        return None

    loop = asyncio.get_running_loop()
    import tempfile
    with tempfile.TemporaryDirectory() as tmp_out:
        try:
            markdown = await loop.run_in_executor(
                _executor,
                _run_mineru,
                str(pdf_path),
                tmp_out,
            )
            return ConversionResult(
                arxiv_id=arxiv_id,
                markdown_content=markdown,
                converter_used="mineru",
                conversion_warnings=[],
            )
        except Exception as e:
            logger.error(
                "MinerU conversion failed: %s",
                str(e),
                extra={"arxiv_id": arxiv_id},
            )
            return None


async def convert_paper(
    arxiv_id: str,
    papers_dir: Path,
) -> ConversionResult | None:
    """Convert a paper using arxiv2md, falling back to MinerU.

    Returns None if both converters fail.
    """
    result = await convert_with_arxiv2md(arxiv_id)
    if result is not None:
        return result

    result = await convert_with_mineru(arxiv_id, papers_dir)
    if result is not None:
        return result

    logger.error(
        "Both converters failed — skipping paper",
        extra={"arxiv_id": arxiv_id},
    )
    return None
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `uv run pytest tests/test_paper_converter.py -v`
Expected: all 5 tests PASS.

- [ ] **Step 5: Commit**

```bash
git add data_loader/paper_converter.py tests/test_paper_converter.py
git commit -m "feat: add paper converter with arxiv2md primary + MinerU PDF fallback"
```

---

## Chunk 5: JSON Writer

### Task 10: JSON Assembly and File Writing

**Files:**
- Create: `data_loader/json_writer.py`
- Create: `tests/test_json_writer.py`

- [ ] **Step 1: Write failing tests**

Create `tests/test_json_writer.py`:

```python
"""Tests for JSON document assembly and writing."""

import json
import pytest
from pathlib import Path
from data_loader.json_writer import assemble_document, write_document, should_skip
from data_loader.models import PaperInput, PaperMetadata, ConversionResult, PaperDocument


@pytest.fixture
def sample_metadata():
    return PaperMetadata(
        arxiv_id="2706.03762",
        title="Attention Is All You Need",
        authors=["Vaswani", "Shazeer"],
        abstract="The dominant sequence...",
        publication_date="2017-06-12",
        categories=["cs.CL", "cs.LG"],
        primary_category="cs.CL",
        math_subject="cs.CL",
        source="arxiv_api",
    )


@pytest.fixture
def sample_conversion():
    return ConversionResult(
        arxiv_id="2706.03762",
        markdown_content="# Attention Is All You Need\n\nContent...",
        converter_used="arxiv2md",
        conversion_warnings=[],
    )


class TestAssembleDocument:
    def test_assembles_with_csv_name(self, sample_metadata, sample_conversion):
        paper_input = PaperInput(arxiv_id="2706.03762", paper_name="Custom Name")
        doc = assemble_document(paper_input, sample_metadata, sample_conversion)
        assert doc.paper_name == "Custom Name"
        assert doc.title == "Attention Is All You Need"
        assert doc.metadata_source == "arxiv_api"
        assert doc.converter_used == "arxiv2md"
        assert doc.processed_at  # should be set

    def test_uses_title_when_no_paper_name(self, sample_metadata, sample_conversion):
        paper_input = PaperInput(arxiv_id="2706.03762")
        doc = assemble_document(paper_input, sample_metadata, sample_conversion)
        assert doc.paper_name == "Attention Is All You Need"

    def test_uses_arxiv_id_when_no_name_or_title(self, sample_conversion):
        metadata = PaperMetadata(
            arxiv_id="2706.03762", title="", authors=[], abstract="",
            publication_date="", categories=[], primary_category="",
            math_subject="", source="arxiv_api",
        )
        paper_input = PaperInput(arxiv_id="2706.03762")
        doc = assemble_document(paper_input, metadata, sample_conversion)
        assert doc.paper_name == "2706.03762"


class TestShouldSkip:
    def test_skip_when_exists(self, tmp_data_dir):
        processed = tmp_data_dir / "processed"
        (processed / "2706.03762.json").write_text("{}")
        assert should_skip("2706.03762", processed, force=False) is True

    def test_no_skip_when_missing(self, tmp_data_dir):
        processed = tmp_data_dir / "processed"
        assert should_skip("2706.03762", processed, force=False) is False

    def test_no_skip_when_force(self, tmp_data_dir):
        processed = tmp_data_dir / "processed"
        (processed / "2706.03762.json").write_text("{}")
        assert should_skip("2706.03762", processed, force=True) is False

    def test_skip_legacy_id_with_slash(self, tmp_data_dir):
        """Legacy IDs like cs/0512078 use underscore in filename."""
        processed = tmp_data_dir / "processed"
        (processed / "cs_0512078.json").write_text("{}")
        assert should_skip("cs/0512078", processed, force=False) is True


class TestWriteDocument:
    def test_writes_valid_json(self, tmp_data_dir, sample_metadata, sample_conversion):
        paper_input = PaperInput(arxiv_id="2706.03762", paper_name="Test")
        doc = assemble_document(paper_input, sample_metadata, sample_conversion)
        processed = tmp_data_dir / "processed"
        write_document(doc, processed)

        json_file = processed / "2706.03762.json"
        assert json_file.exists()

        data = json.loads(json_file.read_text())
        assert data["arxiv_id"] == "2706.03762"
        assert data["title"] == "Attention Is All You Need"

    def test_json_roundtrips(self, tmp_data_dir, sample_metadata, sample_conversion):
        paper_input = PaperInput(arxiv_id="2706.03762", paper_name="Test")
        doc = assemble_document(paper_input, sample_metadata, sample_conversion)
        processed = tmp_data_dir / "processed"
        write_document(doc, processed)

        loaded = PaperDocument.model_validate_json(
            (processed / "2706.03762.json").read_text()
        )
        assert loaded == doc
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `uv run pytest tests/test_json_writer.py -v`
Expected: FAIL — `ImportError`

- [ ] **Step 3: Implement JSON writer**

Create `data_loader/json_writer.py`:

```python
"""Assemble and write PaperDocument JSON files."""

import logging
from datetime import datetime, timezone
from pathlib import Path

from data_loader.models import PaperInput, PaperMetadata, ConversionResult, PaperDocument

logger = logging.getLogger("data_loader")


def assemble_document(
    paper_input: PaperInput,
    metadata: PaperMetadata,
    conversion: ConversionResult,
) -> PaperDocument:
    """Combine input, metadata, and conversion into a PaperDocument."""
    # Resolve paper_name: CSV name > title > arxiv_id
    paper_name = paper_input.paper_name or metadata.title or paper_input.arxiv_id

    return PaperDocument(
        paper_name=paper_name,
        arxiv_id=metadata.arxiv_id,
        title=metadata.title,
        authors=metadata.authors,
        abstract=metadata.abstract,
        publication_date=metadata.publication_date,
        categories=metadata.categories,
        primary_category=metadata.primary_category,
        math_subject=metadata.math_subject,
        extracted_text_markdown=conversion.markdown_content,
        metadata_source=metadata.source,
        converter_used=conversion.converter_used,
        conversion_warnings=conversion.conversion_warnings,
        processed_at=datetime.now(timezone.utc).isoformat(),
    )


def should_skip(arxiv_id: str, processed_dir: Path, force: bool) -> bool:
    """Check if a paper has already been processed."""
    if force:
        return False
    from data_loader.config import sanitize_arxiv_id
    json_file = processed_dir / f"{sanitize_arxiv_id(arxiv_id)}.json"
    return json_file.exists()


def write_document(doc: PaperDocument, processed_dir: Path) -> Path:
    """Write a PaperDocument to a JSON file. Returns the output path."""
    processed_dir.mkdir(parents=True, exist_ok=True)
    from data_loader.config import sanitize_arxiv_id
    json_file = processed_dir / f"{sanitize_arxiv_id(doc.arxiv_id)}.json"

    try:
        json_file.write_text(doc.model_dump_json(indent=2), encoding="utf-8")
    except Exception as e:
        logger.error(
            "Failed to write JSON: %s", str(e),
            extra={"arxiv_id": doc.arxiv_id},
        )
        raise

    return json_file
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `uv run pytest tests/test_json_writer.py -v`
Expected: all 8 tests PASS.

- [ ] **Step 5: Commit**

```bash
git add data_loader/json_writer.py tests/test_json_writer.py
git commit -m "feat: add JSON document assembly, skip logic, and file writing"
```

---

## Chunk 6: Orchestrator, CLI, and Integration

### Task 11: Async Orchestrator

**Files:**
- Create: `data_loader/orchestrator.py`
- Create: `tests/test_orchestrator.py`

- [ ] **Step 1: Write failing test for orchestrator**

Create `tests/test_orchestrator.py`:

```python
"""Tests for the async batch orchestrator."""

import pytest
from pathlib import Path
from data_loader.orchestrator import process_batch
from data_loader.models import PaperInput, PaperMetadata, ConversionResult


@pytest.mark.asyncio
class TestProcessBatch:
    async def test_processes_papers(self, tmp_data_dir, monkeypatch):
        """Full pipeline with mocked metadata + converter."""
        from data_loader import metadata_fetcher, paper_converter

        async def mock_fetch_all(papers, client):
            return {
                "2706.03762": PaperMetadata(
                    arxiv_id="2706.03762",
                    title="Test Paper",
                    authors=["Author"],
                    abstract="Abstract",
                    publication_date="2017-06-12",
                    categories=["cs.CL"],
                    primary_category="cs.CL",
                    math_subject="cs.CL",
                    source="arxiv_api",
                ),
            }

        async def mock_convert(arxiv_id, papers_dir):
            return ConversionResult(
                arxiv_id=arxiv_id,
                markdown_content="# Test\nContent",
                converter_used="arxiv2md",
                conversion_warnings=[],
            )

        monkeypatch.setattr(metadata_fetcher, "fetch_all_metadata", mock_fetch_all)
        monkeypatch.setattr(paper_converter, "convert_paper", mock_convert)

        papers = [PaperInput(arxiv_id="2706.03762", paper_name="Test Paper")]
        processed_dir = tmp_data_dir / "processed"
        papers_dir = tmp_data_dir / "papers"

        summary = await process_batch(
            papers=papers,
            processed_dir=processed_dir,
            papers_dir=papers_dir,
            concurrency=5,
            force=False,
        )

        assert summary["processed"] == 1
        assert summary["arxiv2md"] == 1
        assert summary["failed"] == 0
        assert (processed_dir / "2706.03762.json").exists()

    async def test_skips_existing(self, tmp_data_dir, monkeypatch):
        """Should skip already-processed papers."""
        from data_loader import metadata_fetcher, paper_converter

        async def mock_fetch_all(papers, client):
            return {}

        monkeypatch.setattr(metadata_fetcher, "fetch_all_metadata", mock_fetch_all)

        processed_dir = tmp_data_dir / "processed"
        (processed_dir / "2706.03762.json").write_text("{}")

        papers = [PaperInput(arxiv_id="2706.03762")]
        summary = await process_batch(
            papers=papers,
            processed_dir=processed_dir,
            papers_dir=tmp_data_dir / "papers",
            concurrency=5,
            force=False,
        )

        assert summary["skipped"] == 1
        assert summary["processed"] == 0

    async def test_handles_conversion_failure(self, tmp_data_dir, monkeypatch):
        """Papers that fail conversion are counted as failed."""
        from data_loader import metadata_fetcher, paper_converter

        async def mock_fetch_all(papers, client):
            return {
                "2706.03762": PaperMetadata(
                    arxiv_id="2706.03762", title="T", authors=[], abstract="",
                    publication_date="", categories=[], primary_category="",
                    math_subject="", source="arxiv_api",
                ),
            }

        async def mock_convert(arxiv_id, papers_dir):
            return None  # Both converters failed

        monkeypatch.setattr(metadata_fetcher, "fetch_all_metadata", mock_fetch_all)
        monkeypatch.setattr(paper_converter, "convert_paper", mock_convert)

        papers = [PaperInput(arxiv_id="2706.03762")]
        summary = await process_batch(
            papers=papers,
            processed_dir=tmp_data_dir / "processed",
            papers_dir=tmp_data_dir / "papers",
            concurrency=5,
            force=False,
        )

        assert summary["failed"] == 1
        assert summary["processed"] == 0
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `uv run pytest tests/test_orchestrator.py -v`
Expected: FAIL — `ImportError`

- [ ] **Step 3: Implement orchestrator**

Create `data_loader/orchestrator.py`:

```python
"""Async batch orchestrator for the data loader pipeline."""

import asyncio
import logging
from pathlib import Path

import httpx

from data_loader.json_writer import assemble_document, should_skip, write_document
from data_loader.metadata_fetcher import fetch_all_metadata, parse_frontmatter_metadata
from data_loader.models import PaperInput
from data_loader.paper_converter import convert_paper

logger = logging.getLogger("data_loader")


async def _process_one(
    paper: PaperInput,
    metadata_cache: dict,
    semaphore: asyncio.Semaphore,
    processed_dir: Path,
    papers_dir: Path,
    force: bool,
) -> dict:
    """Process a single paper. Returns a result dict with status info."""
    arxiv_id = paper.arxiv_id

    # Skip check
    if should_skip(arxiv_id, processed_dir, force):
        return {"arxiv_id": arxiv_id, "status": "skipped"}

    # Check metadata — try API cache first, then frontmatter fallback
    metadata = metadata_cache.get(arxiv_id)
    if metadata is None:
        logger.warning(
            "No API metadata, trying frontmatter fallback",
            extra={"arxiv_id": arxiv_id},
        )
        metadata = await parse_frontmatter_metadata(arxiv_id)
    if metadata is None:
        logger.error(
            "Both API and frontmatter metadata failed — skipping",
            extra={"arxiv_id": arxiv_id},
        )
        return {"arxiv_id": arxiv_id, "status": "failed", "reason": "no metadata"}

    # Convert (with concurrency limit)
    async with semaphore:
        conversion = await convert_paper(arxiv_id, papers_dir)

    if conversion is None:
        return {"arxiv_id": arxiv_id, "status": "failed", "reason": "conversion failed"}

    # Assemble and write
    try:
        doc = assemble_document(paper, metadata, conversion)
        write_document(doc, processed_dir)
        return {
            "arxiv_id": arxiv_id,
            "status": "processed",
            "converter": conversion.converter_used,
        }
    except Exception as e:
        logger.error(
            "Failed to write document: %s", str(e),
            extra={"arxiv_id": arxiv_id},
        )
        return {"arxiv_id": arxiv_id, "status": "failed", "reason": str(e)}


async def process_batch(
    papers: list[PaperInput],
    processed_dir: Path,
    papers_dir: Path,
    concurrency: int = 5,
    force: bool = False,
) -> dict:
    """Process a batch of papers concurrently.

    Returns a summary dict with counts of processed, skipped, failed papers.
    """
    semaphore = asyncio.Semaphore(concurrency)

    # Step 1: Fetch all metadata
    async with httpx.AsyncClient() as client:
        metadata_cache = await fetch_all_metadata(papers, client)

    # Step 2: Process papers concurrently
    tasks = [
        _process_one(paper, metadata_cache, semaphore, processed_dir, papers_dir, force)
        for paper in papers
    ]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    # Step 3: Build summary
    summary = {
        "total": len(papers),
        "processed": 0,
        "skipped": 0,
        "failed": 0,
        "arxiv2md": 0,
        "mineru": 0,
    }

    for r in results:
        if isinstance(r, Exception):
            summary["failed"] += 1
            continue
        status = r["status"]
        if status == "processed":
            summary["processed"] += 1
            converter = r.get("converter", "")
            if converter in summary:
                summary[converter] += 1
        elif status == "skipped":
            summary["skipped"] += 1
        elif status == "failed":
            summary["failed"] += 1

    return summary


def print_summary(summary: dict) -> None:
    """Print a human-readable processing summary to stdout."""
    total = summary["total"]
    processed = summary["processed"]
    print(f"\nProcessed: {processed}/{total}")
    if summary["arxiv2md"]:
        print(f"  - arxiv2md: {summary['arxiv2md']}")
    if summary["mineru"]:
        print(f"  - mineru:   {summary['mineru']}")
    if summary["skipped"]:
        print(f"Skipped (already exists): {summary['skipped']}")
    if summary["failed"]:
        print(f"Failed: {summary['failed']} (see logs/loader.log for details)")
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `uv run pytest tests/test_orchestrator.py -v`
Expected: all 3 tests PASS.

- [ ] **Step 5: Commit**

```bash
git add data_loader/orchestrator.py tests/test_orchestrator.py
git commit -m "feat: add async batch orchestrator with concurrency control and summary"
```

---

### Task 12: CLI Entry Point

**Files:**
- Create: `data_loader/cli.py`

- [ ] **Step 1: Implement CLI**

Create `data_loader/cli.py`:

```python
"""CLI entry point for the data loader."""

import argparse
import asyncio
import sys
from pathlib import Path

from data_loader.config import PROCESSED_DIR, PAPERS_DIR, DEFAULT_CONCURRENCY
from data_loader.input_reader import read_csv, read_cli_papers, merge_inputs
from data_loader.logger import setup_logger
from data_loader.orchestrator import process_batch, print_summary


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="data_loader",
        description="Load ArXiv papers into structured JSON.",
    )
    parser.add_argument(
        "--csv",
        type=Path,
        help="Path to CSV file with paper_name, file_path, file_type columns",
    )
    parser.add_argument(
        "--paper",
        action="append",
        default=[],
        help="ArXiv ID or URL to process (can be repeated)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=PROCESSED_DIR,
        help=f"Output directory for JSON files (default: {PROCESSED_DIR})",
    )
    parser.add_argument(
        "--papers-dir",
        type=Path,
        default=PAPERS_DIR,
        help=f"Directory for cached PDFs (default: {PAPERS_DIR})",
    )
    parser.add_argument(
        "--concurrency",
        type=int,
        default=DEFAULT_CONCURRENCY,
        help=f"Max concurrent paper conversions (default: {DEFAULT_CONCURRENCY})",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Reprocess papers even if JSON already exists",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if not args.csv and not args.paper:
        parser.error("Provide at least one of --csv or --paper")

    setup_logger()

    # Read inputs
    csv_papers = read_csv(args.csv) if args.csv else []
    cli_papers = read_cli_papers(args.paper)
    papers = merge_inputs(csv_papers, cli_papers)

    if not papers:
        print("No valid papers to process.")
        sys.exit(0)

    print(f"Processing {len(papers)} paper(s)...")

    # Run pipeline
    summary = asyncio.run(
        process_batch(
            papers=papers,
            processed_dir=args.output,
            papers_dir=args.papers_dir,
            concurrency=args.concurrency,
            force=args.force,
        )
    )

    print_summary(summary)

    # Exit with error code if any failures
    if summary["failed"] > 0:
        sys.exit(1)
```

- [ ] **Step 2: Verify CLI help works**

Run: `uv run python -m data_loader --help`
Expected: prints usage with all flags (--csv, --paper, --output, --papers-dir, --concurrency, --force).

- [ ] **Step 3: Verify CLI rejects empty input**

Run: `uv run python -m data_loader 2>&1; echo "Exit: $?"`
Expected: prints error "Provide at least one of --csv or --paper", exits non-zero.

- [ ] **Step 4: Commit**

```bash
git add data_loader/cli.py data_loader/__main__.py
git commit -m "feat: add CLI entry point with argparse — csv, paper, output, force flags"
```

---

### Task 13: Run All Tests

- [ ] **Step 1: Run the full test suite**

Run: `uv run pytest tests/ -v`
Expected: all tests PASS (approximately 30 tests across 5 test files).

- [ ] **Step 2: Fix any failures**

If any tests fail, fix them and re-run.

- [ ] **Step 3: Final commit**

```bash
git add -A
git commit -m "chore: ensure all tests pass — data loader v1 complete"
```

---

## Chunk 7: Manual Integration Test

### Task 14: End-to-End Smoke Test

This task verifies the full pipeline works against real ArXiv papers. It is a manual test, not automated.

- [ ] **Step 1: Create a test CSV**

Create `test_papers.csv` in the project root:

```csv
paper_name,file_path,file_type
"Attention Is All You Need",1706.03762,html
"BERT",1810.04805,html
```

- [ ] **Step 2: Run the loader**

Run: `uv run python -m data_loader --csv test_papers.csv --output ../Data/processed --papers-dir ../Data/papers`

Expected: processes 2 papers, creates JSON files in `Data/processed/`.

- [ ] **Step 3: Inspect output JSON**

Run: `cat ../Data/processed/1706.03762.json | python -m json.tool | head -30`

Expected: valid JSON with title, authors, abstract, markdown content with LaTeX math.

- [ ] **Step 4: Verify logging**

Run: `cat logs/loader.log`

Expected: either empty (no warnings/errors) or contains expected warnings about fallback usage.

- [ ] **Step 5: Test skip logic**

Run the same command again:
Run: `uv run python -m data_loader --csv test_papers.csv --output ../Data/processed --papers-dir ../Data/papers`

Expected: `Skipped (already exists): 2`, no reprocessing.

- [ ] **Step 6: Test force reprocess**

Run: `uv run python -m data_loader --csv test_papers.csv --output ../Data/processed --papers-dir ../Data/papers --force`

Expected: reprocesses both papers.

- [ ] **Step 7: Clean up and commit**

```bash
rm test_papers.csv
git add -A
git commit -m "chore: verified end-to-end smoke test passes"
```
