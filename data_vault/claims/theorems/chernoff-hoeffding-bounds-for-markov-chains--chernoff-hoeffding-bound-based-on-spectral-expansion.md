---
slug: chernoff-hoeffding-bounds-for-markov-chains--chernoff-hoeffding-bound-based-on-spectral-expansion
label: Chernoff-Hoeffding bound based on spectral expansion
claim_type: theorem
statement: 'Consider an ergodic Markov chain M and a weight function f : [n] → [0,1]
  on the state space [n] of M with mean μ ≜ E_{v∼π}[f(v)], where π is the stationary
  distribution of M. A t-step random walk (v_1, …, v_t) on M starting from the stationary
  distribution π has expected total weight E[X] = μt, where X ≜ ∑_{i=1}^{t} f(v_i).
  Let λ be the spectral expansion of M, which is the square root of the second largest
  eigenvalue (in absolute value) of M∼M, where ∼M is the time-reversal Markov chain
  of M. Then the probability Pr[|X - μt| ≥ δμt] is at most exp(-Ω(δ²(1-λ)μt)) for
  0 ≤ δ ≤ 1, and exp(-Ω(δ(1-λ)μt)) for δ > 1.'
proof: ''
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/expected-weight-mu]]'
- '[[concepts/spectral-expansion-lambda-m]]'
- '[[concepts/ergodic-markov-chains]]'
- '[[concepts/total-weight-x]]'
- '[[concepts/multiplicative-reversiblization]]'
- '[[concepts/stationary-distribution-pi]]'
- '[[concepts/time-reversal-ilde-m]]'
- '[[concepts/deviation-parameter-delta]]'
- '[[concepts/chernoff-bound-for-markov-chains]]'
about_meta:
- target: '[[concepts/expected-weight-mu]]'
  role: primary
  aspect: ''
- target: '[[concepts/spectral-expansion-lambda-m]]'
  role: primary
  aspect: ''
- target: '[[concepts/ergodic-markov-chains]]'
  role: primary
  aspect: ''
- target: '[[concepts/total-weight-x]]'
  role: primary
  aspect: ''
- target: '[[concepts/multiplicative-reversiblization]]'
  role: primary
  aspect: ''
- target: '[[concepts/stationary-distribution-pi]]'
  role: primary
  aspect: ''
- target: '[[concepts/time-reversal-ilde-m]]'
  role: primary
  aspect: ''
- target: '[[concepts/deviation-parameter-delta]]'
  role: primary
  aspect: ''
- target: '[[concepts/chernoff-bound-for-markov-chains]]'
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

# Chernoff-Hoeffding bound based on spectral expansion

Consider an ergodic Markov chain M and a weight function f : [n] → [0,1] on the state space [n] of M with mean μ ≜ E_{v∼π}[f(v)], where π is the stationary distribution of M. A t-step random walk (v_1, …, v_t) on M starting from the stationary distribution π has expected total weight E[X] = μt, where X ≜ ∑_{i=1}^{t} f(v_i). Let λ be the spectral expansion of M, which is the square root of the second largest eigenvalue (in absolute value) of M∼M, where ∼M is the time-reversal Markov chain of M. Then the probability Pr[|X - μt| ≥ δμt] is at most exp(-Ω(δ²(1-λ)μt)) for 0 ≤ δ ≤ 1, and exp(-Ω(δ(1-λ)μt)) for δ > 1.
