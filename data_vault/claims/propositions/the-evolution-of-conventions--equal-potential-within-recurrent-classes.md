---
slug: the-evolution-of-conventions--equal-potential-within-recurrent-classes
label: Equal potential within recurrent classes
claim_type: proposition
statement: All states in the same recurrent communication class have the same potential.
  That is, if $x, y \in X_j$, then $\gamma(x) = \gamma(y)$.
proof: Suppose that $x$ is in $X_j$ and $T$ is an $x$-tree in $G$ with potential $\gamma(x)$.
  Let $y$ be some other vertex in $X_j$. Choose a path of zero resistance from $x$
  to $y$. The union of this path and $T$ contains a $y$-tree $T'$ that has the same
  resistance as $T$. From this it follows that the potential of $y$ is no larger than
  the potential of $x$, and a symmetric argument shows that it is no smaller. Hence
  they have the same potential.
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/resistance-r-x-y]]'
- '[[concepts/stochastic-potential]]'
- '[[concepts/recurrent-communication-class-x-j]]'
- '[[concepts/z-tree]]'
about_meta:
- target: '[[concepts/resistance-r-x-y]]'
  role: primary
  aspect: ''
- target: '[[concepts/stochastic-potential]]'
  role: primary
  aspect: ''
- target: '[[concepts/recurrent-communication-class-x-j]]'
  role: primary
  aspect: ''
- target: '[[concepts/z-tree]]'
  role: primary
  aspect: ''
depends_on: []
depends_on_meta: []
sourced_from:
- '[[sources/the_evolution_of_conventions|the_evolution_of_conventions]]'
sourced_from_meta:
- target: '[[sources/the_evolution_of_conventions|the_evolution_of_conventions]]'
  section: ''
  page: ''
  confidence: 0.0
---

# Equal potential within recurrent classes

All states in the same recurrent communication class have the same potential. That is, if $x, y \in X_j$, then $\gamma(x) = \gamma(y)$.


## Proof

Suppose that $x$ is in $X_j$ and $T$ is an $x$-tree in $G$ with potential $\gamma(x)$. Let $y$ be some other vertex in $X_j$. Choose a path of zero resistance from $x$ to $y$. The union of this path and $T$ contains a $y$-tree $T'$ that has the same resistance as $T$. From this it follows that the potential of $y$ is no larger than the potential of $x$, and a symmetric argument shows that it is no smaller. Hence they have the same potential.
