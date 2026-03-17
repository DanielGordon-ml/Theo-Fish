---
slug: introduction-to-multi-armed-bandits--exercise-4-8-uniform-discretization-for-dynamic-pricing
label: Exercise 4.8 (uniform discretization for dynamic pricing)
claim_type: proposition
statement: Using the one-sided Lipschitzness $\mu(p)-\mu(p')\leq p-p'$ for $p>p'$,
  with any algorithm $\mathtt{ALG}$ satisfying (52) and discretization step $\epsilon=(T/\log
  T)^{-1/3}$, one obtains $\operatornamewithlimits{\mathbb{E}}[R(T)]\leq T^{2/3}\cdot(1+c_{\mathtt{ALG}})(\log
  T)^{1/3}$.
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/one-sided-lipschitzness]]'
- '[[concepts/dynamic-pricing-problem]]'
- '[[concepts/regret-bound]]'
- '[[concepts/expected-regret-r-t]]'
- '[[concepts/uniform-discretization-for-bandits]]'
about_meta:
- target: '[[concepts/one-sided-lipschitzness]]'
  role: primary
  aspect: ''
- target: '[[concepts/dynamic-pricing-problem]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret-bound]]'
  role: primary
  aspect: ''
- target: '[[concepts/expected-regret-r-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/uniform-discretization-for-bandits]]'
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

# Exercise 4.8 (uniform discretization for dynamic pricing)

Using the one-sided Lipschitzness $\mu(p)-\mu(p')\leq p-p'$ for $p>p'$, with any algorithm $\mathtt{ALG}$ satisfying (52) and discretization step $\epsilon=(T/\log T)^{-1/3}$, one obtains $\operatornamewithlimits{\mathbb{E}}[R(T)]\leq T^{2/3}\cdot(1+c_{\mathtt{ALG}})(\log T)^{1/3}$.
