---
slug: introduction-to-multi-armed-bandits--theorem-2-14
label: Theorem 2.14
claim_type: theorem
statement: 'Fix K, the number of arms. Consider an algorithm such that E[R(t)] ≤ O(C_{I,α}
  t^α) for each problem instance I and each α > 0. Here the "constant" C_{I,α} can
  depend on the problem instance I and the α, but not on time t. Fix an arbitrary
  problem instance I. For this problem instance: There exists time t_0 such that for
  any t ≥ t_0, E[R(t)] ≥ C_I ln(t), for some constant C_I that depends on the problem
  instance, but not on time t.'
proof: ''
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/number-of-arms-k]]'
- '[[concepts/regret-r-t]]'
- '[[concepts/bandit-algorithm]]'
- '[[concepts/problem-instance]]'
- '[[concepts/expected-regret-e-r-t]]'
- '[[concepts/stochastic-bandits-problem]]'
- '[[concepts/instance-dependent-constant]]'
- '[[concepts/0-1-rewards]]'
about_meta:
- target: '[[concepts/number-of-arms-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret-r-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/bandit-algorithm]]'
  role: primary
  aspect: ''
- target: '[[concepts/problem-instance]]'
  role: primary
  aspect: ''
- target: '[[concepts/expected-regret-e-r-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/stochastic-bandits-problem]]'
  role: primary
  aspect: ''
- target: '[[concepts/instance-dependent-constant]]'
  role: primary
  aspect: ''
- target: '[[concepts/0-1-rewards]]'
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

# Theorem 2.14

Fix K, the number of arms. Consider an algorithm such that E[R(t)] ≤ O(C_{I,α} t^α) for each problem instance I and each α > 0. Here the "constant" C_{I,α} can depend on the problem instance I and the α, but not on time t. Fix an arbitrary problem instance I. For this problem instance: There exists time t_0 such that for any t ≥ t_0, E[R(t)] ≥ C_I ln(t), for some constant C_I that depends on the problem instance, but not on time t.
