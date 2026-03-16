---
type: lemma
label: Claim 7.16
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: '39 Online Linear Optimization: Follow The Perturbed Leader'
related_entities: []
date_extracted: '2026-03-16T01:32:59.526435+00:00'
---

# Claim 7.16

let $X$ be a random variable uniformly distributed on the interval $[-\frac{1}{\epsilon},\frac{1}{\epsilon}]$. We claim that for any $a\in[0,U/d]$ there exists a deterministic function $g(X,a)$ of $X$ and $a$ such that $g(X,a)$ and $X+a$ have the same marginal distribution, and $\Pr[g(X,a)\neq X]\leq\epsilon U/d$.

## Proof

Let us define $\displaystyle g(X,a)=\begin{cases}X&\text{if $X\in[v-\frac{1}{\epsilon},\frac{1}{\epsilon}]$},\\ a-X&\text{if $X\in[-\frac{1}{\epsilon},v-\frac{1}{\epsilon})$}.\end{cases}$ It is easy to see that $g(X,a)$ is distributed uniformly on $[v- \frac{1}{\epsilon},v+\frac{1}{\epsilon}]$. This is because $a-X$ is distributed uniformly on $[\frac{1}{\epsilon},v+\frac{1}{\epsilon}]$ conditional on $X\in[-\frac{1}{\epsilon},v- \frac{1}{\epsilon})$. Moreover, $\Pr[g(X,a)\neq X]\leq\Pr[X\not\in[v-\tfrac{1}{\epsilon},\tfrac{1}{\epsilon}]]=\epsilon v/2\leq\tfrac{\epsilon U}{2d}.$

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 39 Online Linear Optimization: Follow The Perturbed Leader
