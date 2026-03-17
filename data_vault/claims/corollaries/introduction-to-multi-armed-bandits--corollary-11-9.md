---
slug: introduction-to-multi-armed-bandits--corollary-11-9
label: Corollary 11.9
claim_type: corollary
statement: Consider independent priors. Assume that each arm's prior has a positive
  density, i.e., for each arm $a$, the prior on $\mu_{a}\in[0,1]$ has probability
  density function that is strictly positive on $[0,1]$. Then $\mathtt{GREEDY}$ suffers
  Bayesian regret at least $c_{\mathcal{P}}\cdot T$, where the constant $c_{\mathcal{P}}>0$
  depends only on the prior $\mathcal{P}$.
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/independent-priors]]'
- '[[concepts/positive-density-prior]]'
- '[[concepts/greedy]]'
- '[[concepts/constant-c-p]]'
- '[[concepts/bayesian-regret]]'
about_meta:
- target: '[[concepts/independent-priors]]'
  role: primary
  aspect: ''
- target: '[[concepts/positive-density-prior]]'
  role: primary
  aspect: ''
- target: '[[concepts/greedy]]'
  role: primary
  aspect: ''
- target: '[[concepts/constant-c-p]]'
  role: primary
  aspect: ''
- target: '[[concepts/bayesian-regret]]'
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

# Corollary 11.9

Consider independent priors. Assume that each arm's prior has a positive density, i.e., for each arm $a$, the prior on $\mu_{a}\in[0,1]$ has probability density function that is strictly positive on $[0,1]$. Then $\mathtt{GREEDY}$ suffers Bayesian regret at least $c_{\mathcal{P}}\cdot T$, where the constant $c_{\mathcal{P}}>0$ depends only on the prior $\mathcal{P}$.
