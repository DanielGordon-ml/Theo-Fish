---
slug: chernoff-hoeffding-bounds-for-markov-chains--lemma-iii-2
label: Lemma III.2
claim_type: lemma
statement: For each i ∈ [t], let Pi be the diagonal matrix where the j-th diagonal
  entry is e^{r·fi(j)} for j ∈ [n]. Then ‖(Pi − I)1‖_∞ ≤ e^r − 1 and ‖1^T(Pi − I)Π‖_∞
  ≤ (e^r − 1)μ_i, where 1 denotes the all-ones column vector.
proof: For the first part, ((Pi − I)1)(j) = e^{r·fi(j)} − 1 ≤ e^r − 1 since fi(j)
  ∈ [0,1]. For the second part, (1^T(Pi − I)Π)(j) = π(j)(e^{r·fi(j)} − 1) ≤ π(j)(e^r
  − 1)fi(j) using convexity of exponential, where the inequality e^{rx} − 1 ≤ (e^r
  − 1)x for x ∈ [0,1] is applied. Summing gives the bound (e^r − 1)μ_i.
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/function-f-i]]'
- '[[concepts/mean-mu]]'
- '[[concepts/diagonal-matrix-p-i]]'
about_meta:
- target: '[[concepts/function-f-i]]'
  role: primary
  aspect: ''
- target: '[[concepts/mean-mu]]'
  role: primary
  aspect: ''
- target: '[[concepts/diagonal-matrix-p-i]]'
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

# Lemma III.2

For each i ∈ [t], let Pi be the diagonal matrix where the j-th diagonal entry is e^{r·fi(j)} for j ∈ [n]. Then ‖(Pi − I)1‖_∞ ≤ e^r − 1 and ‖1^T(Pi − I)Π‖_∞ ≤ (e^r − 1)μ_i, where 1 denotes the all-ones column vector.


## Proof

For the first part, ((Pi − I)1)(j) = e^{r·fi(j)} − 1 ≤ e^r − 1 since fi(j) ∈ [0,1]. For the second part, (1^T(Pi − I)Π)(j) = π(j)(e^{r·fi(j)} − 1) ≤ π(j)(e^r − 1)fi(j) using convexity of exponential, where the inequality e^{rx} − 1 ≤ (e^r − 1)x for x ∈ [0,1] is applied. Summing gives the bound (e^r − 1)μ_i.
