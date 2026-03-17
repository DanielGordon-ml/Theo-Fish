---
slug: introduction-to-multi-armed-bandits--equation-25
label: Equation (25)
claim_type: lemma
statement: There are ≥ 2K/3 arms j such that E_0(T_j) ≤ 3T/K.
proof: Assume for contradiction that we have more than K/3 arms with E_0(T_j) > 3T/K.
  Then the expected total number of times these arms are played is strictly greater
  than T, which is a contradiction.
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/expected-plays-e0-t-j]]'
- '[[concepts/problem-instance-i-0]]'
- '[[concepts/number-of-arms-k]]'
about_meta:
- target: '[[concepts/expected-plays-e0-t-j]]'
  role: primary
  aspect: ''
- target: '[[concepts/problem-instance-i-0]]'
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

# Equation (25)

There are ≥ 2K/3 arms j such that E_0(T_j) ≤ 3T/K.


## Proof

Assume for contradiction that we have more than K/3 arms with E_0(T_j) > 3T/K. Then the expected total number of times these arms are played is strictly greater than T, which is a contradiction.
