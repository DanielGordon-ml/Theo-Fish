---
slug: introduction-to-multi-armed-bandits--lemma-2-7
label: Lemma 2.7
claim_type: lemma
statement: Let μ₁ = (1+ε)/2 and μ₂ = 1/2. Fix a decision rule which satisfies (18)
  and (19). Then T > 1/(4ε²).
proof: 'Let A₀ ⊂ Ω be the event this rule returns High. Then


  Pr[A₀ | μ = μ₁] - Pr[A₀ | μ = μ₂] ≥ 0.98.


  Let P_i(A) = Pr[A | μ = μ_i], for each event A ⊂ Ω and each i ∈ {1,2}. Then P_i
  = P_{i,1} × … × P_{i,T}, where P_{i,t} is the distribution of the t-th coin toss
  if μ = μ_i. Thus, the basic KL-divergence argument summarized in Lemma 2.5 applies
  to distributions P₁ and P₂. It follows that |P₁(A) - P₂(A)| ≤ ε√T. Plugging in A
  = A₀ and T ≤ 1/(4ε²), we obtain |P₁(A₀) - P₂(A₀)| < 1/2, contradicting (20). ∎'
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/decision-rule]]'
- '[[concepts/sample-space-omega]]'
- '[[concepts/coin-mean-identification-problem]]'
- '[[concepts/biased-coin-distribution]]'
- '[[concepts/kl-divergence]]'
about_meta:
- target: '[[concepts/decision-rule]]'
  role: primary
  aspect: ''
- target: '[[concepts/sample-space-omega]]'
  role: primary
  aspect: ''
- target: '[[concepts/coin-mean-identification-problem]]'
  role: primary
  aspect: ''
- target: '[[concepts/biased-coin-distribution]]'
  role: primary
  aspect: ''
- target: '[[concepts/kl-divergence]]'
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

# Lemma 2.7

Let μ₁ = (1+ε)/2 and μ₂ = 1/2. Fix a decision rule which satisfies (18) and (19). Then T > 1/(4ε²).


## Proof

Let A₀ ⊂ Ω be the event this rule returns High. Then

Pr[A₀ | μ = μ₁] - Pr[A₀ | μ = μ₂] ≥ 0.98.

Let P_i(A) = Pr[A | μ = μ_i], for each event A ⊂ Ω and each i ∈ {1,2}. Then P_i = P_{i,1} × … × P_{i,T}, where P_{i,t} is the distribution of the t-th coin toss if μ = μ_i. Thus, the basic KL-divergence argument summarized in Lemma 2.5 applies to distributions P₁ and P₂. It follows that |P₁(A) - P₂(A)| ≤ ε√T. Plugging in A = A₀ and T ≤ 1/(4ε²), we obtain |P₁(A₀) - P₂(A₀)| < 1/2, contradicting (20). ∎
