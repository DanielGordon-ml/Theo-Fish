# Extraction Quality Overhaul — Design Spec

**Date:** 2026-03-16
**Status:** Approved
**Scope:** Full quality overhaul of the claim extraction pipeline — proof extraction, LLM upgrade, verification pass, dedup fixes, CLI entry point

---

## Problem Statement

The current extraction pipeline produces claims with:
- Empty `proof` fields on all 33 extracted claims
- Empty `proof_technique` and `strength` fields
- Vague/paraphrased theorem statements instead of verbatim text
- Duplicate `about` edges (same concept listed twice per claim)
- Duplicate `sourced_from` edges
- All concept roles set to `"primary"` with no differentiation
- No proofs visible in Neo4j or the Obsidian vault

**Root causes:**
1. The claim extraction prompt (`prompt_generator.py:131-133`) never asks for `proof`, `proof_technique`, `strength`, or `confidence` in its JSON output spec
2. Deferred proofs (in appendices) are in different sections than their theorems — the per-section extraction never sees them together
3. No verification pass exists to catch paraphrased statements or missing claims
4. Coupling edges from Pass 2 and Pass 3a are appended without dedup
5. Duplicate `sourced_from` in vault export — root cause to be confirmed during implementation (likely from running pipeline twice without clearing, or from the graph reader query returning both Claim and Provenance SOURCED_FROM edges)

---

## Approach: Proof-Aware Pipeline (Approach B)

1. **Proof-linking pre-pass** — Regex scan of full paper text to map theorem labels to proof locations. Inject deferred proof text into the relevant section's LLM context.
2. **LLM upgrade** — Switch claim extraction (Pass 2) and verification (Pass 4) to Claude Opus 4.6. Keep DeepSeek V3 for concepts (Pass 1), edge enrichment (Pass 3a), and gap-fill (Pass 3b).
3. **Enhanced prompt** — Ask for `proof`, `proof_technique`, `strength`, `confidence` per claim. Require verbatim statements.
4. **Verification pass (Pass 4)** — Post-extraction Claude call checks completeness, fidelity, proof completeness, classification, and concept references. Auto-fixes where possible, routes low-confidence claims to `_review/`.
5. **Dedup fixes** — Deduplicate coupling edges, fix double sourced_from creation.
6. **Re-extraction** — Re-run the existing paper with `force=True` after pipeline changes.
7. **CLI entry point** — New `main.py` for running single papers or CSV batches.

---

## Design

### 1. Claude LLM Client

**New file:** `graph_builder/llm/claude_client.py`

**New dependency:** `anthropic>=0.40` — add to `pyproject.toml` under `[project.dependencies]`.

**LLM client protocol:** Introduce `LLMClient` — a `typing.Protocol` class in a new file `graph_builder/llm/protocol.py`:
```python
class LLMClient(Protocol):
    async def call(self, system_prompt: str, user_prompt: str, thinking: bool | None = None) -> LLMResponse: ...
```
All extraction functions (`claim_extractor`, `concept_extractor`, `edge_enricher`, `cross_section_linker`, `claim_verifier`) change their type hints from `DeepSeekClient` to `LLMClient`. Both `DeepSeekClient` and `ClaudeClient` satisfy this protocol.

Async wrapper around `anthropic.AsyncAnthropic`:
- Implements `LLMClient` protocol: `call(system_prompt, user_prompt, thinking?) -> LLMResponse`
- Reads `ANTHROPIC_API_KEY` from config
- Model: `claude-opus-4-6`
- JSON output via prompt instruction ("Return ONLY valid JSON with no additional text.") + robust parsing: (a) attempt `json.loads()` on full response, (b) if that fails, extract content between `` ```json `` and `` ``` `` fences, (c) if that fails, treat as section failure (same as current DeepSeek parse failure path)
- Same retry/backoff logic: exponential backoff with jitter on 429/5xx, max 3 retries
- Same semaphore-based concurrency limiting

