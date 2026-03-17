---
slug: chernoff-hoeffding-bounds-for-markov-chains--claim-3-2
label: Claim 3.2
claim_type: lemma
statement: 'Let M be an ergodic Markov chain with state space [n], stationary distribution
  π, and spectral expansion λ = λ(M). Let (V_1, …, V_t) denote a t-step random walk
  on M starting from an initial distribution φ on [n], i.e., V_1 ~ φ. For every i
  ∈ [t], let f_i : [n] → [0,1] be a weight function at step i such that the expected
  weight E_{v~π}[f_i(v)] = μ for all i. Define the total weight of the walk (V_1,
  …, V_t) by X ≜ Σ_{i=1}^{t} f_i(V_i). There exists some constant c and a parameter
  r > 0 that depends only on λ and δ such that

  1. E[e^{rX}]/e^{r(1+δ)μt} ≤ c‖φ‖_π exp(−δ²(1−λ)μt/36) for 0 ≤ δ ≤ 1, and c‖φ‖_π
  exp(−δ(1−λ)μt/36) for δ > 1.

  2. E[e^{−rX}]/e^{−r(1−δ)μt} ≤ c‖φ‖_π exp(−δ²(1−λ)μt/36) for 0 ≤ δ ≤ 1.'
proof: 'First, recall that E[e^{rX}] = ‖(φP_1 M P_2 ... M P_t)^∥‖_π = ‖(φP_1 M P_2
  ... M P_t M)^∥‖_π = ‖(φ ∏_{i=1}^{t} (P_i M))^∥‖_π where the second equality comes
  from Lemma 5. Our choice of r is r = min{1/2, log(1/λ)/2, 1 − √λ, (1−λ)δ/18}. We
  trace the π-norm of both parallel and perpendicular components of the random walk
  for each application of P_i M. Let z_0 ≜ φ and z_i = z_{i−1} P_i M for i ∈ [t].
  By triangle inequality and Lemma 5 and 6, for every i ∈ [t],

  ‖z_i^∥‖_π = ‖(z_{i−1} P_i M)^∥‖_π ≤ (1 + (e^r − 1)μ)‖z_{i−1}^∥‖_π + (2r√μ)‖z_{i−1}^⊥‖_π,

  and similarly,

  ‖z_i^⊥‖_π ≤ (2rλ√μ)‖z_{i−1}^∥‖_π + (e^r λ)‖z_{i−1}^⊥‖_π ≤ (2rλ√μ)‖z_{i−1}^∥‖_π +
  √λ ‖z_{i−1}^⊥‖_π,

  where the last inequality holds when r ≤ (1/2)log(1/λ) i.e. e^r ≤ 1/√λ. Now let
  α_0 = ‖z_0^∥‖_π = 1 and β_0 = ‖z_0^⊥‖_π, and define for i ∈ [t],

  α_i = (1 + (e^r − 1)μ)α_{i−1} + (2r√μ)β_{i−1} and β_i = (2rλ√μ)α_{i−1} + √λ β_{i−1}.

  One can prove by induction that ‖z_i^∥‖_π ≤ α_i and ‖z_i^⊥‖_π ≤ β_i for every i
  ∈ [t], and α_i''s are strictly increasing. Therefore, bounding E[e^{rX}] = ‖z_t^∥‖_π
  ≤ α_t boils down to bounding the recurrence relation for α_i and β_i.

  One can show that β_i ≤ 2r(Σ_{j=0}^{i−1} √(λ^{j+2} μ))α_{i−1} + √(λ^i) β_0 for every
  i ∈ [t], by expanding the recurrence and using that α_i''s are increasing. Also,
  by substituting β_{i−1}, we get α_1 ≤ (1 + (e^r − 1)μ) + 2r√μ β_0 and α_i ≤ (1 +
  (e^r − 1)μ + 4r²√μ(Σ_{j=0}^{i−2} √(λ^{j+2} μ)))α_{i−1} + 2r√(λ^{i−1} μ) β_0 for
  every 2 ≤ i ≤ t. One can then show that

  α_t ≤ (1 + 8r√μ β_0/(1−λ))(1 + (e^r − 1)) ∏_{i=2}^{t} (1 + (e^r − 1)μ + 4r²√μ(Σ_{j=0}^{i−2}
  √(λ^{j+2} μ)))

  which can be further bounded by

  2 max{1, 8r√μ/(1−λ)} ‖φ‖_π exp{((e^r − 1) + 8r²/(1−λ))μt}

  through elementary analysis. Choosing r = min{1/2, log(1/λ)/2, 1 − √λ, (1−λ)δ/18}
  = (1−λ)δ/18, we complete the proof.'
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/perpendicular-component-operator]]'
- '[[concepts/total-weight-x]]'
- '[[concepts/parallel-component-operator]]'
- '[[concepts/chernoff-bound-for-markov-chains]]'
- '[[concepts/weight-function-f-i]]'
- '[[concepts/stationary-distribution-pi]]'
- '[[concepts/expected-weight-mu]]'
- '[[concepts/random-walk-v1-vt]]'
- '[[concepts/ergodic-markov-chains]]'
- '[[concepts/spectral-expansion-lambda-m]]'
- '[[concepts/pi-norm]]'
- '[[concepts/moment-generating-function-bound]]'
- '[[concepts/initial-distribution-phi]]'
- '[[concepts/weight-function-f-i]]'
- '[[concepts/parallel-component-operator]]'
- '[[concepts/ergodic-markov-chains]]'
- '[[concepts/stationary-distribution-pi]]'
- '[[concepts/moment-generating-function-bound]]'
- '[[concepts/spectral-expansion-lambda-m]]'
- '[[concepts/random-walk-v1-vt]]'
- '[[concepts/perpendicular-component-operator]]'
- '[[concepts/chernoff-bound-for-markov-chains]]'
- '[[concepts/total-weight-x]]'
- '[[concepts/pi-norm]]'
- '[[concepts/initial-distribution-phi]]'
- '[[concepts/expected-weight-mu]]'
about_meta:
- target: '[[concepts/perpendicular-component-operator]]'
  role: primary
  aspect: ''
