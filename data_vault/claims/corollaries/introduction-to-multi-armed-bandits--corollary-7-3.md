---
slug: introduction-to-multi-armed-bandits--corollary-7-3
label: Corollary 7.3
claim_type: corollary
statement: Consider online routing with full feedback. Algorithm Hedge with parameter
  ε = 1/√(dT) achieves regret E[R(T)] ≤ O(d√(dT)).
proof: Applying Theorem 5.16 with a trivial upper bound c_t(·) ≤ d on action costs,
  and the trivial upper bound K ≤ 2^d on the number of paths, we obtain regret E[R(T)]
  ≤ O(d√(dT)).
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/hedge]]'
- '[[concepts/online-routing]]'
- '[[concepts/regret]]'
- '[[concepts/full-feedback]]'
- '[[concepts/online-linear-optimization]]'
about_meta:
- target: '[[concepts/hedge]]'
  role: primary
  aspect: ''
- target: '[[concepts/online-routing]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/full-feedback]]'
  role: primary
  aspect: ''
- target: '[[concepts/online-linear-optimization]]'
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

# Corollary 7.3

Consider online routing with full feedback. Algorithm Hedge with parameter ε = 1/√(dT) achieves regret E[R(T)] ≤ O(d√(dT)).


## Proof

Applying Theorem 5.16 with a trivial upper bound c_t(·) ≤ d on action costs, and the trivial upper bound K ≤ 2^d on the number of paths, we obtain regret E[R(T)] ≤ O(d√(dT)).
