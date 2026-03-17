---
slug: introduction-to-multi-armed-bandits--lower-bound-for-adversarial-bandits-with-expert-advice-eq-87
label: Lower bound for adversarial bandits with expert advice (Eq. 87)
claim_type: theorem
statement: 'For any given triple of parameters K, T, N, there is a lower bound on
  regret for the adversarial bandits with expert advice problem:

  $$\operatornamewithlimits{\mathbb{E}}[R(T)]\geq\min\left(\,T,\;\Omega\left(\,\sqrt{KT\log(N)/\log(K)}\,\right)\,\right).$$'
proof: This lower bound can be proved by an ingenious (yet simple) reduction to the
  basic Ω(√(KT)) lower regret bound for bandits, see Exercise 6.1.
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/number-of-arms-k]]'
- '[[concepts/time-horizon-t]]'
- '[[concepts/adversarial-bandits-with-expert-advice]]'
- '[[concepts/lower-bound-on-regret]]'
- '[[concepts/regret]]'
- '[[concepts/number-of-experts]]'
about_meta:
- target: '[[concepts/number-of-arms-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/time-horizon-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/adversarial-bandits-with-expert-advice]]'
  role: primary
  aspect: ''
- target: '[[concepts/lower-bound-on-regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-experts]]'
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

# Lower bound for adversarial bandits with expert advice (Eq. 87)

For any given triple of parameters K, T, N, there is a lower bound on regret for the adversarial bandits with expert advice problem:
$$\operatornamewithlimits{\mathbb{E}}[R(T)]\geq\min\left(\,T,\;\Omega\left(\,\sqrt{KT\log(N)/\log(K)}\,\right)\,\right).$$


## Proof

This lower bound can be proved by an ingenious (yet simple) reduction to the basic Ω(√(KT)) lower regret bound for bandits, see Exercise 6.1.
