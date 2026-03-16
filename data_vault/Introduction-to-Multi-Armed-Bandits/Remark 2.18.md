---
type: remark
label: Remark 2.18
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 12 Instance-dependent lower bounds (without proofs)
related_entities: []
date_extracted: '2026-03-16T01:32:59.468196+00:00'
---

# Remark 2.18

Part (b) is a stronger (i.e., larger) lower bound which implies the more familiar form in (a). Several algorithms in the literature are known to come arbitrarily close to this lower bound. In particular, a version of Thompson Sampling (another standard algorithm discussed in Chapter 3) achieves regret $\displaystyle R(t)\leq(1+\delta)\,C^{0}_{\mathcal{I}}\;\ln(t)+C^{\prime}_{\mathcal{I}}/\delta^{2},\quad\forall\delta>0,$ where $C^{0}_{\mathcal{I}}$ is from part (b) and $C^{\prime}_{\mathcal{I}}$ is some other instance-dependent constant.

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 12 Instance-dependent lower bounds (without proofs)
