---
slug: achieving-pareto-optimality-in-games-via-single-bit-feedback--theorem-1-main-result
label: Theorem 1 (Main Result)
claim_type: theorem
statement: 'For any n-agent game, if Assumption 4 holds and the exploration length
  is K = log(4MTξ²)/(2ξ²), then the expected total regret is bounded by

  $$\mathrm{E}[R_{T}] < \frac{\Delta}{2\xi^{2}}\left(1+\log(4MT\xi^{2})\left(1-\frac{1}{2T\xi^{2}}\right)\right),$$

  where Δ := max_a (W(a*) − W(a)), M = |A_λ|, and ξ is as described in (16).'
proof: 'Based on the randomness on I_{a^t=a, m^t=1} ∈ {0,1} and (20), the Hoeffding
  bound yields that


  P(|θ̂^K(a) − θ(a)| ≥ ξ) ≤ 2e^{-2Kξ²}


  for each a. Then, using the union bound, we obtain


  P(|θ̂^K(a) − θ(a)| ≥ ξ for some a ∈ A) ≤ 2Me^{-2Kξ²}.


  Correspondingly, we have


  P(|θ̂^K(a) − θ(a)| ≤ ξ, ∀a ∈ A) ≥ 1 − β,


  where β := 2Me^{-2Kξ²}. By Proposition 1 and (27), agents play the best joint action
  a* in the exploitation phase with probability at least 1 − β, and a worse joint
  action a ≠ a* with probability at most β. Thus, the expected regret is:


  E[R_T] ≤ KΔ + β(T − K)Δ < KΔ + βTΔ.


  The optimal K* minimizing KΔ + βTΔ is given by


  K* = (1/(2ξ²)) log(4MTξ²).


  Choosing K = K*, we obtain β = 1/(2Tξ²) and (25), which completes the proof. □'
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/exploitation-phase]]'
- '[[concepts/system-welfare-function-w]]'
- '[[concepts/exploration-horizon-k]]'
- '[[concepts/sbc-pe-algorithm]]'
- '[[concepts/exploration-phase]]'
- '[[concepts/number-of-stages-t]]'
- '[[concepts/logarithmic-regret-bound]]'
- '[[concepts/n-person-game]]'
- '[[concepts/expected-regret]]'
- '[[concepts/explore-then-commit-procedure]]'
about_meta:
- target: '[[concepts/exploitation-phase]]'
  role: primary
  aspect: ''
- target: '[[concepts/system-welfare-function-w]]'
  role: primary
  aspect: ''
- target: '[[concepts/exploration-horizon-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/sbc-pe-algorithm]]'
  role: primary
  aspect: ''
- target: '[[concepts/exploration-phase]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-stages-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/logarithmic-regret-bound]]'
  role: primary
  aspect: ''
- target: '[[concepts/n-person-game]]'
  role: primary
  aspect: ''
- target: '[[concepts/expected-regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/explore-then-commit-procedure]]'
  role: primary
  aspect: ''
depends_on: []
depends_on_meta: []
sourced_from:
- '[[sources/2509.25921|Achieving Pareto Optimality in Games via Single-bit Feedback]]'
sourced_from_meta:
- target: '[[sources/2509.25921|Achieving Pareto Optimality in Games via Single-bit
    Feedback]]'
  section: ''
  page: ''
  confidence: 0.0
---

# Theorem 1 (Main Result)

For any n-agent game, if Assumption 4 holds and the exploration length is K = log(4MTξ²)/(2ξ²), then the expected total regret is bounded by
$$\mathrm{E}[R_{T}] < \frac{\Delta}{2\xi^{2}}\left(1+\log(4MT\xi^{2})\left(1-\frac{1}{2T\xi^{2}}\right)\right),$$
where Δ := max_a (W(a*) − W(a)), M = |A_λ|, and ξ is as described in (16).


## Proof

Based on the randomness on I_{a^t=a, m^t=1} ∈ {0,1} and (20), the Hoeffding bound yields that

P(|θ̂^K(a) − θ(a)| ≥ ξ) ≤ 2e^{-2Kξ²}

for each a. Then, using the union bound, we obtain

P(|θ̂^K(a) − θ(a)| ≥ ξ for some a ∈ A) ≤ 2Me^{-2Kξ²}.

Correspondingly, we have

P(|θ̂^K(a) − θ(a)| ≤ ξ, ∀a ∈ A) ≥ 1 − β,

where β := 2Me^{-2Kξ²}. By Proposition 1 and (27), agents play the best joint action a* in the exploitation phase with probability at least 1 − β, and a worse joint action a ≠ a* with probability at most β. Thus, the expected regret is:

E[R_T] ≤ KΔ + β(T − K)Δ < KΔ + βTΔ.

The optimal K* minimizing KΔ + βTΔ is given by

K* = (1/(2ξ²)) log(4MTξ²).

Choosing K = K*, we obtain β = 1/(2Tξ²) and (25), which completes the proof. □
