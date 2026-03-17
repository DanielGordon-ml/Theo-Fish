---
slug: introduction-to-multi-armed-bandits--theorem-11-17-b
label: Theorem 11.17(b)
claim_type: theorem
statement: 'Performance of RepeatedHE: part (b) establishes the Bayesian regret bound
  for the RepeatedHE algorithm.'
proof: The proof relies on Wald's identity. Let t_i be the i-th round t > N_0 in which
  the "exploration branch" has been chosen. Let u_i be the expected reward of ALG
  in the i-th round of its execution. Let X_i be the expected reward in the time interval
  [t_i, t_{i+1}). Use Wald's identity to prove that E[X_i] = (1/ε) · u_i. Use Wald's
  identity again (in a version for non-IID random variables) to prove that E[∑_{i=1}^{N}
  X_i] = (1/ε) · E[∑_{i=1}^{N} u_i]. Observe that the right-hand side is simply (1/ε)
  · E[U(N)].
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/exploration-probability-epsilon]]'
- '[[concepts/x-i]]'
- '[[concepts/t-i]]'
- '[[concepts/initial-exploration-rounds-n0]]'
- '[[concepts/u-n]]'
- '[[concepts/repeatedhe]]'
- '[[concepts/bayesian-regret]]'
- '[[concepts/n-0]]'
- '[[concepts/u-i]]'
about_meta:
- target: '[[concepts/exploration-probability-epsilon]]'
  role: primary
  aspect: ''
- target: '[[concepts/x-i]]'
  role: primary
  aspect: ''
- target: '[[concepts/t-i]]'
  role: primary
  aspect: ''
- target: '[[concepts/initial-exploration-rounds-n0]]'
  role: primary
  aspect: ''
- target: '[[concepts/u-n]]'
  role: primary
  aspect: ''
- target: '[[concepts/repeatedhe]]'
  role: primary
  aspect: ''
- target: '[[concepts/bayesian-regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/n-0]]'
  role: primary
  aspect: ''
- target: '[[concepts/u-i]]'
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

# Theorem 11.17(b)

Performance of RepeatedHE: part (b) establishes the Bayesian regret bound for the RepeatedHE algorithm.


## Proof

The proof relies on Wald's identity. Let t_i be the i-th round t > N_0 in which the "exploration branch" has been chosen. Let u_i be the expected reward of ALG in the i-th round of its execution. Let X_i be the expected reward in the time interval [t_i, t_{i+1}). Use Wald's identity to prove that E[X_i] = (1/ε) · u_i. Use Wald's identity again (in a version for non-IID random variables) to prove that E[∑_{i=1}^{N} X_i] = (1/ε) · E[∑_{i=1}^{N} u_i]. Observe that the right-hand side is simply (1/ε) · E[U(N)].
