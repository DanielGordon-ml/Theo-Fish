---
slug: introduction-to-multi-armed-bandits--lemma-3-7
label: Lemma 3.7
claim_type: lemma
statement: For each round $t$, arms $a_{t}$ and $\tilde{a}_{t}$ are identically distributed
  given $H_{t}$.
proof: 'Fix a feasible $t$-history $H$. For each arm $a$ we have:


  $\Pr[\tilde{a}_{t}=a\mid H_{t-1}=H] = \mathbb{P}_{H}(a^{*}=a)$ (by definition of
  $\tilde{a}_{t}$) $= p_{t}(a\mid H)$ (by definition of $p_{t}$). $\qed$'
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/feasible-t-history]]'
- '[[concepts/posterior-distribution]]'
- '[[concepts/bayesian-bandits]]'
- '[[concepts/thompson-sampling]]'
about_meta:
- target: '[[concepts/feasible-t-history]]'
  role: primary
  aspect: ''
- target: '[[concepts/posterior-distribution]]'
  role: primary
  aspect: ''
- target: '[[concepts/bayesian-bandits]]'
  role: primary
  aspect: ''
- target: '[[concepts/thompson-sampling]]'
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

# Lemma 3.7

For each round $t$, arms $a_{t}$ and $\tilde{a}_{t}$ are identically distributed given $H_{t}$.


## Proof

Fix a feasible $t$-history $H$. For each arm $a$ we have:

$\Pr[\tilde{a}_{t}=a\mid H_{t-1}=H] = \mathbb{P}_{H}(a^{*}=a)$ (by definition of $\tilde{a}_{t}$) $= p_{t}(a\mid H)$ (by definition of $p_{t}$). $\qed$
