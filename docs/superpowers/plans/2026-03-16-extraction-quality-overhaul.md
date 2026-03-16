# Extraction Quality Overhaul Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix missing proofs, upgrade claim extraction to Claude Opus 4.6, add verification pass, fix duplicate edges, and add CLI entry point.

**Architecture:** Introduce an LLMClient protocol so the pipeline can use both DeepSeek and Claude. Add a proof-linking pre-pass that maps deferred proofs to their theorems. Add a post-extraction verification pass (Pass 4) that checks and auto-fixes extraction quality. Wire everything through the orchestrator with dual LLM support.

**Tech Stack:** Python 3.10+, anthropic SDK, pydantic, neo4j async driver, pytest + pytest-asyncio

**Spec:** `docs/superpowers/specs/2026-03-16-extraction-quality-overhaul-design.md`

---

## File Structure

| File | Responsibility | New/Modified |
|---|---|---|
| `graph_builder/llm/protocol.py` | `LLMClient` protocol definition | New |
| `graph_builder/llm/claude_client.py` | Claude Opus 4.6 async client | New |
| `graph_builder/extraction/proof_linker.py` | Regex-based proof location mapper | New |
| `graph_builder/extraction/claim_verifier.py` | Pass 4 verification + auto-fix | New |
| `main.py` | CLI entry point | New |
| `graph_builder/config/config.py` | Add Anthropic config constants | Modified |
| `graph_builder/models/claim.py` | Add `confidence` field | Modified |
| `graph_builder/extraction/prompt_generator.py` | Enhanced claim prompt with proof fields | Modified |
| `graph_builder/llm/response_parser.py` | Parse proof/strength/confidence | Modified |
| `graph_builder/orchestrator/pipeline_loader.py` | Return full_text from load_paper | Modified |
| `graph_builder/extraction/claim_extractor.py` | Accept proof map, inject deferred proofs | Modified |
| `graph_builder/extraction/concept_extractor.py` | Type hint → LLMClient | Modified |
| `graph_builder/extraction/edge_enricher.py` | Type hint → LLMClient | Modified |
| `graph_builder/extraction/cross_section_linker.py` | Type hint → LLMClient | Modified |
| `graph_builder/graph/graph_writer.py` | Add clear_paper_claims/provenances | Modified |
| `graph_builder/graph/graph_reader.py` | DISTINCT on sourced_from query | Modified |
| `graph_builder/orchestrator/orchestrator.py` | Dual LLM, proof map, Pass 4, dedup, clear | Modified |
| `pyproject.toml` | Add anthropic dependency | Modified |

---

## Chunk 1: Foundation — Protocol, Config, Claude Client, ClaimNode

### Task 1: Add anthropic dependency and config constants

**Files:**
- Modify: `pyproject.toml:14` (dependencies list)
- Modify: `graph_builder/config/config.py:23-26` (after DeepSeek constants)

- [ ] **Step 1: Add anthropic to pyproject.toml**

In `pyproject.toml`, add `"anthropic>=0.40"` to the dependencies list.

- [ ] **Step 2: Add config constants**

In `graph_builder/config/config.py`, after line 26 (`LLM_THINKING = ...`), add:

```python
# Anthropic / Claude
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
CLAUDE_MODEL = "claude-opus-4-6"
CLAIM_LLM = os.environ.get("CLAIM_LLM", "claude")
```

- [ ] **Step 3: Install the new dependency**

Run: `pip install anthropic>=0.40`

- [ ] **Step 4: Commit**

```bash
git add pyproject.toml graph_builder/config/config.py
git commit -m "feat(config): add anthropic dependency and Claude config constants"
```

---

### Task 2: LLM Client Protocol

**Files:**
- Create test: `tests/test_llm_protocol.py`
- Create: `graph_builder/llm/protocol.py`

- [ ] **Step 1: Write the test file**

Create `tests/test_llm_protocol.py`:

```python
"""
@file test_llm_protocol.py
@description Tests that DeepSeekClient satisfies the LLMClient protocol.
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

from graph_builder.llm.protocol import LLMClient
from graph_builder.llm.llm_client import LLMResponse


class TestLLMClientProtocol:
    """Tests for the LLMClient protocol."""

    def test_it_should_accept_any_object_with_async_call_method(self):
        """It should be satisfied by any object with the right call signature."""
        mock = MagicMock()
        mock.call = AsyncMock(return_value=LLMResponse(
            content='{}', input_tokens=0, output_tokens=0, model="test",
        ))

        # Protocol is structural — isinstance check via runtime_checkable
        assert isinstance(mock, LLMClient)

    def test_it_should_reject_objects_without_call_method(self):
        """It should not be satisfied by objects missing a call method."""
        mock = MagicMock(spec=[])

        assert not isinstance(mock, LLMClient)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_llm_protocol.py -v`
Expected: FAIL — `ImportError: cannot import name 'LLMClient' from 'graph_builder.llm.protocol'`

- [ ] **Step 3: Write the implementation**

Create `graph_builder/llm/protocol.py`:

```python
"""
@file protocol.py
@description LLMClient protocol shared by DeepSeek and Claude clients.
"""

from typing import Protocol, runtime_checkable

from graph_builder.llm.llm_client import LLMResponse


@runtime_checkable
class LLMClient(Protocol):
    """Structural protocol for LLM clients used in extraction passes.

    Both DeepSeekClient and ClaudeClient satisfy this protocol.
    """

    async def call(
        self,
        system_prompt: str,
        user_prompt: str,
        thinking: bool | None = None,
    ) -> LLMResponse:
        """Send a chat completion request and return the response.

        @param system_prompt System message content
        @param user_prompt User message content
        @param thinking Optional thinking mode toggle
        @returns LLMResponse with content and token counts
        """
        ...
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_llm_protocol.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add tests/test_llm_protocol.py graph_builder/llm/protocol.py
git commit -m "feat(llm): add LLMClient protocol for multi-backend support"
```

---

### Task 3: Add confidence field to ClaimNode

**Files:**
- Modify test: `tests/test_claim_model.py`
- Modify: `graph_builder/models/claim.py:14`

- [ ] **Step 1: Add test for the confidence field**

Read `tests/test_claim_model.py` first. Then append a new test to the test class:

```python
def test_it_should_default_confidence_to_zero(self):
    """It should set confidence to 0.0 when not provided."""
    claim = ClaimNode(
        source_paper_slug="test-paper",
        label="Theorem 1",
        claim_type="theorem",
    )
    assert claim.confidence == 0.0

def test_it_should_accept_confidence_value(self):
    """It should store a provided confidence value."""
    claim = ClaimNode(
        source_paper_slug="test-paper",
        label="Theorem 1",
        claim_type="theorem",
        confidence=0.95,
    )
    assert claim.confidence == 0.95
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_claim_model.py -v -k "confidence"`
Expected: FAIL — `unexpected keyword argument 'confidence'`

- [ ] **Step 3: Add confidence field to ClaimNode**

In `graph_builder/models/claim.py`, add after line 26 (`status: str = "unverified"`):

```python
    confidence: float = 0.0
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_claim_model.py -v`
Expected: ALL PASS

- [ ] **Step 5: Commit**

```bash
git add tests/test_claim_model.py graph_builder/models/claim.py
git commit -m "feat(models): add confidence field to ClaimNode"
```

---

### Task 4: Claude LLM Client

**Files:**
- Create test: `tests/test_claude_client.py`
- Create: `graph_builder/llm/claude_client.py`

- [ ] **Step 1: Write the test file**

Create `tests/test_claude_client.py`:

```python
"""
@file test_claude_client.py
@description Tests for the Claude Opus 4.6 async client with mocked Anthropic SDK.
"""

import json
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from graph_builder.llm.llm_client import LLMResponse
from graph_builder.llm.protocol import LLMClient


class TestClaudeClient:
    """Tests for ClaudeClient."""

    @pytest.mark.asyncio
    async def test_it_should_return_llm_response_on_success(self):
        """It should parse the Anthropic response into an LLMResponse."""
        from graph_builder.llm.claude_client import ClaudeClient

        mock_response = MagicMock()
        mock_response.content = [MagicMock(text='{"claims": []}')]
        mock_response.usage.input_tokens = 100
        mock_response.usage.output_tokens = 50
        mock_response.model = "claude-opus-4-6"

        with patch("graph_builder.llm.claude_client.AsyncAnthropic") as MockAnthropic:
            mock_client = AsyncMock()
            mock_client.messages.create = AsyncMock(return_value=mock_response)
            MockAnthropic.return_value = mock_client

            client = ClaudeClient(api_key="test-key", concurrency=5)
            result = await client.call("system prompt", "user prompt")

        assert isinstance(result, LLMResponse)
        assert result.content == '{"claims": []}'
        assert result.input_tokens == 100
        assert result.output_tokens == 50

    @pytest.mark.asyncio
    async def test_it_should_extract_json_from_fenced_code_block(self):
        """It should fall back to extracting JSON from code fences."""
        from graph_builder.llm.claude_client import extract_json_content

        raw = 'Here is the result:\n```json\n{"key": "value"}\n```\nDone.'
        result = extract_json_content(raw)
        assert result == '{"key": "value"}'

    @pytest.mark.asyncio
    async def test_it_should_return_raw_content_when_valid_json(self):
        """It should return raw content directly when it is valid JSON."""
        from graph_builder.llm.claude_client import extract_json_content

        raw = '{"key": "value"}'
        result = extract_json_content(raw)
        assert result == '{"key": "value"}'

    @pytest.mark.asyncio
    async def test_it_should_return_raw_content_when_no_json_found(self):
        """It should return raw content when no JSON is extractable."""
        from graph_builder.llm.claude_client import extract_json_content

        raw = "This is not JSON at all."
        result = extract_json_content(raw)
        assert result == raw

    def test_it_should_satisfy_llm_client_protocol(self):
        """It should be recognized as an LLMClient."""
        from graph_builder.llm.claude_client import ClaudeClient

        with patch("graph_builder.llm.claude_client.AsyncAnthropic"):
            client = ClaudeClient(api_key="test-key")
        assert isinstance(client, LLMClient)

    def test_it_should_raise_on_missing_api_key(self):
        """It should raise ValueError when no API key is provided."""
        from graph_builder.llm.claude_client import ClaudeClient

        with pytest.raises(ValueError, match="ANTHROPIC_API_KEY"):
            ClaudeClient(api_key=None)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_claude_client.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'graph_builder.llm.claude_client'`

