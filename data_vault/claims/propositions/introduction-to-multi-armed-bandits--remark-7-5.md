---
slug: introduction-to-multi-armed-bandits--remark-7-5
label: Remark 7.5
claim_type: proposition
statement: Fake cost ĉ_t(e) is determined by the corresponding true cost c_t(e) and
  event Λ_{t,e} which does not depend on algorithm's actions. Therefore, fake costs
  are chosen by a (randomized) oblivious adversary. In particular, in order to apply
  Theorem 7.1 with a different algorithm ALG for online learning with experts, it
  suffices to have an upper bound on regret against an oblivious adversary.
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/semi-bandit-feedback]]'
- '[[concepts/fake-cost-function]]'
- '[[concepts/oblivious-adversary]]'
- '[[concepts/online-routing]]'
- '[[concepts/randomized-oblivious-adversary]]'
about_meta:
- target: '[[concepts/semi-bandit-feedback]]'
  role: primary
  aspect: ''
- target: '[[concepts/fake-cost-function]]'
  role: primary
  aspect: ''
- target: '[[concepts/oblivious-adversary]]'
  role: primary
  aspect: ''
- target: '[[concepts/online-routing]]'
  role: primary
  aspect: ''
- target: '[[concepts/randomized-oblivious-adversary]]'
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

# Remark 7.5

Fake cost ĉ_t(e) is determined by the corresponding true cost c_t(e) and event Λ_{t,e} which does not depend on algorithm's actions. Therefore, fake costs are chosen by a (randomized) oblivious adversary. In particular, in order to apply Theorem 7.1 with a different algorithm ALG for online learning with experts, it suffices to have an upper bound on regret against an oblivious adversary.
