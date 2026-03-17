---
slug: introduction-to-multi-armed-bandits--lemma-10-11
label: Lemma 10.11
claim_type: lemma
statement: 'For each round $\tau\in[T]$, the average play $(\bar{a}_{\tau},\bar{\imath}_{\tau})$
  forms a $\delta_{\tau}$-approximate Nash equilibrium for the expected Lagrange game
  defined by $\mathcal{L}$, where


  $\tau\cdot\delta_{\tau}=R_{1}(\tau)+R_{2}(\tau)+\mathtt{err}_{\tau},\text{ with
  error term }\textstyle\mathtt{err}_{\tau}:=\left|\sum_{t\in[\tau]}\mathcal{L}_{t}(i_{t},j_{t})-\mathcal{L}(i_{t},j_{t})\right|.$'
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/repeated-lagrange-game]]'
- '[[concepts/adversarial-regret]]'
- '[[concepts/lagrange-game]]'
- '[[concepts/approximate-nash-equilibrium]]'
about_meta:
- target: '[[concepts/repeated-lagrange-game]]'
  role: primary
  aspect: ''
- target: '[[concepts/adversarial-regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/lagrange-game]]'
  role: primary
  aspect: ''
- target: '[[concepts/approximate-nash-equilibrium]]'
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

# Lemma 10.11

For each round $\tau\in[T]$, the average play $(\bar{a}_{\tau},\bar{\imath}_{\tau})$ forms a $\delta_{\tau}$-approximate Nash equilibrium for the expected Lagrange game defined by $\mathcal{L}$, where

$\tau\cdot\delta_{\tau}=R_{1}(\tau)+R_{2}(\tau)+\mathtt{err}_{\tau},\text{ with error term }\textstyle\mathtt{err}_{\tau}:=\left|\sum_{t\in[\tau]}\mathcal{L}_{t}(i_{t},j_{t})-\mathcal{L}(i_{t},j_{t})\right|.$
