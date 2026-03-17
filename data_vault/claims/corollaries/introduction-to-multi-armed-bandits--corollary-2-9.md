---
slug: introduction-to-multi-armed-bandits--corollary-2-9
label: Corollary 2.9
claim_type: corollary
statement: Assume $T$ is as in Lemma 2.8. Fix any algorithm for "best-arm identification".
  Choose an arm $a$ uniformly at random, and run the algorithm on instance $\mathcal{I}_{a}$.
  Then $\Pr[y_{T} \neq a] \geq \tfrac{1}{12}$, where the probability is over the choice
  of arm $a$ and the randomness in rewards and the algorithm.
proof: Lemma 2.8 immediately implies this corollary for deterministic algorithms.
  The general case follows because any randomized algorithm can be expressed as a
  distribution over deterministic algorithms.
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/family-of-problem-instances]]'
- '[[concepts/prediction-accuracy-criterion]]'
- '[[concepts/randomized-algorithm]]'
- '[[concepts/random-permutation-of-arms]]'
- '[[concepts/best-arm-identification]]'
about_meta:
- target: '[[concepts/family-of-problem-instances]]'
  role: primary
  aspect: ''
- target: '[[concepts/prediction-accuracy-criterion]]'
  role: primary
  aspect: ''
- target: '[[concepts/randomized-algorithm]]'
  role: primary
  aspect: ''
- target: '[[concepts/random-permutation-of-arms]]'
  role: primary
  aspect: ''
- target: '[[concepts/best-arm-identification]]'
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

# Corollary 2.9

Assume $T$ is as in Lemma 2.8. Fix any algorithm for "best-arm identification". Choose an arm $a$ uniformly at random, and run the algorithm on instance $\mathcal{I}_{a}$. Then $\Pr[y_{T} \neq a] \geq \tfrac{1}{12}$, where the probability is over the choice of arm $a$ and the randomness in rewards and the algorithm.


## Proof

Lemma 2.8 immediately implies this corollary for deterministic algorithms. The general case follows because any randomized algorithm can be expressed as a distribution over deterministic algorithms.