- [ ] **Step 3: Write the implementation**

Create `graph_builder/llm/claude_client.py`:

```python
"""
@file claude_client.py
@description Claude Opus 4.6 async client via Anthropic SDK with rate limiting and retries.
"""

import asyncio
import json
import logging
import random
import re

from anthropic import AsyncAnthropic, APIError, RateLimitError
from pydantic import BaseModel

from graph_builder.config.config import (
    ANTHROPIC_API_KEY,
    CLAUDE_MODEL,
    DEFAULT_CONCURRENCY,
    MAX_RETRIES,
)
from graph_builder.llm.llm_client import LLMResponse

logger = logging.getLogger("graph_builder")

_RETRYABLE_CODES = {429, 500, 502, 503}
_BASE_DELAY = 1.0
_JSON_FENCE_RE = re.compile(r"```json\s*\n(.*?)\n\s*```", re.DOTALL)


def extract_json_content(raw: str) -> str:
    """Extract JSON from raw LLM response, handling code fences.

    Tries in order: (a) raw string is valid JSON, (b) extract from
    code fences, (c) return raw string as fallback.

    @param raw Raw response text from Claude
    @returns Extracted JSON string
    """
    try:
        json.loads(raw)
        return raw
    except (json.JSONDecodeError, ValueError):
        pass

    match = _JSON_FENCE_RE.search(raw)
    if match:
        return match.group(1).strip()

    return raw


class ClaudeClient:
    """Async client for Claude Opus 4.6 with rate limiting and retries."""

    def __init__(
        self,
        api_key: str | None = ANTHROPIC_API_KEY,
        concurrency: int = DEFAULT_CONCURRENCY,
    ):
        """Initialize the Claude client.

        @param api_key Anthropic API key
        @param concurrency Max concurrent LLM calls
        @raises ValueError if api_key is not set
        """
        if not api_key:
            raise ValueError(
                "ANTHROPIC_API_KEY is required. "
                "Set it in Theo-Fish/.env or pass explicitly.",
            )

        self._client = AsyncAnthropic(api_key=api_key)
        self._semaphore = asyncio.Semaphore(concurrency)
        self._model = CLAUDE_MODEL

    async def call(
        self,
        system_prompt: str,
        user_prompt: str,
        thinking: bool | None = None,
    ) -> LLMResponse:
        """Send a message to Claude and return the response.

        @param system_prompt System message content
        @param user_prompt User message content
        @param thinking Unused (kept for protocol compatibility)
        @raises APIError after exhausting retries
        """
        async with self._semaphore:
            return await self._call_with_retries(system_prompt, user_prompt)

    async def _call_with_retries(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> LLMResponse:
        """Execute the call with exponential backoff retries."""
        last_error: Exception | None = None

        for attempt in range(MAX_RETRIES + 1):
            try:
                return await self._execute_call(system_prompt, user_prompt)
            except (RateLimitError, APIError) as err:
                last_error = err
                if not _is_retryable(err) or attempt == MAX_RETRIES:
                    raise
                delay = _BASE_DELAY * (2 ** attempt) + random.uniform(0, 1)
                logger.warning(
                    "Claude call failed (attempt %d/%d), retrying in %.1fs: %s",
                    attempt + 1, MAX_RETRIES + 1, delay, str(err),
                )
                await asyncio.sleep(delay)

        raise last_error  # type: ignore[misc]

    async def _execute_call(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> LLMResponse:
        """Execute a single Anthropic API call."""
        response = await self._client.messages.create(
            model=self._model,
            max_tokens=16384,
            system=system_prompt,
            messages=[{"role": "user", "content": user_prompt}],
        )

        raw_content = response.content[0].text
        content = extract_json_content(raw_content)

        return LLMResponse(
            content=content,
            input_tokens=response.usage.input_tokens,
            output_tokens=response.usage.output_tokens,
            model=response.model,
        )


def _is_retryable(err: APIError) -> bool:
    """Check if an API error warrants a retry.

    @param err The API error to inspect
    @returns True if the error is retryable
    """
    if isinstance(err, RateLimitError):
        return True
    status = getattr(err, "status_code", None)
    return status in _RETRYABLE_CODES
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_claude_client.py -v`
Expected: ALL PASS

- [ ] **Step 5: Commit**

```bash
git add tests/test_claude_client.py graph_builder/llm/claude_client.py
git commit -m "feat(llm): add Claude Opus 4.6 async client"
```

---

## Chunk 2: Proof Linker and Enhanced Prompts

### Task 5: Proof Linker

**Files:**
- Create test: `tests/test_proof_linker.py`
- Create: `graph_builder/extraction/proof_linker.py`

- [ ] **Step 1: Write the test file**

Create `tests/test_proof_linker.py`:

```python
"""
@file test_proof_linker.py
@description Tests for the proof-linking pre-pass that maps claim labels to proof text.
"""

import pytest

from graph_builder.extraction.proof_linker import build_proof_map


class TestBuildProofMap:
    """Tests for build_proof_map()."""

    def test_it_should_find_deferred_proofs_with_colon(self):
        """It should match 'Proof of Theorem X:' patterns."""
        text = (
            "# Main Results\n\n"
            "Theorem III.3. The bound is tight.\n\n"
            "# Appendix\n\n"
            "Proof of Theorem III.3: We proceed by induction. "
            "Base case holds. Inductive step follows.\n\n"
            "# References\n"
        )
        proof_map = build_proof_map(text)

        assert "Theorem III.3" in proof_map
        assert "induction" in proof_map["Theorem III.3"]

    def test_it_should_find_deferred_proofs_with_period(self):
        """It should match 'Proof of Proposition II.1.' patterns."""
        text = (
            "Proposition II.1. Existence is guaranteed.\n\n"
            "Proof of Proposition II.1. We observe that "
            "the optimal is a fixed point.\n\n"
            "## Next Section\n"
        )
        proof_map = build_proof_map(text)

        assert "Proposition II.1" in proof_map
        assert "fixed point" in proof_map["Proposition II.1"]

    def test_it_should_find_inline_proofs(self):
        """It should match 'Proof.' appearing after a claim."""
        text = (
            "Theorem 1. The regret is O(sqrt(T)).\n\n"
            "Proof. By Hoeffding's inequality, we have the bound.\n\n"
            "Theorem 2. Convergence is guaranteed.\n"
        )
        proof_map = build_proof_map(text)

        assert "Theorem 1" in proof_map
        assert "Hoeffding" in proof_map["Theorem 1"]

    def test_it_should_stop_at_qed_symbols(self):
        """It should stop proof text at QED markers."""
        text = (
            "Proof of Theorem 1: By construction. "
            "This completes the proof. $\\square$\n\n"
            "Some other text after QED.\n"
        )
        proof_map = build_proof_map(text)

        assert "Theorem 1" in proof_map
        assert "other text after" not in proof_map["Theorem 1"]

    def test_it_should_return_empty_dict_when_no_proofs(self):
        """It should return {} when the text has no proof markers."""
        text = "# Introduction\n\nThis paper studies games.\n"
        proof_map = build_proof_map(text)

        assert proof_map == {}

    def test_it_should_handle_multiple_proofs(self):
        """It should map multiple claims to their respective proofs."""
        text = (
            "Proof of Theorem 1: First proof text.\n\n"
            "Proof of Lemma 2: Second proof text.\n\n"
            "# End\n"
        )
        proof_map = build_proof_map(text)

        assert len(proof_map) == 2
        assert "First proof" in proof_map["Theorem 1"]
        assert "Second proof" in proof_map["Lemma 2"]

    def test_it_should_handle_corollary_proofs(self):
        """It should match proofs of corollaries."""
        text = (
            "Proof of Corollary 1: This follows immediately "
            "from Theorem 2.\n\n"
            "# Next\n"
        )
        proof_map = build_proof_map(text)

        assert "Corollary 1" in proof_map
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_proof_linker.py -v`
Expected: FAIL — `ModuleNotFoundError`

- [ ] **Step 3: Write the implementation**

Create `graph_builder/extraction/proof_linker.py`:

