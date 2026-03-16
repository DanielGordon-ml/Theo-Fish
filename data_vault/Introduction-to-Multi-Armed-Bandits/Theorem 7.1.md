---
type: theorem
label: Theorem 7.1
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 'Recap: bandits-to-experts reduction'
related_entities: []
date_extracted: '2026-03-16T01:32:59.518395+00:00'
---

# Theorem 7.1

Consider Algorithm 1 with algorithm $\mathtt{ALG}$ that achieves regret bound $\operatornamewithlimits{\mathbb{E}}[R(T)]\leq f(T,K,u)$ against adaptive, $u$-bounded adversary, for any given $u>0$ that is known to the algorithm. Consider adversarial bandits with a deterministic, oblivious adversary. Assume 'fake costs' satisfy $$ $\operatornamewithlimits{\mathbb{E}}\left[\,\widehat{c}_{t}(x)\mid p_{t}\,\right]=c_{t}(x)\text{ and }\widehat{c}_{t}(x)\leq u/\gamma\qquad\text{for all experts $x$ and all rounds $t$},$ $$ where $u$ is some number that is known to the algorithm. Then Algorithm 1 achieves regret $$ $\displaystyle\operatornamewithlimits{\mathbb{E}}[R(T)]\leq f(T,K,u/\gamma)+\gamma T.$ $$

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: Recap: bandits-to-experts reduction
