---
slug: introduction-to-multi-armed-bandits--exercise-1-4-b
label: Exercise 1.4(b)
claim_type: proposition
statement: 'Consider Successive Elimination with y_T = a_T. Prove that (with a slightly
  modified definition of the confidence radius) this algorithm can achieve E[Δ(y_T)]
  ≤ T^{-γ} if T > T_{μ,γ}, where T_{μ,γ} depends only on the mean rewards μ(a): a
  ∈ A and the γ. This holds for an arbitrarily large constant γ, with only a multiplicative-constant
  increase in regret.'
proof: ''
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/best-arm-identification]]'
- '[[concepts/pure-exploration-bandits]]'
- '[[concepts/simple-regret]]'
- '[[concepts/successive-elimination-algorithm]]'
- '[[concepts/confidence-radius]]'
about_meta:
- target: '[[concepts/best-arm-identification]]'
  role: primary
  aspect: ''
- target: '[[concepts/pure-exploration-bandits]]'
  role: primary
  aspect: ''
- target: '[[concepts/simple-regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/successive-elimination-algorithm]]'
  role: primary
  aspect: ''
- target: '[[concepts/confidence-radius]]'
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

# Exercise 1.4(b)

Consider Successive Elimination with y_T = a_T. Prove that (with a slightly modified definition of the confidence radius) this algorithm can achieve E[Δ(y_T)] ≤ T^{-γ} if T > T_{μ,γ}, where T_{μ,γ} depends only on the mean rewards μ(a): a ∈ A and the γ. This holds for an arbitrarily large constant γ, with only a multiplicative-constant increase in regret.
