---
slug: introduction-to-multi-armed-bandits--price-of-incentives-upper-bound-sellke-and-slivkins-2022
label: Price of Incentives upper bound (Sellke and Slivkins 2022)
claim_type: theorem
statement: Since Thompson Sampling is BIC with a warm-start (and, arguably, a reasonable
  benchmark to compare against), the $\mathtt{PoI}$ is only additive, arising due
  to collecting data for the warm-start. The $\mathtt{PoI}$ is upper-bounded by the
  sample complexity of collecting this data. The sufficient number of data points
  per arm, denote it $N$, is $N=O(K)$ under very mild assumptions, and even $N=O(\log
  K)$ for Beta priors with bounded variance. In particular, the $\mathtt{PoI}$ is
  $O_{\mathcal{C}}(K)$ if $\mathtt{minsupp}(\mathcal{C})>\Phi_{\mathcal{C}}$.
proof: ''
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/price-of-incentives-poi]]'
- '[[concepts/warm-start]]'
- '[[concepts/thompson-sampling]]'
- '[[concepts/bic-bayesian-incentive-compatible]]'
- '[[concepts/sample-complexity]]'
about_meta:
- target: '[[concepts/price-of-incentives-poi]]'
  role: primary
  aspect: ''
- target: '[[concepts/warm-start]]'
  role: primary
  aspect: ''
- target: '[[concepts/thompson-sampling]]'
  role: primary
  aspect: ''
- target: '[[concepts/bic-bayesian-incentive-compatible]]'
  role: primary
  aspect: ''
- target: '[[concepts/sample-complexity]]'
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

# Price of Incentives upper bound (Sellke and Slivkins 2022)

Since Thompson Sampling is BIC with a warm-start (and, arguably, a reasonable benchmark to compare against), the $\mathtt{PoI}$ is only additive, arising due to collecting data for the warm-start. The $\mathtt{PoI}$ is upper-bounded by the sample complexity of collecting this data. The sufficient number of data points per arm, denote it $N$, is $N=O(K)$ under very mild assumptions, and even $N=O(\log K)$ for Beta priors with bounded variance. In particular, the $\mathtt{PoI}$ is $O_{\mathcal{C}}(K)$ if $\mathtt{minsupp}(\mathcal{C})>\Phi_{\mathcal{C}}$.