**Config additions** (`config.py`):
- `ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")`
- `CLAUDE_MODEL = "claude-opus-4-6"`
- `CLAIM_LLM = "claude"` — toggle for which LLM handles claim extraction + verification

**Pass-to-LLM mapping:**
| Pass | LLM | Rationale |
|---|---|---|
| Pass 1: Concepts | DeepSeek V3 | Simpler extraction task |
| Pass 2: Claims + Proofs | Claude Opus 4.6 | Needs precision on math text, verbatim extraction, proof parsing |
| Pass 3a: Edge enrichment | DeepSeek V3 | Structured relationship extraction, adequate quality |
| Pass 3b: Gap-fill | DeepSeek V3 | Cross-section linking, adequate quality |
| Pass 4: Verification | Claude Opus 4.6 | Critical quality gate, needs highest reasoning capability |

---

### 2. Proof-Linking Pre-Pass

**New file:** `graph_builder/extraction/proof_linker.py`

**Function:** `build_proof_map(full_text: str) -> dict[str, str]`

**Algorithm:**
1. Regex scan for deferred proof markers: `Proof of (Theorem|Lemma|Proposition|Corollary) <label>:`
2. Regex scan for inline proof markers: `Proof\.` / `Proof:` / `*Proof.*` following a claim
3. Extract proof text: everything from marker until next heading, QED symbol (`∎`, `□`, `$\square$`, `$\blacksquare$`), or next theorem/proof marker
4. Return `dict[str, str]` mapping normalized claim labels to proof text

**Integration with Pass 2:**
- `pipeline_loader.py` → `load_paper()` is modified to return the full markdown text alongside sections: `tuple[str, list[Section], str]` (title, sections, full_text). The full text is read before splitting and returned as the third element.
- Orchestrator calls `build_proof_map(full_text)` once before claim extraction
- `claim_extractor.py` receives the proof map
- When building the user prompt for a section, if any theorem in the section has a deferred proof in the map, append it:

```
[Original section content]

--- DEFERRED PROOF (from appendix) ---
Proof of Theorem III.3: The proof can be outlined in four parts...
```

- Inline proofs (already in the section) are not injected — the LLM sees them naturally
- The proof map is also passed to the verification pass for cross-checking

---

### 3. Enhanced Claim Extraction Prompt

**Changes to** `prompt_generator.py` **→** `_claim_output_format()`:

New JSON output spec:
```json
{
  "claims": [{
    "claim_type": "<type>",
    "label": "<e.g. Theorem III.3>",
    "statement": "<full verbatim statement, including math notation>",
    "assumptions": ["<assumption 1>", "..."],
    "conclusion": "<main result>",
    "proof": "<full proof text if present, empty string if not>",
    "proof_technique": "<e.g. induction, contradiction, constructive, probabilistic>",
    "strength": "<exact|asymptotic|approximate|existential>",
    "confidence": 0.95,
    "about_concepts": ["<slug_1>", "<slug_2>"]
  }]
}
```

**New prompt rules:**
- "Extract the FULL statement verbatim from the paper, preserving all math notation. Do not summarize."
- "Extract the FULL proof text if present in the section or in a deferred proof block. Preserve all math steps."
- "proof_technique is REQUIRED for theorem, lemma, and proposition types."
- "confidence: your confidence that the extraction is complete and accurate (0.0–1.0). Below 0.7 means you are uncertain about completeness."
- "Each concept in about_concepts must have a distinct role. Do not list the same concept twice."

**Changes to** `_format_claim_type()`:
- Emit `strength_values` from schema (e.g., `[exact, asymptotic, approximate, existential]`) so the LLM knows valid values

**Changes to** `response_parser.py` **→** `_build_claim()`:
- Parse `proof`, `proof_technique`, `strength` into ClaimNode fields (already exist on model)
- Extract `confidence` from LLM response — stored as a new optional field on `ClaimNode` (`confidence: float = 0.0`). Not written to Neo4j (excluded from `_claim_params()` in graph_writer). Used by verification pass for review routing. This is simpler than a parallel sidecar structure.

