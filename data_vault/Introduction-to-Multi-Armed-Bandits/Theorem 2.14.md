---
type: theorem
label: Theorem 2.14
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 12 Instance-dependent lower bounds (without proofs)
related_entities: []
date_extracted: '2026-03-16T01:32:59.465082+00:00'
---

# Theorem 2.14

Fix $K$, the number of arms. Consider an algorithm such that $\displaystyle\operatornamewithlimits{\mathbb{E}}[R(t)]\leq O(C_{\mathcal{I},\alpha}\;t^{\alpha})\quad\text{for each problem instance $\mathcal{I}$ and each $\alpha>0$}.$ (32) Fix an arbitrary problem instance $\mathcal{I}$. For this problem instance: $\displaystyle\text{There exists time $t_{0}$ such that for any $t\geq t_{0}$}\quad\operatornamewithlimits{\mathbb{E}}[R(t)]\geq C_{\mathcal{I}}\ln(t),$ (33) for some constant $C_{\mathcal{I}}$ that depends on the problem instance, but not on time $t$.

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 12 Instance-dependent lower bounds (without proofs)
