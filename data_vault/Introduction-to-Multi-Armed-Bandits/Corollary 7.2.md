---
type: corollary
label: Corollary 7.2
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 'Recap: bandits-to-experts reduction'
related_entities: []
date_extracted: '2026-03-16T01:32:59.518866+00:00'
---

# Corollary 7.2

If $\mathtt{ALG}$ is $\mathtt{Hedge}$ in the theorem above, one can take $f(T,K,u)=O(u\cdot\sqrt{T\ln{K}})$ by Theorem 5.16. Then, setting $\gamma=T^{-1/4}\;\sqrt{u\cdot\log K}$, Algorithm 1 achieves regret $$ $\operatornamewithlimits{\mathbb{E}}[R(T)]\leq O\left(\,T^{3/4}\;\sqrt{u\cdot\log K}\,\right).$ $$

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: Recap: bandits-to-experts reduction
