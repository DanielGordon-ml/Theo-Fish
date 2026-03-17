---
slug: chernoff-hoeffding-bounds-for-markov-chains--observation-on-spectral-expansion-1
label: Observation on spectral expansion 1
claim_type: lemma
statement: Let M' be an ergodic Markov chain with stationary distribution π'. If there
  exist two states v and v' such that (i) M'_{v,v'} = 1, i.e., state v leaves to state
  v' with probability 1, and (ii) M'_{u,v'} = 0 for all u ≠ v, i.e., the only state
  that transits to v' is v, then λ(M') = 1.
proof: Note that in this case, π'(v) = π'(v') since all probability mass from v leaves
  to v', which receives probability mass only from v. Consider a distribution x whose
  probability mass all concentrates at v, i.e., x_v = 1 and x_u = 0 for all u ≠ v.
  One step walk from x results in the distribution xM' whose probability mass all
  concentrates at v'. By definition, ||x||_{π'} = ||xM'||_{π'} and thus λ(M') = 1.
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/ergodic-markov-chains]]'
- '[[concepts/stationary-distribution-pi]]'
- '[[concepts/spectral-expansion-lambda-m]]'
- '[[concepts/pi-norm]]'
about_meta:
- target: '[[concepts/ergodic-markov-chains]]'
  role: primary
  aspect: ''
- target: '[[concepts/stationary-distribution-pi]]'
  role: primary
  aspect: ''
- target: '[[concepts/spectral-expansion-lambda-m]]'
  role: primary
  aspect: ''
- target: '[[concepts/pi-norm]]'
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

# Observation on spectral expansion 1

Let M' be an ergodic Markov chain with stationary distribution π'. If there exist two states v and v' such that (i) M'_{v,v'} = 1, i.e., state v leaves to state v' with probability 1, and (ii) M'_{u,v'} = 0 for all u ≠ v, i.e., the only state that transits to v' is v, then λ(M') = 1.


## Proof

Note that in this case, π'(v) = π'(v') since all probability mass from v leaves to v', which receives probability mass only from v. Consider a distribution x whose probability mass all concentrates at v, i.e., x_v = 1 and x_u = 0 for all u ≠ v. One step walk from x results in the distribution xM' whose probability mass all concentrates at v'. By definition, ||x||_{π'} = ||xM'||_{π'} and thus λ(M') = 1.
