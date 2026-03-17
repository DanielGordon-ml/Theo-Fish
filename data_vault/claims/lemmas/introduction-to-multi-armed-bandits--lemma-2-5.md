---
slug: introduction-to-multi-armed-bandits--lemma-2-5
label: Lemma 2.5
claim_type: lemma
statement: Consider sample space Ω = {0,1}ⁿ and two distributions on Ω, p = RC_ε^n
  and q = RC_0^n, for some ε > 0. Then |p(A) − q(A)| ≤ ε√n for any event A ⊂ Ω.
proof: 'By Pinsker''s inequality: 2(p(A) − q(A))² ≤ KL(p,q). By the Chain Rule: KL(p,q)
  = Σⱼ₌₁ⁿ KL(pⱼ,qⱼ). By definition of pⱼ, qⱼ: = n · KL(RC_ε, RC_0). By part (d) of
  Theorem 2.4: ≤ 2nε². It follows that |p(A) − q(A)| ≤ ε√n.'
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/kl-divergence]]'
- '[[concepts/product-probability-distribution]]'
- '[[concepts/sample-space-omega]]'
- '[[concepts/random-coin-rc-epsilon]]'
about_meta:
- target: '[[concepts/kl-divergence]]'
  role: primary
  aspect: ''
- target: '[[concepts/product-probability-distribution]]'
  role: primary
  aspect: ''
- target: '[[concepts/sample-space-omega]]'
  role: primary
  aspect: ''
- target: '[[concepts/random-coin-rc-epsilon]]'
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

# Lemma 2.5

Consider sample space Ω = {0,1}ⁿ and two distributions on Ω, p = RC_ε^n and q = RC_0^n, for some ε > 0. Then |p(A) − q(A)| ≤ ε√n for any event A ⊂ Ω.


## Proof

By Pinsker's inequality: 2(p(A) − q(A))² ≤ KL(p,q). By the Chain Rule: KL(p,q) = Σⱼ₌₁ⁿ KL(pⱼ,qⱼ). By definition of pⱼ, qⱼ: = n · KL(RC_ε, RC_0). By part (d) of Theorem 2.4: ≤ 2nε². It follows that |p(A) − q(A)| ≤ ε√n.
