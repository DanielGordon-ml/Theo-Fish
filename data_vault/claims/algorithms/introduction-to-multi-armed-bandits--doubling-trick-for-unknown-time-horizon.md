---
slug: introduction-to-multi-armed-bandits--doubling-trick-for-unknown-time-horizon
label: Doubling trick for unknown time horizon
claim_type: algorithm
statement: Any algorithm for known time horizon can (usually) be converted to an algorithm
  for an arbitrary time horizon using the doubling trick. Here, the new algorithm
  proceeds in phases of exponential duration. Each phase i=1,2,… lasts 2^i rounds,
  and executes a fresh run of the original algorithm. This approach achieves the 'right'
  theoretical guarantees (see Exercise 1.5).
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/doubling-trick]]'
- '[[concepts/bandit-algorithm]]'
- '[[concepts/regret-bound]]'
- '[[concepts/time-horizon-t]]'
about_meta:
- target: '[[concepts/doubling-trick]]'
  role: primary
  aspect: ''
- target: '[[concepts/bandit-algorithm]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret-bound]]'
  role: primary
  aspect: ''
- target: '[[concepts/time-horizon-t]]'
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

# Doubling trick for unknown time horizon

Any algorithm for known time horizon can (usually) be converted to an algorithm for an arbitrary time horizon using the doubling trick. Here, the new algorithm proceeds in phases of exponential duration. Each phase i=1,2,… lasts 2^i rounds, and executes a fresh run of the original algorithm. This approach achieves the 'right' theoretical guarantees (see Exercise 1.5).
