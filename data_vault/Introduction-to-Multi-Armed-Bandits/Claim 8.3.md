---
type: lemma
label: Claim 8.3
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 42 Lipshitz contextual bandits
related_entities: []
date_extracted: '2026-03-16T01:32:59.528032+00:00'
---

# Claim 8.3

$\operatornamewithlimits{\mathbb{E}}[\mathtt{DE}(S)]\leq\epsilon LT$

## Proof

For each round $t$ and the respective context $x=x_{t}$, $$ $\displaystyle\mu(\pi^{*}_{S}(x)\mid f_{S}(x))$ $\displaystyle\geq\mu(\pi^{*}(x)\mid f_{S}(x))$ (by optimality of $\pi^{*}_{S}$ ) $\displaystyle\geq\mu(\pi^{*}(x)\mid x)-\epsilon L$ $\displaystyle\text{\emph{(by Lipschitzness)}}.$ $$ Summing this up over all rounds $t$, we obtain $$ $\operatornamewithlimits{\mathbb{E}}[\mathtt{REW}(\pi^{*}_{S})]\geq\mathtt{REW}[\pi^{*}]-\epsilon LT.\qed$

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 42 Lipshitz contextual bandits
