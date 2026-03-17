---
slug: introduction-to-multi-armed-bandits--remark-5-3-iid-costs-lower-bound
label: Remark 5.3 (IID costs lower bound)
claim_type: proposition
statement: Consider the special case when the adversary chooses the cost $c_{t}(a)\in[0,1]$
  of each arm $a$ from some fixed distribution $\mathcal{D}_{a}$, same for all rounds
  $t$. With full feedback, there is a lower regret bound $\Omega(\sqrt{T}+\log K)$.
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/iid-costs]]'
- '[[concepts/number-of-arms-k]]'
- '[[concepts/lower-bound-on-regret]]'
- '[[concepts/full-feedback]]'
- '[[concepts/time-horizon-t]]'
about_meta:
- target: '[[concepts/iid-costs]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-arms-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/lower-bound-on-regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/full-feedback]]'
  role: primary
  aspect: ''
- target: '[[concepts/time-horizon-t]]'
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

# Remark 5.3 (IID costs lower bound)

Consider the special case when the adversary chooses the cost $c_{t}(a)\in[0,1]$ of each arm $a$ from some fixed distribution $\mathcal{D}_{a}$, same for all rounds $t$. With full feedback, there is a lower regret bound $\Omega(\sqrt{T}+\log K)$.
