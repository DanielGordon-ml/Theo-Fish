---
slug: introduction-to-multi-armed-bandits--epsilon-regret-bound-for-many-arms-kleinberg-2006
label: ε-regret bound for many arms (Kleinberg 2006)
claim_type: theorem
statement: If there are too many arms (and no helpful additional structure), then
  perhaps competing against the best arm is perhaps too much to ask for. But suppose
  we relax the benchmark so that it ignores the best ε-fraction of arms, for some
  fixed ε>0. We are interested in regret relative to the best remaining arm, call
  it ε-regret for brevity. One can think of 1/ε as an effective number of arms. Kleinberg
  (2006) achieves ε-regret of the form (1/ε) · T^{2/3} · polylog(T). The algorithm
  is very simple, based on a version of the 'doubling trick' described above, although
  the analysis is somewhat subtle. This result allows the ε-fraction to be defined
  relative to an arbitrary 'base distribution' on arms, and extends to infinitely
  many arms.
proof: ''
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/number-of-arms-k]]'
- '[[concepts/epsilon-regret]]'
- '[[concepts/doubling-trick]]'
- '[[concepts/time-horizon-t]]'
- '[[concepts/regret-bound]]'
about_meta:
- target: '[[concepts/number-of-arms-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/epsilon-regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/doubling-trick]]'
  role: primary
  aspect: ''
- target: '[[concepts/time-horizon-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret-bound]]'
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

# ε-regret bound for many arms (Kleinberg 2006)

If there are too many arms (and no helpful additional structure), then perhaps competing against the best arm is perhaps too much to ask for. But suppose we relax the benchmark so that it ignores the best ε-fraction of arms, for some fixed ε>0. We are interested in regret relative to the best remaining arm, call it ε-regret for brevity. One can think of 1/ε as an effective number of arms. Kleinberg (2006) achieves ε-regret of the form (1/ε) · T^{2/3} · polylog(T). The algorithm is very simple, based on a version of the 'doubling trick' described above, although the analysis is somewhat subtle. This result allows the ε-fraction to be defined relative to an arbitrary 'base distribution' on arms, and extends to infinitely many arms.
