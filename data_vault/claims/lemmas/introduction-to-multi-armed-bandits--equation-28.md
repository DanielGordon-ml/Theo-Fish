---
slug: introduction-to-multi-armed-bandits--equation-28
label: Equation (28)
claim_type: lemma
statement: For each arm j satisfying the two properties in (27), P_j[Y_T = j] ≤ 1/2.
proof: 'We consider a reduced sample space Ω* = Ω_j^m × ∏_{a≠j} Ω_a^T where m = min(T,
  24T/K). For each problem instance I_ℓ, define distribution P*_ℓ on Ω* as P*_ℓ(A)
  = Pr[A | I_ℓ] for each A ⊂ Ω*. We apply the KL-divergence argument to distributions
  P*_0 and P*_j. For each event A ⊂ Ω*:


  2(P*_0(A) - P*_j(A))² ≤ KL(P*_0, P*_j) (by Pinsker''s inequality)

  = Σ_{arms a} Σ_{t=1}^T KL(P_0^{a,t}, P_j^{a,t}) (by Chain Rule)

  = Σ_{arms a≠j} Σ_{t=1}^T KL(P_0^{a,t}, P_j^{a,t}) + Σ_{t=1}^m KL(P_0^{j,t}, P_j^{j,t})

  ≤ 0 + m · 2ε²


  The last inequality holds because each arm a≠j has identical reward distributions
  under I_0 and I_j, and for arm j we only sum over m samples. Therefore, assuming
  T ≤ cK/ε² with small enough constant c, |P*_0(A) - P*_j(A)| ≤ ε√m < 1/8 for all
  events A ⊂ Ω*.


  We apply this to events A = {y_T = j and T_j ≤ m} and A'' = {T_j > m}. Note A, A''
  ⊂ Ω*; A'' ⊂ Ω* because whether the algorithm samples arm j more than m times is
  completely determined by the first m samples of this arm and all samples of other
  arms.


  P_j(A) ≤ 1/8 + P_0(A) (by (30)) ≤ 1/8 + P_0(y_T = j) ≤ 1/4 (by our choice of arm
  j).

  P_j(A'') ≤ 1/8 + P_0(A'') (by (30)) ≤ 1/4 (by our choice of arm j, since P_0(T_j
  > m) ≤ 1/8).

  P_j(Y_T = j) ≤ P_j(Y_T = j and T_j ≤ m) + P_j(T_j > m) = P_j(A) + P_j(A'') ≤ 1/2.'
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/problem-instance-i-0]]'
- '[[concepts/number-of-arms-k]]'
- '[[concepts/0-1-rewards]]'
- '[[concepts/kl-divergence]]'
- '[[concepts/reduced-sample-space-omega]]'
- '[[concepts/parameter-epsilon]]'
about_meta:
- target: '[[concepts/problem-instance-i-0]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-arms-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/0-1-rewards]]'
  role: primary
  aspect: ''
- target: '[[concepts/kl-divergence]]'
  role: primary
  aspect: ''
- target: '[[concepts/reduced-sample-space-omega]]'
  role: primary
  aspect: ''
- target: '[[concepts/parameter-epsilon]]'
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

# Equation (28)

For each arm j satisfying the two properties in (27), P_j[Y_T = j] ≤ 1/2.


## Proof

We consider a reduced sample space Ω* = Ω_j^m × ∏_{a≠j} Ω_a^T where m = min(T, 24T/K). For each problem instance I_ℓ, define distribution P*_ℓ on Ω* as P*_ℓ(A) = Pr[A | I_ℓ] for each A ⊂ Ω*. We apply the KL-divergence argument to distributions P*_0 and P*_j. For each event A ⊂ Ω*:

2(P*_0(A) - P*_j(A))² ≤ KL(P*_0, P*_j) (by Pinsker's inequality)
= Σ_{arms a} Σ_{t=1}^T KL(P_0^{a,t}, P_j^{a,t}) (by Chain Rule)
= Σ_{arms a≠j} Σ_{t=1}^T KL(P_0^{a,t}, P_j^{a,t}) + Σ_{t=1}^m KL(P_0^{j,t}, P_j^{j,t})
≤ 0 + m · 2ε²

The last inequality holds because each arm a≠j has identical reward distributions under I_0 and I_j, and for arm j we only sum over m samples. Therefore, assuming T ≤ cK/ε² with small enough constant c, |P*_0(A) - P*_j(A)| ≤ ε√m < 1/8 for all events A ⊂ Ω*.

We apply this to events A = {y_T = j and T_j ≤ m} and A' = {T_j > m}. Note A, A' ⊂ Ω*; A' ⊂ Ω* because whether the algorithm samples arm j more than m times is completely determined by the first m samples of this arm and all samples of other arms.

P_j(A) ≤ 1/8 + P_0(A) (by (30)) ≤ 1/8 + P_0(y_T = j) ≤ 1/4 (by our choice of arm j).
P_j(A') ≤ 1/8 + P_0(A') (by (30)) ≤ 1/4 (by our choice of arm j, since P_0(T_j > m) ≤ 1/8).
P_j(Y_T = j) ≤ P_j(Y_T = j and T_j ≤ m) + P_j(T_j > m) = P_j(A) + P_j(A') ≤ 1/2.
