"""
@file config.py
@description Paths, constants, and DeepSeek configuration for the graph builder.
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

# DeepSeek LLM
DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY")
DEEPSEEK_MODEL = "deepseek-chat"
DEEPSEEK_BASE_URL = "https://api.deepseek.com"
LLM_THINKING = os.environ.get("LLM_THINKING", "True").lower() == "true"

# Processing limits
DEFAULT_CONCURRENCY = 10
MAX_SECTION_CHARS = 30_000
MIN_SECTION_CHARS = 50
MAX_RETRIES = 3
SECTION_TIMEOUT_SECONDS = 300
MAX_TITLE_LENGTH = 80

__all__ = [
    "CLEANED_DIR",
    "DATA_DIR",
    "DEEPSEEK_API_KEY",
    "DEEPSEEK_BASE_URL",
    "DEEPSEEK_MODEL",
    "DEFAULT_CONCURRENCY",
    "LLM_THINKING",
    "LOG_DIR",
    "MAX_RETRIES",
    "SECTION_TIMEOUT_SECONDS",
    "MAX_SECTION_CHARS",
    "MAX_TITLE_LENGTH",
    "MIN_SECTION_CHARS",
    "PROJECT_ROOT",
    "VAULT_DIR",
    "sanitize_arxiv_id",
]
