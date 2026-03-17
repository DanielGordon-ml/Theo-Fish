---
slug: chernoff-hoeffding-bounds-for-markov-chains--theorem-i-1
label: Theorem I.1
claim_type: theorem
statement: 'Let M be an ergodic Markov chain with state space [n], stationary distribution
  π and spectral expansion λ(M). Let (V1, ..., Vt) be a t-step random walk on M starting
  from an initial distribution φ on [n]. For each i ∈ [t], let fi : [n] → [0,1] be
  a weight function applied at step i. Let X = Σ_{i=1}^{t} fi(Vi) be the total weight,
  μ = E[X] be the expected total weight. Then for any δ > 0, Pr[X ≥ (1+δ)μ] ≤ (‖φ/π‖_π)
  · ((e^δ)/((1+δ)^(1+δ)))^((1-λ(M))μ) and Pr[X ≤ (1-δ)μ] ≤ (‖φ/π‖_π) · ((e^(-δ))/((1-δ)^(1-δ)))^((1-λ(M))μ)'
proof: ''
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/weight-function-f-i]]'
- '[[concepts/total-weight-x]]'
- '[[concepts/expected-weight-mu]]'
- '[[concepts/spectral-expansion-lambda-m]]'
- '[[concepts/chernoff-bound-for-markov-chains]]'
- '[[concepts/ergodic-markov-chains]]'
- '[[concepts/norm-phi-pi]]'
about_meta:
- target: '[[concepts/weight-function-f-i]]'
  role: primary
  aspect: ''
- target: '[[concepts/total-weight-x]]'
  role: primary
  aspect: ''
- target: '[[concepts/expected-weight-mu]]'
  role: primary
  aspect: ''
- target: '[[concepts/spectral-expansion-lambda-m]]'
  role: primary
  aspect: ''
- target: '[[concepts/chernoff-bound-for-markov-chains]]'
  role: primary
  aspect: ''
- target: '[[concepts/ergodic-markov-chains]]'
  role: primary
  aspect: ''
- target: '[[concepts/norm-phi-pi]]'
  role: primary
  aspect: ''
depends_on:
- '[[claims/chernoff-hoeffding-bounds-for-markov-chains--lemma-ii-1]]'
- '[[claims/chernoff-hoeffding-bounds-for-markov-chains--lemma-ii-2]]'
depends_on_meta:
- target: '[[claims/chernoff-hoeffding-bounds-for-markov-chains--lemma-ii-1]]'
- target: '[[claims/chernoff-hoeffding-bounds-for-markov-chains--lemma-ii-2]]'
sourced_from:
- '[[sources/chernoff_hoeffding_bounds_for_markov_chains|chernoff_hoeffding_bounds_for_markov_chains]]'
sourced_from_meta:
- target: '[[sources/chernoff_hoeffding_bounds_for_markov_chains|chernoff_hoeffding_bounds_for_markov_chains]]'
  section: ''
  page: ''
  confidence: 0.0
---

# Theorem I.1

Let M be an ergodic Markov chain with state space [n], stationary distribution π and spectral expansion λ(M). Let (V1, ..., Vt) be a t-step random walk on M starting from an initial distribution φ on [n]. For each i ∈ [t], let fi : [n] → [0,1] be a weight function applied at step i. Let X = Σ_{i=1}^{t} fi(Vi) be the total weight, μ = E[X] be the expected total weight. Then for any δ > 0, Pr[X ≥ (1+δ)μ] ≤ (‖φ/π‖_π) · ((e^δ)/((1+δ)^(1+δ)))^((1-λ(M))μ) and Pr[X ≤ (1-δ)μ] ≤ (‖φ/π‖_π) · ((e^(-δ))/((1-δ)^(1-δ)))^((1-λ(M))μ)