- target: '[[concepts/total-weight-x]]'
  role: primary
  aspect: ''
- target: '[[concepts/parallel-component-operator]]'
  role: primary
  aspect: ''
- target: '[[concepts/chernoff-bound-for-markov-chains]]'
  role: primary
  aspect: ''
- target: '[[concepts/weight-function-f-i]]'
  role: primary
  aspect: ''
- target: '[[concepts/stationary-distribution-pi]]'
  role: primary
  aspect: ''
- target: '[[concepts/expected-weight-mu]]'
  role: primary
  aspect: ''
- target: '[[concepts/random-walk-v1-vt]]'
  role: primary
  aspect: ''
- target: '[[concepts/ergodic-markov-chains]]'
  role: primary
  aspect: ''
- target: '[[concepts/spectral-expansion-lambda-m]]'
  role: primary
  aspect: ''
- target: '[[concepts/pi-norm]]'
  role: primary
  aspect: ''
- target: '[[concepts/moment-generating-function-bound]]'
  role: primary
  aspect: ''
- target: '[[concepts/initial-distribution-phi]]'
  role: primary
  aspect: ''
- target: '[[concepts/weight-function-f-i]]'
  role: primary
  aspect: ''
- target: '[[concepts/parallel-component-operator]]'
  role: primary
  aspect: ''
- target: '[[concepts/ergodic-markov-chains]]'
  role: primary
  aspect: ''
- target: '[[concepts/stationary-distribution-pi]]'
  role: primary
  aspect: ''
- target: '[[concepts/moment-generating-function-bound]]'
  role: primary
  aspect: ''
- target: '[[concepts/spectral-expansion-lambda-m]]'
  role: primary
  aspect: ''
- target: '[[concepts/random-walk-v1-vt]]'
  role: primary
  aspect: ''
- target: '[[concepts/perpendicular-component-operator]]'
  role: primary
  aspect: ''
- target: '[[concepts/chernoff-bound-for-markov-chains]]'
  role: primary
  aspect: ''
- target: '[[concepts/total-weight-x]]'
  role: primary
  aspect: ''
- target: '[[concepts/pi-norm]]'
  role: primary
  aspect: ''
- target: '[[concepts/initial-distribution-phi]]'
  role: primary
  aspect: ''
- target: '[[concepts/expected-weight-mu]]'
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

# Claim 3.2