---

### 4. Verification Pass (Pass 4)

**New file:** `graph_builder/extraction/claim_verifier.py`

**Function:** `verify_section_claims(section_text, injected_proofs, extracted_claims, schema, llm_client) -> VerificationResult`

**Execution:** Single Claude call per section (batched, not per-claim).

**Input to verifier:**
- Original section text
- Deferred proof text (if any was injected)
- Extracted claims as JSON

**System prompt checks:**
1. **Completeness** — Claims in the text that weren't extracted?
2. **Fidelity** — Does each statement match the source? Flag hallucinated or paraphrased text.
3. **Proof completeness** — Is proof text complete or truncated/omitted?
4. **Classification** — Is claim_type correct?
5. **proof_technique** — Is the label accurate?
6. **about_concepts** — Correct and non-duplicate references?

**Output format:**
```json
{
  "missing_claims": [
    {"label": "Lemma 2", "statement": "...", "location": "after Theorem III.3"}
  ],
  "corrections": [
    {
      "claim_slug": "...",
      "field": "statement",
      "issue": "paraphrased, not verbatim",
      "corrected_value": "..."
    }
  ],
  "flags": [
    {
      "claim_slug": "...",
      "issue": "proof appears truncated",
      "confidence": 0.4
    }
  ]
}
```

**Auto-fix logic:**
- `missing_claims` → Constructed as new ClaimNodes with `source_paper_slug` and `section` from context. The verifier must supply `label`, `claim_type`, `statement`, `about_concepts`. New claims also get ABOUT coupling edges generated from `about_concepts` (same as Pass 2). Added to the claims and coupling_edges lists before validation.
- `corrections` → Applied to relevant ClaimNode fields in-place. **Rule: `label` corrections are NOT permitted** — changing a label would change the slug, invalidating all edges. If the verifier flags a wrong label, it becomes a `flag` entry for human review instead.
- `flags` with `confidence < 0.7` → `claim.status` is set to `"review_needed"` on the ClaimNode. The existing vault exporter already checks `claim.status == "review_needed"` and copies to `_review/claims/` (see `obsidian_exporter.py:_write_claim_file()`).

**Integration:**
- New `_run_pass4()` in orchestrator, after Pass 3b and before validation
- The orchestrator maintains a `claims_by_section: dict[str, list[ClaimNode]]` mapping (built during Pass 2 using `claim.section`). This mapping persists through Passes 3a/3b and is passed to Pass 4 so the verifier receives per-section claim batches alongside the original section text.
- Parallel per-section, same semaphore pattern as other passes
- Uses Claude client
- Returns `tuple[list[ClaimNode], list[CouplingEdge]]` (new claims + their ABOUT edges) which are appended to the main lists before validation

---

### 5. Dedup Fixes

**Bug 1: Duplicate coupling edges**

Pass 2 creates ABOUT edges from `about_concepts`. Pass 3a also creates ABOUT edges. The orchestrator appends both without dedup.

**Fix:** In `orchestrator.py` → `_run_all_passes()`, after combining coupling edges from Pass 2 and 3a, deduplicate using a dict keyed by `(claim_slug, concept_slug)`:
```python
def _dedup_coupling_edges(edges: list[CouplingEdge]) -> list[CouplingEdge]:
    seen: dict[tuple[str, str], CouplingEdge] = {}
    for edge in edges:
        key = (edge.claim_slug, edge.concept_slug)
        seen[key] = edge  # later entries (Pass 3a) overwrite earlier (Pass 2)
    return list(seen.values())
```
Call this after `coupling_edges.extend(extra_coupling)`, passing the combined list. Pass 3a edges are appended second, so they naturally win.

**Bug 2: Duplicate sourced_from in vault export**

