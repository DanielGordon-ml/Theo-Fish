---
type: remark
label: Remark 7.9
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 38 Combinatorial semi-bandits
related_entities: []
date_extracted: '2026-03-16T01:32:59.522953+00:00'
---

# Remark 7.9

Solving a version with bandit feedback requires more work. The main challenge is to estimate fake costs for all atoms in the chosen action, whereas we only observe the total cost for the action. One solution is to construct a suitable *basis*: a subset of feasible actions, called *base actions*, such that each action can be represented as a linear combination thereof. Then a version of Algorithm 1, where in the “random exploration” step is uniform among the base actions, gives us fake costs for the base actions. The fake cost on each atom is the corresponding linear combination over the base actions. This approach works as long as the linear coefficients are small, and ensuring this property takes some work. This approach is worked out in Awerbuch and Kleinberg (2008), resulting in regret $\operatornamewithlimits{\mathbb{E}}[R(T)]\leq\tilde{O}(d^{10/3}\cdot T^{2/3})$.

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 38 Combinatorial semi-bandits
