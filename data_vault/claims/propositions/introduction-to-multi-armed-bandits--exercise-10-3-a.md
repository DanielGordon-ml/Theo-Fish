---
slug: introduction-to-multi-armed-bandits--exercise-10-3-a
label: Exercise 10.3(a)
claim_type: proposition
statement: 'Consider dynamic pricing with limited supply of d products: actions are
  price vectors p ∈ [0,1]^d, and c_i(p) ∈ [0,1] is the expected per-round amount of
  product i sold at price vector p. Let P_ε := [0,1]^d ∩ ε N^d be a uniform mesh of
  prices with step ε ∈ (0,1). Assume that c_i(p) is Lipschitz in p, for each product
  i: |c_i(p) - c_i(p'')| ≤ L · ||p - p''||_1 for all p, p'' ∈ [0,1]^d. Then the discretization
  error is OPT - OPT(P_ε) ≤ O(ε dL). Using an optimal BwK algorithm with action set
  P_ε, one obtains regret rate OPT - E[REW] < Õ(T^{(d+1)/(d+2)}).'
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/discretization-error]]'
- '[[concepts/p-epsilon]]'
- '[[concepts/bandits-with-knapsacks]]'
- '[[concepts/lipschitz-condition]]'
- '[[concepts/dynamic-pricing-problem]]'
about_meta:
- target: '[[concepts/discretization-error]]'
  role: primary
  aspect: ''
- target: '[[concepts/p-epsilon]]'
  role: primary
  aspect: ''
- target: '[[concepts/bandits-with-knapsacks]]'
  role: primary
  aspect: ''
- target: '[[concepts/lipschitz-condition]]'
  role: primary
  aspect: ''
- target: '[[concepts/dynamic-pricing-problem]]'
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

# Exercise 10.3(a)

Consider dynamic pricing with limited supply of d products: actions are price vectors p ∈ [0,1]^d, and c_i(p) ∈ [0,1] is the expected per-round amount of product i sold at price vector p. Let P_ε := [0,1]^d ∩ ε N^d be a uniform mesh of prices with step ε ∈ (0,1). Assume that c_i(p) is Lipschitz in p, for each product i: |c_i(p) - c_i(p')| ≤ L · ||p - p'||_1 for all p, p' ∈ [0,1]^d. Then the discretization error is OPT - OPT(P_ε) ≤ O(ε dL). Using an optimal BwK algorithm with action set P_ε, one obtains regret rate OPT - E[REW] < Õ(T^{(d+1)/(d+2)}).
