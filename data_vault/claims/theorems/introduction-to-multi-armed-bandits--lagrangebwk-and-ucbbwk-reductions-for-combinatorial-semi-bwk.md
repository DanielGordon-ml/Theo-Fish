---
slug: introduction-to-multi-armed-bandits--lagrangebwk-and-ucbbwk-reductions-for-combinatorial-semi-bwk
label: LagrangeBwK and UcbBwK reductions for combinatorial semi-BwK
claim_type: theorem
statement: Both reductions from Section 59.1 apply to combinatorial semi-bandits with
  knapsacks. LagrangeBwK reduction achieves regret Õ(T/B)√(mT) (Immorlica et al.,
  2022). UcbBwK reduction achieves regret Õ(m√T)(1 + OPT/B) via a computationally
  inefficient algorithm (Sankararaman and Slivkins, 2021).
proof: ''
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/regret]]'
- '[[concepts/combinatorial-semi-bandits-with-knapsacks]]'
- '[[concepts/ucbbwk]]'
- '[[concepts/lagrangebwk]]'
about_meta:
- target: '[[concepts/regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/combinatorial-semi-bandits-with-knapsacks]]'
  role: primary
  aspect: ''
- target: '[[concepts/ucbbwk]]'
  role: primary
  aspect: ''
- target: '[[concepts/lagrangebwk]]'
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

# LagrangeBwK and UcbBwK reductions for combinatorial semi-BwK

Both reductions from Section 59.1 apply to combinatorial semi-bandits with knapsacks. LagrangeBwK reduction achieves regret Õ(T/B)√(mT) (Immorlica et al., 2022). UcbBwK reduction achieves regret Õ(m√T)(1 + OPT/B) via a computationally inefficient algorithm (Sankararaman and Slivkins, 2021).
