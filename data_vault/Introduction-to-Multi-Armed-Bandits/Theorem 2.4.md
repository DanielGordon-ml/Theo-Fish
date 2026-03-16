---
type: theorem
label: Theorem 2.4
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 7 Background on KL-divergence
related_entities:
- '[[Lemma 2.5]]'
date_extracted: '2026-03-16T01:32:59.455395+00:00'
---

# Theorem 2.4

KL-divergence satisfies the following properties:

- (a) Gibbs’ Inequality: $\mathtt{KL}(p,q)\geq 0$ for any two distributions $p,q$, with equality if and only if $p=q$.
- (b) Chain rule for product distributions: Let the sample space be a product $\Omega=\Omega_{1}\times\Omega_{1}\times\dots\times\Omega_{n}$. Let $p$ and $q$ be two distributions on $\Omega$ such that
$p=p_{1}\times p_{2}\times\dots\times p_{n}$
and
$q=q_{1}\times q_{2}\times\dots\times q_{n}$,
where $p_{j},q_{j}$ are distributions on $\Omega_{j}$, for each $j\in[n]$. Then $\mathtt{KL}(p,q)=\sum_{j=1}^{n}\mathtt{KL}(p_{j},q_{j})$.
- (c) Pinsker’s inequality: for any event $A\subset\Omega$
we have $2\left(p(A)-q(A)\right)^{2}\leq\mathtt{KL}(p,q)$.
- (d) Random coins:
$\mathtt{KL}(\mathtt{RC}_{\epsilon},\mathtt{RC}_{0})\leq 2\epsilon^{2}$,
and
$\mathtt{KL}(\mathtt{RC}_{0},\mathtt{RC}_{\epsilon})\leq\epsilon^{2}$
for all $\epsilon\in(0,\tfrac{1}{2})$.

## Relationships

- **Uses (inverse):** [[Lemma 2.5]]

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 7 Background on KL-divergence
