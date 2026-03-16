---
type: theorem
label: Theorem 11.17
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 64 Repeated hidden exploration
related_entities: []
date_extracted: '2026-03-16T01:32:59.562370+00:00'
---

# Theorem 11.17

Consider $\mathtt{RepeatedHE}$ with exploration probability $\epsilon>0$ and $N_{0}$ initial samples. Let $N$ be the number of exploration rounds $t>N_{0}$. (Note that $\operatornamewithlimits{\mathbb{E}}[N]=\epsilon(T-N_{0})$, and $|N-\operatornamewithlimits{\mathbb{E}}[N]|\leq O(\sqrt{T\,\log T})$ with high probability.) Then: - (a) If $\mathtt{ALG}$ always chooses arm $2$, $\mathtt{RepeatedHE}$ chooses arm $2$ at least N times. - (b) The expected reward of $\mathtt{RepeatedHE}$ is at least $\tfrac{1}{\epsilon}\,\operatornamewithlimits{\mathbb{E}}\left[\,\mathtt{REW}^{\mathtt{ALG}}(N)\,\right]$. - (c) Bayesian regret of $\mathtt{RepeatedHE}$ is $\mathtt{BR}(T)\leq N_{0}+\tfrac{1}{\epsilon}\,\operatornamewithlimits{\mathbb{E}}\left[\,\mathtt{BR}^{\mathtt{ALG}}(N)\,\right]$.

## Proof

Part (a) is obvious. Part (c) trivially follows from part (b). The proof of part (b) invokes Wald’s identify and the fact that the expected reward in “exploitation” is at least as large as in “exploration” for the same round.

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 64 Repeated hidden exploration
