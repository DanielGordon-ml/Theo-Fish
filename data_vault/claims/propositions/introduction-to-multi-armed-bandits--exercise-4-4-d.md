---
slug: introduction-to-multi-armed-bandits--exercise-4-4-d
label: Exercise 4.4(d)
claim_type: proposition
statement: Consider Lipschitz bandits in a metric space $(X,\mathcal{D})$. Assume
  $d<\mathtt{COV}(X):=\inf_{c>0}\mathtt{COV}_{c}(X)$. Then there are infinitely many
  time horizons $T$ such that $\operatornamewithlimits{\mathbb{E}}[R(T)]\geq\Omega(T^{(d+1)/(d+2)})$
  holds for some problem instance $\mathcal{I}_T$. In fact, there is a distribution
  over these problem instances (each endowed with an infinite time horizon) such that
  the bound holds for infinitely many $T$.
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/lipschitz-bandits-problem]]'
- '[[concepts/expected-regret]]'
- '[[concepts/covering-dimension]]'
- '[[concepts/covering-dimension-cov-c-x]]'
about_meta:
- target: '[[concepts/lipschitz-bandits-problem]]'
  role: primary
  aspect: ''
- target: '[[concepts/expected-regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/covering-dimension]]'
  role: primary
  aspect: ''
- target: '[[concepts/covering-dimension-cov-c-x]]'
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

# Exercise 4.4(d)

Consider Lipschitz bandits in a metric space $(X,\mathcal{D})$. Assume $d<\mathtt{COV}(X):=\inf_{c>0}\mathtt{COV}_{c}(X)$. Then there are infinitely many time horizons $T$ such that $\operatornamewithlimits{\mathbb{E}}[R(T)]\geq\Omega(T^{(d+1)/(d+2)})$ holds for some problem instance $\mathcal{I}_T$. In fact, there is a distribution over these problem instances (each endowed with an infinite time horizon) such that the bound holds for infinitely many $T$.
