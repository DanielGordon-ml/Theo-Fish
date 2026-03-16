---
type: exercise
label: Exercise 9.4 (stochastic games)
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 54 Exercises and hints
related_entities: []
date_extracted: '2026-03-16T01:32:59.544141+00:00'
---

# Exercise 9.4 (stochastic games)

Consider an extension to stochastic games: in each round $t$, the game matrix $M_{t}$ is drawn independently from some fixed distribution over game matrices. Assume all matrices have the same dimensions (number of rows and columns). Suppose both $\mathtt{ALG}$ and $\mathtt{ADV}$ are regret-minimizing algorithms, as in Section\xa051, and let $R(T)$ and $R^{\prime}(T)$ be their respective regret. Prove that the average play $(\bar{\imath},\bar{\jmath})$ forms a $\delta_{T}$-approximate Nash equilibrium for the expected game matrix $M=\operatornamewithlimits{\mathbb{E}}[M_{t}]$, with

$$ \delta_{T}=\tfrac{R(T)+R^{\prime}(T)}{T}+\mathtt{err},\text{ where }\textstyle\mathtt{err}=\left|\sum_{t\in[T]}M_{t}(i_{t},j_{t})-M(i_{t},j_{i})\right|. $$

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 54 Exercises and hints
