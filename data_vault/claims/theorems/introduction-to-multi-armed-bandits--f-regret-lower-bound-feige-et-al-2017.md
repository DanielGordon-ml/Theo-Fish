---
slug: introduction-to-multi-armed-bandits--f-regret-lower-bound-feige-et-al-2017
label: F-regret lower bound (Feige et al. 2017)
claim_type: theorem
statement: Even with $|S| \leq 3$ (and only 3 algorithms and 3 actions), no 'meta-algorithm'
  can achieve expected regret better than $O(T \log^{-3/2} T)$ relative to the best
  algorithm in $\mathcal{F}$ (henceforth, $\mathcal{F}$-regret).
proof: ''
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/lower-bound-on-regret]]'
- '[[concepts/adversarial-bandits-problem]]'
- '[[concepts/f-regret]]'
about_meta:
- target: '[[concepts/lower-bound-on-regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/adversarial-bandits-problem]]'
  role: primary
  aspect: ''
- target: '[[concepts/f-regret]]'
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

# F-regret lower bound (Feige et al. 2017)

Even with $|S| \leq 3$ (and only 3 algorithms and 3 actions), no 'meta-algorithm' can achieve expected regret better than $O(T \log^{-3/2} T)$ relative to the best algorithm in $\mathcal{F}$ (henceforth, $\mathcal{F}$-regret).
