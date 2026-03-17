---
slug: introduction-to-multi-armed-bandits--theorem-12-2-extensions
label: Theorem 12.2 (Extensions)
claim_type: theorem
statement: 'Eq. (174) holds, for appropriate β, in the following cases: (a) Bounded
  intervals: X_i ∈ [a_i, b_i] for all i ∈ [n], and β = (1/n)∑_{i∈[n]} (b_i − a_i)^2.
  (b) Bounded variance: X_i ∈ [0,1] and Variance(X_i) ≤ β/8 for all i ∈ [n]. (c) Gaussians:
  Each X_i, i ∈ [n] is Gaussian with variance at most β/4.'
proof: ''
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/concentration-inequality]]'
- '[[concepts/variance]]'
- '[[concepts/gaussian-random-variable]]'
- '[[concepts/high-probability-event]]'
- '[[concepts/bounded-support]]'
- '[[concepts/confidence-radius]]'
- '[[concepts/mutual-independence]]'
about_meta:
- target: '[[concepts/concentration-inequality]]'
  role: primary
  aspect: ''
- target: '[[concepts/variance]]'
  role: primary
  aspect: ''
- target: '[[concepts/gaussian-random-variable]]'
  role: primary
  aspect: ''
- target: '[[concepts/high-probability-event]]'
  role: primary
  aspect: ''
- target: '[[concepts/bounded-support]]'
  role: primary
  aspect: ''
- target: '[[concepts/confidence-radius]]'
  role: primary
  aspect: ''
- target: '[[concepts/mutual-independence]]'
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

# Theorem 12.2 (Extensions)

Eq. (174) holds, for appropriate β, in the following cases: (a) Bounded intervals: X_i ∈ [a_i, b_i] for all i ∈ [n], and β = (1/n)∑_{i∈[n]} (b_i − a_i)^2. (b) Bounded variance: X_i ∈ [0,1] and Variance(X_i) ≤ β/8 for all i ∈ [n]. (c) Gaussians: Each X_i, i ∈ [n] is Gaussian with variance at most β/4.
