---
slug: distributed-multi-player-bandits-a-game-of-thrones-approach--theorem-1
label: Theorem 1
claim_type: theorem
statement: Assume that the rewards $\{ r_{n,i}(t) \}_t$ are independent in n and i.i.d.
  in time $t$, with continuous distributions on $[0,1]$ with positive expectations
  $\{ \mu_{n,i} \}$. Let the game have a finite horizon $T$, unknown to the players.
  Denote the optimal objective by $J_1 = \max_{\pmb{a}} \sum_{n=1}^{N} g_n(\pmb{a})$
  and the second best one by $J_2$. Let each player play according to Algorithm 1,
  with a small enough $\varepsilon$, exploration phase length of $c_1 > \frac{16N^2K}{(J_1
  - J_2)^2}$ and $\delta > 0$. Then, for large enough $T$, the expected total regret
  is upper bounded by $\bar{R} \leq 3 c_2 N \log_2^{2+\delta}\left(\frac{T}{c_3} +
  2\right) = O\left(\log^{2+\delta} T\right).$
proof: Let $\delta > 0$. Denote the number of epochs that start within $T$ turns by
  $E$. Since $T \geq \sum_{k=1}^{E-1} \left( c_1 + c_2 k^{1+\delta} + c_3 2^k \right)
  \geq c_3 \left( 2^E - 2 \right)$, $E$ is upper bounded by $E \leq \log_2 \left(
  \frac{T}{c_3} + 2 \right)$. Denote by $P_{e,k}$ and $P_{c,k}$ the error probabilities
  of the exploration and GoT phases of epoch $k$ respectively. Observe that if none
  of these errors occurred, the optimal solution to (5) is played in the $k$-th exploitation
  phase, which adds no additional regret to the total regret. We will prove in Lemma
  2 and Lemma 5 that $P_{e,k} \leq 4K^2 e^{-k}$ and $P_{c,k} \leq A_0 e^{-\frac{c_2(1-\rho)}{1728
  T_m(\frac{1}{8})} k^{1+\delta}}$, where $A_0$ is a constant and $T_m(\frac{1}{8})$
  is the mixing time of the Markov chain of the GoT Dynamics. Note that $T_m(\frac{1}{8})$
  depends on $N, K$ and $\varepsilon$, so there exists a $k_0$ such that for all $k
  > k_0$ we have $e^{-\frac{c_2(1-\rho)}{1728 T_m(\frac{1}{8})} k^{\delta}} < \frac{1}{2}$.
  We now bound the expected total regret of epoch $k > k_0$, denoted by $\bar{R}_k$,
  as follows $\bar{R}_k \leq (c_1 + c_2 k^{1+\delta}) N + (4K^2 e^{-k} + A_0 e^{-\frac{c_2(1-\rho)}{1728
  T_m(\frac{1}{8})} k^{1+\delta}}) c_3 2^k N \leq c_1 N + 2 A_0 c_3 N \beta^k + c_2
  k^{1+\delta} N$ for some constant $\beta < 1$. We conclude that, for some additive
  constant $C$, $\bar{R} = \sum_{k=1}^{E} \bar{R}_k \leq C + 2 c_2 N \sum_{k=k_0+1}^{E}
  k^{1+\delta} \leq C + 2 c_2 N E^{2+\delta} \leq C + 2 c_2 N \log_2^{2+\delta} \left(
  \frac{T}{c_3} + 2 \right)$ where (a) follows since completing the last epoch to
  a full epoch increases $\bar{R}_k$, and (b) is (13).
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/exploration-length]]'
- '[[concepts/mixing-time]]'
- '[[concepts/fully-distributed-algorithm]]'
- '[[concepts/error-probability]]'
- '[[concepts/multi-player-multi-armed-bandit-game]]'
- '[[concepts/epoch]]'
- '[[concepts/exploitation-phase]]'
- '[[concepts/got-algorithm]]'
- '[[concepts/exploration-phase]]'
- '[[concepts/total-regret]]'
- '[[concepts/exploration-exploitation-tradeoff]]'
- '[[concepts/got-phase]]'
- '[[concepts/expected-total-regret]]'
about_meta:
- target: '[[concepts/exploration-length]]'
  role: primary
  aspect: ''
- target: '[[concepts/mixing-time]]'
  role: primary
  aspect: ''
- target: '[[concepts/fully-distributed-algorithm]]'
  role: primary
  aspect: ''
- target: '[[concepts/error-probability]]'
  role: primary
  aspect: ''
- target: '[[concepts/multi-player-multi-armed-bandit-game]]'
  role: primary
  aspect: ''
- target: '[[concepts/epoch]]'
  role: primary
  aspect: ''
