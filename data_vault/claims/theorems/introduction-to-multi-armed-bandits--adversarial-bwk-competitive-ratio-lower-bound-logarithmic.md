---
slug: introduction-to-multi-armed-bandits--adversarial-bwk-competitive-ratio-lower-bound-logarithmic
label: Adversarial BwK Competitive Ratio Lower Bound (logarithmic)
claim_type: theorem
statement: For any $B \leq T$ and any algorithm, there is a problem instance with
  budget $B$ and time horizon $T$ such that $\mathtt{OPT_{FD}}/\operatorname{\mathbb{E}}[\mathtt{REW}]
  \geq \tfrac{1}{2}\ln{\lceil{\nicefrac{{T}}{{B}}}\rceil}+\zeta-\tilde{O}(1/\sqrt{B})$,
  where $\zeta=0.577...$ is the Euler-Mascheroni constant.
proof: A more elaborate version of the two-phase example, with $\Omega(\nicefrac{{T}}{{B}})$
  phases rather than two, proves that competitive ratio can be no better than $\Omega(\log
  \nicefrac{T}{B})$.
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/adversarial-bwk]]'
- '[[concepts/bandits-with-knapsacks]]'
- '[[concepts/opt-fd]]'
- '[[concepts/budget-b]]'
about_meta:
- target: '[[concepts/adversarial-bwk]]'
  role: primary
  aspect: ''
- target: '[[concepts/bandits-with-knapsacks]]'
  role: primary
  aspect: ''
- target: '[[concepts/opt-fd]]'
  role: primary
  aspect: ''
- target: '[[concepts/budget-b]]'
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

# Adversarial BwK Competitive Ratio Lower Bound (logarithmic)

For any $B \leq T$ and any algorithm, there is a problem instance with budget $B$ and time horizon $T$ such that $\mathtt{OPT_{FD}}/\operatorname{\mathbb{E}}[\mathtt{REW}] \geq \tfrac{1}{2}\ln{\lceil{\nicefrac{{T}}{{B}}}\rceil}+\zeta-\tilde{O}(1/\sqrt{B})$, where $\zeta=0.577...$ is the Euler-Mascheroni constant.


## Proof

A more elaborate version of the two-phase example, with $\Omega(\nicefrac{{T}}{{B}})$ phases rather than two, proves that competitive ratio can be no better than $\Omega(\log \nicefrac{T}{B})$.
