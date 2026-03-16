---
type: theorem
label: Theorem 2.10
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: '9 Flipping several coins: “best-arm identification”'
related_entities:
- '[[Lemma 2.8]]'
date_extracted: '2026-03-16T01:32:59.459068+00:00'
---

# Theorem 2.10

Fix time horizon $T$ and the number of arms $K$. Fix a bandit algorithm. Choose an arm $a$ uniformly at random, and run the algorithm on problem instance $\mathcal{I}_{a}$. Then $\displaystyle\operatornamewithlimits{\mathbb{E}}[R(T)]\geq\Omega(\sqrt{KT}),$ (24), where the expectation is over the choice of arm $a$ and the randomness in rewards and the algorithm.

## Proof

Fix the parameter $\epsilon>0$ in (17), to be adjusted later, and assume that $T\leq\frac{cK}{\epsilon^{2}}$, where $c$ is the constant from Lemma\xa02.8. Fix round $t$. Let us interpret the algorithm as a 'best-arm identification' algorithm, where the prediction is simply $a_{t}$, the arm chosen in this round. We can apply Corollary\xa02.9, treating $t$ as the time horizon, to deduce that $\Pr[a_{t}\neq a]\geq\tfrac{1}{12}$. In words, the algorithm chooses a non-optimal arm with probability at least $\tfrac{1}{12}$. Recall that for each problem instances $\mathcal{I}_{a}$, the 'gap' $\Delta(a_{t}):=\mu^{*}-\mu(a_{t})$ is $\epsilon/2$ whenever a non-optimal arm is chosen. Therefore, $\operatornamewithlimits{\mathbb{E}}[\Delta(a_{t})]=\Pr[a_{t}\neq a]\cdot\tfrac{\epsilon}{2}\geq\epsilon/24.$ Summing up over all rounds, $\operatornamewithlimits{\mathbb{E}}[R(T)]=\sum_{t=1}^{T}\operatornamewithlimits{\mathbb{E}}[\Delta(a_{t})]\geq\epsilon T/24$. We obtain (24) with $\epsilon=\sqrt{cK/T}$. ∎

## Relationships

- **Uses:** [[Lemma 2.8]]

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 9 Flipping several coins: “best-arm identification”
