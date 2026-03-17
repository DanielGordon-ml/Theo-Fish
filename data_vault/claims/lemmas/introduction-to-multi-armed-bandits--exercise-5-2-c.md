---
slug: introduction-to-multi-armed-bandits--exercise-5-2-c
label: Exercise 5.2(c)
claim_type: lemma
statement: Algorithms UCB and Successive Elimination achieve logarithmic regret bound
  (11) even for regret (not just pseudo-regret), assuming IID costs and that the best-in-foresight
  arm a* is unique.
proof: Under the "clean event", cost(a) < T · μ(a) + O(√(T log T)) for each arm a
  ≠ a*, where μ(a) is the mean cost. It follows that a* is also the best-in-hindsight
  arm, unless μ(a) - μ(a*) < O(√(T log T)) for some arm a ≠ a* (in which case the
  claimed regret bound holds trivially). [Proof sketch from hint; full proof left
  as exercise.]
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/ucb1-algorithm]]'
- '[[concepts/iid-costs]]'
- '[[concepts/regret]]'
- '[[concepts/clean-event]]'
- '[[concepts/successive-elimination-algorithm]]'
- '[[concepts/best-in-foresight-arm]]'
- '[[concepts/best-in-hindsight-arm]]'
about_meta:
- target: '[[concepts/ucb1-algorithm]]'
  role: primary
  aspect: ''
- target: '[[concepts/iid-costs]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/clean-event]]'
  role: primary
  aspect: ''
- target: '[[concepts/successive-elimination-algorithm]]'
  role: primary
  aspect: ''
- target: '[[concepts/best-in-foresight-arm]]'
  role: primary
  aspect: ''
- target: '[[concepts/best-in-hindsight-arm]]'
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

# Exercise 5.2(c)

Algorithms UCB and Successive Elimination achieve logarithmic regret bound (11) even for regret (not just pseudo-regret), assuming IID costs and that the best-in-foresight arm a* is unique.


## Proof

Under the "clean event", cost(a) < T · μ(a) + O(√(T log T)) for each arm a ≠ a*, where μ(a) is the mean cost. It follows that a* is also the best-in-hindsight arm, unless μ(a) - μ(a*) < O(√(T log T)) for some arm a ≠ a* (in which case the claimed regret bound holds trivially). [Proof sketch from hint; full proof left as exercise.]
