---
type: exercise
label: Exercise 8.3 (Policy evaluation) .
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 48 Exercises and hints
related_entities: []
date_extracted: '2026-03-16T01:32:59.537085+00:00'
---

# Exercise 8.3 (Policy evaluation) .

Use Bernstein Inequality to prove Lemma\xa08.13. In fact, prove a stronger statement: for each policy $\pi$ and each $\delta>0$, with probability at least $1-\delta$ we have:

$$ \displaystyle|\mathtt{IPS}(\pi)-\tilde{r}(\pi)|\leq O\left(\sqrt{V\;\log(\frac{{1}}{{\delta}})/N}\right),\quad\text{where }V=\max_{t}\sum_{a\in\mathcal{A}}\frac{1}{p_{t}(a)}. (117) $$

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 48 Exercises and hints
