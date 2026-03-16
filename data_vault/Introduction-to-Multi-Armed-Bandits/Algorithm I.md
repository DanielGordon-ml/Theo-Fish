---
type: algorithm
label: Algorithm I
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 58 Optimal algorithms and regret bounds (no proofs)
related_entities: []
date_extracted: '2026-03-16T01:32:59.547081+00:00'
---

# Algorithm I

We look for optimal distributions over arms. A distribution $D$ is called potentially optimal if it optimizes $\mathtt{LP}(D\mid B,\mathbf{M})$ for some $\mathbf{M}\in\mathtt{ConfRegion}_{t}$. In each round, we choose a potentially optimal distribution, which suffices for exploitation. But to ensure sufficient exploration, we choose an arm $a$ uniformly at random, and then choose a potentially optimal distribution $D$ that maximizes $D(a)$.

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 58 Optimal algorithms and regret bounds (no proofs)
