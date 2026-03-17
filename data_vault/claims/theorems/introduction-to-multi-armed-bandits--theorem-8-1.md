---
slug: introduction-to-multi-armed-bandits--theorem-8-1
label: Theorem 8.1
claim_type: theorem
statement: Algorithm 1 has regret $\operatornamewithlimits{\mathbb{E}}[R(T)]=O(\sqrt{KT\,|\mathcal{X}|\,\ln
  T})$, provided that the bandit algorithm $\mathtt{ALG}$ has regret $\operatornamewithlimits{\mathbb{E}}[R_{\mathtt{ALG}}(T)]=O(\sqrt{KT\log
  T})$.
proof: Let $n_{x}$ be the number of rounds in which context $x$ arrives. Regret accumulated
  in such rounds, denoted $R_{x}(T)$, satisfies $\operatornamewithlimits{\mathbb{E}}[R_{x}(T)]=O(\sqrt{Kn_{x}\ln
  T})$. The total regret (from all contexts) is $\operatornamewithlimits{\mathbb{E}}[R(T)]=\textstyle\sum_{x\in\mathcal{X}}\operatornamewithlimits{\mathbb{E}}[R_{x}(T)]=\sum_{x\in\mathcal{X}}O(\sqrt{Kn_{x}\,\ln
  T})\leq O(\sqrt{KT\,|\mathcal{X}|\,\ln T}).$
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/contextual-bandit-problem]]'
- '[[concepts/number-of-contexts]]'
- '[[concepts/regret-r-t]]'
- '[[concepts/number-of-arms-k]]'
- '[[concepts/ucb1-algorithm]]'
- '[[concepts/expected-regret-e-r-t]]'
- '[[concepts/time-horizon-t]]'
about_meta:
- target: '[[concepts/contextual-bandit-problem]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-contexts]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret-r-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-arms-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/ucb1-algorithm]]'
  role: primary
  aspect: ''
- target: '[[concepts/expected-regret-e-r-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/time-horizon-t]]'
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

# Theorem 8.1

Algorithm 1 has regret $\operatornamewithlimits{\mathbb{E}}[R(T)]=O(\sqrt{KT\,|\mathcal{X}|\,\ln T})$, provided that the bandit algorithm $\mathtt{ALG}$ has regret $\operatornamewithlimits{\mathbb{E}}[R_{\mathtt{ALG}}(T)]=O(\sqrt{KT\log T})$.


## Proof

Let $n_{x}$ be the number of rounds in which context $x$ arrives. Regret accumulated in such rounds, denoted $R_{x}(T)$, satisfies $\operatornamewithlimits{\mathbb{E}}[R_{x}(T)]=O(\sqrt{Kn_{x}\ln T})$. The total regret (from all contexts) is $\operatornamewithlimits{\mathbb{E}}[R(T)]=\textstyle\sum_{x\in\mathcal{X}}\operatornamewithlimits{\mathbb{E}}[R_{x}(T)]=\sum_{x\in\mathcal{X}}O(\sqrt{Kn_{x}\,\ln T})\leq O(\sqrt{KT\,|\mathcal{X}|\,\ln T}).$
