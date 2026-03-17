---
slug: introduction-to-multi-armed-bandits--polynomial-optimality-of-sample-complexity-sellke-and-slivkins-2022
label: Polynomial optimality of sample complexity (Sellke and Slivkins 2022)
claim_type: theorem
statement: 'Sellke and Slivkins (2022) provide a new algorithm for sampling each arm.
  Compared to $\mathtt{RepeatedHE}$, it inserts a third "branch" which combines exploration
  and exploitation, and allows the exploration probability to increase over time.
  This algorithm is *polynomially optimal* in the following sense: there is an upper
  bound $U$ on its sample complexity and a lower bound $L$ on the sample complexity
  of any BIC algorithm such that $U<\operatornamewithlimits{poly}\left(\,L/\sigma_{\min}(\mathcal{C})\,\right)$.'
proof: ''
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/minimum-variance-sigma-min-2-c]]'
- '[[concepts/incentivized-exploration]]'
- '[[concepts/sample-complexity]]'
- '[[concepts/explorability]]'
- '[[concepts/bic-bayesian-incentive-compatible]]'
about_meta:
- target: '[[concepts/minimum-variance-sigma-min-2-c]]'
  role: primary
  aspect: ''
- target: '[[concepts/incentivized-exploration]]'
  role: primary
  aspect: ''
- target: '[[concepts/sample-complexity]]'
  role: primary
  aspect: ''
- target: '[[concepts/explorability]]'
  role: primary
  aspect: ''
- target: '[[concepts/bic-bayesian-incentive-compatible]]'
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

# Polynomial optimality of sample complexity (Sellke and Slivkins 2022)

Sellke and Slivkins (2022) provide a new algorithm for sampling each arm. Compared to $\mathtt{RepeatedHE}$, it inserts a third "branch" which combines exploration and exploitation, and allows the exploration probability to increase over time. This algorithm is *polynomially optimal* in the following sense: there is an upper bound $U$ on its sample complexity and a lower bound $L$ on the sample complexity of any BIC algorithm such that $U<\operatornamewithlimits{poly}\left(\,L/\sigma_{\min}(\mathcal{C})\,\right)$.
