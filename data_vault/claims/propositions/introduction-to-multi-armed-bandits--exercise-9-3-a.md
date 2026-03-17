---
slug: introduction-to-multi-armed-bandits--exercise-9-3-a
label: Exercise 9.3(a)
claim_type: proposition
statement: Suppose both $\mathtt{ALG}$ and $\mathtt{ADV}$ are implemented by algorithm
  $\mathtt{Hedge}$ with parameter $\epsilon = \sqrt{(\ln K)/(2T)}$ in the full-feedback
  model. Assume that $M$ is a $K \times K$ matrix with entries in $[0,1]$. Then the
  average play $(\bar{\imath}, \bar{\jmath})$ forms a $\delta_T$-approximate Nash
  equilibrium with probability at least $1 - T^{-2}$, where $\delta_T = O\left(\sqrt{\frac{\ln(KT)}{T}}\right)$.
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/full-feedback]]'
- '[[concepts/game-matrix]]'
- '[[concepts/approximate-nash-equilibrium]]'
- '[[concepts/hedge]]'
about_meta:
- target: '[[concepts/full-feedback]]'
  role: primary
  aspect: ''
- target: '[[concepts/game-matrix]]'
  role: primary
  aspect: ''
- target: '[[concepts/approximate-nash-equilibrium]]'
  role: primary
  aspect: ''
- target: '[[concepts/hedge]]'
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

# Exercise 9.3(a)

Suppose both $\mathtt{ALG}$ and $\mathtt{ADV}$ are implemented by algorithm $\mathtt{Hedge}$ with parameter $\epsilon = \sqrt{(\ln K)/(2T)}$ in the full-feedback model. Assume that $M$ is a $K \times K$ matrix with entries in $[0,1]$. Then the average play $(\bar{\imath}, \bar{\jmath})$ forms a $\delta_T$-approximate Nash equilibrium with probability at least $1 - T^{-2}$, where $\delta_T = O\left(\sqrt{\frac{\ln(KT)}{T}}\right)$.
