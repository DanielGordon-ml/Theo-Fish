---
slug: the-evolution-of-conventions--absorbing-state-characterization
label: Absorbing State Characterization
claim_type: theorem
statement: h is an absorbing state of the process P^0 if and only if it consists of
  a strict pure strategy Nash equilibrium played m times in succession.
proof: Suppose that h = (s^1, ..., s^m) is an absorbing state. For each agent i let
  s_i be i's best reply to some subset of k plays drawn from h, and let s = (s_1,
  ..., s_n). By assumption, there is a positive probability of moving from h to h'
  = (s^2, ..., s^m, s) in one period. Since h is absorbing, h = h' and hence s^1 =
  s^2. Continuing in this fashion we conclude that s^1 = s^2 = ... = s^m = s. Hence
  h = (s, s, ..., s). By construction, s_i is a best reply to some sample of k elements
  from h. Hence s_i is a best reply to s_{-i} for each i. It must also be a unique
  best reply to s_{-i}, because otherwise the process could move to a successor that
  is different from h. So s is a strict, pure strategy Nash equilibrium. Conversely,
  any state h consisting of m repetitions of a strict, pure strategy Nash equilibrium
  is clearly an absorbing state.
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/strict-pure-strategy-nash-equilibrium]]'
- '[[concepts/convention]]'
- '[[concepts/adaptive-play-without-mistakes]]'
- '[[concepts/best-reply-distribution]]'
- '[[concepts/markov-chain-p-0]]'
- '[[concepts/strict-nash-equilibrium]]'
- '[[concepts/sample-size-k]]'
- '[[concepts/memory-m]]'
- '[[concepts/absorbing-state]]'
about_meta:
- target: '[[concepts/strict-pure-strategy-nash-equilibrium]]'
  role: primary
  aspect: ''
- target: '[[concepts/convention]]'
  role: primary
  aspect: ''
- target: '[[concepts/adaptive-play-without-mistakes]]'
  role: primary
  aspect: ''
- target: '[[concepts/best-reply-distribution]]'
  role: primary
  aspect: ''
- target: '[[concepts/markov-chain-p-0]]'
  role: primary
  aspect: ''
- target: '[[concepts/strict-nash-equilibrium]]'
  role: primary
  aspect: ''
- target: '[[concepts/sample-size-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/memory-m]]'
  role: primary
  aspect: ''
- target: '[[concepts/absorbing-state]]'
  role: primary
  aspect: ''
depends_on: []
depends_on_meta: []
sourced_from:
- '[[sources/the_evolution_of_conventions|the_evolution_of_conventions]]'
sourced_from_meta:
- target: '[[sources/the_evolution_of_conventions|the_evolution_of_conventions]]'
  section: ''
  page: ''
  confidence: 0.0
---

# Absorbing State Characterization

h is an absorbing state of the process P^0 if and only if it consists of a strict pure strategy Nash equilibrium played m times in succession.


## Proof

Suppose that h = (s^1, ..., s^m) is an absorbing state. For each agent i let s_i be i's best reply to some subset of k plays drawn from h, and let s = (s_1, ..., s_n). By assumption, there is a positive probability of moving from h to h' = (s^2, ..., s^m, s) in one period. Since h is absorbing, h = h' and hence s^1 = s^2. Continuing in this fashion we conclude that s^1 = s^2 = ... = s^m = s. Hence h = (s, s, ..., s). By construction, s_i is a best reply to some sample of k elements from h. Hence s_i is a best reply to s_{-i} for each i. It must also be a unique best reply to s_{-i}, because otherwise the process could move to a successor that is different from h. So s is a strict, pure strategy Nash equilibrium. Conversely, any state h consisting of m repetitions of a strict, pure strategy Nash equilibrium is clearly an absorbing state.
