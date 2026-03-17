---
slug: cooperative-multi-player-bandit-optimization--weakest-link-optimization-for-convergence-time
label: Weakest Link Optimization for Convergence Time
claim_type: proposition
statement: In Algorithm 1, one can choose ε_0 = min_{n,m} π_m^n, and 1/ε_0 appears
  in many of our bounds, implying that maximizing ε_0 = min_{n,m} π_m^n (the 'weakest
  link') will minimize the convergence time. Designing a communication protocol that
  maximizes min_{n,m} π_m^n involves equalizing the frequencies at which messages
  of different players are relayed, helping more remote players to be well represented.
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/convergence-time]]'
- '[[concepts/communication-protocol]]'
- '[[concepts/algorithm-1]]'
- '[[concepts/proper-communication-protocol]]'
- '[[concepts/weakest-link]]'
- '[[concepts/communication-probability-p-m-n]]'
- '[[concepts/epsilon-0]]'
about_meta:
- target: '[[concepts/convergence-time]]'
  role: primary
  aspect: ''
- target: '[[concepts/communication-protocol]]'
  role: primary
  aspect: ''
- target: '[[concepts/algorithm-1]]'
  role: primary
  aspect: ''
- target: '[[concepts/proper-communication-protocol]]'
  role: primary
  aspect: ''
- target: '[[concepts/weakest-link]]'
  role: primary
  aspect: ''
- target: '[[concepts/communication-probability-p-m-n]]'
  role: primary
  aspect: ''
- target: '[[concepts/epsilon-0]]'
  role: primary
  aspect: ''
depends_on: []
depends_on_meta: []
sourced_from:
- '[[sources/cooperative_multi_player_bandit_optimization|cooperative_multi_player_bandit_optimization]]'
sourced_from_meta:
- target: '[[sources/cooperative_multi_player_bandit_optimization|cooperative_multi_player_bandit_optimization]]'
  section: ''
  page: ''
  confidence: 0.0
---

# Weakest Link Optimization for Convergence Time

In Algorithm 1, one can choose ε_0 = min_{n,m} π_m^n, and 1/ε_0 appears in many of our bounds, implying that maximizing ε_0 = min_{n,m} π_m^n (the 'weakest link') will minimize the convergence time. Designing a communication protocol that maximizes min_{n,m} π_m^n involves equalizing the frequencies at which messages of different players are relayed, helping more remote players to be well represented.
