---
type: remark
label: Remark 5.7
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: '26 Initial results: binary prediction with experts advice'
related_entities: []
date_extracted: '2026-03-16T01:32:59.503015+00:00'
---

# Remark 5.7

This simple proof introduces a general technique that will be essential in the subsequent proofs: Define a quantity $W_{t}$ which measures the total remaining amount of “credibility” of the the experts. Make sure that by definition, $W_{1}$ is upper-bounded, and $W_{t}$ does not increase over time. Derive a lower bound on $W_{T}$ from the existence of a “good expert”. Connect $W_{t}$ with the behavior of the algorithm: prove that $W_{t}$ decreases by a constant factor whenever the algorithm makes mistake / incurs a cost.

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 26 Initial results: binary prediction with experts advice
