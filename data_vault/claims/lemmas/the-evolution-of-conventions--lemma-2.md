---
slug: the-evolution-of-conventions--lemma-2
label: Lemma 2
claim_type: lemma
statement: $\gamma(x) = \gamma_j$ for all states $x \in X_j$.
proof: 'Fix one state $x_j$ in each recurrent class $X_j$. We shall show first that
  $\gamma(x_j) \leq \gamma_j$; then we shall show the reverse inequality.


  Fix a class $X_j$ and a $j$-tree $\tau$ in $\mathcal{I}$ whose resistance $r(\tau)$
  equals $\gamma_j$. For every $i \neq j$, there exists exactly one outgoing edge
  $(i, i'') \in \tau$. In the graph $G$ choose a directed path $D_{ii''}$ from $x_i$
  to $x_{i''}$ having resistance $r_{ii''}$. Now choose a directed subtree $T_i$ that
  spans the vertex set $X_i$ such that from every vertex in $X_i$ there is a unique
  directed path to $x_i$. Since $X_i$ is a communication class of $P^0$, $T_i$ can
  be chosen so that it has zero resistance. Let $E$ be the union of all of the edges
  in the trees $T_i$ and all of the edges in the directed paths $D_{ii''}$ where $(i,
  i'') \in \tau$. By construction, $E$ contains at least one directed path from every
  vertex in $X$ to the fixed vertex $x_j$. Therefore it contains a subset of edges
  that form an $x_j$-tree $T$ in $G$. The resistance of $T$ is clearly less than or
  equal to the sum of the resistances of the paths $D_{ii''}$, so it is less than
  or equal to $r(\tau)$. Thus $\gamma(x_j) \leq \gamma_j = r(\tau)$ as claimed.


  To show that $\gamma(x_j) \geq \gamma_j$, fix a class $j$ and a least-resistant
  $x_j$-tree $T$ among all $x_j$-trees on the vertex set $X$. Label each of the specially
  chosen vertices $x_i$ by the class $i$ to which it belongs. These will be called
  special vertices. A junction in $T$ is any vertex $y$ with at least two incoming
  $T$-edges. If the junction $y$ is not a special vertex, label it $i$ if there exists
  a path of zero resistance from $y$ to $X_i$. Every labelled vertex is either a special
  vertex or a junction (or both), and the label identifies a class to which there
  is a path of zero resistance.


  Define the special predecessors of a state $x \in X$ to be the special vertices
  $x_i$ that strictly precede $x$ in the fixed tree $T$ and such that there is no
  other special vertex $x_j$ on the path from $x_i$ to $x$.


  Property (15): If $x_i$ is a special predecessor of $x$, the path from $x_i$ to
  $x$ has resistance at least $r_{ik}$, where $k$ is the label of $x$. This clearly
  holds for the tree $T$ because any path from the special vertex $x_i$ to a vertex
  labelled $k$ can be extended by a zero resistance path to the class $X_k$, and the
  total path must have resistance at least $r_{ik}$.


  We perform operations on the tree $T$ that preserve property (15), eliminating all
  junctions that are not special vertices. Suppose that $T$ contains a junction $y$
  that is not a special vertex, and let its label be $k$.


  Case 1: If $x_k$ is not a predecessor of $y$ in the tree, cut off the subtree consisting
  of all edges and vertices that precede $y$ and glue them onto the tree at the vertex
  $x_k$.


  Case 2: If $x_k$ is a predecessor of $y$, cut off the subtree consisting of all
  edges and vertices that precede $y$ (except for the path from $x_k$ to $y$ and all
  of its predecessors) and glue them onto $x_k$.


  Both of these operations preserve property (15) because $x_k$ and $y$ have the same
  label. Each operation reduces by one the number of junctions that are not special
  vertices. Thus we eventually obtain an $x_j$-tree $T^*$ in which every junction
  is a special vertex, property (15) is satisfied, and $T^*$ has the same resistance
  as the original tree $T$.


  Now construct a $j$-tree $\tau$ on the vertex set $J$ as follows. For every two
  classes $i$ and $i''$ put the directed edge $(i, i'')$ in $\tau$ if and only if
  $x_i$ is a special predecessor of $x_{i''}$ in $T^*$. By construction, $\tau$ forms
  a $j$-tree. Let $D_{ii''}^*$ be the unique path in $T^*$ from $x_i$ to $x_{i''}$.
  By property (15) its resistance is at least $r_{ii''}$. The paths $D_{ii''}^*$ are
  edge-disjoint because every junction is one of the special vertices. Since $T^*$
  has resistance at least $\sum_{(i,i'') \in \tau} r_{ii''}$. But $\sum_{(i,i'') \in
  \tau} r_{ii''}$ is the resistance of $\tau$. Hence $\gamma(x_j) = r(T^*) \geq \sum_{(i,i'')
  \in \tau} r_{ii''} = r(\tau) \geq \gamma_j$ as claimed.'
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/j-tree]]'
- '[[concepts/shortest-arborescence]]'
- '[[concepts/perturbed-adaptive-play-process]]'
- '[[concepts/least-resistance-path]]'
- '[[concepts/number-of-mistakes]]'
- '[[concepts/convention]]'
- '[[concepts/resistance]]'
- '[[concepts/edge-resistance-between-recurrence-classes]]'
- '[[concepts/z-tree]]'
- '[[concepts/stochastic-potential]]'
- '[[concepts/recurrent-communication-class-x-j]]'
- '[[concepts/resistance-graph]]'
- '[[concepts/stochastic-potential]]'
- '[[concepts/recurrent-communication-class-x-j]]'
- '[[concepts/shortest-arborescence]]'
- '[[concepts/z-tree]]'
- '[[concepts/convention]]'
- '[[concepts/number-of-mistakes]]'
- '[[concepts/perturbed-adaptive-play-process]]'
- '[[concepts/resistance-graph]]'
- '[[concepts/resistance]]'
- '[[concepts/edge-resistance-between-recurrence-classes]]'
- '[[concepts/j-tree]]'
- '[[concepts/least-resistance-path]]'
about_meta:
- target: '[[concepts/j-tree]]'
  role: primary
  aspect: ''
