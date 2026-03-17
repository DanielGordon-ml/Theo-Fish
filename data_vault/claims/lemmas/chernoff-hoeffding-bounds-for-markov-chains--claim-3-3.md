---
slug: chernoff-hoeffding-bounds-for-markov-chains--claim-3-3
label: Claim 3.3
claim_type: lemma
statement: Let $x$ be an arbitrary initial distribution. Let $M$ be an ergodic Markov
  chain with stationary distribution $\pi$ and mixing time $T(\epsilon)$. We have
  $\|xM^{T(\epsilon)} - \pi\|_{TV} \le 2\epsilon \|x - \pi\|_{TV}$.
proof: The key idea for proving this claim is to split the difference $x - \pi$ into
  positive and negative components, and analyze $\|xM^{T(\epsilon)} - \pi\|_{TV} =
  \|(x - \pi)M^{T(\epsilon)}\|_{TV}$ using these components together with a rescaling
  to transform the components into probability distributions and then invoke the definition
  of mixing time. Details are available in the full version of this paper.
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/epsilon-mixing-time-t-epsilon]]'
- '[[concepts/total-variation-distance]]'
- '[[concepts/ergodic-markov-chains]]'
- '[[concepts/stationary-distribution-pi]]'
- '[[concepts/contraction-mapping]]'
about_meta:
- target: '[[concepts/epsilon-mixing-time-t-epsilon]]'
  role: primary
  aspect: ''
- target: '[[concepts/total-variation-distance]]'
  role: primary
  aspect: ''
- target: '[[concepts/ergodic-markov-chains]]'
  role: primary
  aspect: ''
- target: '[[concepts/stationary-distribution-pi]]'
  role: primary
  aspect: ''
- target: '[[concepts/contraction-mapping]]'
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

# Claim 3.3

Let $x$ be an arbitrary initial distribution. Let $M$ be an ergodic Markov chain with stationary distribution $\pi$ and mixing time $T(\epsilon)$. We have $\|xM^{T(\epsilon)} - \pi\|_{TV} \le 2\epsilon \|x - \pi\|_{TV}$.


## Proof

The key idea for proving this claim is to split the difference $x - \pi$ into positive and negative components, and analyze $\|xM^{T(\epsilon)} - \pi\|_{TV} = \|(x - \pi)M^{T(\epsilon)}\|_{TV}$ using these components together with a rescaling to transform the components into probability distributions and then invoke the definition of mixing time. Details are available in the full version of this paper.
