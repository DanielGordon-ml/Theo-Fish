---
slug: introduction-to-multi-armed-bandits--theorem-8-4
label: Theorem 8.4
claim_type: theorem
statement: Consider the Lipschitz contextual bandits problem with contexts in $[0,1]$.
  The uniform discretization algorithm (102) yields regret $\operatornamewithlimits{\mathbb{E}}[R(T)]=O(T^{2/3}(LK\ln
  T)^{1/3})$.
proof: The overall regret decomposes as R(T) = R_S(T) + DE(S). From Lemma 8.1, E[R_S(T)]
  = O(√(KT|S| ln T)). From Claim 8.3, E[DE(S)] ≤ εLT. Since |S| = 1/ε + 1 ≈ 1/ε, we
  have E[R(T)] ≤ εLT + O(√((1/ε)KT ln T)). Optimizing the choice of ε yields E[R(T)]
  = O(T^{2/3}(LK ln T)^{1/3}).
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/lipschitz-condition]]'
- '[[concepts/time-horizon]]'
- '[[concepts/number-of-arms]]'
- '[[concepts/lipschitz-constant]]'
- '[[concepts/expected-regret]]'
- '[[concepts/lipschitz-contextual-bandits-problem]]'
- '[[concepts/epsilon-mesh]]'
- '[[concepts/regret-bound]]'
about_meta:
- target: '[[concepts/lipschitz-condition]]'
  role: primary
  aspect: ''
- target: '[[concepts/time-horizon]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-arms]]'
  role: primary
  aspect: ''
- target: '[[concepts/lipschitz-constant]]'
  role: primary
  aspect: ''
- target: '[[concepts/expected-regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/lipschitz-contextual-bandits-problem]]'
  role: primary
  aspect: ''
- target: '[[concepts/epsilon-mesh]]'
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

# Theorem 8.4

Consider the Lipschitz contextual bandits problem with contexts in $[0,1]$. The uniform discretization algorithm (102) yields regret $\operatornamewithlimits{\mathbb{E}}[R(T)]=O(T^{2/3}(LK\ln T)^{1/3})$.


## Proof

The overall regret decomposes as R(T) = R_S(T) + DE(S). From Lemma 8.1, E[R_S(T)] = O(√(KT|S| ln T)). From Claim 8.3, E[DE(S)] ≤ εLT. Since |S| = 1/ε + 1 ≈ 1/ε, we have E[R(T)] ≤ εLT + O(√((1/ε)KT ln T)). Optimizing the choice of ε yields E[R(T)] = O(T^{2/3}(LK ln T)^{1/3}).
