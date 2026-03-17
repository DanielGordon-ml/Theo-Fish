---
slug: introduction-to-multi-armed-bandits--lemma-3-5
label: Lemma 3.5
claim_type: lemma
statement: Assume the prior $\mathbb{P}$ is independent. Fix a subset $\mathcal{M}_{a}\subset[0,1]$
  for each arm $a\in\mathcal{A}$. Then $\mathbb{P}_{H}(\cap_{a\in\mathcal{A}}\,\mathcal{M}_{a})
  = \prod_{a\in\mathcal{A}}\,\mathbb{P}^{a}_{H}(\mathcal{M}_{a}).$
proof: 'The only subtlety is that we focus the $H$-induced bandit algorithm. Then
  the pairs $(\mu(a),\mathtt{proj}(H_{t};a))$, $a\in\mathcal{A}$ are mutually independent
  random variables. We are interested in these two events, for each arm $a$:


  $\mathcal{E}_{a} = \{\mu(a)\in\mathcal{M}_{a}\}$, $\mathcal{E}_{a}^{H} = \{\mathtt{proj}(H_{t};a)=\mathtt{proj}(H;a)\}.$


  Letting $\mathcal{M}=\cap_{a\in\mathcal{A}}\mathcal{M}_{a}$, we have:


  $\Pr[H_{t}=H\text{ and }\mu\in\mathcal{M}] = \Pr\left[\bigcap_{a\in\mathcal{A}}(\mathcal{E}_{a}\cap\mathcal{E}_{a}^{H})\right]=\prod_{a\in\mathcal{A}}\Pr\left[\mathcal{E}_{a}\cap\mathcal{E}_{a}^{H}\right].$


  Likewise, $\Pr[H_{t}=H]=\prod_{a\in\mathcal{A}}\Pr[\mathcal{E}_{a}^{H}]$. Putting
  this together,


  $\mathbb{P}_{H}(\mathcal{M}) = \frac{\Pr[H_{t}=H\text{ and }\mu\in\mathcal{M}]}{\Pr[H_{t}=H]}=\prod_{a\in\mathcal{A}}\frac{\Pr[\mathcal{E}_{a}\cap\mathcal{E}_{a}^{H}]}{\Pr[\mathcal{E}_{a}^{H}]}
  = \prod_{a\in\mathcal{A}}\Pr[\mu\in\mathcal{M}\mid\mathcal{E}_{a}^{H}]=\prod_{a\in\mathcal{A}}\mathbb{P}_{H}^{a}(\mathcal{M}_{a}).$'
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/bayesian-update]]'
- '[[concepts/independent-prior]]'
- '[[concepts/projected-history-for-arm-a]]'
- '[[concepts/bayesian-posterior-distribution]]'
- '[[concepts/independent-priors]]'
- '[[concepts/posterior-distribution-for-arm-a]]'
about_meta:
- target: '[[concepts/bayesian-update]]'
  role: primary
  aspect: ''
- target: '[[concepts/independent-prior]]'
  role: primary
  aspect: ''
- target: '[[concepts/projected-history-for-arm-a]]'
  role: primary
  aspect: ''
- target: '[[concepts/bayesian-posterior-distribution]]'
  role: primary
  aspect: ''
- target: '[[concepts/independent-priors]]'
  role: primary
  aspect: ''
- target: '[[concepts/posterior-distribution-for-arm-a]]'
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

# Lemma 3.5

Assume the prior $\mathbb{P}$ is independent. Fix a subset $\mathcal{M}_{a}\subset[0,1]$ for each arm $a\in\mathcal{A}$. Then $\mathbb{P}_{H}(\cap_{a\in\mathcal{A}}\,\mathcal{M}_{a}) = \prod_{a\in\mathcal{A}}\,\mathbb{P}^{a}_{H}(\mathcal{M}_{a}).$


## Proof

The only subtlety is that we focus the $H$-induced bandit algorithm. Then the pairs $(\mu(a),\mathtt{proj}(H_{t};a))$, $a\in\mathcal{A}$ are mutually independent random variables. We are interested in these two events, for each arm $a$:

$\mathcal{E}_{a} = \{\mu(a)\in\mathcal{M}_{a}\}$, $\mathcal{E}_{a}^{H} = \{\mathtt{proj}(H_{t};a)=\mathtt{proj}(H;a)\}.$

Letting $\mathcal{M}=\cap_{a\in\mathcal{A}}\mathcal{M}_{a}$, we have:

$\Pr[H_{t}=H\text{ and }\mu\in\mathcal{M}] = \Pr\left[\bigcap_{a\in\mathcal{A}}(\mathcal{E}_{a}\cap\mathcal{E}_{a}^{H})\right]=\prod_{a\in\mathcal{A}}\Pr\left[\mathcal{E}_{a}\cap\mathcal{E}_{a}^{H}\right].$

Likewise, $\Pr[H_{t}=H]=\prod_{a\in\mathcal{A}}\Pr[\mathcal{E}_{a}^{H}]$. Putting this together,

$\mathbb{P}_{H}(\mathcal{M}) = \frac{\Pr[H_{t}=H\text{ and }\mu\in\mathcal{M}]}{\Pr[H_{t}=H]}=\prod_{a\in\mathcal{A}}\frac{\Pr[\mathcal{E}_{a}\cap\mathcal{E}_{a}^{H}]}{\Pr[\mathcal{E}_{a}^{H}]} = \prod_{a\in\mathcal{A}}\Pr[\mu\in\mathcal{M}\mid\mathcal{E}_{a}^{H}]=\prod_{a\in\mathcal{A}}\mathbb{P}_{H}^{a}(\mathcal{M}_{a}).$
