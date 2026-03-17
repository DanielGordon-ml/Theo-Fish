---
slug: chernoff-hoeffding-bounds-for-markov-chains--theorem-v-4-rabani-sinclair-wigderson-impagliazzo-kabanets
label: Theorem V.4 (Rabani-Sinclair-Wigderson / Impagliazzo-Kabanets)
claim_type: theorem
statement: 'Consider an ergodic and reversible Markov chain M with state space [n],
  stationary distribution π and spectral expansion λ. Let (V1,...,Vt) be a random
  walk starting from a distribution φ with ‖φ/π‖_π ≤ 1/ε. For each i, let fi : [n]
  → {0,1}. Let X = Σ fi(Vi) and μ = E_π[Σ fi(Vi)]. Then for any δ ∈ (0,1], Pr[X ≥
  (1+δ)μ] ≤ 2/ε · exp(−(1−λ)μδ²/4) and Pr[X ≤ (1−δ)μ] ≤ 2/ε · exp(−(1−λ)μδ²/4).'
proof: ''
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/norm-phi-pi]]'
- '[[concepts/reversible-markov-chain]]'
- '[[concepts/chernoff-bound-for-markov-chains]]'
- '[[concepts/spectral-expansion-lambda-m]]'
about_meta:
- target: '[[concepts/norm-phi-pi]]'
  role: primary
  aspect: ''
- target: '[[concepts/reversible-markov-chain]]'
  role: primary
  aspect: ''
- target: '[[concepts/chernoff-bound-for-markov-chains]]'
  role: primary
  aspect: ''
- target: '[[concepts/spectral-expansion-lambda-m]]'
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

# Theorem V.4 (Rabani-Sinclair-Wigderson / Impagliazzo-Kabanets)

Consider an ergodic and reversible Markov chain M with state space [n], stationary distribution π and spectral expansion λ. Let (V1,...,Vt) be a random walk starting from a distribution φ with ‖φ/π‖_π ≤ 1/ε. For each i, let fi : [n] → {0,1}. Let X = Σ fi(Vi) and μ = E_π[Σ fi(Vi)]. Then for any δ ∈ (0,1], Pr[X ≥ (1+δ)μ] ≤ 2/ε · exp(−(1−λ)μδ²/4) and Pr[X ≤ (1−δ)μ] ≤ 2/ε · exp(−(1−λ)μδ²/4).
