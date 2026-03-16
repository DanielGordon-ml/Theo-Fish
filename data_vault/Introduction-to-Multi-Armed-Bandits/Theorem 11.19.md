---
type: theorem
label: Theorem 11.19
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 65 A necessary and sufficient assumption on the prior
related_entities: []
date_extracted: '2026-03-16T01:32:59.564310+00:00'
---

# Theorem 11.19

Suppose ties in Definition 11.4 are always resolved in favor of arm 1 (i.e., imply $\mathtt{rec}_{t}=1$). Absent (170), any BIC algorithm never plays arm 2.

## Proof

Proof. Suppose Property (170) does not hold. Let $\mathtt{ALG}$ be a strongly BIC algorithm. We prove by induction on $t$ that $\mathtt{ALG}$ cannot recommend arm $2$ to agent $t$. This is trivially true for $t=1$. Suppose the induction hypothesis is true for some $t$. Then the decision whether to recommend arm $2$ in round $t+1$ (i.e., whether $a_{t+1}=2$) is determined by the first $t$ outcomes of arm $1$ and the algorithm’s random seed. Letting $U=\{a_{t+1}=2\}$, we have

$\displaystyle\operatornamewithlimits{\mathbb{E}}[\mu_{2}-\mu_{1}\mid U]$

$\displaystyle=\operatornamewithlimits{\mathbb{E}}\left[\,\;\operatornamewithlimits{\mathbb{E}}[\mu_{2}-\mu_{1}\mid\mathcal{S}_{1,t}]\;\;\mid U\,\right]$ (by Fact 11.6)

$\displaystyle=\operatornamewithlimits{\mathbb{E}}[G_{1,t}|U]$ (by definition of $G_{1,t}$)

$\displaystyle\leq 0$

$\displaystyle\text{\emph{(since (\ref{BIC:eq:prop}) does not hold)}}.$

The last inequality holds because the negation of (170) implies $\Pr[G_{1,t}\leq 0]=1$. This contradicts $\mathtt{ALG}$ being BIC, and completes the induction proof. ∎

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 65 A necessary and sufficient assumption on the prior
