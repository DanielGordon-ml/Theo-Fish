---
slug: introduction-to-multi-armed-bandits--s-shifting-regret-bound-via-exp4
label: S-shifting regret bound via Exp4
claim_type: theorem
statement: Consider S-shifting regret $R_S(T) = \mathtt{cost}(\mathtt{ALG}) - \min_{\text{$S$-shifting
  policies $\pi$}} \mathtt{cost}(\pi)$. Using $\mathtt{Exp4}$ and plugging $N \leq
  (KT)^S$ into Theorem 6.11, we obtain $\operatornamewithlimits{\mathbb{E}}[R_S(T)]
  = \tilde{O}(\sqrt{KST})$.
proof: ''
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/exp4]]'
- '[[concepts/number-of-arms-k]]'
- '[[concepts/time-horizon-t]]'
- '[[concepts/s-shifting-regret]]'
- '[[concepts/adversarial-bandits-with-expert-advice]]'
about_meta:
- target: '[[concepts/exp4]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-arms-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/time-horizon-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/s-shifting-regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/adversarial-bandits-with-expert-advice]]'
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

# S-shifting regret bound via Exp4

Consider S-shifting regret $R_S(T) = \mathtt{cost}(\mathtt{ALG}) - \min_{\text{$S$-shifting policies $\pi$}} \mathtt{cost}(\pi)$. Using $\mathtt{Exp4}$ and plugging $N \leq (KT)^S$ into Theorem 6.11, we obtain $\operatornamewithlimits{\mathbb{E}}[R_S(T)] = \tilde{O}(\sqrt{KST})$.
