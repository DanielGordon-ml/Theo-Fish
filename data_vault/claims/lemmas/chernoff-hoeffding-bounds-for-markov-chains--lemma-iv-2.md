---
slug: chernoff-hoeffding-bounds-for-markov-chains--lemma-iv-2
label: Lemma IV.2
claim_type: lemma
statement: The spectral expansion of M' = I + Q/m satisfies λ(M') ≤ 1 − (1 − λ(C))/m
  for all sufficiently large m.
proof: The reversiblization of M' is R(M') = M̃'M' = (I + Q̃/m)(I + Q/m) = I + (Q̃
  + Q)/m + Q̃Q/m². The spectral gap of R(M') relates to that of the continuous-time
  reversiblization R(C) with generator Q̃Q. For large m, γ(R(M')) ≥ (1 − λ(C)²)/m
  (up to lower order terms), so λ(M') = √(1 − γ(R(M'))) ≤ 1 − (1 − λ(C))/m approximately.
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/spectral-expansion-lambda]]'
- '[[concepts/multiplicative-reversiblization]]'
- '[[concepts/markov-chain-m-prime]]'
- '[[concepts/generator-of-continuous-time-markov-chain]]'
about_meta:
- target: '[[concepts/spectral-expansion-lambda]]'
  role: primary
  aspect: ''
- target: '[[concepts/multiplicative-reversiblization]]'
  role: primary
  aspect: ''
- target: '[[concepts/markov-chain-m-prime]]'
  role: primary
  aspect: ''
- target: '[[concepts/generator-of-continuous-time-markov-chain]]'
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

# Lemma IV.2

The spectral expansion of M' = I + Q/m satisfies λ(M') ≤ 1 − (1 − λ(C))/m for all sufficiently large m.


## Proof

The reversiblization of M' is R(M') = M̃'M' = (I + Q̃/m)(I + Q/m) = I + (Q̃ + Q)/m + Q̃Q/m². The spectral gap of R(M') relates to that of the continuous-time reversiblization R(C) with generator Q̃Q. For large m, γ(R(M')) ≥ (1 − λ(C)²)/m (up to lower order terms), so λ(M') = √(1 − γ(R(M'))) ≤ 1 − (1 − λ(C))/m approximately.
