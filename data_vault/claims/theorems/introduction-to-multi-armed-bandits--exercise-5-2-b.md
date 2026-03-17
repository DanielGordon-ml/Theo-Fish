---
slug: introduction-to-multi-armed-bandits--exercise-5-2-b
label: Exercise 5.2(b)
claim_type: theorem
statement: There exists a problem instance with a deterministic adversary and IID
  costs for which any algorithm suffers regret E[cost(ALG) - min_{a ∈ [K]} cost(a)]
  ≥ Ω(√(T log K)).
proof: 'Assume all arms have 0-1 costs with mean 1/2. Use the following fact about
  random walks: E[min_a cost(a)] ≤ T/2 - Ω(√(T log K)). Since each arm has expected
  cost T/2, any algorithm achieves expected cost at least T/2, so regret is at least
  T/2 - (T/2 - Ω(√(T log K))) = Ω(√(T log K)). [Proof sketch from hint; full proof
  left as exercise.]'
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/deterministic-oblivious-adversary]]'
- '[[concepts/number-of-experts-k]]'
- '[[concepts/number-of-rounds-t]]'
- '[[concepts/0-1-costs]]'
- '[[concepts/hedge]]'
- '[[concepts/regret]]'
- '[[concepts/iid-costs]]'
about_meta:
- target: '[[concepts/deterministic-oblivious-adversary]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-experts-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-rounds-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/0-1-costs]]'
  role: primary
  aspect: ''
- target: '[[concepts/hedge]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/iid-costs]]'
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

# Exercise 5.2(b)

There exists a problem instance with a deterministic adversary and IID costs for which any algorithm suffers regret E[cost(ALG) - min_{a ∈ [K]} cost(a)] ≥ Ω(√(T log K)).


## Proof

Assume all arms have 0-1 costs with mean 1/2. Use the following fact about random walks: E[min_a cost(a)] ≤ T/2 - Ω(√(T log K)). Since each arm has expected cost T/2, any algorithm achieves expected cost at least T/2, so regret is at least T/2 - (T/2 - Ω(√(T log K))) = Ω(√(T log K)). [Proof sketch from hint; full proof left as exercise.]
