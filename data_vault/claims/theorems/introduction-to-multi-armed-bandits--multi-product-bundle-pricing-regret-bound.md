---
slug: introduction-to-multi-armed-bandits--multi-product-bundle-pricing-regret-bound
label: Multi-product bundle pricing regret bound
claim_type: theorem
statement: When there are multiple feasible bundles of goods, and in each round the
  algorithm chooses a bundle and a price, the technique from the single-product case
  applies, and one obtains a regret bound of Õ(n · B^{2/3} · (Nℓ)^{1/3}), where N
  is the number of bundles, each bundle consists of at most ℓ items, and prices are
  in the range [0, ℓ] (Badanidiyuru et al., 2013, 2018).
proof: ''
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/number-of-copies]]'
- '[[concepts/regret]]'
- '[[concepts/dynamic-pricing-with-multiple-products]]'
- '[[concepts/bandits-with-knapsacks]]'
about_meta:
- target: '[[concepts/number-of-copies]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/dynamic-pricing-with-multiple-products]]'
  role: primary
  aspect: ''
- target: '[[concepts/bandits-with-knapsacks]]'
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

# Multi-product bundle pricing regret bound

When there are multiple feasible bundles of goods, and in each round the algorithm chooses a bundle and a price, the technique from the single-product case applies, and one obtains a regret bound of Õ(n · B^{2/3} · (Nℓ)^{1/3}), where N is the number of bundles, each bundle consists of at most ℓ items, and prices are in the range [0, ℓ] (Badanidiyuru et al., 2013, 2018).
