---
slug: introduction-to-multi-armed-bandits--theorem-5-11-exercise-5-3
label: Theorem 5.11 (Exercise 5.3)
claim_type: theorem
statement: Any deterministic algorithm for the online learning problem with K experts
  and 0-1 costs can suffer total cost T for some deterministic-oblivious adversary,
  even if cost* ≤ T/K.
proof: Fix the algorithm. Construct the problem instance by induction on round t,
  so that the chosen arm has cost 1 and all other arms have cost 0. Since the algorithm
  is deterministic, the adversary can predict the chosen arm at each round and assign
  cost 1 to it and cost 0 to all others. The algorithm's total cost is T. The best
  expert has cost at most T/K since total cost across all experts is T (exactly one
  expert incurs cost 1 per round), and by pigeonhole some expert has cost at most
  T/K. [Proof sketch from hint; full proof left as exercise.]
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/deterministic-oblivious-adversary]]'
- '[[concepts/number-of-experts-k]]'
- '[[concepts/online-learning-with-experts]]'
- '[[concepts/number-of-rounds-t]]'
- '[[concepts/total-cost]]'
- '[[concepts/0-1-costs]]'
- '[[concepts/deterministic-algorithm]]'
about_meta:
- target: '[[concepts/deterministic-oblivious-adversary]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-experts-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/online-learning-with-experts]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-rounds-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/total-cost]]'
  role: primary
  aspect: ''
- target: '[[concepts/0-1-costs]]'
  role: primary
  aspect: ''
- target: '[[concepts/deterministic-algorithm]]'
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

# Theorem 5.11 (Exercise 5.3)

Any deterministic algorithm for the online learning problem with K experts and 0-1 costs can suffer total cost T for some deterministic-oblivious adversary, even if cost* ≤ T/K.


## Proof

Fix the algorithm. Construct the problem instance by induction on round t, so that the chosen arm has cost 1 and all other arms have cost 0. Since the algorithm is deterministic, the adversary can predict the chosen arm at each round and assign cost 1 to it and cost 0 to all others. The algorithm's total cost is T. The best expert has cost at most T/K since total cost across all experts is T (exactly one expert incurs cost 1 per round), and by pigeonhole some expert has cost at most T/K. [Proof sketch from hint; full proof left as exercise.]
