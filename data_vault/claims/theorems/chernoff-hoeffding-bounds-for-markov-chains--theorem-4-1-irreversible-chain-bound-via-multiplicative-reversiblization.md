---
slug: chernoff-hoeffding-bounds-for-markov-chains--theorem-4-1-irreversible-chain-bound-via-multiplicative-reversiblization
label: Theorem 4.1 (Irreversible chain bound via multiplicative reversiblization)
claim_type: theorem
statement: 'Let M be an ergodic (possibly irreversible) Markov chain with state space
  [n] and stationary distribution π. Let M̃ be its time-reversal and R = M̃M be its
  multiplicative reversiblization. Then for any t-step random walk on M starting from
  φ, with weight functions f_i : [n] → [0,1] having mean μ_i, X = (1/t)∑ f_i(V_i),
  and μ = (1/t)∑ μ_i, we have Pr[X ≥ μ + δ] ≤ ‖φ/π‖_π · exp(−(1−λ(R))δ²t/4) and Pr[X
  ≤ μ − δ] ≤ ‖φ/π‖_π · exp(−(1−λ(R))δ²t/4), where λ(R) = λ(M̃M) is the spectral expansion
  of the multiplicative reversiblization.'
proof: ''
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/multiplicative-reversiblization]]'
- '[[concepts/chernoff-bound-for-markov-chains]]'
- '[[concepts/irreversible-markov-chain]]'
- '[[concepts/time-reversal]]'
- '[[concepts/norm-phi-pi]]'
- '[[concepts/spectral-expansion-lambda]]'
about_meta:
- target: '[[concepts/multiplicative-reversiblization]]'
  role: primary
  aspect: ''
- target: '[[concepts/chernoff-bound-for-markov-chains]]'
  role: primary
  aspect: ''
- target: '[[concepts/irreversible-markov-chain]]'
  role: primary
  aspect: ''
- target: '[[concepts/time-reversal]]'
  role: primary
  aspect: ''
- target: '[[concepts/norm-phi-pi]]'
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

# Theorem 4.1 (Irreversible chain bound via multiplicative reversiblization)

Let M be an ergodic (possibly irreversible) Markov chain with state space [n] and stationary distribution π. Let M̃ be its time-reversal and R = M̃M be its multiplicative reversiblization. Then for any t-step random walk on M starting from φ, with weight functions f_i : [n] → [0,1] having mean μ_i, X = (1/t)∑ f_i(V_i), and μ = (1/t)∑ μ_i, we have Pr[X ≥ μ + δ] ≤ ‖φ/π‖_π · exp(−(1−λ(R))δ²t/4) and Pr[X ≤ μ − δ] ≤ ‖φ/π‖_π · exp(−(1−λ(R))δ²t/4), where λ(R) = λ(M̃M) is the spectral expansion of the multiplicative reversiblization.
