---
slug: introduction-to-multi-armed-bandits--lagrangebwk-reduction-regret-bound-eq-151
label: LagrangeBwK Reduction Regret Bound (Eq. 151)
claim_type: theorem
statement: LagrangeBwK takes an arbitrary "primal" algorithm ALG_1, and turns it into
  an algorithm for BwK. Algorithm ALG_1 should achieve a high-probability bound on
  its "adversarial regret" R_1(·) (provided that per-round rewards/costs lie in [0,1]).
  Then with probability at least 1−δ one has OPT − REW ≤ O(T/B) · (R_1(T) + √(TK ln(dT/δ))).
proof: ''
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/lagrangebwk]]'
- '[[concepts/number-of-arms-k]]'
- '[[concepts/time-horizon-t]]'
- '[[concepts/number-of-resources-d]]'
- '[[concepts/bandits-with-knapsacks]]'
- '[[concepts/alg1]]'
- '[[concepts/adversarial-regret-r1]]'
- '[[concepts/reduction]]'
- '[[concepts/budget-b]]'
about_meta:
- target: '[[concepts/lagrangebwk]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-arms-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/time-horizon-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-resources-d]]'
  role: primary
  aspect: ''
- target: '[[concepts/bandits-with-knapsacks]]'
  role: primary
  aspect: ''
- target: '[[concepts/alg1]]'
  role: primary
  aspect: ''
- target: '[[concepts/adversarial-regret-r1]]'
  role: primary
  aspect: ''
- target: '[[concepts/reduction]]'
  role: primary
  aspect: ''
- target: '[[concepts/budget-b]]'
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

# LagrangeBwK Reduction Regret Bound (Eq. 151)

LagrangeBwK takes an arbitrary "primal" algorithm ALG_1, and turns it into an algorithm for BwK. Algorithm ALG_1 should achieve a high-probability bound on its "adversarial regret" R_1(·) (provided that per-round rewards/costs lie in [0,1]). Then with probability at least 1−δ one has OPT − REW ≤ O(T/B) · (R_1(T) + √(TK ln(dT/δ))).
