---
slug: introduction-to-multi-armed-bandits--lemma-2-8-general-case
label: Lemma 2.8 (general case)
claim_type: lemma
statement: For K arms with Bernoulli rewards, where problem instance I_j has arm j
  with mean (1+ε)/2 and all other arms with mean 1/2, any algorithm that correctly
  identifies the best arm with probability at least 0.99 on each instance I_j requires
  T ≥ cK/ε² for a small enough constant c.
proof: 'For the sake of the analysis, we will consider an additional problem instance
  I₀ = {μ_i = 1/2 for all arms i}, which we call the "base instance". Let E₀[·] be
  the expectation given this problem instance. Also, let T_a be the total number of
  times arm a is played.


  We consider the algorithm''s performance on problem instance I₀, and focus on arms
  j that are "neglected" by the algorithm. Formally, we observe:


  There are ≥ 2K/3 arms j such that E₀(T_j) ≤ 3T/K, (25)

  There are ≥ 2K/3 arms j such that P₀(y_T = j) ≤ 3/K. (26)


  (To prove (25), assume for contradiction that we have more than K/3 arms with E₀(T_j)
  > 3T/K. Then the expected total number of times these arms are played is strictly
  greater than T, which is a contradiction. (26) is proved similarly.) By Markov inequality,


  E₀(T_j) ≤ 3T/K implies that Pr[T_j ≤ 24T/K] ≥ 7/8.


  Since the sets of arms in (25) and (26) must overlap on at least K/3 arms, we conclude:


  There are at least K/3 arms j such that Pr[T_j ≤ 24T/K] ≥ 7/8 and P₀(y_T = j) ≤
  3/K. (27)


  We will now refine our definition of the sample space. For each arm a, define the
  t-round sample space Ω_a^t = {0,1}^t, where each outcome corresponds to a particular
  realization of the tuple (r_s(a): s ∈ [t]). Then the "full" sample space we considered
  before can be expressed as Ω = ∏_{a ∈ [K]} Ω_a^T.


  Fix an arm j satisfying the two properties in (27). We will prove that P_j[Y_T =
  j] ≤ 1/2. (28)


  Since there are at least K/3 such arms, this suffices to imply the Lemma.


  We consider a "reduced" sample space in which arm j is played only m = min(T, 24T/K)
  times:


  Ω* = Ω_j^m × ∏_{arms a ≠ j} Ω_a^T. (29)


  For each problem instance I_ℓ, we define distribution P*_ℓ on Ω* as follows: P*_ℓ(A)
  = Pr[A | I_ℓ] for each A ⊂ Ω*.


  We apply the KL-divergence argument to distributions P*₀ and P*_j. For each event
  A ⊂ Ω*:


  2(P₀*(A) - P_j*(A))² ≤ KL(P₀*, P_j*) (by Pinsker''s inequality)

  = Σ_{arms a} Σ_{t=1}^T KL(P₀^{a,t}, P_j^{a,t}) (by Chain Rule)

  = Σ_{arms a ≠ j} Σ_{t=1}^T KL(P₀^{a,t}, P_j^{a,t}) + Σ_{t=1}^m KL(P₀^{j,t}, P_j^{j,t})

  ≤ 0 + m · 2ε².


  The last inequality holds because each arm a ≠ j has identical reward distributions
  under problem instances I₀ and I_j (namely the fair coin RC₀), and for arm j we
  only need to sum up over m samples rather than T.


  Therefore, assuming T ≤ cK/ε² with small enough constant c, we can conclude that


  |P₀*(A) - P_j*(A)| ≤ ε√m < 1/8 for all events A ⊂ Ω*. (30)


  To apply (30), we need to make sure that A ⊂ Ω*, i.e., that whether this event holds
  is completely determined by the first m samples of arm j (and all samples of other
  arms). We apply (30) twice: to events


  A = {y_T = j and T_j ≤ m} and A'' = {T_j > m}. (31)


  Note that A, A'' ⊂ Ω*; indeed, A'' ⊂ Ω* because whether the algorithm samples arm
  j more than m times is completely determined by the first m samples of this arm
  (and all samples of the other arms). We are ready for the final computation:


  P_j(A) ≤ 1/8 + P₀(A) (by (30))

  ≤ 1/8 + P₀(y_T = j)

  ≤ 1/4 (by our choice of arm j).


  P_j(A'') ≤ 1/8 + P₀(A'') (by (30))

  ≤ 1/4 (by our choice of arm j).


  P_j(Y_T = j) ≤ P_j*(Y_T = j and T_j ≤ m) + P_j*(T_j > m)

  = P_j(A) + P_j(A'') ≤ 1/2.


  This completes the proof of Eq. (28), and hence that of the Lemma.'
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/reduced-sample-space-omega]]'
- '[[concepts/bernoulli-distribution]]'
- '[[concepts/kl-divergence]]'
- '[[concepts/best-arm-identification]]'
- '[[concepts/number-of-arms-k]]'
- '[[concepts/parameter-epsilon]]'
- '[[concepts/expected-plays-e0-t-j]]'
- '[[concepts/event-a]]'
- '[[concepts/problem-instance-i-0]]'
- '[[concepts/event-a-prime]]'
about_meta:
- target: '[[concepts/reduced-sample-space-omega]]'
  role: primary
  aspect: ''
