# Theo-Fish ETL Pipeline

A three-stage ETL pipeline for ingesting ArXiv math papers, cleaning their content, and building a knowledge graph exported as an Obsidian vault.

## Architecture

```
Data/papers/ -> Data Loader -> Data/processed/ -> Data Cleaner -> Data/cleaned/ -> Graph Builder -> data_vault/
```

## Modules

### Data Loader (`data_loader/`)

Ingests ArXiv papers by ID or URL and converts them to structured JSON. Supports two conversion backends:

- **arxiv2md** -- lightweight Markdown-based conversion
- **MinerU** -- higher-fidelity PDF extraction

Output: `Data/processed/*.json`

### Data Cleaner (`data_cleaner/`)

Normalizes raw paper text through six sequential stages:

1. Newline normalization
2. LaTeX normalization
3. Artifact removal
4. Heading normalization
5. Whitespace cleaning
6. Metadata repair

Output: `Data/cleaned/*.json`

### Knowledge Graph Builder (`graph_builder/`)

Uses LLM-powered extraction (DeepSeek V3.2) to identify mathematical entities -- theorems, definitions, lemmas, corollaries, propositions -- and the relationships between them. Produces an Obsidian markdown vault with YAML frontmatter and wikilinks for graph navigation.

Output: `data_vault/`

## Setup

Dependencies are managed via `pyproject.toml` with [uv](https://github.com/astral-sh/uv).

```bash
uv pip install -e ".[dev]"
```

Create a `.env` file at `Theo-Fish/.env` with:

```
DEEPSEEK_API_KEY=<your-key>
```

This is required by the graph builder module.

## Usage

### Data Loader

```bash
# Load a single paper by ArXiv ID
python -m data_loader --paper 1904.07272

# Load multiple papers from a CSV
python -m data_loader --csv papers.csv
```

### Data Cleaner

```bash
# Clean a single paper
python -m data_cleaner --paper 1904.07272

# Clean all papers in the processed directory
python -m data_cleaner --input Data/processed/
```

### Knowledge Graph Builder

```bash
# Build graph for a single paper
python -m graph_builder --paper 1904.07272

# Build graph from all cleaned papers
python -m graph_builder --input-dir Data/cleaned/
```

## Tests

Dev dependencies include pytest and pytest-asyncio.

```bash
uv run pytest tests/ -v
```
