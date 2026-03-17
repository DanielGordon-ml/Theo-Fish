---
slug: achieving-pareto-optimality-through-distributed-learning--lemma-3
label: Lemma 3
claim_type: lemma
statement: The stochastic potential of any state $z = [\bar{a}, \bar{u}]$ in $C^{0}$
  is $\gamma(z) = c\left(\left|C^{0}\right| - 1\right) + \sum_{i \in N}\left(1 - \bar{u}_{i}\right).$
proof: 'We first prove that (6) is an upper bound for the stochastic potential of
  $z$ by constructing a tree rooted at $z$ with the prescribed resistance. To that
  end, consider the tree $T$ with the following properties:


  P-1: The edge exiting each state $z^{\prime} \in C^{0} \setminus \{z\}$ is of the
  form $z^{\prime} \to D$. The total resistance associated with these edges is $c(|C^{0}|
  - 1)$.


  P-2: The edge exiting the state $D$ is of the form $D \to z$. The resistance associated
  with this edge is $\sum_{i \in N}(1 - \bar{u}_{i})$.


  The tree $T$ is rooted at $z$ and has total resistance $c(|C^{0}| - 1) + \sum_{i
  \in N}(1 - \bar{u}_{i})$. It follows that $\gamma(z) \leq c(|C^{0}| - 1) + \sum_{i
  \in N}(1 - \bar{u}_{i})$, hence (6) holds as an inequality. It remains to be shown
  that the right-hand side of (6) is also a lower bound for the stochastic potential.


  We argue this by contradiction. Suppose there exists a tree $T$ rooted at $z$ with
  resistance $R(T) < c(|C^{0}| - 1) + \sum_{i \in N}(1 - \bar{u}_{i})$. Since the
  tree $T$ is rooted at $z$ we know that there exists a path $\mathcal{P}$ from $D$
  to $z$ of the form $\mathcal{P} = \{D \to z^{1} \to z^{2} \to \ldots \to z^{m} \to
  z\}$, where $z^{k} \in C^{0}$ for each $k \in \{1, ..., m\}$. We claim that the
  resistance associated with this path of $m + 1$ transitions satisfies $R(\mathcal{P})
  \geq mc + \sum_{i \in N}(1 - \bar{u}_{i})$. The term $mc$ comes from applying observation
  (iii) to the last $m$ transitions on the path $\mathcal{P}$. The term $\sum_{i \in
  N}(1 - \bar{u}_{i})$ comes from the fact that each agent needs to accept $\bar{u}_{i}$
  as the benchmark payoff at some point during the transitions.


  Construct a new tree $T^{\prime}$ still rooted at $z$ by removing the edges in $\mathcal{P}$
  and adding the following edges: $D \to z$ which has resistance $\sum_{i \in N}(1
  - \bar{u}_{i})$; $z^{k} \to D$ for each $k \in \{1, ..., m\}$ which has total resistance
  $mc$. The new tree $T^{\prime}$ is still rooted at $z$ and has a total resistance
  that satisfies $R(T^{\prime}) \leq R(T)$.


  Now suppose that there exists an edge $z^{\prime} \to z^{\prime\prime}$ in the tree
  $T^{\prime}$ for some states $z^{\prime}, z^{\prime\prime} \in C^{0}$. By observation
  (iii), the resistance of this edge satisfies $r(z^{\prime} \to z^{\prime\prime})
  \geq c$. Construct a new tree $T^{\prime\prime}$ by removing the edge $z^{\prime}
  \to z^{\prime\prime}$ and adding the edge $z^{\prime} \to D$, which has a resistance
  $c$. This new tree $T^{\prime\prime}$ is rooted at $z$, and its resistance satisfies
  $R(T^{\prime\prime}) = R(T^{\prime}) + r(z^{\prime} \to D) - r(z^{\prime} \to z^{\prime\prime})
  \leq R(T^{\prime}) \leq R(T)$. Repeat this process until we have constructed a tree
  $T^{*}$ for which no such edges exist. Note that the tree $T^{*}$ satisfies properties
  P-1 and P-2 and consequently has a total resistance $R(T^{*}) = c(|C^{0}| - 1) +
  \sum_{i \in N}(1 - \bar{u}_{i})$. Since by construction $R(T^{*}) \leq R(T)$ we
  have a contradiction. This completes the proof of Lemma 3.'
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/content-aligned-states]]'
- '[[concepts/stochastic-potential]]'
- '[[concepts/number-of-agents]]'
- '[[concepts/edge-resistance-between-recurrence-classes]]'
- '[[concepts/resistance-tree]]'
- '[[concepts/experimentation-cost]]'
- '[[concepts/j-tree]]'
about_meta:
- target: '[[concepts/content-aligned-states]]'
  role: primary
  aspect: ''
