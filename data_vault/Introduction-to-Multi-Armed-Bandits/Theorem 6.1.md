---
type: theorem
label: Theorem 6.1
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: Recap from Chapter 5
related_entities: []
date_extracted: '2026-03-16T01:32:59.512027+00:00'
---

# Theorem 6.1

Consider online learning with $N$ experts and $T$ rounds. Consider an adaptive adversary and regret $R(T)$ relative to the best-observed expert. Suppose in any run of $\mathtt{Hedge}$, with any parameter $\epsilon>0$, it holds that $\sum_{t\in[T]}\;\operatornamewithlimits{\mathbb{E}}[G_{t}]\leq uT$ for some known $u>0$, where $G_{t}=\sum_{\text{experts $e$}}p_{t}(e)\;c_{t}^{2}(e)$. Then $$ \operatornamewithlimits{\mathbb{E}}[R(T)]\leq 2\sqrt{3}\cdot\sqrt{uT\log N}\qquad\text{provided that}\quad\epsilon=\epsilon_{u}:=\sqrt{\tfrac{\ln N}{3uT}}. $$

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: Recap from Chapter 5
