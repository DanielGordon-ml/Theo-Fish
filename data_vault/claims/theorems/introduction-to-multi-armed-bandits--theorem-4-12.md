---
slug: introduction-to-multi-armed-bandits--theorem-4-12
label: Theorem 4.12
claim_type: theorem
statement: 'Consider Lipschitz bandits on metric space ([0,1], ℓ_2^{1/d}), for any
  d ≥ 1, with time horizon T. For any algorithm, there exists a problem instance ℐ
  such that


  𝔼[R(T) | ℐ] ≥ Ω(T^{(d+1)/(d+2)}).'
proof: ''
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/expected-regret-r-t]]'
- '[[concepts/covering-dimension]]'
- '[[concepts/lower-bound-on-regret]]'
- '[[concepts/lipschitz-bandits-problem]]'
about_meta:
- target: '[[concepts/expected-regret-r-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/covering-dimension]]'
  role: primary
  aspect: ''
- target: '[[concepts/lower-bound-on-regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/lipschitz-bandits-problem]]'
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

# Theorem 4.12

Consider Lipschitz bandits on metric space ([0,1], ℓ_2^{1/d}), for any d ≥ 1, with time horizon T. For any algorithm, there exists a problem instance ℐ such that

𝔼[R(T) | ℐ] ≥ Ω(T^{(d+1)/(d+2)}).
