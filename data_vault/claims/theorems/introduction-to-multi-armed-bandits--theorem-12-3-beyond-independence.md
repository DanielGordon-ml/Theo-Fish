---
slug: introduction-to-multi-armed-bandits--theorem-12-3-beyond-independence
label: Theorem 12.3 (Beyond independence)
claim_type: theorem
statement: Consider random variables X_1, X_2, … ∈ [0,1] that are not necessarily
  independent or identically distributed. For each i ∈ [n], posit a number μ_i ∈ [0,1]
  such that E[X_i | X_1 ∈ J_1, …, X_{i-1} ∈ J_{i-1}] = μ_i, for any intervals J_1,
  …, J_{i-1} ⊂ [0,1]. Then Eq. (174) holds, with β=4. That is, Pr[|X̄_n − μ_n| ≤ √(4α·log(T)/n)]
  ≥ 1 − 2·T^{−2α} for all α > 0.
proof: ''
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/expected-average]]'
- '[[concepts/confidence-radius]]'
- '[[concepts/sample-average]]'
- '[[concepts/martingale-assumption]]'
- '[[concepts/concentration-inequality]]'
- '[[concepts/high-probability-event]]'
- '[[concepts/bounded-support]]'
about_meta:
- target: '[[concepts/expected-average]]'
  role: primary
  aspect: ''
- target: '[[concepts/confidence-radius]]'
  role: primary
  aspect: ''
- target: '[[concepts/sample-average]]'
  role: primary
  aspect: ''
- target: '[[concepts/martingale-assumption]]'
  role: primary
  aspect: ''
- target: '[[concepts/concentration-inequality]]'
  role: primary
  aspect: ''
- target: '[[concepts/high-probability-event]]'
  role: primary
  aspect: ''
- target: '[[concepts/bounded-support]]'
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

# Theorem 12.3 (Beyond independence)

Consider random variables X_1, X_2, … ∈ [0,1] that are not necessarily independent or identically distributed. For each i ∈ [n], posit a number μ_i ∈ [0,1] such that E[X_i | X_1 ∈ J_1, …, X_{i-1} ∈ J_{i-1}] = μ_i, for any intervals J_1, …, J_{i-1} ⊂ [0,1]. Then Eq. (174) holds, with β=4. That is, Pr[|X̄_n − μ_n| ≤ √(4α·log(T)/n)] ≥ 1 − 2·T^{−2α} for all α > 0.
