---
slug: introduction-to-multi-armed-bandits--counterfactual-regret-against-memory-restricted-adversaries-dekel-et-al-2012
label: Counterfactual regret against memory-restricted adversaries (Dekel et al. 2012)
claim_type: theorem
statement: 'One can obtain $\tilde{O}(mK^{1/3}T^{2/3})$ counterfactual regret for
  all $m < T^{2/3}$, without knowing $m$. This can be achieved using a simple ''batching''
  trick: use some bandit algorithm $\mathtt{ALG}$ so that one round in the execution
  of $\mathtt{ALG}$ corresponds to a batch of $\tau$ consecutive rounds in the original
  problems.'
proof: ''
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/adaptive-adversary]]'
- '[[concepts/counterfactual-regret]]'
- '[[concepts/adversarial-bandits-problem]]'
about_meta:
- target: '[[concepts/adaptive-adversary]]'
  role: primary
  aspect: ''
- target: '[[concepts/counterfactual-regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/adversarial-bandits-problem]]'
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

# Counterfactual regret against memory-restricted adversaries (Dekel et al. 2012)

One can obtain $\tilde{O}(mK^{1/3}T^{2/3})$ counterfactual regret for all $m < T^{2/3}$, without knowing $m$. This can be achieved using a simple 'batching' trick: use some bandit algorithm $\mathtt{ALG}$ so that one round in the execution of $\mathtt{ALG}$ corresponds to a batch of $\tau$ consecutive rounds in the original problems.
