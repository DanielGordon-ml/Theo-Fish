---
slug: introduction-to-multi-armed-bandits--exercise-4-3
label: Exercise 4.3
claim_type: proposition
statement: The optimal uniform discretization from Eq. (58) is optimal up to $O(\log
  T)$ factors. Specifically, using the notation $f(S)=c_{\mathtt{ALG}}\cdot\sqrt{|S|\,T\log
  T}+T\cdot\epsilon(S)$, for any metric space $(X,\mathcal{D})$, any algorithm and
  any time horizon $T$ there is a problem instance on $(X,\mathcal{D})$ such that
  $\operatornamewithlimits{\mathbb{E}}[R(T)]\geq\widetilde{\Omega}(\inf_{S\subset
  X}f(S))$.
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/uniform-discretization-for-bandits]]'
- '[[concepts/lipschitz-bandits-problem]]'
- '[[concepts/expected-regret]]'
- '[[concepts/f-s]]'
- '[[concepts/regret-bound]]'
about_meta:
- target: '[[concepts/uniform-discretization-for-bandits]]'
  role: primary
  aspect: ''
- target: '[[concepts/lipschitz-bandits-problem]]'
  role: primary
  aspect: ''
- target: '[[concepts/expected-regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/f-s]]'
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

# Exercise 4.3

The optimal uniform discretization from Eq. (58) is optimal up to $O(\log T)$ factors. Specifically, using the notation $f(S)=c_{\mathtt{ALG}}\cdot\sqrt{|S|\,T\log T}+T\cdot\epsilon(S)$, for any metric space $(X,\mathcal{D})$, any algorithm and any time horizon $T$ there is a problem instance on $(X,\mathcal{D})$ such that $\operatornamewithlimits{\mathbb{E}}[R(T)]\geq\widetilde{\Omega}(\inf_{S\subset X}f(S))$.
