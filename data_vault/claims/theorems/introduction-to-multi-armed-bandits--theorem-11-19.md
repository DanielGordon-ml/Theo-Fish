---
slug: introduction-to-multi-armed-bandits--theorem-11-19
label: Theorem 11.19
claim_type: theorem
statement: Suppose ties in Definition 11.4 are always resolved in favor of arm 1 (i.e.,
  imply rec_t = 1). Absent (170), any BIC algorithm never plays arm 2.
proof: 'Suppose Property (170) does not hold. Let ALG be a strongly BIC algorithm.
  We prove by induction on t that ALG cannot recommend arm 2 to agent t.


  This is trivially true for t=1. Suppose the induction hypothesis is true for some
  t. Then the decision whether to recommend arm 2 in round t+1 (i.e., whether a_{t+1}=2)
  is determined by the first t outcomes of arm 1 and the algorithm''s random seed.
  Letting U = {a_{t+1}=2}, we have


  E[μ_2 - μ_1 | U] = E[ E[μ_2 - μ_1 | S_{1,t}] | U ]  (by Fact 11.6)

  = E[G_{1,t} | U]  (by definition of G_{1,t})

  ≤ 0  (since (170) does not hold).


  The last inequality holds because the negation of (170) implies Pr[G_{1,t} ≤ 0]
  = 1. This contradicts ALG being BIC, and completes the induction proof.'
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/bic-bayesian-incentive-compatible]]'
- '[[concepts/bic-algorithm]]'
- '[[concepts/bic-property]]'
- '[[concepts/posterior-gap]]'
- '[[concepts/incentivized-exploration-bandit-problem]]'
about_meta:
- target: '[[concepts/bic-bayesian-incentive-compatible]]'
  role: primary
  aspect: ''
- target: '[[concepts/bic-algorithm]]'
  role: primary
  aspect: ''
- target: '[[concepts/bic-property]]'
  role: primary
  aspect: ''
- target: '[[concepts/posterior-gap]]'
  role: primary
  aspect: ''
- target: '[[concepts/incentivized-exploration-bandit-problem]]'
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

# Theorem 11.19

Suppose ties in Definition 11.4 are always resolved in favor of arm 1 (i.e., imply rec_t = 1). Absent (170), any BIC algorithm never plays arm 2.


## Proof

Suppose Property (170) does not hold. Let ALG be a strongly BIC algorithm. We prove by induction on t that ALG cannot recommend arm 2 to agent t.

This is trivially true for t=1. Suppose the induction hypothesis is true for some t. Then the decision whether to recommend arm 2 in round t+1 (i.e., whether a_{t+1}=2) is determined by the first t outcomes of arm 1 and the algorithm's random seed. Letting U = {a_{t+1}=2}, we have

E[μ_2 - μ_1 | U] = E[ E[μ_2 - μ_1 | S_{1,t}] | U ]  (by Fact 11.6)
= E[G_{1,t} | U]  (by definition of G_{1,t})
≤ 0  (since (170) does not hold).

The last inequality holds because the negation of (170) implies Pr[G_{1,t} ≤ 0] = 1. This contradicts ALG being BIC, and completes the induction proof.
