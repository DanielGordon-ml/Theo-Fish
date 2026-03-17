---
slug: introduction-to-multi-armed-bandits--theorem-1-10
label: Theorem 1.10
claim_type: theorem
statement: Successive Elimination algorithm achieves regret $\operatornamewithlimits{\mathbb{E}}\left[\,R(t)\,\right]=O\left(\,\sqrt{Kt\log
  T}\,\right)$ for all rounds $t\leq T$.
proof: 'Focus on the clean event (6). Let a* be an optimal arm, and note that it cannot
  be deactivated. Fix any arm a such that μ(a) < μ(a*). Consider the last round t
  ≤ T when deactivation rule was invoked and arm a remained active. The confidence
  intervals of a and a* must overlap at round t. Therefore, Δ(a) := μ(a*) - μ(a) ≤
  2(r_t(a*) + r_t(a)) = 4·r_t(a). The last equality is because n_t(a) = n_t(a*), since
  the algorithm has been alternating active arms and both a and a* have been active
  before round t. By the choice of t, arm a can be played at most once afterwards:
  n_T(a) ≤ 1 + n_t(a). Thus, Δ(a) ≤ O(r_T(a)) = O(√(log(T)/n_T(a))) for each arm a
  with μ(a) < μ(a*). The contribution of arm a to regret at round t is R(t;a) = n_t(a)·Δ(a)
  ≤ n_t(a)·O(√(log(T)/n_t(a))) = O(√(n_t(a) log T)). Summing up over all arms, R(t)
  = Σ_a R(t;a) ≤ O(√(log T)) Σ_a √(n_t(a)). Since f(x) = √x is a real concave function,
  and Σ_a n_t(a) = t, by Jensen''s Inequality we have (1/K) Σ_a √(n_t(a)) ≤ √((1/K)
  Σ_a n_t(a)) = √(t/K). Plugging this in, R(t) ≤ O(√(Kt log T)).'
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/confidence-radius-r-t-a]]'
- '[[concepts/clean-event]]'
- '[[concepts/instance-independent-regret-bound]]'
- '[[concepts/successive-elimination]]'
- '[[concepts/regret-r-t]]'
- '[[concepts/time-horizon-t]]'
- '[[concepts/number-of-arms-k]]'
about_meta:
- target: '[[concepts/confidence-radius-r-t-a]]'
  role: primary
  aspect: ''
- target: '[[concepts/clean-event]]'
  role: primary
  aspect: ''
- target: '[[concepts/instance-independent-regret-bound]]'
  role: primary
  aspect: ''
- target: '[[concepts/successive-elimination]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret-r-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/time-horizon-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-arms-k]]'
  role: primary
  aspect: ''
depends_on: []
depends_on_meta: []
sourced_from:
- '[[sources/1904.07272|Introduction to Multi-Armed Bandits]]'
sourced_from_meta:
- target: '[[sources/1904.07272|Introduction to Multi-Armed Bandits]]'
  section: ''
  page: ''
  confidence: 0.0
---

# Theorem 1.10

Successive Elimination algorithm achieves regret $\operatornamewithlimits{\mathbb{E}}\left[\,R(t)\,\right]=O\left(\,\sqrt{Kt\log T}\,\right)$ for all rounds $t\leq T$.


## Proof

Focus on the clean event (6). Let a* be an optimal arm, and note that it cannot be deactivated. Fix any arm a such that μ(a) < μ(a*). Consider the last round t ≤ T when deactivation rule was invoked and arm a remained active. The confidence intervals of a and a* must overlap at round t. Therefore, Δ(a) := μ(a*) - μ(a) ≤ 2(r_t(a*) + r_t(a)) = 4·r_t(a). The last equality is because n_t(a) = n_t(a*), since the algorithm has been alternating active arms and both a and a* have been active before round t. By the choice of t, arm a can be played at most once afterwards: n_T(a) ≤ 1 + n_t(a). Thus, Δ(a) ≤ O(r_T(a)) = O(√(log(T)/n_T(a))) for each arm a with μ(a) < μ(a*). The contribution of arm a to regret at round t is R(t;a) = n_t(a)·Δ(a) ≤ n_t(a)·O(√(log(T)/n_t(a))) = O(√(n_t(a) log T)). Summing up over all arms, R(t) = Σ_a R(t;a) ≤ O(√(log T)) Σ_a √(n_t(a)). Since f(x) = √x is a real concave function, and Σ_a n_t(a) = t, by Jensen's Inequality we have (1/K) Σ_a √(n_t(a)) ≤ √((1/K) Σ_a n_t(a)) = √(t/K). Plugging this in, R(t) ≤ O(√(Kt log T)).
