---
slug: chernoff-hoeffding-bounds-for-markov-chains--modification-to-achieve-spectral-expansion-1
label: Modification to achieve spectral expansion 1
claim_type: theorem
statement: Any ergodic Markov chain M with mixing time T = T(1/4) can be modified
  to a chain M' such that M' has mixing time O(T) but spectral expansion λ(M') = 1.
proof: 'For every state v in M, we ''split'' it into three states (v, in), (v, mid),
  (v, out) in M''. For every state (v, in) in M'', we set M''_{(v,in),(v,in)} = M''_{(v,in),(v,mid)}
  = 1/2. For every state (v, mid) in M'', we set M''_{(v,mid),(v,out)} = 1. For every
  pairs of states u, v in M, we set the transition probability M''_{(u,out),(v,in)}
  = M_{u,v}. The modified chain M'' is well-defined, ergodic, and satisfies the property
  that (v, mid) leaves to (v, out) with probability 1 and is the only state that transits
  to (v, out), hence λ(M'') = 1. To show M'' has mixing-time O(T), define a Markov
  chain C on three states {in, mid, out} with transition probability C_{in,in} = C_{in,mid}
  = 1/2, and C_{mid,out} = C_{out,in} = 1. C is ergodic and has constant mixing-time.
  A random walk on M'' can be decomposed into walks on M and C: every step on M''
  corresponds to a step on C in a natural way, and one step on M'' from (u, out) to
  (v, in) can be identified as a step from u to v in M. The walks on M and C are independent,
  and in expectation, every 4 steps of walk on M'' induce one step of walk on M. From
  these observations, the mixing time of M'' is at most 8T.'
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/mixing-time]]'
- '[[concepts/markov-chain-m-prime]]'
- '[[concepts/spectral-expansion-lambda-m]]'
- '[[concepts/epsilon-mixing-time-t-epsilon]]'
- '[[concepts/markov-chain-c]]'
- '[[concepts/ergodic-markov-chains]]'
about_meta:
- target: '[[concepts/mixing-time]]'
  role: primary
  aspect: ''
- target: '[[concepts/markov-chain-m-prime]]'
  role: primary
  aspect: ''
- target: '[[concepts/spectral-expansion-lambda-m]]'
  role: primary
  aspect: ''
- target: '[[concepts/epsilon-mixing-time-t-epsilon]]'
  role: primary
  aspect: ''
- target: '[[concepts/markov-chain-c]]'
  role: primary
  aspect: ''
- target: '[[concepts/ergodic-markov-chains]]'
  role: primary
  aspect: ''
depends_on: []
depends_on_meta: []
sourced_from:
- '[[sources/chernoff_hoeffding_bounds_for_markov_chains|chernoff_hoeffding_bounds_for_markov_chains]]'
sourced_from_meta:
- target: '[[sources/chernoff_hoeffding_bounds_for_markov_chains|chernoff_hoeffding_bounds_for_markov_chains]]'
  section: ''
  page: ''
  confidence: 0.0
---

# Modification to achieve spectral expansion 1

Any ergodic Markov chain M with mixing time T = T(1/4) can be modified to a chain M' such that M' has mixing time O(T) but spectral expansion λ(M') = 1.


## Proof

For every state v in M, we 'split' it into three states (v, in), (v, mid), (v, out) in M'. For every state (v, in) in M', we set M'_{(v,in),(v,in)} = M'_{(v,in),(v,mid)} = 1/2. For every state (v, mid) in M', we set M'_{(v,mid),(v,out)} = 1. For every pairs of states u, v in M, we set the transition probability M'_{(u,out),(v,in)} = M_{u,v}. The modified chain M' is well-defined, ergodic, and satisfies the property that (v, mid) leaves to (v, out) with probability 1 and is the only state that transits to (v, out), hence λ(M') = 1. To show M' has mixing-time O(T), define a Markov chain C on three states {in, mid, out} with transition probability C_{in,in} = C_{in,mid} = 1/2, and C_{mid,out} = C_{out,in} = 1. C is ergodic and has constant mixing-time. A random walk on M' can be decomposed into walks on M and C: every step on M' corresponds to a step on C in a natural way, and one step on M' from (u, out) to (v, in) can be identified as a step from u to v in M. The walks on M and C are independent, and in expectation, every 4 steps of walk on M' induce one step of walk on M. From these observations, the mixing time of M' is at most 8T.
