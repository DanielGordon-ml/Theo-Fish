---
type: lemma
label: Lemma 3.7
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 16 Algorithm specification and implementation
related_entities: []
date_extracted: '2026-03-16T01:32:59.472874+00:00'
---

# Lemma 3.7

For each round $t$, arms $a_{t}$ and $\tilde{a}_{t}$ are identically distributed given $H_{t}$.

## Proof

Fix a feasible $t$-history $H$. For each arm $a$ we have: $$ \Pr[\tilde{a}_{t}=a\mid H_{t-1}=H] = \mathbb{P}_{H}(a^{*}=a) \text{ (by definition of $\tilde{a}_{t}$ ) } = p_{t}(a\mid H) \text{ \emph{(by definition of $p_{t}$)}. } \qed $$

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 16 Algorithm specification and implementation
