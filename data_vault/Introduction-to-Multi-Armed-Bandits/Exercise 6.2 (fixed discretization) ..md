---
type: exercise
label: Exercise 6.2 (fixed discretization) .
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 36 Exercises and hints
related_entities: []
date_extracted: '2026-03-16T01:32:59.517356+00:00'
---

# Exercise 6.2 (fixed discretization) .

Let us extend the fixed discretization approach from Chapter\xa04 to adversarial bandits.
Consider adversarial bandits with the set of arms $\mathcal{A}=[0,1]$. Fix $\epsilon>0$ and let $S_{\epsilon}$ be the $\epsilon$-uniform mesh over $\mathcal{A}$, i.e.,\xa0the set of all points in $[0,1]$ that are integer multiples of $\epsilon$. For a subset $S\subset\mathcal{A}$, the optimal total cost is
$\mathtt{cost}^{*}(S):=\min_{a\in S}\mathtt{cost}(a)$,
and the discretization error is defined as
$\mathtt{DE}(S_{\epsilon})=\left(\,\mathtt{cost}^{*}(S)-\mathtt{cost}^{*}(\mathcal{A})\,\right)/T$.

- (a)
Prove that $\mathtt{DE}(S_{\epsilon})\leq L\epsilon$, assuming Lipschitz property:
$\displaystyle|c_{t}(a)-c_{t}(a^{\prime})|\leq L\cdot|a-a^{\prime}|\quad\text{for all arms $a,a^{\prime}\in\mathcal{A}$ and all rounds $t$}.$
(93)
- (b)
Consider a version of dynamic pricing (see Section\xa024.4), where the values $v_{1}\,,\ \ldots\ ,v_{T}$ are chosen by a deterministic, oblivious adversary. For compatibility, state the problem in terms of costs rather than rewards: in each round $t$, the cost is $-p_{t}$ if there is a sale, 0 otherwise. Prove that $\mathtt{DE}(S_{\epsilon})\leq\epsilon$.
Note: It is a special case of adversarial bandits with some extra structure which allows us to bound discretization error *without assuming Lipschitzness*.
- (c)
Assume that $\mathtt{DE}(S_{\epsilon})\leq\epsilon$ for all $\epsilon>0$. Obtain an algorithm with regret
$\operatornamewithlimits{\mathbb{E}}[R(T)]\leq O(T^{2/3}\log T)$.
Hint: Use algorithm $\mathtt{Exp3}$ with arms $S\subset\mathcal{A}$, for a well-chosen subset $S$.

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 36 Exercises and hints
