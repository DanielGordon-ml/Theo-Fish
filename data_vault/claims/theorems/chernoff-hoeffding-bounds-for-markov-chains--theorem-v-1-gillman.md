---
slug: chernoff-hoeffding-bounds-for-markov-chains--theorem-v-1-gillman
label: Theorem V.1 (Gillman)
claim_type: theorem
statement: 'Let M be an ergodic and reversible Markov chain with state space [n],
  stationary distribution π, and spectral gap γ. Let (V1, ..., Vt) be a random walk
  on M starting from distribution φ. For each i ∈ [t], let fi : [n] → [0,1]. Let X
  = Σ fi(Vi) and μ = E[X]. Then for any δ ≥ 0, Pr[X ≥ μ + δ] ≤ ‖φ/π‖_π · exp(−δ²γ/(2t)).'
proof: ''
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/reversible-markov-chain]]'
- '[[concepts/chernoff-bound-for-markov-chains]]'
- '[[concepts/norm-phi-pi]]'
- '[[concepts/spectral-gap]]'
about_meta:
- target: '[[concepts/reversible-markov-chain]]'
  role: primary
  aspect: ''
- target: '[[concepts/chernoff-bound-for-markov-chains]]'
  role: primary
  aspect: ''
- target: '[[concepts/norm-phi-pi]]'
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

# Theorem V.1 (Gillman)

Let M be an ergodic and reversible Markov chain with state space [n], stationary distribution π, and spectral gap γ. Let (V1, ..., Vt) be a random walk on M starting from distribution φ. For each i ∈ [t], let fi : [n] → [0,1]. Let X = Σ fi(Vi) and μ = E[X]. Then for any δ ≥ 0, Pr[X ≥ μ + δ] ≤ ‖φ/π‖_π · exp(−δ²γ/(2t)).
