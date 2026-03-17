---
slug: introduction-to-multi-armed-bandits--equation-27
label: Equation (27)
claim_type: lemma
statement: There are at least K/3 arms j such that Pr[T_j ≤ 24T/K] ≥ 7/8 and P_0(y_T
  = j) ≤ 3/K.
proof: By Markov inequality, E_0(T_j) ≤ 3T/K implies that Pr[T_j ≤ 24T/K] ≥ 7/8. Since
  the sets of arms in (25) and (26) must overlap on at least K/3 arms (each has at
  least 2K/3 arms out of K total), we conclude the result.
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/probability-p0-yt-equals-j]]'
- '[[concepts/number-of-arms-k]]'
- '[[concepts/expected-plays-e0-t-j]]'
about_meta:
- target: '[[concepts/probability-p0-yt-equals-j]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-arms-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/expected-plays-e0-t-j]]'
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

# Equation (27)

There are at least K/3 arms j such that Pr[T_j ≤ 24T/K] ≥ 7/8 and P_0(y_T = j) ≤ 3/K.


## Proof

By Markov inequality, E_0(T_j) ≤ 3T/K implies that Pr[T_j ≤ 24T/K] ≥ 7/8. Since the sets of arms in (25) and (26) must overlap on at least K/3 arms (each has at least 2K/3 arms out of K total), we conclude the result.
