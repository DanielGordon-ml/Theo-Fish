---
slug: achieving-pareto-optimality-in-games-via-single-bit-feedback--sbc-pe-algorithm
label: SBC-PE Algorithm
claim_type: algorithm
statement: SBC-PE is an explore-then-commit multi-agent learning algorithm requiring
  only one bit per agent per round. Agents first explore by randomly sampling actions,
  then commit to those most often aligned with collective satisfaction. At each step,
  agents broadcast a single-bit signal generated probabilistically from their realized
  utilities and parameters. The dynamics provably drives the system to the exact socially
  optimal outcome with O(log T) expected total regret.
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/finite-strategic-form-games]]'
- '[[concepts/signal-bit]]'
- '[[concepts/system-welfare-function]]'
- '[[concepts/communication-efficient]]'
- '[[concepts/exploitation-phase]]'
- '[[concepts/explore-then-commit-procedure]]'
- '[[concepts/expected-regret]]'
- '[[concepts/sbc-pe-algorithm]]'
- '[[concepts/multi-agent-system]]'
- '[[concepts/exploration-phase]]'
- '[[concepts/logarithmic-regret-bound]]'
about_meta:
- target: '[[concepts/finite-strategic-form-games]]'
  role: primary
  aspect: ''
- target: '[[concepts/signal-bit]]'
  role: primary
  aspect: ''
- target: '[[concepts/system-welfare-function]]'
  role: primary
  aspect: ''
- target: '[[concepts/communication-efficient]]'
  role: primary
  aspect: ''
- target: '[[concepts/exploitation-phase]]'
  role: primary
  aspect: ''
- target: '[[concepts/explore-then-commit-procedure]]'
  role: primary
  aspect: ''
- target: '[[concepts/expected-regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/sbc-pe-algorithm]]'
  role: primary
  aspect: ''
- target: '[[concepts/multi-agent-system]]'
  role: primary
  aspect: ''
- target: '[[concepts/exploration-phase]]'
  role: primary
  aspect: ''
- target: '[[concepts/logarithmic-regret-bound]]'
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

# Single-Bit Coordination Dynamics for Pareto-Efficient Outcomes (SBC-PE)

SBC-PE is an explore-then-commit multi-agent learning algorithm requiring only one bit per agent per round. Agents first explore by randomly sampling actions, then commit to those most often aligned with collective satisfaction. At each step, agents broadcast a single-bit signal generated probabilistically from their realized utilities and parameters. The dynamics provably drives the system to the exact socially optimal outcome with O(log T) expected total regret.
