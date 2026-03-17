---
slug: chernoff-hoeffding-bounds-for-markov-chains--lemma-6
label: Lemma 6
claim_type: lemma
statement: '(The effect of the P operator) Let M be an ergodic Markov chain with state
  space [n] and stationary distribution π. Let f : [n] → [0,1] be a weight function
  with E_{v~π}[f(v)] = μ. Let P be a diagonal matrix with diagonal entries P_{j,j}
  ≜ e^{r f(j)} for j ∈ [n], where r is a parameter satisfying 0 ≤ r ≤ 1/2. Then

  1. ‖(πP)^∥‖_π ≤ 1 + (e^r − 1)μ.

  2. ‖(πP)^⊥‖_π ≤ 2r√μ.

  3. For every vector y ⊥ π, ‖(yP)^∥‖_π ≤ 2r√μ ‖y‖_π.

  4. For every vector y ⊥ π, ‖(yP)^⊥‖_π ≤ e^r ‖y‖_π.'
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/stationary-distribution-pi]]'
- '[[concepts/diagonal-matrix-p-i]]'
- '[[concepts/parallel-component-operator]]'
- '[[concepts/weight-function]]'
- '[[concepts/pi-norm]]'
- '[[concepts/mean-mu]]'
- '[[concepts/perpendicular-component-operator]]'
about_meta:
- target: '[[concepts/stationary-distribution-pi]]'
  role: primary
  aspect: ''
- target: '[[concepts/diagonal-matrix-p-i]]'
  role: primary
  aspect: ''
- target: '[[concepts/parallel-component-operator]]'
  role: primary
  aspect: ''
- target: '[[concepts/weight-function]]'
  role: primary
  aspect: ''
- target: '[[concepts/pi-norm]]'
  role: primary
  aspect: ''
- target: '[[concepts/mean-mu]]'
  role: primary
  aspect: ''
- target: '[[concepts/perpendicular-component-operator]]'
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

# Lemma 6

(The effect of the P operator) Let M be an ergodic Markov chain with state space [n] and stationary distribution π. Let f : [n] → [0,1] be a weight function with E_{v~π}[f(v)] = μ. Let P be a diagonal matrix with diagonal entries P_{j,j} ≜ e^{r f(j)} for j ∈ [n], where r is a parameter satisfying 0 ≤ r ≤ 1/2. Then
1. ‖(πP)^∥‖_π ≤ 1 + (e^r − 1)μ.
2. ‖(πP)^⊥‖_π ≤ 2r√μ.
3. For every vector y ⊥ π, ‖(yP)^∥‖_π ≤ 2r√μ ‖y‖_π.
4. For every vector y ⊥ π, ‖(yP)^⊥‖_π ≤ e^r ‖y‖_π.
