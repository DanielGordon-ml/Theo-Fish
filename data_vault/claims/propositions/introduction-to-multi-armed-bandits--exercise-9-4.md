---
slug: introduction-to-multi-armed-bandits--exercise-9-4
label: Exercise 9.4
claim_type: proposition
statement: 'Consider an extension to stochastic games: in each round $t$, the game
  matrix $M_t$ is drawn independently from some fixed distribution over game matrices.
  Assume all matrices have the same dimensions. Suppose both $\mathtt{ALG}$ and $\mathtt{ADV}$
  are regret-minimizing algorithms, and let $R(T)$ and $R''(T)$ be their respective
  regret. Then the average play $(\bar{\imath}, \bar{\jmath})$ forms a $\delta_T$-approximate
  Nash equilibrium for the expected game matrix $M = \mathbb{E}[M_t]$, with $\delta_T
  = \frac{R(T) + R''(T)}{T} + \mathtt{err}$, where $\mathtt{err} = \left|\sum_{t \in
  [T]} M_t(i_t, j_t) - M(i_t, j_t)\right|$.'
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/game-matrix]]'
- '[[concepts/approximate-nash-equilibrium]]'
- '[[concepts/stochastic-games]]'
- '[[concepts/regret-minimizing-algorithm]]'
about_meta:
- target: '[[concepts/game-matrix]]'
  role: primary
  aspect: ''
- target: '[[concepts/approximate-nash-equilibrium]]'
  role: primary
  aspect: ''
- target: '[[concepts/stochastic-games]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret-minimizing-algorithm]]'
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

# Exercise 9.4

Consider an extension to stochastic games: in each round $t$, the game matrix $M_t$ is drawn independently from some fixed distribution over game matrices. Assume all matrices have the same dimensions. Suppose both $\mathtt{ALG}$ and $\mathtt{ADV}$ are regret-minimizing algorithms, and let $R(T)$ and $R'(T)$ be their respective regret. Then the average play $(\bar{\imath}, \bar{\jmath})$ forms a $\delta_T$-approximate Nash equilibrium for the expected game matrix $M = \mathbb{E}[M_t]$, with $\delta_T = \frac{R(T) + R'(T)}{T} + \mathtt{err}$, where $\mathtt{err} = \left|\sum_{t \in [T]} M_t(i_t, j_t) - M(i_t, j_t)\right|$.
