---
slug: the-evolution-of-conventions--theorem-1
label: Theorem 1
claim_type: theorem
statement: Let Γ be a weakly acyclic n-person game. If k ≤ m/(L_Γ + 2) then adaptive
  play converges almost surely to a convention.
proof: 'Fix k and m, where k ≤ m/(L_Γ + 2). We shall show that there exists a positive
  integer M, and a positive probability p, such that from any state h, the probability
  is at least p that adaptive play converges within M periods to a convention. M and
  p are time-independent and state-independent. Hence the probability of not reaching
  a convention after at least rM periods is at most (1 - p)^r, which goes to zero
  as r → ∞.


  Let h = (s(t - m + 1), ..., s(t)) be the state in period t ≥ m. In period t + 1
  there is a positive probability that each of the n agents samples the last k plays
  in h, namely, (s(t - k + 1), ..., s(t)) = η. There is also a positive probability
  that, from periods t + 1 to t + k inclusive, every agent draws the sample η every
  time. Finally, there is a positive probability that, if an agent has a choice of
  several best replies to η, then he will choose the same one k times in succession.
  Thus there is a positive probability of a run (s, s, ..., s) from periods t + 1
  to t + k inclusive. Note that this argument depends on the agents'' memory being
  at least 2k - 1, since otherwise they could not choose the sample η in period t
  + k.


  Suppose that s happens to be a strict Nash equilibrium. There is a positive probability
  that, from periods t + k + 1 through t + m, each agent will sample only the last
  k plays, in which case the unique best response of each agent i is s_i. So they
  play s for m - k more periods. At this point an absorbing state has been reached,
  and they continue to play s forever.


  Suppose instead that s is not a strict Nash equilibrium. Since Γ is weakly acyclic,
  there exists a directed path s, s'', ..., s^r in the best reply graph such that
  s^r is a strict Nash equilibrium. The first edge on this path is s → s''. Let i
  be the index such that s''_{-i} = s_{-i} and s''_i is a best reply to s_{-i}. Consider
  the event in which agent i samples from the run of s established in periods t +
  1 to t + k and responds by playing s''_i, while every agent j ≠ i draws the sample
  η = (s(t - k + 1), ..., s(t)). By assumption, a best response of every agent j to
  this sample is s_j. These events occur together with positive probability, and there
  is a positive probability that they occur in every period from t + k + 1 to t +
  2k, assuming that m ≥ 3k - 1. The result is a run of s'' = (s''_i, s_{-i}) for k
  periods in succession.


  Continuing in this fashion, we see that there is a positive probability of obtaining
  a run of s, followed by a run of s'' ... followed eventually by a run of s^r. Each
  run is of length k, and the run of s^r occurs from period t + kr + 1 to t + kr +
  k. To reach this point may require that some agent look back kr + 2k - 1 periods,
  namely, from period t + kr + k to period t - k + 1. This is possible because of
  the assumption that k ≤ m/(L_Γ + 2).


  After this, the process can converge to the absorbing state (s^r, s^r, ..., s^r)
  by period t + kr + m if each agent samples the previous k plays from periods t +
  kr + k + 1 to t + kr + m inclusive.


  Since r ≤ L_Γ, we have established that, given an initial state h, there is a probability
  p_h > 0 of converging to an absorbing state within M = kL_Γ + m periods. Letting
  p = min_{h ∈ H} p_h > 0, it follows that from any initial state the process converges
  with probability at least p to an absorbing state within at most M periods. This
  completes the proof.'
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/adaptive-play-without-mistakes]]'
- '[[concepts/convention]]'
- '[[concepts/strict-nash-equilibrium]]'
- '[[concepts/best-reply-graph]]'
- '[[concepts/adaptive-play]]'
- '[[concepts/path-length-l-s]]'
- '[[concepts/convergence-of-adaptive-play]]'
- '[[concepts/weakly-acyclic-game]]'
- '[[concepts/sampling-parameter-k]]'
- '[[concepts/absorbing-state]]'
- '[[concepts/memory-parameter-m]]'
- '[[concepts/adaptive-play]]'
- '[[concepts/strict-nash-equilibrium]]'
- '[[concepts/memory-parameter-m]]'
- '[[concepts/sampling-parameter-k]]'
- '[[concepts/adaptive-play-without-mistakes]]'
- '[[concepts/weakly-acyclic-game]]'
- '[[concepts/best-reply-graph]]'
- '[[concepts/convergence-of-adaptive-play]]'
- '[[concepts/absorbing-state]]'
- '[[concepts/path-length-l-s]]'
- '[[concepts/convention]]'
about_meta:
- target: '[[concepts/adaptive-play-without-mistakes]]'
  role: primary
  aspect: ''
- target: '[[concepts/convention]]'
  role: primary
  aspect: ''
- target: '[[concepts/strict-nash-equilibrium]]'
  role: primary
  aspect: ''
- target: '[[concepts/best-reply-graph]]'
  role: primary
  aspect: ''
- target: '[[concepts/adaptive-play]]'
  role: primary
  aspect: ''
- target: '[[concepts/path-length-l-s]]'
  role: primary
  aspect: ''
