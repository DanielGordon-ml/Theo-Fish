---
type: exercise
label: Exercise 9.5 (infinite action sets)
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 54 Exercises and hints
related_entities: []
date_extracted: '2026-03-16T01:32:59.544714+00:00'
---

# Exercise 9.5 (infinite action sets)

Consider an extension of the repeated game to infinite action sets. Formally, $\mathtt{ALG}$ and $\mathtt{ADV}$ have action sets $I$, $J$, resp., and the game matrix $M$ is a function $I\times J\to[0,1]$. $I$ and $J$ can be arbitrary sets with well-defined probability measures such that each singleton set is measurable. Assume there exists a function $\tilde{R}(T)=o(T)$ such that expected regret of $\mathtt{ALG}$ is at most $\tilde{R}(T)$ for any $\mathtt{ADV}$, and likewise expected regret of $\mathtt{ADV}$ is at most $\tilde{R}(T)$ for any $\mathtt{ALG}$.

- (a) Prove an appropriate versions of the minimax theorem:
$\displaystyle\inf_{p\in\Delta_{\mathtt{rows}}}\;\sup_{j\in J}\;\int M(p,j)\mathop{}\!\mathrm{d}p=\sup_{q\in\Delta_{\mathtt{cols}}}\;\inf_{i\in I}\;\int M(i,q)\mathop{}\!\mathrm{d}q,$
where $\Delta_{\mathtt{rows}}$ and $\Delta_{\mathtt{cols}}$ are now the sets of all probability measures on $I$ and $J$.
- (b) Formulate and prove an appropriate version of Theorem\xa09.5.

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 54 Exercises and hints
