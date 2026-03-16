---
type: remark
label: Remark 10.16
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 58 Optimal algorithms and regret bounds (no proofs)
related_entities: []
date_extracted: '2026-03-16T01:32:59.548604+00:00'
---

# Remark 10.16

For a given distribution $D$, the supremum in (149) is obtained when upper confidence bounds are used for rewards, and lower confidence bounds are used for resource consumption: $\displaystyle\mathtt{UCB}_{t}(D\mid B^{\prime})=\begin{cases}r^{\mathtt{UCB}}(D)&\text{if $c^{\mathtt{LCB}}_{i}(D)\leq B^{\prime}/T$ for each resource $i$},\\ 0&\text{otherwise}.\end{cases}$ Accordingly, choosing a distribution with maximal $\mathtt{UCB}$ can be implemented by a linear program: $\begin{array}{ll}\text{maximize}&r^{\mathtt{UCB}}(D)\\ \text{subject to}\\ &D\in\Delta_{K}\\ &c_{i}^{\mathtt{LCB}}(D)\leq B^{\prime}/T.\end{array}$

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 58 Optimal algorithms and regret bounds (no proofs)
