---
type: theorem
label: Theorem 4.3 ( $\mathtt{MainLB}$ )
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 20 Continuum-armed bandits
related_entities: []
date_extracted: '2026-03-16T01:32:59.479549+00:00'
---

# Theorem 4.3 ( $\mathtt{MainLB}$ )

Consider stochastic bandits, with $K$ arms and time horizon $T$ (for any $K,T$). Let $\mathtt{ALG}$ be any algorithm for this problem. Pick any positive $\epsilon\leq\sqrt{cK/T}$, where $c$ is an absolute constant from Lemma 2.8. Then there exists a problem instance $\mathcal{J}=\mathcal{J}(a^{*},\epsilon)$, $a^{*}\in[K]$, such that $$ \operatornamewithlimits{\mathbb{E}}\left[R(T)\mid\mathcal{J}\right]\geq\Omega(\epsilon T). $$

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 20 Continuum-armed bandits
