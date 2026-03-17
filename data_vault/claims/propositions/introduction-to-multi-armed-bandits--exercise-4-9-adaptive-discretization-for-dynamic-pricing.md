---
slug: introduction-to-multi-armed-bandits--exercise-4-9-adaptive-discretization-for-dynamic-pricing
label: Exercise 4.9 (adaptive discretization for dynamic pricing)
claim_type: proposition
statement: A modified zooming algorithm for dynamic pricing, where the confidence
  ball of arm $x$ is redefined as the interval $[x, x+r_t(x)]$ and in the activation
  rule the smallest uncovered arm is activated, achieves the regret bound in Theorem
  4.18.
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/confidence-ball]]'
- '[[concepts/zooming-algorithm-for-lipschitz-bandits]]'
- '[[concepts/dynamic-pricing-problem]]'
- '[[concepts/activation-rule]]'
- '[[concepts/one-sided-lipschitzness]]'
about_meta:
- target: '[[concepts/confidence-ball]]'
  role: primary
  aspect: ''
- target: '[[concepts/zooming-algorithm-for-lipschitz-bandits]]'
  role: primary
  aspect: ''
- target: '[[concepts/dynamic-pricing-problem]]'
  role: primary
  aspect: ''
- target: '[[concepts/activation-rule]]'
  role: primary
  aspect: ''
- target: '[[concepts/one-sided-lipschitzness]]'
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

# Exercise 4.9 (adaptive discretization for dynamic pricing)

A modified zooming algorithm for dynamic pricing, where the confidence ball of arm $x$ is redefined as the interval $[x, x+r_t(x)]$ and in the activation rule the smallest uncovered arm is activated, achieves the regret bound in Theorem 4.18.
