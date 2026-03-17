---
slug: introduction-to-multi-armed-bandits--dynamic-regret-with-total-variation-v-unknown-v
label: Dynamic regret with total variation V (unknown V)
claim_type: theorem
statement: The same regret rate $\tilde{O}(V^{1/3}T^{2/3})$ can be achieved even without
  knowing $V$, using a more advanced algorithm (Chen et al., 2019). This result also
  obtains the best possible regret rate when each arm's expected costs change by at
  most $\epsilon$ per round, without knowing the $\epsilon$.
proof: ''
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/adversarial-bandits-problem]]'
- '[[concepts/total-variation-in-cost-distributions]]'
- '[[concepts/dynamic-regret]]'
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

# Dynamic regret with total variation V (unknown V)

The same regret rate $\tilde{O}(V^{1/3}T^{2/3})$ can be achieved even without knowing $V$, using a more advanced algorithm (Chen et al., 2019). This result also obtains the best possible regret rate when each arm's expected costs change by at most $\epsilon$ per round, without knowing the $\epsilon$.
