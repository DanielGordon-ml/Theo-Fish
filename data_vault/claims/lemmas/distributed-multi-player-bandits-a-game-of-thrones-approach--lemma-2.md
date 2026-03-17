---
slug: distributed-multi-player-bandits-a-game-of-thrones-approach--lemma-2
label: Lemma 2
claim_type: lemma
statement: Let $\left\{ \mu_{n,i}^{k} \right\}$ be the estimated reward expectations
  using all the exploration phases up to epoch $k$. Denote $\pmb{a}^{*} = \arg\max_{\pmb{a}}
  \sum_{n=1}^{N} g_n(\pmb{a})$ and $\mathbf{a}^{k*} = \arg\max_{\pmb{a}} \sum_{n=1}^{N}
  \mu_{n,a_n}^{k} \eta_{a_n}(\pmb{a})$. Also denote $J_1 = \sum_{n=1}^{N} g_n(\pmb{a}^{*})$
  and the second best objective by $J_2$. If the length of the exploration phase satisfies
  $c_1 > \frac{16 N^2 K}{(J_1 - J_2)^2}$, then after the $k$-th epoch we have $P_{e,k}
  \triangleq \Pr(\pmb{a}^{*} \neq \pmb{a}^{k*}) \le 4 K^2 e^{-k}.$
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/error-probability]]'
- '[[concepts/epoch]]'
- '[[concepts/c1]]'
- '[[concepts/number-of-arms-k]]'
- '[[concepts/number-of-players-n]]'
- '[[concepts/second-best-welfare]]'
- '[[concepts/optimal-assignment]]'
- '[[concepts/exploration-length]]'
- '[[concepts/exploration-error-probability]]'
- '[[concepts/optimal-solution-a-k]]'
- '[[concepts/exploration-phase]]'
- '[[concepts/estimated-mean-reward]]'
about_meta:
- target: '[[concepts/error-probability]]'
  role: primary
  aspect: ''
- target: '[[concepts/epoch]]'
  role: primary
  aspect: ''
- target: '[[concepts/c1]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-arms-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-players-n]]'
  role: primary
  aspect: ''
- target: '[[concepts/second-best-welfare]]'
  role: primary
  aspect: ''
- target: '[[concepts/optimal-assignment]]'
  role: primary
  aspect: ''
- target: '[[concepts/exploration-length]]'
  role: primary
  aspect: ''
- target: '[[concepts/exploration-error-probability]]'
  role: primary
  aspect: ''
- target: '[[concepts/optimal-solution-a-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/exploration-phase]]'
  role: primary
  aspect: ''
- target: '[[concepts/estimated-mean-reward]]'
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

# Lemma 2

Let $\left\{ \mu_{n,i}^{k} \right\}$ be the estimated reward expectations using all the exploration phases up to epoch $k$. Denote $\pmb{a}^{*} = \arg\max_{\pmb{a}} \sum_{n=1}^{N} g_n(\pmb{a})$ and $\mathbf{a}^{k*} = \arg\max_{\pmb{a}} \sum_{n=1}^{N} \mu_{n,a_n}^{k} \eta_{a_n}(\pmb{a})$. Also denote $J_1 = \sum_{n=1}^{N} g_n(\pmb{a}^{*})$ and the second best objective by $J_2$. If the length of the exploration phase satisfies $c_1 > \frac{16 N^2 K}{(J_1 - J_2)^2}$, then after the $k$-th epoch we have $P_{e,k} \triangleq \Pr(\pmb{a}^{*} \neq \pmb{a}^{k*}) \le 4 K^2 e^{-k}.$
