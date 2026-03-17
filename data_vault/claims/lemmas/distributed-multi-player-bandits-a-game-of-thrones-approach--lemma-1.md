---
slug: distributed-multi-player-bandits-a-game-of-thrones-approach--lemma-1
label: Lemma 1
claim_type: lemma
statement: Assume that $\{ \mu_{n,i} \}$ are known up to an uncertainty of $\Delta$,
  i.e., $| \hat{\mu}_{n,i} - \mu_{n,i} | \leq \Delta$ for each $n$ and $i$ for some
  $\{ \hat{\mu}_{n,i} \}$. Denote the optimal assignment by $\pmb{a}_1 = \arg\max_{\pmb{a}}
  \sum_{n=1}^{N} g_n(\pmb{a})$ and its objective by $J_1 = \sum_{n=1}^{N} g_n(\pmb{a}_1)$.
  Denote the second best objective and the corresponding assignment by $J_2$ and $\mathbf{a_2}$,
  respectively. If $\Delta < \frac{J_1 - J_2}{2N}$ then $\arg\max_{\pmb{a}} \sum_{n=1}^{N}
  g_n(\pmb{a}) = \arg\max_{\pmb{a}} \sum_{n=1}^{N} \hat{\mu}_{n,a_n} \eta_{a_n}(\pmb{a})$
  so that the optimal assignment does not change due to the uncertainty.
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/number-of-players-n]]'
- '[[concepts/estimated-mean-reward]]'
- '[[concepts/mean-reward-mu]]'
- '[[concepts/eta-function]]'
- '[[concepts/optimal-assignment]]'
- '[[concepts/second-best-welfare]]'
- '[[concepts/assignment-problem]]'
- '[[concepts/uncertainty-bound]]'
about_meta:
- target: '[[concepts/number-of-players-n]]'
  role: primary
  aspect: ''
- target: '[[concepts/estimated-mean-reward]]'
  role: primary
  aspect: ''
- target: '[[concepts/mean-reward-mu]]'
  role: primary
  aspect: ''
- target: '[[concepts/eta-function]]'
  role: primary
  aspect: ''
- target: '[[concepts/optimal-assignment]]'
  role: primary
  aspect: ''
- target: '[[concepts/second-best-welfare]]'
  role: primary
  aspect: ''
- target: '[[concepts/assignment-problem]]'
  role: primary
  aspect: ''
- target: '[[concepts/uncertainty-bound]]'
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

# Lemma 1

Assume that $\{ \mu_{n,i} \}$ are known up to an uncertainty of $\Delta$, i.e., $| \hat{\mu}_{n,i} - \mu_{n,i} | \leq \Delta$ for each $n$ and $i$ for some $\{ \hat{\mu}_{n,i} \}$. Denote the optimal assignment by $\pmb{a}_1 = \arg\max_{\pmb{a}} \sum_{n=1}^{N} g_n(\pmb{a})$ and its objective by $J_1 = \sum_{n=1}^{N} g_n(\pmb{a}_1)$. Denote the second best objective and the corresponding assignment by $J_2$ and $\mathbf{a_2}$, respectively. If $\Delta < \frac{J_1 - J_2}{2N}$ then $\arg\max_{\pmb{a}} \sum_{n=1}^{N} g_n(\pmb{a}) = \arg\max_{\pmb{a}} \sum_{n=1}^{N} \hat{\mu}_{n,a_n} \eta_{a_n}(\pmb{a})$ so that the optimal assignment does not change due to the uncertainty.
