---
slug: introduction-to-multi-armed-bandits--claim-6-2
label: Claim 6.2
claim_type: lemma
statement: Assuming Eq. (88), i.e., $\operatorname{\mathbb{E}}[\,\widehat{c}_{t}(e)\mid\vec{p}_{t}\,]
  = c_{t}(e)$ for all experts $e$, it holds that $\operatorname{\mathbb{E}}[R_{\mathtt{Hedge}}(T)]\leq\operatorname{\mathbb{E}}[\widehat{R}_{\mathtt{Hedge}}(T)]$.
proof: 'First, we connect true costs of Hedge with the corresponding fake costs.


  $\operatorname{\mathbb{E}}\left[\,\widehat{c}_{t}(e_{t})\mid\vec{p}_{t}\,\right]
  = \sum_{e\in\mathcal{E}}\Pr\left[\,e_{t}=e\mid\vec{p}_{t}\,\right]\;\operatorname{\mathbb{E}}\left[\,\widehat{c}_{t}(e)\mid\vec{p}_{t}\,\right]
  = \sum_{e\in\mathcal{E}}p_{t}(e)\;c_{t}(e)$ (use definition of $p_{t}(e)$ and Eq.
  (88)) $= \operatorname{\mathbb{E}}\left[\,c_{t}(e_{t})\mid\vec{p}_{t}\,\right].$


  Taking expectation of both sides, $\operatorname{\mathbb{E}}[\widehat{c}_{t}(e_{t})]=\operatorname{\mathbb{E}}[c_{t}(e_{t})]$.
  Summing over all rounds, it follows that


  $\operatorname{\mathbb{E}}\left[\,\widehat{\mathtt{cost}}(\mathtt{Hedge})\,\right]=\operatorname{\mathbb{E}}\left[\,\mathtt{cost}(\mathtt{Hedge})\,\right].$


  To complete the proof, we deal with the benchmark:


  $\operatorname{\mathbb{E}}\left[\,\min_{e\in\mathcal{E}}\widehat{\mathtt{cost}}(e)\,\right]\leq\min_{e\in\mathcal{E}}\operatorname{\mathbb{E}}\left[\,\widehat{\mathtt{cost}}(e)\,\right]=\min_{e\in\mathcal{E}}\operatorname{\mathbb{E}}\left[\,\mathtt{cost}(e)\,\right]=\min_{e\in\mathcal{E}}\mathtt{cost}(e).$


  The first equality holds by (88), and the second equality holds because true costs
  $c_{t}(e)$ are deterministic.'
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/hedge]]'
- '[[concepts/fake-regret]]'
- '[[concepts/fake-cost-function-on-expert]]'
- '[[concepts/regret-for-hedge]]'
- '[[concepts/unbiasedness]]'
about_meta:
- target: '[[concepts/hedge]]'
  role: primary
  aspect: ''
- target: '[[concepts/fake-regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/fake-cost-function-on-expert]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret-for-hedge]]'
  role: primary
  aspect: ''
- target: '[[concepts/unbiasedness]]'
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

# Claim 6.2

Assuming Eq. (88), i.e., $\operatorname{\mathbb{E}}[\,\widehat{c}_{t}(e)\mid\vec{p}_{t}\,] = c_{t}(e)$ for all experts $e$, it holds that $\operatorname{\mathbb{E}}[R_{\mathtt{Hedge}}(T)]\leq\operatorname{\mathbb{E}}[\widehat{R}_{\mathtt{Hedge}}(T)]$.


## Proof

First, we connect true costs of Hedge with the corresponding fake costs.

$\operatorname{\mathbb{E}}\left[\,\widehat{c}_{t}(e_{t})\mid\vec{p}_{t}\,\right] = \sum_{e\in\mathcal{E}}\Pr\left[\,e_{t}=e\mid\vec{p}_{t}\,\right]\;\operatorname{\mathbb{E}}\left[\,\widehat{c}_{t}(e)\mid\vec{p}_{t}\,\right] = \sum_{e\in\mathcal{E}}p_{t}(e)\;c_{t}(e)$ (use definition of $p_{t}(e)$ and Eq. (88)) $= \operatorname{\mathbb{E}}\left[\,c_{t}(e_{t})\mid\vec{p}_{t}\,\right].$

Taking expectation of both sides, $\operatorname{\mathbb{E}}[\widehat{c}_{t}(e_{t})]=\operatorname{\mathbb{E}}[c_{t}(e_{t})]$. Summing over all rounds, it follows that

$\operatorname{\mathbb{E}}\left[\,\widehat{\mathtt{cost}}(\mathtt{Hedge})\,\right]=\operatorname{\mathbb{E}}\left[\,\mathtt{cost}(\mathtt{Hedge})\,\right].$

To complete the proof, we deal with the benchmark:

$\operatorname{\mathbb{E}}\left[\,\min_{e\in\mathcal{E}}\widehat{\mathtt{cost}}(e)\,\right]\leq\min_{e\in\mathcal{E}}\operatorname{\mathbb{E}}\left[\,\widehat{\mathtt{cost}}(e)\,\right]=\min_{e\in\mathcal{E}}\operatorname{\mathbb{E}}\left[\,\mathtt{cost}(e)\,\right]=\min_{e\in\mathcal{E}}\mathtt{cost}(e).$

The first equality holds by (88), and the second equality holds because true costs $c_{t}(e)$ are deterministic.