Let M be an ergodic Markov chain with state space [n], stationary distribution π, and spectral expansion λ = λ(M). Let (V_1, …, V_t) denote a t-step random walk on M starting from an initial distribution φ on [n], i.e., V_1 ~ φ. For every i ∈ [t], let f_i : [n] → [0,1] be a weight function at step i such that the expected weight E_{v~π}[f_i(v)] = μ for all i. Define the total weight of the walk (V_1, …, V_t) by X ≜ Σ_{i=1}^{t} f_i(V_i). There exists some constant c and a parameter r > 0 that depends only on λ and δ such that
1. E[e^{rX}]/e^{r(1+δ)μt} ≤ c‖φ‖_π exp(−δ²(1−λ)μt/36) for 0 ≤ δ ≤ 1, and c‖φ‖_π exp(−δ(1−λ)μt/36) for δ > 1.
2. E[e^{−rX}]/e^{−r(1−δ)μt} ≤ c‖φ‖_π exp(−δ²(1−λ)μt/36) for 0 ≤ δ ≤ 1.


## Proof

First, recall that E[e^{rX}] = ‖(φP_1 M P_2 ... M P_t)^∥‖_π = ‖(φP_1 M P_2 ... M P_t M)^∥‖_π = ‖(φ ∏_{i=1}^{t} (P_i M))^∥‖_π where the second equality comes from Lemma 5. Our choice of r is r = min{1/2, log(1/λ)/2, 1 − √λ, (1−λ)δ/18}. We trace the π-norm of both parallel and perpendicular components of the random walk for each application of P_i M. Let z_0 ≜ φ and z_i = z_{i−1} P_i M for i ∈ [t]. By triangle inequality and Lemma 5 and 6, for every i ∈ [t],
‖z_i^∥‖_π = ‖(z_{i−1} P_i M)^∥‖_π ≤ (1 + (e^r − 1)μ)‖z_{i−1}^∥‖_π + (2r√μ)‖z_{i−1}^⊥‖_π,
and similarly,
‖z_i^⊥‖_π ≤ (2rλ√μ)‖z_{i−1}^∥‖_π + (e^r λ)‖z_{i−1}^⊥‖_π ≤ (2rλ√μ)‖z_{i−1}^∥‖_π + √λ ‖z_{i−1}^⊥‖_π,
where the last inequality holds when r ≤ (1/2)log(1/λ) i.e. e^r ≤ 1/√λ. Now let α_0 = ‖z_0^∥‖_π = 1 and β_0 = ‖z_0^⊥‖_π, and define for i ∈ [t],
α_i = (1 + (e^r − 1)μ)α_{i−1} + (2r√μ)β_{i−1} and β_i = (2rλ√μ)α_{i−1} + √λ β_{i−1}.
One can prove by induction that ‖z_i^∥‖_π ≤ α_i and ‖z_i^⊥‖_π ≤ β_i for every i ∈ [t], and α_i's are strictly increasing. Therefore, bounding E[e^{rX}] = ‖z_t^∥‖_π ≤ α_t boils down to bounding the recurrence relation for α_i and β_i.
One can show that β_i ≤ 2r(Σ_{j=0}^{i−1} √(λ^{j+2} μ))α_{i−1} + √(λ^i) β_0 for every i ∈ [t], by expanding the recurrence and using that α_i's are increasing. Also, by substituting β_{i−1}, we get α_1 ≤ (1 + (e^r − 1)μ) + 2r√μ β_0 and α_i ≤ (1 + (e^r − 1)μ + 4r²√μ(Σ_{j=0}^{i−2} √(λ^{j+2} μ)))α_{i−1} + 2r√(λ^{i−1} μ) β_0 for every 2 ≤ i ≤ t. One can then show that
α_t ≤ (1 + 8r√μ β_0/(1−λ))(1 + (e^r − 1)) ∏_{i=2}^{t} (1 + (e^r − 1)μ + 4r²√μ(Σ_{j=0}^{i−2} √(λ^{j+2} μ)))
which can be further bounded by
2 max{1, 8r√μ/(1−λ)} ‖φ‖_π exp{((e^r − 1) + 8r²/(1−λ))μt}
through elementary analysis. Choosing r = min{1/2, log(1/λ)/2, 1 − √λ, (1−λ)δ/18} = (1−λ)δ/18, we complete the proof.
