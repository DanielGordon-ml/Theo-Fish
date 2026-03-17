---
slug: introduction-to-multi-armed-bandits--theorem-5-8-exercise-5-1
label: Theorem 5.8 (Exercise 5.1)
claim_type: theorem
statement: Consider binary prediction with expert advice, with a perfect expert. Any
  algorithm makes at least Ω(min(T, log K)) mistakes in the worst case.
proof: For simplicity, let K = 2^d and T ≥ d, for some integer d. Construct a distribution
  over problem instances such that each algorithm makes Ω(d) mistakes in expectation.
  Each expert e corresponds to a binary sequence e ∈ {0,1}^T, where e_t is the prediction
  for round t. Put experts in 1-1 correspondence with all possible binary sequences
  for the first d rounds. Pick the "perfect expert" u.a.r. among the experts. [Proof
  sketch from hint; full proof left as exercise.]
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/number-of-experts-k]]'
- '[[concepts/perfect-expert]]'
- '[[concepts/binary-prediction-with-expert-advice-problem]]'
- '[[concepts/time-horizon-t]]'
- '[[concepts/mistake]]'
about_meta:
- target: '[[concepts/number-of-experts-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/perfect-expert]]'
  role: primary
  aspect: ''
- target: '[[concepts/binary-prediction-with-expert-advice-problem]]'
  role: primary
  aspect: ''
- target: '[[concepts/time-horizon-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/mistake]]'
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

# Theorem 5.8 (Exercise 5.1)

Consider binary prediction with expert advice, with a perfect expert. Any algorithm makes at least Ω(min(T, log K)) mistakes in the worst case.


## Proof

For simplicity, let K = 2^d and T ≥ d, for some integer d. Construct a distribution over problem instances such that each algorithm makes Ω(d) mistakes in expectation. Each expert e corresponds to a binary sequence e ∈ {0,1}^T, where e_t is the prediction for round t. Put experts in 1-1 correspondence with all possible binary sequences for the first d rounds. Pick the "perfect expert" u.a.r. among the experts. [Proof sketch from hint; full proof left as exercise.]
