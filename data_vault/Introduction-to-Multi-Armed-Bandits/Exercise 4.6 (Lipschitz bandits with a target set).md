---
type: exercise
label: Exercise 4.6 (Lipschitz bandits with a target set)
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 24 Exercises and hints
related_entities: []
date_extracted: '2026-03-16T01:32:59.495989+00:00'
---

# Exercise 4.6 (Lipschitz bandits with a target set)

Consider Lipschitz bandits on metric space $(X,\mathcal{D})$ with $\mathcal{D}(\cdot,\cdot)\leq\frac{1}{2}$. Fix the best reward $\mu^{*}\in[\frac{3}{4},1]$ and a subset $S\subset X$ and assume that $$ \mu(x)=\mu^{*}-\mathcal{D}(x,S)\quad\forall x\in X,\qquad\text{where }\mathcal{D}(x,S):=\inf_{y\in S}\mathcal{D}(x,y). $$ In words, the mean reward is determined by the distance to some “target set” $S$. - (a) Prove that $\mu^{*}-\mu(x)\leq\mathcal{D}(x,S)$ for all arms $x$, and that this condition suffices for the analysis of the zooming algorithm, instead of the full Lipschitz condition (57). - (b) Assume the metric space is $([0,1]^{d},\ell_{2})$, for some $d\in\mathbb{N}$. Prove that the zooming dimension of the problem instance (with a suitably chosen multiplier) is at most the covering dimension of $S$. Take-away: In part (b), the zooming algorithm achieves regret $\tilde{O}(T^{(b+1)/(b+2)})$, where $b$ is the covering dimension of the target set $S$. Note that $b$ could be much smaller than $d$, the covering dimension of the entire metric space. In particular, one achieves regret $\tilde{O}(\sqrt{T})$ if $S$ is finite.

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 24 Exercises and hints