```python
"""
@file proof_linker.py
@description Regex-based proof-location mapper. Scans full paper text for
proof markers and builds a mapping from claim labels to proof text.
"""

import re

# Matches "Proof of Theorem III.3:" or "Proof of Theorem III.3."
_DEFERRED_PROOF_RE = re.compile(
    r"Proof\s+of\s+"
    r"((?:Theorem|Lemma|Proposition|Corollary)\s+[\w\.\-]+)"
    r"\s*[:\.]",
    re.IGNORECASE,
)

# Matches "Proof." or "Proof:" at the start of a line or after blank line
_INLINE_PROOF_RE = re.compile(
    r"(?:^|\n\n)\s*Proof\s*[\.:]",
    re.IGNORECASE,
)

# Matches claim labels like "Theorem 1.", "Lemma III.3.", "Proposition II.1."
_CLAIM_LABEL_RE = re.compile(
    r"((?:Theorem|Lemma|Proposition|Corollary)\s+[\w\.\-]+)\s*[\.:]",
    re.IGNORECASE,
)

# QED markers that terminate a proof
_QED_RE = re.compile(
    r"(?:\$\\square\$|\$\\blacksquare\$|∎|□)",
)

# Heading that terminates a proof
_HEADING_RE = re.compile(r"^#{1,6}\s+", re.MULTILINE)

# (No module-level _NEXT_MARKER_RE — searches done inline in _next_marker_search)


def build_proof_map(full_text: str) -> dict[str, str]:
    """Build a mapping from claim labels to their proof text.

    Scans for both deferred proofs ('Proof of Theorem X:') and inline
    proofs ('Proof.' following a claim). Returns a dict mapping
    normalized labels (e.g., 'Theorem III.3') to proof text.

    @param full_text Full markdown text of the paper
    @returns Dict mapping claim labels to proof text
    """
    proof_map: dict[str, str] = {}

    _find_deferred_proofs(full_text, proof_map)
    _find_inline_proofs(full_text, proof_map)

    return proof_map


def _find_deferred_proofs(text: str, proof_map: dict[str, str]) -> None:
    """Find 'Proof of X:' patterns and extract proof text."""
    for match in _DEFERRED_PROOF_RE.finditer(text):
        label = _normalize_label(match.group(1))
        proof_start = match.end()
        proof_text = _extract_proof_text(text, proof_start)
        if proof_text.strip():
            proof_map[label] = proof_text.strip()


def _find_inline_proofs(text: str, proof_map: dict[str, str]) -> None:
    """Find 'Proof.' patterns and link to the preceding claim."""
    for match in _INLINE_PROOF_RE.finditer(text):
        preceding = text[:match.start()]
        claim_label = _find_preceding_claim(preceding)
        if claim_label and claim_label not in proof_map:
            proof_start = match.end()
            proof_text = _extract_proof_text(text, proof_start)
            if proof_text.strip():
                proof_map[claim_label] = proof_text.strip()


def _find_preceding_claim(text: str) -> str | None:
    """Find the last claim label before a given position.

    @param text Text preceding the proof marker
    @returns Normalized claim label, or None
    """
    matches = list(_CLAIM_LABEL_RE.finditer(text))
    if not matches:
        return None
    return _normalize_label(matches[-1].group(1))


def _extract_proof_text(text: str, start: int) -> str:
    """Extract proof text from start position until a terminator.

    Terminators: QED symbol, heading, next proof/claim marker.

    @param text Full paper text
    @param start Character position after the proof marker
    @returns Extracted proof text
    """
    remaining = text[start:]

    end = len(remaining)

    qed = _QED_RE.search(remaining)
    if qed:
        end = min(end, qed.end())

    heading = _HEADING_RE.search(remaining)
    if heading:
        end = min(end, heading.start())

    # Find next proof/claim marker (skip the first few chars to avoid self-match)
    next_marker = _next_marker_search(remaining)
    if next_marker:
        end = min(end, next_marker)

    return remaining[:end]


def _next_marker_search(text: str) -> int | None:
    """Find the position of the next proof or claim marker.

    Skips the first 20 characters to avoid matching the current marker.

    @param text Text to search
    @returns Position of next marker, or None
    """
    search_start = min(20, len(text))
    for pattern in [_DEFERRED_PROOF_RE, _CLAIM_LABEL_RE]:
        match = pattern.search(text, search_start)
        if match:
            return match.start()
    return None


def _normalize_label(label: str) -> str:
    """Normalize a claim label by collapsing whitespace.

    @param label Raw label text (e.g., 'Theorem  III.3')
    @returns Normalized label (e.g., 'Theorem III.3')
    """
    return re.sub(r"\s+", " ", label).strip()
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_proof_linker.py -v`
Expected: ALL PASS (some may need regex tuning — iterate until green)

- [ ] **Step 5: Commit**

```bash
git add tests/test_proof_linker.py graph_builder/extraction/proof_linker.py
git commit -m "feat(extraction): add proof-linking pre-pass"
```

---

### Task 6: Enhanced Claim Extraction Prompt

**Files:**
- Modify test: `tests/test_prompt_generator.py`
- Modify: `graph_builder/extraction/prompt_generator.py:99-140`

- [ ] **Step 1: Read existing tests**

Read `tests/test_prompt_generator.py` to understand current test coverage.

- [ ] **Step 2: Add tests for enhanced claim prompt**

Append to the claim prompt test class in `tests/test_prompt_generator.py`:

```python
def test_it_should_include_proof_field_in_claim_output_format(self):
    """It should instruct the LLM to extract proof text."""
    schema = _make_schema()
    prompt = build_claim_prompt(schema)
    assert '"proof"' in prompt

def test_it_should_include_proof_technique_in_claim_output_format(self):
    """It should instruct the LLM to extract proof_technique."""
    schema = _make_schema()
    prompt = build_claim_prompt(schema)
    assert '"proof_technique"' in prompt

def test_it_should_include_strength_in_claim_output_format(self):
    """It should instruct the LLM to extract strength."""
    schema = _make_schema()
    prompt = build_claim_prompt(schema)
    assert '"strength"' in prompt

def test_it_should_include_confidence_in_claim_output_format(self):
    """It should instruct the LLM to extract confidence."""
    schema = _make_schema()
    prompt = build_claim_prompt(schema)
    assert '"confidence"' in prompt

def test_it_should_include_verbatim_extraction_rule(self):
    """It should instruct verbatim statement extraction."""
    schema = _make_schema()
    prompt = build_claim_prompt(schema)
    assert "verbatim" in prompt.lower()

def test_it_should_include_strength_values_for_theorem_type(self):
    """It should show valid strength values from schema."""
    schema = _make_schema()
    prompt = build_claim_prompt(schema)
    assert "exact" in prompt or "asymptotic" in prompt
```

- [ ] **Step 3: Run tests to verify they fail**

Run: `python -m pytest tests/test_prompt_generator.py -v -k "proof or strength or confidence or verbatim"`
Expected: FAIL — the current prompt does not include these fields

- [ ] **Step 4: Update prompt_generator.py**

Replace `_claim_output_format()` (lines 125-140) with:

```python
def _claim_output_format() -> list[str]:
    """Return the output format instructions for claim extraction."""
    return [
        "## Output Format",
        "Return ONLY valid JSON with no additional text:",
        _JSON_FENCE,
        '{"claims": [{"claim_type": "<one of the types above>", '
        '"label": "<e.g. Theorem III.3>", '
        '"statement": "<full verbatim statement, preserving math notation>", '
        '"assumptions": ["<assumption 1>", "..."], '
        '"conclusion": "<main result>", '
        '"proof": "<full proof text if present, empty string if not>", '
        '"proof_technique": "<e.g. induction, contradiction, constructive>", '
        '"strength": "<exact|asymptotic|approximate|existential>", '
        '"confidence": 0.95, '
        '"about_concepts": ["<concept_slug_1>", "<concept_slug_2>"]}]}',
        _FENCE_END,
        "",
        "Rules:",
        "- Extract the FULL statement verbatim from the paper, preserving all math notation. Do not summarize.",
        "- Extract the FULL proof text if present in the section or in a deferred proof block. Preserve all math steps.",
        "- proof_technique is REQUIRED for theorem, lemma, and proposition types.",
        "- confidence: your confidence that the extraction is complete and accurate (0.0-1.0).",
        "- Each concept in about_concepts must be unique. Do not list the same concept twice.",
        "- Only extract types listed above.",
        "- Do NOT extract concept definitions or structures.",
        "- Every claim must reference at least one concept by slug.",
    ]
```

Also update `_format_claim_type()` (lines 99-108) to emit strength_values:

```python
def _format_claim_type(name: str, defn: ClaimTypeDef) -> list[str]:
    """Format a single claim type block for the prompt."""
    block = [
        f"### {name}",
        f"Description: {defn.description}",
        f"Required fields: {', '.join(defn.required_fields)}",
    ]
    if defn.optional_fields:
        block.append(f"Optional fields: {', '.join(defn.optional_fields)}")
    if hasattr(defn, "strength_values") and defn.strength_values:
        block.append(f"Strength values: {', '.join(defn.strength_values)}")
    block.append("")
    return block
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `python -m pytest tests/test_prompt_generator.py -v`
Expected: ALL PASS

- [ ] **Step 6: Commit**

```bash
git add tests/test_prompt_generator.py graph_builder/extraction/prompt_generator.py
git commit -m "feat(extraction): enhance claim prompt with proof, strength, confidence fields"
```

---

### Task 7: Response Parser — Parse New Claim Fields

**Files:**
- Modify test: `tests/test_response_parser.py`
- Modify: `graph_builder/llm/response_parser.py:161-205`

- [ ] **Step 1: Read existing tests**

Read `tests/test_response_parser.py` to understand current coverage.

- [ ] **Step 2: Add tests for new fields**

Append to the claim parsing test class in `tests/test_response_parser.py`:

```python
def test_it_should_parse_proof_field(self):
    """It should populate ClaimNode.proof from LLM response."""
    schema = _make_schema()
    claim_data = {**_VALID_CLAIM, "proof": "By induction on n."}
    json_str = json.dumps({"claims": [claim_data]})

    claims = parse_claims(json_str, "paper", schema)

    assert claims[0].proof == "By induction on n."

