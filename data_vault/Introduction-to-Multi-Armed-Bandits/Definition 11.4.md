---
type: definition
label: Definition 11.4
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: '61 Problem formulation: incentivized exploration'
related_entities: []
date_extracted: '2026-03-16T01:32:59.557945+00:00'
---

# Definition 11.4

An algorithm is called *Bayesian incentive-compatible* (*BIC*) if for all rounds $t$ we have $$ \displaystyle\operatornamewithlimits{\mathbb{E}}\left[\,\mu_{a}-\mu_{a^{\prime}}\mid\mathtt{rec}_{t}=a,\,\mathcal{E}_{t-1}\,\right]\geq 0, $ (159) $$ where $a,a^{\prime}$ are any two distinct arms such that $\Pr\left[\,\mathtt{rec}_{t}=a,\,\mathcal{E}_{t-1}\,\right]>0$.

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 61 Problem formulation: incentivized exploration
