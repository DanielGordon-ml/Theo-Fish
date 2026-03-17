---
slug: introduction-to-multi-armed-bandits--exercise-1-5-a
label: Exercise 1.5(a)
claim_type: proposition
statement: Take any bandit algorithm A for fixed time horizon T. Convert it to an
  algorithm A_∞ which runs forever, in phases i = 1, 2, 3, ... of 2^i rounds each.
  In each phase i algorithm A is restarted and run with time horizon 2^i. State and
  prove a theorem which converts an instance-independent upper bound on regret for
  A into similar bound for A_∞ (so that this theorem applies to both UCB1 and Explore-first).
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/explore-first-algorithm]]'
- '[[concepts/regret-bound]]'
- '[[concepts/doubling-trick]]'
- '[[concepts/instance-independent-regret-bound]]'
- '[[concepts/bandit-algorithm]]'
- '[[concepts/ucb1-algorithm]]'
about_meta:
- target: '[[concepts/explore-first-algorithm]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret-bound]]'
  role: primary
  aspect: ''
- target: '[[concepts/doubling-trick]]'
  role: primary
  aspect: ''
- target: '[[concepts/instance-independent-regret-bound]]'
  role: primary
  aspect: ''
- target: '[[concepts/bandit-algorithm]]'
  role: primary
  aspect: ''
- target: '[[concepts/ucb1-algorithm]]'
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

# Exercise 1.5(a)

Take any bandit algorithm A for fixed time horizon T. Convert it to an algorithm A_∞ which runs forever, in phases i = 1, 2, 3, ... of 2^i rounds each. In each phase i algorithm A is restarted and run with time horizon 2^i. State and prove a theorem which converts an instance-independent upper bound on regret for A into similar bound for A_∞ (so that this theorem applies to both UCB1 and Explore-first).
