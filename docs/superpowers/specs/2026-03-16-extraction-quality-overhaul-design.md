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
5. `SOURCED_FROM` edges are created twice (once in claim CREATE query, once in explicit edge writes)

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

Async wrapper around `anthropic.AsyncAnthropic`:
- Same interface as `DeepSeekClient`: `call(system_prompt, user_prompt, thinking?) -> LLMResponse`
- Reads `ANTHROPIC_API_KEY` from config
- Model: `claude-opus-4-6`
- JSON output via prompt instruction + response parsing (Anthropic SDK does not support `response_format: json_object`)
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
- Extract `confidence` from LLM response into return metadata (not stored on ClaimNode — used by verification pass and review routing)

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
- `missing_claims` → Extracted as new ClaimNodes, added to claims list
- `corrections` → Applied directly to relevant ClaimNode fields
- `flags` with `confidence < 0.7` → Claim status set to `"review_needed"`, routes to `_review/claims/` during vault export

**Integration:** New `_run_pass4()` in orchestrator, after Pass 3b and before validation. Parallel per-section, same pattern as other passes. Uses Claude client.

---

### 5. Dedup Fixes

**Bug 1: Duplicate coupling edges**

Pass 2 creates ABOUT edges from `about_concepts`. Pass 3a also creates ABOUT edges. The orchestrator appends both without dedup.

**Fix:** In `orchestrator.py` → `_run_all_passes()`, after combining coupling edges from Pass 2 and 3a, deduplicate by `(claim_slug, concept_slug)` pair. When duplicates exist, keep Pass 3a's version (richer `role`/`aspect` attributes).

**Bug 2: Duplicate sourced_from edges**

The claim CREATE query already creates a `SOURCED_FROM` edge. Then `pipeline_writer.py` writes explicit `SOURCED_FROM` edges from the edge list, creating a second.

**Fix:** In `pipeline_writer.py`, skip writing explicit `SOURCED_FROM` edges for claims since they're already created in the claim CREATE query. Alternatively, deduplicate in `graph_reader.py` → `get_all_sourced_from_edges()` using `DISTINCT`.

**Bug 3: All roles "primary"**

Pass 2 doesn't ask for roles — just flat slug list. Pass 3a should refine roles but its enriched edges get appended as duplicates. Already handled by Bug 1 fix: keeping Pass 3a's version preserves refined roles.

---

### 6. Re-extraction Flow

**Problem:** Claim nodes use `CREATE` (not `MERGE`), so re-running creates duplicates.

**Fix:** Add `_clear_paper_data()` in `_execute_pipeline()`, gated on `force=True`.

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
1. Clear existing claims for this paper
2. Clear existing provenances for this paper
3. Concept nodes update in place (already `MERGE`-based)
4. Run full pipeline as normal
5. Write new data
6. Export vault

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
Auto-detects plain text (one ID per line) vs CSV with header.

---

## Files Changed

| File | Change Type |
|---|---|
| `ETL/main.py` | **New** — CLI entry point |
| `graph_builder/llm/claude_client.py` | **New** — Claude Opus 4.6 async client |
| `graph_builder/extraction/proof_linker.py` | **New** — Proof location mapper |
| `graph_builder/extraction/claim_verifier.py` | **New** — Pass 4 verification |
| `graph_builder/config/config.py` | Modified — Anthropic config, CLAIM_LLM toggle |
| `graph_builder/extraction/prompt_generator.py` | Modified — Enhanced claim prompt |
| `graph_builder/extraction/claim_extractor.py` | Modified — Accept proof map, inject deferred proofs |
| `graph_builder/llm/response_parser.py` | Modified — Parse proof/strength/confidence fields |
| `graph_builder/orchestrator/orchestrator.py` | Modified — Proof linker, Pass 4, dedup, clear-on-force, dual LLM |
| `graph_builder/orchestrator/pipeline_writer.py` | Modified — Fix duplicate sourced_from |
| `graph_builder/graph/graph_writer.py` | Modified — Add clear methods |

**Unchanged:** `schema.yaml`, `ClaimNode` model, vault exporter, frontmatter builder, section splitter, concept extractor, edge enricher, cross-section linker, validator.

---

## Pipeline Flow After Changes

```
main.py (CLI)
  │
  ├─ Load schema, init clients (Claude + DeepSeek + Neo4j)
  │
  └─ Per paper:
       ├─ Load paper → Split sections
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
       ├─ Clear old data (if force=True) ← NEW
       ├─ Write to Neo4j (fix duplicate sourced_from) ← FIX
       └─ Export vault
```
