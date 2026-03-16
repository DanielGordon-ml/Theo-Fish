# Data Loader

Downloads ArXiv papers and converts them into structured JSON — extracting titles, authors, abstracts, categories, and the full paper text as markdown (with LaTeX math preserved).

---

## Prerequisites

Before you start, make sure you have:

- **Python 3.10 or newer** — check with `python --version`
- **uv** package manager — install from [astral.sh/uv](https://astral.sh/uv)
- **Internet connection** — the loader fetches papers directly from ArXiv

---

## Installation

1. Open a terminal and navigate to the project folder:

   ```bash
   cd path/to/Theo-Fish/ETL
   ```

2. Create a virtual environment and install dependencies:

   ```bash
   uv venv
   uv pip install -e ".[dev]"
   ```

3. That's it. On the first run, if the loader needs MinerU (the PDF converter), it will download roughly 20 GB of model files. This only happens once.

---

## Quick Start

Process a single paper by its ArXiv ID:

```bash
python -m data_loader --paper 1706.03762
```

This downloads the "Attention Is All You Need" paper, extracts its content, and saves a JSON file to:

```
Theo-Fish/Data/processed/1706.03762.json
```

That JSON file contains everything — title, authors, abstract, categories, and the full text in markdown.

---

## Using a CSV File

If you have a list of papers to process, put them in a CSV file with this format:

```csv
paper_name,file_path,file_type
Attention Is All You Need,1706.03762,arxiv
Diffusion Models,2006.11239,arxiv
BERT,1810.04805,arxiv
```

Then run:

```bash
python -m data_loader --csv path/to/papers.csv
```

You can also combine a CSV with individual papers in one command:

```bash
python -m data_loader --csv papers.csv --paper 2301.07041
```

---

## Accepted ArXiv ID Formats

You don't need to worry about formatting your ArXiv IDs perfectly. The loader accepts all of these:

| Format | Example |
|--------|---------|
| Raw ID | `1706.03762` |
| Versioned | `1706.03762v2` |
| Abstract URL | `https://arxiv.org/abs/1706.03762` |
| PDF URL | `https://arxiv.org/pdf/1706.03762` |
| `arxiv:` prefix | `arxiv:1706.03762` |
| Legacy format | `math-ph/0603001` |

Version suffixes (like `v2`) are stripped automatically — you always get the latest version. If an ID can't be recognized, it's skipped and a warning is logged.

---

## All CLI Options

| Flag | Description | Default |
|------|-------------|---------|
| `--csv` | Path to a CSV file listing papers to process | *(none)* |
| `--paper` | An ArXiv ID or URL to process (repeatable) | *(none)* |
| `--output` | Directory where JSON files are saved | `Data/processed` |
| `--papers-dir` | Directory for caching downloaded PDFs | `Data/papers` |
| `--concurrency` | How many papers to process at the same time | `5` |
| `--force` | Reprocess papers even if their JSON already exists | off |

You must provide at least `--csv` or `--paper` (or both).

To process multiple individual papers, repeat the `--paper` flag:

```bash
python -m data_loader --paper 1706.03762 --paper 2006.11239 --paper 1810.04805
```

---

## Understanding the Output

Each processed paper becomes a JSON file at `Data/processed/{arxiv_id}.json`. Here's what a typical file looks like (trimmed for brevity):

```json
{
  "paper_name": "Attention Is All You Need",
  "arxiv_id": "1706.03762",
  "title": "Attention Is All You Need",
  "authors": ["Ashish Vaswani", "Noam Shazeer", "..."],
  "abstract": "The dominant sequence transduction models are based on...",
  "publication_date": "2017-06-12",
  "categories": ["cs.CL", "cs.LG"],
  "primary_category": "cs.CL",
  "math_subject": "",
  "extracted_text_markdown": "# Attention Is All You Need\n\n## Abstract\n...",
  "metadata_source": "arxiv_api",
  "converter_used": "arxiv2md",
  "conversion_warnings": [],
  "processed_at": "2026-03-15T10:30:00"
}
```

**What each field means:**

| Field | What it contains |
|-------|-----------------|
| `paper_name` | Display name for the paper |
| `arxiv_id` | The normalized ArXiv identifier |
| `title` | Paper title from ArXiv metadata |
| `authors` | List of author names |
| `abstract` | The paper's abstract |
| `publication_date` | When the paper was published (ISO format) |
| `categories` | All ArXiv categories the paper belongs to |
| `primary_category` | The main category |
| `math_subject` | Math subject classification (if applicable) |
| `extracted_text_markdown` | The full paper text converted to markdown, with LaTeX math intact |
| `metadata_source` | Where metadata came from — `arxiv_api` or `frontmatter_fallback` |
| `converter_used` | Which converter was used — `arxiv2md` or `mineru` |
| `conversion_warnings` | Any issues encountered during conversion |
| `processed_at` | Timestamp of when processing completed |

**Re-running is safe.** If you run the same command again, papers that already have a JSON file are automatically skipped. Use `--force` to reprocess them.

---

## Using in Python (SDK)

If you want to call the loader from a Python script or Jupyter notebook, you can use the SDK directly:

```python
import asyncio
from data_loader import load_paper, load_papers, is_processed

# Check if a paper has already been processed
if not is_processed("1706.03762"):
    # Process a single paper
    result = asyncio.run(load_paper("1706.03762"))
    print(result.status)       # "processed", "skipped", or "failed"
    print(result.output_path)  # path to the JSON file

# Process multiple papers at once
results = asyncio.run(load_papers(["1706.03762", "2006.11239", "1810.04805"]))
print(f"{results.processed} of {results.total} papers processed")
print(f"{results.failed} failures")
```

---

## Running the API Server

For a web-based interface, start the API server:

```bash
python -m data_loader.api
```

The server runs at `http://localhost:8000`. Here are the available endpoints:

| Method | Endpoint | What it does |
|--------|----------|-------------|
| `POST` | `/papers` | Submit a single paper for processing |
| `POST` | `/papers/batch` | Submit multiple papers for processing |
| `GET` | `/jobs/{job_id}` | Check the status of a processing job |
| `GET` | `/papers/{arxiv_id}` | Retrieve the processed JSON for a paper |
| `GET` | `/health` | Check if the server is running |

**Example: submit a paper and check its status:**

```bash
# Submit a paper
curl -X POST http://localhost:8000/papers \
  -H "Content-Type: application/json" \
  -d '{"arxiv_id": "1706.03762"}'

# Response: {"job_id": "abc123", "status": "pending"}

# Poll for completion
curl http://localhost:8000/jobs/abc123

# Once done, get the result
curl http://localhost:8000/papers/1706.03762
```

---

## Logs & Troubleshooting

**Log file location:** `ETL/logs/loader.log`

Only warnings and errors are logged — you won't see routine processing messages. The log directory is created automatically on first run.

**Common issues:**

| Problem | What to do |
|---------|-----------|
| Network timeout | Check your internet connection and try again. ArXiv may be temporarily slow. |
| No HTML version available | Some older papers don't have HTML. The loader automatically falls back to MinerU (PDF conversion). |
| MinerU download is slow | The first run downloads ~20 GB of models. This is a one-time cost — subsequent runs are fast. |
| Paper not found | Double-check the ArXiv ID. The loader logs a warning for any ID it can't recognize. |

---

## How It Works

The loader follows a four-step pipeline for each paper:

```
  Input             Metadata           Convert            Save
┌─────────┐     ┌─────────────┐     ┌──────────┐     ┌──────────┐
│ ArXiv ID │ ──▶ │ Fetch from  │ ──▶ │ Convert  │ ──▶ │ Write    │
│ or URL   │     │ ArXiv API   │     │ to       │     │ JSON to  │
│          │     │ (metadata)  │     │ markdown │     │ disk     │
└─────────┘     └─────────────┘     └──────────┘     └──────────┘
```

**Two conversion methods are tried in order:**

1. **arxiv2md** (fast) — Uses the paper's HTML version on ArXiv. Most modern papers have one.
2. **MinerU** (fallback) — Downloads the PDF and converts it. Slower but works for any paper.

The loader picks the best method automatically. You don't need to configure anything.