def test_it_should_parse_proof_technique_field(self):
    """It should populate ClaimNode.proof_technique from LLM response."""
    schema = _make_schema()
    claim_data = {**_VALID_CLAIM, "proof_technique": "induction"}
    json_str = json.dumps({"claims": [claim_data]})

    claims = parse_claims(json_str, "paper", schema)

    assert claims[0].proof_technique == "induction"

def test_it_should_parse_strength_field(self):
    """It should populate ClaimNode.strength from LLM response."""
    schema = _make_schema()
    claim_data = {**_VALID_CLAIM, "strength": "exact"}
    json_str = json.dumps({"claims": [claim_data]})

    claims = parse_claims(json_str, "paper", schema)

    assert claims[0].strength == "exact"

def test_it_should_parse_confidence_field(self):
    """It should populate ClaimNode.confidence from LLM response."""
    schema = _make_schema()
    claim_data = {**_VALID_CLAIM, "confidence": 0.85}
    json_str = json.dumps({"claims": [claim_data]})

    claims = parse_claims(json_str, "paper", schema)

    assert claims[0].confidence == 0.85

def test_it_should_default_confidence_to_zero(self):
    """It should set confidence to 0.0 when not in response."""
    schema = _make_schema()
    json_str = json.dumps({"claims": [_VALID_CLAIM]})

    claims = parse_claims(json_str, "paper", schema)

    assert claims[0].confidence == 0.0
```

- [ ] **Step 3: Run tests to verify new tests pass**

The `_build_claim` function uses `**{k: v for k, v in entry.items() if v is not None}` which passes all fields through to ClaimNode. The `proof`, `proof_technique`, `strength` fields already exist on ClaimNode, and `confidence` was added in Task 3. However, the enhanced prompt now also returns `about_concepts` which is NOT a ClaimNode field — it would cause a Pydantic validation error.

**Fix:** In `response_parser.py`, update `_build_claim` to filter out keys that aren't ClaimNode fields. Change the constructor call (around line 199):

```python
    # Keys the LLM returns that are not ClaimNode fields
    _CLAIM_EXTRA_KEYS = {"about_concepts", "location"}

    try:
        filtered = {k: v for k, v in entry.items()
                    if v is not None and k not in _CLAIM_EXTRA_KEYS}
        return ClaimNode(
            source_paper_slug=paper_slug,
            **filtered,
        )
```

Move `_CLAIM_EXTRA_KEYS` to module level (after imports).

Run: `python -m pytest tests/test_response_parser.py -v -k "proof or strength or confidence"`
Expected: PASS

- [ ] **Step 4: Commit**

```bash
git add tests/test_response_parser.py
git commit -m "test(parser): add tests for proof, strength, confidence field parsing"
```

---

## Chunk 3: Pipeline Loader, Claim Extractor, Type Hints

### Task 8: Pipeline Loader — Return Full Text

**Files:**
- Modify: `graph_builder/orchestrator/pipeline_loader.py:18-32`
- Modify: `tests/test_v2_orchestrator.py` (if it tests load_paper)

- [ ] **Step 1: Read existing tests and add a test for 3-tuple return**

Read `tests/test_v2_orchestrator.py` to see if `load_paper` is tested. Also check for a `test_pipeline_loader.py` or similar. If `load_paper` is not directly tested, add a simple test verifying the 3-tuple return:

In the appropriate test file, add:

```python
@pytest.mark.asyncio
async def test_load_paper_should_return_full_text_as_third_element(self, tmp_path):
    """It should return (title, sections, full_text) where full_text is the raw markdown."""
    # This test requires a cleaned JSON file to exist — mock or use fixture
    # The key assertion is that the return is a 3-tuple
    pass  # Will be fleshed out based on existing test patterns
```

If `load_paper` is only tested indirectly through the orchestrator, update the `_patch_pipeline` mock to return a 3-tuple (see Task 14).

- [ ] **Step 2: Update load_paper to return full_text**

In `graph_builder/orchestrator/pipeline_loader.py`, change the function signature and implementation (lines 18-32):

```python
async def load_paper(arxiv_id: str) -> tuple[str, list[Section], str]:
    """Load cleaned JSON and split into sections.

    @param arxiv_id ArXiv identifier
    @returns Tuple of (title, sections, full_text)
    @raises FileNotFoundError if cleaned JSON does not exist
    """
    from graph_builder.extraction.section_splitter import split_into_sections

    json_path = _find_json_path(arxiv_id)
    paper_data = _read_json(json_path)
    title = paper_data.get("title", arxiv_id)
    markdown = paper_data.get("extracted_text_markdown", "")
    sections = split_into_sections(markdown)
    return title, sections, markdown
```

- [ ] **Step 3: Update orchestrator to accept the new return value**

In `graph_builder/orchestrator/orchestrator.py`, update line 89:

Change:
```python
    title, sections = await load_paper(arxiv_id)
```
To:
```python
    title, sections, full_text = await load_paper(arxiv_id)
```

Pass `full_text` through to `_run_all_passes` — add it as a parameter. We will wire the proof linker in Task 14.

- [ ] **Step 4: Run existing tests**

Run: `python -m pytest tests/test_v2_orchestrator.py -v`
Expected: PASS (or skip if the test mocks load_paper)

- [ ] **Step 5: Commit**

```bash
git add graph_builder/orchestrator/pipeline_loader.py graph_builder/orchestrator/orchestrator.py
git commit -m "feat(loader): return full markdown text from load_paper for proof linking"
```

---

### Task 9: Claim Extractor — Accept Proof Map

**Files:**
- Modify test: `tests/test_claim_extractor.py`
- Modify: `graph_builder/extraction/claim_extractor.py`

- [ ] **Step 1: Add tests for proof map injection**

Append to `tests/test_claim_extractor.py`:

```python
@pytest.mark.asyncio
async def test_it_should_inject_deferred_proof_into_user_prompt(self):
    """It should append deferred proof text to the section content."""
    schema = _make_schema()
    section = _make_section(
        heading="Main Results",
        content="Theorem III.3. The bound is tight.",
    )
    client = _make_mock_client([_VALID_CLAIM])
    proof_map = {"Theorem III.3": "We proceed by induction."}

    await extract_claims_from_section(
        section, schema, client, _CONCEPT_LIST, "test-paper",
        proof_map=proof_map,
    )

    _, user_prompt = client.call.call_args[0]
    assert "DEFERRED PROOF" in user_prompt
    assert "We proceed by induction" in user_prompt

@pytest.mark.asyncio
async def test_it_should_not_inject_when_no_matching_proof(self):
    """It should not modify the prompt when no proof matches."""
    schema = _make_schema()
    section = _make_section(content="Theorem 99. Something else.")
    client = _make_mock_client([])
    proof_map = {"Theorem III.3": "Some proof."}

    await extract_claims_from_section(
        section, schema, client, _CONCEPT_LIST, "test-paper",
        proof_map=proof_map,
    )

    _, user_prompt = client.call.call_args[0]
    assert "DEFERRED PROOF" not in user_prompt
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_claim_extractor.py -v -k "deferred"`
Expected: FAIL — `extract_claims_from_section() got an unexpected keyword argument 'proof_map'`

- [ ] **Step 3: Update claim_extractor.py**

In `graph_builder/extraction/claim_extractor.py`:

1. Change `extract_claims_from_section` signature (add `proof_map` parameter):

```python
async def extract_claims_from_section(
    section: Section,
    schema: GraphSchema,
    llm_client: LLMClient,
    concept_list: list[dict],
    paper_slug: str,
    proof_map: dict[str, str] | None = None,
) -> tuple[list[ClaimNode], list[CouplingEdge]]:
```

2. Update the import at the top — change `DeepSeekClient` to `LLMClient`:

```python
from graph_builder.llm.protocol import LLMClient
```

3. Build user prompt with proof injection. Replace `user_prompt = section.content` with:

```python
    user_prompt = _build_user_prompt(section.content, proof_map)
```

4. Add the helper function:

```python
def _build_user_prompt(
    section_content: str,
    proof_map: dict[str, str] | None,
) -> str:
    """Build user prompt, injecting deferred proofs if they match.

    @param section_content Raw section text
    @param proof_map Optional mapping of claim labels to proof text
    @returns User prompt with any deferred proofs appended
    """
    if not proof_map:
        return section_content

    injections = _find_matching_proofs(section_content, proof_map)
    if not injections:
        return section_content

    parts = [section_content, "", "--- DEFERRED PROOF (from appendix) ---"]
    for label, proof_text in injections:
        parts.append(f"Proof of {label}: {proof_text}")
    return "\n".join(parts)


def _find_matching_proofs(
    content: str,
    proof_map: dict[str, str],
) -> list[tuple[str, str]]:
    """Find proof map entries whose labels appear in the section content.

    @param content Section text to search
    @param proof_map Mapping of labels to proof text
    @returns List of (label, proof_text) tuples for matches
    """
    matches = []
    for label, proof_text in proof_map.items():
        if label in content:
            matches.append((label, proof_text))
    return matches