- target: '[[concepts/bernoulli-distribution]]'
  role: primary
  aspect: ''
- target: '[[concepts/kl-divergence]]'
  role: primary
  aspect: ''
- target: '[[concepts/best-arm-identification]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-arms-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/parameter-epsilon]]'
  role: primary
  aspect: ''
- target: '[[concepts/expected-plays-e0-t-j]]'
  role: primary
  aspect: ''
- target: '[[concepts/event-a]]'
  role: primary
  aspect: ''
- target: '[[concepts/problem-instance-i-0]]'
  role: primary
  aspect: ''
- target: '[[concepts/event-a-prime]]'
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

# Lemma 2.8 (general case)

For K arms with Bernoulli rewards, where problem instance I_j has arm j with mean (1+ε)/2 and all other arms with mean 1/2, any algorithm that correctly identifies the best arm with probability at least 0.99 on each instance I_j requires T ≥ cK/ε² for a small enough constant c.


## Proof

For the sake of the analysis, we will consider an additional problem instance I₀ = {μ_i = 1/2 for all arms i}, which we call the "base instance". Let E₀[·] be the expectation given this problem instance. Also, let T_a be the total number of times arm a is played.

We consider the algorithm's performance on problem instance I₀, and focus on arms j that are "neglected" by the algorithm. Formally, we observe:

There are ≥ 2K/3 arms j such that E₀(T_j) ≤ 3T/K, (25)
There are ≥ 2K/3 arms j such that P₀(y_T = j) ≤ 3/K. (26)

(To prove (25), assume for contradiction that we have more than K/3 arms with E₀(T_j) > 3T/K. Then the expected total number of times these arms are played is strictly greater than T, which is a contradiction. (26) is proved similarly.) By Markov inequality,

E₀(T_j) ≤ 3T/K implies that Pr[T_j ≤ 24T/K] ≥ 7/8.

Since the sets of arms in (25) and (26) must overlap on at least K/3 arms, we conclude:

There are at least K/3 arms j such that Pr[T_j ≤ 24T/K] ≥ 7/8 and P₀(y_T = j) ≤ 3/K. (27)

We will now refine our definition of the sample space. For each arm a, define the t-round sample space Ω_a^t = {0,1}^t, where each outcome corresponds to a particular realization of the tuple (r_s(a): s ∈ [t]). Then the "full" sample space we considered before can be expressed as Ω = ∏_{a ∈ [K]} Ω_a^T.

Fix an arm j satisfying the two properties in (27). We will prove that P_j[Y_T = j] ≤ 1/2. (28)

Since there are at least K/3 such arms, this suffices to imply the Lemma.

We consider a "reduced" sample space in which arm j is played only m = min(T, 24T/K) times:

Ω* = Ω_j^m × ∏_{arms a ≠ j} Ω_a^T. (29)

For each problem instance I_ℓ, we define distribution P*_ℓ on Ω* as follows: P*_ℓ(A) = Pr[A | I_ℓ] for each A ⊂ Ω*.

We apply the KL-divergence argument to distributions P*₀ and P*_j. For each event A ⊂ Ω*:

2(P₀*(A) - P_j*(A))² ≤ KL(P₀*, P_j*) (by Pinsker's inequality)
= Σ_{arms a} Σ_{t=1}^T KL(P₀^{a,t}, P_j^{a,t}) (by Chain Rule)
= Σ_{arms a ≠ j} Σ_{t=1}^T KL(P₀^{a,t}, P_j^{a,t}) + Σ_{t=1}^m KL(P₀^{j,t}, P_j^{j,t})
≤ 0 + m · 2ε².

The last inequality holds because each arm a ≠ j has identical reward distributions under problem instances I₀ and I_j (namely the fair coin RC₀), and for arm j we only need to sum up over m samples rather than T.

Therefore, assuming T ≤ cK/ε² with small enough constant c, we can conclude that

|P₀*(A) - P_j*(A)| ≤ ε√m < 1/8 for all events A ⊂ Ω*. (30)

To apply (30), we need to make sure that A ⊂ Ω*, i.e., that whether this event holds is completely determined by the first m samples of arm j (and all samples of other arms). We apply (30) twice: to events

A = {y_T = j and T_j ≤ m} and A' = {T_j > m}. (31)

Note that A, A' ⊂ Ω*; indeed, A' ⊂ Ω* because whether the algorithm samples arm j more than m times is completely determined by the first m samples of this arm (and all samples of the other arms). We are ready for the final computation:

P_j(A) ≤ 1/8 + P₀(A) (by (30))
≤ 1/8 + P₀(y_T = j)
≤ 1/4 (by our choice of arm j).

P_j(A') ≤ 1/8 + P₀(A') (by (30))
≤ 1/4 (by our choice of arm j).

P_j(Y_T = j) ≤ P_j*(Y_T = j and T_j ≤ m) + P_j*(T_j > m)
= P_j(A) + P_j(A') ≤ 1/2.

This completes the proof of Eq. (28), and hence that of the Lemma.
