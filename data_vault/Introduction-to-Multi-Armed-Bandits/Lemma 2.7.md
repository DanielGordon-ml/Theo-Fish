---
type: lemma
label: Lemma 2.7
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: '8 A simple example: flipping one coin'
related_entities: []
date_extracted: '2026-03-16T01:32:59.457042+00:00'
---

# Lemma 2.7

Let $\mu_{1}=\frac{1+\epsilon}{2}$ and $\mu_{2}=\frac{1}{2}$. Fix a decision rule which satisfies (18) and (19). Then $T>\tfrac{1}{4\,\epsilon^{2}}$.

## Proof

Let $A_{0}\subset\Omega$ be the event this rule returns $\mathtt{High}$. Then $$ \displaystyle\Pr[A_{0}\mid\mu=\mu_{1}]-\Pr[A_{0}\mid\mu=\mu_{2}]\geq 0.98. $$ Let $P_{i}(A)=\Pr[A\mid\mu=\mu_{i}]$, for each event $A\subset\Omega$ and each $i\in\{1,2\}$. Then $P_{i}=P_{i,1}\times\ldots\times P_{i,T}$, where $P_{i,t}$ is the distribution of the $t^{th}$ coin toss if $\mu=\mu_{i}$. Thus, the basic KL-divergence argument summarized in Lemma 2.5 applies to distributions $P_{1}$ and $P_{2}$. It follows that $|P_{1}(A)-P_{2}(A)|\leq\epsilon\,\sqrt{T}$. Plugging in $A=A_{0}$ and $T\leq\tfrac{1}{4\epsilon^{2}}$, we obtain $|P_{1}(A_{0})-P_{2}(A_{0})|<\tfrac{1}{2}$, contradicting (20).

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 8 A simple example: flipping one coin
