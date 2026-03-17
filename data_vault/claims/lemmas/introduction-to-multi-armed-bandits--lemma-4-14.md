---
slug: introduction-to-multi-armed-bandits--lemma-4-14
label: Lemma 4.14
claim_type: lemma
statement: Δ(x) ≤ 3 r_t(x) for each arm x and each round t.
proof: 'Suppose arm x is played in this round. By the covering invariant, the best
  arm x* was covered by the confidence ball of some active arm y, i.e., x* ∈ B_t(y).
  It follows that


  index(x) ≥ index(y) = (μ_t(y) + r_t(y)) + r_t(y) ≥ μ(x*) = μ*


  where (μ_t(y) + r_t(y)) ≥ μ(y) by the clean event. The last inequality holds because
  of the Lipschitz condition. On the other hand:


  index(x) = μ_t(x) + 2·r_t(x) ≤ μ(x) + 3·r_t(x)


  where μ_t(x) ≤ μ(x) + r_t(x) by the clean event. Putting these two equations together:

  Δ(x) := μ* - μ(x) ≤ 3·r_t(x).


  Now suppose arm x is not played in round t. If it has never been played before round
  t, then r_t(x) > 1 and the lemma follows trivially. Else, letting s be the last
  time when x has been played before round t, we see that r_t(x) = r_s(x) ≥ Δ(x)/3.'
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/lipschitz-property]]'
- '[[concepts/index-function]]'
- '[[concepts/zooming-algorithm-for-lipschitz-bandits]]'
- '[[concepts/confidence-radius-r-t-a]]'
- '[[concepts/gap-d-a]]'
about_meta:
- target: '[[concepts/lipschitz-property]]'
  role: primary
  aspect: ''
- target: '[[concepts/index-function]]'
  role: primary
  aspect: ''
- target: '[[concepts/zooming-algorithm-for-lipschitz-bandits]]'
  role: primary
  aspect: ''
- target: '[[concepts/confidence-radius-r-t-a]]'
  role: primary
  aspect: ''
- target: '[[concepts/gap-d-a]]'
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

# Lemma 4.14

Δ(x) ≤ 3 r_t(x) for each arm x and each round t.


## Proof

Suppose arm x is played in this round. By the covering invariant, the best arm x* was covered by the confidence ball of some active arm y, i.e., x* ∈ B_t(y). It follows that

index(x) ≥ index(y) = (μ_t(y) + r_t(y)) + r_t(y) ≥ μ(x*) = μ*

where (μ_t(y) + r_t(y)) ≥ μ(y) by the clean event. The last inequality holds because of the Lipschitz condition. On the other hand:

index(x) = μ_t(x) + 2·r_t(x) ≤ μ(x) + 3·r_t(x)

where μ_t(x) ≤ μ(x) + r_t(x) by the clean event. Putting these two equations together:
Δ(x) := μ* - μ(x) ≤ 3·r_t(x).

Now suppose arm x is not played in round t. If it has never been played before round t, then r_t(x) > 1 and the lemma follows trivially. Else, letting s be the last time when x has been played before round t, we see that r_t(x) = r_s(x) ≥ Δ(x)/3.
