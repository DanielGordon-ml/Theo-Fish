---
slug: introduction-to-multi-armed-bandits--theorem-7-1
label: Theorem 7.1
claim_type: theorem
statement: 'Consider Algorithm 1 with algorithm ALG that achieves regret bound E[R(T)]
  ≤ f(T,K,u) against adaptive, u-bounded adversary, for any given u > 0 that is known
  to the algorithm.


  Consider adversarial bandits with a deterministic, oblivious adversary. Assume "fake
  costs" satisfy


  E[ĉ_t(x) | p_t] = c_t(x) and ĉ_t(x) ≤ u/γ for all experts x and all rounds t,


  where u is some number that is known to the algorithm. Then Algorithm 1 achieves
  regret


  E[R(T)] ≤ f(T,K,u/γ) + γT.'
proof: ''
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/deterministic-oblivious-adversary]]'
- '[[concepts/u-bounded]]'
- '[[concepts/adversarial-bandits-problem]]'
- '[[concepts/bandit-feedback]]'
- '[[concepts/regret]]'
- '[[concepts/fake-cost-function-on-arm]]'
- '[[concepts/full-feedback]]'
- '[[concepts/gamma]]'
about_meta:
- target: '[[concepts/deterministic-oblivious-adversary]]'
  role: primary
  aspect: ''
- target: '[[concepts/u-bounded]]'
  role: primary
  aspect: ''
- target: '[[concepts/adversarial-bandits-problem]]'
  role: primary
  aspect: ''
- target: '[[concepts/bandit-feedback]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/fake-cost-function-on-arm]]'
  role: primary
  aspect: ''
- target: '[[concepts/full-feedback]]'
  role: primary
  aspect: ''
- target: '[[concepts/gamma]]'
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

# Theorem 7.1

Consider Algorithm 1 with algorithm ALG that achieves regret bound E[R(T)] ≤ f(T,K,u) against adaptive, u-bounded adversary, for any given u > 0 that is known to the algorithm.

Consider adversarial bandits with a deterministic, oblivious adversary. Assume "fake costs" satisfy

E[ĉ_t(x) | p_t] = c_t(x) and ĉ_t(x) ≤ u/γ for all experts x and all rounds t,

where u is some number that is known to the algorithm. Then Algorithm 1 achieves regret

E[R(T)] ≤ f(T,K,u/γ) + γT.
