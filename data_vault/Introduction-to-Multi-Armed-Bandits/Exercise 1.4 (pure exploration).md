---
type: exercise
label: Exercise 1.4 (pure exploration)
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 6 Exercises and hints
related_entities: []
date_extracted: '2026-03-16T01:32:59.452471+00:00'
---

# Exercise 1.4 (pure exploration)

Recall that in “pure-exploration bandits”, after $T$ rounds the algorithm outputs a prediction: a guess $y_{T}$ for the best arm. We focus on the instantaneous regret $\Delta(y_{T})$ for the prediction.
- (a) Take any bandit algorithm with an instance-independent regret bound $E[R(T)]\leq f(T)$, and construct an algorithm for “pure-exploration bandits” such that $\operatornamewithlimits{\mathbb{E}}[\Delta(y_{T})]\leq f(T)/T$. Note: Surprisingly, taking $y_{T}=a_{t}$ does not seem to work in general – definitely not immediately. Taking $y_{T}$ to be the arm with a maximal empirical reward does not seem to work, either. But there is a simple solution … Take-away: We can easily obtain $\operatornamewithlimits{\mathbb{E}}[\Delta(y_{T})]=O(\sqrt{K\log(T)/T}$ from standard algorithms such as $\mathtt{UCB1}$ and Successive Elimination. However, as parts (bc) show, one can do much better!
- (b) Consider Successive Elimination with $y_{T}=a_{T}$. Prove that (with a slightly modified definition of the confidence radius) this algorithm can achieve $\displaystyle\operatornamewithlimits{\mathbb{E}}\left[\,\Delta(y_{T})\,\right]\leq T^{-\gamma}\quad\text{if $T>T_{\mu,\gamma}$},$ where $T_{\mu,\gamma}$ depends only on the mean rewards $\mu(a):a\in\mathcal{A}$ and the $\gamma$. This holds for an arbitrarily large constant $\gamma$, with only a multiplicative-constant increase in regret.
- (c) Prove that alternating the arms (and predicting the best one) achieves, for any fixed $\gamma<1$: $\displaystyle\operatornamewithlimits{\mathbb{E}}\left[\,\Delta(y_{T})\,\right]\leq e^{-\Omega(T^{\gamma})}\quad\text{if $T>T_{\mu,\gamma}$},$ where $T_{\mu,\gamma}$ depends only on the mean rewards $\mu(a):a\in\mathcal{A}$ and the $\gamma$.

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 6 Exercises and hints
