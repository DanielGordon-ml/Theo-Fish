---
slug: distributed-multi-player-bandits-a-game-of-thrones-approach--lemma-3
label: Lemma 3
claim_type: lemma
statement: Denote by $D_0$ the set of all the discontent states (all players are discontent)
  and by $C_0$ the set of all singleton content states (all players are content).
  The recurrence classes of the unperturbed process $P^0$ are $D_0$ and all $z \in
  C_0$.
proof: In $P^0$, there is no path between the discontent states and the content ones.
  Moreover, all the discontent states are connected and all the content states are
  absorbing (i.e., singletons). Now assume there is a different recurrence class.
  In any state in this class, denoted $z_{C/D}$, not all the players are content,
  otherwise this is a $z \in C_0$ singleton. Denote one of the discontent players
  by $n$. Since she chooses her action at random, there is a positive probability
  that she will pick the same arm as any of the content players. By doing so, she
  changes the state of this player to discontent with probability 1. With $\varepsilon
  = 0$, every discontent player remains so with probability one. On the next turn,
  a discontent player may again choose the arm of a content player with a positive
  probability. By repeating this process, we conclude that there is a positive probability
  that all players become discontent. Hence, $z_{C/D}$ is connected to $D$ in $P^0$.
  We conclude that this different recurrence class is in fact connected to $\boldsymbol{D}$,
  which is a contradiction. □
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/recurrence-classes-of-unperturbed-process]]'
- '[[concepts/markov-chain]]'
- '[[concepts/discontent-states-d-0]]'
- '[[concepts/content-states-c-0]]'
- '[[concepts/mood-set-m]]'
- '[[concepts/state-space-z]]'
- '[[concepts/got-dynamics]]'
about_meta:
- target: '[[concepts/recurrence-classes-of-unperturbed-process]]'
  role: primary
  aspect: ''
- target: '[[concepts/markov-chain]]'
  role: primary
  aspect: ''
- target: '[[concepts/discontent-states-d-0]]'
  role: primary
  aspect: ''
- target: '[[concepts/content-states-c-0]]'
  role: primary
  aspect: ''
- target: '[[concepts/mood-set-m]]'
  role: primary
  aspect: ''
- target: '[[concepts/state-space-z]]'
  role: primary
  aspect: ''
- target: '[[concepts/got-dynamics]]'
  role: primary
  aspect: ''
depends_on: []
depends_on_meta: []
sourced_from:
- '[[sources/distributed_multi_player_bandits_a_game_of_thrones_approach|distributed_multi_player_bandits_a_game_of_thrones_approach]]'
sourced_from_meta:
- target: '[[sources/distributed_multi_player_bandits_a_game_of_thrones_approach|distributed_multi_player_bandits_a_game_of_thrones_approach]]'
  section: ''
  page: ''
  confidence: 0.0
---

# Lemma 3

Denote by $D_0$ the set of all the discontent states (all players are discontent) and by $C_0$ the set of all singleton content states (all players are content). The recurrence classes of the unperturbed process $P^0$ are $D_0$ and all $z \in C_0$.


## Proof

In $P^0$, there is no path between the discontent states and the content ones. Moreover, all the discontent states are connected and all the content states are absorbing (i.e., singletons). Now assume there is a different recurrence class. In any state in this class, denoted $z_{C/D}$, not all the players are content, otherwise this is a $z \in C_0$ singleton. Denote one of the discontent players by $n$. Since she chooses her action at random, there is a positive probability that she will pick the same arm as any of the content players. By doing so, she changes the state of this player to discontent with probability 1. With $\varepsilon = 0$, every discontent player remains so with probability one. On the next turn, a discontent player may again choose the arm of a content player with a positive probability. By repeating this process, we conclude that there is a positive probability that all players become discontent. Hence, $z_{C/D}$ is connected to $D$ in $P^0$. We conclude that this different recurrence class is in fact connected to $\boldsymbol{D}$, which is a contradiction. □
