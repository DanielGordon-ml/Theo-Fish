---
type: algorithm
label: Algorithm 1
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: '26 Initial results: binary prediction with experts advice'
related_entities: []
date_extracted: '2026-03-16T01:32:59.504170+00:00'
---

# Algorithm 1

We assign a confidence weight $w_{a}\geq 0$ to each expert $a$: the higher the weight, the larger the confidence. We update the weights over time, decreasing the weight of a given expert whenever he makes a mistake. More specifically, in this case we multiply the weight by a factor $1-\epsilon$, for some fixed parameter $\epsilon>0$. We treat each round as a weighted vote among the experts, and we choose a prediction with a largest total weight. This algorithm is called Weighted Majority Algorithm (WMA).

## Relationships

- **Cross-paper:** [[Combinatorial-Network-Optimization-with-Unknown-Variables-Multi-Armed-Bandits-wi/Algorithm 1|Algorithm 1 (Combinatorial-Network-Optimization-with-Unknown-Variables-Multi-Armed-Bandits-wi)]]

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 26 Initial results: binary prediction with experts advice
