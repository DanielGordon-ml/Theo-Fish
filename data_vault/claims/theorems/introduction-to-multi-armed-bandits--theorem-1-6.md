---
slug: introduction-to-multi-armed-bandits--theorem-1-6
label: Theorem 1.6
claim_type: theorem
statement: Epsilon-greedy algorithm with exploration probabilities $\epsilon_{t}=t^{-1/3}\cdot(K\log
  t)^{1/3}$ achieves regret bound $\operatornamewithlimits{\mathbb{E}}[R(t)]\leq t^{2/3}\cdot
  O(K\log t)^{1/3}$ for each round $t$.
proof: ''
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/number-of-arms-k]]'
- '[[concepts/exploration-probability-epsilon-t]]'
- '[[concepts/stochastic-bandits-problem]]'
- '[[concepts/epsilon-greedy-algorithm]]'
- '[[concepts/non-adaptive-exploration]]'
- '[[concepts/expected-regret-e-r-t]]'
- '[[concepts/bounded-rewards]]'
about_meta:
- target: '[[concepts/number-of-arms-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/exploration-probability-epsilon-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/stochastic-bandits-problem]]'
  role: primary
  aspect: ''
- target: '[[concepts/epsilon-greedy-algorithm]]'
  role: primary
  aspect: ''
- target: '[[concepts/non-adaptive-exploration]]'
  role: primary
  aspect: ''
- target: '[[concepts/expected-regret-e-r-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/bounded-rewards]]'
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

# Theorem 1.6

Epsilon-greedy algorithm with exploration probabilities $\epsilon_{t}=t^{-1/3}\cdot(K\log t)^{1/3}$ achieves regret bound $\operatornamewithlimits{\mathbb{E}}[R(t)]\leq t^{2/3}\cdot O(K\log t)^{1/3}$ for each round $t$.
