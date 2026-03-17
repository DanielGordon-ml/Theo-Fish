---
slug: introduction-to-multi-armed-bandits--theorem-9-8
label: Theorem 9.8
claim_type: theorem
statement: Distribution $\bar{\sigma}$ defined in (135) forms an $\epsilon_{T}$-approximate
  CCE, where $\epsilon_{T}=\tfrac{\operatornamewithlimits{\mathbb{E}}[R(T)]}{T}$.
proof: 'We compute: $U_{\bar{\sigma}} := \operatornamewithlimits{\mathbb{E}}_{(i,j)\sim\bar{\sigma}}\left[\,M(i,j)\,\right]
  = \tfrac{1}{T}\,\sum_{t=1}^{T}\operatornamewithlimits{\mathbb{E}}_{(i,j)\sim\sigma_{t}}\left[\,M(i,j)\,\right]
  = \tfrac{1}{T}\,\operatornamewithlimits{\mathbb{E}}[\mathtt{cost}(\mathtt{ALG})]$
  and $U_{\bar{\sigma}}(i_{0}) := \operatornamewithlimits{\mathbb{E}}_{(i,j)\sim\bar{\sigma}}\left[\,M(i_{0},j)\,\right]
  = \tfrac{1}{T}\,\sum_{t=1}^{T}\operatornamewithlimits{\mathbb{E}}_{j\sim q_{t}}\left[\,M(i_{0},j)\,\right]
  = \tfrac{1}{T}\,\operatornamewithlimits{\mathbb{E}}[\mathtt{cost}(i_{0})]$. Hence,
  $\bar{\sigma}$ satisfies $U_{\bar{\sigma}} \geq U_{\bar{\sigma}}(i_0) - \epsilon$
  with $\epsilon=\tfrac{\operatornamewithlimits{\mathbb{E}}[R(T)]}{T}$ by definition
  of regret. A similar argument holds for ADV.'
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/r-t]]'
- '[[concepts/epsilon-t]]'
- '[[concepts/d-pairs]]'
- '[[concepts/sigma-t]]'
- '[[concepts/epsilon-approximate-coarse-correlated-equilibrium]]'
- '[[concepts/coarse-correlated-equilibrium]]'
- '[[concepts/sigma-bar]]'
- '[[concepts/expected-regret]]'
- '[[concepts/regret-minimization]]'
- '[[concepts/game-matrix]]'
about_meta:
- target: '[[concepts/r-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/epsilon-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/d-pairs]]'
  role: primary
  aspect: ''
- target: '[[concepts/sigma-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/epsilon-approximate-coarse-correlated-equilibrium]]'
  role: primary
  aspect: ''
- target: '[[concepts/coarse-correlated-equilibrium]]'
  role: primary
  aspect: ''
- target: '[[concepts/sigma-bar]]'
  role: primary
  aspect: ''
- target: '[[concepts/expected-regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret-minimization]]'
  role: primary
  aspect: ''
- target: '[[concepts/game-matrix]]'
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

# Theorem 9.8

Distribution $\bar{\sigma}$ defined in (135) forms an $\epsilon_{T}$-approximate CCE, where $\epsilon_{T}=\tfrac{\operatornamewithlimits{\mathbb{E}}[R(T)]}{T}$.


## Proof

We compute: $U_{\bar{\sigma}} := \operatornamewithlimits{\mathbb{E}}_{(i,j)\sim\bar{\sigma}}\left[\,M(i,j)\,\right] = \tfrac{1}{T}\,\sum_{t=1}^{T}\operatornamewithlimits{\mathbb{E}}_{(i,j)\sim\sigma_{t}}\left[\,M(i,j)\,\right] = \tfrac{1}{T}\,\operatornamewithlimits{\mathbb{E}}[\mathtt{cost}(\mathtt{ALG})]$ and $U_{\bar{\sigma}}(i_{0}) := \operatornamewithlimits{\mathbb{E}}_{(i,j)\sim\bar{\sigma}}\left[\,M(i_{0},j)\,\right] = \tfrac{1}{T}\,\sum_{t=1}^{T}\operatornamewithlimits{\mathbb{E}}_{j\sim q_{t}}\left[\,M(i_{0},j)\,\right] = \tfrac{1}{T}\,\operatornamewithlimits{\mathbb{E}}[\mathtt{cost}(i_{0})]$. Hence, $\bar{\sigma}$ satisfies $U_{\bar{\sigma}} \geq U_{\bar{\sigma}}(i_0) - \epsilon$ with $\epsilon=\tfrac{\operatornamewithlimits{\mathbb{E}}[R(T)]}{T}$ by definition of regret. A similar argument holds for ADV.