```

- [ ] **Step 4: Run all claim extractor tests**

Run: `python -m pytest tests/test_claim_extractor.py -v`
Expected: ALL PASS

- [ ] **Step 5: Commit**

```bash
git add tests/test_claim_extractor.py graph_builder/extraction/claim_extractor.py
git commit -m "feat(extraction): accept proof map and inject deferred proofs into claim extraction"
```

---

### Task 10: Update Type Hints Across Extractors

**Files:**
- Modify: `graph_builder/extraction/concept_extractor.py` (import line)
- Modify: `graph_builder/extraction/edge_enricher.py` (import line)
- Modify: `graph_builder/extraction/cross_section_linker.py` (import line)

- [ ] **Step 1: Update concept_extractor.py**

Read `graph_builder/extraction/concept_extractor.py`. Change the import:
```python
# Before:
from graph_builder.llm.llm_client import DeepSeekClient
# After:
from graph_builder.llm.protocol import LLMClient
```
And update the type hint on the `llm_client` parameter from `DeepSeekClient` to `LLMClient`.

- [ ] **Step 2: Update edge_enricher.py**

Same pattern: change import and type hint from `DeepSeekClient` to `LLMClient`.

- [ ] **Step 3: Update cross_section_linker.py**

Same pattern: change import and type hint from `DeepSeekClient` to `LLMClient`.

- [ ] **Step 4: Run all existing extraction tests**

Run: `python -m pytest tests/test_concept_extractor.py tests/test_edge_enricher.py tests/test_cross_section_linker.py -v`
Expected: ALL PASS (mocks still satisfy the protocol)

- [ ] **Step 5: Commit**

```bash
git add graph_builder/extraction/concept_extractor.py graph_builder/extraction/edge_enricher.py graph_builder/extraction/cross_section_linker.py
git commit -m "refactor(extraction): update LLM type hints to LLMClient protocol"
```

---

## Chunk 4: Verification Pass, Graph Writer Clear, DISTINCT Fix

### Task 11: Graph Writer — Clear Methods

**Files:**
- Modify test: `tests/test_graph_writer.py`
- Modify: `graph_builder/graph/graph_writer.py`

- [ ] **Step 1: Read existing tests**

Read `tests/test_graph_writer.py` to understand mocking patterns for Neo4j.

- [ ] **Step 2: Add tests for clear methods**

Append to `tests/test_graph_writer.py`:

```python
@pytest.mark.asyncio
async def test_it_should_clear_paper_claims(self):
    """It should execute DETACH DELETE for claims of a given paper."""
    client = _make_mock_neo4j()
    writer = GraphWriter(client)

    await writer.clear_paper_claims("my-paper-slug")

    client.execute_write.assert_called_once()
    cypher = client.execute_write.call_args[0][0]
    assert "DETACH DELETE" in cypher
    assert "source_paper_slug" in cypher

@pytest.mark.asyncio
async def test_it_should_clear_paper_provenances(self):
    """It should execute DETACH DELETE for provenances of a given paper."""
    client = _make_mock_neo4j()
    writer = GraphWriter(client)

    await writer.clear_paper_provenances("arxiv-123")

    client.execute_write.assert_called_once()
    cypher = client.execute_write.call_args[0][0]
    assert "DETACH DELETE" in cypher
    assert "source_arxiv_id" in cypher
```

- [ ] **Step 3: Run tests to verify they fail**

Run: `python -m pytest tests/test_graph_writer.py -v -k "clear"`
Expected: FAIL — `AttributeError: 'GraphWriter' object has no attribute 'clear_paper_claims'`

- [ ] **Step 4: Add clear methods to GraphWriter**

Add Cypher constants after `_COUPLING_EDGE_CYPHER` (after line 128):

```python
_CLEAR_CLAIMS_CYPHER = """
MATCH (cl:Claim {source_paper_slug: $paper_slug})
DETACH DELETE cl
"""

_CLEAR_PROVENANCES_CYPHER = """
MATCH (p:Provenance {source_arxiv_id: $arxiv_id})
DETACH DELETE p
"""
```

Add methods to `GraphWriter` class:

```python
    async def clear_paper_claims(self, paper_slug: str) -> None:
        """Delete all claim nodes and their edges for a given paper.

        @param paper_slug Source paper slug to match
        """
        await self._client.execute_write(
            _CLEAR_CLAIMS_CYPHER, paper_slug=paper_slug,
        )

    async def clear_paper_provenances(self, arxiv_id: str) -> None:
        """Delete all provenance nodes and their edges for a given paper.

        @param arxiv_id ArXiv ID of the source paper
        """
        await self._client.execute_write(
            _CLEAR_PROVENANCES_CYPHER, arxiv_id=arxiv_id,
        )
```

- [ ] **Step 5: Run tests**

Run: `python -m pytest tests/test_graph_writer.py -v`
Expected: ALL PASS

- [ ] **Step 6: Commit**

```bash
git add tests/test_graph_writer.py graph_builder/graph/graph_writer.py
git commit -m "feat(graph): add clear_paper_claims and clear_paper_provenances methods"
```

---

### Task 12: Graph Reader — DISTINCT Sourced-From Fix

**Files:**
- Modify: `graph_builder/graph/graph_reader.py` (get_all_sourced_from_edges method)

- [ ] **Step 1: Update the query**

In `graph_builder/graph/graph_reader.py`, find `get_all_sourced_from_edges` and add `DISTINCT` to the query:

Change:
```python
        "RETURN coalesce(n.slug, n.concept_slug) AS node_slug, "
```
To:
```python
        "RETURN DISTINCT coalesce(n.slug, n.concept_slug) AS node_slug, "
```

- [ ] **Step 2: Run existing tests**

Run: `python -m pytest tests/test_graph_reader.py -v`
Expected: ALL PASS

- [ ] **Step 3: Commit**

```bash
git add graph_builder/graph/graph_reader.py
git commit -m "fix(graph): add DISTINCT to sourced_from query to prevent duplicates"
```

---

### Task 13: Claim Verifier (Pass 4)

**Files:**
- Create test: `tests/test_claim_verifier.py`
- Create: `graph_builder/extraction/claim_verifier.py`

- [ ] **Step 1: Write the test file**

Create `tests/test_claim_verifier.py`:

```python
"""
@file test_claim_verifier.py
@description Tests for the Pass 4 claim verification and auto-fix logic.
"""

import json
from unittest.mock import AsyncMock, MagicMock

import pytest

from graph_builder.extraction.claim_verifier import (
    verify_section_claims,
    apply_corrections,
    apply_flags,
    build_missing_claims,
)
from graph_builder.llm.llm_client import LLMResponse
from graph_builder.models.claim import ClaimNode
from graph_builder.models.edges import CouplingEdge


def _make_claim(
    slug: str = "paper--theorem-1",
    label: str = "Theorem 1",
    claim_type: str = "theorem",
    statement: str = "The bound holds.",
) -> ClaimNode:
    """Build a minimal ClaimNode for testing."""
    return ClaimNode(
        slug=slug,
        source_paper_slug="paper",
        label=label,
        claim_type=claim_type,
        statement=statement,
    )


def _make_mock_client(response_data: dict) -> MagicMock:
    """Return a mock LLM client returning the given verification JSON."""
    client = MagicMock()
    client.call = AsyncMock(return_value=LLMResponse(
        content=json.dumps(response_data),
        input_tokens=100,
        output_tokens=50,
        model="claude-opus-4-6",
    ))
    return client


class TestApplyCorrections:
    """Tests for apply_corrections()."""

    def test_it_should_update_statement_field(self):
        """It should overwrite a claim's statement when corrected."""
        claim = _make_claim()
        corrections = [{
            "claim_slug": "paper--theorem-1",
            "field": "statement",
            "issue": "paraphrased",
            "corrected_value": "The exact bound is 2.",
        }]

        apply_corrections([claim], corrections)

        assert claim.statement == "The exact bound is 2."

    def test_it_should_reject_label_corrections(self):
        """It should skip corrections that target the label field."""
        claim = _make_claim(label="Theorem 1")
        corrections = [{
            "claim_slug": "paper--theorem-1",
            "field": "label",
            "issue": "wrong label",
            "corrected_value": "Theorem 2",
        }]

        apply_corrections([claim], corrections)

        assert claim.label == "Theorem 1"

    def test_it_should_skip_unknown_slugs(self):
        """It should silently skip corrections for non-existent claims."""
        claim = _make_claim()
        corrections = [{
            "claim_slug": "paper--nonexistent",
            "field": "statement",
            "issue": "wrong",
            "corrected_value": "new value",
        }]

        apply_corrections([claim], corrections)

        assert claim.statement == "The bound holds."


class TestApplyFlags:
    """Tests for apply_flags()."""

    def test_it_should_set_review_needed_for_low_confidence(self):
        """It should set status to review_needed when confidence < 0.7."""
        claim = _make_claim()
        flags = [{
            "claim_slug": "paper--theorem-1",
            "issue": "proof truncated",
            "confidence": 0.4,
        }]

        apply_flags([claim], flags)

        assert claim.status == "review_needed"

    def test_it_should_not_flag_high_confidence(self):
        """It should not modify status when confidence >= 0.7."""
        claim = _make_claim()
        flags = [{
            "claim_slug": "paper--theorem-1",
            "issue": "minor",
            "confidence": 0.8,
        }]

        apply_flags([claim], flags)

        assert claim.status == "unverified"


