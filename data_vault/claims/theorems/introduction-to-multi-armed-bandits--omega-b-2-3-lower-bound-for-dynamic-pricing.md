---
slug: introduction-to-multi-armed-bandits--omega-b-2-3-lower-bound-for-dynamic-pricing
label: Ω(B^{2/3}) lower bound for dynamic pricing
claim_type: theorem
statement: 'The regret rate Õ(B^{2/3}) is optimal for dynamic pricing, for any given
  B, T: a complementary Ω(B^{2/3}) lower bound has been proved in Babaioff et al.
  (2015a), even against the best fixed price.'
proof: The lower bound is proved in Babaioff et al. (2015a) via a reduction to the
  respective lower bounds from Kleinberg and Leighton (2003) for the unconstrained
  case (B=T). The latter lower bounds encapsulate most of the 'heavy lifting' in the
  analysis.
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/regret]]'
- '[[concepts/number-of-copies]]'
- '[[concepts/dynamic-pricing]]'
- '[[concepts/best-fixed-price-reward]]'
about_meta:
- target: '[[concepts/regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-copies]]'
  role: primary
  aspect: ''
- target: '[[concepts/dynamic-pricing]]'
  role: primary
  aspect: ''
- target: '[[concepts/best-fixed-price-reward]]'
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

# Ω(B^{2/3}) lower bound for dynamic pricing

The regret rate Õ(B^{2/3}) is optimal for dynamic pricing, for any given B, T: a complementary Ω(B^{2/3}) lower bound has been proved in Babaioff et al. (2015a), even against the best fixed price.


## Proof

The lower bound is proved in Babaioff et al. (2015a) via a reduction to the respective lower bounds from Kleinberg and Leighton (2003) for the unconstrained case (B=T). The latter lower bounds encapsulate most of the 'heavy lifting' in the analysis.
