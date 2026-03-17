---
slug: achieving-pareto-optimality-through-distributed-learning--learning-algorithm-agent-dynamics-state-dynamics
label: Learning Algorithm (Agent Dynamics + State Dynamics)
claim_type: algorithm
statement: 'A payoff-based learning algorithm where each agent i maintains a state
  triple [ā_i, ū_i, m_i] consisting of a benchmark action, benchmark payoff, and mood
  (content or discontent). Agent Dynamics: Fix an experimentation rate 1 > ε > 0 and
  constant c ≥ n. When content (m_i = C), agent i plays ā_i with probability 1 - ε^c
  and each other action with probability ε^c/(|A_i| - 1). When discontent (m_i = D),
  agent i plays each action uniformly with probability 1/|A_i|. State Dynamics: When
  content and [a_i, u_i] = [ā_i, ū_i], state remains [ā_i, ū_i, C]. When content and
  [a_i, u_i] ≠ [ā_i, ū_i], transition to [a_i, u_i, C] with prob ε^{1-u_i} and [a_i,
  u_i, D] with prob 1 - ε^{1-u_i}. When discontent, transition to [a_i, u_i, C] with
  prob ε^{1-u_i} and [a_i, u_i, D] with prob 1 - ε^{1-u_i}.'
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/agent-state-triple]]'
- '[[concepts/welfare-function]]'
- '[[concepts/mood-set]]'
- '[[concepts/state-dynamics]]'
- '[[concepts/constant-c]]'
- '[[concepts/payoff-based-learning-algorithm]]'
- '[[concepts/experimentation-rate]]'
- '[[concepts/agent-dynamics]]'
- '[[concepts/efficient-joint-action]]'
- '[[concepts/interdependence]]'
- '[[concepts/stochastically-stable-state]]'
about_meta:
- target: '[[concepts/agent-state-triple]]'
  role: primary
  aspect: ''
- target: '[[concepts/welfare-function]]'
  role: primary
  aspect: ''
- target: '[[concepts/mood-set]]'
  role: primary
  aspect: ''
- target: '[[concepts/state-dynamics]]'
  role: primary
  aspect: ''
- target: '[[concepts/constant-c]]'
  role: primary
  aspect: ''
- target: '[[concepts/payoff-based-learning-algorithm]]'
  role: primary
  aspect: ''
- target: '[[concepts/experimentation-rate]]'
  role: primary
  aspect: ''
- target: '[[concepts/agent-dynamics]]'
  role: primary
  aspect: ''
- target: '[[concepts/efficient-joint-action]]'
  role: primary
  aspect: ''
- target: '[[concepts/interdependence]]'
  role: primary
  aspect: ''
- target: '[[concepts/stochastically-stable-state]]'
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

# Learning Algorithm (Agent Dynamics + State Dynamics)

A payoff-based learning algorithm where each agent i maintains a state triple [ā_i, ū_i, m_i] consisting of a benchmark action, benchmark payoff, and mood (content or discontent). Agent Dynamics: Fix an experimentation rate 1 > ε > 0 and constant c ≥ n. When content (m_i = C), agent i plays ā_i with probability 1 - ε^c and each other action with probability ε^c/(|A_i| - 1). When discontent (m_i = D), agent i plays each action uniformly with probability 1/|A_i|. State Dynamics: When content and [a_i, u_i] = [ā_i, ū_i], state remains [ā_i, ū_i, C]. When content and [a_i, u_i] ≠ [ā_i, ū_i], transition to [a_i, u_i, C] with prob ε^{1-u_i} and [a_i, u_i, D] with prob 1 - ε^{1-u_i}. When discontent, transition to [a_i, u_i, C] with prob ε^{1-u_i} and [a_i, u_i, D] with prob 1 - ε^{1-u_i}.
