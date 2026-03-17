---
slug: introduction-to-multi-armed-bandits--example-4-7
label: Example 4.7
claim_type: proposition
statement: 'Suppose the metric space is X = [0,1]^d, d ∈ ℕ under the ℓ_p metric, p
  ≥ 1. Consider a subset S ⊂ X that consists of all points whose coordinates are multiples
  of a given ε > 0. Then |S| ≤ ⌈1/ε⌉^d points, and its discretization error is DE(S)
  ≤ c_{p,d} · ε, where c_{p,d} is a constant that depends only on p and d; e.g., c_{p,d}
  = d for p = 1. Plugging this into (53) and taking ε = (T / log T)^{-1/(d+2)}, we
  obtain


  𝔼[R(T)] ≤ (1 + c_{ALG}) · T^{(d+1)/(d+2)} · (c log T)^{1/(d+2)}.'
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/lipschitz-bandits-problem]]'
- '[[concepts/discretization-error]]'
- '[[concepts/expected-regret-r-t]]'
- '[[concepts/uniform-discretization-for-bandits]]'
about_meta:
- target: '[[concepts/lipschitz-bandits-problem]]'
  role: primary
  aspect: ''
- target: '[[concepts/discretization-error]]'
  role: primary
  aspect: ''
- target: '[[concepts/expected-regret-r-t]]'
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

# Example 4.7

Suppose the metric space is X = [0,1]^d, d ∈ ℕ under the ℓ_p metric, p ≥ 1. Consider a subset S ⊂ X that consists of all points whose coordinates are multiples of a given ε > 0. Then |S| ≤ ⌈1/ε⌉^d points, and its discretization error is DE(S) ≤ c_{p,d} · ε, where c_{p,d} is a constant that depends only on p and d; e.g., c_{p,d} = d for p = 1. Plugging this into (53) and taking ε = (T / log T)^{-1/(d+2)}, we obtain

𝔼[R(T)] ≤ (1 + c_{ALG}) · T^{(d+1)/(d+2)} · (c log T)^{1/(d+2)}.
