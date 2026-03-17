---
slug: chernoff-hoeffding-bounds-for-markov-chains--theorem-1-1
label: Theorem 1.1
claim_type: theorem
statement: 'Let M be an ergodic Markov chain with state space [n], stationary distribution
  π, and spectral expansion λ(M). Let (V_1, ..., V_t) be a t-step random walk on M
  starting from an initial distribution φ. For each i ∈ [t], let f_i : [n] → [0,1]
  be a weight function with mean μ_i = E_{v~π}[f_i(v)] and let μ = (1/t)∑_{i=1}^{t}
  μ_i. Let X = (1/t)∑_{i=1}^{t} f_i(V_i). Then for any δ > 0, Pr[X ≥ μ + δ] ≤ ‖φ/π‖_π
  · exp(−(1−λ(M))δ²t/2) and Pr[X ≤ μ − δ] ≤ ‖φ/π‖_π · exp(−(1−λ(M))δ²t/2).'
proof: ''
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/deviation-parameter-delta]]'
- '[[concepts/chernoff-bound-for-markov-chains]]'
- '[[concepts/initial-distribution-phi]]'
- '[[concepts/spectral-expansion-lambda-m]]'
- '[[concepts/expected-weight-mu]]'
- '[[concepts/ergodic-markov-chains]]'
- '[[concepts/total-weight-x]]'
- '[[concepts/norm-phi-pi]]'
- '[[concepts/weight-function-f-i]]'
about_meta:
- target: '[[concepts/deviation-parameter-delta]]'
  role: primary
  aspect: ''
- target: '[[concepts/chernoff-bound-for-markov-chains]]'
  role: primary
  aspect: ''
- target: '[[concepts/initial-distribution-phi]]'
  role: primary
  aspect: ''
- target: '[[concepts/spectral-expansion-lambda-m]]'
  role: primary
  aspect: ''
- target: '[[concepts/expected-weight-mu]]'
  role: primary
  aspect: ''
- target: '[[concepts/ergodic-markov-chains]]'
  role: primary
  aspect: ''
- target: '[[concepts/total-weight-x]]'
  role: primary
  aspect: ''
- target: '[[concepts/norm-phi-pi]]'
  role: primary
  aspect: ''
- target: '[[concepts/weight-function-f-i]]'
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

# Theorem 1.1

Let M be an ergodic Markov chain with state space [n], stationary distribution π, and spectral expansion λ(M). Let (V_1, ..., V_t) be a t-step random walk on M starting from an initial distribution φ. For each i ∈ [t], let f_i : [n] → [0,1] be a weight function with mean μ_i = E_{v~π}[f_i(v)] and let μ = (1/t)∑_{i=1}^{t} μ_i. Let X = (1/t)∑_{i=1}^{t} f_i(V_i). Then for any δ > 0, Pr[X ≥ μ + δ] ≤ ‖φ/π‖_π · exp(−(1−λ(M))δ²t/2) and Pr[X ≤ μ − δ] ≤ ‖φ/π‖_π · exp(−(1−λ(M))δ²t/2).
