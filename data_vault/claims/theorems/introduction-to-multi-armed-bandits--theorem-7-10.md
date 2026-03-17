---
slug: introduction-to-multi-armed-bandits--theorem-7-10
label: Theorem 7.10
claim_type: theorem
statement: Assume that $v_t \in [0, U/d]^d$ for some known parameter $U$. Algorithm
  $\mathtt{FTPL}$ achieves regret $\operatorname{\mathbb{E}}[R(T)] \leq 2U \cdot \sqrt{dT}$.
  The running time in each round is polynomial in $d$ plus one call to the oracle.
proof: The proof follows from Lemma 7.12. By Lemma 7.12(i), $\mathtt{cost}(\mathtt{BTPL})
  \leq \mathtt{OPT} + \frac{d}{\epsilon}$. By Lemma 7.12(ii), $\operatorname{\mathbb{E}}[\mathtt{cost}(\mathtt{FTPL})]
  \leq \operatorname{\mathbb{E}}[\mathtt{cost}(\mathtt{BTPL})] + \epsilon \cdot U^2
  \cdot T$. Combining these, $\operatorname{\mathbb{E}}[R(T)] \leq \frac{d}{\epsilon}
  + \epsilon U^2 T$. Choosing $\epsilon = \frac{\sqrt{d}}{U\sqrt{T}}$ gives $\operatorname{\mathbb{E}}[R(T)]
  \leq \frac{d}{\sqrt{d}/(U\sqrt{T})} + \frac{\sqrt{d}}{U\sqrt{T}} \cdot U^2 \cdot
  T = U\sqrt{dT} + U\sqrt{dT} = 2U\sqrt{dT}$.
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/regret]]'
- '[[concepts/optimization-oracle]]'
- '[[concepts/follow-the-perturbed-leader-ftpl]]'
- '[[concepts/online-linear-optimization]]'
about_meta:
- target: '[[concepts/regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/optimization-oracle]]'
  role: primary
  aspect: ''
- target: '[[concepts/follow-the-perturbed-leader-ftpl]]'
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

# Theorem 7.10

Assume that $v_t \in [0, U/d]^d$ for some known parameter $U$. Algorithm $\mathtt{FTPL}$ achieves regret $\operatorname{\mathbb{E}}[R(T)] \leq 2U \cdot \sqrt{dT}$. The running time in each round is polynomial in $d$ plus one call to the oracle.


## Proof

The proof follows from Lemma 7.12. By Lemma 7.12(i), $\mathtt{cost}(\mathtt{BTPL}) \leq \mathtt{OPT} + \frac{d}{\epsilon}$. By Lemma 7.12(ii), $\operatorname{\mathbb{E}}[\mathtt{cost}(\mathtt{FTPL})] \leq \operatorname{\mathbb{E}}[\mathtt{cost}(\mathtt{BTPL})] + \epsilon \cdot U^2 \cdot T$. Combining these, $\operatorname{\mathbb{E}}[R(T)] \leq \frac{d}{\epsilon} + \epsilon U^2 T$. Choosing $\epsilon = \frac{\sqrt{d}}{U\sqrt{T}}$ gives $\operatorname{\mathbb{E}}[R(T)] \leq \frac{d}{\sqrt{d}/(U\sqrt{T})} + \frac{\sqrt{d}}{U\sqrt{T}} \cdot U^2 \cdot T = U\sqrt{dT} + U\sqrt{dT} = 2U\sqrt{dT}$.
