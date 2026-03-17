---
slug: introduction-to-multi-armed-bandits--sharp-k-dependence-dichotomy-for-sample-complexity
label: Sharp K-dependence dichotomy for sample complexity
claim_type: theorem
statement: 'The dependence on $K$ admits a very sharp separation: essentially, it
  is either linear or at least exponential, depending on the collection $\mathcal{C}$
  of feasible per-arm priors. In particular, if $\mathcal{C}$ is finite then one compares
  $\mathtt{minsupp}(\mathcal{C}):=\min_{\mathcal{P}\in\mathcal{C}}\sup(\text{support}(\mathcal{P}))$
  and $\Phi_{\mathcal{C}}:=\max_{\mathcal{P}\in\mathcal{C}}\operatornamewithlimits{\mathbb{E}}[\mathcal{P}]$.
  The $\mathcal{C}$-optimal sample complexity is $O_{\mathcal{C}}(K)$ if $\mathtt{minsupp}(\mathcal{C})>\Phi_{\mathcal{C}}$,
  and $\exp\left(\,\Omega_{\mathcal{C}}(K)\,\right)$ if $\mathtt{minsupp}(\mathcal{C})<\Phi_{\mathcal{C}}$.'
proof: ''
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/incentivized-exploration]]'
- '[[concepts/sample-complexity]]'
- '[[concepts/number-of-arms-k]]'
- '[[concepts/minimum-support-supremum-minsupp-c]]'
- '[[concepts/maximum-expected-value-phi-c]]'
about_meta:
- target: '[[concepts/incentivized-exploration]]'
  role: primary
  aspect: ''
- target: '[[concepts/sample-complexity]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-arms-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/minimum-support-supremum-minsupp-c]]'
  role: primary
  aspect: ''
- target: '[[concepts/maximum-expected-value-phi-c]]'
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

# Sharp K-dependence dichotomy for sample complexity

The dependence on $K$ admits a very sharp separation: essentially, it is either linear or at least exponential, depending on the collection $\mathcal{C}$ of feasible per-arm priors. In particular, if $\mathcal{C}$ is finite then one compares $\mathtt{minsupp}(\mathcal{C}):=\min_{\mathcal{P}\in\mathcal{C}}\sup(\text{support}(\mathcal{P}))$ and $\Phi_{\mathcal{C}}:=\max_{\mathcal{P}\in\mathcal{C}}\operatornamewithlimits{\mathbb{E}}[\mathcal{P}]$. The $\mathcal{C}$-optimal sample complexity is $O_{\mathcal{C}}(K)$ if $\mathtt{minsupp}(\mathcal{C})>\Phi_{\mathcal{C}}$, and $\exp\left(\,\Omega_{\mathcal{C}}(K)\,\right)$ if $\mathtt{minsupp}(\mathcal{C})<\Phi_{\mathcal{C}}$.
