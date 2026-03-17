---
slug: introduction-to-multi-armed-bandits--regret-bound-for-adversarial-bandits
label: Regret bound for adversarial bandits
claim_type: theorem
statement: For adversarial bandits with deterministic oblivious adversary, bounded
  per-round costs $c_t(a) \leq 1$ for all rounds $t$ and all arms $a$, the algorithm
  achieves regret bound $\operatornamewithlimits{\mathbb{E}}[R(T)] \leq O\left(\sqrt{KT\log
  K}\right)$.
proof: ''
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/number-of-arms-k]]'
- '[[concepts/regret]]'
- '[[concepts/deterministic-oblivious-adversary]]'
- '[[concepts/adversarial-bandits-problem]]'
- '[[concepts/time-horizon-t]]'
- '[[concepts/bounded-per-round-costs]]'
about_meta:
- target: '[[concepts/number-of-arms-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/deterministic-oblivious-adversary]]'
  role: primary
  aspect: ''
- target: '[[concepts/adversarial-bandits-problem]]'
  role: primary
  aspect: ''
- target: '[[concepts/time-horizon-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/bounded-per-round-costs]]'
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

# Regret bound for adversarial bandits

For adversarial bandits with deterministic oblivious adversary, bounded per-round costs $c_t(a) \leq 1$ for all rounds $t$ and all arms $a$, the algorithm achieves regret bound $\operatornamewithlimits{\mathbb{E}}[R(T)] \leq O\left(\sqrt{KT\log K}\right)$.
