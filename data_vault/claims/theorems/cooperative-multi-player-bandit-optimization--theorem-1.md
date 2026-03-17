---
slug: cooperative-multi-player-bandit-optimization--theorem-1
label: Theorem 1
claim_type: theorem
statement: 'Let the $N$ players each independently run Algorithm 1 to play the game
  in Definition 1. Let $\eta(t) = \frac{\eta_0}{t^p}$, $\delta(t) = \frac{\delta_0}{t^q}$
  for some $\delta_0, \eta_0 > 0$. Assume that $G(t)$ is an ergodic Markov chain on
  $\mathcal{G}$ such that the graph union $\cup_{G \in \mathcal{G}} G$ is connected,
  and that the communication protocol is proper (Definition 4). Assume that the memory
  $M$ is large enough, as a function of the distribution of $G(t)$ and the communication
  protocol. If $0 < p, q \le 1$, $p - q > \frac{1}{2}$ and $p > \frac{q+3}{4}$ (e.g.,
  $p = 0.8, q = 0.1$) then, as $t \to \infty$, the action profile $(X_1(t), ..., X_N(t))$
  converges with probability 1 to the set of KKT stationary points:

  $$\mathcal{KKT} = \left\{ x \left| \forall n, \exists \lambda^n \geq 0 \text{ s.t.
  } -\nabla_{x_n} \sum_{m=1}^{N} u_m(\pmb{x}) + \sum_{i: q_i^n(\pmb{x}_n) = 0} \lambda_i^n
  \nabla q_i^n(\pmb{x}_n) = 0 \right. \right\}.$$

  Hence, if $\sum_{n=1}^{N} u_n(\pmb{x})$ is concave and for all $n$, there exists
  an $\pmb{x}_n$ s.t. $q_i^n(\pmb{x}_n) < 0$ for all $i$, then $(X_1(t), ..., X_N(t))$
  converges to the set $\arg\max \sum_{n=1}^{N} u_n(\pmb{x})$ with probability 1 as
  $t \to \infty$.'
proof: ''
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/projected-gradient-ascent]]'
- '[[concepts/memory-m]]'
- '[[concepts/ergodic-markov-chain]]'
- '[[concepts/stochastic-approximation-algorithms]]'
- '[[concepts/sampling-radius-d-t]]'
- '[[concepts/communication-graph-process]]'
- '[[concepts/step-size-eta-t]]'
- '[[concepts/set-of-kkt-stationary-points]]'
- '[[concepts/sum-of-rewards-objective]]'
- '[[concepts/proper-communication-protocol]]'
- '[[concepts/connected-graph-union]]'
- '[[concepts/algorithm-1]]'
about_meta:
- target: '[[concepts/projected-gradient-ascent]]'
  role: primary
  aspect: ''
- target: '[[concepts/memory-m]]'
  role: primary
  aspect: ''
- target: '[[concepts/ergodic-markov-chain]]'
  role: primary
  aspect: ''
- target: '[[concepts/stochastic-approximation-algorithms]]'
  role: primary
  aspect: ''
- target: '[[concepts/sampling-radius-d-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/communication-graph-process]]'
  role: primary
  aspect: ''
- target: '[[concepts/step-size-eta-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/set-of-kkt-stationary-points]]'
  role: primary
  aspect: ''
- target: '[[concepts/sum-of-rewards-objective]]'
  role: primary
  aspect: ''
- target: '[[concepts/proper-communication-protocol]]'
  role: primary
  aspect: ''
- target: '[[concepts/connected-graph-union]]'
  role: primary
  aspect: ''
- target: '[[concepts/algorithm-1]]'
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

# Theorem 1

Let the $N$ players each independently run Algorithm 1 to play the game in Definition 1. Let $\eta(t) = \frac{\eta_0}{t^p}$, $\delta(t) = \frac{\delta_0}{t^q}$ for some $\delta_0, \eta_0 > 0$. Assume that $G(t)$ is an ergodic Markov chain on $\mathcal{G}$ such that the graph union $\cup_{G \in \mathcal{G}} G$ is connected, and that the communication protocol is proper (Definition 4). Assume that the memory $M$ is large enough, as a function of the distribution of $G(t)$ and the communication protocol. If $0 < p, q \le 1$, $p - q > \frac{1}{2}$ and $p > \frac{q+3}{4}$ (e.g., $p = 0.8, q = 0.1$) then, as $t \to \infty$, the action profile $(X_1(t), ..., X_N(t))$ converges with probability 1 to the set of KKT stationary points:
$$\mathcal{KKT} = \left\{ x \left| \forall n, \exists \lambda^n \geq 0 \text{ s.t. } -\nabla_{x_n} \sum_{m=1}^{N} u_m(\pmb{x}) + \sum_{i: q_i^n(\pmb{x}_n) = 0} \lambda_i^n \nabla q_i^n(\pmb{x}_n) = 0 \right. \right\}.$$
Hence, if $\sum_{n=1}^{N} u_n(\pmb{x})$ is concave and for all $n$, there exists an $\pmb{x}_n$ s.t. $q_i^n(\pmb{x}_n) < 0$ for all $i$, then $(X_1(t), ..., X_N(t))$ converges to the set $\arg\max \sum_{n=1}^{N} u_n(\pmb{x})$ with probability 1 as $t \to \infty$.
