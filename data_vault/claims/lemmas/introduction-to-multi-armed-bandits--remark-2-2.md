---
slug: introduction-to-multi-armed-bandits--remark-2-2
label: Remark 2.2
claim_type: lemma
statement: 'Note that (ii) implies (i), because if regret is high in expectation over
  problem instances, then there exists at least one problem instance with high regret.
  Conversely, (i) implies (ii) if $|\mathcal{F}|$ is a constant: indeed, if we have
  high regret $H$ for some problem instance in $\mathcal{F}$, then in expectation
  over a uniform distribution over $\mathcal{F}$ regret is at least $H/|\mathcal{F}|$.
  However, this argument breaks if $|\mathcal{F}|$ is large. Yet, a stronger version
  of (i) which says that regret is high for a constant fraction of the instances in
  $\mathcal{F}$ implies (ii), with uniform distribution over the instances, regardless
  of how large $|\mathcal{F}|$ is.'
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/expected-regret]]'
- '[[concepts/bandit-algorithm]]'
- '[[concepts/family-of-problem-instances]]'
about_meta:
- target: '[[concepts/expected-regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/bandit-algorithm]]'
  role: primary
  aspect: ''
- target: '[[concepts/family-of-problem-instances]]'
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

# Remark 2.2

Note that (ii) implies (i), because if regret is high in expectation over problem instances, then there exists at least one problem instance with high regret. Conversely, (i) implies (ii) if $|\mathcal{F}|$ is a constant: indeed, if we have high regret $H$ for some problem instance in $\mathcal{F}$, then in expectation over a uniform distribution over $\mathcal{F}$ regret is at least $H/|\mathcal{F}|$. However, this argument breaks if $|\mathcal{F}|$ is large. Yet, a stronger version of (i) which says that regret is high for a constant fraction of the instances in $\mathcal{F}$ implies (ii), with uniform distribution over the instances, regardless of how large $|\mathcal{F}|$ is.
