---
slug: introduction-to-multi-armed-bandits--exercise-5-2-a
label: Exercise 5.2(a)
claim_type: lemma
statement: Assume IID costs. Then min_a E[cost(a)] ≤ E[min_a cost(a)] + O(√(T log(KT))).
proof: 'Define the "clean event" as follows: the event in Hoeffding inequality holds
  for the cost sequence of each arm. [Proof sketch from hint; full proof left as exercise.]'
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/iid-costs]]'
- '[[concepts/regret]]'
- '[[concepts/hoeffding-inequality]]'
- '[[concepts/clean-event]]'
- '[[concepts/number-of-experts-k]]'
- '[[concepts/number-of-rounds-t]]'
about_meta:
- target: '[[concepts/iid-costs]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/hoeffding-inequality]]'
  role: primary
  aspect: ''
- target: '[[concepts/clean-event]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-experts-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-rounds-t]]'
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

# Exercise 5.2(a)

Assume IID costs. Then min_a E[cost(a)] ≤ E[min_a cost(a)] + O(√(T log(KT))).


## Proof

Define the "clean event" as follows: the event in Hoeffding inequality holds for the cost sequence of each arm. [Proof sketch from hint; full proof left as exercise.]
