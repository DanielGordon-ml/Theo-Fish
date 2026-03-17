---
slug: chernoff-hoeffding-bounds-for-markov-chains--chernoff-hoeffding-bound-based-on-l1-mixing-time
label: Chernoff-Hoeffding bound based on L1 mixing-time
claim_type: theorem
statement: 'Consider an ergodic Markov chain M and a weight function f : [n] → [0,1]
  on the state space [n] of M with mean μ ≜ E_{v∼π}[f(v)], where π is the stationary
  distribution of M. A t-step random walk (v_1, …, v_t) on M starting from the stationary
  distribution π has expected total weight E[X] = μt, where X ≜ ∑_{i=1}^{t} f(v_i).
  Let T be the L_1 mixing-time of M. Then the probability Pr[|X - μt| ≥ δμt] is at
  most exp(-Ω(δ²μt/T)) for 0 ≤ δ ≤ 1, and exp(-Ω(δμt/T)) for δ > 1. The bounds hold
  even if the weight functions f_i''s for i ∈ [t] are distinct, provided that all
  of them have the same mean μ.'
proof: ''
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/stationary-distribution-pi]]'
- '[[concepts/total-weight-x]]'
- '[[concepts/l1-mixing-time]]'
- '[[concepts/weight-function-f-i]]'
- '[[concepts/deviation-parameter-delta]]'
- '[[concepts/chernoff-bound-for-markov-chains]]'
- '[[concepts/ergodic-markov-chains]]'
- '[[concepts/expected-weight-mu]]'
about_meta:
- target: '[[concepts/stationary-distribution-pi]]'
  role: primary
  aspect: ''
- target: '[[concepts/total-weight-x]]'
  role: primary
  aspect: ''
- target: '[[concepts/l1-mixing-time]]'
  role: primary
  aspect: ''
- target: '[[concepts/weight-function-f-i]]'
  role: primary
  aspect: ''
- target: '[[concepts/deviation-parameter-delta]]'
  role: primary
  aspect: ''
- target: '[[concepts/chernoff-bound-for-markov-chains]]'
  role: primary
  aspect: ''
- target: '[[concepts/ergodic-markov-chains]]'
  role: primary
  aspect: ''
- target: '[[concepts/expected-weight-mu]]'
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

# Chernoff-Hoeffding bound based on L1 mixing-time

Consider an ergodic Markov chain M and a weight function f : [n] → [0,1] on the state space [n] of M with mean μ ≜ E_{v∼π}[f(v)], where π is the stationary distribution of M. A t-step random walk (v_1, …, v_t) on M starting from the stationary distribution π has expected total weight E[X] = μt, where X ≜ ∑_{i=1}^{t} f(v_i). Let T be the L_1 mixing-time of M. Then the probability Pr[|X - μt| ≥ δμt] is at most exp(-Ω(δ²μt/T)) for 0 ≤ δ ≤ 1, and exp(-Ω(δμt/T)) for δ > 1. The bounds hold even if the weight functions f_i's for i ∈ [t] are distinct, provided that all of them have the same mean μ.
