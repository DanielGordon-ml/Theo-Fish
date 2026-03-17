---
slug: introduction-to-multi-armed-bandits--optimal-regret-bound-148
label: Optimal regret bound (148)
claim_type: theorem
statement: 'The optimal regret bound is in terms of (unknown) optimum OPT and budget
  B rather than time horizon T:


  OPT - E[REW] ≤ Õ(√(K · OPT) + OPT√(K/B)).


  This regret bound is essentially optimal for any given triple (K,B,T): no algorithm
  can achieve better regret, up to logarithmic factors, over all problem instances
  with these (K,B,T). More precisely, no algorithm can achieve regret Ω(min(OPT, reg)),
  where reg = √(K · OPT) + OPT√(K/B).'
proof: ''
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/bandits-with-knapsacks]]'
- '[[concepts/optimal-regret-bound-for-bwk]]'
- '[[concepts/number-of-arms-k]]'
- '[[concepts/budget-b]]'
- '[[concepts/optimum-opt]]'
about_meta:
- target: '[[concepts/bandits-with-knapsacks]]'
  role: primary
  aspect: ''
- target: '[[concepts/optimal-regret-bound-for-bwk]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-arms-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/budget-b]]'
  role: primary
  aspect: ''
- target: '[[concepts/optimum-opt]]'
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

# Optimal regret bound (148)

The optimal regret bound is in terms of (unknown) optimum OPT and budget B rather than time horizon T:

OPT - E[REW] ≤ Õ(√(K · OPT) + OPT√(K/B)).

This regret bound is essentially optimal for any given triple (K,B,T): no algorithm can achieve better regret, up to logarithmic factors, over all problem instances with these (K,B,T). More precisely, no algorithm can achieve regret Ω(min(OPT, reg)), where reg = √(K · OPT) + OPT√(K/B).
