---
type: theorem
label: Theorem 4.11
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 21 Lipschitz bandits
related_entities:
- '[[Definition 4.8]]'
date_extracted: '2026-03-16T01:32:59.486431+00:00'
---

# Theorem 4.11

Consider Lipschitz bandits on a metric space $(X,\mathcal{D})$, with time horizon $T$. Let $\mathtt{ALG}$ be any algorithm satisfying (52). Fix any $c>0$, and let $d=\mathtt{COV}_{c}(X)$ be the covering dimension. Then there exists a subset $S\subset X$ such that running $\mathtt{ALG}$ on the set of arms $S$ yields regret $\displaystyle \operatornamewithlimits{\mathbb{E}}[R(T)]\leq(1+c_{\mathtt{ALG}})\cdot T^{(d+1)/(d+2)}\cdot(c\,\log T)^{1/(d+2)}.$ Specifically, $S$ can be any $\epsilon$-mesh of size $|S|\leq O(c/\epsilon^{d})$, where $\epsilon=(T\,/\,\log T)^{-1/(d+2)}$; such $S$ exists.

## Relationships

- **Uses:** [[Definition 4.8]]

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 21 Lipschitz bandits
