---
slug: introduction-to-multi-armed-bandits--confidence-sum-bound-eq-152
label: Confidence Sum Bound (Eq. 152)
claim_type: lemma
statement: For a particular version of confidence radius rad_t(a) and any bandit algorithm,
  it holds that ∑_{t∈S} rad_t(a_t) ≤ √(β|S|) for all subsets of rounds S ⊂ [T], where
  β is some application-specific parameter. Eq. (152) holds with β = K for stochastic
  bandits.
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/beta]]'
- '[[concepts/confidence-sum]]'
- '[[concepts/ucb1-algorithm]]'
- '[[concepts/confidence-radius-rad-t]]'
- '[[concepts/stochastic-bandits]]'
- '[[concepts/set-of-rounds-t]]'
about_meta:
- target: '[[concepts/beta]]'
  role: primary
  aspect: ''
- target: '[[concepts/confidence-sum]]'
  role: primary
  aspect: ''
- target: '[[concepts/ucb1-algorithm]]'
  role: primary
  aspect: ''
- target: '[[concepts/confidence-radius-rad-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/stochastic-bandits]]'
  role: primary
  aspect: ''
- target: '[[concepts/set-of-rounds-t]]'
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

# Confidence Sum Bound (Eq. 152)

For a particular version of confidence radius rad_t(a) and any bandit algorithm, it holds that ∑_{t∈S} rad_t(a_t) ≤ √(β|S|) for all subsets of rounds S ⊂ [T], where β is some application-specific parameter. Eq. (152) holds with β = K for stochastic bandits.
