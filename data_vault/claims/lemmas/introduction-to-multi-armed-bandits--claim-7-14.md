---
slug: introduction-to-multi-armed-bandits--claim-7-14
label: Claim 7.14
claim_type: lemma
statement: 'For any vectors $v \in \mathbb{R}^d$ and $v_t \in [0, U/d]^d$, and any
  function $f: \mathbb{R}^d \rightarrow [0, R]$, $\left| \operatorname{\mathbb{E}}_{v_0
  \sim \mathcal{D}} \left[ f(v_0 + v) - f(v_0 + v + v_t) \right] \right| \leq \epsilon
  U R.$'
proof: This follows from Claim 7.15. By Claim 7.15, there exists a random variable
  $v'_0$ such that $v'_0$ and $v_0 + v_t$ have the same marginal distribution, and
  $\Pr[v'_0 \neq v_0] \leq \epsilon U$. Then $\left| \operatorname{\mathbb{E}}\left[
  f(v_0 + v) - f(v_0 + v + v_t) \right] \right| = \left| \operatorname{\mathbb{E}}\left[
  f(v_0 + v) - f(v'_0 + v) \right] \right| \leq \Pr[v'_0 \neq v_0] \cdot R = \epsilon
  U R.$
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/follow-the-perturbed-leader-ftpl]]'
- '[[concepts/perturbation-distribution]]'
about_meta:
- target: '[[concepts/follow-the-perturbed-leader-ftpl]]'
  role: primary
  aspect: ''
- target: '[[concepts/perturbation-distribution]]'
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

# Claim 7.14

For any vectors $v \in \mathbb{R}^d$ and $v_t \in [0, U/d]^d$, and any function $f: \mathbb{R}^d \rightarrow [0, R]$, $\left| \operatorname{\mathbb{E}}_{v_0 \sim \mathcal{D}} \left[ f(v_0 + v) - f(v_0 + v + v_t) \right] \right| \leq \epsilon U R.$


## Proof

This follows from Claim 7.15. By Claim 7.15, there exists a random variable $v'_0$ such that $v'_0$ and $v_0 + v_t$ have the same marginal distribution, and $\Pr[v'_0 \neq v_0] \leq \epsilon U$. Then $\left| \operatorname{\mathbb{E}}\left[ f(v_0 + v) - f(v_0 + v + v_t) \right] \right| = \left| \operatorname{\mathbb{E}}\left[ f(v_0 + v) - f(v'_0 + v) \right] \right| \leq \Pr[v'_0 \neq v_0] \cdot R = \epsilon U R.$
