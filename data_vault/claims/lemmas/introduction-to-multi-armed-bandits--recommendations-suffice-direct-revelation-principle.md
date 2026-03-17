---
slug: introduction-to-multi-armed-bandits--recommendations-suffice-direct-revelation-principle
label: Recommendations suffice (Direct Revelation Principle)
claim_type: lemma
statement: Given an algorithm $\mathtt{ALG}$ that sends arbitrary messages $\sigma_t$
  including a recommended arm $\mathtt{rec}_t \in [K]$ and satisfies the BIC constraint
  $\mathtt{rec}_{t}\in\operatorname{argmax}_{a\in[K]}\operatorname{\mathbb{E}}[\mu_{a}\mid\sigma_{t},\mathcal{E}_{t-1}]$
  for all $t\in[T]$, consider another algorithm $\mathtt{ALG}'$ which only reveals
  recommendation $\mathtt{rec}_t$ in each round $t$. Then $\mathtt{ALG}'$ is BIC,
  as per (159).
proof: Fix round $t$ and arm $a$ such that $\Pr[\mathtt{rec}_{t}=a, \mathcal{E}_{t-1}]>0$.
  Then $\operatorname{\mathbb{E}}[\mu_{a}-\mu_{a'}\mid\sigma_{t}, \mathtt{rec}_{t}=a,
  \mathcal{E}_{t-1}]\geq 0$ for all $a'\in[K]$. We obtain (159) by integrating out
  the message $\sigma_{t}$, i.e., by taking conditional expectation of both sides
  given $\{\mathtt{rec}_{t}=a, \mathcal{E}_{t-1}\}$.
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/signal]]'
- '[[concepts/bic-bayesian-incentive-compatible]]'
- '[[concepts/incentivized-exploration]]'
- '[[concepts/bic-constraint]]'
about_meta:
- target: '[[concepts/signal]]'
  role: primary
  aspect: ''
- target: '[[concepts/bic-bayesian-incentive-compatible]]'
  role: primary
  aspect: ''
- target: '[[concepts/incentivized-exploration]]'
  role: primary
  aspect: ''
- target: '[[concepts/bic-constraint]]'
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

# Recommendations suffice (Direct Revelation Principle)

Given an algorithm $\mathtt{ALG}$ that sends arbitrary messages $\sigma_t$ including a recommended arm $\mathtt{rec}_t \in [K]$ and satisfies the BIC constraint $\mathtt{rec}_{t}\in\operatorname{argmax}_{a\in[K]}\operatorname{\mathbb{E}}[\mu_{a}\mid\sigma_{t},\mathcal{E}_{t-1}]$ for all $t\in[T]$, consider another algorithm $\mathtt{ALG}'$ which only reveals recommendation $\mathtt{rec}_t$ in each round $t$. Then $\mathtt{ALG}'$ is BIC, as per (159).


## Proof

Fix round $t$ and arm $a$ such that $\Pr[\mathtt{rec}_{t}=a, \mathcal{E}_{t-1}]>0$. Then $\operatorname{\mathbb{E}}[\mu_{a}-\mu_{a'}\mid\sigma_{t}, \mathtt{rec}_{t}=a, \mathcal{E}_{t-1}]\geq 0$ for all $a'\in[K]$. We obtain (159) by integrating out the message $\sigma_{t}$, i.e., by taking conditional expectation of both sides given $\{\mathtt{rec}_{t}=a, \mathcal{E}_{t-1}\}$.
