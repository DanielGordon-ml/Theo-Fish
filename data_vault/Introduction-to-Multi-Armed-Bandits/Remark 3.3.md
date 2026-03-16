---
type: remark
label: Remark 3.3
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 15 Bayesian update in Bayesian bandits
related_entities: []
date_extracted: '2026-03-16T01:32:59.470688+00:00'
---

# Remark 3.3

Lemma 3.1 should not be taken for granted. Indeed, there are two very natural extensions of Bayesian update for which this lemma does *not* hold. First, suppose we condition on an arbitrary observable event. That is, fix a set $\mathcal{H}$ of feasible $t$-histories. For any algorithm with $\Pr[H_{t}\in\mathcal{H}]>0$, consider the posterior distribution given the event $\{H_{t}\in\mathcal{H}\}$:

$$\displaystyle\Pr[\mu\in\mathcal{M}\mid H_{t}\in\mathcal{H}],\quad\forall\mathcal{M}\subset[0,1]^{K}.$$ (37)

This distribution may depend on the bandit algorithm. For a simple example, consider a problem instance with Bernoulli rewards, three arms $\mathcal{A}=\{a,a^{\prime},a^{\prime\prime}\}$, and a single round. Say $\mathcal{H}$ consists of two feasible $1$-histories, $H=(a,1)$ and $H^{\prime}=(a^{\prime},1)$. Two algorithms, $\mathtt{ALG}$ and $\mathtt{ALG}^{\prime}$, deterministically choose arms $a$ and $a^{\prime}$, respectively. Then the distribution (37) equals $\mathbb{P}_{H}$ under $\mathtt{ALG}$, and $\mathbb{P}_{H^{\prime}}$ under $\mathtt{ALG}^{\prime}$.

Second, suppose we condition on a *subset* of rounds. The algorithm’s history for a subset $S\subset[T]$ of rounds, called *$S$-history*, is an ordered tuple

$$\displaystyle H_{S}=((a_{t},r_{t}):\,t\in S)\in(\mathcal{A}\times\mathbb{R})^{|S|}.$$ (38)

For any feasible $|S|$-history $H$, the posterior distribution given the event $\{H_{S}=H\}$, denoted $\mathbb{P}_{H,S}$, is

$$\displaystyle\mathbb{P}_{H,S}(\mathcal{M}):=\Pr[\mu\in\mathcal{M}\mid H_{S}=H],\quad\forall\mathcal{M}\subset[0,1]^{K}.$$ (39)

However, this distribution may depend on the bandit algorithm, too. Consider a problem instance with Bernoulli rewards, two arms $\mathcal{A}=\{a,a^{\prime}\}$, and two rounds. Let $S=\{2\}$ (i.e.,\xa0we only condition on what happens in the second round), and $H=(a,1)$. Consider two algorithms, $\mathtt{ALG}$ and $\mathtt{ALG}^{\prime}$, which choose different arms in the first round (say, $a$ for $\mathtt{ALG}$ and $a^{\prime}$ for $\mathtt{ALG}^{\prime}$), and choose arm $a$ in the second round if and only if they receive a reward of $1$ in the first round. Then the distribution (39) additionally conditions on $H_{1}=(a,1)$ under $\mathtt{ALG}$, and on $H_{1}=(a^{\prime},1)$ under $\mathtt{ALG}^{\prime}$.

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 15 Bayesian update in Bayesian bandits
