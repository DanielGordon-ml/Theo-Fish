---
slug: distributed-multi-player-bandits-a-game-of-thrones-approach--algorithm-1-got-algorithm
label: Algorithm 1 (GoT Algorithm)
claim_type: algorithm
statement: 'Initialization - Set o_{n,i} = 0 and s_{n,i}(0) = 0 for all i. Set δ >
  0, 0 < ρ < 1 and ε > 0. Define k_T as the index of the last epoch where the horizon
  is T.


  For each epoch k = 1, ..., k_T


  1. Exploration Phase - for the next c_1 turns

  (a) Sample an arm i uniformly at random from all K arms.

  (b) Receive r_{n,i}(t) and set η_i(a(t)) = 0 if r_{n,i}(t) = 0 and η_i(a(t)) = 1
  otherwise.

  (c) If η_i(a(t)) = 1 then update o_{n,i} = o_{n,i} + 1 and s_{n,i}(t) = s_{n,i}(t-1)
  + r_{n,i}(t).

  (d) Estimate the expectation of the arm i by μ_{n,i}^k = s_{n,i}(t) / o_{n,i}, for
  each i = 1, ..., K.


  2. GoT Phase - for the next c_2 k^{1+δ} turns, play according to Algorithm 2 with
  ε and ρ

  (a) Starting from the d_g = ⌈ρ c_2 k^{1+δ}⌉-th turn inside the GoT Phase, keep track
  on the number of times each action was played that resulted in being content

  F_t^n(i) = Σ_{l=d_g}^{c_2 k^{1+δ}} I(a_n(l) = i, M_n(l) = C)

  where I is the indicator function.


  3. Exploitation Phase - for the next c_3 2^k turns, play

  a_n^k = argmax_i F_t^n(i)


  End'
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/k-t]]'
- '[[concepts/c1]]'
- '[[concepts/exploitation-phase]]'
- '[[concepts/indicator-function]]'
- '[[concepts/epoch-index]]'
- '[[concepts/c2]]'
- '[[concepts/content-action-count]]'
- '[[concepts/exploration-phase]]'
- '[[concepts/got-phase]]'
- '[[concepts/delta]]'
- '[[concepts/collision-indicator-function-for-arm-a-n]]'
- '[[concepts/epoch]]'
- '[[concepts/multi-player-multi-armed-bandit-game]]'
- '[[concepts/estimated-expected-reward-of-arm-a-n-for-player-n-at-epoch-k]]'
- '[[concepts/exploration-exploitation-tradeoff]]'
- '[[concepts/empirical-mean-estimator]]'
- '[[concepts/algorithm-2]]'
- '[[concepts/argmax-action-selector]]'
- '[[concepts/no-communication]]'
- '[[concepts/rho]]'
- '[[concepts/c3]]'
- '[[concepts/epsilon]]'
- '[[concepts/got-algorithm]]'
- '[[concepts/fully-distributed-multi-player-multi-armed-bandit-algorithm]]'
about_meta:
- target: '[[concepts/k-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/c1]]'
  role: primary
  aspect: ''
- target: '[[concepts/exploitation-phase]]'
  role: primary
  aspect: ''
- target: '[[concepts/indicator-function]]'
  role: primary
  aspect: ''
- target: '[[concepts/epoch-index]]'
  role: primary
  aspect: ''
- target: '[[concepts/c2]]'
  role: primary
  aspect: ''
- target: '[[concepts/content-action-count]]'
  role: primary
  aspect: ''
- target: '[[concepts/exploration-phase]]'
  role: primary
  aspect: ''
- target: '[[concepts/got-phase]]'
  role: primary
  aspect: ''
- target: '[[concepts/delta]]'
  role: primary
  aspect: ''
- target: '[[concepts/collision-indicator-function-for-arm-a-n]]'
  role: primary
  aspect: ''
- target: '[[concepts/epoch]]'
  role: primary
  aspect: ''
- target: '[[concepts/multi-player-multi-armed-bandit-game]]'
  role: primary
  aspect: ''
- target: '[[concepts/estimated-expected-reward-of-arm-a-n-for-player-n-at-epoch-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/exploration-exploitation-tradeoff]]'
  role: primary
  aspect: ''
- target: '[[concepts/empirical-mean-estimator]]'
  role: primary
  aspect: ''
- target: '[[concepts/algorithm-2]]'
  role: primary
  aspect: ''
- target: '[[concepts/argmax-action-selector]]'
  role: primary
  aspect: ''
- target: '[[concepts/no-communication]]'
  role: primary
  aspect: ''
- target: '[[concepts/rho]]'
  role: primary
  aspect: ''
- target: '[[concepts/c3]]'
  role: primary
  aspect: ''
- target: '[[concepts/epsilon]]'
  role: primary
  aspect: ''
- target: '[[concepts/got-algorithm]]'
  role: primary
  aspect: ''
- target: '[[concepts/fully-distributed-multi-player-multi-armed-bandit-algorithm]]'
  role: primary
  aspect: ''
depends_on: []
depends_on_meta: []
sourced_from:
- '[[sources/distributed_multi_player_bandits_a_game_of_thrones_approach|distributed_multi_player_bandits_a_game_of_thrones_approach]]'
sourced_from_meta:
- target: '[[sources/distributed_multi_player_bandits_a_game_of_thrones_approach|distributed_multi_player_bandits_a_game_of_thrones_approach]]'
  section: ''
  page: ''
  confidence: 0.0
---

# Algorithm 1 (GoT Algorithm)

Initialization - Set o_{n,i} = 0 and s_{n,i}(0) = 0 for all i. Set δ > 0, 0 < ρ < 1 and ε > 0. Define k_T as the index of the last epoch where the horizon is T.

For each epoch k = 1, ..., k_T

1. Exploration Phase - for the next c_1 turns
(a) Sample an arm i uniformly at random from all K arms.
(b) Receive r_{n,i}(t) and set η_i(a(t)) = 0 if r_{n,i}(t) = 0 and η_i(a(t)) = 1 otherwise.
(c) If η_i(a(t)) = 1 then update o_{n,i} = o_{n,i} + 1 and s_{n,i}(t) = s_{n,i}(t-1) + r_{n,i}(t).
(d) Estimate the expectation of the arm i by μ_{n,i}^k = s_{n,i}(t) / o_{n,i}, for each i = 1, ..., K.

2. GoT Phase - for the next c_2 k^{1+δ} turns, play according to Algorithm 2 with ε and ρ
(a) Starting from the d_g = ⌈ρ c_2 k^{1+δ}⌉-th turn inside the GoT Phase, keep track on the number of times each action was played that resulted in being content
F_t^n(i) = Σ_{l=d_g}^{c_2 k^{1+δ}} I(a_n(l) = i, M_n(l) = C)
where I is the indicator function.

3. Exploitation Phase - for the next c_3 2^k turns, play
a_n^k = argmax_i F_t^n(i)

End
