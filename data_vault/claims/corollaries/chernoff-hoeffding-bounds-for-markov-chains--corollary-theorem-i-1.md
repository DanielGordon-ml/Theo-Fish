---
slug: chernoff-hoeffding-bounds-for-markov-chains--corollary-theorem-i-1
label: Corollary (Theorem I.1)
claim_type: corollary
statement: Under the same setting as Theorem I.1, for any δ > 0, Pr[X ≥ (1+δ)μ] ≤
  ‖φ/π‖_π · (e^δ/((1+δ)^{(1+δ)}))^{(1−λ(M))μ} and Pr[X ≤ (1−δ)μ] ≤ ‖φ/π‖_π · (e^{−δ}/((1−δ)^{(1−δ)}))^{(1−λ(M))μ}.
proof: By Markov's inequality, Pr[X ≥ (1+δ)μ] ≤ e^{−r(1+δ)μ} · E[e^{rX}] ≤ ‖φ/π‖_π
  · e^{−r(1+δ)μ} · (1 + (e^r − 1)μ/t)^{(1−λ)t}. Setting r = ln(1+δ) and using the
  inequality (1 + x/t)^t ≤ e^x gives the upper tail. The lower tail follows similarly
  by considering E[e^{−rX}].
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/norm-phi-pi]]'
- '[[concepts/total-weight-x]]'
- '[[concepts/chernoff-bound-for-markov-chains]]'
- '[[concepts/expected-weight-mu]]'
about_meta:
- target: '[[concepts/norm-phi-pi]]'
  role: primary
  aspect: ''
- target: '[[concepts/total-weight-x]]'
  role: primary
  aspect: ''
- target: '[[concepts/chernoff-bound-for-markov-chains]]'
  role: primary
  aspect: ''
- target: '[[concepts/expected-weight-mu]]'
  role: primary
  aspect: ''
depends_on:
- '[[claims/chernoff-hoeffding-bounds-for-markov-chains--theorem-iii-4]]'
depends_on_meta:
- target: '[[claims/chernoff-hoeffding-bounds-for-markov-chains--theorem-iii-4]]'
sourced_from:
- '[[sources/chernoff_hoeffding_bounds_for_markov_chains|chernoff_hoeffding_bounds_for_markov_chains]]'
sourced_from_meta:
- target: '[[sources/chernoff_hoeffding_bounds_for_markov_chains|chernoff_hoeffding_bounds_for_markov_chains]]'
  section: ''
  page: ''
  confidence: 0.0
---

# Corollary (Theorem I.1)

Under the same setting as Theorem I.1, for any δ > 0, Pr[X ≥ (1+δ)μ] ≤ ‖φ/π‖_π · (e^δ/((1+δ)^{(1+δ)}))^{(1−λ(M))μ} and Pr[X ≤ (1−δ)μ] ≤ ‖φ/π‖_π · (e^{−δ}/((1−δ)^{(1−δ)}))^{(1−λ(M))μ}.


## Proof

By Markov's inequality, Pr[X ≥ (1+δ)μ] ≤ e^{−r(1+δ)μ} · E[e^{rX}] ≤ ‖φ/π‖_π · e^{−r(1+δ)μ} · (1 + (e^r − 1)μ/t)^{(1−λ)t}. Setting r = ln(1+δ) and using the inequality (1 + x/t)^t ≤ e^x gives the upper tail. The lower tail follows similarly by considering E[e^{−rX}].
