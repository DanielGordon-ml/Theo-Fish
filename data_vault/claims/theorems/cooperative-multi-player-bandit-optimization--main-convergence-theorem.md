---
slug: cooperative-multi-player-bandit-optimization--main-convergence-theorem
label: Main Convergence Theorem
claim_type: theorem
statement: We prove that even if at every turn players take actions based only on
  the small random subset of the players' rewards that they know, our algorithm converges
  with probability 1 to the set of stationary points of (projected) gradient ascent
  on the sum of rewards function.
proof: ''
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/projected-gradient-ascent]]'
- '[[concepts/bandit-feedback]]'
- '[[concepts/communication-graph-process]]'
- '[[concepts/ergodic-markov-chain]]'
- '[[concepts/distributed-learning-algorithm]]'
- '[[concepts/twice-continuously-differentiable]]'
- '[[concepts/sum-of-rewards-function]]'
- '[[concepts/compact]]'
- '[[concepts/set-of-kkt-stationary-points]]'
- '[[concepts/convex]]'
about_meta:
- target: '[[concepts/projected-gradient-ascent]]'
  role: primary
  aspect: ''
- target: '[[concepts/bandit-feedback]]'
  role: primary
  aspect: ''
- target: '[[concepts/communication-graph-process]]'
  role: primary
  aspect: ''
- target: '[[concepts/ergodic-markov-chain]]'
  role: primary
  aspect: ''
- target: '[[concepts/distributed-learning-algorithm]]'
  role: primary
  aspect: ''
- target: '[[concepts/twice-continuously-differentiable]]'
  role: primary
  aspect: ''
- target: '[[concepts/sum-of-rewards-function]]'
  role: primary
  aspect: ''
- target: '[[concepts/compact]]'
  role: primary
  aspect: ''
- target: '[[concepts/set-of-kkt-stationary-points]]'
  role: primary
  aspect: ''
- target: '[[concepts/convex]]'
  role: primary
  aspect: ''
depends_on:
- '[[claims/cooperative-multi-player-bandit-optimization--gradient-estimation-via-random-perturbation]]'
depends_on_meta:
- target: '[[claims/cooperative-multi-player-bandit-optimization--gradient-estimation-via-random-perturbation]]'
sourced_from:
- '[[sources/cooperative_multi_player_bandit_optimization|cooperative_multi_player_bandit_optimization]]'
sourced_from_meta:
- target: '[[sources/cooperative_multi_player_bandit_optimization|cooperative_multi_player_bandit_optimization]]'
  section: ''
  page: ''
  confidence: 0.0
---

# Main Convergence Theorem

We prove that even if at every turn players take actions based only on the small random subset of the players' rewards that they know, our algorithm converges with probability 1 to the set of stationary points of (projected) gradient ascent on the sum of rewards function.
