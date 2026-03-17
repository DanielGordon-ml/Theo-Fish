---
slug: introduction-to-multi-armed-bandits--corollary-5-17
label: Corollary 5.17
claim_type: corollary
statement: 'Consider online learning with experts, with a randomized, oblivious adversary.
  Assume the costs are independent across rounds, and satisfy $\operatornamewithlimits{\mathbb{E}}\left[\,c_{t}(a)\,\right]\leq\mu$
  and $\text{Var}\left[\,c_{t}(a)\,\right]\leq\sigma^{2}$ for all rounds $t$ and all
  arms $a$, for some $\mu$ and $\sigma$ known to the algorithm. Then $\mathtt{Hedge}$
  with parameter $\epsilon=\sqrt{\ln{K}/(3T(\mu^{2}+\sigma^{2}))}$ has regret

  $$\operatornamewithlimits{\mathbb{E}}[\mathtt{cost}(\mathtt{ALG})-\mathtt{cost}^{*}]<2\sqrt{3}\cdot\sqrt{T(\mu^{2}+\sigma^{2})\ln{K}}.$$'
proof: 'For each round $t$ we have:

  $$\operatornamewithlimits{\mathbb{E}}\left[\,c_{t}(a)^{2}\,\right]=\text{Var}\left[\,c_{t}(a)\,\right]+\left(\,\operatornamewithlimits{\mathbb{E}}[c_{t}(a)]\,\right)^{2}\leq\sigma^{2}+\mu^{2}.$$

  $$\operatornamewithlimits{\mathbb{E}}[G_{t}]=\sum_{a\in[K]}p_{t}(a)\,\operatornamewithlimits{\mathbb{E}}\left[\,c_{t}(a)^{2}\,\right]\leq\sum_{a\in[K]}p_{t}(a)\,(\mu^{2}+\sigma^{2})=\mu^{2}+\sigma^{2}.$$

  Thus, Theorem 5.16 with $u=\mu^{2}+\sigma^{2}$ yields the result.'
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/regret]]'
- '[[concepts/hedge]]'
- '[[concepts/randomized-oblivious-adversary]]'
- '[[concepts/online-learning-with-experts]]'
- '[[concepts/variance]]'
about_meta:
- target: '[[concepts/regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/hedge]]'
  role: primary
  aspect: ''
- target: '[[concepts/randomized-oblivious-adversary]]'
  role: primary
  aspect: ''
- target: '[[concepts/online-learning-with-experts]]'
  role: primary
  aspect: ''
- target: '[[concepts/variance]]'
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

# Corollary 5.17

Consider online learning with experts, with a randomized, oblivious adversary. Assume the costs are independent across rounds, and satisfy $\operatornamewithlimits{\mathbb{E}}\left[\,c_{t}(a)\,\right]\leq\mu$ and $\text{Var}\left[\,c_{t}(a)\,\right]\leq\sigma^{2}$ for all rounds $t$ and all arms $a$, for some $\mu$ and $\sigma$ known to the algorithm. Then $\mathtt{Hedge}$ with parameter $\epsilon=\sqrt{\ln{K}/(3T(\mu^{2}+\sigma^{2}))}$ has regret
$$\operatornamewithlimits{\mathbb{E}}[\mathtt{cost}(\mathtt{ALG})-\mathtt{cost}^{*}]<2\sqrt{3}\cdot\sqrt{T(\mu^{2}+\sigma^{2})\ln{K}}.$$


## Proof

For each round $t$ we have:
$$\operatornamewithlimits{\mathbb{E}}\left[\,c_{t}(a)^{2}\,\right]=\text{Var}\left[\,c_{t}(a)\,\right]+\left(\,\operatornamewithlimits{\mathbb{E}}[c_{t}(a)]\,\right)^{2}\leq\sigma^{2}+\mu^{2}.$$
$$\operatornamewithlimits{\mathbb{E}}[G_{t}]=\sum_{a\in[K]}p_{t}(a)\,\operatornamewithlimits{\mathbb{E}}\left[\,c_{t}(a)^{2}\,\right]\leq\sum_{a\in[K]}p_{t}(a)\,(\mu^{2}+\sigma^{2})=\mu^{2}+\sigma^{2}.$$
Thus, Theorem 5.16 with $u=\mu^{2}+\sigma^{2}$ yields the result.