- target: '[[concepts/shortest-arborescence]]'
  role: primary
  aspect: ''
- target: '[[concepts/perturbed-adaptive-play-process]]'
  role: primary
  aspect: ''
- target: '[[concepts/least-resistance-path]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-mistakes]]'
  role: primary
  aspect: ''
- target: '[[concepts/convention]]'
  role: primary
  aspect: ''
- target: '[[concepts/resistance]]'
  role: primary
  aspect: ''
- target: '[[concepts/edge-resistance-between-recurrence-classes]]'
  role: primary
  aspect: ''
- target: '[[concepts/z-tree]]'
  role: primary
  aspect: ''
- target: '[[concepts/stochastic-potential]]'
  role: primary
  aspect: ''
- target: '[[concepts/recurrent-communication-class-x-j]]'
  role: primary
  aspect: ''
- target: '[[concepts/resistance-graph]]'
  role: primary
  aspect: ''
- target: '[[concepts/stochastic-potential]]'
  role: primary
  aspect: ''
- target: '[[concepts/recurrent-communication-class-x-j]]'
  role: primary
  aspect: ''
- target: '[[concepts/shortest-arborescence]]'
  role: primary
  aspect: ''
- target: '[[concepts/z-tree]]'
  role: primary
  aspect: ''
- target: '[[concepts/convention]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-mistakes]]'
  role: primary
  aspect: ''
- target: '[[concepts/perturbed-adaptive-play-process]]'
  role: primary
  aspect: ''
- target: '[[concepts/resistance-graph]]'
  role: primary
  aspect: ''
- target: '[[concepts/resistance]]'
  role: primary
  aspect: ''
- target: '[[concepts/edge-resistance-between-recurrence-classes]]'
  role: primary
  aspect: ''
- target: '[[concepts/j-tree]]'
  role: primary
  aspect: ''
- target: '[[concepts/least-resistance-path]]'
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

# Lemma 2

$\gamma(x) = \gamma_j$ for all states $x \in X_j$.


## Proof

Fix one state $x_j$ in each recurrent class $X_j$. We shall show first that $\gamma(x_j) \leq \gamma_j$; then we shall show the reverse inequality.

