---
type: lemma
label: Lemma 4.14
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: '22 Adaptive discretization: the Zooming Algorithm'
related_entities: []
date_extracted: '2026-03-16T01:32:59.488481+00:00'
---

# Lemma 4.14

$\Delta(x)\leq 3\,r_{t}(x)$ for each arm $x$ and each round $t$.

## Proof

Suppose arm $x$ is played in this round. By the covering invariant, the best arm $x^{*}$ was covered by the confidence ball of some active arm $y$, i.e.,\xa0$x^{*}\in\mathbf{B}_{t}(y)$.
It follows that

$$ \mathtt{index}(x)\geq\mathtt{index}(y)=\underbrace{\mu_{t}(y)+r_{t}(y)}_{\geq\mu(y)}+r_{t}(y)\geq\mu(x^{*})=\mu^{*} $$

The last inequality holds because of the Lipschitz condition. On the other hand:

$$ \mathtt{index}(x)=\underbrace{\mu_{t}(x)}_{\leq\mu(x)+r_{t}(x)}+2\cdot r_{t}(x)\leq\mu(x)+3\cdot r_{t}(x) $$

Putting these two equations together: $\Delta(x):=\mu^{*}-\mu(x)\leq 3\cdot r_{t}(x)$.

Now suppose arm $x$ is not played in round $t$. If it has never been played before round $t$, then $r_{t}(x)>1$ and the lemma follows trivially. Else, letting $s$ be the last time when $x$ has been played before round $t$, we see that $r_{t}(x)=r_{s}(x)\geq\Delta(x)/3$.
∎

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 22 Adaptive discretization: the Zooming Algorithm
