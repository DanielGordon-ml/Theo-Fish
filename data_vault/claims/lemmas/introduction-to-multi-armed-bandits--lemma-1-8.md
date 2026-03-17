---
slug: introduction-to-multi-armed-bandits--lemma-1-8
label: Lemma 1.8
claim_type: lemma
statement: For two arms, Algorithm 3 achieves regret $\operatornamewithlimits{\mathbb{E}}\left[\,R(t)\,\right]\leq
  O\left(\,\sqrt{t\log T}\,\right)$ for each round $t\leq T$.
proof: 'Assume the clean event E defined as {∀a ∀t |μ̄_t(a) - μ(a)| ≤ r_t(a)} which
  holds with probability at least 1 - 2/T². Let t be the last round when the stopping
  rule was not invoked, i.e., when the confidence intervals of the two arms still
  overlap. Then Δ := |μ(a) - μ(a'')| ≤ 2(r_t(a) + r_t(a'')). Since the algorithm has
  been alternating the two arms before time t, we have n_t(a) = t/2 (up to floor and
  ceiling), which yields Δ ≤ 2(r_t(a) + r_t(a'')) ≤ 4√(2log(T)/⌊t/2⌋) = O(√(log(T)/t)).
  Then the total regret accumulated till round t is R(t) ≤ Δ × t ≤ O(t · √(log T /
  t)) = O(√(t log T)). Since we''ve chosen the best arm from then on, R(t) ≤ O(√(t
  log T)). To complete the analysis, we need to argue that the bad event E̅ contributes
  a negligible amount to regret: E[R(t)] = E[R(t) | clean event] × Pr[clean event]
  + E[R(t) | bad event] × Pr[bad event] ≤ E[R(t) | clean event] + t × O(T^{-2}) ≤
  O(√(t log T)).'
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/successive-elimination]]'
- '[[concepts/number-of-arms-k]]'
- '[[concepts/clean-event]]'
- '[[concepts/confidence-interval]]'
- '[[concepts/regret-r-t]]'
about_meta:
- target: '[[concepts/successive-elimination]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-arms-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/clean-event]]'
  role: primary
  aspect: ''
- target: '[[concepts/confidence-interval]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret-r-t]]'
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

# Lemma 1.8

For two arms, Algorithm 3 achieves regret $\operatornamewithlimits{\mathbb{E}}\left[\,R(t)\,\right]\leq O\left(\,\sqrt{t\log T}\,\right)$ for each round $t\leq T$.


## Proof

Assume the clean event E defined as {∀a ∀t |μ̄_t(a) - μ(a)| ≤ r_t(a)} which holds with probability at least 1 - 2/T². Let t be the last round when the stopping rule was not invoked, i.e., when the confidence intervals of the two arms still overlap. Then Δ := |μ(a) - μ(a')| ≤ 2(r_t(a) + r_t(a')). Since the algorithm has been alternating the two arms before time t, we have n_t(a) = t/2 (up to floor and ceiling), which yields Δ ≤ 2(r_t(a) + r_t(a')) ≤ 4√(2log(T)/⌊t/2⌋) = O(√(log(T)/t)). Then the total regret accumulated till round t is R(t) ≤ Δ × t ≤ O(t · √(log T / t)) = O(√(t log T)). Since we've chosen the best arm from then on, R(t) ≤ O(√(t log T)). To complete the analysis, we need to argue that the bad event E̅ contributes a negligible amount to regret: E[R(t)] = E[R(t) | clean event] × Pr[clean event] + E[R(t) | bad event] × Pr[bad event] ≤ E[R(t) | clean event] + t × O(T^{-2}) ≤ O(√(t log T)).
