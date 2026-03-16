# The Dual-Graph Approach to Mathematical Knowledge Graphs
## The Reframe: Rhetorical Type Becomes Metadata, Not Node Identity

Don't throw away your current types. **Demote them from node type to node attribute.** Every node in *both* graphs carries a `rhetorical_origin` field, but its primary type comes from a new semantic schema.

---

## Graph A — Concept Ontology

These are nodes for **the mathematical objects themselves**. The node types should be:

| Type | What It Captures | Typical Source |
|---|---|---|
| `structure` | Named mathematical objects | definitions |
| `space` | Sets, domains, topologies | definitions |
| `operator` | Functions, maps, transforms | definitions, notations |
| `property` | Attributes a structure can have | definitions, remarks |
| `quantity` | Measurable values, metrics | definitions, notations |
| `relation` | Named relationships between objects | definitions |
| `class` | Families/categories of objects | definitions, remarks |

So your old `definition` node for "MDP" becomes:

```
Graph A node:
  name: "Markov Decision Process"
  semantic_type: structure
  rhetorical_origin: definition    ← your old type, preserved
  formal_spec: "(S, A, P, R, γ)"
  components: [state_space, action_space, transition_fn, reward_fn, discount]
```

**Graph A edges** are taxonomic and compositional:

- `IS_A` — "MDP `IS_A` stochastic_process"
- `HAS_COMPONENT` — "MDP `HAS_COMPONENT` transition_function"
- `INSTANCE_OF` — "grid_world `INSTANCE_OF` MDP"
- `DUAL_OF` — "value_function `DUAL_OF` policy"
- `GENERALIZES` / `SPECIALIZES` — "POMDP `GENERALIZES` MDP"
- `EQUIPPED_WITH` — "policy_space `EQUIPPED_WITH` KL_divergence"

Where do your old types feed in?

- **`definition`** → spawns Graph A nodes (the concept being defined)
- **`notation`** → becomes a `symbol` attribute on Graph A nodes
- **`example`** → spawns `INSTANCE_OF` edges pointing to the concept it exemplifies
- **`remark`** → becomes contextual metadata or `CLARIFIES` edges within Graph A

---

## Graph B — Reasoning / Claims Graph

These are nodes for **assertions about the concepts in Graph A**. Here your current rhetorical types actually do map more naturally:

| Type | Role in Graph B |
|---|---|
| `theorem` | Major proven claim |
| `lemma` | Supporting proven claim |
| `proposition` | Intermediate proven claim |
| `corollary` | Derived proven claim |
| `conjecture` | Unproven claim |
| `algorithm` | Procedural claim ("this procedure achieves X") |
| `exercise` | Challenge claim (usually with known answer) |

Each Graph B node has richer internal structure than you probably capture now:

```
Graph B node:
  name: "Policy Gradient Theorem"
  claim_type: theorem          ← your old type, now meaningful
  assumptions: ["differentiable policy", "finite MDP"]
  conclusion: "∇J(θ) = E[...]"
  proof_technique: "likelihood ratio trick"
  strength: "exact"            ← vs "approximate", "asymptotic"
```

**Graph B edges** are logical:

- `DEPENDS_ON` — "Theorem 4.1 `DEPENDS_ON` Lemma 3.3"
- `IMPLIES` — "Theorem 2 `IMPLIES` Corollary 2.1"
- `STRENGTHENS` / `WEAKENS` — one result tightens another's bound
- `CONTRADICTS` — important for conjectures
- `PROVES_VIA` — with a `technique` attribute
- `ENABLES` — "Lemma X `ENABLES` Algorithm Y" (the lemma justifies a step)

---

## The Coupling Layer (This Is the Critical Part)

The two graphs connect via **`ABOUT`** edges, and this is where the real power lives:

```
Graph B: "Policy Gradient Theorem"
  ──ABOUT──►  Graph A: "policy" (structure)
  ──ABOUT──►  Graph A: "expected_return" (quantity)
  ──ABOUT──►  Graph A: "gradient" (operator)

Graph B: "Nash Existence Theorem"
  ──ABOUT──►  Graph A: "Nash Equilibrium" (structure)
  ──ABOUT──►  Graph A: "finite game" (class)
```

This coupling is what makes traversal powerful. You can now ask:

- *"What claims exist about Nash Equilibrium?"* → follow `ABOUT` edges into Graph B
- *"What concepts does this theorem touch?"* → follow `ABOUT` edges into Graph A
- *"If I change the definition of X, what theorems break?"* → Graph A → `ABOUT` → Graph B → `DEPENDS_ON` chain

---

## The Extraction Prompt Shift

Your current prompt probably looks something like:

> *"Extract entities (definitions, theorems, lemmas...) from this text."*

You need **two-pass extraction**:

**Pass 1 — Concept extraction (Graph A):**
> "Identify the mathematical objects, structures, spaces, properties, and quantities **introduced or referenced** in this text. For each, state its semantic type and its relationship to other concepts."

**Pass 2 — Claim extraction (Graph B):**
> "Identify the theorems, lemmas, propositions, and algorithms stated in this text. For each, list: its assumptions, its conclusion, which concepts from the following list it is ABOUT, and which other claims it DEPENDS_ON."

Pass 2 receives the output of Pass 1 as context — so DeepSeek is grounding claims against already-extracted concepts rather than inventing freestanding entity nodes.

