---
slug: introduction-to-multi-armed-bandits--algorithm-2-linucb
label: Algorithm 2 LinUCB
claim_type: algorithm
statement: 'LinUCB: UCB-based algorithm for linear contextual bandits. In each round
  t, construct a confidence region C_t ⊂ Θ such that θ ∈ C_t with high probability.
  Then use C_t to construct an UCB on the mean reward of each arm given context x_t,
  and play an arm with the highest UCB.'
proof: ''
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/linear-contextual-bandit-problem]]'
- '[[concepts/linucb-algorithm]]'
- '[[concepts/upper-confidence-bound]]'
- '[[concepts/regret-r-t]]'
- '[[concepts/dimensionality-d]]'
- '[[concepts/minimal-gap-d]]'
- '[[concepts/confidence-region-c-t]]'
about_meta:
- target: '[[concepts/linear-contextual-bandit-problem]]'
  role: primary
  aspect: ''
- target: '[[concepts/linucb-algorithm]]'
  role: primary
  aspect: ''
- target: '[[concepts/upper-confidence-bound]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret-r-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/dimensionality-d]]'
  role: primary
  aspect: ''
- target: '[[concepts/minimal-gap-d]]'
  role: primary
  aspect: ''
- target: '[[concepts/confidence-region-c-t]]'
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

# Algorithm 2 LinUCB

LinUCB: UCB-based algorithm for linear contextual bandits. In each round t, construct a confidence region C_t ⊂ Θ such that θ ∈ C_t with high probability. Then use C_t to construct an UCB on the mean reward of each arm given context x_t, and play an arm with the highest UCB.
