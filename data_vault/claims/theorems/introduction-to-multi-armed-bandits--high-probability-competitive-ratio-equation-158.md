---
slug: introduction-to-multi-armed-bandits--high-probability-competitive-ratio-equation-158
label: High-Probability Competitive Ratio (Equation 158)
claim_type: theorem
statement: 'One can achieve an $O(d\log T)$ competitive ratio with high probability:
  $\Pr\left[\,(\mathtt{OPT_{FD}}-\mathtt{reg})/\mathtt{REW}\leq O(d\log T)\,\right]\geq
  1-T^{-2}$, with a somewhat larger regret term $\mathtt{reg}$. This result uses $\mathtt{LagrangeBwK}$
  as a subroutine, and its analysis as a key lemma. The algorithm is considerably
  more involved: instead of guessing the parameter $\gamma$ upfront, the guess is
  iteratively refined over time.'
proof: ''
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/number-of-resources-d]]'
- '[[concepts/bandits-with-knapsacks]]'
- '[[concepts/lagrangebwk]]'
- '[[concepts/adversarial-bwk]]'
- '[[concepts/high-probability-regret]]'
about_meta:
- target: '[[concepts/number-of-resources-d]]'
  role: primary
  aspect: ''
- target: '[[concepts/bandits-with-knapsacks]]'
  role: primary
  aspect: ''
- target: '[[concepts/lagrangebwk]]'
  role: primary
  aspect: ''
- target: '[[concepts/adversarial-bwk]]'
  role: primary
  aspect: ''
- target: '[[concepts/high-probability-regret]]'
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

# High-Probability Competitive Ratio (Equation 158)

One can achieve an $O(d\log T)$ competitive ratio with high probability: $\Pr\left[\,(\mathtt{OPT_{FD}}-\mathtt{reg})/\mathtt{REW}\leq O(d\log T)\,\right]\geq 1-T^{-2}$, with a somewhat larger regret term $\mathtt{reg}$. This result uses $\mathtt{LagrangeBwK}$ as a subroutine, and its analysis as a key lemma. The algorithm is considerably more involved: instead of guessing the parameter $\gamma$ upfront, the guess is iteratively refined over time.
