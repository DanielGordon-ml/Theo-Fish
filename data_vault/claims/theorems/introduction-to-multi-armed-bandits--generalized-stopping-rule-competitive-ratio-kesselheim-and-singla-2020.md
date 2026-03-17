---
slug: introduction-to-multi-armed-bandits--generalized-stopping-rule-competitive-ratio-kesselheim-and-singla-2020
label: Generalized Stopping Rule Competitive Ratio (Kesselheim and Singla 2020)
claim_type: theorem
statement: 'Kesselheim and Singla (2020) consider a more general version of the stopping
  rule: the algorithm stops at time $t$ if $\|(C_{t,1}\,,\ \ldots\ ,C_{t,d}\|_{p}>B$,
  where $p\geq 1$ and $C_{t,i}$ is the total consumption of resource $i$ at time $t$.
  The case $p=\infty$ corresponds to $\mathtt{BwK}$. They obtain the same competitive
  ratio, $O\left(\,\log(d)\,\log(T)\,\right)$, using a version of $\mathtt{LagrangeBwK}$
  with a different "dual" algorithm and a different analysis.'
proof: ''
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/number-of-resources-d]]'
- '[[concepts/lagrangebwk]]'
- '[[concepts/adversarial-bwk]]'
- '[[concepts/bandits-with-knapsacks]]'
about_meta:
- target: '[[concepts/number-of-resources-d]]'
  role: primary
  aspect: ''
- target: '[[concepts/lagrangebwk]]'
  role: primary
  aspect: ''
- target: '[[concepts/adversarial-bwk]]'
  role: primary
  aspect: ''
- target: '[[concepts/bandits-with-knapsacks]]'
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

# Generalized Stopping Rule Competitive Ratio (Kesselheim and Singla 2020)

Kesselheim and Singla (2020) consider a more general version of the stopping rule: the algorithm stops at time $t$ if $\|(C_{t,1}\,,\ \ldots\ ,C_{t,d}\|_{p}>B$, where $p\geq 1$ and $C_{t,i}$ is the total consumption of resource $i$ at time $t$. The case $p=\infty$ corresponds to $\mathtt{BwK}$. They obtain the same competitive ratio, $O\left(\,\log(d)\,\log(T)\,\right)$, using a version of $\mathtt{LagrangeBwK}$ with a different "dual" algorithm and a different analysis.
