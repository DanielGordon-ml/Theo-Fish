---
slug: chernoff-hoeffding-bounds-for-markov-chains--theorem-3
label: Theorem 3
claim_type: theorem
statement: 'Let M be an ergodic Markov chain with state space [n], stationary distribution
  π, ε-mixing time T(ε), and let (V_1, …, V_t) be a t-step random walk starting from
  initial distribution φ. For every i ∈ [t], let f_i : [n] → [0,1] with E_{v~π}[f_i(v)]
  = μ for all i. Define X = Σ_{i=1}^{t} f_i(V_i). Then:

  Pr[X ≥ (1+δ)μt] ≤ c‖φ‖_π exp(−δ²μt/(72T)) for 0 ≤ δ ≤ 1, and c‖φ‖_π exp(−δμt/(72T))
  for δ > 1.

  Pr[X ≤ (1−δ)μt] ≤ c‖φ‖_π exp(−δ²μt/(72T)) for 0 ≤ δ ≤ 1.'
proof: 'We partition the walk V_1, ..., V_t into T = T(ε) subgroups so that the i-th
  sub-walk consists of the steps (V_i, V_{i+T}, …). These sub-walks can be viewed
  as generated from Markov chain N ≜ M^T. Also, denote X^{(i)} ≜ Σ_{0≤j≤t/T} f_{i+jT}(V_{i+jT})
  as the total weight for each sub-walk and X̄ = Σ_{i=1}^{T} X^{(i)}/T as the average
  total weight.


  Next, we follow Hoeffding''s approach to cope with the correlation among the X^{(i)}.
  To start,

  Pr[X ≥ (1+δ)μt] = Pr[X̄ ≥ (1+δ)μt/T] ≤ E[e^{rX̄}]/e^{r(1+δ)μt/T}.


  Now noting that exp(·) is a convex function, we use Jensen''s inequality to obtain

  E[e^{rX̄}] ≤ Σ_{i≤T} (1/T) E[e^{rX^{(i)}}].


  Using Claim 3.1, we know λ(N) ≤ 1/2. Next, by Claim 3.2, for the i-th sub-walk,
  we have

  E[e^{rX^{(i)}}]/e^{r(1+δ)μt/T} ≤ c‖φM^i‖_π exp(−δ²μt/(72T)) for 0 ≤ δ ≤ 1, and c‖φM^i‖_π
  exp(−δμt/(72T)) for δ > 1,

  for an appropriately chosen r. Note that M^i arises because X^{(i)} starts from
  the distribution φM^i. On the other hand, ‖φM^i‖_π² = ‖φ^∥M^i‖_π² + ‖φ^⊥M^i‖_π²
  ≤ ‖φ^∥‖_π² + λ²(M^i)‖φ^⊥‖_π² ≤ ‖φ‖_π² (by using Lemma 5), so ‖φM^i‖_π ≤ ‖φ‖_π. Together
  with the above, we obtain

  Pr[X ≥ (1+δ)μt] ≤ c‖φ‖_π exp(−δ²μt/(72T)) for 0 ≤ δ ≤ 1, c‖φ‖_π exp(−δμt/(72T))
  for δ > 1.


  The second case is proved similarly:

  Pr[X ≤ (1−δ)μt] ≤ E[e^{−rX̄}]/e^{−r(1−δ)μt/T} ≤ Σ_{k=1}^{T} (1/T) E[e^{−rX^{(k)}}]/e^{−r(1−δ)μt/T}
  ≤ c‖φ‖_π exp(−δ²μt/(72T))

  again by Jensen''s inequality applied to exp(·).'
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/chernoff-bound-for-markov-chains]]'
- '[[concepts/mixing-time]]'
- '[[concepts/pi-norm]]'
- '[[concepts/weight-function-f-i]]'
- '[[concepts/total-weight-x]]'
- '[[concepts/spectral-expansion-lambda-m]]'
- '[[concepts/ergodic-markov-chains]]'
- '[[concepts/random-walk-v1-vt]]'
- '[[concepts/concentration-inequality]]'
- '[[concepts/expected-weight-mu]]'
- '[[concepts/stationary-distribution-pi]]'
- '[[concepts/epsilon-mixing-time-t-epsilon]]'
- '[[concepts/initial-distribution-phi]]'
- '[[concepts/total-weight-x]]'
- '[[concepts/expected-weight-mu]]'
- '[[concepts/epsilon-mixing-time-t-epsilon]]'
- '[[concepts/stationary-distribution-pi]]'
- '[[concepts/pi-norm]]'
- '[[concepts/spectral-expansion-lambda-m]]'
- '[[concepts/weight-function-f-i]]'
- '[[concepts/chernoff-bound-for-markov-chains]]'
- '[[concepts/initial-distribution-phi]]'
- '[[concepts/ergodic-markov-chains]]'
- '[[concepts/concentration-inequality]]'
- '[[concepts/random-walk-v1-vt]]'
- '[[concepts/mixing-time]]'
about_meta:
- target: '[[concepts/chernoff-bound-for-markov-chains]]'
  role: primary
  aspect: ''
- target: '[[concepts/mixing-time]]'
  role: primary
  aspect: ''
- target: '[[concepts/pi-norm]]'
  role: primary
  aspect: ''
- target: '[[concepts/weight-function-f-i]]'
  role: primary
  aspect: ''
