---
slug: introduction-to-multi-armed-bandits--theorem-5-14
label: Theorem 5.14
claim_type: theorem
statement: 'Assume all costs are at most $1$. Consider an adaptive adversary such
  that $\mathtt{cost}^{*}\leq uT$ for some known number $u$; trivially, $u=1$. Then
  $\mathtt{Hedge}$ with parameter $\epsilon=\sqrt{\tfrac{\ln K}{uT}}$ satisfies

  $$\operatornamewithlimits{\mathbb{E}}[\mathtt{cost}(\mathtt{ALG})-\mathtt{cost}^{*}]<2\cdot\sqrt{uT\ln{K}}.$$'
proof: 'Using the first-order variant of Eq. (79) with $\alpha=\epsilon$, $\beta=0$,
  $u=1$ (costs at most 1), we obtain from Eq. (83):

  $$\operatornamewithlimits{\mathbb{E}}[\mathtt{cost}(\mathtt{ALG})]<\tfrac{\ln{K}}{\epsilon}+\underbrace{\tfrac{1}{\epsilon}\ln(\tfrac{1}{1-\epsilon})}_{\leq
  1+\epsilon \text{ if } \epsilon\in(0,\nicefrac{1}{2})}\operatornamewithlimits{\mathbb{E}}[\mathtt{cost}^{*}].$$

  $$\operatornamewithlimits{\mathbb{E}}[\mathtt{cost}(\mathtt{ALG})-\mathtt{cost}^{*}]<\frac{\ln{K}}{\epsilon}+\epsilon\;\operatornamewithlimits{\mathbb{E}}[\mathtt{cost}^{*}].$$

  Substituting $\epsilon=\sqrt{\tfrac{\ln K}{uT}}$ and using $\operatornamewithlimits{\mathbb{E}}[\mathtt{cost}^{*}]\leq
  uT$, we get $\frac{\ln K}{\epsilon}+\epsilon\cdot uT = \sqrt{uT\ln K}+\sqrt{uT\ln
  K}=2\sqrt{uT\ln K}$.'
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/bounded-per-round-costs]]'
- '[[concepts/regret]]'
- '[[concepts/online-learning-with-experts]]'
- '[[concepts/hedge]]'
- '[[concepts/adaptive-adversary]]'
about_meta:
- target: '[[concepts/bounded-per-round-costs]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/online-learning-with-experts]]'
  role: primary
  aspect: ''
- target: '[[concepts/hedge]]'
  role: primary
  aspect: ''
- target: '[[concepts/adaptive-adversary]]'
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

# Theorem 5.14

Assume all costs are at most $1$. Consider an adaptive adversary such that $\mathtt{cost}^{*}\leq uT$ for some known number $u$; trivially, $u=1$. Then $\mathtt{Hedge}$ with parameter $\epsilon=\sqrt{\tfrac{\ln K}{uT}}$ satisfies
$$\operatornamewithlimits{\mathbb{E}}[\mathtt{cost}(\mathtt{ALG})-\mathtt{cost}^{*}]<2\cdot\sqrt{uT\ln{K}}.$$


## Proof

Using the first-order variant of Eq. (79) with $\alpha=\epsilon$, $\beta=0$, $u=1$ (costs at most 1), we obtain from Eq. (83):
$$\operatornamewithlimits{\mathbb{E}}[\mathtt{cost}(\mathtt{ALG})]<\tfrac{\ln{K}}{\epsilon}+\underbrace{\tfrac{1}{\epsilon}\ln(\tfrac{1}{1-\epsilon})}_{\leq 1+\epsilon \text{ if } \epsilon\in(0,\nicefrac{1}{2})}\operatornamewithlimits{\mathbb{E}}[\mathtt{cost}^{*}].$$
$$\operatornamewithlimits{\mathbb{E}}[\mathtt{cost}(\mathtt{ALG})-\mathtt{cost}^{*}]<\frac{\ln{K}}{\epsilon}+\epsilon\;\operatornamewithlimits{\mathbb{E}}[\mathtt{cost}^{*}].$$
Substituting $\epsilon=\sqrt{\tfrac{\ln K}{uT}}$ and using $\operatornamewithlimits{\mathbb{E}}[\mathtt{cost}^{*}]\leq uT$, we get $\frac{\ln K}{\epsilon}+\epsilon\cdot uT = \sqrt{uT\ln K}+\sqrt{uT\ln K}=2\sqrt{uT\ln K}$.
