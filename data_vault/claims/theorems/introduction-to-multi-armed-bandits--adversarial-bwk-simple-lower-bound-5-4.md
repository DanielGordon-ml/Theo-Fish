---
slug: introduction-to-multi-armed-bandits--adversarial-bwk-simple-lower-bound-5-4
label: Adversarial BwK Simple Lower Bound (5/4)
claim_type: theorem
statement: There are two arms and one resource with budget $\nicefrac{{T}}{{2}}$.
  Arm $1$ has zero rewards and zero consumption. Arm $2$ has consumption $1$ in each
  round, and offers reward $\nicefrac{{1}}{{2}}$ in each round of the first half-time
  ($\nicefrac{{T}}{{2}}$ rounds). In the second half-time, it offers either reward
  $1$ in all rounds, or reward 0 in all rounds. Thus, there are two problem instances
  that coincide for the first half-time and differ in the second half-time. Any choice
  leads to competitive ratio at least $\nicefrac{{5}}{{4}}$ on one of the two instances.
proof: The algorithm needs to choose how much budget to invest in the first half-time,
  without knowing what comes in the second. Any choice leads to competitive ratio
  at least $\nicefrac{{5}}{{4}}$ on one of the two instances.
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/opt-fd]]'
- '[[concepts/adversarial-bwk]]'
- '[[concepts/bandits-with-knapsacks]]'
about_meta:
- target: '[[concepts/opt-fd]]'
  role: primary
  aspect: ''
- target: '[[concepts/adversarial-bwk]]'
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

# Adversarial BwK Simple Lower Bound (5/4)

There are two arms and one resource with budget $\nicefrac{{T}}{{2}}$. Arm $1$ has zero rewards and zero consumption. Arm $2$ has consumption $1$ in each round, and offers reward $\nicefrac{{1}}{{2}}$ in each round of the first half-time ($\nicefrac{{T}}{{2}}$ rounds). In the second half-time, it offers either reward $1$ in all rounds, or reward 0 in all rounds. Thus, there are two problem instances that coincide for the first half-time and differ in the second half-time. Any choice leads to competitive ratio at least $\nicefrac{{5}}{{4}}$ on one of the two instances.


## Proof

The algorithm needs to choose how much budget to invest in the first half-time, without knowing what comes in the second. Any choice leads to competitive ratio at least $\nicefrac{{5}}{{4}}$ on one of the two instances.
