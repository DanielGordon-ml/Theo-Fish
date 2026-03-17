---
slug: achieving-pareto-optimality-in-games-via-single-bit-feedback--lemma-1
label: Lemma 1
claim_type: lemma
statement: 'Under Assumption 4, we have

  $$\theta(a^{*})-\xi>\sum_{\begin{subarray}{c}a\in A_{\lambda}:\\ a\neq a^{*}\end{subarray}}(\theta(a)+\xi),$$

  where

  $$\xi\coloneqq\frac{\delta}{|A|M}\cdot\epsilon^{n-\max_{\tilde{a}\neq a^{*}}W(a)}.$$'
proof: 'Using Assumption 4, we have ε^{-Δ_1} > M + δ, and from there, we have


  θ(a*) − Mξ = (1/|A|) ε^{n − max_{ã ≠ a*} W(a)} (ε^{-Δ_1} − δ)

  > (M/|A|) ε^{n − max_{ã ≠ a*} W(a)}

  > Σ_{a ∈ A_λ, a ≠ a*} θ(a).


  Then, by adding (M−1)ξ to both sides, we obtain (15). □'
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/welfare-gap]]'
- '[[concepts/sbc-pe]]'
- '[[concepts/exploration-phase]]'
- '[[concepts/epsilon-parameter]]'
- '[[concepts/system-welfare-function-w]]'
about_meta:
- target: '[[concepts/welfare-gap]]'
  role: primary
  aspect: ''
- target: '[[concepts/sbc-pe]]'
  role: primary
  aspect: ''
- target: '[[concepts/exploration-phase]]'
  role: primary
  aspect: ''
- target: '[[concepts/epsilon-parameter]]'
  role: primary
  aspect: ''
- target: '[[concepts/system-welfare-function-w]]'
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

# Lemma 1

Under Assumption 4, we have
$$\theta(a^{*})-\xi>\sum_{\begin{subarray}{c}a\in A_{\lambda}:\\ a\neq a^{*}\end{subarray}}(\theta(a)+\xi),$$
where
$$\xi\coloneqq\frac{\delta}{|A|M}\cdot\epsilon^{n-\max_{\tilde{a}\neq a^{*}}W(a)}.$$


## Proof

Using Assumption 4, we have ε^{-Δ_1} > M + δ, and from there, we have

θ(a*) − Mξ = (1/|A|) ε^{n − max_{ã ≠ a*} W(a)} (ε^{-Δ_1} − δ)
> (M/|A|) ε^{n − max_{ã ≠ a*} W(a)}
> Σ_{a ∈ A_λ, a ≠ a*} θ(a).

Then, by adding (M−1)ξ to both sides, we obtain (15). □
