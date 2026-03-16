---
type: corollary
label: Corollary 2.9
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: '9 Flipping several coins: “best-arm identification”'
related_entities: []
date_extracted: '2026-03-16T01:32:59.458065+00:00'
---

# Corollary 2.9

Assume $T$ is as in Lemma\xa02.8. Fix any algorithm for 'best-arm identification'. Choose an arm $a$ uniformly at random, and run the algorithm on instance $\mathcal{I}_{a}$. Then $\Pr[y_{T}\neq a]\geq\tfrac{1}{12}$, where the probability is over the choice of arm $a$ and the randomness in rewards and the algorithm.

## Proof

Lemma\xa02.8 immediately implies this corollary for deterministic algorithms. The general case follows because any randomized algorithm can be expressed as a distribution over deterministic algorithms. ∎

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 9 Flipping several coins: “best-arm identification”
