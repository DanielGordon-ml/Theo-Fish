---
slug: introduction-to-multi-armed-bandits--theorem-1-15
label: Theorem 1.15
claim_type: theorem
statement: Algorithm $\mathtt{UCB1}$ satisfies regret bounds in (9) and (11).
proof: 'Focus on the clean event (6). Recall that a* is an optimal arm, and a_t is
  the arm chosen by the algorithm in round t. According to the algorithm, UCB_t(a_t)
  ≥ UCB_t(a*). Under the clean event, μ(a_t) + r_t(a_t) ≥ μ̄_t(a_t) and UCB_t(a*)
  ≥ μ(a*). Therefore: μ(a_t) + 2r_t(a_t) ≥ μ̄_t(a_t) + r_t(a_t) = UCB_t(a_t) ≥ UCB_t(a*)
  ≥ μ(a*). It follows that Δ(a_t) := μ(a*) - μ(a_t) ≤ 2r_t(a_t) = 2√(2log(T)/n_t(a_t)).
  For each arm a consider the last round t when this arm is chosen by the algorithm.
  Applying the above to this round gives us property (7): Δ(a) ≤ O(√(log(T)/n_T(a)))
  for each arm a with μ(a) < μ(a*). The rest of the analysis follows from that property,
  as in the analysis of Successive Elimination.'
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/confidence-radius-r-t-a]]'
- '[[concepts/ucb1]]'
- '[[concepts/upper-confidence-bound]]'
- '[[concepts/regret-r-t]]'
- '[[concepts/instance-independent-regret-bound]]'
- '[[concepts/clean-event]]'
- '[[concepts/exploration-exploitation-tradeoff]]'
- '[[concepts/instance-dependent-constant]]'
about_meta:
- target: '[[concepts/confidence-radius-r-t-a]]'
  role: primary
  aspect: ''
- target: '[[concepts/ucb1]]'
  role: primary
  aspect: ''
- target: '[[concepts/upper-confidence-bound]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret-r-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/instance-independent-regret-bound]]'
  role: primary
  aspect: ''
- target: '[[concepts/clean-event]]'
  role: primary
  aspect: ''
- target: '[[concepts/exploration-exploitation-tradeoff]]'
  role: primary
  aspect: ''
- target: '[[concepts/instance-dependent-constant]]'
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

# Theorem 1.15

Algorithm $\mathtt{UCB1}$ satisfies regret bounds in (9) and (11).


## Proof

Focus on the clean event (6). Recall that a* is an optimal arm, and a_t is the arm chosen by the algorithm in round t. According to the algorithm, UCB_t(a_t) ≥ UCB_t(a*). Under the clean event, μ(a_t) + r_t(a_t) ≥ μ̄_t(a_t) and UCB_t(a*) ≥ μ(a*). Therefore: μ(a_t) + 2r_t(a_t) ≥ μ̄_t(a_t) + r_t(a_t) = UCB_t(a_t) ≥ UCB_t(a*) ≥ μ(a*). It follows that Δ(a_t) := μ(a*) - μ(a_t) ≤ 2r_t(a_t) = 2√(2log(T)/n_t(a_t)). For each arm a consider the last round t when this arm is chosen by the algorithm. Applying the above to this round gives us property (7): Δ(a) ≤ O(√(log(T)/n_T(a))) for each arm a with μ(a) < μ(a*). The rest of the analysis follows from that property, as in the analysis of Successive Elimination.
