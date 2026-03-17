---
slug: introduction-to-multi-armed-bandits--theorem-4-5
label: Theorem 4.5
claim_type: theorem
statement: 'Consider Lipschitz bandits with time horizon T. Optimizing over the choice
  of an ε-mesh, uniform discretization with algorithm ALG satisfying (52) attains
  regret


  𝔼[R(T)] ≤ inf_{ε>0, ε-mesh S} εT + c_{ALG} · √(|S| T log T).'
proof: ''
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/discretization-error]]'
- '[[concepts/lipschitz-bandits-problem]]'
- '[[concepts/bandit-algorithm-alg]]'
- '[[concepts/mesh]]'
- '[[concepts/expected-regret-r-t]]'
about_meta:
- target: '[[concepts/discretization-error]]'
  role: primary
  aspect: ''
- target: '[[concepts/lipschitz-bandits-problem]]'
  role: primary
  aspect: ''
- target: '[[concepts/bandit-algorithm-alg]]'
  role: primary
  aspect: ''
- target: '[[concepts/mesh]]'
  role: primary
  aspect: ''
- target: '[[concepts/expected-regret-r-t]]'
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

# Theorem 4.5

Consider Lipschitz bandits with time horizon T. Optimizing over the choice of an ε-mesh, uniform discretization with algorithm ALG satisfying (52) attains regret

𝔼[R(T)] ≤ inf_{ε>0, ε-mesh S} εT + c_{ALG} · √(|S| T log T).
