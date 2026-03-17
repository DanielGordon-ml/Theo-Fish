---
slug: introduction-to-multi-armed-bandits--theorem-2-4
label: Theorem 2.4
claim_type: theorem
statement: 'KL-divergence satisfies the following properties:

  (a) Gibbs'' Inequality: KL(p,q) ≥ 0 for any two distributions p,q, with equality
  if and only if p = q.

  (b) Chain rule for product distributions: Let the sample space be a product Ω =
  Ω₁ × Ω₁ × … × Ωₙ. Let p and q be two distributions on Ω such that p = p₁ × p₂ ×
  … × pₙ and q = q₁ × q₂ × … × qₙ, where pⱼ, qⱼ are distributions on Ωⱼ, for each
  j ∈ [n]. Then KL(p,q) = Σⱼ₌₁ⁿ KL(pⱼ,qⱼ).

  (c) Pinsker''s inequality: for any event A ⊂ Ω we have 2(p(A) − q(A))² ≤ KL(p,q).

  (d) Random coins: KL(RC_ε, RC_0) ≤ 2ε² and KL(RC_0, RC_ε) ≤ ε² for all ε ∈ (0, 1/2).'
proof: ''
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/kl-divergence]]'
- '[[concepts/random-coin-rc-epsilon]]'
- '[[concepts/product-probability-distribution]]'
- '[[concepts/probability-distribution]]'
about_meta:
- target: '[[concepts/kl-divergence]]'
  role: primary
  aspect: ''
- target: '[[concepts/random-coin-rc-epsilon]]'
  role: primary
  aspect: ''
- target: '[[concepts/product-probability-distribution]]'
  role: primary
  aspect: ''
- target: '[[concepts/probability-distribution]]'
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

# Theorem 2.4

KL-divergence satisfies the following properties:
(a) Gibbs' Inequality: KL(p,q) ≥ 0 for any two distributions p,q, with equality if and only if p = q.
(b) Chain rule for product distributions: Let the sample space be a product Ω = Ω₁ × Ω₁ × … × Ωₙ. Let p and q be two distributions on Ω such that p = p₁ × p₂ × … × pₙ and q = q₁ × q₂ × … × qₙ, where pⱼ, qⱼ are distributions on Ωⱼ, for each j ∈ [n]. Then KL(p,q) = Σⱼ₌₁ⁿ KL(pⱼ,qⱼ).
(c) Pinsker's inequality: for any event A ⊂ Ω we have 2(p(A) − q(A))² ≤ KL(p,q).
(d) Random coins: KL(RC_ε, RC_0) ≤ 2ε² and KL(RC_0, RC_ε) ≤ ε² for all ε ∈ (0, 1/2).
