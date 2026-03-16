---
type: remark
label: Remark 4.6
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 21 Lipschitz bandits
related_entities: []
date_extracted: '2026-03-16T01:32:59.481244+00:00'
---

# Remark 4.6

How do we *construct* a good $\epsilon$-mesh? For many examples the construction is trivial, e.g., a uniform discretization in continuum-armed bandits or in the next example. For an arbitrary metric space and a given $\epsilon>0$, a standard construction starts with an empty set $S$, adds any arm that is within distance $>\epsilon$ from all arms in $S$, and stops when such arm does not exist. Now, consider different values of $\epsilon$ in exponentially decreasing order: $\epsilon=2^{-i}$, $i=1,2,3,\,\ldots$. For each such $\epsilon$, compute an $\epsilon$-mesh $S_{\epsilon}$ as specified above, and stop at the largest $\epsilon$ such that $\epsilon T\geq c_{\mathtt{ALG}}\cdot\sqrt{|S_{\epsilon}|\,T\log T}$. This $\epsilon$-mesh optimizes the right-hand side in (58) up to a constant factor, see Exercise 4.1

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 21 Lipschitz bandits
