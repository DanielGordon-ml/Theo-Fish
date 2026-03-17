---
slug: achieving-pareto-optimality-through-distributed-learning--theorem-1
label: Theorem 1
claim_type: theorem
statement: A state is stochastically stable if and only if the action profile is efficient,
  i.e., $\bar{a} \in \arg\max_{a^{*} \in \mathcal{A}} \left\{\sum_{i \in N} U_{i}(a^{*})\right\}$.
proof: 'We first show that the state $D$ is not stochastically stable. Suppose, by
  way of contradiction, that there exists a minimum resistance tree $T$ rooted at
  the state $D$. Then there exists an edge in the tree $T$ of the form $z \to D$ for
  some state $z \in C^{0}$. The resistance of this edge is $c$ and the resistance
  of the opposing edge $D \to z$ (not in the tree $T$) is strictly less than $n$.
  Note that the only way the resistance of this opposing edge $D \to z = [\bar{a},
  \bar{u}]$ could equal $n$ is if $\bar{u}_{i} = 0$ for all $i \in N$. By interdependence,
  this is not possible for all $z \in C^{0}$.


  Create a new tree $T^{\prime}$ rooted at $z$ by removing the edge $z \to D$ from
  $T$ and adding the edge $D \to z$. Therefore $R(T^{\prime}) = R(T) + r(D \to z)
  - r(z \to D) < R(T) + n - c \leq R(T)$. It follows that $T$ is not a minimum resistance
  tree. This contradiction shows that the state $D$ is not stochastically stable.
  It follows that all the stochastically stable states are contained in the set $C^{0}$.


  From Lemma 3, we know that a state $z = [\bar{a}, \bar{u}]$ in $C^{0}$ is stochastically
  stable if and only if $\bar{a} \in \arg\min_{a^{*} \in \mathcal{A}} \left\{c(|C^{0}|
  - 1) + \sum_{i \in N}(1 - U_{i}(a^{*}))\right\}$, equivalently $\bar{a} \in \arg\max_{a^{*}
  \in \mathcal{A}} \left\{\sum_{i \in N} U_{i}(a^{*})\right\}$. Therefore, a state
  is stochastically stable if and only if the action profile is efficient.'
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/welfare-function]]'
- '[[concepts/efficient-joint-action]]'
- '[[concepts/interdependence]]'
- '[[concepts/markov-process]]'
- '[[concepts/stochastic-potential]]'
- '[[concepts/stochastically-stable-states]]'
- '[[concepts/system-welfare-function]]'
- '[[concepts/content-aligned-states]]'
- '[[concepts/n-person-game]]'
- '[[concepts/regular-perturbed-markov-process]]'
- '[[concepts/resistance-tree]]'
- '[[concepts/discontent-states]]'
- '[[concepts/stochastically-stable-state]]'
- '[[concepts/efficient-action-profile]]'
- '[[concepts/stochastic-potential]]'
- '[[concepts/content-aligned-states]]'
- '[[concepts/resistance-tree]]'
- '[[concepts/stochastically-stable-states]]'
- '[[concepts/markov-process]]'
- '[[concepts/system-welfare-function]]'
- '[[concepts/regular-perturbed-markov-process]]'
- '[[concepts/stochastically-stable-state]]'
- '[[concepts/welfare-function]]'
- '[[concepts/efficient-joint-action]]'
- '[[concepts/discontent-states]]'
- '[[concepts/interdependence]]'
- '[[concepts/efficient-action-profile]]'
- '[[concepts/n-person-game]]'
about_meta:
- target: '[[concepts/welfare-function]]'
  role: primary
  aspect: ''
- target: '[[concepts/efficient-joint-action]]'
  role: primary
  aspect: ''
- target: '[[concepts/interdependence]]'
  role: primary
  aspect: ''
- target: '[[concepts/markov-process]]'
  role: primary
  aspect: ''
- target: '[[concepts/stochastic-potential]]'
  role: primary
  aspect: ''
