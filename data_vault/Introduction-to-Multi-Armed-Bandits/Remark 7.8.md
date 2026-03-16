---
type: remark
label: Remark 7.8
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 38 Combinatorial semi-bandits
related_entities: []
date_extracted: '2026-03-16T01:32:59.522484+00:00'
---

# Remark 7.8

In terms of the running time, it is essential that the fake costs on atoms can be computed *fast*: this is because the normalizing probability in (95) is known in advance.

Alternatively, we could have defined fake costs on atoms $e$ as

$$ \displaystyle\widehat{c}_{t}(e)=\begin{cases}c_{t}(e)/\Pr[e\in a_{t}\mid p_{t}]&\text{if $e\in a_{t}$}\\ 0&\text{otherwise}.\end{cases} $$

This definition leads to essentially the same regret bound (and, in fact, is somewhat better in practice). However, computing the probability $\Pr[e\in a_{t}\mid p_{t}]$ in a brute-force way requires iterating over all actions, which leads to running times exponential in $d$, similar to $\mathtt{Hedge}$.

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 38 Combinatorial semi-bandits
