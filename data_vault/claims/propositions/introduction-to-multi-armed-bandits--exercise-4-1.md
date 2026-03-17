---
slug: introduction-to-multi-armed-bandits--exercise-4-1
label: Exercise 4.1
claim_type: proposition
statement: 'The construction in Remark 4.6 attains the infimum in (58) up to a constant
  factor. Specifically, let $\epsilon(S)=\inf\{\epsilon>0: S \text{ is an } \epsilon\text{-mesh}\}$
  for $S\subset X$, and $f(S)=c_{\mathtt{ALG}}\cdot\sqrt{|S|\,T\log T}+T\cdot\epsilon(S)$.
  Let $\mathcal{N}_i$ be the $\epsilon$-mesh computed in Remark 4.6 for $\epsilon=2^{-i}$,
  and suppose the construction stops at $i=i^*$. Then $f(\mathcal{N}_{i^*})\leq 16\,\inf_{S\subset
  X}f(S)$.'
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/mesh]]'
- '[[concepts/discretization-error]]'
- '[[concepts/covering-number]]'
- '[[concepts/f-s]]'
- '[[concepts/net]]'
about_meta:
- target: '[[concepts/mesh]]'
  role: primary
  aspect: ''
- target: '[[concepts/discretization-error]]'
  role: primary
  aspect: ''
- target: '[[concepts/covering-number]]'
  role: primary
  aspect: ''
- target: '[[concepts/f-s]]'
  role: primary
  aspect: ''
- target: '[[concepts/net]]'
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

# Exercise 4.1

The construction in Remark 4.6 attains the infimum in (58) up to a constant factor. Specifically, let $\epsilon(S)=\inf\{\epsilon>0: S \text{ is an } \epsilon\text{-mesh}\}$ for $S\subset X$, and $f(S)=c_{\mathtt{ALG}}\cdot\sqrt{|S|\,T\log T}+T\cdot\epsilon(S)$. Let $\mathcal{N}_i$ be the $\epsilon$-mesh computed in Remark 4.6 for $\epsilon=2^{-i}$, and suppose the construction stops at $i=i^*$. Then $f(\mathcal{N}_{i^*})\leq 16\,\inf_{S\subset X}f(S)$.
