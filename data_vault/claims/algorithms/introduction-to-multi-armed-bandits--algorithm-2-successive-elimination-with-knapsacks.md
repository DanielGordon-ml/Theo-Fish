---
slug: introduction-to-multi-armed-bandits--algorithm-2-successive-elimination-with-knapsacks
label: 'Algorithm 2: Successive Elimination with Knapsacks'
claim_type: algorithm
statement: Successive Elimination with Knapsacks maintains a confidence region on
  the expected outcome matrix M_exp. A distribution D over arms is called potentially
  optimal if it optimizes LP(D | B, M) for some M ∈ ConfRegion_t. In each round, an
  arm b_t is chosen uniformly at random, and then a potentially optimal distribution
  D that maximizes D(b_t) is selected and played. The algorithm achieves the regret
  bound (148) with an extra multiplicative term of √d.
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/confidence-region]]'
- '[[concepts/potentially-optimal-distribution]]'
- '[[concepts/bandits-with-knapsacks]]'
- '[[concepts/successive-elimination-with-knapsacks-algorithm]]'
- '[[concepts/optimum-opt]]'
about_meta:
- target: '[[concepts/confidence-region]]'
  role: primary
  aspect: ''
- target: '[[concepts/potentially-optimal-distribution]]'
  role: primary
  aspect: ''
- target: '[[concepts/bandits-with-knapsacks]]'
  role: primary
  aspect: ''
- target: '[[concepts/successive-elimination-with-knapsacks-algorithm]]'
  role: primary
  aspect: ''
- target: '[[concepts/optimum-opt]]'
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

# Algorithm 2: Successive Elimination with Knapsacks

Successive Elimination with Knapsacks maintains a confidence region on the expected outcome matrix M_exp. A distribution D over arms is called potentially optimal if it optimizes LP(D | B, M) for some M ∈ ConfRegion_t. In each round, an arm b_t is chosen uniformly at random, and then a potentially optimal distribution D that maximizes D(b_t) is selected and played. The algorithm achieves the regret bound (148) with an extra multiplicative term of √d.
