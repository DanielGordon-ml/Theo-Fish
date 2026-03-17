---
slug: introduction-to-multi-armed-bandits--exercise-1-4-c
label: Exercise 1.4(c)
claim_type: proposition
statement: 'Prove that alternating the arms (and predicting the best one) achieves,
  for any fixed γ < 1: E[Δ(y_T)] ≤ e^{-Ω(T^γ)} if T > T_{μ,γ}, where T_{μ,γ} depends
  only on the mean rewards μ(a): a ∈ A and the γ.'
proof: ''
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/confidence-radius]]'
- '[[concepts/hoeffding-inequality]]'
- '[[concepts/pure-exploration-bandits]]'
- '[[concepts/simple-regret]]'
- '[[concepts/best-arm-identification]]'
about_meta:
- target: '[[concepts/confidence-radius]]'
  role: primary
  aspect: ''
- target: '[[concepts/hoeffding-inequality]]'
  role: primary
  aspect: ''
- target: '[[concepts/pure-exploration-bandits]]'
  role: primary
  aspect: ''
- target: '[[concepts/simple-regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/best-arm-identification]]'
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

# Exercise 1.4(c)

Prove that alternating the arms (and predicting the best one) achieves, for any fixed γ < 1: E[Δ(y_T)] ≤ e^{-Ω(T^γ)} if T > T_{μ,γ}, where T_{μ,γ} depends only on the mean rewards μ(a): a ∈ A and the γ.
