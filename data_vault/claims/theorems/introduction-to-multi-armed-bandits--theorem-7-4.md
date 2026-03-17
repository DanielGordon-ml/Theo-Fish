---
slug: introduction-to-multi-armed-bandits--theorem-7-4
label: Theorem 7.4
claim_type: theorem
statement: Consider the online routing problem with semi-bandit feedback. Assume deterministic
  oblivious adversary. Algorithm SemiBanditHedge achieved regret E[R(T)] ≤ O(d^{3/2}
  T^{3/4}).
proof: Since the fake cost for each edge is at most d/γ, it follows that c_t(a) ≤
  d²/γ for each action a. Thus, we can immediately use Corollary 7.2 with u = d².
  For the number of actions, let us use an upper bound K ≤ 2^d. Then u log K ≤ d³,
  and so E[R(T)] ≤ O(d^{3/2} T^{3/4}).
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/semi-bandit-feedback]]'
- '[[concepts/online-routing]]'
- '[[concepts/hedge]]'
- '[[concepts/deterministic-oblivious-adversary]]'
- '[[concepts/fake-cost-function]]'
- '[[concepts/online-linear-optimization]]'
- '[[concepts/regret]]'
about_meta:
- target: '[[concepts/semi-bandit-feedback]]'
  role: primary
  aspect: ''
- target: '[[concepts/online-routing]]'
  role: primary
  aspect: ''
- target: '[[concepts/hedge]]'
  role: primary
  aspect: ''
- target: '[[concepts/deterministic-oblivious-adversary]]'
  role: primary
  aspect: ''
- target: '[[concepts/fake-cost-function]]'
  role: primary
  aspect: ''
- target: '[[concepts/online-linear-optimization]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret]]'
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

# Theorem 7.4

Consider the online routing problem with semi-bandit feedback. Assume deterministic oblivious adversary. Algorithm SemiBanditHedge achieved regret E[R(T)] ≤ O(d^{3/2} T^{3/4}).


## Proof

Since the fake cost for each edge is at most d/γ, it follows that c_t(a) ≤ d²/γ for each action a. Thus, we can immediately use Corollary 7.2 with u = d². For the number of actions, let us use an upper bound K ≤ 2^d. Then u log K ≤ d³, and so E[R(T)] ≤ O(d^{3/2} T^{3/4}).
