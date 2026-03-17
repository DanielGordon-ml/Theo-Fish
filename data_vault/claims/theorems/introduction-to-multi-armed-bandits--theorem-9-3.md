---
slug: introduction-to-multi-armed-bandits--theorem-9-3
label: Theorem 9.3
claim_type: theorem
statement: 'If ADV is the best-response adversary, as in (122), then


  $M(\,\operatornamewithlimits{\mathbb{E}}[\bar{\imath}],q\,)\leq\tfrac{1}{T}\,\operatornamewithlimits{\mathbb{E}}[\mathtt{cost}(\mathtt{ALG})]\leq
  v^{*}+\operatornamewithlimits{\mathbb{E}}[R(T)]/T\qquad\forall q\in\Delta_{\mathtt{cols}}.$


  Thus, if $\operatornamewithlimits{\mathbb{E}}[R(t)]=o(t)$ then ALG''s expected average
  play $\operatornamewithlimits{\mathbb{E}}[\bar{\imath}]$ asymptotically achieves
  the minimax property of $p^{*}$, as expressed by Eq. (120).'
proof: 'We argue that the expected average play E[ī] performs well against an arbitrary
  column j:


  E[M(i_t, j)] = E[E[M(i_t, j) | H_t]] ≤ E[E[M(i_t, j_t) | H_t]] (by best response)
  = E[M(i_t, j_t)]


  M(E[ī], j) = (1/T) ∑_{t=1}^{T} E[M(i_t, j)] (by linearity of M(·,·)) ≤ (1/T) ∑_{t=1}^{T}
  E[M(i_t, j_t)] = (1/T)·E[cost(ALG)].


  Plugging this into Theorem 9.1 yields the result.'
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/minimax-value]]'
- '[[concepts/game-m]]'
- '[[concepts/minimax-strategy]]'
- '[[concepts/sublinear-expected-regret]]'
- '[[concepts/best-response-adversary]]'
- '[[concepts/d-rows]]'
- '[[concepts/average-play]]'
- '[[concepts/d-cols]]'
- '[[concepts/cost-for-alg]]'
- '[[concepts/regret]]'
about_meta:
- target: '[[concepts/minimax-value]]'
  role: primary
  aspect: ''
- target: '[[concepts/game-m]]'
  role: primary
  aspect: ''
- target: '[[concepts/minimax-strategy]]'
  role: primary
  aspect: ''
- target: '[[concepts/sublinear-expected-regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/best-response-adversary]]'
  role: primary
  aspect: ''
- target: '[[concepts/d-rows]]'
  role: primary
  aspect: ''
- target: '[[concepts/average-play]]'
  role: primary
  aspect: ''
- target: '[[concepts/d-cols]]'
  role: primary
  aspect: ''
- target: '[[concepts/cost-for-alg]]'
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

# Theorem 9.3

If ADV is the best-response adversary, as in (122), then

$M(\,\operatornamewithlimits{\mathbb{E}}[\bar{\imath}],q\,)\leq\tfrac{1}{T}\,\operatornamewithlimits{\mathbb{E}}[\mathtt{cost}(\mathtt{ALG})]\leq v^{*}+\operatornamewithlimits{\mathbb{E}}[R(T)]/T\qquad\forall q\in\Delta_{\mathtt{cols}}.$

Thus, if $\operatornamewithlimits{\mathbb{E}}[R(t)]=o(t)$ then ALG's expected average play $\operatornamewithlimits{\mathbb{E}}[\bar{\imath}]$ asymptotically achieves the minimax property of $p^{*}$, as expressed by Eq. (120).


## Proof

We argue that the expected average play E[ī] performs well against an arbitrary column j:

E[M(i_t, j)] = E[E[M(i_t, j) | H_t]] ≤ E[E[M(i_t, j_t) | H_t]] (by best response) = E[M(i_t, j_t)]

M(E[ī], j) = (1/T) ∑_{t=1}^{T} E[M(i_t, j)] (by linearity of M(·,·)) ≤ (1/T) ∑_{t=1}^{T} E[M(i_t, j_t)] = (1/T)·E[cost(ALG)].

Plugging this into Theorem 9.1 yields the result.
