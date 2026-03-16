---
type: algorithm
label: 'Problem protocol: Incentivized exploration'
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: '61 Problem formulation: incentivized exploration'
related_entities: []
date_extracted: '2026-03-16T01:32:59.555517+00:00'
---

# Problem protocol: Incentivized exploration

Parameters: $K$ arms, $T$ rounds, common prior $\mathcal{P}$, reward distributions $(\mathcal{D}_{x}:\,x\in[0,1])$. Initialization: the mean rewards vector $\mu\in[0,1]^{K}$ is drawn from the prior $\mathcal{P}$. In each round $t=1,2,3\,,\ \ldots\ ,T$: 1. Algorithm chooses its recommended arm $\mathtt{rec}_{t}\in[K]$. 2. Agent $t$ arrives, receives recommendation $\mathtt{rec}_{t}$, and chooses arm $a_{t}\in[K]$. 3. (Agent’s) reward $r_{t}\in[0,1]$ is realized as an independent draw from $D_{x}$, where $x=\mu_{a_{t}}$. 4. Action $a_{t}$ and reward $r_{t}$ are observed by the algorithm.

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 61 Problem formulation: incentivized exploration
