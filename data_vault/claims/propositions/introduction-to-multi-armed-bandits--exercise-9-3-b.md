---
slug: introduction-to-multi-armed-bandits--exercise-9-3-b
label: Exercise 9.3(b)
claim_type: proposition
statement: 'Suppose both $\mathtt{ALG}$ and $\mathtt{ADV}$ are implemented by algorithm
  $\mathtt{Hedge}$ with parameter $\epsilon = \sqrt{(\ln K)/(2T)}$. Consider a modified
  feedback model: in each round $t$, $\mathtt{ALG}$ is given costs $M(\cdot, q_t)$,
  and $\mathtt{ADV}$ is given rewards $M(p_t, \cdot)$, where $p_t \in \Delta_{\mathtt{rows}}$
  and $q_t \in \Delta_{\mathtt{cols}}$ are the distributions chosen by $\mathtt{ALG}$
  and $\mathtt{ADV}$, respectively. Assume that $M$ is a $K \times K$ matrix with
  entries in $[0,1]$. Then the average play $(\bar{\imath}, \bar{\jmath})$ forms a
  $\delta_T$-approximate Nash equilibrium where $\delta_T = O\left(\sqrt{\frac{\ln(KT)}{T}}\right)$.'
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/feedback-model]]'
- '[[concepts/approximate-nash-equilibrium]]'
- '[[concepts/hedge]]'
about_meta:
- target: '[[concepts/feedback-model]]'
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

# Exercise 9.3(b)

Suppose both $\mathtt{ALG}$ and $\mathtt{ADV}$ are implemented by algorithm $\mathtt{Hedge}$ with parameter $\epsilon = \sqrt{(\ln K)/(2T)}$. Consider a modified feedback model: in each round $t$, $\mathtt{ALG}$ is given costs $M(\cdot, q_t)$, and $\mathtt{ADV}$ is given rewards $M(p_t, \cdot)$, where $p_t \in \Delta_{\mathtt{rows}}$ and $q_t \in \Delta_{\mathtt{cols}}$ are the distributions chosen by $\mathtt{ALG}$ and $\mathtt{ADV}$, respectively. Assume that $M$ is a $K \times K$ matrix with entries in $[0,1]$. Then the average play $(\bar{\imath}, \bar{\jmath})$ forms a $\delta_T$-approximate Nash equilibrium where $\delta_T = O\left(\sqrt{\frac{\ln(KT)}{T}}\right)$.
