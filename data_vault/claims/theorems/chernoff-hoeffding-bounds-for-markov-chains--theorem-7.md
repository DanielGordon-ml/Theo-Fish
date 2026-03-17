---
slug: chernoff-hoeffding-bounds-for-markov-chains--theorem-7
label: Theorem 7
claim_type: theorem
statement: 'Let Λ be the generator of an ergodic continuous time Markov chain with
  state space [n] and mixing time T = T(ε). Let {v_t : t ∈ R⁺} be a random walk on
  the chain starting from an initial distribution φ such that v_t represents the state
  where the walk stays at time t. Let {f_t : [n] → [0,1] | t ∈ R⁺} be a family of
  functions such that μ = E_{v~π}[f_t(v)] for all t. Define the weight over the walk
  {v_s : s ∈ R⁺} up to time t by X_t ≜ ∫₀ᵗ f_s(v_s) ds. There exists a constant c
  such that

  1. Pr[X ≥ (1+δ)μt] ≤ c‖φ‖_π exp(−δ²μt/(72T)) for 0 ≤ δ ≤ 1, and c‖φ‖_π exp(−δμt/(72T))
  for δ > 1

  2. Pr[X ≤ (1−δ)μt] ≤ c‖φ‖_π exp(−δ²μt/(72T)) for 0 ≤ δ ≤ 1'
proof: ''
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/deviation-parameter-delta]]'
- '[[concepts/cumulative-weight-x-t]]'
- '[[concepts/generator]]'
- '[[concepts/mixing-time]]'
- '[[concepts/positive-real-time]]'
- '[[concepts/concentration-inequality]]'
- '[[concepts/state-space-n]]'
- '[[concepts/expected-value-mu]]'
- '[[concepts/norm-phi-pi]]'
- '[[concepts/ergodic]]'
- '[[concepts/continuous-time-markov-chain]]'
- '[[concepts/chernoff-bound-for-markov-chains]]'
- '[[concepts/stationary-distribution-pi]]'
about_meta:
- target: '[[concepts/deviation-parameter-delta]]'
  role: primary
  aspect: ''
- target: '[[concepts/cumulative-weight-x-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/generator]]'
  role: primary
  aspect: ''
- target: '[[concepts/mixing-time]]'
  role: primary
  aspect: ''
- target: '[[concepts/positive-real-time]]'
  role: primary
  aspect: ''
- target: '[[concepts/concentration-inequality]]'
  role: primary
  aspect: ''
- target: '[[concepts/state-space-n]]'
  role: primary
  aspect: ''
- target: '[[concepts/expected-value-mu]]'
  role: primary
  aspect: ''
- target: '[[concepts/norm-phi-pi]]'
  role: primary
  aspect: ''
- target: '[[concepts/ergodic]]'
  role: primary
  aspect: ''
- target: '[[concepts/continuous-time-markov-chain]]'
  role: primary
  aspect: ''
- target: '[[concepts/chernoff-bound-for-markov-chains]]'
  role: primary
  aspect: ''
- target: '[[concepts/stationary-distribution-pi]]'
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

# Theorem 7

Let Λ be the generator of an ergodic continuous time Markov chain with state space [n] and mixing time T = T(ε). Let {v_t : t ∈ R⁺} be a random walk on the chain starting from an initial distribution φ such that v_t represents the state where the walk stays at time t. Let {f_t : [n] → [0,1] | t ∈ R⁺} be a family of functions such that μ = E_{v~π}[f_t(v)] for all t. Define the weight over the walk {v_s : s ∈ R⁺} up to time t by X_t ≜ ∫₀ᵗ f_s(v_s) ds. There exists a constant c such that
1. Pr[X ≥ (1+δ)μt] ≤ c‖φ‖_π exp(−δ²μt/(72T)) for 0 ≤ δ ≤ 1, and c‖φ‖_π exp(−δμt/(72T)) for δ > 1
2. Pr[X ≤ (1−δ)μt] ≤ c‖φ‖_π exp(−δ²μt/(72T)) for 0 ≤ δ ≤ 1
