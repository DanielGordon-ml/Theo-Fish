---
slug: introduction-to-multi-armed-bandits--remark-5-15-high-probability-bound
label: Remark 5.15 (high-probability bound)
claim_type: proposition
statement: 'Using the same parameters, $\alpha=\epsilon=\sqrt{\tfrac{\ln K}{T}}$ and
  $\beta=0$, and assuming all costs are at most $1$, Eq. (82) implies that

  $$\textstyle\sum_{t\in[T]}p_{t}\cdot c_{t}-\mathtt{cost}^{*}<2\cdot\sqrt{T\ln{K}}.$$

  This holds with probability $1$ (deterministically over the algorithm''s randomness
  in a specific sense).'
proof: Directly from Eq. (82) with $\alpha=\epsilon=\sqrt{\tfrac{\ln K}{T}}$ and $\beta=0$.
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/online-learning-with-experts]]'
- '[[concepts/hedge]]'
- '[[concepts/regret]]'
- '[[concepts/high-probability-regret]]'
about_meta:
- target: '[[concepts/online-learning-with-experts]]'
  role: primary
  aspect: ''
- target: '[[concepts/hedge]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/high-probability-regret]]'
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

# Remark 5.15 (high-probability bound)

Using the same parameters, $\alpha=\epsilon=\sqrt{\tfrac{\ln K}{T}}$ and $\beta=0$, and assuming all costs are at most $1$, Eq. (82) implies that
$$\textstyle\sum_{t\in[T]}p_{t}\cdot c_{t}-\mathtt{cost}^{*}<2\cdot\sqrt{T\ln{K}}.$$
This holds with probability $1$ (deterministically over the algorithm's randomness in a specific sense).


## Proof

Directly from Eq. (82) with $\alpha=\epsilon=\sqrt{\tfrac{\ln K}{T}}$ and $\beta=0$.