- target: '[[concepts/stochastic-potential]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-agents]]'
  role: primary
  aspect: ''
- target: '[[concepts/edge-resistance-between-recurrence-classes]]'
  role: primary
  aspect: ''
- target: '[[concepts/resistance-tree]]'
  role: primary
  aspect: ''
- target: '[[concepts/experimentation-cost]]'
  role: primary
  aspect: ''
- target: '[[concepts/j-tree]]'
  role: primary
  aspect: ''
depends_on: []
depends_on_meta: []
sourced_from:
- '[[sources/achieving_pareto_optimality_through_distributed_learning|achieving_pareto_optimality_through_distributed_learning]]'
sourced_from_meta:
- target: '[[sources/achieving_pareto_optimality_through_distributed_learning|achieving_pareto_optimality_through_distributed_learning]]'
  section: ''
  page: ''
  confidence: 0.0
---

# Lemma 3

The stochastic potential of any state $z = [\bar{a}, \bar{u}]$ in $C^{0}$ is $\gamma(z) = c\left(\left|C^{0}\right| - 1\right) + \sum_{i \in N}\left(1 - \bar{u}_{i}\right).$


## Proof

We first prove that (6) is an upper bound for the stochastic potential of $z$ by constructing a tree rooted at $z$ with the prescribed resistance. To that end, consider the tree $T$ with the following properties:

P-1: The edge exiting each state $z^{\prime} \in C^{0} \setminus \{z\}$ is of the form $z^{\prime} \to D$. The total resistance associated with these edges is $c(|C^{0}| - 1)$.

P-2: The edge exiting the state $D$ is of the form $D \to z$. The resistance associated with this edge is $\sum_{i \in N}(1 - \bar{u}_{i})$.

The tree $T$ is rooted at $z$ and has total resistance $c(|C^{0}| - 1) + \sum_{i \in N}(1 - \bar{u}_{i})$. It follows that $\gamma(z) \leq c(|C^{0}| - 1) + \sum_{i \in N}(1 - \bar{u}_{i})$, hence (6) holds as an inequality. It remains to be shown that the right-hand side of (6) is also a lower bound for the stochastic potential.

We argue this by contradiction. Suppose there exists a tree $T$ rooted at $z$ with resistance $R(T) < c(|C^{0}| - 1) + \sum_{i \in N}(1 - \bar{u}_{i})$. Since the tree $T$ is rooted at $z$ we know that there exists a path $\mathcal{P}$ from $D$ to $z$ of the form $\mathcal{P} = \{D \to z^{1} \to z^{2} \to \ldots \to z^{m} \to z\}$, where $z^{k} \in C^{0}$ for each $k \in \{1, ..., m\}$. We claim that the resistance associated with this path of $m + 1$ transitions satisfies $R(\mathcal{P}) \geq mc + \sum_{i \in N}(1 - \bar{u}_{i})$. The term $mc$ comes from applying observation (iii) to the last $m$ transitions on the path $\mathcal{P}$. The term $\sum_{i \in N}(1 - \bar{u}_{i})$ comes from the fact that each agent needs to accept $\bar{u}_{i}$ as the benchmark payoff at some point during the transitions.

Construct a new tree $T^{\prime}$ still rooted at $z$ by removing the edges in $\mathcal{P}$ and adding the following edges: $D \to z$ which has resistance $\sum_{i \in N}(1 - \bar{u}_{i})$; $z^{k} \to D$ for each $k \in \{1, ..., m\}$ which has total resistance $mc$. The new tree $T^{\prime}$ is still rooted at $z$ and has a total resistance that satisfies $R(T^{\prime}) \leq R(T)$.

Now suppose that there exists an edge $z^{\prime} \to z^{\prime\prime}$ in the tree $T^{\prime}$ for some states $z^{\prime}, z^{\prime\prime} \in C^{0}$. By observation (iii), the resistance of this edge satisfies $r(z^{\prime} \to z^{\prime\prime}) \geq c$. Construct a new tree $T^{\prime\prime}$ by removing the edge $z^{\prime} \to z^{\prime\prime}$ and adding the edge $z^{\prime} \to D$, which has a resistance $c$. This new tree $T^{\prime\prime}$ is rooted at $z$, and its resistance satisfies $R(T^{\prime\prime}) = R(T^{\prime}) + r(z^{\prime} \to D) - r(z^{\prime} \to z^{\prime\prime}) \leq R(T^{\prime}) \leq R(T)$. Repeat this process until we have constructed a tree $T^{*}$ for which no such edges exist. Note that the tree $T^{*}$ satisfies properties P-1 and P-2 and consequently has a total resistance $R(T^{*}) = c(|C^{0}| - 1) + \sum_{i \in N}(1 - \bar{u}_{i})$. Since by construction $R(T^{*}) \leq R(T)$ we have a contradiction. This completes the proof of Lemma 3.
