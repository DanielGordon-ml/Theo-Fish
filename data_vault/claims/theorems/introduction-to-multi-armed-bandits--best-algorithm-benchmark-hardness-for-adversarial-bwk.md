---
slug: introduction-to-multi-armed-bandits--best-algorithm-benchmark-hardness-for-adversarial-bwk
label: Best-Algorithm Benchmark Hardness for Adversarial BwK
claim_type: theorem
statement: 'The ratio $\mathtt{OPT}/\operatorname{\mathbb{E}}[\mathtt{REW}]$ cannot
  be better than $\nicefrac{{T}}{{B}}$ in the worst case. Balseiro and Gur (2019)
  construct this lower bound: for any time horizon $T$, any constants $0<\gamma<\rho<1$,
  and any algorithm there is a problem instance with budget $B=\rho T$ such that $\mathtt{OPT}/\operatorname{\mathbb{E}}[\mathtt{REW}]\geq\gamma-o(T)$.
  Immorlica et al. (2022) provide a simpler but weaker guarantee with only $K=2$ arms:
  for any time horizon $T$, any budget $B<\sqrt{T}$ and any algorithm, there is a
  problem instance with $\mathtt{OPT}/\operatorname{\mathbb{E}}[\mathtt{REW}]\geq
  T/B^{2}$.'
proof: ''
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/adversarial-bwk]]'
- '[[concepts/bandits-with-knapsacks]]'
- '[[concepts/budget-b]]'
- '[[concepts/opt]]'
about_meta:
- target: '[[concepts/adversarial-bwk]]'
  role: primary
  aspect: ''
- target: '[[concepts/bandits-with-knapsacks]]'
  role: primary
  aspect: ''
- target: '[[concepts/budget-b]]'
  role: primary
  aspect: ''
- target: '[[concepts/opt]]'
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

# Best-Algorithm Benchmark Hardness for Adversarial BwK

The ratio $\mathtt{OPT}/\operatorname{\mathbb{E}}[\mathtt{REW}]$ cannot be better than $\nicefrac{{T}}{{B}}$ in the worst case. Balseiro and Gur (2019) construct this lower bound: for any time horizon $T$, any constants $0<\gamma<\rho<1$, and any algorithm there is a problem instance with budget $B=\rho T$ such that $\mathtt{OPT}/\operatorname{\mathbb{E}}[\mathtt{REW}]\geq\gamma-o(T)$. Immorlica et al. (2022) provide a simpler but weaker guarantee with only $K=2$ arms: for any time horizon $T$, any budget $B<\sqrt{T}$ and any algorithm, there is a problem instance with $\mathtt{OPT}/\operatorname{\mathbb{E}}[\mathtt{REW}]\geq T/B^{2}$.
