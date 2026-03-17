---
slug: introduction-to-multi-armed-bandits--corollary-8-14
label: Corollary 8.14
claim_type: corollary
statement: Consider the setting in Lemma 8.13. Fix policy class Π and let π₀ ∈ argmax_{π∈Π}
  IPS(π). Then for each δ > 0, with probability at least 1 − δ we have max_{π∈Π} r̃(π)
  − r̃(π₀) ≤ O(√(1/p₀ · log(|Π|/δ)/N)).
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/minimum-sampling-probability]]'
- '[[concepts/policy-evaluation-and-training]]'
- '[[concepts/contextual-bandit-problem]]'
- '[[concepts/ips-estimator]]'
- '[[concepts/realized-policy-value]]'
- '[[concepts/classification-oracle]]'
- '[[concepts/policy-class]]'
about_meta:
- target: '[[concepts/minimum-sampling-probability]]'
  role: primary
  aspect: ''
- target: '[[concepts/policy-evaluation-and-training]]'
  role: primary
  aspect: ''
- target: '[[concepts/contextual-bandit-problem]]'
  role: primary
  aspect: ''
- target: '[[concepts/ips-estimator]]'
  role: primary
  aspect: ''
- target: '[[concepts/realized-policy-value]]'
  role: primary
  aspect: ''
- target: '[[concepts/classification-oracle]]'
  role: primary
  aspect: ''
- target: '[[concepts/policy-class]]'
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

# Corollary 8.14

Consider the setting in Lemma 8.13. Fix policy class Π and let π₀ ∈ argmax_{π∈Π} IPS(π). Then for each δ > 0, with probability at least 1 − δ we have max_{π∈Π} r̃(π) − r̃(π₀) ≤ O(√(1/p₀ · log(|Π|/δ)/N)).
