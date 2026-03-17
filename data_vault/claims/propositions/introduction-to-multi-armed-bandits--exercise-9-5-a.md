---
slug: introduction-to-multi-armed-bandits--exercise-9-5-a
label: Exercise 9.5(a)
claim_type: proposition
statement: Consider an extension of the repeated game to infinite action sets. $\mathtt{ALG}$
  and $\mathtt{ADV}$ have action sets $I$, $J$, resp., and the game matrix $M$ is
  a function $I \times J \to [0,1]$. Assume there exists a function $\tilde{R}(T)
  = o(T)$ such that expected regret of $\mathtt{ALG}$ is at most $\tilde{R}(T)$ for
  any $\mathtt{ADV}$, and likewise expected regret of $\mathtt{ADV}$ is at most $\tilde{R}(T)$
  for any $\mathtt{ALG}$. Then $\inf_{p \in \Delta_{\mathtt{rows}}} \sup_{j \in J}
  \int M(p,j) \, \mathrm{d}p = \sup_{q \in \Delta_{\mathtt{cols}}} \inf_{i \in I}
  \int M(i,q) \, \mathrm{d}q$, where $\Delta_{\mathtt{rows}}$ and $\Delta_{\mathtt{cols}}$
  are the sets of all probability measures on $I$ and $J$.
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/minimax-value]]'
- '[[concepts/game-matrix]]'
- '[[concepts/d-rows]]'
- '[[concepts/infinite-action-sets]]'
- '[[concepts/d-cols]]'
about_meta:
- target: '[[concepts/minimax-value]]'
  role: primary
  aspect: ''
- target: '[[concepts/game-matrix]]'
  role: primary
  aspect: ''
- target: '[[concepts/d-rows]]'
  role: primary
  aspect: ''
- target: '[[concepts/infinite-action-sets]]'
  role: primary
  aspect: ''
- target: '[[concepts/d-cols]]'
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

# Exercise 9.5(a)

Consider an extension of the repeated game to infinite action sets. $\mathtt{ALG}$ and $\mathtt{ADV}$ have action sets $I$, $J$, resp., and the game matrix $M$ is a function $I \times J \to [0,1]$. Assume there exists a function $\tilde{R}(T) = o(T)$ such that expected regret of $\mathtt{ALG}$ is at most $\tilde{R}(T)$ for any $\mathtt{ADV}$, and likewise expected regret of $\mathtt{ADV}$ is at most $\tilde{R}(T)$ for any $\mathtt{ALG}$. Then $\inf_{p \in \Delta_{\mathtt{rows}}} \sup_{j \in J} \int M(p,j) \, \mathrm{d}p = \sup_{q \in \Delta_{\mathtt{cols}}} \inf_{i \in I} \int M(i,q) \, \mathrm{d}q$, where $\Delta_{\mathtt{rows}}$ and $\Delta_{\mathtt{cols}}$ are the sets of all probability measures on $I$ and $J$.