- target: '[[concepts/convergence-of-adaptive-play]]'
  role: primary
  aspect: ''
- target: '[[concepts/weakly-acyclic-game]]'
  role: primary
  aspect: ''
- target: '[[concepts/sampling-parameter-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/absorbing-state]]'
  role: primary
  aspect: ''
- target: '[[concepts/memory-parameter-m]]'
  role: primary
  aspect: ''
- target: '[[concepts/adaptive-play]]'
  role: primary
  aspect: ''
- target: '[[concepts/strict-nash-equilibrium]]'
  role: primary
  aspect: ''
- target: '[[concepts/memory-parameter-m]]'
  role: primary
  aspect: ''
- target: '[[concepts/sampling-parameter-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/adaptive-play-without-mistakes]]'
  role: primary
  aspect: ''
- target: '[[concepts/weakly-acyclic-game]]'
  role: primary
  aspect: ''
- target: '[[concepts/best-reply-graph]]'
  role: primary
  aspect: ''
- target: '[[concepts/convergence-of-adaptive-play]]'
  role: primary
  aspect: ''
- target: '[[concepts/absorbing-state]]'
  role: primary
  aspect: ''
- target: '[[concepts/path-length-l-s]]'
  role: primary
  aspect: ''
- target: '[[concepts/convention]]'
  role: primary
  aspect: ''
depends_on:
- '[[claims/the-evolution-of-conventions--proposition-1]]'
- '[[claims/the-evolution-of-conventions--proposition-1]]'
depends_on_meta:
- target: '[[claims/the-evolution-of-conventions--proposition-1]]'
- target: '[[claims/the-evolution-of-conventions--proposition-1]]'
sourced_from:
- '[[sources/the_evolution_of_conventions|the_evolution_of_conventions]]'
sourced_from_meta:
- target: '[[sources/the_evolution_of_conventions|the_evolution_of_conventions]]'
  section: ''
  page: ''
  confidence: 0.0
---

# Theorem 1

Let Γ be a weakly acyclic n-person game. If k ≤ m/(L_Γ + 2) then adaptive play converges almost surely to a convention.


## Proof

Fix k and m, where k ≤ m/(L_Γ + 2). We shall show that there exists a positive integer M, and a positive probability p, such that from any state h, the probability is at least p that adaptive play converges within M periods to a convention. M and p are time-independent and state-independent. Hence the probability of not reaching a convention after at least rM periods is at most (1 - p)^r, which goes to zero as r → ∞.

Let h = (s(t - m + 1), ..., s(t)) be the state in period t ≥ m. In period t + 1 there is a positive probability that each of the n agents samples the last k plays in h, namely, (s(t - k + 1), ..., s(t)) = η. There is also a positive probability that, from periods t + 1 to t + k inclusive, every agent draws the sample η every time. Finally, there is a positive probability that, if an agent has a choice of several best replies to η, then he will choose the same one k times in succession. Thus there is a positive probability of a run (s, s, ..., s) from periods t + 1 to t + k inclusive. Note that this argument depends on the agents' memory being at least 2k - 1, since otherwise they could not choose the sample η in period t + k.

Suppose that s happens to be a strict Nash equilibrium. There is a positive probability that, from periods t + k + 1 through t + m, each agent will sample only the last k plays, in which case the unique best response of each agent i is s_i. So they play s for m - k more periods. At this point an absorbing state has been reached, and they continue to play s forever.

Suppose instead that s is not a strict Nash equilibrium. Since Γ is weakly acyclic, there exists a directed path s, s', ..., s^r in the best reply graph such that s^r is a strict Nash equilibrium. The first edge on this path is s → s'. Let i be the index such that s'_{-i} = s_{-i} and s'_i is a best reply to s_{-i}. Consider the event in which agent i samples from the run of s established in periods t + 1 to t + k and responds by playing s'_i, while every agent j ≠ i draws the sample η = (s(t - k + 1), ..., s(t)). By assumption, a best response of every agent j to this sample is s_j. These events occur together with positive probability, and there is a positive probability that they occur in every period from t + k + 1 to t + 2k, assuming that m ≥ 3k - 1. The result is a run of s' = (s'_i, s_{-i}) for k periods in succession.

Continuing in this fashion, we see that there is a positive probability of obtaining a run of s, followed by a run of s' ... followed eventually by a run of s^r. Each run is of length k, and the run of s^r occurs from period t + kr + 1 to t + kr + k. To reach this point may require that some agent look back kr + 2k - 1 periods, namely, from period t + kr + k to period t - k + 1. This is possible because of the assumption that k ≤ m/(L_Γ + 2).

After this, the process can converge to the absorbing state (s^r, s^r, ..., s^r) by period t + kr + m if each agent samples the previous k plays from periods t + kr + k + 1 to t + kr + m inclusive.

Since r ≤ L_Γ, we have established that, given an initial state h, there is a probability p_h > 0 of converging to an absorbing state within M = kL_Γ + m periods. Letting p = min_{h ∈ H} p_h > 0, it follows that from any initial state the process converges with probability at least p to an absorbing state within at most M periods. This completes the proof.