Investigation shows `pipeline_writer.py` does NOT write explicit `SOURCED_FROM` edges for claims — the only creation is inside `graph_writer.py`'s `_CREATE_CLAIM_CYPHER`. The duplication in the vault files is most likely caused by running the pipeline multiple times without clearing (the `force` flag was not previously wired to clear old data). The re-extraction fix (Section 6) resolves this by clearing claims before re-writing.

**Fix:** Add `DISTINCT` to the graph reader's `get_all_sourced_from_edges()` query as a defensive measure:
```cypher
MATCH (n)-[r:SOURCED_FROM]->(s:Source)
WHERE n:Claim OR n:Provenance
RETURN DISTINCT coalesce(n.slug, n.concept_slug) AS node_slug, ...
```

**Bug 3: All roles "primary"**

Pass 2 doesn't ask for roles — just flat slug list. Pass 3a should refine roles but its enriched edges get appended as duplicates. Already handled by Bug 1 fix: keeping Pass 3a's version preserves refined roles.

---

### 6. Re-extraction Flow

**Problem:** Claim nodes use `CREATE` (not `MERGE`), so re-running creates duplicates.

**Fix:** Add `_clear_paper_data()` in `_run_all_passes()`, called **after validation succeeds and before writing to Neo4j**. This ensures old data is only deleted when new data is ready to replace it. If extraction or validation fails, old data is preserved.

**New methods on** `GraphWriter`:
- `clear_paper_claims(paper_slug)`:
  ```cypher
  MATCH (cl:Claim {source_paper_slug: $paper_slug})
  DETACH DELETE cl
  ```
- `clear_paper_provenances(arxiv_id)`:
  ```cypher
  MATCH (p:Provenance {source_arxiv_id: $arxiv_id})
  DETACH DELETE p
  ```

**Flow when `force=True`:**
1. Run full extraction pipeline (Passes 1-4)
2. Validate extracted data
3. If validation passes: clear existing claims and provenances for this paper
4. Write new data (concepts update in place via `MERGE`)
5. Export vault

If extraction or validation fails, old data remains untouched.

---

### 7. CLI Entry Point

**New file:** `ETL/main.py`

**Usage:**
```bash
# Single paper
python main.py k_strong_price_of_anarchy

# CSV file
python main.py --csv papers.csv

# Options
python main.py k_strong_price_of_anarchy --force
python main.py --csv papers.csv --concurrency 5
python main.py k_strong_price_of_anarchy --no-export
```

**Flow:**
1. Parse args (`argparse`): positional `arxiv_id` or `--csv` path, plus `--force`, `--concurrency`, `--no-export`
2. Load schema from `schema.yaml`
3. Initialize clients: Claude (claims/verification), DeepSeek (concepts/edges), Neo4j, Embedding (optional)
4. For each paper:
   - Call `process_paper()` with appropriate clients
   - Log result (built/skipped/failed)
5. After all papers: `export_vault()` unless `--no-export`
6. Print summary: X built, Y skipped, Z failed
7. Exit code 0 if all succeeded, 1 if any failed

**CSV format:**
```csv
arxiv_id
k_strong_price_of_anarchy
1904.07272
```
CSV files must include an `arxiv_id` header row. Plain text files (one ID per line, no header) are also accepted — detection rule: if the first line is exactly `arxiv_id`, treat as CSV; otherwise treat as plain text.

---

## Files Changed

