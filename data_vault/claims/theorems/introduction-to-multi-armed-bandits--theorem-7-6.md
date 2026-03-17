---
slug: introduction-to-multi-armed-bandits--theorem-7-6
label: Theorem 7.6
claim_type: theorem
statement: Consider combinatorial semi-bandits with deterministic oblivious adversary.
  Algorithm SemiBanditHedge achieved regret E[R(T)] ≤ O(d^{3/2} T^{3/4}).
proof: The algorithm and analysis from the previous section (online routing with semi-bandit
  feedback) does not rely on any special properties of u-v paths. Thus, they carry
  over word-by-word to combinatorial semi-bandits, replacing edges with atoms, and
  u-v paths with feasible subsets.
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/combinatorial-semi-bandits]]'
- '[[concepts/semi-bandit-feedback]]'
- '[[concepts/deterministic-oblivious-adversary]]'
- '[[concepts/regret-r-t]]'
- '[[concepts/hedge]]'
about_meta:
- target: '[[concepts/combinatorial-semi-bandits]]'
  role: primary
  aspect: ''
- target: '[[concepts/semi-bandit-feedback]]'
  role: primary
  aspect: ''
- target: '[[concepts/deterministic-oblivious-adversary]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret-r-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/hedge]]'
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

# Theorem 7.6

Consider combinatorial semi-bandits with deterministic oblivious adversary. Algorithm SemiBanditHedge achieved regret E[R(T)] ≤ O(d^{3/2} T^{3/4}).


## Proof

The algorithm and analysis from the previous section (online routing with semi-bandit feedback) does not rely on any special properties of u-v paths. Thus, they carry over word-by-word to combinatorial semi-bandits, replacing edges with atoms, and u-v paths with feasible subsets.
