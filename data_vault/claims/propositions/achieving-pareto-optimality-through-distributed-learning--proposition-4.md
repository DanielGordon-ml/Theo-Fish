---
slug: achieving-pareto-optimality-through-distributed-learning--proposition-4
label: Proposition 4
claim_type: proposition
statement: There exists no uncoupled learning algorithm that leads to an efficient
  action profile for all finite strategic-form games.
proof: 'We will prove this proposition by contradiction. Suppose that there exists
  a uncoupled learning algorithm of the form (1) that leads to an efficient action
  profile for all finite strategic-form games. When considering the two-player game
  highlighted above, this algorithm will lead behavior to the action profile $(B,
  B)$. However, from player 1''s perspective, this game is equivalent to a simple
  one-player game with payoffs.


  | | A 1/2 |

  | --- | --- |

  | | B 1/4 |


  This learning algorithm leads to the behavior $A$ in this one-player game. Therefore,
  we have a contradiction since the same learning algorithm is not able to ensure
  that behavior leads to $(A)$ for the one-player setting and $(B, B)$ for the two-player
  setting.'
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/uncoupled-learning-algorithm]]'
- '[[concepts/one-player-game]]'
- '[[concepts/interdependence]]'
- '[[concepts/two-player-game]]'
- '[[concepts/finite-strategic-form-games]]'
- '[[concepts/efficient-action-profile]]'
about_meta:
- target: '[[concepts/uncoupled-learning-algorithm]]'
  role: primary
  aspect: ''
- target: '[[concepts/one-player-game]]'
  role: primary
  aspect: ''
- target: '[[concepts/interdependence]]'
  role: primary
  aspect: ''
- target: '[[concepts/two-player-game]]'
  role: primary
  aspect: ''
- target: '[[concepts/finite-strategic-form-games]]'
  role: primary
  aspect: ''
- target: '[[concepts/efficient-action-profile]]'
  role: primary
  aspect: ''
depends_on: []
depends_on_meta: []
contradicts:
- '[[claims/achieving-pareto-optimality-through-distributed-learning--main-theorem]]'
contradicts_meta:
- target: '[[claims/achieving-pareto-optimality-through-distributed-learning--main-theorem]]'
sourced_from:
- '[[sources/achieving_pareto_optimality_through_distributed_learning|achieving_pareto_optimality_through_distributed_learning]]'
sourced_from_meta:
- target: '[[sources/achieving_pareto_optimality_through_distributed_learning|achieving_pareto_optimality_through_distributed_learning]]'
  section: ''
  page: ''
  confidence: 0.0
---

# Proposition 4

There exists no uncoupled learning algorithm that leads to an efficient action profile for all finite strategic-form games.


## Proof

We will prove this proposition by contradiction. Suppose that there exists a uncoupled learning algorithm of the form (1) that leads to an efficient action profile for all finite strategic-form games. When considering the two-player game highlighted above, this algorithm will lead behavior to the action profile $(B, B)$. However, from player 1's perspective, this game is equivalent to a simple one-player game with payoffs.

| | A 1/2 |
| --- | --- |
| | B 1/4 |

This learning algorithm leads to the behavior $A$ in this one-player game. Therefore, we have a contradiction since the same learning algorithm is not able to ensure that behavior leads to $(A)$ for the one-player setting and $(B, B)$ for the two-player setting.
