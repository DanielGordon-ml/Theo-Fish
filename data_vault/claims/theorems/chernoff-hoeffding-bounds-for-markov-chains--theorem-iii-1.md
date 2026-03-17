---
slug: chernoff-hoeffding-bounds-for-markov-chains--theorem-iii-1
label: Theorem III.1
claim_type: theorem
statement: 'Let M be an ergodic Markov chain with state space [n], stationary distribution
  π and spectral expansion λ = λ(M). Let (V1,...,Vt) be a t-step random walk on M
  starting from an initial distribution φ on [n]. For each i ∈ [t], let fi : [n] →
  [0,1] be a weight function applied at step i. Let X = Σ_{i=1}^{t} fi(Vi) be the
  total weight and μ = E[X]. Then for any r > 0, E[e^{rX}] ≤ ‖φ/π‖_π · ∏_{i=1}^{t}(1
  + (e^r − 1)μ_i)^{1−λ} where μ_i = Σ_{j∈[n]} π(j) fi(j) for each i ∈ [t].'
proof: 'The proof proceeds by writing E_φ[e^{rX}] = E_φ[e^{r·Σ fi(Vi)}] and decomposing
  the computation step by step. For each step i, the vector is decomposed into components
  parallel and perpendicular to the stationary distribution π. Using Lemma III.2 and
  Lemma III.3, the parallel and perpendicular components are bounded. Specifically,
  by Lemma III.2, ‖e^{r·fi}‖_∞ ≤ 1 + (e^r − 1)μ_i when applied to the parallel component.
  By Lemma III.3, ‖P_i · x‖_π ≤ ‖P_i‖_∞ · ‖x‖_π. Combined with Lemma II.4 (contraction),
  at each step the perpendicular component shrinks by factor λ while the parallel
  component grows by at most (1 + (e^r − 1)μ_i). The final bound is obtained by telescoping
  these bounds across all t steps: E_φ[e^{rX}] ≤ ‖φ/π‖_π · ∏_{i=1}^{t}(1 + (e^r −
  1)μ_i)^{1−λ}.'
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/expected-weight-mu]]'
- '[[concepts/perpendicular-component-operator]]'
- '[[concepts/norm-phi-pi]]'
- '[[concepts/ergodic-markov-chains]]'
- '[[concepts/parallel-component-operator]]'
- '[[concepts/total-weight-x]]'
- '[[concepts/weight-function-f-i]]'
- '[[concepts/moment-generating-function-bound]]'
- '[[concepts/spectral-expansion-lambda-m]]'
about_meta:
- target: '[[concepts/expected-weight-mu]]'
  role: primary
  aspect: ''
- target: '[[concepts/perpendicular-component-operator]]'
  role: primary
  aspect: ''
- target: '[[concepts/norm-phi-pi]]'
  role: primary
  aspect: ''
- target: '[[concepts/ergodic-markov-chains]]'
  role: primary
  aspect: ''
- target: '[[concepts/parallel-component-operator]]'
  role: primary
  aspect: ''
- target: '[[concepts/total-weight-x]]'
  role: primary
  aspect: ''
- target: '[[concepts/weight-function-f-i]]'
  role: primary
  aspect: ''
- target: '[[concepts/moment-generating-function-bound]]'
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

# Theorem III.1

Let M be an ergodic Markov chain with state space [n], stationary distribution π and spectral expansion λ = λ(M). Let (V1,...,Vt) be a t-step random walk on M starting from an initial distribution φ on [n]. For each i ∈ [t], let fi : [n] → [0,1] be a weight function applied at step i. Let X = Σ_{i=1}^{t} fi(Vi) be the total weight and μ = E[X]. Then for any r > 0, E[e^{rX}] ≤ ‖φ/π‖_π · ∏_{i=1}^{t}(1 + (e^r − 1)μ_i)^{1−λ} where μ_i = Σ_{j∈[n]} π(j) fi(j) for each i ∈ [t].


## Proof

The proof proceeds by writing E_φ[e^{rX}] = E_φ[e^{r·Σ fi(Vi)}] and decomposing the computation step by step. For each step i, the vector is decomposed into components parallel and perpendicular to the stationary distribution π. Using Lemma III.2 and Lemma III.3, the parallel and perpendicular components are bounded. Specifically, by Lemma III.2, ‖e^{r·fi}‖_∞ ≤ 1 + (e^r − 1)μ_i when applied to the parallel component. By Lemma III.3, ‖P_i · x‖_π ≤ ‖P_i‖_∞ · ‖x‖_π. Combined with Lemma II.4 (contraction), at each step the perpendicular component shrinks by factor λ while the parallel component grows by at most (1 + (e^r − 1)μ_i). The final bound is obtained by telescoping these bounds across all t steps: E_φ[e^{rX}] ≤ ‖φ/π‖_π · ∏_{i=1}^{t}(1 + (e^r − 1)μ_i)^{1−λ}.
