---
slug: introduction-to-multi-armed-bandits--claim-7-15
label: Claim 7.15
claim_type: lemma
statement: Fix $v_t \in [0, U/d]^d$. There exists a random variable $v'_0 \in \mathbb{R}^d$
  such that (i) $v'_0$ and $v_0 + v_t$ have the same marginal distribution, and (ii)
  $\Pr[v'_0 \neq v_0] \leq \epsilon U$.
proof: Write $v_t = (v_{t,1}, v_{t,2}, \ldots, v_{t,d})$, and define $v'_0 \in \mathbb{R}^d$
  by setting its $j$-th coordinate to $g(v_{0,j}, v_{t,j})$ from Claim 7.16, for each
  coordinate $j$. By Claim 7.16, each coordinate $g(v_{0,j}, v_{t,j})$ has the same
  distribution as $v_{0,j} + v_{t,j}$, so $v'_0$ and $v_0 + v_t$ have the same marginal
  distribution. Moreover, by a union bound over $d$ coordinates, $\Pr[v'_0 \neq v_0]
  \leq \sum_{j=1}^{d} \Pr[g(v_{0,j}, v_{t,j}) \neq v_{0,j}] \leq d \cdot \frac{\epsilon
  U}{2d} = \frac{\epsilon U}{2} \leq \epsilon U$.
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/perturbation-distribution]]'
- '[[concepts/follow-the-perturbed-leader-ftpl]]'
about_meta:
- target: '[[concepts/perturbation-distribution]]'
  role: primary
  aspect: ''
- target: '[[concepts/follow-the-perturbed-leader-ftpl]]'
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

# Claim 7.15

Fix $v_t \in [0, U/d]^d$. There exists a random variable $v'_0 \in \mathbb{R}^d$ such that (i) $v'_0$ and $v_0 + v_t$ have the same marginal distribution, and (ii) $\Pr[v'_0 \neq v_0] \leq \epsilon U$.


## Proof

Write $v_t = (v_{t,1}, v_{t,2}, \ldots, v_{t,d})$, and define $v'_0 \in \mathbb{R}^d$ by setting its $j$-th coordinate to $g(v_{0,j}, v_{t,j})$ from Claim 7.16, for each coordinate $j$. By Claim 7.16, each coordinate $g(v_{0,j}, v_{t,j})$ has the same distribution as $v_{0,j} + v_{t,j}$, so $v'_0$ and $v_0 + v_t$ have the same marginal distribution. Moreover, by a union bound over $d$ coordinates, $\Pr[v'_0 \neq v_0] \leq \sum_{j=1}^{d} \Pr[g(v_{0,j}, v_{t,j}) \neq v_{0,j}] \leq d \cdot \frac{\epsilon U}{2d} = \frac{\epsilon U}{2} \leq \epsilon U$.
