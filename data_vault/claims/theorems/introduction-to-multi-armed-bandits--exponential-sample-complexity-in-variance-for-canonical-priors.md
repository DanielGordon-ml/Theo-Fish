---
slug: introduction-to-multi-armed-bandits--exponential-sample-complexity-in-variance-for-canonical-priors
label: Exponential sample complexity in variance for canonical priors
claim_type: theorem
statement: 'The $\mathcal{C}$-optimal sample complexity is exponential in $\sigma_{\min}(\mathcal{C})$,
  for two canonical special cases: all per-arm priors are, resp., Beta distributions
  and truncated Gaussians. For the latter case, all per-arm priors are assumed to
  be Gaussian with the same variance $\sigma^{2}\leq 1$, conditioned to lie in $[0,1]$.
  For Beta priors, different arms may have different variances. Given a problem instance,
  the optimal sample complexity is exponential in the *second*-smallest variance,
  but only polynomial in the smallest variance.'
proof: ''
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/gaussian-distribution]]'
- '[[concepts/beta-distribution]]'
- '[[concepts/minimum-variance-sigma-min-2-c]]'
- '[[concepts/incentivized-exploration]]'
- '[[concepts/sample-complexity]]'
about_meta:
- target: '[[concepts/gaussian-distribution]]'
  role: primary
  aspect: ''
- target: '[[concepts/beta-distribution]]'
  role: primary
  aspect: ''
- target: '[[concepts/minimum-variance-sigma-min-2-c]]'
  role: primary
  aspect: ''
- target: '[[concepts/incentivized-exploration]]'
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

# Exponential sample complexity in variance for canonical priors

The $\mathcal{C}$-optimal sample complexity is exponential in $\sigma_{\min}(\mathcal{C})$, for two canonical special cases: all per-arm priors are, resp., Beta distributions and truncated Gaussians. For the latter case, all per-arm priors are assumed to be Gaussian with the same variance $\sigma^{2}\leq 1$, conditioned to lie in $[0,1]$. For Beta priors, different arms may have different variances. Given a problem instance, the optimal sample complexity is exponential in the *second*-smallest variance, but only polynomial in the smallest variance.
