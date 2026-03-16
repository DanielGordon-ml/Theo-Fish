---
type: example
label: Example 4.7
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 21 Lipschitz bandits
related_entities: []
date_extracted: '2026-03-16T01:32:59.483863+00:00'
---

# Example 4.7

To characterize the regret of uniform discretization more compactly, suppose the metric space is $X=[0,1]^{d}$, $d\in\mathbb{N}$ under the $\ell_{p}$ metric, $p\geq 1$. Consider a subset $S\subset X$ that consists of all points whose coordinates are multiples of a given $\epsilon>0$. Then $|S|\leq{\lceil{1/\epsilon}\rceil}^{d}$ points, and its discretization error is $\mathtt{DE}(S)\leq c_{p,d}\cdot\epsilon$, where $c_{p,d}$ is a constant that depends only on $p$ and $d$; e.g., $c_{p,d}=d$ for $p=1$. Plugging this into (53) and taking $\epsilon=(T\,/\,\log T)^{-1/(d+2)}$, we obtain $\displaystyle \operatornamewithlimits{\mathbb{E}}[R(T)]\leq(1+c_{\mathtt{ALG}})\cdot T^{(d+1)/(d+2)}\;(c\log T)^{1/(d+2)}.$

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 21 Lipschitz bandits
