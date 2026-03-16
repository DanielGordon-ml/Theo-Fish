---
type: theorem
label: Theorem 5.6
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: '26 Initial results: binary prediction with experts advice'
related_entities: []
date_extracted: '2026-03-16T01:32:59.502495+00:00'
---

# Theorem 5.6

Consider binary prediction with experts advice. Assuming a perfect expert, the majority vote algorithm makes at most $\log_{2}K$ mistakes, where $K$ is the number of experts.

## Proof

Let $S_{t}$ be the set of experts who make no mistakes up to round $t$, and let $W_{t}=|S_{t}|$. Note that $W_{1}=K$, and $W_{t}\geq 1$ for all rounds $t$, because the perfect expert is always in $S_{t}$. If the algorithm makes a mistake at round $t$, then $W_{t+1}\leq W_{t}/2$ because the majority of experts in $S_{t}$ is wrong and thus excluded from $S_{t+1}$. It follows that the algorithm cannot make more than $\log_{2}K$ mistakes.

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 26 Initial results: binary prediction with experts advice
