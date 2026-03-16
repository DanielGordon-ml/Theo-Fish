---
type: exercise
label: Exercise 10.3
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 60 Exercises and hints
related_entities: []
date_extracted: '2026-03-16T01:32:59.554089+00:00'
---

# Exercise 10.3

Consider dynamic pricing with limited supply of $d$ products: actions are price vectors $p\in[0,1]^{d}$, and
$c_{i}(p)\in[0,1]$
is the expected per-round amount of product $i$ sold at price vector $p$. Let
$P_{\epsilon}:=[0,1]^{d}\cap\epsilon\,\mathbb{N}^{d}$
be a uniform mesh of prices with step $\epsilon\in(0,1)$. Let $\mathtt{OPT}(P_{\epsilon})$ and $\mathtt{OPT_{FA}}(P_{\epsilon})$ be the resp. benchmark restricted to the price vectors in $P_{\epsilon}$.
- (a)
Assume that $c_{i}(p)$ is Lipschitz in $p$, for each product $i$:
$|c_{i}(p)-c_{i}(p^{\prime})|\leq L\cdot\|p-p\|_{1},\quad\forall p,p^{\prime}\in[0,1]^{d}.$
Prove that the discretization error is
$\mathtt{OPT}-\mathtt{OPT}(P_{\epsilon})\leq O(\epsilon dL)$.
Using an optimal $\mathtt{BwK}$ algorithm with appropriately action set $P_{\epsilon}$, obtain regret rate
$\mathtt{OPT}-\operatornamewithlimits{\mathbb{E}}[\mathtt{REW}]<\tilde{O}(T^{(d+1)/(d+2)})$.
Hint: To bound the discretization error, use the approach from Exercise\xa010.1; now the deviations in rewards/consumptions are due to the change in $p$.
- (b)
For the single-product case ($d=1$), consider the fixed-arm benchmark, and prove that the resp. discretization error is
$\mathtt{OPT_{FA}}-\mathtt{OPT_{FA}}(P_{\epsilon})\leq O(\epsilon\,\sqrt{B})$.
Hint: Consider “approximate total reward” at price $p$ as
$V(p)=p\cdot\min(B,\,T\cdot S(p))$.
Prove that the expected total reward for always using price $p$ lies between
$V(p)-\tilde{O}(\sqrt{B})$ and $V(p)$.

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 60 Exercises and hints
