---
slug: introduction-to-multi-armed-bandits--algorithm-3-ucbbwk-optimism-under-uncertainty-with-knapsacks
label: 'Algorithm 3: UcbBwK (Optimism under Uncertainty with Knapsacks)'
claim_type: algorithm
statement: 'UcbBwK maintains a confidence region on the expected outcome matrix M_exp.
  In each round t, the algorithm picks distribution D which maximizes the UCB defined
  as UCB_t(D | B) = sup_{M ∈ ConfRegion_t} LP(D | B, M). An additional trick is to
  pretend that all budgets are scaled down by the same factor 1 - ε, for an appropriately
  chosen parameter ε. For a given distribution D, the supremum is obtained when upper
  confidence bounds are used for rewards and lower confidence bounds are used for
  resource consumption. Choosing a distribution with maximal UCB can be implemented
  by the linear program (150):


  maximize r^{UCB}(D)

  subject to D ∈ Δ_K, c_i^{LCB}(D) ≤ B''/T.'
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/ucb-function]]'
- '[[concepts/confidence-region]]'
- '[[concepts/ucbbwk-algorithm]]'
- '[[concepts/bandits-with-knapsacks]]'
- '[[concepts/optimism-under-uncertainty]]'
- '[[concepts/optimum-opt]]'
- '[[concepts/linear-program-for-bwk]]'
about_meta:
- target: '[[concepts/ucb-function]]'
  role: primary
  aspect: ''
- target: '[[concepts/confidence-region]]'
  role: primary
  aspect: ''
- target: '[[concepts/ucbbwk-algorithm]]'
  role: primary
  aspect: ''
- target: '[[concepts/bandits-with-knapsacks]]'
  role: primary
  aspect: ''
- target: '[[concepts/optimism-under-uncertainty]]'
  role: primary
  aspect: ''
- target: '[[concepts/optimum-opt]]'
  role: primary
  aspect: ''
- target: '[[concepts/linear-program-for-bwk]]'
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

# Algorithm 3: UcbBwK (Optimism under Uncertainty with Knapsacks)

UcbBwK maintains a confidence region on the expected outcome matrix M_exp. In each round t, the algorithm picks distribution D which maximizes the UCB defined as UCB_t(D | B) = sup_{M ∈ ConfRegion_t} LP(D | B, M). An additional trick is to pretend that all budgets are scaled down by the same factor 1 - ε, for an appropriately chosen parameter ε. For a given distribution D, the supremum is obtained when upper confidence bounds are used for rewards and lower confidence bounds are used for resource consumption. Choosing a distribution with maximal UCB can be implemented by the linear program (150):

maximize r^{UCB}(D)
subject to D ∈ Δ_K, c_i^{LCB}(D) ≤ B'/T.
