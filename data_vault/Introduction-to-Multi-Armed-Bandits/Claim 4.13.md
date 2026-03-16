---
type: lemma
label: Claim 4.13
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: '22 Adaptive discretization: the Zooming Algorithm'
related_entities: []
date_extracted: '2026-03-16T01:32:59.487845+00:00'
---

# Claim 4.13

Assume that realized rewards take values on a finite set. Then $\Pr[\mathcal{E}] \geq 1-\frac{1}{T^{2}}$.

## Proof

By Hoeffding Inequality, $\Pr[\mathcal{E}_{x}] \geq 1-\frac{1}{T^{4}}$ for each arm $x\in X$. However, one cannot immediately apply the Union Bound here because there may be too many arms.

Fix an instance of Lipschitz bandits. Let $X_{0}$ be the set of all arms that can possibly be activated by the algorithm on this problem instance. Note that $X_{0}$ is finite; this is because the algorithm is deterministic, the time horizon $T$ is fixed, and, as we assumed upfront, realized rewards can take only finitely many values. (This is the only place where we use this assumption.)

Let $N$ be the total number of arms activated by the algorithm.
Define arms $y_{j}\in X_{0}$, $j\in[T]$, as follows

$$ y_{j}=\left\{\begin{array}{ll}j\text{-th arm activated,}&\text{\quad if }j\leq N\\ y_{N},&\text{\quad otherwise}.\end{array}\right. $$

Here $N$ and $y_{j}$'s are random variables, the randomness coming from the reward realizations. Note that $\{y_{1}\,,\ \ldots\ ,y_{T}\}$ is precisely the set of arms activated in a given execution of the algorithm. Since the clean event holds trivially for all arms that are not activated, the clean event can be rewritten as $\mathcal{E}=\cap_{j=1}^{T}\mathcal{E}_{y_{j}}.$
In what follows, we prove that the clean event $\mathcal{E}_{y_{j}}$ happens with high probability for each $j\in[T]$.

Fix an arm $x\in X_{0}$ and fix $j\in[T]$. Whether the event $\{y_{j}=x\}$ holds is determined by the rewards of other arms. (Indeed, by the time arm $x$ is selected by the algorithm, it is already determined whether $x$ is the $j$-th arm activated!) Whereas whether the clean event $\mathcal{E}_{x}$ holds is determined by the rewards of arm $x$ alone. It follows that the events $\{y_{j}=x\}$ and $\mathcal{E}_{x}$ are independent. Therefore, if $\Pr[y_{j}=x]>0$ then

$$ \Pr[\mathcal{E}_{y_{j}}\mid y_{j}=x]=\Pr[\mathcal{E}_{x}\mid y_{j}=x]=\Pr[\mathcal{E}_{x}]\geq 1-\tfrac{1}{T^{4}} $$

Now we can sum over all $x\in X_{0}$:

$$ \Pr[\mathcal{E}_{y_{j}}]=\sum_{x\in X_{0}}\Pr[y_{j}=x]\cdot\Pr[\mathcal{E}_{y_{j}}\mid x=y_{j}]\geq 1-\tfrac{1}{T^{4}} $$

To complete the proof, we apply the Union bound over all $j\in[T]$:

$$ \Pr[\mathcal{E}_{y_{j}},j\in[T]]\geq 1-\tfrac{1}{T^{3}}.\qed $$

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 22 Adaptive discretization: the Zooming Algorithm
