---
type: exercise
label: Exercise 1.5 (Doubling trick)
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 6 Exercises and hints
related_entities: []
date_extracted: '2026-03-16T01:32:59.453101+00:00'
---

# Exercise 1.5 (Doubling trick)

Take any bandit algorithm $\mathcal{A}$ for fixed time horizon $T$. Convert it to an algorithm $\mathcal{A}_{\infty}$ which runs forever, in phases $i=1,2,3,\,...$ of $2^{i}$ rounds each. In each phase $i$ algorithm $\mathcal{A}$ is restarted and run with time horizon $2^{i}$.
- (a) State and prove a theorem which converts an instance-independent upper bound on regret for $\mathcal{A}$ into similar bound for $\mathcal{A}_{\infty}$ (so that this theorem applies to both $\mathtt{UCB1}$ and Explore-first).
- (b) Do the same for $\log(T)$ instance-dependent upper bounds on regret. (Then regret increases by a $\log(T)$ factor.)

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 6 Exercises and hints
