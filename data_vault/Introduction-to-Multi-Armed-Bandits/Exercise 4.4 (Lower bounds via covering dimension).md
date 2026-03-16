---
type: exercise
label: Exercise 4.4 (Lower bounds via covering dimension)
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 24 Exercises and hints
related_entities: []
date_extracted: '2026-03-16T01:32:59.494975+00:00'
---

# Exercise 4.4 (Lower bounds via covering dimension)

Consider Lipschitz bandits in a metric space $(X,\mathcal{D})$. Fix $d<\mathtt{COV}_{c}(X)$, for some fixed absolute constant $c>0$. Fix an arbitrary algorithm $\mathtt{ALG}$. We are interested proving that this algorithm suffers lower bounds of the form $$ \displaystyle\operatornamewithlimits{\mathbb{E}}[R(T)]\geq\Omega\left(\,T^{(d+1)/(d+2)}\,\right). $$ (70) The subtlety is, for which $T$ can this be achieved? - (a) Assume that the covering property is nearly tight at a particular scale $\epsilon>0$, namely: $\displaystyle N_{\epsilon}(X)\geq c^{\prime}\cdot\epsilon^{-d}\quad\text{for some absolute constant $c^{\prime}$.}$ (71) Prove that (70) holds for some problem instance and $T=c^{\prime}\cdot\epsilon^{-d-2}$. - (b) Assume (71) holds for all $\epsilon>0$. Prove that for each $T$ there is a problem instance with (70). - (c) Prove that (70) holds for *some* time horizon $T$ and some problem instance. - (d) Assume that $d<\mathtt{COV}(X):=\inf_{c>0}\mathtt{COV}_{c}(X)$. Prove that there are *infinitely many* time horizons $T$ such that (70) holds for some problem instance $\mathcal{I}_{T}$. In fact, there is a distribution over these problem instances (each endowed with an infinite time horizon) such that (70) holds for *infinitely many* $T$. Hints: Part (a) follows from Exercise 4.2(c), the rest follows from part (a). For part (c), observe that (71) holds for some $\epsilon$. For part (d), observe that (71) holds for arbitrarily small $\epsilon>0$, e.g., with $c^{\prime}=1$, then apply part (a) to each such $\epsilon$. To construct the distribution over problem instances $\mathcal{I}_{T}$, choose a sufficiently sparse sequence $(T_{i}:\,i\in\mathbb{N})$, and include each instance $\mathcal{I}_{T_{i}}$ with probability $\sim 1/\log(T_{i})$, say. To remove the $\log T$ factor from the lower bound, carry out the argument above for some $d^{\prime}\in(d,\mathtt{COV}_{c}(X))$.

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 24 Exercises and hints
