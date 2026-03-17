---
slug: introduction-to-multi-armed-bandits--ucb1-with-log-t-confidence-radius-does-not-require-known-t
label: UCB1 with log(t) confidence radius does not require known T
claim_type: proposition
statement: Use UCB1 with confidence radius r_t(a) = √(2 log(t) / n_t(a)), as in (Auer
  et al., 2002a). This version does not input T, and its regret analysis works for
  an arbitrary T.
proof: ''
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/regret-bound]]'
- '[[concepts/time-horizon-t]]'
- '[[concepts/ucb1-algorithm]]'
- '[[concepts/confidence-radius-r-t-a]]'
about_meta:
- target: '[[concepts/regret-bound]]'
  role: primary
  aspect: ''
- target: '[[concepts/time-horizon-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/ucb1-algorithm]]'
  role: primary
  aspect: ''
- target: '[[concepts/confidence-radius-r-t-a]]'
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

# UCB1 with log(t) confidence radius does not require known T

Use UCB1 with confidence radius r_t(a) = √(2 log(t) / n_t(a)), as in (Auer et al., 2002a). This version does not input T, and its regret analysis works for an arbitrary T.
