---
slug: cooperative-multi-player-bandit-optimization--algorithm-1
label: Algorithm 1
claim_type: algorithm
statement: 'Initialization: Let non-negative integer δ(t) = δ_0 / t^q, η(t) = η_0
  / t^p ∀t. Let δ_0, η_0, p, q > 0. Let the memory M be large enough (as a function
  of θ, r > 0, B_r(θ) ⊆ A_n, ε_0 > 0, the distribution of G(t) and the communication
  protocol, see Lemma 1). Initialize X_n(1) ∈ A_n.


  For each t ≥ 1, each player n runs:


  1. Playing a perturbed action:

  (a) Generate Z_n(t) uniformly at random on the d_n-dimensional unit sphere S^{d_n}.

  (b) Play the perturbed action X̃_n(t) = X_n(t) + δ(t)(Z_n(t) - (X_n(t) - θ)/r).

  (c) Receive the reward u_n(t) = u_n(X̃_1(t), ..., X̃_N(t)).


  2. Communication:

  (a) Generate a random subset B_n(t) ⊆ U_n(t).

  (b) Broadcast {u_l(t - τ), l, τ}_{(l,τ) ∈ B_n(t)} for all neighbors m ∈ N_n(t).

  (c) Receive {u_l(t - τ), l, τ}_{(l,τ) ∈ B_m(t)} from all neighbors m ∈ N_n(t).

  (d) Update U_n^{τ+1}(t+1) = U_n^τ(t) ∪ {l} for every (l, τ) received.

  (e) Update p_m^n(t) = (1/t) Σ_{τ=1}^t 1_{m ∈ U_n^M(τ)} for all m.


  3. Learning the next action:

  (a) Define a_m^n(t) = 1/max{p_m^n(t), ε_0}.

  (b) Compute the sum of gradients estimation Y_n(t) = (d_n Z_n(t-M))/(δ(t-M)) Σ_{m
  ∈ U_n^M(t)} a_m^n(t) u_m(t-M).

  (c) Update the learned action and project it onto A_n: X_n(t+1) = Π_{A_n}(X_n(t)
  + η(t) Y_n(t)).'
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/projected-gradient-ascent]]'
- '[[concepts/cooperative-multi-player-bandit-optimization]]'
- '[[concepts/gradient-estimation-from-bandit-feedback]]'
- '[[concepts/time-varying-communication-graph]]'
- '[[concepts/proper-communication-protocol]]'
- '[[concepts/ergodic-markov-chain]]'
- '[[concepts/sum-of-rewards-objective]]'
- '[[concepts/sampling-radius-d-t]]'
- '[[concepts/bandit-feedback]]'
- '[[concepts/projection-operator-onto-action-set]]'
- '[[concepts/memory-m]]'
- '[[concepts/distributed-learning-algorithm]]'
- '[[concepts/step-size-eta-t]]'
- '[[concepts/gradient-approximation-operator]]'
- '[[concepts/set-of-kkt-stationary-points]]'
about_meta:
- target: '[[concepts/projected-gradient-ascent]]'
  role: primary
  aspect: ''
- target: '[[concepts/cooperative-multi-player-bandit-optimization]]'
  role: primary
  aspect: ''
- target: '[[concepts/gradient-estimation-from-bandit-feedback]]'
  role: primary
  aspect: ''
- target: '[[concepts/time-varying-communication-graph]]'
  role: primary
  aspect: ''
- target: '[[concepts/proper-communication-protocol]]'
  role: primary
  aspect: ''
- target: '[[concepts/ergodic-markov-chain]]'
  role: primary
  aspect: ''
- target: '[[concepts/sum-of-rewards-objective]]'
  role: primary
  aspect: ''
- target: '[[concepts/sampling-radius-d-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/bandit-feedback]]'
  role: primary
  aspect: ''
- target: '[[concepts/projection-operator-onto-action-set]]'
  role: primary
  aspect: ''
- target: '[[concepts/memory-m]]'
  role: primary
  aspect: ''
- target: '[[concepts/distributed-learning-algorithm]]'
  role: primary
  aspect: ''
- target: '[[concepts/step-size-eta-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/gradient-approximation-operator]]'
  role: primary
  aspect: ''
- target: '[[concepts/set-of-kkt-stationary-points]]'
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

# Algorithm 1

Initialization: Let non-negative integer δ(t) = δ_0 / t^q, η(t) = η_0 / t^p ∀t. Let δ_0, η_0, p, q > 0. Let the memory M be large enough (as a function of θ, r > 0, B_r(θ) ⊆ A_n, ε_0 > 0, the distribution of G(t) and the communication protocol, see Lemma 1). Initialize X_n(1) ∈ A_n.

For each t ≥ 1, each player n runs:

1. Playing a perturbed action:
(a) Generate Z_n(t) uniformly at random on the d_n-dimensional unit sphere S^{d_n}.
(b) Play the perturbed action X̃_n(t) = X_n(t) + δ(t)(Z_n(t) - (X_n(t) - θ)/r).
(c) Receive the reward u_n(t) = u_n(X̃_1(t), ..., X̃_N(t)).

2. Communication:
(a) Generate a random subset B_n(t) ⊆ U_n(t).
(b) Broadcast {u_l(t - τ), l, τ}_{(l,τ) ∈ B_n(t)} for all neighbors m ∈ N_n(t).
(c) Receive {u_l(t - τ), l, τ}_{(l,τ) ∈ B_m(t)} from all neighbors m ∈ N_n(t).
(d) Update U_n^{τ+1}(t+1) = U_n^τ(t) ∪ {l} for every (l, τ) received.
(e) Update p_m^n(t) = (1/t) Σ_{τ=1}^t 1_{m ∈ U_n^M(τ)} for all m.

3. Learning the next action:
(a) Define a_m^n(t) = 1/max{p_m^n(t), ε_0}.
(b) Compute the sum of gradients estimation Y_n(t) = (d_n Z_n(t-M))/(δ(t-M)) Σ_{m ∈ U_n^M(t)} a_m^n(t) u_m(t-M).
(c) Update the learned action and project it onto A_n: X_n(t+1) = Π_{A_n}(X_n(t) + η(t) Y_n(t)).
