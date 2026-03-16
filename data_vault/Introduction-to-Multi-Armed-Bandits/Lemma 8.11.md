---
type: lemma
label: Lemma 8.11
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 45 Learning from contextual bandit data
related_entities: []
date_extracted: '2026-03-16T01:32:59.533181+00:00'
---

# Lemma 8.11

The IPS estimator is unbiased: $\operatornamewithlimits{\mathbb{E}}\left[\,\mathtt{IPS}(\pi)\,\right]=\mu(\pi)$ for each policy $\pi$. Moreover, the IPS estimator is accurate with high probability: for each $\delta>0$, with probability at least $1-\delta$ $\displaystyle|\mathtt{IPS}(\pi)-\mu(\pi)|\leq O\left(\sqrt{\tfrac{1}{p_{0}}\;\log(\tfrac{1}{\delta})/N}\right),\quad\text{where $p_{0}=\min_{t,a}p_{t}(a)$}.$

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 45 Learning from contextual bandit data
