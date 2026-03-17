---
slug: distributed-multi-player-bandits-a-game-of-thrones-approach--lemma-5
label: Lemma 5
claim_type: lemma
statement: Let $\delta > 0$. Define $\pmb{a}^{k*} = \arg \max_{\pmb{a}} \sum_{n=1}^{N}
  u_n(\pmb{a})$ and $\widetilde{\pmb{a}} = (\widetilde{a}_1, ..., \widetilde{a}_N)$
  where $\widetilde{a}_n = \arg \max_i F_t^n(i)$ for all $n$. For a small enough $\varepsilon$,
  the error probability of the $k$-th GoT phase, which is the probability that another
  strategy profile than $\pmb{a}^{k*}$ will be played in the exploitation phase, is
  bounded as follows $P_{c,k} \triangleq \Pr(\widetilde{\pmb{a}} \neq \pmb{a}^{k*})
  \le A_0 e^{-\frac{c_2(1-\rho)}{1728 T_m(\frac{1}{8})} k^{1+\delta}}$ where $A_0$
  is a constant with respect to $t$ (or $k$), and may depend on $N, K, \varepsilon$
  and the initial state.
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/optimal-solution-a-k]]'
- '[[concepts/mixing-time]]'
- '[[concepts/got-phase]]'
- '[[concepts/error-probability-of-got-phase]]'
- '[[concepts/got-dynamics]]'
- '[[concepts/epoch]]'
- '[[concepts/exploitation-phase]]'
about_meta:
- target: '[[concepts/optimal-solution-a-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/mixing-time]]'
  role: primary
  aspect: ''
- target: '[[concepts/got-phase]]'
  role: primary
  aspect: ''
- target: '[[concepts/error-probability-of-got-phase]]'
  role: primary
  aspect: ''
- target: '[[concepts/got-dynamics]]'
  role: primary
  aspect: ''
- target: '[[concepts/epoch]]'
  role: primary
  aspect: ''
- target: '[[concepts/exploitation-phase]]'
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

# Lemma 5

Let $\delta > 0$. Define $\pmb{a}^{k*} = \arg \max_{\pmb{a}} \sum_{n=1}^{N} u_n(\pmb{a})$ and $\widetilde{\pmb{a}} = (\widetilde{a}_1, ..., \widetilde{a}_N)$ where $\widetilde{a}_n = \arg \max_i F_t^n(i)$ for all $n$. For a small enough $\varepsilon$, the error probability of the $k$-th GoT phase, which is the probability that another strategy profile than $\pmb{a}^{k*}$ will be played in the exploitation phase, is bounded as follows $P_{c,k} \triangleq \Pr(\widetilde{\pmb{a}} \neq \pmb{a}^{k*}) \le A_0 e^{-\frac{c_2(1-\rho)}{1728 T_m(\frac{1}{8})} k^{1+\delta}}$ where $A_0$ is a constant with respect to $t$ (or $k$), and may depend on $N, K, \varepsilon$ and the initial state.
