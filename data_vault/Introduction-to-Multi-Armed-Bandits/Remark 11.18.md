---
type: remark
label: Remark 11.18
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 64 Repeated hidden exploration
related_entities: []
date_extracted: '2026-03-16T01:32:59.562844+00:00'
---

# Remark 11.18

We match the Bayesian regret of $\mathtt{ALG}$ up to factors $N_{0},\,\tfrac{1}{\epsilon}$, which depend only on the prior $\mathcal{P}$ (and not on the time horizon or the realization of the mean rewards). In particular, we can achieve $\tilde{O}(\sqrt{T})$ regret for all problem instances, e.g., using algorithm $\mathtt{UCB1}$ from Chapter 1. If a smaller regret rate $f(T)=o(T)$ is achievable for a given prior using some other algorithm $\mathtt{ALG}$, we can match it, too. However, the prior-dependent factors can be arbitrarily large, depending on the prior.

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 64 Repeated hidden exploration
