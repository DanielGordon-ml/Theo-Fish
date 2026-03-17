---
slug: introduction-to-multi-armed-bandits--equation-2
label: Equation (2)
claim_type: lemma
statement: For each action $a$ after the exploration phase of the Explore-First algorithm
  with parameter $N$, the average reward $\bar{\mu}(a)$ satisfies $\Pr\left[\,|\bar{\mu}(a)-\mu(a)|\leq\mathtt{rad}\,\right]\geq
  1-\nicefrac{2}{T^{4}}$, where $\mathtt{rad}:=\sqrt{2\log(T)\,/\,N}$.
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/confidence-radius]]'
- '[[concepts/hoeffding-inequality]]'
- '[[concepts/average-reward-mu-a]]'
- '[[concepts/true-expected-reward-mu-a]]'
- '[[concepts/explore-first-algorithm]]'
- '[[concepts/parameter-n]]'
about_meta:
- target: '[[concepts/confidence-radius]]'
  role: primary
  aspect: ''
- target: '[[concepts/hoeffding-inequality]]'
  role: primary
  aspect: ''
- target: '[[concepts/average-reward-mu-a]]'
  role: primary
  aspect: ''
- target: '[[concepts/true-expected-reward-mu-a]]'
  role: primary
  aspect: ''
- target: '[[concepts/explore-first-algorithm]]'
  role: primary
  aspect: ''
- target: '[[concepts/parameter-n]]'
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

# Equation (2)

For each action $a$ after the exploration phase of the Explore-First algorithm with parameter $N$, the average reward $\bar{\mu}(a)$ satisfies $\Pr\left[\,|\bar{\mu}(a)-\mu(a)|\leq\mathtt{rad}\,\right]\geq 1-\nicefrac{2}{T^{4}}$, where $\mathtt{rad}:=\sqrt{2\log(T)\,/\,N}$.
