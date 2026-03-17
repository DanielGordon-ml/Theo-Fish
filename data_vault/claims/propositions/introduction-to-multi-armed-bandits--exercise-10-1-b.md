---
slug: introduction-to-multi-armed-bandits--exercise-10-1-b
label: Exercise 10.1(b)
claim_type: proposition
statement: Fix time horizon T and budget B. Consider an algorithm ALG which explores
  uniformly at random for the first N steps, where N is fixed in advance, then chooses
  some distribution D over arms and draws independently from this distribution in
  each subsequent rounds. Assume B > Ω(T). Then N and D can be chosen so that ALG
  achieves regret OPT - E[REW] < Õ(T^{2/3}).
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/regret-r-t]]'
- '[[concepts/linear-program-150]]'
- '[[concepts/budget-b]]'
- '[[concepts/explore-first]]'
- '[[concepts/bandits-with-knapsacks]]'
about_meta:
- target: '[[concepts/regret-r-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/linear-program-150]]'
  role: primary
  aspect: ''
- target: '[[concepts/budget-b]]'
  role: primary
  aspect: ''
- target: '[[concepts/explore-first]]'
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

# Exercise 10.1(b)

Fix time horizon T and budget B. Consider an algorithm ALG which explores uniformly at random for the first N steps, where N is fixed in advance, then chooses some distribution D over arms and draws independently from this distribution in each subsequent rounds. Assume B > Ω(T). Then N and D can be chosen so that ALG achieves regret OPT - E[REW] < Õ(T^{2/3}).
