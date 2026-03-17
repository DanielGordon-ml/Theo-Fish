---
slug: introduction-to-multi-armed-bandits--exercise-4-6-a
label: Exercise 4.6(a)
claim_type: proposition
statement: Consider Lipschitz bandits on metric space $(X,\mathcal{D})$ with $\mathcal{D}(\cdot,\cdot)\leq
  \frac{1}{2}$. Fix $\mu^*\in[\frac{3}{4},1]$ and a subset $S\subset X$ and assume
  $\mu(x)=\mu^*-\mathcal{D}(x,S)$ for all $x\in X$. Then $\mu^*-\mu(x)\leq\mathcal{D}(x,S)$
  for all arms $x$, and this condition suffices for the analysis of the zooming algorithm,
  instead of the full Lipschitz condition (57).
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/target-set-s]]'
- '[[concepts/lipschitz-property]]'
- '[[concepts/mean-reward-function]]'
- '[[concepts/zooming-algorithm-for-lipschitz-bandits]]'
about_meta:
- target: '[[concepts/target-set-s]]'
  role: primary
  aspect: ''
- target: '[[concepts/lipschitz-property]]'
  role: primary
  aspect: ''
- target: '[[concepts/mean-reward-function]]'
  role: primary
  aspect: ''
- target: '[[concepts/zooming-algorithm-for-lipschitz-bandits]]'
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

# Exercise 4.6(a)

Consider Lipschitz bandits on metric space $(X,\mathcal{D})$ with $\mathcal{D}(\cdot,\cdot)\leq \frac{1}{2}$. Fix $\mu^*\in[\frac{3}{4},1]$ and a subset $S\subset X$ and assume $\mu(x)=\mu^*-\mathcal{D}(x,S)$ for all $x\in X$. Then $\mu^*-\mu(x)\leq\mathcal{D}(x,S)$ for all arms $x$, and this condition suffices for the analysis of the zooming algorithm, instead of the full Lipschitz condition (57).
