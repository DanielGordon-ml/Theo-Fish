---
slug: introduction-to-multi-armed-bandits--theorem-10-14
label: Theorem 10.14
claim_type: theorem
statement: 'Suppose algorithm $\mathtt{LagrangeBwK}$ is used with $\mathtt{EXP3.P.1}$
  as $\mathtt{ALG}_{1}$, and $\mathtt{Hedge}$ as $\mathtt{ALG}_{2}$. Then the following
  regret bound is achieved, with probability at least $1-\delta$:


  $\textstyle\mathtt{OPT}-\mathtt{REW}\leq O\left(\,\nicefrac{{T}}{{B}}\,\right)\cdot\sqrt{TK\ln\left(\,\frac{dT}{\delta}\,\right)}.$'
proof: ''
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/bandits-with-knapsacks]]'
- '[[concepts/exp3-p-1-algorithm]]'
- '[[concepts/hedge]]'
- '[[concepts/lagrangebwk]]'
- '[[concepts/regret-bound]]'
- '[[concepts/optimal-regret-bound-for-bwk]]'
about_meta:
- target: '[[concepts/bandits-with-knapsacks]]'
  role: primary
  aspect: ''
- target: '[[concepts/exp3-p-1-algorithm]]'
  role: primary
  aspect: ''
- target: '[[concepts/hedge]]'
  role: primary
  aspect: ''
- target: '[[concepts/lagrangebwk]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret-bound]]'
  role: primary
  aspect: ''
- target: '[[concepts/optimal-regret-bound-for-bwk]]'
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

# Theorem 10.14

Suppose algorithm $\mathtt{LagrangeBwK}$ is used with $\mathtt{EXP3.P.1}$ as $\mathtt{ALG}_{1}$, and $\mathtt{Hedge}$ as $\mathtt{ALG}_{2}$. Then the following regret bound is achieved, with probability at least $1-\delta$:

$\textstyle\mathtt{OPT}-\mathtt{REW}\leq O\left(\,\nicefrac{{T}}{{B}}\,\right)\cdot\sqrt{TK\ln\left(\,\frac{dT}{\delta}\,\right)}.$
