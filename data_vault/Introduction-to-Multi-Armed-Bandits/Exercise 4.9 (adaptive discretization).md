---
type: exercise
label: Exercise 4.9 (adaptive discretization)
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 24 Exercises and hints
related_entities: []
date_extracted: '2026-03-16T01:32:59.497730+00:00'
---

# Exercise 4.9 (adaptive discretization)

Modify the zooming algorithm as follows. The confidence ball of arm $x$ is redefined as the interval $[x,\,x+r_{t}(x)]$. In the activation rule, when some arm is not covered by the confidence balls of active arms, pick the smallest (infimum) such arm and activate it. Prove that this modified algorithm achieves the regret bound in Theorem 4.18. Hint: The invariant (62) still holds. The one-sided Lipschitzness (72) suffices for the proof of Lemma 4.14.

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 24 Exercises and hints
