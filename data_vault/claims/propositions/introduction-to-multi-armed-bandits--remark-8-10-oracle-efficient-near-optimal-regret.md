---
slug: introduction-to-multi-armed-bandits--remark-8-10-oracle-efficient-near-optimal-regret
label: Remark 8.10 (oracle-efficient near-optimal regret)
claim_type: proposition
statement: 'A near-optimal regret bound can in fact be achieved with an oracle-efficient
  algorithm: one that makes only a small number of oracle calls. Specifically, one
  can achieve regret $O(\sqrt{KT\log(T|\Pi|)})$ with only $\tilde{O}(\sqrt{KT/\log|\Pi|})$
  oracle calls across all $T$ rounds.'
proof: ''
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/computationally-efficient]]'
- '[[concepts/classification-oracle]]'
- '[[concepts/contextual-bandits-with-fixed-policy-class]]'
- '[[concepts/policy-class-pi]]'
- '[[concepts/regret-relative-to-policy-class-pi-r-pi-t]]'
about_meta:
- target: '[[concepts/computationally-efficient]]'
  role: primary
  aspect: ''
- target: '[[concepts/classification-oracle]]'
  role: primary
  aspect: ''
- target: '[[concepts/contextual-bandits-with-fixed-policy-class]]'
  role: primary
  aspect: ''
- target: '[[concepts/policy-class-pi]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret-relative-to-policy-class-pi-r-pi-t]]'
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

# Remark 8.10 (oracle-efficient near-optimal regret)

A near-optimal regret bound can in fact be achieved with an oracle-efficient algorithm: one that makes only a small number of oracle calls. Specifically, one can achieve regret $O(\sqrt{KT\log(T|\Pi|)})$ with only $\tilde{O}(\sqrt{KT/\log|\Pi|})$ oracle calls across all $T$ rounds.
