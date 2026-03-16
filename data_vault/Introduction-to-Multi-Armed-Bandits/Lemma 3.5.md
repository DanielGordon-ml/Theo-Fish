---
type: lemma
label: Lemma 3.5
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 15 Bayesian update in Bayesian bandits
related_entities: []
date_extracted: '2026-03-16T01:32:59.471831+00:00'
---

# Lemma 3.5

Assume the prior $\mathbb{P}$ is independent. Fix a subset $\mathcal{M}_{a}\subset[0,1]$ for each arm $a\in\mathcal{A}$. Then

$$\displaystyle\mathbb{P}_{H}(\cap_{a\in\mathcal{A}}\,\mathcal{M}_{a})=\prod_{a\in\mathcal{A}}\,\mathbb{P}^{a}_{H}(\mathcal{M}_{a}).$$

## Proof

The only subtlety is that we focus the $H$-induced bandit algorithm. Then the pairs $(\mu(a),\mathtt{proj}(H_{t};a))$, $a\in\mathcal{A}$ are mutually independent random variables. We are interested in these two events, for each arm $a$:

$$\displaystyle\mathcal{E}_{a}$$ $\displaystyle=\{\mu(a)\in\mathcal{M}_{a}\}$ $\displaystyle\mathcal{E}_{a}^{H}$ $\displaystyle=\{\mathtt{proj}(H_{t};a)=\mathtt{proj}(H;a)\}.$

Letting $\mathcal{M}=\cap_{a\in\mathcal{A}}\,\mathcal{M}_{a}$, we have:

$$\displaystyle\Pr[H_{t}=H\text{ and }\mu\in\mathcal{M}]$$ $\displaystyle=\Pr\left[\bigcap_{a\in\mathcal{A}}(\mathcal{E}_{a}\cap\mathcal{E}_{a}^{H})\right]=\prod_{a\in\mathcal{A}}\Pr\left[\mathcal{E}_{a}\cap\mathcal{E}_{a}^{H}\right].$

Likewise, $\Pr[H_{t}=H]=\prod_{a\in\mathcal{A}}\Pr[\mathcal{E}_{a}^{H}]$. Putting this together,

$$\displaystyle\mathbb{P}_{H}(\mathcal{M})$$ $\displaystyle=\frac{\Pr[H_{t}=H\text{ and }\mu\in\mathcal{M}]}{\Pr[H_{t}=H]}=\prod_{a\in\mathcal{A}}\frac{\Pr[\mathcal{E}_{a}\cap\mathcal{E}_{a}^{H}]}{\Pr[\mathcal{E}_{a}^{H}]}$ $\displaystyle=\prod_{a\in\mathcal{A}}\Pr[\mu\in\mathcal{M}\mid\mathcal{E}_{a}^{H}]=\prod_{a\in\mathcal{A}}\mathbb{P}_{H}^{a}(\mathcal{M}_{a}).\qed$

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 15 Bayesian update in Bayesian bandits
