---
slug: introduction-to-multi-armed-bandits--theorem-6-1
label: Theorem 6.1
claim_type: theorem
statement: 'Consider online learning with $N$ experts and $T$ rounds. Consider an
  adaptive adversary and regret $R(T)$ relative to the best-observed expert. Suppose
  in any run of $\mathtt{Hedge}$, with any parameter $\epsilon>0$, it holds that

  $\sum_{t\in[T]}\;\operatorname{\mathbb{E}}[G_{t}]\leq uT$

  for some known $u>0$,

  where

  $G_{t}=\sum_{\text{experts $e$}}p_{t}(e)\;c_{t}^{2}(e)$.

  Then

  $\operatorname{\mathbb{E}}[R(T)]\leq 2\sqrt{3}\cdot\sqrt{uT\log N}\qquad\text{provided
  that}\quad\epsilon=\epsilon_{u}:=\sqrt{\tfrac{\ln N}{3uT}}.$'
proof: ''
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/number-of-experts-n]]'
- '[[concepts/probability-distribution-p-t]]'
- '[[concepts/u]]'
- '[[concepts/learning-rate-parameter-epsilon]]'
- '[[concepts/number-of-rounds-t]]'
- '[[concepts/regret]]'
- '[[concepts/g-t]]'
- '[[concepts/hedge]]'
- '[[concepts/adaptive-adversary]]'
- '[[concepts/online-learning-with-experts]]'
about_meta:
- target: '[[concepts/number-of-experts-n]]'
  role: primary
  aspect: ''
- target: '[[concepts/probability-distribution-p-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/u]]'
  role: primary
  aspect: ''
- target: '[[concepts/learning-rate-parameter-epsilon]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-rounds-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/g-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/hedge]]'
  role: primary
  aspect: ''
- target: '[[concepts/adaptive-adversary]]'
  role: primary
  aspect: ''
- target: '[[concepts/online-learning-with-experts]]'
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

# Theorem 6.1

Consider online learning with $N$ experts and $T$ rounds. Consider an adaptive adversary and regret $R(T)$ relative to the best-observed expert. Suppose in any run of $\mathtt{Hedge}$, with any parameter $\epsilon>0$, it holds that
$\sum_{t\in[T]}\;\operatorname{\mathbb{E}}[G_{t}]\leq uT$
for some known $u>0$,
where
$G_{t}=\sum_{\text{experts $e$}}p_{t}(e)\;c_{t}^{2}(e)$.
Then
$\operatorname{\mathbb{E}}[R(T)]\leq 2\sqrt{3}\cdot\sqrt{uT\log N}\qquad\text{provided that}\quad\epsilon=\epsilon_{u}:=\sqrt{\tfrac{\ln N}{3uT}}.$
