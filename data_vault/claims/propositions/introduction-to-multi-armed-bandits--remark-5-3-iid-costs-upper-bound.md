---
slug: introduction-to-multi-armed-bandits--remark-5-3-iid-costs-upper-bound
label: Remark 5.3 (IID costs upper bound)
claim_type: proposition
statement: Consider the special case when the adversary chooses the cost $c_{t}(a)\in[0,1]$
  of each arm $a$ from some fixed distribution $\mathcal{D}_{a}$, same for all rounds
  $t$. With full feedback, playing arm with the lowest average cost achieves regret
  $O\left(\sqrt{T\log\left(KT\right)}\right)$.
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/time-horizon-t]]'
- '[[concepts/full-feedback]]'
- '[[concepts/confidence-radius]]'
- '[[concepts/iid-costs]]'
- '[[concepts/regret]]'
- '[[concepts/number-of-arms-k]]'
about_meta:
- target: '[[concepts/time-horizon-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/full-feedback]]'
  role: primary
  aspect: ''
- target: '[[concepts/confidence-radius]]'
  role: primary
  aspect: ''
- target: '[[concepts/iid-costs]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-arms-k]]'
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

# Remark 5.3 (IID costs upper bound)

Consider the special case when the adversary chooses the cost $c_{t}(a)\in[0,1]$ of each arm $a$ from some fixed distribution $\mathcal{D}_{a}$, same for all rounds $t$. With full feedback, playing arm with the lowest average cost achieves regret $O\left(\sqrt{T\log\left(KT\right)}\right)$.
