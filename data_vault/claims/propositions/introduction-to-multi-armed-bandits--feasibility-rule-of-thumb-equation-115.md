---
slug: introduction-to-multi-armed-bandits--feasibility-rule-of-thumb-equation-115
label: Feasibility Rule-of-Thumb (Equation 115)
claim_type: proposition
statement: For policy training algorithms based on linear classifiers, a good rule-of-thumb
  is that the stationarity timescale should be much larger than the typical delay,
  and moreover we should have $\mathtt{StatInterval} \times \mathtt{DataRate} \times
  \mathtt{RareEventFreq} \gg \mathtt{\#actions} \times \mathtt{\#features}$. The left-hand
  side is the number of rare events in the timescale, and the right-hand side characterizes
  the complexity of the learning problem.
proof: ''
strength: approximate
status: unverified
human_notes: ''
about:
- '[[concepts/contextual-bandits]]'
- '[[concepts/rare-event-frequency]]'
- '[[concepts/stationarity-timescale]]'
- '[[concepts/number-of-features]]'
- '[[concepts/linear-contextual-bandits]]'
- '[[concepts/data-rate]]'
- '[[concepts/policy-training]]'
about_meta:
- target: '[[concepts/contextual-bandits]]'
  role: primary
  aspect: ''
- target: '[[concepts/rare-event-frequency]]'
  role: primary
  aspect: ''
- target: '[[concepts/stationarity-timescale]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-features]]'
  role: primary
  aspect: ''
- target: '[[concepts/linear-contextual-bandits]]'
  role: primary
  aspect: ''
- target: '[[concepts/data-rate]]'
  role: primary
  aspect: ''
- target: '[[concepts/policy-training]]'
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

# Feasibility Rule-of-Thumb (Equation 115)

For policy training algorithms based on linear classifiers, a good rule-of-thumb is that the stationarity timescale should be much larger than the typical delay, and moreover we should have $\mathtt{StatInterval} \times \mathtt{DataRate} \times \mathtt{RareEventFreq} \gg \mathtt{\#actions} \times \mathtt{\#features}$. The left-hand side is the number of rare events in the timescale, and the right-hand side characterizes the complexity of the learning problem.
