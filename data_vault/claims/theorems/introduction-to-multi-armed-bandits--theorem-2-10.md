---
slug: introduction-to-multi-armed-bandits--theorem-2-10
label: Theorem 2.10
claim_type: theorem
statement: Fix time horizon $T$ and the number of arms $K$. Fix a bandit algorithm.
  Choose an arm $a$ uniformly at random, and run the algorithm on problem instance
  $\mathcal{I}_{a}$. Then $\mathbb{E}[R(T)] \geq \Omega(\sqrt{KT})$, where the expectation
  is over the choice of arm $a$ and the randomness in rewards and the algorithm.
proof: 'Fix the parameter $\epsilon > 0$ in (17), to be adjusted later, and assume
  that $T \leq \frac{cK}{\epsilon^{2}}$, where $c$ is the constant from Lemma 2.8.


  Fix round $t$. Let us interpret the algorithm as a "best-arm identification" algorithm,
  where the prediction is simply $a_{t}$, the arm chosen in this round. We can apply
  Corollary 2.9, treating $t$ as the time horizon, to deduce that $\Pr[a_{t} \neq
  a] \geq \tfrac{1}{12}$. In words, the algorithm chooses a non-optimal arm with probability
  at least $\tfrac{1}{12}$. Recall that for each problem instance $\mathcal{I}_{a}$,
  the "gap" $\Delta(a_{t}) := \mu^{*} - \mu(a_{t})$ is $\epsilon/2$ whenever a non-optimal
  arm is chosen. Therefore, $\mathbb{E}[\Delta(a_{t})] = \Pr[a_{t} \neq a] \cdot \tfrac{\epsilon}{2}
  \geq \epsilon/24$.


  Summing up over all rounds, $\mathbb{E}[R(T)] = \sum_{t=1}^{T} \mathbb{E}[\Delta(a_{t})]
  \geq \epsilon T / 24$. We obtain (24) with $\epsilon = \sqrt{cK/T}$.'
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/time-horizon-t]]'
- '[[concepts/stochastic-bandits]]'
- '[[concepts/instantaneous-regret]]'
- '[[concepts/expected-regret]]'
- '[[concepts/family-of-problem-instances]]'
- '[[concepts/gap]]'
- '[[concepts/number-of-arms-k]]'
- '[[concepts/regret-r-t]]'
- '[[concepts/bandit-algorithm]]'
about_meta:
- target: '[[concepts/time-horizon-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/stochastic-bandits]]'
  role: primary
  aspect: ''
- target: '[[concepts/instantaneous-regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/expected-regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/family-of-problem-instances]]'
  role: primary
  aspect: ''
- target: '[[concepts/gap]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-arms-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret-r-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/bandit-algorithm]]'
  role: primary
  aspect: ''
depends_on: []
depends_on_meta: []
sourced_from:
- '[[sources/1904.07272|Introduction to Multi-Armed Bandits]]'
sourced_from_meta:
- target: '[[sources/1904.07272|Introduction to Multi-Armed Bandits]]'
  section: ''
  page: ''
  confidence: 0.0
---

# Theorem 2.10

Fix time horizon $T$ and the number of arms $K$. Fix a bandit algorithm. Choose an arm $a$ uniformly at random, and run the algorithm on problem instance $\mathcal{I}_{a}$. Then $\mathbb{E}[R(T)] \geq \Omega(\sqrt{KT})$, where the expectation is over the choice of arm $a$ and the randomness in rewards and the algorithm.


## Proof

Fix the parameter $\epsilon > 0$ in (17), to be adjusted later, and assume that $T \leq \frac{cK}{\epsilon^{2}}$, where $c$ is the constant from Lemma 2.8.

Fix round $t$. Let us interpret the algorithm as a "best-arm identification" algorithm, where the prediction is simply $a_{t}$, the arm chosen in this round. We can apply Corollary 2.9, treating $t$ as the time horizon, to deduce that $\Pr[a_{t} \neq a] \geq \tfrac{1}{12}$. In words, the algorithm chooses a non-optimal arm with probability at least $\tfrac{1}{12}$. Recall that for each problem instance $\mathcal{I}_{a}$, the "gap" $\Delta(a_{t}) := \mu^{*} - \mu(a_{t})$ is $\epsilon/2$ whenever a non-optimal arm is chosen. Therefore, $\mathbb{E}[\Delta(a_{t})] = \Pr[a_{t} \neq a] \cdot \tfrac{\epsilon}{2} \geq \epsilon/24$.

Summing up over all rounds, $\mathbb{E}[R(T)] = \sum_{t=1}^{T} \mathbb{E}[\Delta(a_{t})] \geq \epsilon T / 24$. We obtain (24) with $\epsilon = \sqrt{cK/T}$.
