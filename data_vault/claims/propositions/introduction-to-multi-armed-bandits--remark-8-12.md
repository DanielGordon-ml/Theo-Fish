---
slug: introduction-to-multi-armed-bandits--remark-8-12
label: Remark 8.12
claim_type: proposition
statement: How many data points do we need to evaluate M policies simultaneously?
  Suppose we have some fixed parameters ε, δ > 0 in mind, and want to ensure that
  Pr[|IPS(π) − μ(π)| ≤ ε for each policy π] > 1 − δ. Taking a union bound over (112),
  it suffices to take N ~ √(log(M/δ)) / (p₀ · ε²).
proof: Taking a union bound over (112) for all M policies yields the result.
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/ips-estimator]]'
- '[[concepts/sample-complexity]]'
- '[[concepts/minimum-sampling-probability]]'
- '[[concepts/policy-value]]'
- '[[concepts/policy-evaluation-and-training]]'
about_meta:
- target: '[[concepts/ips-estimator]]'
  role: primary
  aspect: ''
- target: '[[concepts/sample-complexity]]'
  role: primary
  aspect: ''
- target: '[[concepts/minimum-sampling-probability]]'
  role: primary
  aspect: ''
- target: '[[concepts/policy-value]]'
  role: primary
  aspect: ''
- target: '[[concepts/policy-evaluation-and-training]]'
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

# Remark 8.12

How many data points do we need to evaluate M policies simultaneously? Suppose we have some fixed parameters ε, δ > 0 in mind, and want to ensure that Pr[|IPS(π) − μ(π)| ≤ ε for each policy π] > 1 − δ. Taking a union bound over (112), it suffices to take N ~ √(log(M/δ)) / (p₀ · ε²).


## Proof

Taking a union bound over (112) for all M policies yields the result.
