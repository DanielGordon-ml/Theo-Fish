---
slug: achieving-pareto-optimality-through-distributed-learning--lemma-2
label: Lemma 2
claim_type: lemma
statement: The recurrence classes of the unperturbed process $P^{0}$ are $D^{0}$ and
  all singletons $z \in C^{0}$.
proof: 'The set of states $D^{0}$ represents a single recurrence class of the unperturbed
  process since the probability of transitioning between any two states $z_{1}, z_{2}
  \in D^{0}$ is $O(1)$ and when $\epsilon = 0$ there is no possibility of exiting
  from $D^{0}$. Any state $[\bar{a}, \bar{u}, C] \in C^{0}$ is a recurrent class of
  the unperturbed process, because all agents will continue to play their baseline
  action at all future times.


  We will now show that the states $D^{0}$ and all singletons $z \in C^{0}$ represent
  the only recurrent states. Suppose that a proper subset of agents $S \subset N$
  is discontent, and the benchmark actions and benchmark utilities of all other agents
  are $\bar{a}_{-S}$ and $\bar{u}_{-S}$, respectively. By interdependence, there exists
  an agent $j \not\in S$ and an action tuple $a_{S}^{\prime} \in \prod_{i \in S} \mathcal{A}_{i}$
  such that $u_{j} \ne U_{j}(a_{S}^{\prime}, \bar{a}_{-S})$. This situation cannot
  be a recurrence class of the unperturbed process because the agent set $S$ will
  eventually play action $a_{S}^{\prime}$ with probability 1, thereby causing agent
  $j$ to become discontent. Agent set $S$ will eventually play action $a_{S}^{\prime}$
  with probability 1, because each agent $i \in S$ is discontent and hence selects
  actions uniformly for the action set $\mathcal{A}_{i}$. Consequently, at each subsequent
  period, the action $a_{S}^{\prime}$ will be played with probability $1/|A_{S}|$.
  Note that once the agent set $S$ selects action $a_{S}^{\prime}$, the payoff of
  agent $j$ will be different from agent $j$''s baseline utility, i.e., $\bar{u}_{j}
  \neq U_{j}(a_{S}^{\prime}, \bar{a}_{-S})$, thereby causing agent $j$ to become discontent.
  This process can be repeated to show that all agents will eventually become discontent
  with probability $O(1)$; hence any state that consists of a partial collection of
  discontent agents $S \subset N$ is not a recurrence class of the unperturbed process.


  Lastly, consider a state $[\bar{a}, \bar{u}, C]$ where all agents are content, but
  there exists at least one agent $i$ whose benchmark action and benchmark utility
  are not aligned, i.e., $\bar{u}_{i} \neq U_{i}(\bar{a})$. For the unperturbed process,
  at the ensuing time step the action profile $\bar{a}$ will be played and agent $i$
  will become discontent since $\bar{u}_{i} \neq U_{i}(\bar{a})$. Since one agent
  is discontent, all agents will eventually become discontent. This completes the
  proof of Lemma 2.'
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/unperturbed-probability-transition-matrix]]'
- '[[concepts/markov-process]]'
- '[[concepts/content-aligned-states]]'
- '[[concepts/discontent-states]]'
- '[[concepts/recurrence-class]]'
- '[[concepts/interdependence]]'
about_meta:
- target: '[[concepts/unperturbed-probability-transition-matrix]]'
  role: primary
  aspect: ''
- target: '[[concepts/markov-process]]'
  role: primary
  aspect: ''
- target: '[[concepts/content-aligned-states]]'
  role: primary
  aspect: ''
- target: '[[concepts/discontent-states]]'
  role: primary
  aspect: ''
- target: '[[concepts/recurrence-class]]'
  role: primary
  aspect: ''
- target: '[[concepts/interdependence]]'
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

# Lemma 2

The recurrence classes of the unperturbed process $P^{0}$ are $D^{0}$ and all singletons $z \in C^{0}$.


## Proof

The set of states $D^{0}$ represents a single recurrence class of the unperturbed process since the probability of transitioning between any two states $z_{1}, z_{2} \in D^{0}$ is $O(1)$ and when $\epsilon = 0$ there is no possibility of exiting from $D^{0}$. Any state $[\bar{a}, \bar{u}, C] \in C^{0}$ is a recurrent class of the unperturbed process, because all agents will continue to play their baseline action at all future times.

We will now show that the states $D^{0}$ and all singletons $z \in C^{0}$ represent the only recurrent states. Suppose that a proper subset of agents $S \subset N$ is discontent, and the benchmark actions and benchmark utilities of all other agents are $\bar{a}_{-S}$ and $\bar{u}_{-S}$, respectively. By interdependence, there exists an agent $j \not\in S$ and an action tuple $a_{S}^{\prime} \in \prod_{i \in S} \mathcal{A}_{i}$ such that $u_{j} \ne U_{j}(a_{S}^{\prime}, \bar{a}_{-S})$. This situation cannot be a recurrence class of the unperturbed process because the agent set $S$ will eventually play action $a_{S}^{\prime}$ with probability 1, thereby causing agent $j$ to become discontent. Agent set $S$ will eventually play action $a_{S}^{\prime}$ with probability 1, because each agent $i \in S$ is discontent and hence selects actions uniformly for the action set $\mathcal{A}_{i}$. Consequently, at each subsequent period, the action $a_{S}^{\prime}$ will be played with probability $1/|A_{S}|$. Note that once the agent set $S$ selects action $a_{S}^{\prime}$, the payoff of agent $j$ will be different from agent $j$'s baseline utility, i.e., $\bar{u}_{j} \neq U_{j}(a_{S}^{\prime}, \bar{a}_{-S})$, thereby causing agent $j$ to become discontent. This process can be repeated to show that all agents will eventually become discontent with probability $O(1)$; hence any state that consists of a partial collection of discontent agents $S \subset N$ is not a recurrence class of the unperturbed process.

Lastly, consider a state $[\bar{a}, \bar{u}, C]$ where all agents are content, but there exists at least one agent $i$ whose benchmark action and benchmark utility are not aligned, i.e., $\bar{u}_{i} \neq U_{i}(\bar{a})$. For the unperturbed process, at the ensuing time step the action profile $\bar{a}$ will be played and agent $i$ will become discontent since $\bar{u}_{i} \neq U_{i}(\bar{a})$. Since one agent is discontent, all agents will eventually become discontent. This completes the proof of Lemma 2.
