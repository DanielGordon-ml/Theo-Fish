---
type: theorem
label: Theorem 5.16
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 27 Hedge Algorithm
related_entities: []
date_extracted: '2026-03-16T01:32:59.508416+00:00'
---

# Theorem 5.16

Assume $\sum_{t\in[T]}\;\operatornamewithlimits{\mathbb{E}}[G_{t}]\leq uT$ for some known number $u$, where $\operatornamewithlimits{\mathbb{E}}[G_{t}]=\operatornamewithlimits{\mathbb{E}}\left[\,c_{t}^{2}(a_{t})\,\right]$ as per (81). Then $\mathtt{Hedge}$ with parameter $\epsilon=\sqrt{\frac{\ln K}{3uT}}$ achieves regret $\operatornamewithlimits{\mathbb{E}}[\mathtt{cost}(\mathtt{ALG})-\mathtt{cost}^{*}]<2\sqrt{3}\cdot\sqrt{uT\ln{K}}$.

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 27 Hedge Algorithm