- target: '[[concepts/total-weight-x]]'
  role: primary
  aspect: ''
- target: '[[concepts/spectral-expansion-lambda-m]]'
  role: primary
  aspect: ''
- target: '[[concepts/ergodic-markov-chains]]'
  role: primary
  aspect: ''
- target: '[[concepts/random-walk-v1-vt]]'
  role: primary
  aspect: ''
- target: '[[concepts/concentration-inequality]]'
  role: primary
  aspect: ''
- target: '[[concepts/expected-weight-mu]]'
  role: primary
  aspect: ''
- target: '[[concepts/stationary-distribution-pi]]'
  role: primary
  aspect: ''
- target: '[[concepts/epsilon-mixing-time-t-epsilon]]'
  role: primary
  aspect: ''
- target: '[[concepts/initial-distribution-phi]]'
  role: primary
  aspect: ''
- target: '[[concepts/total-weight-x]]'
  role: primary
  aspect: ''
- target: '[[concepts/expected-weight-mu]]'
  role: primary
  aspect: ''
- target: '[[concepts/epsilon-mixing-time-t-epsilon]]'
  role: primary
  aspect: ''
- target: '[[concepts/stationary-distribution-pi]]'
  role: primary
  aspect: ''
- target: '[[concepts/pi-norm]]'
  role: primary
  aspect: ''
- target: '[[concepts/spectral-expansion-lambda-m]]'
  role: primary
  aspect: ''
- target: '[[concepts/weight-function-f-i]]'
  role: primary
  aspect: ''
- target: '[[concepts/chernoff-bound-for-markov-chains]]'
  role: primary
  aspect: ''
- target: '[[concepts/initial-distribution-phi]]'
  role: primary
  aspect: ''
- target: '[[concepts/ergodic-markov-chains]]'
  role: primary
  aspect: ''
- target: '[[concepts/concentration-inequality]]'
  role: primary
  aspect: ''
- target: '[[concepts/random-walk-v1-vt]]'
  role: primary
  aspect: ''
- target: '[[concepts/mixing-time]]'
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

# Theorem 3

Let M be an ergodic Markov chain with state space [n], stationary distribution π, ε-mixing time T(ε), and let (V_1, …, V_t) be a t-step random walk starting from initial distribution φ. For every i ∈ [t], let f_i : [n] → [0,1] with E_{v~π}[f_i(v)] = μ for all i. Define X = Σ_{i=1}^{t} f_i(V_i). Then:
Pr[X ≥ (1+δ)μt] ≤ c‖φ‖_π exp(−δ²μt/(72T)) for 0 ≤ δ ≤ 1, and c‖φ‖_π exp(−δμt/(72T)) for δ > 1.
Pr[X ≤ (1−δ)μt] ≤ c‖φ‖_π exp(−δ²μt/(72T)) for 0 ≤ δ ≤ 1.


## Proof

We partition the walk V_1, ..., V_t into T = T(ε) subgroups so that the i-th sub-walk consists of the steps (V_i, V_{i+T}, …). These sub-walks can be viewed as generated from Markov chain N ≜ M^T. Also, denote X^{(i)} ≜ Σ_{0≤j≤t/T} f_{i+jT}(V_{i+jT}) as the total weight for each sub-walk and X̄ = Σ_{i=1}^{T} X^{(i)}/T as the average total weight.

Next, we follow Hoeffding's approach to cope with the correlation among the X^{(i)}. To start,
Pr[X ≥ (1+δ)μt] = Pr[X̄ ≥ (1+δ)μt/T] ≤ E[e^{rX̄}]/e^{r(1+δ)μt/T}.

Now noting that exp(·) is a convex function, we use Jensen's inequality to obtain
E[e^{rX̄}] ≤ Σ_{i≤T} (1/T) E[e^{rX^{(i)}}].

Using Claim 3.1, we know λ(N) ≤ 1/2. Next, by Claim 3.2, for the i-th sub-walk, we have
E[e^{rX^{(i)}}]/e^{r(1+δ)μt/T} ≤ c‖φM^i‖_π exp(−δ²μt/(72T)) for 0 ≤ δ ≤ 1, and c‖φM^i‖_π exp(−δμt/(72T)) for δ > 1,
for an appropriately chosen r. Note that M^i arises because X^{(i)} starts from the distribution φM^i. On the other hand, ‖φM^i‖_π² = ‖φ^∥M^i‖_π² + ‖φ^⊥M^i‖_π² ≤ ‖φ^∥‖_π² + λ²(M^i)‖φ^⊥‖_π² ≤ ‖φ‖_π² (by using Lemma 5), so ‖φM^i‖_π ≤ ‖φ‖_π. Together with the above, we obtain
Pr[X ≥ (1+δ)μt] ≤ c‖φ‖_π exp(−δ²μt/(72T)) for 0 ≤ δ ≤ 1, c‖φ‖_π exp(−δμt/(72T)) for δ > 1.

The second case is proved similarly:
Pr[X ≤ (1−δ)μt] ≤ E[e^{−rX̄}]/e^{−r(1−δ)μt/T} ≤ Σ_{k=1}^{T} (1/T) E[e^{−rX^{(k)}}]/e^{−r(1−δ)μt/T} ≤ c‖φ‖_π exp(−δ²μt/(72T))
again by Jensen's inequality applied to exp(·).
