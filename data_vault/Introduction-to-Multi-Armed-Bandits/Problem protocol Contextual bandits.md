---
type: definition
label: 'Problem protocol: Contextual bandits'
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: Chapter 8 Contextual Bandits
related_entities: []
date_extracted: '2026-03-16T01:32:59.526940+00:00'
---

# Problem protocol: Contextual bandits

We consider a generalization called *contextual bandits*, defined as follows: Problem protocol: Contextual bandits For each round $t\in[T]$: - 1. algorithm observes a “context” $x_{t}$, - 2. algorithm picks an arm $a_{t}$, - 3. reward $r_{t}\in[0,1]$ is realized. The reward $r_{t}$ in each round $t$ depends both on the context $x_{t}$ and the chosen action $a_{t}$. We make the IID assumption: reward $r_{t}$ is drawn independently from some distribution parameterized by the $(x_{t},a_{t})$ pair, but same for all rounds $t$. The expected reward of action $a$ given context $x$ is denoted $\mu(a|x)$.

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: Chapter 8 Contextual Bandits
