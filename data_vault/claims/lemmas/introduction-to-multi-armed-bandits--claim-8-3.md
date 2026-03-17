---
slug: introduction-to-multi-armed-bandits--claim-8-3
label: Claim 8.3
claim_type: lemma
statement: $\operatornamewithlimits{\mathbb{E}}[\mathtt{DE}(S)]\leq\epsilon LT$.
proof: "For each round t and the respective context x = x_t,\n\nμ(π*_S(x) | f_S(x))\
  \ ≥ μ(π*(x) | f_S(x))  (by optimality of π*_S)\n                      ≥ μ(π*(x)\
  \ | x) - εL  (by Lipschitzness).\n\nSumming this up over all rounds t, we obtain\n\
  \nE[REW(π*_S)] ≥ REW[π*] - εLT."
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/lipschitz-condition]]'
- '[[concepts/lipschitz-contextual-bandits-problem]]'
- '[[concepts/epsilon-mesh]]'
- '[[concepts/discretization-error]]'
- '[[concepts/discretized-best-response]]'
about_meta:
- target: '[[concepts/lipschitz-condition]]'
  role: primary
  aspect: ''
- target: '[[concepts/lipschitz-contextual-bandits-problem]]'
  role: primary
  aspect: ''
- target: '[[concepts/epsilon-mesh]]'
  role: primary
  aspect: ''
- target: '[[concepts/discretization-error]]'
  role: primary
  aspect: ''
- target: '[[concepts/discretized-best-response]]'
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

# Claim 8.3

$\operatornamewithlimits{\mathbb{E}}[\mathtt{DE}(S)]\leq\epsilon LT$.


## Proof

For each round t and the respective context x = x_t,

μ(π*_S(x) | f_S(x)) ≥ μ(π*(x) | f_S(x))  (by optimality of π*_S)
                      ≥ μ(π*(x) | x) - εL  (by Lipschitzness).

Summing this up over all rounds t, we obtain

E[REW(π*_S)] ≥ REW[π*] - εLT.
