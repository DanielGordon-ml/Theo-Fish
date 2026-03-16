---
type: definition
label: Definition 4.8
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 21 Lipschitz bandits
related_entities:
- '[[Theorem 4.11]]'
date_extracted: '2026-03-16T01:32:59.484454+00:00'
---

# Definition 4.8

Fix a metric space $(X,\mathcal{D})$. An $\epsilon$-covering, $\epsilon>0$ is a collection of subsets $X_{i}\subset X$ such that the diameter of each subset is at most $\epsilon$ and $X=\bigcup X_{i}$. The smallest number of subsets in an $\epsilon$-covering is called the *covering number* and denoted $N_{\epsilon}(X)$. The *covering dimension*, with multiplier $c>0$, is $\displaystyle \mathtt{COV}_{c}(X)=\inf_{d\geq 0}\left\{\,N_{\epsilon}(X)\leq c\cdot\epsilon^{-d}\quad\forall\epsilon>0\,\right\}.$ (59)

## Relationships

- **Uses (inverse):** [[Theorem 4.11]]

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 21 Lipschitz bandits
