---
slug: distributed-multi-player-bandits-a-game-of-thrones-approach--lemma-4
label: Lemma 4
claim_type: lemma
statement: The optimal solution to $\max_{\pmb{a}} \sum_{n=1}^{N} u_n(\pmb{a})$ is
  unique with probability 1.
proof: First note that an optimal solution must not have any collisions, otherwise
  it can be improved since $K \geq N$. For two different $\tilde{\mathbf{a}} \ne a^*$,
  $\tilde{\mathbf{a}}$ and $\mathbf{a}^*$ must differ in at least one assignment.
  Since the distributions of the rewards are continuous, so are the distributions
  of $\sum_{n=1}^N \mu^k_{n,a_n}$ (as a sum of the average of the rewards). Hence
  $\Pr\left(\sum_{n=1}^{N} \mu_{n,\tilde{a}_n}^k = \sum_{n=1}^{N} \mu_{n,a_n^*}^k\right)
  = 0$, and the result follows. □
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/continuous-distribution-of-rewards]]'
- '[[concepts/number-of-players-n]]'
- '[[concepts/utility-function-of-player-n]]'
- '[[concepts/optimal-assignment]]'
- '[[concepts/optimal-solution-a-k]]'
- '[[concepts/game-of-thrones-g]]'
- '[[concepts/number-of-arms-k]]'
- '[[concepts/sum-of-utilities]]'
- '[[concepts/assignment-problem]]'
- '[[concepts/number-of-players-n]]'
- '[[concepts/continuous-distribution-of-rewards]]'
- '[[concepts/optimal-solution-a-k]]'
- '[[concepts/number-of-arms-k]]'
- '[[concepts/optimal-assignment]]'
- '[[concepts/utility-function-of-player-n]]'
- '[[concepts/sum-of-utilities]]'
- '[[concepts/game-of-thrones-g]]'
- '[[concepts/assignment-problem]]'
about_meta:
- target: '[[concepts/continuous-distribution-of-rewards]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-players-n]]'
  role: primary
  aspect: ''
- target: '[[concepts/utility-function-of-player-n]]'
  role: primary
  aspect: ''
- target: '[[concepts/optimal-assignment]]'
  role: primary
  aspect: ''
- target: '[[concepts/optimal-solution-a-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/game-of-thrones-g]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-arms-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/sum-of-utilities]]'
  role: primary
  aspect: ''
- target: '[[concepts/assignment-problem]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-players-n]]'
  role: primary
  aspect: ''
- target: '[[concepts/continuous-distribution-of-rewards]]'
  role: primary
  aspect: ''
- target: '[[concepts/optimal-solution-a-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-arms-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/optimal-assignment]]'
  role: primary
  aspect: ''
- target: '[[concepts/utility-function-of-player-n]]'
  role: primary
  aspect: ''
- target: '[[concepts/sum-of-utilities]]'
  role: primary
  aspect: ''
- target: '[[concepts/game-of-thrones-g]]'
  role: primary
  aspect: ''
- target: '[[concepts/assignment-problem]]'
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

# Lemma 4

The optimal solution to $\max_{\pmb{a}} \sum_{n=1}^{N} u_n(\pmb{a})$ is unique with probability 1.


## Proof

First note that an optimal solution must not have any collisions, otherwise it can be improved since $K \geq N$. For two different $\tilde{\mathbf{a}} \ne a^*$, $\tilde{\mathbf{a}}$ and $\mathbf{a}^*$ must differ in at least one assignment. Since the distributions of the rewards are continuous, so are the distributions of $\sum_{n=1}^N \mu^k_{n,a_n}$ (as a sum of the average of the rewards). Hence $\Pr\left(\sum_{n=1}^{N} \mu_{n,\tilde{a}_n}^k = \sum_{n=1}^{N} \mu_{n,a_n^*}^k\right) = 0$, and the result follows. □
