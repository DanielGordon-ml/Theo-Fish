---
slug: achieving-pareto-optimality-in-games-via-single-bit-feedback--algorithm-1
label: Algorithm 1
claim_type: algorithm
statement: The Single-Bit Coordination Dynamics for Pareto-Efficient Outcomes (SBC-PE)
  is an explore-then-commit procedure. In the exploration phase, agents play random
  actions for K rounds, observe utilities, and broadcast a one-bit signal m_i^t stochastically
  generated as in (3). Each agent i keeps counters c_i(a_i), incrementing when all
  broadcast {m_j^t=1}_{j∈N}. After exploration, agent i selects ā_i ∈ argmax_{a_i
  ∈ A_i} c_i(a_i). In the exploitation phase, agent i repeatedly plays the selected
  action ā_i, so the joint action ā=(ā_1,…,ā_n) achieves the Pareto-efficient outcome.
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/exploration-phase]]'
- '[[concepts/explore-then-commit-procedure]]'
- '[[concepts/increment-counter-operation]]'
- '[[concepts/signal-bit]]'
- '[[concepts/stochastic-signal-generation]]'
- '[[concepts/counter-c-i-a-i]]'
- '[[concepts/exploitation-phase]]'
- '[[concepts/committed-joint-action]]'
- '[[concepts/pareto-efficient-outcome]]'
- '[[concepts/sbc-pe-algorithm]]'
- '[[concepts/one-bit-signal]]'
- '[[concepts/communication-efficient]]'
- '[[concepts/exploration-parameter-epsilon]]'
- '[[concepts/exploration-horizon-k]]'
- '[[concepts/action-selection-operator]]'
about_meta:
- target: '[[concepts/exploration-phase]]'
  role: primary
  aspect: ''
- target: '[[concepts/explore-then-commit-procedure]]'
  role: primary
  aspect: ''
- target: '[[concepts/increment-counter-operation]]'
  role: primary
  aspect: ''
- target: '[[concepts/signal-bit]]'
  role: primary
  aspect: ''
- target: '[[concepts/stochastic-signal-generation]]'
  role: primary
  aspect: ''
- target: '[[concepts/counter-c-i-a-i]]'
  role: primary
  aspect: ''
- target: '[[concepts/exploitation-phase]]'
  role: primary
  aspect: ''
- target: '[[concepts/committed-joint-action]]'
  role: primary
  aspect: ''
- target: '[[concepts/pareto-efficient-outcome]]'
  role: primary
  aspect: ''
- target: '[[concepts/sbc-pe-algorithm]]'
  role: primary
  aspect: ''
- target: '[[concepts/one-bit-signal]]'
  role: primary
  aspect: ''
- target: '[[concepts/communication-efficient]]'
  role: primary
  aspect: ''
- target: '[[concepts/exploration-parameter-epsilon]]'
  role: primary
  aspect: ''
- target: '[[concepts/exploration-horizon-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/action-selection-operator]]'
  role: primary
  aspect: ''
depends_on: []
depends_on_meta: []
sourced_from:
- '[[sources/2509.25921|Achieving Pareto Optimality in Games via Single-bit Feedback]]'
sourced_from_meta:
- target: '[[sources/2509.25921|Achieving Pareto Optimality in Games via Single-bit
    Feedback]]'
  section: ''
  page: ''
  confidence: 0.0
---

# Algorithm 1

The Single-Bit Coordination Dynamics for Pareto-Efficient Outcomes (SBC-PE) is an explore-then-commit procedure. In the exploration phase, agents play random actions for K rounds, observe utilities, and broadcast a one-bit signal m_i^t stochastically generated as in (3). Each agent i keeps counters c_i(a_i), incrementing when all broadcast {m_j^t=1}_{j∈N}. After exploration, agent i selects ā_i ∈ argmax_{a_i ∈ A_i} c_i(a_i). In the exploitation phase, agent i repeatedly plays the selected action ā_i, so the joint action ā=(ā_1,…,ā_n) achieves the Pareto-efficient outcome.
