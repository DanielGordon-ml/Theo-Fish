---
slug: introduction-to-multi-armed-bandits--generalized-resources-bwk-regret-bound
label: Generalized resources BwK regret bound
claim_type: theorem
statement: Agrawal and Devanur (2014, 2019) consider a version of BwK with a more
  abstract version of resources. The total reward is T·f(ō_T) for an arbitrary Lipschitz
  concave function f:[0,1]^d → [0,1], resource constraints expressed by an arbitrary
  convex set S ⊂ [0,1]^d which ō_T must belong to, and they allow soft constraints.
  They obtain regret bounds that scale as √T, with distance between ō_t and S scaling
  as 1/√T. Their results extend to the hard-constraint version by rescaling the budgets,
  as long as the constraint set S is downward closed.
proof: ''
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/regret]]'
- '[[concepts/bandits-with-knapsacks]]'
- '[[concepts/bwk-generalized-resources]]'
about_meta:
- target: '[[concepts/regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/bandits-with-knapsacks]]'
  role: primary
  aspect: ''
- target: '[[concepts/bwk-generalized-resources]]'
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

# Generalized resources BwK regret bound

Agrawal and Devanur (2014, 2019) consider a version of BwK with a more abstract version of resources. The total reward is T·f(ō_T) for an arbitrary Lipschitz concave function f:[0,1]^d → [0,1], resource constraints expressed by an arbitrary convex set S ⊂ [0,1]^d which ō_T must belong to, and they allow soft constraints. They obtain regret bounds that scale as √T, with distance between ō_t and S scaling as 1/√T. Their results extend to the hard-constraint version by rescaling the budgets, as long as the constraint set S is downward closed.
