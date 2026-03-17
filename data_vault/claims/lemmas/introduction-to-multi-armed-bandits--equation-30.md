---
slug: introduction-to-multi-armed-bandits--equation-30
label: Equation (30)
claim_type: lemma
statement: Assuming T ≤ cK/ε² with small enough constant c, |P*_0(A) - P*_j(A)| ≤
  ε√m < 1/8 for all events A ⊂ Ω*.
proof: By Pinsker's inequality, 2(P*_0(A) - P*_j(A))² ≤ KL(P*_0, P*_j). By the chain
  rule, KL(P*_0, P*_j) = Σ_{arms a} Σ_t KL(P_0^{a,t}, P_j^{a,t}). For arms a≠j the
  distributions are identical so KL = 0. For arm j, summing over m samples gives m
  · 2ε². Thus 2(P*_0(A) - P*_j(A))² ≤ 2mε², giving |P*_0(A) - P*_j(A)| ≤ ε√m. Since
  m ≤ 24T/K ≤ 24c/ε², choosing c small enough gives ε√m < 1/8.
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/time-horizon-t]]'
- '[[concepts/reduced-sample-space-omega]]'
- '[[concepts/kl-divergence]]'
- '[[concepts/parameter-epsilon]]'
- '[[concepts/number-of-arms-k]]'
about_meta:
- target: '[[concepts/time-horizon-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/reduced-sample-space-omega]]'
  role: primary
  aspect: ''
- target: '[[concepts/kl-divergence]]'
  role: primary
  aspect: ''
- target: '[[concepts/parameter-epsilon]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-arms-k]]'
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

# Equation (30)

Assuming T ≤ cK/ε² with small enough constant c, |P*_0(A) - P*_j(A)| ≤ ε√m < 1/8 for all events A ⊂ Ω*.


## Proof

By Pinsker's inequality, 2(P*_0(A) - P*_j(A))² ≤ KL(P*_0, P*_j). By the chain rule, KL(P*_0, P*_j) = Σ_{arms a} Σ_t KL(P_0^{a,t}, P_j^{a,t}). For arms a≠j the distributions are identical so KL = 0. For arm j, summing over m samples gives m · 2ε². Thus 2(P*_0(A) - P*_j(A))² ≤ 2mε², giving |P*_0(A) - P*_j(A)| ≤ ε√m. Since m ≤ 24T/K ≤ 24c/ε², choosing c small enough gives ε√m < 1/8.
