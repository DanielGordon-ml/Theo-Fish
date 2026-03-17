---
slug: introduction-to-multi-armed-bandits--theorem-1-11
label: Theorem 1.11
claim_type: theorem
statement: Successive Elimination algorithm achieves regret $\operatornamewithlimits{\mathbb{E}}[R(T)]\leq
  O(\log{T})\left[\,\sum_{\text{arms $a$ with $\mu(a)<\mu(a^{*})$}}\frac{1}{\mu(a^{*})-\mu(a)}\,\right]$.
proof: From property (7), Δ(a) ≤ O(√(log(T)/n_T(a))). Rearranging the terms, n_T(a)
  ≤ O(log(T)/[Δ(a)]²). So, R(T;a) = Δ(a)·n_T(a) ≤ Δ(a)·O(log(T)/[Δ(a)]²) = O(log(T)/Δ(a)).
  Summing up over all suboptimal arms gives the result.
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/instance-dependent-constant]]'
- '[[concepts/time-horizon-t]]'
- '[[concepts/minimal-gap]]'
- '[[concepts/regret-r-t]]'
- '[[concepts/successive-elimination]]'
- '[[concepts/suboptimality-gap]]'
about_meta:
- target: '[[concepts/instance-dependent-constant]]'
  role: primary
  aspect: ''
- target: '[[concepts/time-horizon-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/minimal-gap]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret-r-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/successive-elimination]]'
  role: primary
  aspect: ''
- target: '[[concepts/suboptimality-gap]]'
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

# Theorem 1.11

Successive Elimination algorithm achieves regret $\operatornamewithlimits{\mathbb{E}}[R(T)]\leq O(\log{T})\left[\,\sum_{\text{arms $a$ with $\mu(a)<\mu(a^{*})$}}\frac{1}{\mu(a^{*})-\mu(a)}\,\right]$.


## Proof

From property (7), Δ(a) ≤ O(√(log(T)/n_T(a))). Rearranging the terms, n_T(a) ≤ O(log(T)/[Δ(a)]²). So, R(T;a) = Δ(a)·n_T(a) ≤ Δ(a)·O(log(T)/[Δ(a)]²) = O(log(T)/Δ(a)). Summing up over all suboptimal arms gives the result.
