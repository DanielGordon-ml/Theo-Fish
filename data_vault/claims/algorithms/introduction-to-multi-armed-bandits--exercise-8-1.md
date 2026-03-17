---
slug: introduction-to-multi-armed-bandits--exercise-8-1
label: Exercise 8.1
claim_type: algorithm
statement: Consider the Lipschitz condition in (103). Design an algorithm with regret
  bound \tilde{O}(T^{(d+1)/(d+2)}), where d is the covering dimension of \mathcal{X}\times\mathcal{A}.
  Fix an \epsilon-mesh S_{\mathcal{X}} for (\mathcal{X},\mathcal{D}_{\mathcal{X}})
  and an \epsilon-mesh S_{\mathcal{A}} for (\mathcal{A},\mathcal{D}_{\mathcal{A}}),
  for some \epsilon>0 to be chosen in the analysis. Fix an optimal bandit algorithm
  \mathtt{ALG} such as \mathtt{UCB1}, with S_{\mathcal{A}} as a set of arms. Run a
  separate copy \mathtt{ALG}_{x} of this algorithm for each context x\in S_{\mathcal{X}}.
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/regret-bound]]'
- '[[concepts/covering-dimension]]'
- '[[concepts/mesh]]'
- '[[concepts/ucb1-algorithm]]'
- '[[concepts/lipschitz-contextual-bandits]]'
about_meta:
- target: '[[concepts/regret-bound]]'
  role: primary
  aspect: ''
- target: '[[concepts/covering-dimension]]'
  role: primary
  aspect: ''
- target: '[[concepts/mesh]]'
  role: primary
  aspect: ''
- target: '[[concepts/ucb1-algorithm]]'
  role: primary
  aspect: ''
- target: '[[concepts/lipschitz-contextual-bandits]]'
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

# Exercise 8.1

Consider the Lipschitz condition in (103). Design an algorithm with regret bound \tilde{O}(T^{(d+1)/(d+2)}), where d is the covering dimension of \mathcal{X}\times\mathcal{A}. Fix an \epsilon-mesh S_{\mathcal{X}} for (\mathcal{X},\mathcal{D}_{\mathcal{X}}) and an \epsilon-mesh S_{\mathcal{A}} for (\mathcal{A},\mathcal{D}_{\mathcal{A}}), for some \epsilon>0 to be chosen in the analysis. Fix an optimal bandit algorithm \mathtt{ALG} such as \mathtt{UCB1}, with S_{\mathcal{A}} as a set of arms. Run a separate copy \mathtt{ALG}_{x} of this algorithm for each context x\in S_{\mathcal{X}}.
