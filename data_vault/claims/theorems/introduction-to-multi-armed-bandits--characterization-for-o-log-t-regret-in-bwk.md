---
slug: introduction-to-multi-armed-bandits--characterization-for-o-log-t-regret-in-bwk
label: Characterization for O(log T) regret in BwK
claim_type: theorem
statement: 'O(log T) regret rates are possible for BwK if and only if two conditions
  hold: there is only one resource other than time (i.e., d=2), and the best distribution
  over arms reduces to the best fixed arm (best-arm-optimality). If either condition
  fails, any algorithm is doomed to Ω(√T) regret in a wide range of problem instances.
  The precise formulation of this lower bound starts with any problem instance I_0
  with three arms, under mild assumptions, such that either d>2 or best-arm optimality
  fails with some margin. Then it constructs two problem instances I, I'' which are
  ε-perturbations of I_0, ε=O(1/√T), in the sense that expected rewards and resource
  consumptions of each arm differ by at most ε. The guarantee is that any algorithm
  suffers regret Ω(√T) on either I or I''. Here both upper and lower bounds are against
  the fixed-distribution benchmark (OPT_FD).'
proof: ''
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/ucbbwk-algorithm]]'
- '[[concepts/best-arm-optimality]]'
- '[[concepts/regret-r-t]]'
- '[[concepts/dimension-d]]'
- '[[concepts/bandits-with-knapsacks]]'
- '[[concepts/opt-fd]]'
about_meta:
- target: '[[concepts/ucbbwk-algorithm]]'
  role: primary
  aspect: ''
- target: '[[concepts/best-arm-optimality]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret-r-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/dimension-d]]'
  role: primary
  aspect: ''
- target: '[[concepts/bandits-with-knapsacks]]'
  role: primary
  aspect: ''
- target: '[[concepts/opt-fd]]'
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

# Characterization for O(log T) regret in BwK

O(log T) regret rates are possible for BwK if and only if two conditions hold: there is only one resource other than time (i.e., d=2), and the best distribution over arms reduces to the best fixed arm (best-arm-optimality). If either condition fails, any algorithm is doomed to Ω(√T) regret in a wide range of problem instances. The precise formulation of this lower bound starts with any problem instance I_0 with three arms, under mild assumptions, such that either d>2 or best-arm optimality fails with some margin. Then it constructs two problem instances I, I' which are ε-perturbations of I_0, ε=O(1/√T), in the sense that expected rewards and resource consumptions of each arm differ by at most ε. The guarantee is that any algorithm suffers regret Ω(√T) on either I or I'. Here both upper and lower bounds are against the fixed-distribution benchmark (OPT_FD).
