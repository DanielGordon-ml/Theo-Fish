---
slug: introduction-to-multi-armed-bandits--exercise-4-4-b
label: Exercise 4.4(b)
claim_type: proposition
statement: Consider Lipschitz bandits in a metric space $(X,\mathcal{D})$. Fix $d<\mathtt{COV}_{c}(X)$
  for some fixed absolute constant $c>0$. Assume $N_{\epsilon}(X)\geq c'\cdot\epsilon^{-d}$
  holds for all $\epsilon>0$. Then for each $T$ there is a problem instance such that
  $\operatornamewithlimits{\mathbb{E}}[R(T)]\geq\Omega(T^{(d+1)/(d+2)})$.
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/covering-dimension]]'
- '[[concepts/covering-number]]'
- '[[concepts/expected-regret]]'
- '[[concepts/lipschitz-bandits-problem]]'
about_meta:
- target: '[[concepts/covering-dimension]]'
  role: primary
  aspect: ''
- target: '[[concepts/covering-number]]'
  role: primary
  aspect: ''
- target: '[[concepts/expected-regret]]'
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

# Exercise 4.4(b)

Consider Lipschitz bandits in a metric space $(X,\mathcal{D})$. Fix $d<\mathtt{COV}_{c}(X)$ for some fixed absolute constant $c>0$. Assume $N_{\epsilon}(X)\geq c'\cdot\epsilon^{-d}$ holds for all $\epsilon>0$. Then for each $T$ there is a problem instance such that $\operatornamewithlimits{\mathbb{E}}[R(T)]\geq\Omega(T^{(d+1)/(d+2)})$.
