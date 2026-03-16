---
type: remark
label: Remark 1.13
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: '3 Advanced algorithms: adaptive exploration'
related_entities:
- '[[Theorem 1.10]]'
date_extracted: '2026-03-16T01:32:59.447468+00:00'
---

# Remark 1.13

It is instructive to derive Theorem 1.10 in a different way: starting from the logarithmic regret bound in (10). Informally, we need to get rid of arbitrarily small gaps $\Delta(a)$ in the denominator. Let us fix some $\epsilon>0$, then regret consists of two parts:

- $\bullet$ all arms $a$ with $\Delta(a)\leq\epsilon$ contribute at most $\epsilon$ per round, for a total of $\epsilon T$;
- $\bullet$ each arm $a$ with $\Delta(a)>\epsilon$ contributes $R(T;a)\leq O\left(\,\frac{1}{\epsilon}\log T\,\right)$, under the clean event.

Combining these two parts and assuming the clean event, we see that $R(T)\leq O\left(\epsilon T+\tfrac{K}{\epsilon}\log{T}\right).$ Since this holds for any $\epsilon>0$, we can choose one that minimizes the right-hand side. Ensuring that $\epsilon T=\frac{K}{\epsilon}\log{T}$ yields $\epsilon=\sqrt{\frac{K}{T}\log{T}}$, and therefore $R(T)\leq O\left(\,\sqrt{KT\log T}\,\right)$.

## Relationships

- **Is Equivalent To:** [[Theorem 1.10]]

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 3 Advanced algorithms: adaptive exploration
