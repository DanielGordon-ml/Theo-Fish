---
type: remark
label: Remark 8.12
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 45 Learning from contextual bandit data
related_entities: []
date_extracted: '2026-03-16T01:32:59.533678+00:00'
---

# Remark 8.12

How many data points do we need to evaluate $M$ policies simultaneously? To make this question more precise, suppose we have some fixed parameters $\epsilon,\delta>0$ in mind, and want to ensure that $\displaystyle\Pr\left[\;|\mathtt{IPS}(\pi)-\mu(\pi)|\leq\epsilon\quad\text{for each policy $\pi$}\;\right]>1-\delta.$ How large should $N$ be, as a function of $M$ and the parameters? Taking a union bound over (112), we see that it suffices to take $N\sim\frac{\sqrt{\log(M/\delta)}}{p_{0}\cdot\epsilon^{2}}.$ The logarithmic dependence on $M$ is due to the fact that each data point $t$ can be reused to evaluate many policies, namely all policies $\pi$ with $\pi(x_{t})=a_{t}$.

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 45 Learning from contextual bandit data
