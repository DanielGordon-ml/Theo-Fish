---
slug: introduction-to-multi-armed-bandits--regret-bound-for-adversarial-bandits-with-expert-advice
label: Regret bound for adversarial bandits with expert advice
claim_type: theorem
statement: 'For the adversarial bandits with expert advice problem with K arms, N
  experts, T rounds, and a deterministic oblivious adversary, solving the problem
  via the reduction in Algorithm 1 achieves

  $$\operatornamewithlimits{\mathbb{E}}[R(T)]\leq O\left(\,\sqrt{KT\log N}\,\right).$$'
proof: ''
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/adversarial-bandits-with-expert-advice]]'
- '[[concepts/time-horizon-t]]'
- '[[concepts/regret]]'
- '[[concepts/deterministic-oblivious-adversary]]'
- '[[concepts/number-of-experts]]'
- '[[concepts/number-of-arms-k]]'
about_meta:
- target: '[[concepts/adversarial-bandits-with-expert-advice]]'
  role: primary
  aspect: ''
- target: '[[concepts/time-horizon-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/deterministic-oblivious-adversary]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-experts]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-arms-k]]'
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

# Regret bound for adversarial bandits with expert advice

For the adversarial bandits with expert advice problem with K arms, N experts, T rounds, and a deterministic oblivious adversary, solving the problem via the reduction in Algorithm 1 achieves
$$\operatornamewithlimits{\mathbb{E}}[R(T)]\leq O\left(\,\sqrt{KT\log N}\,\right).$$
