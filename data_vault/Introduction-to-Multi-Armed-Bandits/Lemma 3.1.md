---
type: lemma
label: Lemma 3.1
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 15 Bayesian update in Bayesian bandits
related_entities: []
date_extracted: '2026-03-16T01:32:59.469715+00:00'
---

# Lemma 3.1

Distribution $\mathbb{P}_{H}$ is the same for all $H$-consistent bandit algorithms.

## Proof

It suffices to prove the lemma for a singleton set $\mathcal{M}=\{\tilde{\mu}\}$, for any given vector $\tilde{\mu}\in[0,1]^{K}$. Thus, we are interested in the conditional probability of $\{\mu=\tilde{\mu}\}$. Recall that the reward distribution with mean reward $\tilde{\mu}(a)$ places probability $\mathcal{D}_{\tilde{\mu}(a)}(r)$ on every given value $r\in\mathbb{R}$.

Let us use induction on $t$. The base case is $t=0$. To make it well-defined, let us define the 0-history as $H_{0}=\emptyset$, so that $H=\emptyset$ to be the only feasible 0-history. Then, all algorithms are $\emptyset$-consistent, and the conditional probability $\Pr[\mu=\tilde{\mu}\mid H_{0}=H]$ is simply the prior probability $\mathbb{P}(\tilde{\mu})$.

The main argument is the induction step. Consider round $t\geq 1$. Write $H$ as concatenation of some feasible $(t-1)$-history $H^{\prime}$ and an action-reward pair $(a,r)$. Fix an $H$-consistent bandit algorithm, and let

$$\pi(a)=\Pr\left[\,a_{t}=a\mid H_{t-1}=H^{\prime}\,\right]$$

be the probability that this algorithm assigns to each arm $a$ in round $t$ given the history $H^{\prime}$. Note that this probability does not depend on the mean reward vector $\mu$.

$$\displaystyle\frac{\Pr[\mu=\tilde{\mu}\text{ and }H_{t}=H]}{\Pr[H_{t-1}=H^{\prime}]}$$ $\displaystyle=\Pr\left[\,\mu=\tilde{\mu}\text{ and }(a_{t},r_{t})=(a,r)\mid H_{t-1}=H^{\prime}\,\right]$ $\displaystyle=\mathbb{P}_{H^{\prime}}(\tilde{\mu})\cdot\Pr[(a_{t},r_{t})=(a,r)\mid\mu=\tilde{\mu}\text{ and }H_{t-1}=H^{\prime}]$ $\displaystyle=\mathbb{P}_{H^{\prime}}(\tilde{\mu})$ $\displaystyle\quad\Pr\left[\,r_{t}=r\mid a_{t}=a\text{ and }\mu=\tilde{\mu}\text{ and }H_{t-1}=H^{\prime}\,\right]$ $\displaystyle\quad\Pr\left[\,a_{t}=a\mid\mu=\tilde{\mu}\text{ and }H_{t-1}=H^{\prime}\,\right]$ $\displaystyle=\mathbb{P}_{H^{\prime}}(\tilde{\mu})\cdot\mathcal{D}_{\tilde{\mu}(a)}(r)\cdot\pi(a).$

Therefore,

$$\displaystyle\Pr[H_{t}=H]=\pi(a)\cdot\Pr[H_{t-1}=H^{\prime}]\;\sum_{\tilde{\mu}\in\mathcal{F}}\mathbb{P}_{H^{\prime}}(\tilde{\mu})\cdot\mathcal{D}_{\tilde{\mu}(a)}(r).$$

It follows that

$$\displaystyle\mathbb{P}_{H}(\tilde{\mu})=\frac{\Pr[\mu=\tilde{\mu}\text{ and }H_{t}=H]}{\Pr[H_{t}=H]}=\frac{\mathbb{P}_{H^{\prime}}(\tilde{\mu})\cdot\mathcal{D}_{\tilde{\mu}(a)}(r)}{\sum_{\tilde{\mu}\in\mathcal{F}}\mathbb{P}_{H^{\prime}}(\tilde{\mu})\cdot\mathcal{D}_{\tilde{\mu}(a)}(r)}.$$

By the induction hypothesis, the posterior distribution $\mathbb{P}_{H^{\prime}}$ does not depend on the algorithm. So, the expression above does not depend on the algorithm, either.
∎

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 15 Bayesian update in Bayesian bandits
