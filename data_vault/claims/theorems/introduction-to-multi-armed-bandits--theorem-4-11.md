---
slug: introduction-to-multi-armed-bandits--theorem-4-11
label: Theorem 4.11
claim_type: theorem
statement: 'Consider Lipschitz bandits on a metric space (X, D), with time horizon
  T. Let ALG be any algorithm satisfying (52). Fix any c > 0, and let d = COV_c(X)
  be the covering dimension. Then there exists a subset S ⊂ X such that running ALG
  on the set of arms S yields regret


  𝔼[R(T)] ≤ (1 + c_{ALG}) · T^{(d+1)/(d+2)} · (c log T)^{1/(d+2)}.


  Specifically, S can be any ε-mesh of size |S| ≤ O(c/ε^d), where ε = (T / log T)^{-1/(d+2)};
  such S exists.'
proof: We take an ε-mesh S of size |S| = N_ε(X) ≤ O(c/ε^d). Taking ε = (T / log T)^{-1/(d+2)},
  like in Example 4.7, and plugging this into Eq. (53), we obtain the result.
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/expected-regret-r-t]]'
- '[[concepts/lipschitz-bandits-problem]]'
- '[[concepts/mesh]]'
- '[[concepts/covering-number]]'
- '[[concepts/covering-dimension]]'
- '[[concepts/uniform-discretization-for-bandits]]'
about_meta:
- target: '[[concepts/expected-regret-r-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/lipschitz-bandits-problem]]'
  role: primary
  aspect: ''
- target: '[[concepts/mesh]]'
  role: primary
  aspect: ''
- target: '[[concepts/covering-number]]'
  role: primary
  aspect: ''
- target: '[[concepts/covering-dimension]]'
  role: primary
  aspect: ''
- target: '[[concepts/uniform-discretization-for-bandits]]'
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

# Theorem 4.11

Consider Lipschitz bandits on a metric space (X, D), with time horizon T. Let ALG be any algorithm satisfying (52). Fix any c > 0, and let d = COV_c(X) be the covering dimension. Then there exists a subset S ⊂ X such that running ALG on the set of arms S yields regret

𝔼[R(T)] ≤ (1 + c_{ALG}) · T^{(d+1)/(d+2)} · (c log T)^{1/(d+2)}.

Specifically, S can be any ε-mesh of size |S| ≤ O(c/ε^d), where ε = (T / log T)^{-1/(d+2)}; such S exists.


## Proof

We take an ε-mesh S of size |S| = N_ε(X) ≤ O(c/ε^d). Taking ε = (T / log T)^{-1/(d+2)}, like in Example 4.7, and plugging this into Eq. (53), we obtain the result.
