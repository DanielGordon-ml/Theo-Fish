---
type: exercise
label: Exercise 9.3 (Hedge vs. Hedge)
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 54 Exercises and hints
related_entities: []
date_extracted: '2026-03-16T01:32:59.543634+00:00'
---

# Exercise 9.3 (Hedge vs. Hedge)

Suppose both $\mathtt{ALG}$ and $\mathtt{ADV}$ are implemented by algorithm $\mathtt{Hedge}$. Assume that $M$ is a $K\times K$ matrix with entries in $[0,1]$, and the parameter in $\mathtt{Hedge}$ is
$\epsilon=\sqrt{(\ln K)/(2T)}$.

- (a) Consider the full-feedback model. Prove that the average play $(\bar{\imath},\bar{\jmath})$ forms a $\delta_{T}$-approximate Nash equilibrium with high probability (e.g.,\xa0with probability at least $1-T^{-2}$),
where
$\delta_{T}=O\left(\sqrt{\tfrac{\ln(KT)}{T}}\right)$.
- (b) Consider a modified feedback model: in each round $t$, $\mathtt{ALG}$ is given costs $M(\cdot,q_{t})$, and $\mathtt{ADV}$ is given rewards $M(p_{t},\cdot)$, where $p_{t}\in\Delta_{\mathtt{rows}}$ and $q_{t}\in\Delta_{\mathtt{cols}}$ are the distributions chosen by $\mathtt{ALG}$ and $\mathtt{ADV}$, respectively. Prove that the average play $(\bar{\imath},\bar{\jmath})$ forms a $\delta_{T}$-approximate Nash equilibrium.
- (c) Suppose $\mathtt{ADV}$ is the best-response adversary, as per Eq.\xa0(122), and $\mathtt{ALG}$ is $\mathtt{Hedge}$ with full feedback. Prove that $(\bar{\imath},\bar{\jmath})$ forms a $\delta_{T}$-approximate Nash equilibrium.

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 54 Exercises and hints
