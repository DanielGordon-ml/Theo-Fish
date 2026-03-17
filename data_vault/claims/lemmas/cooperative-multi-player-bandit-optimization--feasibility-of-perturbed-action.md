---
slug: cooperative-multi-player-bandit-optimization--feasibility-of-perturbed-action
label: Feasibility of Perturbed Action
claim_type: lemma
statement: If δ(t)/r < 1, then the perturbed action X̃_n(t) = X_n(t) + δ(t)W_n(t),
  where W_n(t) = Z_n(t) − (X_n(t)−θ)/r, satisfies X̃_n(t) ∈ A_n. This follows because
  X̃_n(t) = (1 − δ(t)/r) X_n(t) + (δ(t)/r)(θ + r Z_n(t)) ∈ A_n, where θ + r Z_n(t)
  ∈ B_r(θ) ⊆ A_n, and the result follows from the convexity of A_n.
proof: Since θ + r Z_n(t) ∈ B_r(θ) ⊆ A_n and X_n(t) ∈ A_n, we can write X̃_n(t) =
  (1 − δ(t)/r) X_n(t) + (δ(t)/r)(θ + r Z_n(t)). Since δ(t)/r < 1, this is a convex
  combination of two points in A_n. By convexity of A_n, the result is in A_n.
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/sampling-radius-d-t]]'
- '[[concepts/convexity]]'
- '[[concepts/perturbed-action-operator]]'
- '[[concepts/radius-r]]'
- '[[concepts/parameter-theta]]'
- '[[concepts/action-set-of-agent-n]]'
- '[[concepts/ball-around-theta]]'
- '[[concepts/d-n-dimensional-unit-sphere]]'
about_meta:
- target: '[[concepts/sampling-radius-d-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/convexity]]'
  role: primary
  aspect: ''
- target: '[[concepts/perturbed-action-operator]]'
  role: primary
  aspect: ''
- target: '[[concepts/radius-r]]'
  role: primary
  aspect: ''
- target: '[[concepts/parameter-theta]]'
  role: primary
  aspect: ''
- target: '[[concepts/action-set-of-agent-n]]'
  role: primary
  aspect: ''
- target: '[[concepts/ball-around-theta]]'
  role: primary
  aspect: ''
- target: '[[concepts/d-n-dimensional-unit-sphere]]'
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

# Feasibility of Perturbed Action

If δ(t)/r < 1, then the perturbed action X̃_n(t) = X_n(t) + δ(t)W_n(t), where W_n(t) = Z_n(t) − (X_n(t)−θ)/r, satisfies X̃_n(t) ∈ A_n. This follows because X̃_n(t) = (1 − δ(t)/r) X_n(t) + (δ(t)/r)(θ + r Z_n(t)) ∈ A_n, where θ + r Z_n(t) ∈ B_r(θ) ⊆ A_n, and the result follows from the convexity of A_n.


## Proof

Since θ + r Z_n(t) ∈ B_r(θ) ⊆ A_n and X_n(t) ∈ A_n, we can write X̃_n(t) = (1 − δ(t)/r) X_n(t) + (δ(t)/r)(θ + r Z_n(t)). Since δ(t)/r < 1, this is a convex combination of two points in A_n. By convexity of A_n, the result is in A_n.
