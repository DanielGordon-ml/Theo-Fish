---
slug: introduction-to-multi-armed-bandits--theorem-2-12
label: Theorem 2.12
claim_type: theorem
statement: 'In the setup of Theorem 2.11, suppose E[R(T)] ≤ C · T^γ for all problem
  instances, for some numbers γ ∈ [2/3, 1) and C > 0. Then for any problem instance
  a random permutation of arms yields E[R(T)] ≥ Ω(C^{-2} · T^λ · Σ_a Δ(a)), where
  λ = 2(1−γ). In particular, if an algorithm achieves regret E[R(T)] ≤ Õ(T^{2/3} ·
  K^{1/3}) over all problem instances, like Explore-first and Epsilon-greedy, this
  algorithm incurs a similar regret for *every* problem instance, if the arms therein
  are randomly permuted: E[R(T)] ≥ Ω̃(Δ · T^{2/3} · K^{1/3}), where Δ is the minimal
  gap. This follows by taking C = Õ(K^{1/3}) in the theorem.'
proof: The KL-divergence technique is "imported" via Corollary 2.9. Theorem 2.12 is
  fairly straightforward given this corollary.
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/minimal-gap-d]]'
- '[[concepts/non-adaptive-exploration]]'
- '[[concepts/lower-bound-on-regret]]'
- '[[concepts/number-of-arms-k]]'
- '[[concepts/random-permutation-of-arms]]'
- '[[concepts/satisfies-polynomial-regret-bound]]'
- '[[concepts/epsilon-greedy-algorithm]]'
- '[[concepts/explore-first-algorithm]]'
- '[[concepts/time-horizon-t]]'
- '[[concepts/gap-per-arm-d-a]]'
- '[[concepts/expected-regret-e-r-t]]'
about_meta:
- target: '[[concepts/minimal-gap-d]]'
  role: primary
  aspect: ''
- target: '[[concepts/non-adaptive-exploration]]'
  role: primary
  aspect: ''
- target: '[[concepts/lower-bound-on-regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-arms-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/random-permutation-of-arms]]'
  role: primary
  aspect: ''
- target: '[[concepts/satisfies-polynomial-regret-bound]]'
  role: primary
  aspect: ''
- target: '[[concepts/epsilon-greedy-algorithm]]'
  role: primary
  aspect: ''
- target: '[[concepts/explore-first-algorithm]]'
  role: primary
  aspect: ''
- target: '[[concepts/time-horizon-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/gap-per-arm-d-a]]'
  role: primary
  aspect: ''
- target: '[[concepts/expected-regret-e-r-t]]'
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

# Theorem 2.12

In the setup of Theorem 2.11, suppose E[R(T)] ≤ C · T^γ for all problem instances, for some numbers γ ∈ [2/3, 1) and C > 0. Then for any problem instance a random permutation of arms yields E[R(T)] ≥ Ω(C^{-2} · T^λ · Σ_a Δ(a)), where λ = 2(1−γ). In particular, if an algorithm achieves regret E[R(T)] ≤ Õ(T^{2/3} · K^{1/3}) over all problem instances, like Explore-first and Epsilon-greedy, this algorithm incurs a similar regret for *every* problem instance, if the arms therein are randomly permuted: E[R(T)] ≥ Ω̃(Δ · T^{2/3} · K^{1/3}), where Δ is the minimal gap. This follows by taking C = Õ(K^{1/3}) in the theorem.


## Proof

The KL-divergence technique is "imported" via Corollary 2.9. Theorem 2.12 is fairly straightforward given this corollary.
