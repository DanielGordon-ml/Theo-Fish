---
slug: introduction-to-multi-armed-bandits--lemma-8-13
label: Lemma 8.13
claim_type: lemma
statement: 'Assume rewards r̃_t(·) are chosen by a deterministic oblivious adversary.
  Then we have E[IPS(π)] = r̃(π) for each policy π. Moreover, for each δ > 0, with
  probability at least 1 − δ we have: |IPS(π) − r̃(π)| ≤ O(√(1/p₀ · log(1/δ)/N)),
  where p₀ = min_{t,a} p_t(a).'
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/ips-estimator]]'
- '[[concepts/minimum-sampling-probability]]'
- '[[concepts/realized-policy-value]]'
- '[[concepts/deterministic-oblivious-adversary]]'
- '[[concepts/concentration-inequality]]'
- '[[concepts/contextual-bandit-problem]]'
about_meta:
- target: '[[concepts/ips-estimator]]'
  role: primary
  aspect: ''
- target: '[[concepts/minimum-sampling-probability]]'
  role: primary
  aspect: ''
- target: '[[concepts/realized-policy-value]]'
  role: primary
  aspect: ''
- target: '[[concepts/deterministic-oblivious-adversary]]'
  role: primary
  aspect: ''
- target: '[[concepts/concentration-inequality]]'
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

# Lemma 8.13

Assume rewards r̃_t(·) are chosen by a deterministic oblivious adversary. Then we have E[IPS(π)] = r̃(π) for each policy π. Moreover, for each δ > 0, with probability at least 1 − δ we have: |IPS(π) − r̃(π)| ≤ O(√(1/p₀ · log(1/δ)/N)), where p₀ = min_{t,a} p_t(a).
