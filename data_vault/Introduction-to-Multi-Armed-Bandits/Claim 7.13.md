---
type: lemma
label: Claim 7.13
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: '39 Online Linear Optimization: Follow The Perturbed Leader'
related_entities: []
date_extracted: '2026-03-16T01:32:59.524930+00:00'
---

# Claim 7.13

For all rounds $i<j$, $\sum_{t=1}^{j}v_{t}\cdot M(v_{i:t})\leq v_{i:j}\cdot M(v_{i:j})$.

## Proof

The proof is by induction on $j-i$. The claim is trivially satisfied for the base case $i=j$. For the inductive step: $\displaystyle\sum_{t=i}^{j-1}v_{t}\cdot M(v_{i:t})$ $\displaystyle\leq v_{i:j-1}\cdot M(v_{i:j-1})$ (by the inductive hypothesis) $\displaystyle\leq v_{i:j-1}\cdot M(v_{i:j})$ $\displaystyle\text{\emph{(by (\ref{lin:eq:FPL-analysis-M}) with $a=M(v_{i:j})$)}}.$ Add $v_{j}\cdot M(v_{i:j})$ to both sides to complete the proof.

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 39 Online Linear Optimization: Follow The Perturbed Leader
