---
type: algorithm
label: Algorithm II
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 58 Optimal algorithms and regret bounds (no proofs)
related_entities: []
date_extracted: '2026-03-16T01:32:59.548075+00:00'
---

# Algorithm II

For each round $t$ and each distribution $D$ over arms, define the Upper Confidence Bound as $\displaystyle\mathtt{UCB}_{t}(D\mid B)=\sup_{\mathbf{M}\in\mathtt{ConfRegion}_{t}}\mathtt{LP}(D\mid B,\mathbf{M})$. In each round, the algorithm picks distribution $D$ which maximizes the UCB. An additional trick is to pretend that all budgets are scaled down by the same factor $1-\epsilon$, for an appropriately chosen parameter $\epsilon$.

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 58 Optimal algorithms and regret bounds (no proofs)
