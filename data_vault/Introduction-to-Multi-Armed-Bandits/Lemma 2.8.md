---
type: lemma
label: Lemma 2.8
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: '9 Flipping several coins: “best-arm identification”'
related_entities:
- '[[Theorem 2.10]]'
date_extracted: '2026-03-16T01:32:59.457540+00:00'
---

# Lemma 2.8

Consider a 'best-arm identification' problem with $T\leq\frac{cK}{\epsilon^{2}}$, for a small enough absolute constant $c>0$. Fix any deterministic algorithm for this problem. Then there exists at least $\lceil{K/3}\rceil$ arms $a$ such that, for problem instances $\mathcal{I}_{a}$ defined in (17), we have $\Pr\left[\,y_{T}=a\mid\mathcal{I}_{a}\,\right]<\tfrac{3}{4}.$ (22)

## Proof

Proof ($K=2$ arms). Let us set up the sample space which we will use in the proof. Let $\left(\,r_{t}(a):\;a\in[K],t\in[T]\,\right)$ be a tuple of mutually independent Bernoulli random variables such that $\operatornamewithlimits{\mathbb{E}}\left[\,r_{t}(a)\,\right]=\mu(a)$. We refer to this tuple as the *rewards table*, where we interpret $r_{t}(a)$ as the reward received by the algorithm for the $t$-th time it chooses arm $a$. The sample space is $\Omega=\{0,1\}^{K\times T}$, where each outcome $\omega\in\Omega$ corresponds to a particular realization of the rewards table. Any event about the algorithm can be interpreted as a subset of $\Omega$, i.e.,\xa0the set of outcomes $\omega\in\Omega$ for which this event happens; we assume this interpretation throughout without further notice. Each problem instance $\mathcal{I}_{j}$ defines distribution $P_{j}$ on $\Omega$: $P_{j}(A)=\Pr\left[\,A\mid\text{instance $\mathcal{I}_{j}$}\,\right]\quad\text{for each $A\subset\Omega$}.$ Let $P_{j}^{a,t}$ be the distribution of $r_{t}(a)$ under instance $\mathcal{I}_{j}$, so that $P_{j}=\prod_{a\in[K],\;t\in[T]}P_{j}^{a,t}$. We need to prove that (22) holds for at least one of the arms. For the sake of contradiction, assume it fails for both arms. Let $A=\{y_{T}=1\}\subset\Omega$ be the event that the algorithm predicts arm $1$. Then $P_{1}(A)\geq\tfrac{3}{4}$ and $P_{2}(A)\leq\tfrac{1}{4}$, so their difference is $P_{1}(A)-P_{2}(A)\geq\tfrac{1}{2}$. To arrive at a contradiction, we use a similar KL-divergence argument as before: $\displaystyle 2\left(\,P_{1}(A)-P_{2}(A)\,\right)^{2}$ $\displaystyle\leq\mathtt{KL}(P_{1},P_{2})$ (by Pinsker's inequality) $\displaystyle=\sum_{a=1}^{K}\sum_{t=1}^{T}\mathtt{KL}(P_{1}^{a,t},P_{2}^{a,t})$ (by Chain Rule) $\displaystyle\leq 2T\cdot 2\epsilon^{2}$ $\displaystyle\text{\emph{(by Theorem~\ref{LB:thm:KL-props}(d))}}.$ (23) The last inequality holds because for each arm $a$ and each round $t$, one of the distributions $P_{1}^{a,t}$ and $P_{2}^{a,t}$ is a fair coin $\mathtt{RC}_{0}$, and another is a biased coin $\mathtt{RC}_{\epsilon}$. Simplifying (23), $P_{1}(A)-P_{2}(A)\leq\epsilon\sqrt{2\,T}<\tfrac{1}{2}\quad\text{whenever $T\leq(\tfrac{1}{4\epsilon})^{2}$}.\qed$

## Relationships

- **Uses (inverse):** [[Theorem 2.10]]

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 9 Flipping several coins: “best-arm identification”
