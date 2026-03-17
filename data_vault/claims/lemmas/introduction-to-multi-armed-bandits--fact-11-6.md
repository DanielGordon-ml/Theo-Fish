---
slug: introduction-to-multi-armed-bandits--fact-11-6
label: Fact 11.6
claim_type: lemma
statement: Suppose random variable Z is determined by Y and some other random variable
  Z_0 such that X and Z_0 are independent (think of Z_0 as algorithm's random seed).
  Then E[E[X|Y] | Z] = E[X|Z].
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/random-variable]]'
- '[[concepts/conditional-expectation-operator]]'
- '[[concepts/independence]]'
about_meta:
- target: '[[concepts/random-variable]]'
  role: primary
  aspect: ''
- target: '[[concepts/conditional-expectation-operator]]'
  role: primary
  aspect: ''
- target: '[[concepts/independence]]'
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

# Fact 11.6

Suppose random variable Z is determined by Y and some other random variable Z_0 such that X and Z_0 are independent (think of Z_0 as algorithm's random seed). Then E[E[X|Y] | Z] = E[X|Z].
