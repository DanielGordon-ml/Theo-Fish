---
slug: introduction-to-multi-armed-bandits--theorem-12-1-hoeffding-inequality
label: Theorem 12.1 (Hoeffding Inequality)
claim_type: theorem
statement: Eq. (174) holds, with β=1, if X_1, …, X_n ∈ [0,1]. That is, Pr[ℰ_{α,β}]
  ≥ 1 − 2·T^{−2α}, ∀α>0, where ℰ_{α,β} := {|X̄_n − μ_n| ≤ √(α·β·log(T)/n)}, with β=1,
  provided X_1, …, X_n ∈ [0,1] are mutually independent.
proof: ''
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/sample-average]]'
- '[[concepts/concentration-inequality]]'
- '[[concepts/mutual-independence]]'
- '[[concepts/number-of-samples-n]]'
- '[[concepts/expected-average]]'
- '[[concepts/confidence-interval]]'
- '[[concepts/bounded-support]]'
- '[[concepts/confidence-radius]]'
- '[[concepts/high-probability-event]]'
- '[[concepts/hoeffding-inequality]]'
about_meta:
- target: '[[concepts/sample-average]]'
  role: primary
  aspect: ''
- target: '[[concepts/concentration-inequality]]'
  role: primary
  aspect: ''
- target: '[[concepts/mutual-independence]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-samples-n]]'
  role: primary
  aspect: ''
- target: '[[concepts/expected-average]]'
  role: primary
  aspect: ''
- target: '[[concepts/confidence-interval]]'
  role: primary
  aspect: ''
- target: '[[concepts/bounded-support]]'
  role: primary
  aspect: ''
- target: '[[concepts/confidence-radius]]'
  role: primary
  aspect: ''
- target: '[[concepts/high-probability-event]]'
  role: primary
  aspect: ''
- target: '[[concepts/hoeffding-inequality]]'
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

# Theorem 12.1 (Hoeffding Inequality)

Eq. (174) holds, with β=1, if X_1, …, X_n ∈ [0,1]. That is, Pr[ℰ_{α,β}] ≥ 1 − 2·T^{−2α}, ∀α>0, where ℰ_{α,β} := {|X̄_n − μ_n| ≤ √(α·β·log(T)/n)}, with β=1, provided X_1, …, X_n ∈ [0,1] are mutually independent.
