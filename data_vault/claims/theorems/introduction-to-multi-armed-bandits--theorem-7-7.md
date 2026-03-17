---
slug: introduction-to-multi-armed-bandits--theorem-7-7
label: Theorem 7.7
claim_type: theorem
statement: Consider combinatorial semi-bandits with deterministic oblivious adversary.
  Then algorithm SemiBanditFTPL with appropriately chosen parameter γ achieved regret
  E[R(T)] ≤ O(d^{5/4} T^{3/4}).
proof: We use algorithm SemiBanditHedge as before, but replace Hedge with FTPL; call
  the new algorithm SemiBanditFTPL. The analysis from Section 37 carries over to SemiBanditFTPL.
  We take u = d^2/γ as a known upper bound on the fake costs of actions, and note
  that the fake costs of atoms are at most u/d. Thus, we can apply Theorem 7.1 for
  FTPL with fake costs, and obtain regret E[R(T)] ≤ O(u√(dT)) + γT. Optimizing the
  choice of parameter γ, we immediately obtain E[R(T)] ≤ O(d^{5/4} T^{3/4}).
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/combinatorial-semi-bandits]]'
- '[[concepts/deterministic-oblivious-adversary]]'
- '[[concepts/semi-bandit-feedback]]'
- '[[concepts/optimization-oracle]]'
- '[[concepts/follow-the-perturbed-leader]]'
- '[[concepts/regret-r-t]]'
about_meta:
- target: '[[concepts/combinatorial-semi-bandits]]'
  role: primary
  aspect: ''
- target: '[[concepts/deterministic-oblivious-adversary]]'
  role: primary
  aspect: ''
- target: '[[concepts/semi-bandit-feedback]]'
  role: primary
  aspect: ''
- target: '[[concepts/optimization-oracle]]'
  role: primary
  aspect: ''
- target: '[[concepts/follow-the-perturbed-leader]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret-r-t]]'
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

# Theorem 7.7

Consider combinatorial semi-bandits with deterministic oblivious adversary. Then algorithm SemiBanditFTPL with appropriately chosen parameter γ achieved regret E[R(T)] ≤ O(d^{5/4} T^{3/4}).


## Proof

We use algorithm SemiBanditHedge as before, but replace Hedge with FTPL; call the new algorithm SemiBanditFTPL. The analysis from Section 37 carries over to SemiBanditFTPL. We take u = d^2/γ as a known upper bound on the fake costs of actions, and note that the fake costs of atoms are at most u/d. Thus, we can apply Theorem 7.1 for FTPL with fake costs, and obtain regret E[R(T)] ≤ O(u√(dT)) + γT. Optimizing the choice of parameter γ, we immediately obtain E[R(T)] ≤ O(d^{5/4} T^{3/4}).
