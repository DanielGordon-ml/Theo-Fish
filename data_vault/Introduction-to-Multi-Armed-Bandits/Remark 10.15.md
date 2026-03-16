---
type: remark
label: Remark 10.15
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 58 Optimal algorithms and regret bounds (no proofs)
related_entities: []
date_extracted: '2026-03-16T01:32:59.547589+00:00'
---

# Remark 10.15

The step of maximizing $D(b_{t})$ does not have a computationally efficient implementation (more precisely, such implementation is not known for the general case of $\mathtt{BwK}$). This algorithm can be seen as an extension of Successive Elimination. Recall that in Successive Elimination, we start with all arms being “active” and permanently de-activate a given arm $a$ once we have high-confidence evidence that some other arm is better. The idea is that each arm that is currently active can potentially be an optimal arm given the evidence collected so far. In each round we choose among arms that are still “potentially optimal”, which suffices for the purpose of exploitation. And choosing uniformly (or round-robin) among the potentially optimal arms suffices for the purpose of exploration.

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 58 Optimal algorithms and regret bounds (no proofs)
