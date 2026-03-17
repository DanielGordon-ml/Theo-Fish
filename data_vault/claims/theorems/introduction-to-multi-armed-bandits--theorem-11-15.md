---
slug: introduction-to-multi-armed-bandits--theorem-11-15
label: Theorem 11.15
claim_type: theorem
statement: RepeatedHE with exploration probability ε > 0 and N_0 initial samples of
  arm 1 is BIC as long as ε < (1/3) E[G · 1_{G > 0}], where G = G_{N_0+1}.
proof: 'The only remaining piece is the claim that the quantity E[G_t · 1_{G_t > 0}]
  does not decrease over time. This claim holds for any sequence of signals (S_1,
  S_2, ..., S_T) such that each signal S_t is determined by the next signal S_{t+1}.


  Fix round t. Applying Fact 11.6 twice, we obtain


  E[G_t | G_t > 0] = E[μ_2 - μ_1 | G_t > 0] = E[G_{t+1} | G_t > 0].


  (The last equality uses the fact that S_{t+1} determines S_t.) Then,


  E[G_t · 1_{G_t > 0}] = E[G_t | G_t > 0] · Pr[G_t > 0] = E[G_{t+1} | G_t > 0] · Pr[G_t
  > 0] = E[G_{t+1} · 1_{G_t > 0}] ≤ E[G_{t+1} · 1_{G_{t+1} > 0}].


  The last inequality holds because x · 1_{·} ≤ x · 1_{x > 0} for any x ∈ R.'
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/bic-bayesian-incentive-compatible]]'
- '[[concepts/posterior-gap-gt]]'
- '[[concepts/exploration-probability-epsilon]]'
- '[[concepts/initial-exploration-rounds-n0]]'
- '[[concepts/repeatedhe]]'
about_meta:
- target: '[[concepts/bic-bayesian-incentive-compatible]]'
  role: primary
  aspect: ''
- target: '[[concepts/posterior-gap-gt]]'
  role: primary
  aspect: ''
- target: '[[concepts/exploration-probability-epsilon]]'
  role: primary
  aspect: ''
- target: '[[concepts/initial-exploration-rounds-n0]]'
  role: primary
  aspect: ''
- target: '[[concepts/repeatedhe]]'
  role: primary
  aspect: ''
depends_on:
- '[[claims/introduction-to-multi-armed-bandits--lemma-3-4]]'
depends_on_meta:
- target: '[[claims/introduction-to-multi-armed-bandits--lemma-3-4]]'
sourced_from:
- '[[sources/1904.07272|Introduction to Multi-Armed Bandits]]'
sourced_from_meta:
- target: '[[sources/1904.07272|Introduction to Multi-Armed Bandits]]'
  section: ''
  page: ''
  confidence: 0.0
---

# Theorem 11.15

RepeatedHE with exploration probability ε > 0 and N_0 initial samples of arm 1 is BIC as long as ε < (1/3) E[G · 1_{G > 0}], where G = G_{N_0+1}.


## Proof

The only remaining piece is the claim that the quantity E[G_t · 1_{G_t > 0}] does not decrease over time. This claim holds for any sequence of signals (S_1, S_2, ..., S_T) such that each signal S_t is determined by the next signal S_{t+1}.

Fix round t. Applying Fact 11.6 twice, we obtain

E[G_t | G_t > 0] = E[μ_2 - μ_1 | G_t > 0] = E[G_{t+1} | G_t > 0].

(The last equality uses the fact that S_{t+1} determines S_t.) Then,

E[G_t · 1_{G_t > 0}] = E[G_t | G_t > 0] · Pr[G_t > 0] = E[G_{t+1} | G_t > 0] · Pr[G_t > 0] = E[G_{t+1} · 1_{G_t > 0}] ≤ E[G_{t+1} · 1_{G_{t+1} > 0}].

The last inequality holds because x · 1_{·} ≤ x · 1_{x > 0} for any x ∈ R.