class TestBuildMissingClaims:
    """Tests for build_missing_claims()."""

    def test_it_should_create_claim_nodes_from_missing_entries(self):
        """It should construct ClaimNodes from missing_claims data."""
        missing = [{
            "label": "Lemma 3",
            "claim_type": "lemma",
            "statement": "The auxiliary bound holds.",
            "about_concepts": ["regret"],
        }]

        claims, edges = build_missing_claims(
            missing, "paper", "Section III",
        )

        assert len(claims) == 1
        assert claims[0].label == "Lemma 3"
        assert claims[0].source_paper_slug == "paper"
        assert claims[0].section == "Section III"
        assert len(edges) == 1
        assert edges[0].concept_slug == "regret"


class TestVerifySectionClaims:
    """Tests for verify_section_claims()."""

    @pytest.mark.asyncio
    async def test_it_should_return_empty_results_on_no_issues(self):
        """It should return empty lists when verification finds no problems."""
        client = _make_mock_client({
            "missing_claims": [],
            "corrections": [],
            "flags": [],
        })
        claims = [_make_claim()]

        new_claims, new_edges = await verify_section_claims(
            "section text", {}, claims, None, client, "paper", "Section I",
        )

        assert new_claims == []
        assert new_edges == []

    @pytest.mark.asyncio
    async def test_it_should_apply_corrections_in_place(self):
        """It should mutate existing claims based on corrections."""
        client = _make_mock_client({
            "missing_claims": [],
            "corrections": [{
                "claim_slug": "paper--theorem-1",
                "field": "proof_technique",
                "issue": "missing",
                "corrected_value": "induction",
            }],
            "flags": [],
        })
        claims = [_make_claim()]

        await verify_section_claims(
            "section text", {}, claims, None, client, "paper", "Section I",
        )

        assert claims[0].proof_technique == "induction"

    @pytest.mark.asyncio
    async def test_it_should_handle_llm_failure_gracefully(self):
        """It should return empty results when the LLM call fails."""
        client = MagicMock()
        client.call = AsyncMock(side_effect=RuntimeError("LLM down"))
        claims = [_make_claim()]

        new_claims, new_edges = await verify_section_claims(
            "section text", {}, claims, None, client, "paper", "Section I",
        )

        assert new_claims == []
        assert new_edges == []
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_claim_verifier.py -v`
Expected: FAIL — `ModuleNotFoundError`

- [ ] **Step 3: Write the implementation**

Create `graph_builder/extraction/claim_verifier.py`:

```python
"""
@file claim_verifier.py
@description Pass 4 verification: checks extraction quality against source text
and auto-fixes issues. Routes low-confidence claims to review.
"""

import json
import logging

from graph_builder.config.schema_types import GraphSchema
from graph_builder.llm.llm_client import LLMResponse
from graph_builder.llm.protocol import LLMClient
from graph_builder.models.claim import ClaimNode
from graph_builder.models.edges import CouplingEdge

logger = logging.getLogger("graph_builder")

_REVIEW_CONFIDENCE_THRESHOLD = 0.7
_FORBIDDEN_CORRECTION_FIELDS = {"label", "slug", "source_paper_slug"}


async def verify_section_claims(
    section_text: str,
    proof_map: dict[str, str],
    claims: list[ClaimNode],
    schema: GraphSchema | None,
    llm_client: LLMClient,
    paper_slug: str,
    section_heading: str,
) -> tuple[list[ClaimNode], list[CouplingEdge]]:
    """Verify extracted claims against source text and auto-fix issues.

    Calls the LLM to check completeness, fidelity, proof completeness,
    classification, and concept references. Applies corrections in-place,
    flags low-confidence claims for review, and returns any missing claims.

    @param section_text Original section text
    @param proof_map Mapping of claim labels to deferred proof text
    @param claims Extracted claims for this section (mutated in-place)
    @param schema GraphSchema (reserved for future use)
    @param llm_client LLM client for verification call
    @param paper_slug Source paper slug for new claims
    @param section_heading Section heading for new claims
    @returns Tuple of (new_claims, new_coupling_edges)
    """
    if not claims:
        return [], []

    try:
        response = await llm_client.call(
            _build_system_prompt(),
            _build_user_prompt(section_text, proof_map, claims),
        )
    except Exception as err:
        logger.error("Verification failed for '%s': %s", section_heading, err)
        return [], []

    result = _safe_parse_json(response.content)
    if result is None:
        return [], []

    corrections = result.get("corrections", [])
    flags = result.get("flags", [])
    missing = result.get("missing_claims", [])

    apply_corrections(claims, corrections)
    apply_flags(claims, flags)
    new_claims, new_edges = build_missing_claims(
        missing, paper_slug, section_heading,
    )

    return new_claims, new_edges


def apply_corrections(
    claims: list[ClaimNode],
    corrections: list[dict],
) -> None:
    """Apply field corrections to claims in-place.

    Skips corrections targeting forbidden fields (label, slug).

    @param claims List of ClaimNodes to mutate
    @param corrections List of correction dicts from verifier
    """
    claim_index = {c.slug: c for c in claims}

    for corr in corrections:
        slug = corr.get("claim_slug", "")
        field = corr.get("field", "")
        value = corr.get("corrected_value", "")

        if field in _FORBIDDEN_CORRECTION_FIELDS:
            logger.warning("Skipping forbidden correction to '%s'", field)
            continue

        claim = claim_index.get(slug)
        if claim is None:
            continue

        if hasattr(claim, field):
            setattr(claim, field, value)


def apply_flags(
    claims: list[ClaimNode],
    flags: list[dict],
) -> None:
    """Route low-confidence claims to review.

    Sets status to 'review_needed' for claims with confidence below threshold.

    @param claims List of ClaimNodes to mutate
    @param flags List of flag dicts from verifier
    """
    claim_index = {c.slug: c for c in claims}

    for flag in flags:
        slug = flag.get("claim_slug", "")
        confidence = flag.get("confidence", 1.0)

        if confidence >= _REVIEW_CONFIDENCE_THRESHOLD:
            continue

        claim = claim_index.get(slug)
        if claim is not None:
            claim.status = "review_needed"


def build_missing_claims(
    missing: list[dict],
    paper_slug: str,
    section_heading: str,
) -> tuple[list[ClaimNode], list[CouplingEdge]]:
    """Construct ClaimNodes and coupling edges from missing claim data.

    @param missing List of missing claim dicts from verifier
    @param paper_slug Source paper slug
    @param section_heading Section heading for provenance
    @returns Tuple of (claims, coupling_edges)
    """
    claims: list[ClaimNode] = []
    edges: list[CouplingEdge] = []

    for entry in missing:
        label = entry.get("label", "")
        if not label:
            continue

        claim = ClaimNode(
            source_paper_slug=paper_slug,
            label=label,
            claim_type=entry.get("claim_type", "theorem"),
            statement=entry.get("statement", ""),
            section=section_heading,
        )
        claims.append(claim)

        for slug in entry.get("about_concepts", []):
            if isinstance(slug, str) and slug:
                edges.append(CouplingEdge(
                    claim_slug=claim.slug,
                    concept_slug=slug,
                ))

    return claims, edges


def _build_system_prompt() -> str:
    """Build the system prompt for claim verification."""
    return (
        "You are a mathematical claim verification agent.\n"
        "You are given the original section text and extracted claims as JSON.\n"
        "Check each claim for:\n"
        "1. Completeness — are there claims in the text that weren't extracted?\n"
        "2. Fidelity — does each statement match the source verbatim?\n"
        "3. Proof completeness — is the proof text complete or truncated?\n"
        "4. Classification — is claim_type correct?\n"
        "5. proof_technique — is the label accurate?\n"
        "6. about_concepts — are references correct and non-duplicate?\n\n"
        "Return ONLY valid JSON with no additional text:\n"
        '{"missing_claims": [...], "corrections": [...], "flags": [...]}\n\n'
        "missing_claims: [{\"label\": \"...\", \"claim_type\": \"...\", "
        "\"statement\": \"...\", \"about_concepts\": [\"slug1\"]}]\n"
        "corrections: [{\"claim_slug\": \"...\", \"field\": \"...\", "
        "\"issue\": \"...\", \"corrected_value\": \"...\"}]\n"
        "flags: [{\"claim_slug\": \"...\", \"issue\": \"...\", "
        "\"confidence\": 0.5}]\n\n"
        "Rules:\n"
        "- Do NOT correct the 'label' field. Flag it instead.\n"
        "- Only flag claims with confidence below 0.7.\n"
        "- If everything looks correct, return empty arrays."
    )


def _build_user_prompt(
    section_text: str,
    proof_map: dict[str, str],
    claims: list[ClaimNode],
) -> str:
    """Build the user prompt with section text and extracted claims."""
    claims_json = json.dumps(
        [{"slug": c.slug, "label": c.label, "claim_type": c.claim_type,
          "statement": c.statement, "proof": c.proof,
          "proof_technique": c.proof_technique, "strength": c.strength}
         for c in claims],
        indent=2,
    )

    parts = [
        "## Source Text\n",
        section_text,
    ]

    if proof_map:
        parts.append("\n\n## Deferred Proofs\n")
        for label, text in proof_map.items():
            parts.append(f"Proof of {label}: {text}\n")

    parts.append(f"\n\n## Extracted Claims\n```json\n{claims_json}\n```")

    return "\n".join(parts)


