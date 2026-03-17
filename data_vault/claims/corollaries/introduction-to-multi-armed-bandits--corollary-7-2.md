---
slug: introduction-to-multi-armed-bandits--corollary-7-2
label: Corollary 7.2
claim_type: corollary
statement: 'If ALG is Hedge in the theorem above, one can take f(T,K,u) = O(u · √(T
  ln K)) by Theorem 5.16. Then, setting γ = T^{-1/4} √(u · log K), Algorithm 1 achieves
  regret


  E[R(T)] ≤ O(T^{3/4} √(u · log K)).'
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/gamma]]'
- '[[concepts/u-bounded]]'
- '[[concepts/regret]]'
- '[[concepts/adversarial-bandits-problem]]'
- '[[concepts/hedge]]'
about_meta:
- target: '[[concepts/gamma]]'
  role: primary
  aspect: ''
- target: '[[concepts/u-bounded]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/adversarial-bandits-problem]]'
  role: primary
  aspect: ''
- target: '[[concepts/hedge]]'
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

# Corollary 7.2

If ALG is Hedge in the theorem above, one can take f(T,K,u) = O(u · √(T ln K)) by Theorem 5.16. Then, setting γ = T^{-1/4} √(u · log K), Algorithm 1 achieves regret

E[R(T)] ≤ O(T^{3/4} √(u · log K)).