Fix a class $X_j$ and a $j$-tree $\tau$ in $\mathcal{I}$ whose resistance $r(\tau)$ equals $\gamma_j$. For every $i \neq j$, there exists exactly one outgoing edge $(i, i') \in \tau$. In the graph $G$ choose a directed path $D_{ii'}$ from $x_i$ to $x_{i'}$ having resistance $r_{ii'}$. Now choose a directed subtree $T_i$ that spans the vertex set $X_i$ such that from every vertex in $X_i$ there is a unique directed path to $x_i$. Since $X_i$ is a communication class of $P^0$, $T_i$ can be chosen so that it has zero resistance. Let $E$ be the union of all of the edges in the trees $T_i$ and all of the edges in the directed paths $D_{ii'}$ where $(i, i') \in \tau$. By construction, $E$ contains at least one directed path from every vertex in $X$ to the fixed vertex $x_j$. Therefore it contains a subset of edges that form an $x_j$-tree $T$ in $G$. The resistance of $T$ is clearly less than or equal to the sum of the resistances of the paths $D_{ii'}$, so it is less than or equal to $r(\tau)$. Thus $\gamma(x_j) \leq \gamma_j = r(\tau)$ as claimed.

To show that $\gamma(x_j) \geq \gamma_j$, fix a class $j$ and a least-resistant $x_j$-tree $T$ among all $x_j$-trees on the vertex set $X$. Label each of the specially chosen vertices $x_i$ by the class $i$ to which it belongs. These will be called special vertices. A junction in $T$ is any vertex $y$ with at least two incoming $T$-edges. If the junction $y$ is not a special vertex, label it $i$ if there exists a path of zero resistance from $y$ to $X_i$. Every labelled vertex is either a special vertex or a junction (or both), and the label identifies a class to which there is a path of zero resistance.

Define the special predecessors of a state $x \in X$ to be the special vertices $x_i$ that strictly precede $x$ in the fixed tree $T$ and such that there is no other special vertex $x_j$ on the path from $x_i$ to $x$.

Property (15): If $x_i$ is a special predecessor of $x$, the path from $x_i$ to $x$ has resistance at least $r_{ik}$, where $k$ is the label of $x$. This clearly holds for the tree $T$ because any path from the special vertex $x_i$ to a vertex labelled $k$ can be extended by a zero resistance path to the class $X_k$, and the total path must have resistance at least $r_{ik}$.

We perform operations on the tree $T$ that preserve property (15), eliminating all junctions that are not special vertices. Suppose that $T$ contains a junction $y$ that is not a special vertex, and let its label be $k$.

Case 1: If $x_k$ is not a predecessor of $y$ in the tree, cut off the subtree consisting of all edges and vertices that precede $y$ and glue them onto the tree at the vertex $x_k$.

Case 2: If $x_k$ is a predecessor of $y$, cut off the subtree consisting of all edges and vertices that precede $y$ (except for the path from $x_k$ to $y$ and all of its predecessors) and glue them onto $x_k$.

Both of these operations preserve property (15) because $x_k$ and $y$ have the same label. Each operation reduces by one the number of junctions that are not special vertices. Thus we eventually obtain an $x_j$-tree $T^*$ in which every junction is a special vertex, property (15) is satisfied, and $T^*$ has the same resistance as the original tree $T$.

Now construct a $j$-tree $\tau$ on the vertex set $J$ as follows. For every two classes $i$ and $i'$ put the directed edge $(i, i')$ in $\tau$ if and only if $x_i$ is a special predecessor of $x_{i'}$ in $T^*$. By construction, $\tau$ forms a $j$-tree. Let $D_{ii'}^*$ be the unique path in $T^*$ from $x_i$ to $x_{i'}$. By property (15) its resistance is at least $r_{ii'}$. The paths $D_{ii'}^*$ are edge-disjoint because every junction is one of the special vertices. Since $T^*$ has resistance at least $\sum_{(i,i') \in \tau} r_{ii'}$. But $\sum_{(i,i') \in \tau} r_{ii'}$ is the resistance of $\tau$. Hence $\gamma(x_j) = r(T^*) \geq \sum_{(i,i') \in \tau} r_{ii'} = r(\tau) \geq \gamma_j$ as claimed.
