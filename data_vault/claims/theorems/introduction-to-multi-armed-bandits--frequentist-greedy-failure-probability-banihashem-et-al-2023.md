---
slug: introduction-to-multi-armed-bandits--frequentist-greedy-failure-probability-banihashem-et-al-2023
label: Frequentist-greedy failure probability (Banihashem et al. 2023)
claim_type: theorem
statement: 'A trivial argument yields failure probability $e^{-\Omega(N_{0})}$ for
  the frequentist-greedy algorithm with $K=2$ arms: consider the event when the good
  arm receives 0 reward in all warm-up rounds, and the bad arm receives a non-zero
  reward in some warm-up round. However, this trivial guarantee is rather weak because
  of the exponential dependence on $N_{0}$. A similar but exponentially stronger guarantee
  is proved in Banihashem et al. (2023), with failure probability on the order of
  $1/\sqrt{N_{0}}$. This result is extended to a broader class of agent behaviors
  (including, e.g., mild optimism and pessimism), and to $K>2$ arms.'
proof: ''
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/warm-start]]'
- '[[concepts/sample-complexity]]'
- '[[concepts/frequentist-greedy-algorithm]]'
- '[[concepts/number-of-arms-k]]'
about_meta:
- target: '[[concepts/warm-start]]'
  role: primary
  aspect: ''
- target: '[[concepts/sample-complexity]]'
  role: primary
  aspect: ''
- target: '[[concepts/frequentist-greedy-algorithm]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-arms-k]]'
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

# Frequentist-greedy failure probability (Banihashem et al. 2023)

A trivial argument yields failure probability $e^{-\Omega(N_{0})}$ for the frequentist-greedy algorithm with $K=2$ arms: consider the event when the good arm receives 0 reward in all warm-up rounds, and the bad arm receives a non-zero reward in some warm-up round. However, this trivial guarantee is rather weak because of the exponential dependence on $N_{0}$. A similar but exponentially stronger guarantee is proved in Banihashem et al. (2023), with failure probability on the order of $1/\sqrt{N_{0}}$. This result is extended to a broader class of agent behaviors (including, e.g., mild optimism and pessimism), and to $K>2$ arms.
