---
slug: introduction-to-multi-armed-bandits--exercise-6-2-a-discretization-error-under-lipschitz-property
label: Exercise 6.2(a) (discretization error under Lipschitz property)
claim_type: conjecture
statement: 'Consider adversarial bandits with the set of arms A=[0,1]. Fix ε>0 and
  let S_ε be the ε-uniform mesh over A. Prove that DE(S_ε) ≤ Lε, assuming Lipschitz
  property: |c_t(a) - c_t(a'')| ≤ L·|a - a''| for all arms a,a'' ∈ A and all rounds
  t.'
proof: ''
strength: ''
status: exercise
human_notes: ''
about:
- '[[concepts/lipschitz-condition]]'
- '[[concepts/epsilon-uniform-mesh]]'
- '[[concepts/continuous-arm-space]]'
- '[[concepts/adversarial-bandits-problem]]'
- '[[concepts/discretization-error]]'
about_meta:
- target: '[[concepts/lipschitz-condition]]'
  role: primary
  aspect: ''
- target: '[[concepts/epsilon-uniform-mesh]]'
  role: primary
  aspect: ''
- target: '[[concepts/continuous-arm-space]]'
  role: primary
  aspect: ''
- target: '[[concepts/adversarial-bandits-problem]]'
  role: primary
  aspect: ''
- target: '[[concepts/discretization-error]]'
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

# Exercise 6.2(a) (discretization error under Lipschitz property)

Consider adversarial bandits with the set of arms A=[0,1]. Fix ε>0 and let S_ε be the ε-uniform mesh over A. Prove that DE(S_ε) ≤ Lε, assuming Lipschitz property: |c_t(a) - c_t(a')| ≤ L·|a - a'| for all arms a,a' ∈ A and all rounds t.