- target: '[[concepts/stochastically-stable-states]]'
  role: primary
  aspect: ''
- target: '[[concepts/system-welfare-function]]'
  role: primary
  aspect: ''
- target: '[[concepts/content-aligned-states]]'
  role: primary
  aspect: ''
- target: '[[concepts/n-person-game]]'
  role: primary
  aspect: ''
- target: '[[concepts/regular-perturbed-markov-process]]'
  role: primary
  aspect: ''
- target: '[[concepts/resistance-tree]]'
  role: primary
  aspect: ''
- target: '[[concepts/discontent-states]]'
  role: primary
  aspect: ''
- target: '[[concepts/stochastically-stable-state]]'
  role: primary
  aspect: ''
- target: '[[concepts/efficient-action-profile]]'
  role: primary
  aspect: ''
- target: '[[concepts/stochastic-potential]]'
  role: primary
  aspect: ''
- target: '[[concepts/content-aligned-states]]'
  role: primary
  aspect: ''
- target: '[[concepts/resistance-tree]]'
  role: primary
  aspect: ''
- target: '[[concepts/stochastically-stable-states]]'
  role: primary
  aspect: ''
- target: '[[concepts/markov-process]]'
  role: primary
  aspect: ''
- target: '[[concepts/system-welfare-function]]'
  role: primary
  aspect: ''
- target: '[[concepts/regular-perturbed-markov-process]]'
  role: primary
  aspect: ''
- target: '[[concepts/stochastically-stable-state]]'
  role: primary
  aspect: ''
- target: '[[concepts/welfare-function]]'
  role: primary
  aspect: ''
- target: '[[concepts/efficient-joint-action]]'
  role: primary
  aspect: ''
- target: '[[concepts/discontent-states]]'
  role: primary
  aspect: ''
- target: '[[concepts/interdependence]]'
  role: primary
  aspect: ''
- target: '[[concepts/efficient-action-profile]]'
  role: primary
  aspect: ''
- target: '[[concepts/n-person-game]]'
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

# Theorem 1

A state is stochastically stable if and only if the action profile is efficient, i.e., $\bar{a} \in \arg\max_{a^{*} \in \mathcal{A}} \left\{\sum_{i \in N} U_{i}(a^{*})\right\}$.


## Proof

We first show that the state $D$ is not stochastically stable. Suppose, by way of contradiction, that there exists a minimum resistance tree $T$ rooted at the state $D$. Then there exists an edge in the tree $T$ of the form $z \to D$ for some state $z \in C^{0}$. The resistance of this edge is $c$ and the resistance of the opposing edge $D \to z$ (not in the tree $T$) is strictly less than $n$. Note that the only way the resistance of this opposing edge $D \to z = [\bar{a}, \bar{u}]$ could equal $n$ is if $\bar{u}_{i} = 0$ for all $i \in N$. By interdependence, this is not possible for all $z \in C^{0}$.

Create a new tree $T^{\prime}$ rooted at $z$ by removing the edge $z \to D$ from $T$ and adding the edge $D \to z$. Therefore $R(T^{\prime}) = R(T) + r(D \to z) - r(z \to D) < R(T) + n - c \leq R(T)$. It follows that $T$ is not a minimum resistance tree. This contradiction shows that the state $D$ is not stochastically stable. It follows that all the stochastically stable states are contained in the set $C^{0}$.

From Lemma 3, we know that a state $z = [\bar{a}, \bar{u}]$ in $C^{0}$ is stochastically stable if and only if $\bar{a} \in \arg\min_{a^{*} \in \mathcal{A}} \left\{c(|C^{0}| - 1) + \sum_{i \in N}(1 - U_{i}(a^{*}))\right\}$, equivalently $\bar{a} \in \arg\max_{a^{*} \in \mathcal{A}} \left\{\sum_{i \in N} U_{i}(a^{*})\right\}$. Therefore, a state is stochastically stable if and only if the action profile is efficient.
