---
slug: introduction-to-multi-armed-bandits--claim-6-5
label: Claim 6.5
claim_type: lemma
statement: Eq. (88) holds if $q_{t}(a_{t,e})>0$ for each expert $e$.
proof: 'Let us argue about each arm $a$ separately. If $q_{t}(a)>0$ then

  $$\operatorname{\mathbb{E}}[\widehat{c}_{t}(a)\mid\vec{p}_{t}]=\Pr[a_{t}=a\mid\vec{p}_{t}]\cdot\frac{c_{t}(a_{t})}{q_{t}(a)}+\Pr[a_{t}\neq
  a\mid\vec{p}_{t}]\cdot 0=c_{t}(a).$$

  For a given expert $e$ plug in arm $a=a_{t,e}$, its choice in round $t$.'
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/fake-cost-function-on-arm]]'
- '[[concepts/arm-selection-distribution]]'
- '[[concepts/unbiasedness]]'
- '[[concepts/fake-cost-function-on-expert]]'
- '[[concepts/inverse-propensity-scoring-estimator]]'
about_meta:
- target: '[[concepts/fake-cost-function-on-arm]]'
  role: primary
  aspect: ''
- target: '[[concepts/arm-selection-distribution]]'
  role: primary
  aspect: ''
- target: '[[concepts/unbiasedness]]'
  role: primary
  aspect: ''
- target: '[[concepts/fake-cost-function-on-expert]]'
  role: primary
  aspect: ''
- target: '[[concepts/inverse-propensity-scoring-estimator]]'
  role: primary
  aspect: ''
depends_on: []
depends_on_meta: []
sourced_from:
- '[[sources/1904.07272|Introduction to Multi-Armed Bandits]]'
sourced_from_meta:
- target: '[[sources/1904.07272|Introduction to Multi-Armed Bandits]]'
  section: ''
  page: ''
  confidence: 0.0
---

# Claim 6.5

Eq. (88) holds if $q_{t}(a_{t,e})>0$ for each expert $e$.


## Proof

Let us argue about each arm $a$ separately. If $q_{t}(a)>0$ then
$$\operatorname{\mathbb{E}}[\widehat{c}_{t}(a)\mid\vec{p}_{t}]=\Pr[a_{t}=a\mid\vec{p}_{t}]\cdot\frac{c_{t}(a_{t})}{q_{t}(a)}+\Pr[a_{t}\neq a\mid\vec{p}_{t}]\cdot 0=c_{t}(a).$$
For a given expert $e$ plug in arm $a=a_{t,e}$, its choice in round $t$.
