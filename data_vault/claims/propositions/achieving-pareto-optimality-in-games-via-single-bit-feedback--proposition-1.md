---
slug: achieving-pareto-optimality-in-games-via-single-bit-feedback--proposition-1
label: Proposition 1
claim_type: proposition
statement: 'For a given stage t, if Assumption 4 holds, and |θ̂^t(a) − θ(a)| < ξ for
  all a ∈ A, then we have

  $$\left(\operatorname{arg\,max}_{a_{i}\in A_{i}}\left\{\widehat{\theta}_{i}^{t}(a_{i})\right\}\right)_{i=1}^{n}
  = \operatorname{arg\,max}_{a\in A}\{\theta(a)\} = a^{*}.$$'
proof: 'From the definition of θ̂_i^t, and θ̂^t, we have


  θ̂_i^t(a_i*) = Σ_{a ∈ A: a_i = a_i*} θ̂^t(a) > θ̂^t(a*) > θ(a*) − ξ.


  On the other hand, Lemma 1 yields


  θ(a*) − ξ > Σ_{a ≠ a*} (θ(a) + ξ) > Σ_{a ≠ a*} θ̂^t(a) > θ̂_i^t(ã_i)


  for all ã_i ≠ a_i*. Hence, θ̂_i^t(a_i*) > θ̂_i^t(ã_i) for all ã_i ≠ a_i*, and we
  obtain (22). □'
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/most-frequently-played-content-endorsed-joint-action]]'
- '[[concepts/pareto-efficient-action-profile]]'
- '[[concepts/sbc-pe]]'
- '[[concepts/action-selection-operator]]'
- '[[concepts/communication-efficient]]'
about_meta:
- target: '[[concepts/most-frequently-played-content-endorsed-joint-action]]'
  role: primary
  aspect: ''
- target: '[[concepts/pareto-efficient-action-profile]]'
  role: primary
  aspect: ''
- target: '[[concepts/sbc-pe]]'
  role: primary
  aspect: ''
- target: '[[concepts/action-selection-operator]]'
  role: primary
  aspect: ''
- target: '[[concepts/communication-efficient]]'
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

# Proposition 1

For a given stage t, if Assumption 4 holds, and |θ̂^t(a) − θ(a)| < ξ for all a ∈ A, then we have
$$\left(\operatorname{arg\,max}_{a_{i}\in A_{i}}\left\{\widehat{\theta}_{i}^{t}(a_{i})\right\}\right)_{i=1}^{n} = \operatorname{arg\,max}_{a\in A}\{\theta(a)\} = a^{*}.$$


## Proof

From the definition of θ̂_i^t, and θ̂^t, we have

θ̂_i^t(a_i*) = Σ_{a ∈ A: a_i = a_i*} θ̂^t(a) > θ̂^t(a*) > θ(a*) − ξ.

On the other hand, Lemma 1 yields

θ(a*) − ξ > Σ_{a ≠ a*} (θ(a) + ξ) > Σ_{a ≠ a*} θ̂^t(a) > θ̂_i^t(ã_i)

for all ã_i ≠ a_i*. Hence, θ̂_i^t(a_i*) > θ̂_i^t(ã_i) for all ã_i ≠ a_i*, and we obtain (22). □
