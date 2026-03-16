---
type: definition
label: 'Problem protocol: Adversarial bandits with expert advice'
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 31 Adversarial bandits with expert advice
related_entities: []
date_extracted: '2026-03-16T01:32:59.512658+00:00'
---

# Problem protocol: Adversarial bandits with expert advice

Given: $K$ arms, set $\mathcal{E}$ of $N$ experts, $T$ rounds (all known). In each round $t\in[T]$: 1. adversary picks cost $c_{t}(a)\geq 0$ for each arm $a\in[K]$, 2. each expert $e\in\mathcal{E}$ recommends an arm $a_{t,e}$ (observed by the algorithm), 3. algorithm picks arm $a_{t}\in[K]$ and receives the corresponding cost $c_{t}(a_{t})$. The total cost of each expert is defined as $\mathtt{cost}(e)=\sum_{t\in[T]}c_{t}(a_{t,e})$. The goal is to minimize regret relative to the best expert: $$ R(T)=\mathtt{cost}(\text{$\mathtt{ALG}$})-\min_{e\in\mathcal{E}}{\mathtt{cost}(e)}. $$

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 31 Adversarial bandits with expert advice