- target: '[[concepts/exploitation-phase]]'
  role: primary
  aspect: ''
- target: '[[concepts/got-algorithm]]'
  role: primary
  aspect: ''
- target: '[[concepts/exploration-phase]]'
  role: primary
  aspect: ''
- target: '[[concepts/total-regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/exploration-exploitation-tradeoff]]'
  role: primary
  aspect: ''
- target: '[[concepts/got-phase]]'
  role: primary
  aspect: ''
- target: '[[concepts/expected-total-regret]]'
  role: primary
  aspect: ''
depends_on:
- '[[claims/distributed-multi-player-bandits-a-game-of-thrones-approach--lemma-2]]'
- '[[claims/distributed-multi-player-bandits-a-game-of-thrones-approach--lemma-5]]'
depends_on_meta:
- target: '[[claims/distributed-multi-player-bandits-a-game-of-thrones-approach--lemma-2]]'
- target: '[[claims/distributed-multi-player-bandits-a-game-of-thrones-approach--lemma-5]]'
sourced_from:
- '[[sources/distributed_multi_player_bandits_a_game_of_thrones_approach|distributed_multi_player_bandits_a_game_of_thrones_approach]]'
sourced_from_meta:
- target: '[[sources/distributed_multi_player_bandits_a_game_of_thrones_approach|distributed_multi_player_bandits_a_game_of_thrones_approach]]'
  section: ''
  page: ''
  confidence: 0.0
---

# Theorem 1

Assume that the rewards $\{ r_{n,i}(t) \}_t$ are independent in n and i.i.d. in time $t$, with continuous distributions on $[0,1]$ with positive expectations $\{ \mu_{n,i} \}$. Let the game have a finite horizon $T$, unknown to the players. Denote the optimal objective by $J_1 = \max_{\pmb{a}} \sum_{n=1}^{N} g_n(\pmb{a})$ and the second best one by $J_2$. Let each player play according to Algorithm 1, with a small enough $\varepsilon$, exploration phase length of $c_1 > \frac{16N^2K}{(J_1 - J_2)^2}$ and $\delta > 0$. Then, for large enough $T$, the expected total regret is upper bounded by $\bar{R} \leq 3 c_2 N \log_2^{2+\delta}\left(\frac{T}{c_3} + 2\right) = O\left(\log^{2+\delta} T\right).$


## Proof

Let $\delta > 0$. Denote the number of epochs that start within $T$ turns by $E$. Since $T \geq \sum_{k=1}^{E-1} \left( c_1 + c_2 k^{1+\delta} + c_3 2^k \right) \geq c_3 \left( 2^E - 2 \right)$, $E$ is upper bounded by $E \leq \log_2 \left( \frac{T}{c_3} + 2 \right)$. Denote by $P_{e,k}$ and $P_{c,k}$ the error probabilities of the exploration and GoT phases of epoch $k$ respectively. Observe that if none of these errors occurred, the optimal solution to (5) is played in the $k$-th exploitation phase, which adds no additional regret to the total regret. We will prove in Lemma 2 and Lemma 5 that $P_{e,k} \leq 4K^2 e^{-k}$ and $P_{c,k} \leq A_0 e^{-\frac{c_2(1-\rho)}{1728 T_m(\frac{1}{8})} k^{1+\delta}}$, where $A_0$ is a constant and $T_m(\frac{1}{8})$ is the mixing time of the Markov chain of the GoT Dynamics. Note that $T_m(\frac{1}{8})$ depends on $N, K$ and $\varepsilon$, so there exists a $k_0$ such that for all $k > k_0$ we have $e^{-\frac{c_2(1-\rho)}{1728 T_m(\frac{1}{8})} k^{\delta}} < \frac{1}{2}$. We now bound the expected total regret of epoch $k > k_0$, denoted by $\bar{R}_k$, as follows $\bar{R}_k \leq (c_1 + c_2 k^{1+\delta}) N + (4K^2 e^{-k} + A_0 e^{-\frac{c_2(1-\rho)}{1728 T_m(\frac{1}{8})} k^{1+\delta}}) c_3 2^k N \leq c_1 N + 2 A_0 c_3 N \beta^k + c_2 k^{1+\delta} N$ for some constant $\beta < 1$. We conclude that, for some additive constant $C$, $\bar{R} = \sum_{k=1}^{E} \bar{R}_k \leq C + 2 c_2 N \sum_{k=k_0+1}^{E} k^{1+\delta} \leq C + 2 c_2 N E^{2+\delta} \leq C + 2 c_2 N \log_2^{2+\delta} \left( \frac{T}{c_3} + 2 \right)$ where (a) follows since completing the last epoch to a full epoch increases $\bar{R}_k$, and (b) is (13).
