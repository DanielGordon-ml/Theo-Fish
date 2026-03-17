---
slug: introduction-to-multi-armed-bandits--lemma-7-12
label: Lemma 7.12
claim_type: lemma
statement: 'For each value of parameter $\epsilon > 0$,

  (i) $\mathtt{cost}(\mathtt{BTPL}) \leq \mathtt{OPT} + \frac{d}{\epsilon}$

  (ii) $\operatorname{\mathbb{E}}[\mathtt{cost}(\mathtt{FTPL})] \leq \operatorname{\mathbb{E}}[\mathtt{cost}(\mathtt{BTPL})]
  + \epsilon \cdot U^2 \cdot T$'
proof: 'Part (i): By definition of the oracle $M$, $v \cdot M(v) \leq v \cdot a$ for
  any cost vector $v$ and feasible action $a$. Then $\mathtt{cost}(\mathtt{BTPL})
  + v_0 \cdot M(v_0) = \sum_{t=0}^{T} v_t \cdot M(v_{0:t}) \leq v_{0:T} \cdot M(v_{0:T})$
  (by Claim 7.13) $\leq v_{0:T} \cdot M(v_{1:T})$ (by (97) with $a = M(v_{1:T})$)
  $= v_0 \cdot M(v_{1:T}) + v_{1:T} \cdot M(v_{1:T})$. Subtracting $v_0 \cdot M(v_0)$
  from both sides: $\mathtt{cost}(\mathtt{BTPL}) - \mathtt{OPT} \leq v_0 \cdot [M(v_{1:T})
  - M(v_0)] \leq \frac{d}{\epsilon}$ since $v_0 \in [-1/\epsilon, 1/\epsilon]^d$ and
  $M(v_{1:T}) - M(v_0) \in [-1,1]^d$.


  Part (ii): We prove round by round that $\operatorname{\mathbb{E}}[v_t \cdot M(v_{0:t-1})]
  \leq \operatorname{\mathbb{E}}[v_t \cdot M(v_{0:t})] + \epsilon U^2$, which follows
  from Claim 7.14 applied with $f(u) = v_t \cdot M(u)$, $v = v_{1:t-1}$, and $R =
  U$. Summing over all $T$ rounds gives the result.'
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/be-the-perturbed-leader-algorithm]]'
- '[[concepts/follow-the-perturbed-leader-ftpl]]'
- '[[concepts/optimal-cost]]'
- '[[concepts/online-linear-optimization]]'
about_meta:
- target: '[[concepts/be-the-perturbed-leader-algorithm]]'
  role: primary
  aspect: ''
- target: '[[concepts/follow-the-perturbed-leader-ftpl]]'
  role: primary
  aspect: ''
- target: '[[concepts/optimal-cost]]'
  role: primary
  aspect: ''
- target: '[[concepts/online-linear-optimization]]'
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

# Lemma 7.12

For each value of parameter $\epsilon > 0$,
(i) $\mathtt{cost}(\mathtt{BTPL}) \leq \mathtt{OPT} + \frac{d}{\epsilon}$
(ii) $\operatorname{\mathbb{E}}[\mathtt{cost}(\mathtt{FTPL})] \leq \operatorname{\mathbb{E}}[\mathtt{cost}(\mathtt{BTPL})] + \epsilon \cdot U^2 \cdot T$


## Proof

Part (i): By definition of the oracle $M$, $v \cdot M(v) \leq v \cdot a$ for any cost vector $v$ and feasible action $a$. Then $\mathtt{cost}(\mathtt{BTPL}) + v_0 \cdot M(v_0) = \sum_{t=0}^{T} v_t \cdot M(v_{0:t}) \leq v_{0:T} \cdot M(v_{0:T})$ (by Claim 7.13) $\leq v_{0:T} \cdot M(v_{1:T})$ (by (97) with $a = M(v_{1:T})$) $= v_0 \cdot M(v_{1:T}) + v_{1:T} \cdot M(v_{1:T})$. Subtracting $v_0 \cdot M(v_0)$ from both sides: $\mathtt{cost}(\mathtt{BTPL}) - \mathtt{OPT} \leq v_0 \cdot [M(v_{1:T}) - M(v_0)] \leq \frac{d}{\epsilon}$ since $v_0 \in [-1/\epsilon, 1/\epsilon]^d$ and $M(v_{1:T}) - M(v_0) \in [-1,1]^d$.

Part (ii): We prove round by round that $\operatorname{\mathbb{E}}[v_t \cdot M(v_{0:t-1})] \leq \operatorname{\mathbb{E}}[v_t \cdot M(v_{0:t})] + \epsilon U^2$, which follows from Claim 7.14 applied with $f(u) = v_t \cdot M(u)$, $v = v_{1:t-1}$, and $R = U$. Summing over all $T$ rounds gives the result.
