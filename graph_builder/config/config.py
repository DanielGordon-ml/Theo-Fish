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
