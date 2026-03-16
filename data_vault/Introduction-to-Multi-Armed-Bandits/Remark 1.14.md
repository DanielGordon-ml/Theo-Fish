---
type: remark
label: Remark 1.14
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: '3 Advanced algorithms: adaptive exploration'
related_entities: []
date_extracted: '2026-03-16T01:32:59.448015+00:00'
---

# Remark 1.14

Let’s see why UCB-based selection rule makes sense. An arm $a$ can have a large $\mathtt{UCB}_{t}(a)$ for two reasons (or combination thereof): because the average reward $\bar{\mu}_{t}(a)$ is large, in which case this arm is likely to have a high reward, and/or because the confidence radius $r_{t}(a)$ is large, in which case this arm has not been explored much. Either reason makes this arm worth choosing. Put differently, the two summands in $\mathtt{UCB}_{t}(a)=\bar{\mu}_{t}(a)+r_{t}(a)$ represent, resp., exploitation and exploration, and summing them up is one natural way to resolve exploration-exploitation tradeoff.

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 3 Advanced algorithms: adaptive exploration
