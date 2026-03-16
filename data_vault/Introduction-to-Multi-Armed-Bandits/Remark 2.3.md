---
type: remark
label: Remark 2.3
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 7 Background on KL-divergence
related_entities: []
date_extracted: '2026-03-16T01:32:59.454871+00:00'
---

# Remark 2.3

KL-divergence is a mathematical construct with amazingly useful properties, see Theorem 2.4. The precise definition is not essential to us: any other construct with the same properties would work just as well. The deep reasons as to why KL-divergence should be defined in this way are beyond our scope.

That said, here’s see some intuition behind this definition. Suppose data points $x_{1}\,,\ \ldots\ ,x_{n}\in\Omega$ are drawn independently from some fixed, but unknown distribution $p^{*}$. Further, suppose we know that this distribution is either $p$ or $q$, and we wish to use the data to estimate which one is more likely. One standard way to quantify whether distribution $p$ is more likely than $q$ is the *log-likelihood ratio*,

$$ $\Lambda_{n}:=\sum_{i=1}^{n}\ln\frac{p(x_{i})}{q(x_{i})}.$ $$

KL-divergence is the expectation of this quantity when $p^{*}=p$, and also the limit as $n\to\infty$:

$$ $\lim_{n\to\infty}\Lambda_{n}=\operatornamewithlimits{\mathbb{E}}[\Lambda_{n}]=\mathtt{KL}(p,q)\quad\text{if $p^{*}=p$}.$ $$

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 7 Background on KL-divergence