| File | Change Type |
|---|---|
| `ETL/main.py` | **New** — CLI entry point |
| `graph_builder/llm/protocol.py` | **New** — `LLMClient` protocol definition |
| `graph_builder/llm/claude_client.py` | **New** — Claude Opus 4.6 async client |
| `graph_builder/extraction/proof_linker.py` | **New** — Proof location mapper |
| `graph_builder/extraction/claim_verifier.py` | **New** — Pass 4 verification |
| `graph_builder/config/config.py` | Modified — Anthropic config, CLAIM_LLM toggle |
| `graph_builder/extraction/prompt_generator.py` | Modified — Enhanced claim prompt |
| `graph_builder/extraction/claim_extractor.py` | Modified — Accept proof map, inject deferred proofs, type hint `LLMClient` |
| `graph_builder/extraction/concept_extractor.py` | Modified — Type hint `LLMClient` |
| `graph_builder/extraction/edge_enricher.py` | Modified — Type hint `LLMClient` |
| `graph_builder/extraction/cross_section_linker.py` | Modified — Type hint `LLMClient` |
| `graph_builder/llm/response_parser.py` | Modified — Parse proof/strength/confidence fields |
| `graph_builder/models/claim.py` | Modified — Add `confidence: float = 0.0` field |
| `graph_builder/orchestrator/orchestrator.py` | Modified — Proof linker, Pass 4, dedup, clear-on-force, dual LLM, section-claims mapping |
| `graph_builder/orchestrator/pipeline_loader.py` | Modified — Return full markdown text as third element |
| `graph_builder/graph/graph_writer.py` | Modified — Add clear methods |
| `graph_builder/graph/graph_reader.py` | Modified — Add DISTINCT to sourced_from query |
| `pyproject.toml` | Modified — Add `anthropic>=0.40` dependency |

**Unchanged:** `schema.yaml`, vault exporter, frontmatter builder, section splitter, validator.

---

## Test Files

Per project rules (CLAUDE.md: "ALWAYS write the test file before the implementation file"), the following test files must be created before their corresponding implementation files:

| Test File | Covers |
|---|---|
| `graph_builder/llm/test_protocol.py` | LLMClient protocol compliance for both clients |
| `graph_builder/llm/test_claude_client.py` | Claude client: retry logic, JSON extraction fallbacks, semaphore |
| `graph_builder/extraction/test_proof_linker.py` | Proof map building: inline proofs, deferred proofs, edge cases (no proofs, multiple proofs for same theorem) |
| `graph_builder/extraction/test_claim_verifier.py` | Verification pass: missing claims, corrections, flags, label-correction rejection |
| `test_main.py` | CLI: single paper, CSV input, plain text input, --force, --no-export |
| `graph_builder/extraction/test_prompt_generator.py` | Updated — New claim output format includes proof/strength/confidence fields |
| `graph_builder/llm/test_response_parser.py` | Updated — Parsing proof/strength/confidence from claim JSON |
| `graph_builder/orchestrator/test_orchestrator.py` | Updated — Coupling edge dedup, Pass 4 integration, clear-on-force ordering |
| `graph_builder/graph/test_graph_writer.py` | Updated — Clear methods |

---

## Pipeline Flow After Changes

```
main.py (CLI)
  │
  ├─ Load schema, init clients (Claude + DeepSeek + Neo4j)
  │
  └─ Per paper:
       ├─ Load paper → Split sections + retain full_text
       ├─ Proof linker: build_proof_map(full_text) ← NEW
       │
       ├─ Pass 1: Concept extraction (DeepSeek, parallel per-section)
       ├─ Merge: intra-paper dedup + cross-vault cascade
       │
       ├─ Pass 2: Claim + Proof extraction (Claude, parallel per-section)
       │   └─ Injects deferred proofs from proof map
       │
       ├─ Pass 3a: Edge enrichment (DeepSeek, parallel per-section)
       ├─ Dedup coupling edges (Pass 2 vs 3a) ← FIX
       ├─ Pass 3b: Cross-section gap-fill (DeepSeek, single call)
       │
       ├─ Pass 4: Verification (Claude, parallel per-section) ← NEW
       │   └─ Auto-fix + route low-confidence to _review/
       │
       ├─ Validate
       ├─ Clear old data (if force=True, AFTER validation) ← NEW
       ├─ Write to Neo4j ← FIX (DISTINCT sourced_from)
       └─ Export vault
```
