---
slug: introduction-to-multi-armed-bandits--swap-regret-via-blum-mansour-transformation-with-exp3
label: Swap regret via Blum-Mansour transformation with Exp3
claim_type: theorem
statement: Blum and Mansour (2007) provided an explicit transformation that takes
  an algorithm with a 'standard' regret bound, and transforms it into an algorithm
  with a bound on swap regret. Plugging in $\mathtt{Exp3}$ algorithm, this approach
  results in $\tilde{O}(K\sqrt{KT})$ regret rate.
proof: ''
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/adversarial-bandits-problem]]'
- '[[concepts/swap-regret]]'
- '[[concepts/exp3]]'
about_meta:
- target: '[[concepts/adversarial-bandits-problem]]'
  role: primary
  aspect: ''
- target: '[[concepts/swap-regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/exp3]]'
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

# Swap regret via Blum-Mansour transformation with Exp3

Blum and Mansour (2007) provided an explicit transformation that takes an algorithm with a 'standard' regret bound, and transforms it into an algorithm with a bound on swap regret. Plugging in $\mathtt{Exp3}$ algorithm, this approach results in $\tilde{O}(K\sqrt{KT})$ regret rate.
