---
slug: introduction-to-multi-armed-bandits--lemma-10-13
label: Lemma 10.13
claim_type: lemma
statement: 'For an arbitrary $\mathtt{BwK}$ algorithm $\mathtt{ALG}$,


  $\mathtt{REW}(\mathtt{ALG})\geq\tau\cdot\mathcal{L}(\bar{a}_{\tau},i)+(T-\tau)\cdot\mathtt{OPT}_{\mathtt{LP}}-\mathtt{err}^{*}_{\tau,i},$


  where $\mathtt{err}^{*}_{\tau,i}:=\left|\tau\cdot r(\bar{a}_{\tau})-\sum_{t\in[\tau]}r_{t}\right|+\tfrac{T}{B}\,\left|\tau\cdot
  c_{i}(\bar{a}_{\tau})-\sum_{t\in[\tau]}c_{i,t}\right|$ is the error term.'
proof: 'Note that $\sum_{t\in[\tau]}c_{t,i}>B$ because of the stopping. Then:


  $\tau\cdot\mathcal{L}(\bar{a}_{\tau},i) =\tau\cdot\left(r(\bar{a})+1-\tfrac{T}{B}c_{i}(\bar{a})\right)
  \leq\sum_{t\in[\tau]}r_{t}+\tau-\tfrac{T}{B}\sum_{t\in[\tau]}c_{i,t}+\mathtt{err}^{*}_{\tau,i}
  \leq\mathtt{REW}+\tau-T+\mathtt{err}^{*}_{\tau,i}.$


  The Lemma follows since $\mathtt{OPT}_{\mathtt{LP}}\leq 1$.'
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/bandits-with-knapsacks]]'
- '[[concepts/adjusted-total-reward]]'
- '[[concepts/stopping-time]]'
- '[[concepts/lagrange-game]]'
about_meta:
- target: '[[concepts/bandits-with-knapsacks]]'
  role: primary
  aspect: ''
- target: '[[concepts/adjusted-total-reward]]'
  role: primary
  aspect: ''
- target: '[[concepts/stopping-time]]'
  role: primary
  aspect: ''
- target: '[[concepts/lagrange-game]]'
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

# Lemma 10.13

For an arbitrary $\mathtt{BwK}$ algorithm $\mathtt{ALG}$,

$\mathtt{REW}(\mathtt{ALG})\geq\tau\cdot\mathcal{L}(\bar{a}_{\tau},i)+(T-\tau)\cdot\mathtt{OPT}_{\mathtt{LP}}-\mathtt{err}^{*}_{\tau,i},$

where $\mathtt{err}^{*}_{\tau,i}:=\left|\tau\cdot r(\bar{a}_{\tau})-\sum_{t\in[\tau]}r_{t}\right|+\tfrac{T}{B}\,\left|\tau\cdot c_{i}(\bar{a}_{\tau})-\sum_{t\in[\tau]}c_{i,t}\right|$ is the error term.


## Proof

Note that $\sum_{t\in[\tau]}c_{t,i}>B$ because of the stopping. Then:

$\tau\cdot\mathcal{L}(\bar{a}_{\tau},i) =\tau\cdot\left(r(\bar{a})+1-\tfrac{T}{B}c_{i}(\bar{a})\right) \leq\sum_{t\in[\tau]}r_{t}+\tau-\tfrac{T}{B}\sum_{t\in[\tau]}c_{i,t}+\mathtt{err}^{*}_{\tau,i} \leq\mathtt{REW}+\tau-T+\mathtt{err}^{*}_{\tau,i}.$

The Lemma follows since $\mathtt{OPT}_{\mathtt{LP}}\leq 1$.
