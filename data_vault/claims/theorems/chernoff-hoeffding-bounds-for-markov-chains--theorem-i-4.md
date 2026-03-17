---
slug: chernoff-hoeffding-bounds-for-markov-chains--theorem-i-4
label: Theorem I.4
claim_type: theorem
statement: 'Let C be an ergodic continuous-time Markov chain with state space [n],
  generator Q, stationary distribution π, and spectral expansion λ(C). Let (V(s))_{s≥0}
  be a continuous-time random walk on C starting from an initial distribution φ on
  [n]. For s ≥ 0, let fs : [n] → [0,1] be a weight function. Let X_t = ∫₀ᵗ fs(V(s))ds
  and μ = E[X_t]. Then for any δ ∈ (0, 1], Pr[X_t ≥ (1+δ)μ] ≤ (‖φ/π‖_π) · exp(−(1−λ(C))μδ²/3)
  and Pr[X_t ≤ (1−δ)μ] ≤ (‖φ/π‖_π) · exp(−(1−λ(C))μδ²/2). Furthermore, for any δ ≥
  0, Pr[X_t ≥ μ + δ] ≤ (‖φ/π‖_π) · exp(−2(1−λ(C))δ²/t).'
proof: ''
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/chernoff-bound-for-markov-chains]]'
- '[[concepts/cumulative-weight-x-t]]'
- '[[concepts/norm-phi-pi]]'
- '[[concepts/continuous-time-markov-chain]]'
- '[[concepts/generator]]'
- '[[concepts/spectral-expansion-lambda]]'
about_meta:
- target: '[[concepts/chernoff-bound-for-markov-chains]]'
  role: primary
  aspect: ''
- target: '[[concepts/cumulative-weight-x-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/norm-phi-pi]]'
  role: primary
  aspect: ''
- target: '[[concepts/continuous-time-markov-chain]]'
  role: primary
  aspect: ''
- target: '[[concepts/generator]]'
  role: primary
  aspect: ''
- target: '[[concepts/spectral-expansion-lambda]]'
  role: primary
  aspect: ''
depends_on: []
depends_on_meta: []
sourced_from:
- '[[sources/chernoff_hoeffding_bounds_for_markov_chains|chernoff_hoeffding_bounds_for_markov_chains]]'
sourced_from_meta:
- target: '[[sources/chernoff_hoeffding_bounds_for_markov_chains|chernoff_hoeffding_bounds_for_markov_chains]]'
  section: ''
  page: ''
  confidence: 0.0
---

# Theorem I.4

Let C be an ergodic continuous-time Markov chain with state space [n], generator Q, stationary distribution π, and spectral expansion λ(C). Let (V(s))_{s≥0} be a continuous-time random walk on C starting from an initial distribution φ on [n]. For s ≥ 0, let fs : [n] → [0,1] be a weight function. Let X_t = ∫₀ᵗ fs(V(s))ds and μ = E[X_t]. Then for any δ ∈ (0, 1], Pr[X_t ≥ (1+δ)μ] ≤ (‖φ/π‖_π) · exp(−(1−λ(C))μδ²/3) and Pr[X_t ≤ (1−δ)μ] ≤ (‖φ/π‖_π) · exp(−(1−λ(C))μδ²/2). Furthermore, for any δ ≥ 0, Pr[X_t ≥ μ + δ] ≤ (‖φ/π‖_π) · exp(−2(1−λ(C))δ²/t).