def _safe_parse_json(content: str) -> dict | None:
    """Parse JSON, returning None on failure."""
    try:
        return json.loads(content)
    except (json.JSONDecodeError, ValueError):
        logger.warning("Verifier returned invalid JSON")
        return None
```

- [ ] **Step 4: Run tests**

Run: `python -m pytest tests/test_claim_verifier.py -v`
Expected: ALL PASS

- [ ] **Step 5: Commit**

```bash
git add tests/test_claim_verifier.py graph_builder/extraction/claim_verifier.py
git commit -m "feat(extraction): add Pass 4 claim verification with auto-fix"
```

---

## Chunk 5: Orchestrator Integration

### Task 14: Orchestrator — Dual LLM, Proof Map, Pass 4, Dedup, Clear

This is the largest task. It wires everything together.

**Files:**
- Modify test: `tests/test_v2_orchestrator.py`
- Modify: `graph_builder/orchestrator/orchestrator.py`

- [ ] **Step 1: Read existing orchestrator tests**

Read `tests/test_v2_orchestrator.py` to understand what's already tested.

- [ ] **Step 2: Add tests for new orchestrator functionality**

Append to `tests/test_v2_orchestrator.py`:

```python
class TestDedupCouplingEdges:
    """Tests for _dedup_coupling_edges()."""

    def test_it_should_remove_duplicate_coupling_edges(self):
        """It should keep only one edge per (claim_slug, concept_slug) pair."""
        from graph_builder.orchestrator.orchestrator import _dedup_coupling_edges

        edges = [
            CouplingEdge(claim_slug="c1", concept_slug="x", role="primary"),
            CouplingEdge(claim_slug="c1", concept_slug="x", role="scope"),
            CouplingEdge(claim_slug="c1", concept_slug="y", role="primary"),
        ]
        result = _dedup_coupling_edges(edges)

        assert len(result) == 2
        slugs = {(e.claim_slug, e.concept_slug) for e in result}
        assert slugs == {("c1", "x"), ("c1", "y")}

    def test_it_should_keep_later_entries_over_earlier(self):
        """It should prefer Pass 3a edges (appended later) over Pass 2."""
        from graph_builder.orchestrator.orchestrator import _dedup_coupling_edges

        edges = [
            CouplingEdge(claim_slug="c1", concept_slug="x", role="primary"),
            CouplingEdge(claim_slug="c1", concept_slug="x", role="mechanism"),
        ]
        result = _dedup_coupling_edges(edges)

        assert len(result) == 1
        assert result[0].role == "mechanism"
```

- [ ] **Step 3: Run tests to verify they fail**

Run: `python -m pytest tests/test_v2_orchestrator.py -v -k "dedup"`
Expected: FAIL — `cannot import name '_dedup_coupling_edges'`

- [ ] **Step 4: Update orchestrator.py**

Read the full current `graph_builder/orchestrator/orchestrator.py`. Make these changes:

**4a. Update imports** — add at the top:

```python
from graph_builder.extraction.proof_linker import build_proof_map
from graph_builder.extraction.claim_verifier import verify_section_claims
from graph_builder.llm.protocol import LLMClient
```

**4b. Update `process_paper` signature** — accept two LLM clients:

```python
async def process_paper(
    arxiv_id: str,
    options: PipelineOptions,
    llm_client: LLMClient,
    claim_llm_client: LLMClient | None = None,
    neo4j_client: Neo4jClient | None = None,
    embedding_client: EmbeddingClient | None = None,
) -> BuildResult:
```

When `claim_llm_client is None`, fall back to `llm_client` (backward-compatible). Pass both through `_execute_pipeline` and `_run_all_passes`.

**IMPORTANT:** This keeps the existing call signature working. Existing tests that pass `(arxiv_id, options, llm, neo4j, embedding)` will still work because `claim_llm_client` defaults to `None`.

Also update the `_patch_pipeline` helper in `tests/test_v2_orchestrator.py` to patch `load_paper` with a 3-tuple default:

Read `tests/test_v2_orchestrator.py` and find the `_patch_pipeline` helper. Change the `"load"` default from `("Test Paper", [_make_section("Intro", 0)])` to `("Test Paper", [_make_section("Intro", 0)], "Full paper text")`.

Also add a patch for `_run_pass4` (or `verify_section_claims`) returning `([], [])` by default, so existing tests don't hit real LLM calls during verification.

**4c. Update `_run_all_passes` signature** — accept `full_text` and `claim_llm_client`:

```python
async def _run_all_passes(
    arxiv_id: str,
    title: str,
    sections: list[Section],
    full_text: str,
    options: PipelineOptions,
    llm_client: LLMClient,
    claim_llm_client: LLMClient,
    neo4j_client: Neo4jClient,
    embedding_client: EmbeddingClient | None,
) -> BuildResult:
```

**4d. Add proof linker call** — in `_run_all_passes`, after getting the paper_slug:

```python
    proof_map = build_proof_map(full_text)
```

**4e. Pass proof_map and claim_llm_client to Pass 2** — update `_run_pass2` call:

Use `claim_llm_client` instead of `llm_client` for Pass 2, and pass `proof_map`.

**4f. Add coupling edge dedup** — after `coupling_edges.extend(extra_coupling)`:

```python
    coupling_edges = _dedup_coupling_edges(coupling_edges)
```

**4g. Add `_dedup_coupling_edges` function:**

```python
def _dedup_coupling_edges(edges: list[CouplingEdge]) -> list[CouplingEdge]:
    """Deduplicate coupling edges, keeping later entries (Pass 3a over Pass 2).

    @param edges Combined coupling edges from all passes
    @returns Deduplicated list
    """
    seen: dict[tuple[str, str], CouplingEdge] = {}
    for edge in edges:
        key = (edge.claim_slug, edge.concept_slug)
        seen[key] = edge
    return list(seen.values())
```

**4h. Add Pass 4** — after `_run_pass3b`, before validation:

```python
    new_claims, new_coupling = await _run_pass4(
        sections, claims, proof_map, claim_llm_client,
        paper_slug, options.concurrency,
    )
    claims.extend(new_claims)
    coupling_edges.extend(new_coupling)
```

**4i. Add `_run_pass4` function:**

```python
async def _run_pass4(
    sections: list[Section],
    claims: list[ClaimNode],
    proof_map: dict[str, str],
    llm_client: LLMClient,
    paper_slug: str,
    concurrency: int,
) -> tuple[list[ClaimNode], list[CouplingEdge]]:
    """Pass 4: parallel per-section claim verification.

    @param sections Paper sections
    @param claims All extracted claims (mutated in-place for corrections/flags)
    @param proof_map Proof location mapping
    @param llm_client Claude client for verification
    @param paper_slug Paper slug for new claims
    @param concurrency Max parallel calls
    @returns Tuple of (new_claims, new_coupling_edges)
    """
    claims_by_section = _group_claims_by_section(claims, sections)
    semaphore = asyncio.Semaphore(concurrency)

    tasks = [
        _verify_section_guarded(
            section, claims_by_section.get(section.heading, []),
            proof_map, llm_client, paper_slug, semaphore,
        )
        for section in sections
    ]
    results = await asyncio.gather(*tasks)
    return _flatten_claim_results(results)


async def _verify_section_guarded(
    section: Section,
    section_claims: list[ClaimNode],
    proof_map: dict[str, str],
    llm_client: LLMClient,
    paper_slug: str,
    semaphore: asyncio.Semaphore,
) -> tuple[list[ClaimNode], list[CouplingEdge]]:
    """Verify a section's claims with error isolation.

    @param section Section to verify
    @param section_claims Claims in this section
    @param proof_map Proof location mapping
    @param llm_client Claude client
    @param paper_slug Paper slug
    @param semaphore Concurrency limiter
    @returns Tuple of (new_claims, coupling_edges), empty on failure
    """
    async with semaphore:
        try:
            return await verify_section_claims(
                section.content, proof_map, section_claims,
                None, llm_client, paper_slug, section.heading,
            )
        except Exception as err:
            logger.warning(
                "Verification failed for '%s': %s",
                section.heading, err,
            )
            return [], []
```

**4j. Add clear-on-force** — in `_run_all_passes`, after validation and before write:

```python
    if options.force:
        writer = GraphWriter(neo4j_client)
        await writer.clear_paper_claims(paper_slug)
        await writer.clear_paper_provenances(arxiv_id)

    writer = GraphWriter(neo4j_client)
```

**4k. Update `_run_pass2`** — add `proof_map` parameter, pass to `extract_claims_from_section`:

```python
async def _run_pass2(
    sections: list[Section],
    schema: GraphSchema,
    llm_client: LLMClient,
    merged: list[MergedConcept],
    paper_slug: str,
    concurrency: int,
    proof_map: dict[str, str] | None = None,
) -> tuple[list[ClaimNode], list[CouplingEdge]]:
```

And pass `proof_map=proof_map` to `extract_claims_from_section`.

- [ ] **Step 5: Run all tests**

Run: `python -m pytest tests/test_v2_orchestrator.py -v`
Expected: ALL PASS

- [ ] **Step 6: Commit**

```bash
git add tests/test_v2_orchestrator.py graph_builder/orchestrator/orchestrator.py
git commit -m "feat(orchestrator): integrate proof linker, Pass 4, dedup, dual LLM, clear-on-force"
```

---

## Chunk 6: CLI Entry Point and Re-extraction

### Task 15: CLI Entry Point — main.py

**Files:**
- Create test: `tests/test_main_cli.py`
- Create: `main.py`

- [ ] **Step 1: Write the test file**

Create `tests/test_main_cli.py`:

```python
"""
@file test_main_cli.py
@description Tests for the CLI entry point argument parsing and file detection.
"""

