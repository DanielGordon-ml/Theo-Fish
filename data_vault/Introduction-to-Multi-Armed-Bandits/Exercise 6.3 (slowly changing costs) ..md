---
type: exercise
label: Exercise 6.3 (slowly changing costs) .
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 36 Exercises and hints
related_entities: []
date_extracted: '2026-03-16T01:32:59.517861+00:00'
---

# Exercise 6.3 (slowly changing costs) .

Consider a randomized oblivious adversary such that the expected cost of each arm changes by at most $\epsilon$ from one round to another, for some fixed and known $\epsilon>0$. Use algorithm $\mathtt{Exp4}$ to obtain dynamic regret

$$ $\displaystyle\operatornamewithlimits{\mathbb{E}}[R^{*}(T)]\leq O(T)\cdot(\epsilon\cdot K\log K)^{1/3}.$ (94) $$

Hint: Recall the application of $\mathtt{Exp4}$ to $n$-shifting regret, denote it $\mathtt{Exp4}(n)$. Let $\mathtt{OPT}_{n}=\min\mathtt{cost}(\pi)$, where the $\min$ is over all $n$-shifting policies $\pi$, be the benchmark in $n$-shifting regret. Analyze the “discretization error”: the difference between $\mathtt{OPT}_{n}$ and
$\mathtt{OPT}^{*}=\sum_{t=1}^{T}\min_{a}c_{t}(a)$,
the benchmark in dynamic regret. Namely: prove that
$\mathtt{OPT}_{n}-\mathtt{OPT}^{*}\leq O(\epsilon T^{2}/n)$.
Derive an upper bound on dynamic regret that is in terms of $n$. Optimize the choice of $n$.

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 36 Exercises and hints
