---
slug: achieving-pareto-optimality-through-distributed-learning--theorem-1-proof-via-lemma-3
label: Theorem 1 (Proof via Lemma 3)
claim_type: theorem
statement: The stochastically stable states of the proposed learning algorithm are
  precisely those states whose action profiles are efficient, i.e., maximize the sum
  of agent utilities ∑_{i ∈ N} U_i(a*).
proof: 'We first show that the state D is not stochastically stable. Suppose, by way
  of contradiction, that there exists a minimum resistance tree T rooted at the state
  D. Then there exists an edge in the tree T of the form z → D for some state z ∈
  C⁰. The resistance of this edge is c and the resistance of the opposing edge D →
  z (not in the tree T) is strictly less than n. Note that the only way the resistance
  of this opposing edge D → z = [ā, ū] could equal n is if ū_i = 0 for all i ∈ N.
  By interdependence, this is not possible for all z ∈ C⁰.


  Create a new tree T'' rooted at z by removing the edge z → D from T and adding the
  edge D → z. Therefore


  R(T'') = R(T) + r(D → z) - r(z → D) < R(T) + n - c ≤ R(T).


  It follows that T is not a minimum resistance tree. This contradiction shows that
  the state D is not stochastically stable. It follows that all the stochastically
  stable states are contained in the set C⁰.


  From Lemma 3, we know that a state z = [ā, ū] in C⁰ is stochastically stable if
  and only if


  ā ∈ arg min_{a* ∈ A} { c(|C⁰| - 1) + ∑_{i ∈ N} (1 - U_i(a*)) },


  equivalently


  ā ∈ arg max_{a* ∈ A} { ∑_{i ∈ N} U_i(a*) }.


  Therefore, a state is stochastically stable if and only if the action profile is
  efficient. □'
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/stochastically-stable-states]]'
- '[[concepts/interdependence]]'
- '[[concepts/efficient-joint-action]]'
- '[[concepts/welfare-function]]'
- '[[concepts/resistance-tree]]'
- '[[concepts/discontent-state]]'
- '[[concepts/stochastic-potential]]'
- '[[concepts/content-aligned-states]]'
about_meta:
- target: '[[concepts/stochastically-stable-states]]'
  role: primary
  aspect: ''
- target: '[[concepts/interdependence]]'
  role: primary
  aspect: ''
- target: '[[concepts/efficient-joint-action]]'
  role: primary
  aspect: ''
- target: '[[concepts/welfare-function]]'
  role: primary
  aspect: ''
- target: '[[concepts/resistance-tree]]'
  role: primary
  aspect: ''
- target: '[[concepts/discontent-state]]'
  role: primary
  aspect: ''
- target: '[[concepts/stochastic-potential]]'
  role: primary
  aspect: ''
- target: '[[concepts/content-aligned-states]]'
  role: primary
  aspect: ''
depends_on:
- '[[claims/achieving-pareto-optimality-through-distributed-learning--lemma-3]]'
depends_on_meta:
- target: '[[claims/achieving-pareto-optimality-through-distributed-learning--lemma-3]]'
sourced_from:
- '[[sources/achieving_pareto_optimality_through_distributed_learning|achieving_pareto_optimality_through_distributed_learning]]'
sourced_from_meta:
- target: '[[sources/achieving_pareto_optimality_through_distributed_learning|achieving_pareto_optimality_through_distributed_learning]]'
  section: ''
  page: ''
  confidence: 0.0
---

# Theorem 1 (Proof via Lemma 3)

The stochastically stable states of the proposed learning algorithm are precisely those states whose action profiles are efficient, i.e., maximize the sum of agent utilities ∑_{i ∈ N} U_i(a*).


## Proof

We first show that the state D is not stochastically stable. Suppose, by way of contradiction, that there exists a minimum resistance tree T rooted at the state D. Then there exists an edge in the tree T of the form z → D for some state z ∈ C⁰. The resistance of this edge is c and the resistance of the opposing edge D → z (not in the tree T) is strictly less than n. Note that the only way the resistance of this opposing edge D → z = [ā, ū] could equal n is if ū_i = 0 for all i ∈ N. By interdependence, this is not possible for all z ∈ C⁰.

Create a new tree T' rooted at z by removing the edge z → D from T and adding the edge D → z. Therefore

R(T') = R(T) + r(D → z) - r(z → D) < R(T) + n - c ≤ R(T).

It follows that T is not a minimum resistance tree. This contradiction shows that the state D is not stochastically stable. It follows that all the stochastically stable states are contained in the set C⁰.

From Lemma 3, we know that a state z = [ā, ū] in C⁰ is stochastically stable if and only if

ā ∈ arg min_{a* ∈ A} { c(|C⁰| - 1) + ∑_{i ∈ N} (1 - U_i(a*)) },

equivalently

ā ∈ arg max_{a* ∈ A} { ∑_{i ∈ N} U_i(a*) }.

Therefore, a state is stochastically stable if and only if the action profile is efficient. □