import pytest


class TestParseArxivIds:
    """Tests for _parse_arxiv_ids()."""

    def test_it_should_return_single_id_from_positional_arg(self):
        """It should wrap a single arxiv_id in a list."""
        from main import _parse_arxiv_ids

        result = _parse_arxiv_ids("k_strong_price_of_anarchy", None)
        assert result == ["k_strong_price_of_anarchy"]

    def test_it_should_read_ids_from_csv_with_header(self, tmp_path):
        """It should read arxiv_ids from a CSV file with header."""
        from main import _parse_arxiv_ids

        csv_file = tmp_path / "papers.csv"
        csv_file.write_text("arxiv_id\n1904.07272\n1011.4748\n")

        result = _parse_arxiv_ids(None, str(csv_file))
        assert result == ["1904.07272", "1011.4748"]

    def test_it_should_read_ids_from_plain_text_file(self, tmp_path):
        """It should read one ID per line from a plain text file."""
        from main import _parse_arxiv_ids

        txt_file = tmp_path / "papers.txt"
        txt_file.write_text("1904.07272\n1011.4748\n")

        result = _parse_arxiv_ids(None, str(txt_file))
        assert result == ["1904.07272", "1011.4748"]

    def test_it_should_skip_empty_lines(self, tmp_path):
        """It should ignore blank lines in the input file."""
        from main import _parse_arxiv_ids

        txt_file = tmp_path / "papers.txt"
        txt_file.write_text("1904.07272\n\n1011.4748\n\n")

        result = _parse_arxiv_ids(None, str(txt_file))
        assert result == ["1904.07272", "1011.4748"]

    def test_it_should_raise_when_no_input_provided(self):
        """It should raise SystemExit when no arxiv_id or csv is given."""
        from main import _parse_arxiv_ids

        with pytest.raises(SystemExit):
            _parse_arxiv_ids(None, None)
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_main_cli.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'main'`

- [ ] **Step 3: Write main.py**

Create `main.py` at the project root:

```python
"""
@file main.py
@description CLI entry point for the Theo-Fish ETL extraction pipeline.
Processes single papers or CSV batches through the full pipeline.
"""

import argparse
import asyncio
import logging
import sys
from pathlib import Path

from graph_builder.config.config import (
    ANTHROPIC_API_KEY,
    DEEPSEEK_API_KEY,
    DEFAULT_CONCURRENCY,
    SCHEMA_PATH,
    VAULT_DIR,
)
from graph_builder.config.schema_loader import load_schema
from graph_builder.graph.neo4j_client import Neo4jClient
from graph_builder.llm.claude_client import ClaudeClient
from graph_builder.llm.llm_client import DeepSeekClient
from graph_builder.orchestrator.orchestrator import PipelineOptions, process_paper
from graph_builder.vault.obsidian_exporter import export_vault
from graph_builder.graph.graph_reader import GraphReader

logger = logging.getLogger("graph_builder")

_CSV_HEADER = "arxiv_id"


def _parse_arxiv_ids(
    arxiv_id: str | None,
    csv_path: str | None,
) -> list[str]:
    """Parse paper IDs from CLI arguments.

    @param arxiv_id Single paper ID from positional arg
    @param csv_path Path to CSV or plain text file
    @returns List of arxiv IDs
    @raises SystemExit if no input provided
    """
    if arxiv_id:
        return [arxiv_id]

    if csv_path is None:
        print("Error: provide an arxiv_id or --csv file", file=sys.stderr)
        raise SystemExit(1)

    return _read_id_file(csv_path)


def _read_id_file(path: str) -> list[str]:
    """Read arxiv IDs from a CSV or plain text file.

    Detection: if first line is exactly 'arxiv_id', treat as CSV with
    header. Otherwise treat as plain text with one ID per line.

    @param path Path to the input file
    @returns List of arxiv IDs
    """
    lines = Path(path).read_text(encoding="utf-8").strip().splitlines()
    if not lines:
        return []

    if lines[0].strip() == _CSV_HEADER:
        lines = lines[1:]

    return [line.strip() for line in lines if line.strip()]


def _build_arg_parser() -> argparse.ArgumentParser:
    """Build the CLI argument parser."""
    parser = argparse.ArgumentParser(
        description="Theo-Fish ETL: extract mathematical knowledge from papers",
    )
    parser.add_argument(
        "arxiv_id", nargs="?", default=None,
        help="ArXiv ID or paper name to process",
    )
    parser.add_argument(
        "--csv", dest="csv_path", default=None,
        help="Path to CSV or text file with paper IDs",
    )
    parser.add_argument(
        "--force", action="store_true",
        help="Re-extract even if paper already built",
    )
    parser.add_argument(
        "--concurrency", type=int, default=DEFAULT_CONCURRENCY,
        help=f"Max parallel LLM calls (default: {DEFAULT_CONCURRENCY})",
    )
    parser.add_argument(
        "--no-export", action="store_true",
        help="Skip vault export after processing",
    )
    return parser


async def _run(args: argparse.Namespace) -> int:
    """Execute the pipeline for all papers and return exit code.

    @param args Parsed CLI arguments
    @returns 0 on success, 1 if any paper failed
    """
    arxiv_ids = _parse_arxiv_ids(args.arxiv_id, args.csv_path)
    schema = load_schema(SCHEMA_PATH)

    deepseek_client = DeepSeekClient(concurrency=args.concurrency)
    claude_client = ClaudeClient(concurrency=args.concurrency)
    neo4j_client = Neo4jClient()

    options = PipelineOptions(
        schema=schema,
        concurrency=args.concurrency,
        force=args.force,
    )

    built, skipped, failed = 0, 0, 0

    try:
        await neo4j_client.connect()

        for paper_id in arxiv_ids:
            logger.info("Processing: %s", paper_id)
            result = await process_paper(
                paper_id, options, deepseek_client,
                claude_client, neo4j_client,
            )
            if result.status == "built":
                built += 1
                logger.info("Built: %s", paper_id)
            elif result.status == "skipped":
                skipped += 1
                logger.info("Skipped: %s", paper_id)
            else:
                failed += 1
                logger.error("Failed: %s — %s", paper_id, result.error)

        if not args.no_export:
            reader = GraphReader(neo4j_client)
            await export_vault(VAULT_DIR, reader, neo4j_client)
            logger.info("Vault exported to %s", VAULT_DIR)

    finally:
        await neo4j_client.close()

    print(f"\nSummary: {built} built, {skipped} skipped, {failed} failed")
    return 1 if failed > 0 else 0


def main():
    """CLI entry point."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    parser = _build_arg_parser()
    args = parser.parse_args()
    exit_code = asyncio.run(_run(args))
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run tests**

Run: `python -m pytest tests/test_main_cli.py -v`
Expected: ALL PASS

- [ ] **Step 5: Commit**

```bash
git add tests/test_main_cli.py main.py
git commit -m "feat(cli): add main.py entry point for single paper and CSV batch processing"
```

---

### Task 16: Re-extract Existing Paper

This is a manual execution step, not code.

- [ ] **Step 1: Run the full pipeline on the existing paper**

```bash
python main.py k_strong_price_of_anarchy --force
```

Expected: Pipeline processes the paper through all passes (P1-P4), clears old data, writes new data with proofs, and exports the vault.

- [ ] **Step 2: Verify proofs are populated**

Check a theorem file:
```bash
head -20 data_vault/claims/theorems/k-strong-price-of-anarchy--theorem-iii-3.md
```

Expected: The `proof:` field should now contain proof text instead of `''`.

- [ ] **Step 3: Verify no duplicate edges**

Check the about edges in a theorem file — there should be no duplicate concept links.

- [ ] **Step 4: Check Neo4j for proofs**

Open http://localhost:7474/browser/ and run:
```cypher
MATCH (cl:Claim) WHERE cl.proof <> '' RETURN cl.label, cl.proof LIMIT 5
```

Expected: Results with populated proof text.

- [ ] **Step 5: Commit any post-run fixes**

If any issues are found during re-extraction, fix and commit.

---

## Run Order Summary

| Task | Name | Depends On |
|---|---|---|
| 1 | Config + dependency | — |
| 2 | LLM Protocol | — |
| 3 | ClaimNode confidence | — |
| 4 | Claude Client | 1, 2 |
| 5 | Proof Linker | — |
| 6 | Enhanced Prompt | — |
| 7 | Response Parser Tests | 3 |
| 8 | Pipeline Loader | — |
| 9 | Claim Extractor Changes | 2, 5 |
| 10 | Type Hint Updates | 2 |
| 11 | Graph Writer Clear | — |
| 12 | Graph Reader DISTINCT | — |
| 13 | Claim Verifier | 2, 3 |
| 14 | Orchestrator Integration | 4, 5, 8, 9, 10, 11, 13 |
| 15 | CLI main.py | 4, 14 |
| 16 | Re-extraction | 15 |

**Parallelizable groups:**
- Tasks 1, 2, 3, 5, 6, 8, 11, 12 can run in parallel (no interdependencies)
- Tasks 4, 7, 9, 10 can run in parallel after their deps
- Task 13 after 2+3
- Task 14 after all above
- Task 15 after 14
- Task 16 after 15
