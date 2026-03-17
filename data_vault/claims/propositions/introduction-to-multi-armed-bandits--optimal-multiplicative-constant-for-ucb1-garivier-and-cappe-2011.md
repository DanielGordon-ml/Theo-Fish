---
slug: introduction-to-multi-armed-bandits--optimal-multiplicative-constant-for-ucb1-garivier-and-cappe-2011
label: Optimal multiplicative constant for UCB1 (Garivier and Cappé 2011)
claim_type: proposition
statement: Garivier and Cappé (2011) derive the constant α/(2 ln 2), using confidence
  radius r_t(a) = √(α · ln(t) / n_t(a)) with any α > 1. The original analysis in Auer
  et al. (2002a) obtained constant 8/(ln 2) using α = 2.
proof: ''
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/ucb1-algorithm]]'
- '[[concepts/leading-constant]]'
- '[[concepts/regret-bound]]'
- '[[concepts/confidence-radius-r-t-a]]'
about_meta:
- target: '[[concepts/ucb1-algorithm]]'
  role: primary
  aspect: ''
- target: '[[concepts/leading-constant]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret-bound]]'
  role: primary
  aspect: ''
- target: '[[concepts/confidence-radius-r-t-a]]'
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

# Optimal multiplicative constant for UCB1 (Garivier and Cappé 2011)

Garivier and Cappé (2011) derive the constant α/(2 ln 2), using confidence radius r_t(a) = √(α · ln(t) / n_t(a)) with any α > 1. The original analysis in Auer et al. (2002a) obtained constant 8/(ln 2) using α = 2.
