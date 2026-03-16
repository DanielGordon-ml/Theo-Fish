---
type: corollary
label: Corollary 4.15
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: '22 Adaptive discretization: the Zooming Algorithm'
related_entities: []
date_extracted: '2026-03-16T01:32:59.489007+00:00'
---

# Corollary 4.15

For any two active arms $x,y$, we have $\mathcal{D}(x,y)>\tfrac{1}{3}\;\min\left(\Delta(x),\;\Delta(y)\right)$.

## Proof

W.l.o.g. assume that $x$ has been activated before $y$. Let $s$ be the time when $y$ has been activated. Then $\mathcal{D}(x,y)>r_{s}(x)$ by the activation rule. And $r_{s}(x)\geq\Delta(x)/3$ by Lemma\xa04.14.
∎

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 22 Adaptive discretization: the Zooming Algorithm
