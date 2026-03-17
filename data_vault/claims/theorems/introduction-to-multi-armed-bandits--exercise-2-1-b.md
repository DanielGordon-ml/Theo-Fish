---
slug: introduction-to-multi-armed-bandits--exercise-2-1-b
label: Exercise 2.1(b)
claim_type: theorem
statement: Consider an algorithm which satisfies non-adaptive exploration. Let N be
  the number of exploration rounds. Then for each problem instance, randomly permuting
  the arms yields E[R(T)] ≥ E[N] · (1/K) Σ_a Δ(a).
proof: ''
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/gap-per-arm-d-a]]'
- '[[concepts/non-adaptive-exploration]]'
- '[[concepts/random-permutation-of-arms]]'
- '[[concepts/number-of-arms-k]]'
- '[[concepts/parameter-n]]'
- '[[concepts/expected-regret-e-r-t]]'
about_meta:
- target: '[[concepts/gap-per-arm-d-a]]'
  role: primary
  aspect: ''
- target: '[[concepts/non-adaptive-exploration]]'
  role: primary
  aspect: ''
- target: '[[concepts/random-permutation-of-arms]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-arms-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/parameter-n]]'
  role: primary
  aspect: ''
- target: '[[concepts/expected-regret-e-r-t]]'
  role: primary
  aspect: ''
depends_on: []
depends_on_meta: []
sourced_from:
- '[[sources/1904.07272|Introduction to Multi-Armed Bandits]]'
sourced_from_meta:
- target: '[[sources/1904.07272|Introduction to Multi-Armed Bandits]]'
  section: ''
  page: ''
  confidence: 0.0
---

# Exercise 2.1(b)

Consider an algorithm which satisfies non-adaptive exploration. Let N be the number of exploration rounds. Then for each problem instance, randomly permuting the arms yields E[R(T)] ≥ E[N] · (1/K) Σ_a Δ(a).
