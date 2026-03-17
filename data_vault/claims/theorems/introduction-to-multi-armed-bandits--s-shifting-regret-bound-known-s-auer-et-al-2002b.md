---
slug: introduction-to-multi-armed-bandits--s-shifting-regret-bound-known-s-auer-et-al-2002b
label: S-shifting regret bound (known S, Auer et al. 2002b)
claim_type: theorem
statement: Auer et al. (2002b) tackle shifting regret using a modification of $\mathtt{Exp3}$
  algorithm, with essentially the same running time as $\mathtt{Exp3}$ and a more
  involved analysis. They obtain $\operatornamewithlimits{\mathbb{E}}[R_S(T)] = \tilde{O}(\sqrt{SKT})$
  if $S$ is known.
proof: ''
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/adversarial-bandits-problem]]'
- '[[concepts/s-shifting-regret]]'
- '[[concepts/exp3]]'
about_meta:
- target: '[[concepts/adversarial-bandits-problem]]'
  role: primary
  aspect: ''
- target: '[[concepts/s-shifting-regret]]'
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

# S-shifting regret bound (known S, Auer et al. 2002b)

Auer et al. (2002b) tackle shifting regret using a modification of $\mathtt{Exp3}$ algorithm, with essentially the same running time as $\mathtt{Exp3}$ and a more involved analysis. They obtain $\operatornamewithlimits{\mathbb{E}}[R_S(T)] = \tilde{O}(\sqrt{SKT})$ if $S$ is known.
