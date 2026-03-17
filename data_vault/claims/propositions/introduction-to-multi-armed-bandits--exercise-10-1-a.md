---
slug: introduction-to-multi-armed-bandits--exercise-10-1-a
label: Exercise 10.1(a)
claim_type: proposition
statement: 'Fix time horizon T and budget B. Consider an algorithm ALG which explores
  uniformly at random for the first N steps, where N is fixed in advance, then chooses
  some distribution D over arms and draws independently from this distribution in
  each subsequent rounds. Assume B < √T. Then there exists a problem instance on which
  ALG suffers linear regret: OPT - E[REW] > Ω(T).'
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/budget-b]]'
- '[[concepts/explore-first]]'
- '[[concepts/time-horizon-t]]'
- '[[concepts/bandits-with-knapsacks]]'
- '[[concepts/regret-r-t]]'
about_meta:
- target: '[[concepts/budget-b]]'
  role: primary
  aspect: ''
- target: '[[concepts/explore-first]]'
  role: primary
  aspect: ''
- target: '[[concepts/time-horizon-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/bandits-with-knapsacks]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret-r-t]]'
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

# Exercise 10.1(a)

Fix time horizon T and budget B. Consider an algorithm ALG which explores uniformly at random for the first N steps, where N is fixed in advance, then chooses some distribution D over arms and draws independently from this distribution in each subsequent rounds. Assume B < √T. Then there exists a problem instance on which ALG suffers linear regret: OPT - E[REW] > Ω(T).
