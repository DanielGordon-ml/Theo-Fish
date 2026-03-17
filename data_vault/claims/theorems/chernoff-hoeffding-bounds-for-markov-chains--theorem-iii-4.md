---
slug: chernoff-hoeffding-bounds-for-markov-chains--theorem-iii-4
label: Theorem III.4
claim_type: theorem
statement: Under the same setting as Theorem III.1, for any r > 0, E[e^{rX}] ≤ ‖φ/π‖_π
  · (1 + (e^r − 1)μ/t)^{(1−λ)t}.
proof: 'This follows from Theorem III.1 by AM-GM inequality: ∏_{i=1}^{t}(1 + (e^r
  − 1)μ_i)^{1−λ} ≤ ((1/t)Σ_{i=1}^{t}(1 + (e^r − 1)μ_i))^{(1−λ)t} = (1 + (e^r − 1)μ/t)^{(1−λ)t}.'
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/spectral-expansion-lambda-m]]'
- '[[concepts/total-weight-x]]'
- '[[concepts/moment-generating-function-bound]]'
- '[[concepts/norm-phi-pi]]'
- '[[concepts/ergodic-markov-chains]]'
about_meta:
- target: '[[concepts/spectral-expansion-lambda-m]]'
  role: primary
  aspect: ''
- target: '[[concepts/total-weight-x]]'
  role: primary
  aspect: ''
- target: '[[concepts/moment-generating-function-bound]]'
  role: primary
  aspect: ''
- target: '[[concepts/norm-phi-pi]]'
  role: primary
  aspect: ''
- target: '[[concepts/ergodic-markov-chains]]'
  role: primary
  aspect: ''
depends_on:
- '[[claims/chernoff-hoeffding-bounds-for-markov-chains--lemma-ii-4]]'
depends_on_meta:
- target: '[[claims/chernoff-hoeffding-bounds-for-markov-chains--lemma-ii-4]]'
sourced_from:
- '[[sources/chernoff_hoeffding_bounds_for_markov_chains|chernoff_hoeffding_bounds_for_markov_chains]]'
sourced_from_meta:
- target: '[[sources/chernoff_hoeffding_bounds_for_markov_chains|chernoff_hoeffding_bounds_for_markov_chains]]'
  section: ''
  page: ''
  confidence: 0.0
---

# Theorem III.4

Under the same setting as Theorem III.1, for any r > 0, E[e^{rX}] ≤ ‖φ/π‖_π · (1 + (e^r − 1)μ/t)^{(1−λ)t}.


## Proof

This follows from Theorem III.1 by AM-GM inequality: ∏_{i=1}^{t}(1 + (e^r − 1)μ_i)^{1−λ} ≤ ((1/t)Σ_{i=1}^{t}(1 + (e^r − 1)μ_i))^{(1−λ)t} = (1 + (e^r − 1)μ/t)^{(1−λ)t}.
