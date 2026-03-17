---
slug: chernoff-hoeffding-bounds-for-markov-chains--theorem-v-3-healy
label: Theorem V.3 (Healy)
claim_type: theorem
statement: 'Let M be an ergodic and reversible Markov chain with state space [n],
  stationary distribution π, and spectral gap γ. Let (V1,...,Vt) be a random walk
  on M from initial distribution π. For each i, let fi : [n] → [0,1]. Let X = Σ fi(Vi)
  and μ = E[X]. Then for any δ ∈ (0,1], Pr[X ≥ (1+δ)μ] ≤ (e^δ/((1+δ)^{(1+δ)}))^{γμ/(1+γδ/(1+δ))}.'
proof: ''
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/reversible-markov-chain]]'
- '[[concepts/stationary-distribution-pi]]'
- '[[concepts/spectral-gap]]'
- '[[concepts/chernoff-bound-for-markov-chains]]'
about_meta:
- target: '[[concepts/reversible-markov-chain]]'
  role: primary
  aspect: ''
- target: '[[concepts/stationary-distribution-pi]]'
  role: primary
  aspect: ''
- target: '[[concepts/spectral-gap]]'
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

# Theorem V.3 (Healy)

Let M be an ergodic and reversible Markov chain with state space [n], stationary distribution π, and spectral gap γ. Let (V1,...,Vt) be a random walk on M from initial distribution π. For each i, let fi : [n] → [0,1]. Let X = Σ fi(Vi) and μ = E[X]. Then for any δ ∈ (0,1], Pr[X ≥ (1+δ)μ] ≤ (e^δ/((1+δ)^{(1+δ)}))^{γμ/(1+γδ/(1+δ))}.
