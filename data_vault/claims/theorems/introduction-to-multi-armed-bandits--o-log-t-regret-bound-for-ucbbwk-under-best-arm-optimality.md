---
slug: introduction-to-multi-armed-bandits--o-log-t-regret-bound-for-ucbbwk-under-best-arm-optimality
label: O(log T) regret bound for UcbBwK under best-arm-optimality
claim_type: theorem
statement: Assuming d=2 and best-arm optimality, O(log T) regret against OPT_FD is
  achievable with UcbBwK algorithm. In particular, the algorithm does not know in
  advance whether best-arm-optimality holds, and attains the optimal worst-case regret
  bound for all instances, best-arm-optimal or not. The Lagrangian gap of arm a is
  defined as G_LAG(a) := OPT_LP - L(a, λ*), where λ* is a minimizer dual vector, and
  G_LAG := min_{a not in {a*, null}} G_LAG(a). The regret bound scales as O(K G_LAG^{-1}
  log T), which is optimal in G_LAG, under a mild additional assumption that the expected
  consumption of the best arm is not very close to B/T. Otherwise, regret is O(K G_LAG^{-2}
  log T).
proof: ''
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/number-of-arms-k]]'
- '[[concepts/opt-fd]]'
- '[[concepts/ucbbwk-algorithm]]'
- '[[concepts/opt-lp]]'
- '[[concepts/best-arm-optimality]]'
- '[[concepts/lagrangian-gap]]'
- '[[concepts/bandits-with-knapsacks]]'
about_meta:
- target: '[[concepts/number-of-arms-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/opt-fd]]'
  role: primary
  aspect: ''
- target: '[[concepts/ucbbwk-algorithm]]'
  role: primary
  aspect: ''
- target: '[[concepts/opt-lp]]'
  role: primary
  aspect: ''
- target: '[[concepts/best-arm-optimality]]'
  role: primary
  aspect: ''
- target: '[[concepts/lagrangian-gap]]'
  role: primary
  aspect: ''
- target: '[[concepts/bandits-with-knapsacks]]'
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

# O(log T) regret bound for UcbBwK under best-arm-optimality

Assuming d=2 and best-arm optimality, O(log T) regret against OPT_FD is achievable with UcbBwK algorithm. In particular, the algorithm does not know in advance whether best-arm-optimality holds, and attains the optimal worst-case regret bound for all instances, best-arm-optimal or not. The Lagrangian gap of arm a is defined as G_LAG(a) := OPT_LP - L(a, λ*), where λ* is a minimizer dual vector, and G_LAG := min_{a not in {a*, null}} G_LAG(a). The regret bound scales as O(K G_LAG^{-1} log T), which is optimal in G_LAG, under a mild additional assumption that the expected consumption of the best arm is not very close to B/T. Otherwise, regret is O(K G_LAG^{-2} log T).
