---
slug: chernoff-hoeffding-bounds-for-markov-chains--theorem-1-3-continuous-time-version
label: Theorem 1.3 (Continuous-time version)
claim_type: theorem
statement: 'Let C be an ergodic continuous-time Markov chain with state space [n],
  stationary distribution π, and generator Q with spectral gap γ. Let {V_s}_{s≥0}
  be a random walk on C starting from initial distribution φ. For each time s ≥ 0,
  let f_s : [n] → [0,1] be a weight function with E_{v~π}[f_s(v)] = μ_s. Let X_t =
  (1/t)∫_0^t f_s(V_s)ds and μ = (1/t)∫_0^t μ_s ds. Then for any δ > 0, Pr[X_t ≥ μ
  + δ] ≤ ‖φ/π‖_π · exp(−γδ²t/2) and Pr[X_t ≤ μ − δ] ≤ ‖φ/π‖_π · exp(−γδ²t/2).'
proof: ''
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/deviation-parameter-delta]]'
- '[[concepts/chernoff-bound-for-markov-chains]]'
- '[[concepts/ergodic-markov-chains]]'
- '[[concepts/generator]]'
- '[[concepts/norm-phi-pi]]'
- '[[concepts/continuous-time-markov-chain]]'
- '[[concepts/spectral-gap]]'
about_meta:
- target: '[[concepts/deviation-parameter-delta]]'
  role: primary
  aspect: ''
- target: '[[concepts/chernoff-bound-for-markov-chains]]'
  role: primary
  aspect: ''
- target: '[[concepts/ergodic-markov-chains]]'
  role: primary
  aspect: ''
- target: '[[concepts/generator]]'
  role: primary
  aspect: ''
- target: '[[concepts/norm-phi-pi]]'
  role: primary
  aspect: ''
- target: '[[concepts/continuous-time-markov-chain]]'
  role: primary
  aspect: ''
- target: '[[concepts/spectral-gap]]'
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

# Theorem 1.3 (Continuous-time version)

Let C be an ergodic continuous-time Markov chain with state space [n], stationary distribution π, and generator Q with spectral gap γ. Let {V_s}_{s≥0} be a random walk on C starting from initial distribution φ. For each time s ≥ 0, let f_s : [n] → [0,1] be a weight function with E_{v~π}[f_s(v)] = μ_s. Let X_t = (1/t)∫_0^t f_s(V_s)ds and μ = (1/t)∫_0^t μ_s ds. Then for any δ > 0, Pr[X_t ≥ μ + δ] ≤ ‖φ/π‖_π · exp(−γδ²t/2) and Pr[X_t ≤ μ − δ] ≤ ‖φ/π‖_π · exp(−γδ²t/2).
