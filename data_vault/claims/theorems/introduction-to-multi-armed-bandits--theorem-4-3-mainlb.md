---
slug: introduction-to-multi-armed-bandits--theorem-4-3-mainlb
label: Theorem 4.3 (MainLB)
claim_type: theorem
statement: 'Consider stochastic bandits, with $K$ arms and time horizon $T$ (for any
  $K,T$). Let $\mathtt{ALG}$ be any algorithm for this problem. Pick any positive
  $\epsilon\leq\sqrt{cK/T}$, where $c$ is an absolute constant from Lemma 2.8. Then
  there exists a problem instance $\mathcal{J}=\mathcal{J}(a^{*},\epsilon)$, $a^{*}\in[K]$,
  such that

  $$\operatornamewithlimits{\mathbb{E}}\left[R(T)\mid\mathcal{J}\right]\geq\Omega(\epsilon
  T).$$'
proof: ''
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/0-1-rewards]]'
- '[[concepts/parameter-epsilon]]'
- '[[concepts/time-horizon-t]]'
- '[[concepts/lower-bound-on-regret]]'
- '[[concepts/stochastic-bandits-problem]]'
- '[[concepts/number-of-arms-k]]'
about_meta:
- target: '[[concepts/0-1-rewards]]'
  role: primary
  aspect: ''
- target: '[[concepts/parameter-epsilon]]'
  role: primary
  aspect: ''
- target: '[[concepts/time-horizon-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/lower-bound-on-regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/stochastic-bandits-problem]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-arms-k]]'
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

# Theorem 4.3 (MainLB)

Consider stochastic bandits, with $K$ arms and time horizon $T$ (for any $K,T$). Let $\mathtt{ALG}$ be any algorithm for this problem. Pick any positive $\epsilon\leq\sqrt{cK/T}$, where $c$ is an absolute constant from Lemma 2.8. Then there exists a problem instance $\mathcal{J}=\mathcal{J}(a^{*},\epsilon)$, $a^{*}\in[K]$, such that
$$\operatornamewithlimits{\mathbb{E}}\left[R(T)\mid\mathcal{J}\right]\geq\Omega(\epsilon T).$$
