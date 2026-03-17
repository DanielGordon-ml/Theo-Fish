---
slug: cooperative-multi-player-bandit-optimization--gradient-estimation-via-random-perturbation
label: Gradient Estimation via Random Perturbation
claim_type: proposition
statement: In the one-dimensional case where Z_n(t) = ±1 with probability 1/2, the
  quantity (Z_n(t)/δ(t)) u_m(x + δ(t) Z_n(t)) satisfies E{(Z_n(t)/δ(t)) u_m(x + δ(t)
  Z_n(t))} = (u_m(x + δ(t)) − u_m(x − δ(t)))/(2δ(t)), which converges to the gradient
  as the sampling radius δ(t) decreases. Hence (Z_n(t)/δ(t)) u_m(x + δ(t) Z_n(t))
  is a noisy estimation of ∇_{x_n} u_m(x) with a vanishing bias.
proof: ''
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/utility-function-u-n]]'
- '[[concepts/sampling-radius-d-t]]'
- '[[concepts/gradient-estimation-from-bandit-feedback]]'
- '[[concepts/gradient-estimation-operator]]'
- '[[concepts/bias]]'
about_meta:
- target: '[[concepts/utility-function-u-n]]'
  role: primary
  aspect: ''
- target: '[[concepts/sampling-radius-d-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/gradient-estimation-from-bandit-feedback]]'
  role: primary
  aspect: ''
- target: '[[concepts/gradient-estimation-operator]]'
  role: primary
  aspect: ''
- target: '[[concepts/bias]]'
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

# Gradient Estimation via Random Perturbation

In the one-dimensional case where Z_n(t) = ±1 with probability 1/2, the quantity (Z_n(t)/δ(t)) u_m(x + δ(t) Z_n(t)) satisfies E{(Z_n(t)/δ(t)) u_m(x + δ(t) Z_n(t))} = (u_m(x + δ(t)) − u_m(x − δ(t)))/(2δ(t)), which converges to the gradient as the sampling radius δ(t) decreases. Hence (Z_n(t)/δ(t)) u_m(x + δ(t) Z_n(t)) is a noisy estimation of ∇_{x_n} u_m(x) with a vanishing bias.
