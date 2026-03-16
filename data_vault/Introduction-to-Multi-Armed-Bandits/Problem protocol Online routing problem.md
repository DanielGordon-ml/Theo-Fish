---
type: definition
label: 'Problem protocol: Online routing problem'
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 37 Online routing problem
related_entities: []
date_extracted: '2026-03-16T01:32:59.519433+00:00'
---

# Problem protocol: Online routing problem

Given: graph $G$, source node $u$, destination node $v$.

For each round $t\in[T]$:
- 1. Adversary chooses costs $c_{t}(e)\in[0,1]$ for all edges $e$.
- 2. Algorithm chooses $u$-$v$-path $a_{t}\subset\mathtt{Edges}(G)$.
- 3. Algorithm incurs cost $c_{t}(a_{t})=\sum_{e\in a_{t}}a_{e}\cdot c_{t}(e)$ and receives feedback.

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 37 Online routing problem
