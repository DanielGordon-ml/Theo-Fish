---
slug: introduction-to-multi-armed-bandits--lemma-8-11
label: Lemma 8.11
claim_type: lemma
statement: 'The IPS estimator is unbiased: E[IPS(π)] = μ(π) for each policy π. Moreover,
  the IPS estimator is accurate with high probability: for each δ > 0, with probability
  at least 1 − δ, |IPS(π) − μ(π)| ≤ O(√(1/p₀ · log(1/δ)/N)), where p₀ = min_{t,a}
  p_t(a).'
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/minimum-sampling-probability]]'
- '[[concepts/unbiasedness]]'
- '[[concepts/policy-value]]'
- '[[concepts/policy-evaluation]]'
- '[[concepts/ips-estimator]]'
- '[[concepts/contextual-bandit-problem]]'
about_meta:
- target: '[[concepts/minimum-sampling-probability]]'
  role: primary
  aspect: ''
- target: '[[concepts/unbiasedness]]'
  role: primary
  aspect: ''
- target: '[[concepts/policy-value]]'
  role: primary
  aspect: ''
- target: '[[concepts/policy-evaluation]]'
  role: primary
  aspect: ''
- target: '[[concepts/ips-estimator]]'
  role: primary
  aspect: ''
- target: '[[concepts/contextual-bandit-problem]]'
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

# Lemma 8.11

The IPS estimator is unbiased: E[IPS(π)] = μ(π) for each policy π. Moreover, the IPS estimator is accurate with high probability: for each δ > 0, with probability at least 1 − δ, |IPS(π) − μ(π)| ≤ O(√(1/p₀ · log(1/δ)/N)), where p₀ = min_{t,a} p_t(a).
