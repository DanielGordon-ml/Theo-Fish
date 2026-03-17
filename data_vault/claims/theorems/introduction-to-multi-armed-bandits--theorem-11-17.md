---
slug: introduction-to-multi-armed-bandits--theorem-11-17
label: Theorem 11.17
claim_type: theorem
statement: 'Consider RepeatedHE with exploration probability ε > 0 and N_0 initial
  samples. Let N be the number of exploration rounds t > N_0. Then:

  (a) If ALG always chooses arm 2, RepeatedHE chooses arm 2 at least N times.

  (b) The expected reward of RepeatedHE is at least (1/ε) E[REW^{ALG}(N)].

  (c) Bayesian regret of RepeatedHE is BR(T) ≤ N_0 + (1/ε) E[BR^{ALG}(N)].'
proof: Part (a) is obvious. Part (c) trivially follows from part (b). The proof of
  part (b) invokes Wald's identity and the fact that the expected reward in "exploitation"
  is at least as large as in "exploration" for the same round.
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/repeatedhe]]'
- '[[concepts/bayesian-regret-r-t]]'
- '[[concepts/exploration-probability-epsilon]]'
- '[[concepts/bandit-algorithm]]'
- '[[concepts/initial-exploration-rounds-n0]]'
about_meta:
- target: '[[concepts/repeatedhe]]'
  role: primary
  aspect: ''
- target: '[[concepts/bayesian-regret-r-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/exploration-probability-epsilon]]'
  role: primary
  aspect: ''
- target: '[[concepts/bandit-algorithm]]'
  role: primary
  aspect: ''
- target: '[[concepts/initial-exploration-rounds-n0]]'
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

# Theorem 11.17

Consider RepeatedHE with exploration probability ε > 0 and N_0 initial samples. Let N be the number of exploration rounds t > N_0. Then:
(a) If ALG always chooses arm 2, RepeatedHE chooses arm 2 at least N times.
(b) The expected reward of RepeatedHE is at least (1/ε) E[REW^{ALG}(N)].
(c) Bayesian regret of RepeatedHE is BR(T) ≤ N_0 + (1/ε) E[BR^{ALG}(N)].


## Proof

Part (a) is obvious. Part (c) trivially follows from part (b). The proof of part (b) invokes Wald's identity and the fact that the expected reward in "exploitation" is at least as large as in "exploration" for the same round.
