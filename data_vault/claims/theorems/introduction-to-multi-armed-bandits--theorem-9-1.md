---
slug: introduction-to-multi-armed-bandits--theorem-9-1
label: Theorem 9.1
claim_type: theorem
statement: 'For an arbitrary adversary ADV it holds that


  $\tfrac{1}{T}\,\mathtt{cost}(\mathtt{ALG})\leq v^{*}+R(T)/T.$


  In particular, if we (only) posit sublinear expected regret, $\operatornamewithlimits{\mathbb{E}}[R(t)]=o(t)$,
  then the expected average cost $\tfrac{1}{T}\,\operatornamewithlimits{\mathbb{E}}[\mathtt{cost}(\mathtt{ALG})]$
  is asymptotically upper-bounded by $v^{*}$.'
proof: We have cost* = min_{rows i} cost(i) ≤ E_{i ~ p*}[cost(i)] = ∑_{t=1}^{T} M(p*,
  j_t) ≤ T·v*. The first inequality holds because the minimum over rows is at most
  the expectation over any distribution over rows. The last inequality follows by
  Eq. (120), i.e., M(p*, j) ≤ v* for all columns j. By definition of regret, cost(ALG)
  ≤ cost* + R(T) ≤ T·v* + R(T), so (1/T)·cost(ALG) ≤ v* + R(T)/T.
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/game-m]]'
- '[[concepts/cost-for-alg]]'
- '[[concepts/regret]]'
- '[[concepts/minimax-value]]'
- '[[concepts/sublinear-expected-regret]]'
- '[[concepts/minimax-strategy]]'
about_meta:
- target: '[[concepts/game-m]]'
  role: primary
  aspect: ''
- target: '[[concepts/cost-for-alg]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/minimax-value]]'
  role: primary
  aspect: ''
- target: '[[concepts/sublinear-expected-regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/minimax-strategy]]'
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

# Theorem 9.1

For an arbitrary adversary ADV it holds that

$\tfrac{1}{T}\,\mathtt{cost}(\mathtt{ALG})\leq v^{*}+R(T)/T.$

In particular, if we (only) posit sublinear expected regret, $\operatornamewithlimits{\mathbb{E}}[R(t)]=o(t)$, then the expected average cost $\tfrac{1}{T}\,\operatornamewithlimits{\mathbb{E}}[\mathtt{cost}(\mathtt{ALG})]$ is asymptotically upper-bounded by $v^{*}$.


## Proof

We have cost* = min_{rows i} cost(i) ≤ E_{i ~ p*}[cost(i)] = ∑_{t=1}^{T} M(p*, j_t) ≤ T·v*. The first inequality holds because the minimum over rows is at most the expectation over any distribution over rows. The last inequality follows by Eq. (120), i.e., M(p*, j) ≤ v* for all columns j. By definition of regret, cost(ALG) ≤ cost* + R(T) ≤ T·v* + R(T), so (1/T)·cost(ALG) ≤ v* + R(T)/T.
