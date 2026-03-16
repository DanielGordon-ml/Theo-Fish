---
type: exercise
label: Exercise 10.1
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 60 Exercises and hints
related_entities: []
date_extracted: '2026-03-16T01:32:59.553132+00:00'
---

# Exercise 10.1

Fix time horizon $T$ and budget $B$. Consider an algorithm $\mathtt{ALG}$ which explores uniformly at random for the first $N$ steps, where $N$ is fixed in advance, then chooses some distribution $D$ over arms and draws independently from this distribution in each subsequent rounds.
- (a)
Assume $B<\sqrt{T}$. Prove that there exists a problem instance on which $\mathtt{ALG}$ suffers linear regret:
$\mathtt{OPT}-\operatornamewithlimits{\mathbb{E}}[\mathtt{REW}]>\Omega(T).$
Hint: Posit one resource other than time, and three arms:
$\bullet$
the *bad arm*, with deterministic reward 0 and consumption $1$;
$\bullet$
the *good arm*, with deterministic reward $1$ and expected consumption $\tfrac{B}{T}$;
$\bullet$
the *decoy arm*, with deterministic reward $1$ and expected consumption
$2\tfrac{B}{T}$.
Use the following fact: given two coins with expectations $\tfrac{B}{T}$ and $\tfrac{B}{T}+c/\sqrt{N}$, for a sufficiently low absolute constant $c$, after only $N$ tosses of each coin, for any algorithm it is a constant-probability event that this algorithm cannot tell one coin from another.
- (b)
Assume $B>\Omega(T)$. Choose $N$ and $D$ so that $\mathtt{ALG}$ achieves regret
$\mathtt{OPT}-\operatornamewithlimits{\mathbb{E}}[\mathtt{REW}]<\tilde{O}(T^{2/3})$.
Hint: Choose $D$ as a solution to the “optimistic” linear program (150), with rescaled budget
$B^{\prime}=B(1-\sqrt{K/T})$.
Compare $D$ to the value of the original linear program (141) with budget $B^{\prime}$, and the latter to the value of (141) with budget $B$.

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 60 Exercises and hints
