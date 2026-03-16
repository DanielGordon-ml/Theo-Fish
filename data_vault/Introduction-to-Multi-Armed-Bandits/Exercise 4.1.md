---
type: exercise
label: Exercise 4.1
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 24 Exercises and hints
related_entities: []
date_extracted: '2026-03-16T01:32:59.493360+00:00'
---

# Exercise 4.1

Compare $f(N_{i^{*}})$ against (67). Specifically, prove that $$ \displaystyle f(\mathcal{N}_{i^{*}})\leq 16\,\inf_{S\subset X}f(S). $$ (68) The key notion in the proof is *$\epsilon$-net*, $\epsilon>0$: it is an $\epsilon$-mesh where any two points are at distance $>\epsilon$. - (a) Observe that each $\epsilon$-mesh computed in Remark 4.6 is in fact an $\epsilon$-net. - (b) Prove that for any $\epsilon$-mesh $S$ and any $\epsilon^{\prime}$-net $\mathcal{N}$, $\epsilon^{\prime}\geq 2\epsilon$, it holds that $|\mathcal{N}|\leq|S|$. Use (a) to conclude that $\min_{i\in\mathbb{N}}f(\mathcal{N}_{i})\leq 4\,f(S)$. - (c) Prove that $f(\mathcal{N}_{i^{*}})\leq 4\,\min_{i\in\mathbb{N}}f(\mathcal{N}_{i})$. Use (b) to conclude that (68) holds.

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 24 Exercises and hints
