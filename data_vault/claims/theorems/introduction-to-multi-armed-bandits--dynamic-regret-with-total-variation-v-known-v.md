---
slug: introduction-to-multi-armed-bandits--dynamic-regret-with-total-variation-v-known-v
label: Dynamic regret with total variation V (known V)
claim_type: theorem
statement: Consider the total variation in cost distributions, $V = \sum_{t \in [T-1]}
  V_t$, where $V_t$ is the amount of change in a given round $t$ (defined as a total-variation
  distance between the cost distribution for rounds $t$ and $t+1$). The optimal regret
  rate is $\tilde{O}(V^{1/3}T^{2/3})$ when $V$ is known; it can be achieved, e.g.,
  by $\mathtt{Exp4}$ algorithm with restarts.
proof: ''
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/adversarial-bandits-problem]]'
- '[[concepts/total-variation-in-cost-distributions]]'
- '[[concepts/dynamic-regret]]'
- '[[concepts/exp4]]'
about_meta:
- target: '[[concepts/adversarial-bandits-problem]]'
  role: primary
  aspect: ''
- target: '[[concepts/total-variation-in-cost-distributions]]'
  role: primary
  aspect: ''
- target: '[[concepts/dynamic-regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/exp4]]'
  role: primary
  aspect: ''
depends_on: []
depends_on_meta: []
sourced_from:
- '[[sources/1904.07272|Introduction to Multi-Armed Bandits]]'
sourced_from_meta:
- target: '[[sources/1904.07272|Introduction to Multi-Armed Bandits]]'
  section: ''
  page: ''
  confidence: 0.0
---

# Dynamic regret with total variation V (known V)

Consider the total variation in cost distributions, $V = \sum_{t \in [T-1]} V_t$, where $V_t$ is the amount of change in a given round $t$ (defined as a total-variation distance between the cost distribution for rounds $t$ and $t+1$). The optimal regret rate is $\tilde{O}(V^{1/3}T^{2/3})$ when $V$ is known; it can be achieved, e.g., by $\mathtt{Exp4}$ algorithm with restarts.
