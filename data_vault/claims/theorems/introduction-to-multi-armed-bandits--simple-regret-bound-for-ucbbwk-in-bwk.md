---
slug: introduction-to-multi-armed-bandits--simple-regret-bound-for-ucbbwk-in-bwk
label: Simple regret bound for UcbBwK in BwK
claim_type: theorem
statement: Simple regret for BwK is defined, for a given round t, as OPT/T - r(X_t),
  where X_t is the distribution over arms chosen by the algorithm in this round. Simple
  regret can be at least ε in at most Õ(K/ε²) rounds, for all ε > 0 simultaneously.
  This is achieved by UcbBwK algorithm, along with the worst-case and logarithmic
  regret bounds. This holds if B > Ω(T) ≫ K, without any other assumptions.
proof: ''
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/number-of-arms-k]]'
- '[[concepts/simple-regret]]'
- '[[concepts/bandits-with-knapsacks]]'
- '[[concepts/ucbbwk-algorithm]]'
about_meta:
- target: '[[concepts/number-of-arms-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/simple-regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/bandits-with-knapsacks]]'
  role: primary
  aspect: ''
- target: '[[concepts/ucbbwk-algorithm]]'
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

# Simple regret bound for UcbBwK in BwK

Simple regret for BwK is defined, for a given round t, as OPT/T - r(X_t), where X_t is the distribution over arms chosen by the algorithm in this round. Simple regret can be at least ε in at most Õ(K/ε²) rounds, for all ε > 0 simultaneously. This is achieved by UcbBwK algorithm, along with the worst-case and logarithmic regret bounds. This holds if B > Ω(T) ≫ K, without any other assumptions.
