---
slug: introduction-to-multi-armed-bandits--ucbbwk-reduction-regret-bound-eq-153
label: UcbBwK Reduction Regret Bound (Eq. 153)
claim_type: theorem
statement: Whenever Eq. (152) holds for some extension of stochastic bandits, one
  can define a version of UcbBwK algorithm which uses r̂(a) + rad_t(a) and ĉ_{t,i}
  − rad_t(a) as, resp., UCB on r(a) and LCB on c_i(a) in (150). Plugging (152) into
  the original analysis of UcbBwK yields OPT − E[REW] ≤ O(√(βT))(1 + OPT/B).
proof: ''
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/confidence-sum]]'
- '[[concepts/confidence-radius-rad-t]]'
- '[[concepts/optimum-opt]]'
- '[[concepts/budget-b]]'
- '[[concepts/ucbbwk]]'
- '[[concepts/bandits-with-knapsacks]]'
- '[[concepts/beta]]'
- '[[concepts/reduction]]'
about_meta:
- target: '[[concepts/confidence-sum]]'
  role: primary
  aspect: ''
- target: '[[concepts/confidence-radius-rad-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/optimum-opt]]'
  role: primary
  aspect: ''
- target: '[[concepts/budget-b]]'
  role: primary
  aspect: ''
- target: '[[concepts/ucbbwk]]'
  role: primary
  aspect: ''
- target: '[[concepts/bandits-with-knapsacks]]'
  role: primary
  aspect: ''
- target: '[[concepts/beta]]'
  role: primary
  aspect: ''
- target: '[[concepts/reduction]]'
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

# UcbBwK Reduction Regret Bound (Eq. 153)

Whenever Eq. (152) holds for some extension of stochastic bandits, one can define a version of UcbBwK algorithm which uses r̂(a) + rad_t(a) and ĉ_{t,i} − rad_t(a) as, resp., UCB on r(a) and LCB on c_i(a) in (150). Plugging (152) into the original analysis of UcbBwK yields OPT − E[REW] ≤ O(√(βT))(1 + OPT/B).
