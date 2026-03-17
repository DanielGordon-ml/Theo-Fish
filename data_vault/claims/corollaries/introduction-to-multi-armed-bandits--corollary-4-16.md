---
slug: introduction-to-multi-armed-bandits--corollary-4-16
label: Corollary 4.16
claim_type: corollary
statement: For each arm x, we have n(x) ≤ O(log T) Δ⁻²(x).
proof: Use Lemma 4.14 for t = T, and plug in the definition of the confidence radius.
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/sample-count]]'
- '[[concepts/confidence-radius-r-t-a]]'
- '[[concepts/zooming-algorithm-for-lipschitz-bandits]]'
- '[[concepts/gap-d-a]]'
about_meta:
- target: '[[concepts/sample-count]]'
  role: primary
  aspect: ''
- target: '[[concepts/confidence-radius-r-t-a]]'
  role: primary
  aspect: ''
- target: '[[concepts/zooming-algorithm-for-lipschitz-bandits]]'
  role: primary
  aspect: ''
- target: '[[concepts/gap-d-a]]'
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

# Corollary 4.16

For each arm x, we have n(x) ≤ O(log T) Δ⁻²(x).


## Proof

Use Lemma 4.14 for t = T, and plug in the definition of the confidence radius.
