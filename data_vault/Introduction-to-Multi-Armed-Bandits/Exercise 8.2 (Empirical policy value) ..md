---
type: exercise
label: Exercise 8.2 (Empirical policy value) .
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 48 Exercises and hints
related_entities: []
date_extracted: '2026-03-16T01:32:59.536584+00:00'
---

# Exercise 8.2 (Empirical policy value) .

Prove that realized policy value $\tilde{r}(\pi)$, as defined in (109), is close to the policy value $\mu(\pi)$. Specifically, observe that $\operatornamewithlimits{\mathbb{E}}[\tilde{r}(\pi)]=\mu(\pi)$. Next, fix $\delta>0$ and prove that

$$ \displaystyle|\mu(\pi)-\tilde{r}(\pi)|\leq\mathtt{conf}(N)\quad\text{with probability at least $1-\delta/|\Pi|$}, $$

where the confidence term is $\mathtt{conf}(N)=O\left(\,\sqrt{\frac{{1}}{{N}}\cdot\log(|\Pi|/\delta)}\,\right)$. Letting $\pi_{0}$ be the policy with a largest realized policy value, it follows that

$$ \displaystyle\max_{\pi\in\Pi}\mu(\pi)-\mu(\pi_{0}) \displaystyle\leq\mathtt{conf}(N)\quad\text{with probability at least $1-\delta$} $$

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 48 Exercises and hints
