---
slug: introduction-to-multi-armed-bandits--theorem-2-11
label: Theorem 2.11
claim_type: theorem
statement: Consider any algorithm which satisfies non-adaptive exploration. Fix time
  horizon T and the number of arms K<T. Then there exists a problem instance such
  that E[R(T)] ≥ Ω(T^{2/3} · K^{1/3}).
proof: The KL-divergence technique is "imported" via Corollary 2.9. Theorem 2.11 follows
  by taking C=K^{1/3} in Theorem 2.12; see Exercise 2.1 and hints therein.
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/time-horizon-t]]'
- '[[concepts/non-adaptive-exploration]]'
- '[[concepts/lower-bound-on-regret]]'
- '[[concepts/number-of-arms-k]]'
- '[[concepts/expected-regret-e-r-t]]'
- '[[concepts/regret-bound]]'
about_meta:
- target: '[[concepts/time-horizon-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/non-adaptive-exploration]]'
  role: primary
  aspect: ''
- target: '[[concepts/lower-bound-on-regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-arms-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/expected-regret-e-r-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret-bound]]'
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

# Theorem 2.11

Consider any algorithm which satisfies non-adaptive exploration. Fix time horizon T and the number of arms K<T. Then there exists a problem instance such that E[R(T)] ≥ Ω(T^{2/3} · K^{1/3}).


## Proof

The KL-divergence technique is "imported" via Corollary 2.9. Theorem 2.11 follows by taking C=K^{1/3} in Theorem 2.12; see Exercise 2.1 and hints therein.
