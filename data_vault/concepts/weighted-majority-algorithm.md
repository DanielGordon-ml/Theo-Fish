---
slug: weighted-majority-algorithm
name: weighted majority algorithm
semantic_type: operator
canonical_definition: ''
formal_spec: 'Initialize w_1(a)=1 for all experts a. In each round t, predict the
  action with maximum total weight among experts predicting that action. Update weights:
  for experts that predicted incorrectly, w_{t+1}(a) = (1-ε) w_t(a); for others, w_{t+1}(a)
  = w_t(a).'
aliases: []
status: canonical
human_notes: ''
generalizes: []
generalizes_meta: []
has_component: []
has_component_meta: []
depends_on: []
depends_on_meta: []
related_to: []
related_to_meta: []
equivalent_to: []
equivalent_to_meta: []
instantiates: []
instantiates_meta: []
sourced_from:
- '[[sources/1904.07272|Introduction to Multi-Armed Bandits]]'
sourced_from_meta:
- target: '[[sources/1904.07272|Introduction to Multi-Armed Bandits]]'
  section: ''
  page: ''
  confidence: 0.0
---

# weighted majority algorithm




## Provenance

| Source | Section | Formulation | Confidence |
|--------|---------|-------------|------------|
| [[sources/1904.07272]] |  | "" | 0.0 |
