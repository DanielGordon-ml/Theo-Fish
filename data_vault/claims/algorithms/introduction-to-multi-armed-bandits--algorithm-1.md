---
slug: introduction-to-multi-armed-bandits--algorithm-1
label: Algorithm 1
claim_type: algorithm
statement: Reduction from bandit feedback to full feedback. For each arm, we create
  an expert which always recommends this arm. We use Hedge with this set of experts.
  In each round t, we use the expert e_t chosen by Hedge to pick an arm a_t, and define
  "fake costs" \widehat{c}_t(\cdot) on all experts in order to provide Hedge with
  valid inputs.
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/adversarial-bandits-problem]]'
- '[[concepts/bandit-feedback]]'
- '[[concepts/fake-cost-function-on-expert]]'
- '[[concepts/full-feedback]]'
- '[[concepts/exp3]]'
- '[[concepts/hedge]]'
- '[[concepts/fake-cost-function-on-arm]]'
about_meta:
- target: '[[concepts/adversarial-bandits-problem]]'
  role: primary
  aspect: ''
- target: '[[concepts/bandit-feedback]]'
  role: primary
  aspect: ''
- target: '[[concepts/fake-cost-function-on-expert]]'
  role: primary
  aspect: ''
- target: '[[concepts/full-feedback]]'
  role: primary
  aspect: ''
- target: '[[concepts/exp3]]'
  role: primary
  aspect: ''
- target: '[[concepts/hedge]]'
  role: primary
  aspect: ''
- target: '[[concepts/fake-cost-function-on-arm]]'
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

# Algorithm 1

Reduction from bandit feedback to full feedback. For each arm, we create an expert which always recommends this arm. We use Hedge with this set of experts. In each round t, we use the expert e_t chosen by Hedge to pick an arm a_t, and define "fake costs" \widehat{c}_t(\cdot) on all experts in order to provide Hedge with valid inputs.
