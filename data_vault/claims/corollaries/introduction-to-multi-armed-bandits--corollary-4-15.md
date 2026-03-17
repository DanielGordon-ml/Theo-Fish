---
slug: introduction-to-multi-armed-bandits--corollary-4-15
label: Corollary 4.15
claim_type: corollary
statement: For any two active arms x, y, we have D(x,y) > 1/3 min(Δ(x), Δ(y)).
proof: W.l.o.g. assume that x has been activated before y. Let s be the time when
  y has been activated. Then D(x,y) > r_s(x) by the activation rule. And r_s(x) ≥
  Δ(x)/3 by Lemma 4.14.
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/activation-rule]]'
- '[[concepts/gap-d-a]]'
- '[[concepts/metric-d]]'
- '[[concepts/zooming-algorithm-for-lipschitz-bandits]]'
about_meta:
- target: '[[concepts/activation-rule]]'
  role: primary
  aspect: ''
- target: '[[concepts/gap-d-a]]'
  role: primary
  aspect: ''
- target: '[[concepts/metric-d]]'
  role: primary
  aspect: ''
- target: '[[concepts/zooming-algorithm-for-lipschitz-bandits]]'
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

# Corollary 4.15

For any two active arms x, y, we have D(x,y) > 1/3 min(Δ(x), Δ(y)).


## Proof

W.l.o.g. assume that x has been activated before y. Let s be the time when y has been activated. Then D(x,y) > r_s(x) by the activation rule. And r_s(x) ≥ Δ(x)/3 by Lemma 4.14.
