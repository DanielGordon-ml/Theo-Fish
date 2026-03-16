---
type: remark
label: Remark 5.3 (IID costs)
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: Chapter 5 Full Feedback and Adversarial Costs
related_entities: []
date_extracted: '2026-03-16T01:32:59.499650+00:00'
---

# Remark 5.3 (IID costs)

Consider the special case when the adversary chooses the cost $c_{t}(a)\in[0,1]$ of each arm $a$ from some fixed distribution $\mathcal{D}_{a}$, same for all rounds $t$. With full feedback, this special case is “easy”: indeed, there is no need to explore, since costs of all arms are revealed after each round. With a naive strategy such as playing arm with the lowest average cost, one can achieve regret $O\left(\sqrt{T\log\left(KT\right)}\right)$. Further, there is a nearly matching lower regret bound $\Omega(\sqrt{T}+\log K)$. The proofs of these results are left as exercise. The upper bound can be proved by a simple application of clean event/confidence radius technique that we’ve been using since Chapter\xa01. The $\sqrt{T}$ lower bound follows from the same argument as the bandit lower bound for two arms in Chapter\xa02, as this argument does not rely on bandit feedback. The $\Omega(\log K)$ lower bound holds for a simple special case, see Theorem\xa05.8.

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: Chapter 5 Full Feedback and Adversarial Costs
