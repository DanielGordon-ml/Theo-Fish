---
type: exercise
label: Exercise 8.1 (Lipschitz contextual bandits) .
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 48 Exercises and hints
related_entities: []
date_extracted: '2026-03-16T01:32:59.536027+00:00'
---

# Exercise 8.1 (Lipschitz contextual bandits) .

Consider the Lipschitz condition in (103). Design an algorithm with regret bound $\tilde{O}(T^{(d+1)/(d+2})$, where $d$ is the covering dimension of $\mathcal{X}\times\mathcal{A}$.

Hint: Extend the uniform discretization approach, using the notion of $\epsilon$-mesh from Definition\xa04.4. Fix an $\epsilon$-mesh $S_{\mathcal{X}}$ for $(\mathcal{X},\mathcal{D}_{\mathcal{X}})$ and an $\epsilon$-mesh $S_{\mathcal{A}}$ for $(\mathcal{A},\mathcal{D}_{\mathcal{A}})$, for some $\epsilon>0$ to be chosen in the analysis. Fix an optimal bandit algorithm $\mathtt{ALG}$ such as $\mathtt{UCB1}$, with $S_{\mathcal{A}}$ as a set of arms. Run a separate copy $\mathtt{ALG}_{x}$ of this algorithm for each context $x\in S_{\mathcal{X}}$.

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 48 Exercises and hints
