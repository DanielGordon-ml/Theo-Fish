---
slug: introduction-to-multi-armed-bandits--adversarial-bwk-near-optimal-competitive-ratio-in-expectation-equation-157
label: Adversarial BwK Near-Optimal Competitive Ratio in Expectation (Equation 157)
claim_type: theorem
statement: 'One can achieve a near-optimal competitive ratio, $(\mathtt{OPT_{FD}}-\mathtt{reg})/\operatorname{\mathbb{E}}[\mathtt{REW}]\leq
  O_{d}(\log T)$, up to a regret term $\mathtt{reg}=O(1+\tfrac{\mathtt{OPT_{FD}}}{dB})\sqrt{TK\log(Td)}$.
  This is achieved using a version of $\mathtt{LagrangeBwK}$ algorithm, with two important
  differences: the time resource is not included in the outcome matrices, and the
  $\nicefrac{{T}}{{B}}$ ratio in the Lagrange function (146) is replaced by a parameter
  $\gamma\in(0,\nicefrac{{T}}{{B}}]$, sampled at random from some exponential scale.'
proof: The initial analysis in Immorlica et al. (2022) obtains (157) with competitive
  ratio $\tfrac{d+1}{2}\ln T$. Kesselheim and Singla (2020) refine this analysis to
  (157) with competitive ratio $O\left(\,\log(d)\,\log(T)\,\right)$. When $\gamma$
  is sampled close to $\mathtt{OPT_{FD}}/B$, the algorithm obtains a constant competitive
  ratio. A completely new analysis of $\mathtt{LagrangeBwK}$ is needed, as the zero-games
  framework from Chapter 9 is no longer applicable.
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/time-horizon-t]]'
- '[[concepts/adversarial-bwk]]'
- '[[concepts/bandits-with-knapsacks]]'
- '[[concepts/opt-fd]]'
- '[[concepts/lagrangebwk]]'
- '[[concepts/number-of-arms-k]]'
about_meta:
- target: '[[concepts/time-horizon-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/adversarial-bwk]]'
  role: primary
  aspect: ''
- target: '[[concepts/bandits-with-knapsacks]]'
  role: primary
  aspect: ''
- target: '[[concepts/opt-fd]]'
  role: primary
  aspect: ''
- target: '[[concepts/lagrangebwk]]'
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

# Adversarial BwK Near-Optimal Competitive Ratio in Expectation (Equation 157)

One can achieve a near-optimal competitive ratio, $(\mathtt{OPT_{FD}}-\mathtt{reg})/\operatorname{\mathbb{E}}[\mathtt{REW}]\leq O_{d}(\log T)$, up to a regret term $\mathtt{reg}=O(1+\tfrac{\mathtt{OPT_{FD}}}{dB})\sqrt{TK\log(Td)}$. This is achieved using a version of $\mathtt{LagrangeBwK}$ algorithm, with two important differences: the time resource is not included in the outcome matrices, and the $\nicefrac{{T}}{{B}}$ ratio in the Lagrange function (146) is replaced by a parameter $\gamma\in(0,\nicefrac{{T}}{{B}}]$, sampled at random from some exponential scale.


## Proof

The initial analysis in Immorlica et al. (2022) obtains (157) with competitive ratio $\tfrac{d+1}{2}\ln T$. Kesselheim and Singla (2020) refine this analysis to (157) with competitive ratio $O\left(\,\log(d)\,\log(T)\,\right)$. When $\gamma$ is sampled close to $\mathtt{OPT_{FD}}/B$, the algorithm obtains a constant competitive ratio. A completely new analysis of $\mathtt{LagrangeBwK}$ is needed, as the zero-games framework from Chapter 9 is no longer applicable.
