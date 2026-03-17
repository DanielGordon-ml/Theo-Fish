---
slug: chernoff-hoeffding-bounds-for-markov-chains--lemma-3-4
label: Lemma 3.4
claim_type: lemma
statement: 'Let M be an ergodic Markov chain with state space [n], stationary distribution
  π, and spectral expansion λ = λ(M). For each i ∈ [t], let f_i : [n] → [0,1] be a
  weight function. Let P_i be the diagonal matrix with (P_i)_{jj} = f_i(j), and P_i^⊥
  = I − P_i. For any r > 0, E_{φ}[e^{rX·t}] ≤ ‖φ/π‖_π · ((1+λ)e^r/2 + (1−λ)/2)^t,
  where X = (1/t)∑_{i=1}^{t} f_i(V_i).'
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/norm-phi-pi]]'
- '[[concepts/spectral-expansion-lambda-m]]'
- '[[concepts/ergodic-markov-chains]]'
- '[[concepts/parameter-r]]'
- '[[concepts/diagonal-matrix-p-i]]'
- '[[concepts/moment-generating-function-bound]]'
about_meta:
- target: '[[concepts/norm-phi-pi]]'
  role: primary
  aspect: ''
- target: '[[concepts/spectral-expansion-lambda-m]]'
  role: primary
  aspect: ''
- target: '[[concepts/ergodic-markov-chains]]'
  role: primary
  aspect: ''
- target: '[[concepts/parameter-r]]'
  role: primary
  aspect: ''
- target: '[[concepts/diagonal-matrix-p-i]]'
  role: primary
  aspect: ''
- target: '[[concepts/moment-generating-function-bound]]'
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

# Lemma 3.4

Let M be an ergodic Markov chain with state space [n], stationary distribution π, and spectral expansion λ = λ(M). For each i ∈ [t], let f_i : [n] → [0,1] be a weight function. Let P_i be the diagonal matrix with (P_i)_{jj} = f_i(j), and P_i^⊥ = I − P_i. For any r > 0, E_{φ}[e^{rX·t}] ≤ ‖φ/π‖_π · ((1+λ)e^r/2 + (1−λ)/2)^t, where X = (1/t)∑_{i=1}^{t} f_i(V_i).
