---
slug: introduction-to-multi-armed-bandits--corollary-9-4
label: Corollary 9.4
claim_type: corollary
statement: '$M(p^{*},q^{*})=v^{*}$, and the pair $(p^{*},q^{*})$ forms a *Nash equilibrium*,
  in the sense that

  $$p^{*}\in\operatornamewithlimits{argmin}_{p\in\Delta_{\mathtt{rows}}}M(p,q^{*})
  \quad\text{and}\quad q^{*}\in\operatornamewithlimits{argmax}_{q\in\Delta_{\mathtt{cols}}}M(p^{*},q).$$'
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/minimax-strategy]]'
- '[[concepts/minimax-value]]'
- '[[concepts/zero-sum-game]]'
- '[[concepts/maximin-strategy]]'
- '[[concepts/d-cols]]'
- '[[concepts/nash-equilibrium]]'
- '[[concepts/m-p-q]]'
- '[[concepts/d-rows]]'
about_meta:
- target: '[[concepts/minimax-strategy]]'
  role: primary
  aspect: ''
- target: '[[concepts/minimax-value]]'
  role: primary
  aspect: ''
- target: '[[concepts/zero-sum-game]]'
  role: primary
  aspect: ''
- target: '[[concepts/maximin-strategy]]'
  role: primary
  aspect: ''
- target: '[[concepts/d-cols]]'
  role: primary
  aspect: ''
- target: '[[concepts/nash-equilibrium]]'
  role: primary
  aspect: ''
- target: '[[concepts/m-p-q]]'
  role: primary
  aspect: ''
- target: '[[concepts/d-rows]]'
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

# Corollary 9.4

$M(p^{*},q^{*})=v^{*}$, and the pair $(p^{*},q^{*})$ forms a *Nash equilibrium*, in the sense that
$$p^{*}\in\operatornamewithlimits{argmin}_{p\in\Delta_{\mathtt{rows}}}M(p,q^{*}) \quad\text{and}\quad q^{*}\in\operatornamewithlimits{argmax}_{q\in\Delta_{\mathtt{cols}}}M(p^{*},q).$$
