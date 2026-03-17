---
slug: introduction-to-multi-armed-bandits--experts-with-knapsacks-regret-bounds
label: Experts with knapsacks regret bounds
claim_type: theorem
statement: In the full-feedback version of BwK, the entire outcome matrix M_t is revealed
  after each round t. Essentially, one can achieve regret bound (148) with K replaced
  by log K using UcbBwK algorithm (Algorithm 3) with a slightly modified analysis.
  LagrangeBwK reduction achieves regret O(T/B) · √(T log(dKT)) if the primal algorithm
  ALG_1 is Hedge from Section 27.
proof: ''
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/hedge]]'
- '[[concepts/lagrangebwk]]'
- '[[concepts/experts-with-knapsacks]]'
- '[[concepts/regret]]'
- '[[concepts/ucbbwk]]'
- '[[concepts/full-feedback]]'
about_meta:
- target: '[[concepts/hedge]]'
  role: primary
  aspect: ''
- target: '[[concepts/lagrangebwk]]'
  role: primary
  aspect: ''
- target: '[[concepts/experts-with-knapsacks]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/ucbbwk]]'
  role: primary
  aspect: ''
- target: '[[concepts/full-feedback]]'
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

# Experts with knapsacks regret bounds

In the full-feedback version of BwK, the entire outcome matrix M_t is revealed after each round t. Essentially, one can achieve regret bound (148) with K replaced by log K using UcbBwK algorithm (Algorithm 3) with a slightly modified analysis. LagrangeBwK reduction achieves regret O(T/B) · √(T log(dKT)) if the primal algorithm ALG_1 is Hedge from Section 27.
