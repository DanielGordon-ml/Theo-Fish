---
slug: introduction-to-multi-armed-bandits--exercise-6-3-dynamic-regret-under-slowly-changing-costs
label: Exercise 6.3 (dynamic regret under slowly changing costs)
claim_type: conjecture
statement: Consider a randomized oblivious adversary such that the expected cost of
  each arm changes by at most ε from one round to another, for some fixed and known
  ε>0. Use algorithm Exp4 to obtain dynamic regret E[R*(T)] ≤ O(T)·(ε·K log K)^{1/3}.
proof: ''
strength: ''
status: exercise
human_notes: ''
about:
- '[[concepts/number-of-arms-k]]'
- '[[concepts/dynamic-regret]]'
- '[[concepts/adversarial-bandits-problem]]'
- '[[concepts/exp4-algorithm]]'
- '[[concepts/randomized-oblivious-adversary]]'
- '[[concepts/n-shifting-regret]]'
about_meta:
- target: '[[concepts/number-of-arms-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/dynamic-regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/adversarial-bandits-problem]]'
  role: primary
  aspect: ''
- target: '[[concepts/exp4-algorithm]]'
  role: primary
  aspect: ''
- target: '[[concepts/randomized-oblivious-adversary]]'
  role: primary
  aspect: ''
- target: '[[concepts/n-shifting-regret]]'
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

# Exercise 6.3 (dynamic regret under slowly changing costs)

Consider a randomized oblivious adversary such that the expected cost of each arm changes by at most ε from one round to another, for some fixed and known ε>0. Use algorithm Exp4 to obtain dynamic regret E[R*(T)] ≤ O(T)·(ε·K log K)^{1/3}.
