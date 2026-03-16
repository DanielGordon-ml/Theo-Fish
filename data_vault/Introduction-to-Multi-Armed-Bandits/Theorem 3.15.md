---
type: theorem
label: Theorem 3.15
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 18 Thompson Sampling with no prior (and no proofs)
related_entities: []
date_extracted: '2026-03-16T01:32:59.477306+00:00'
---

# Theorem 3.15

For each problem instance, Thompson Sampling with approach (i) achieves, for all $\epsilon>0$, $$ \displaystyle\operatornamewithlimits{\mathbb{E}}[R(T)]\leq(1+\epsilon)\,C\,\log(T)+\frac{f(\mu)}{\epsilon^{2}},\quad\text{where}\quad C=\sum_{\text{arms $a$}:\,\Delta(a)<0}\;\frac{\mu(a^{*})-\mu(a)}{\mathtt{KL}(\mu(a),\mu^{*})}. $$ Here $f(\mu)$ depends on the mean reward vector $\mu$, but not on $\epsilon$ or $T$.

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 18 Thompson Sampling with no prior (and no proofs)
