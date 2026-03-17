---
slug: introduction-to-multi-armed-bandits--lemma-6-10
label: Lemma 6.10
claim_type: lemma
statement: Fix parameter $\gamma\in[0,\tfrac{1}{2})$ and round $t$. Then $\operatornamewithlimits{\mathbb{E}}[\widehat{G}_{t}]\leq\tfrac{K}{1-\gamma}$.
proof: 'For each arm $a$, let $\mathcal{E}_{a}=\{e\in\mathcal{E}:a_{t,e}=a\}$ be the
  set of all experts that recommended this arm. Let p_t(a) := ∑_e ∈E_a p_t(e) be the
  probability that the expert chosen by Hedge recommends arm $a$. Then $q_{t}(a)=p_{t}(a)(1-\gamma)+\frac{\gamma}{K}\geq(1-\gamma)\;p_{t}(a)$.
  For each expert $e$, letting $a=a_{t,e}$ be the recommended arm, we have: $\widehat{c}_{t}(e)=\widehat{c}_{t}(a)\leq\frac{c_{t}(a)}{q_{t}(a)}\leq\frac{1}{q_{t}(a)}\leq\frac{1}{(1-\gamma)\;p_{t}(a)}$.
  Each realization of $\widehat{G}_{t}$ satisfies: $\widehat{G}_{t}:=\sum_{e\in\mathcal{E}}p_{t}(e)\;\widehat{c}_{t}^{2}(e)=\sum_{a}\sum_{e\in\mathcal{E}_{a}}p_{t}(e)\cdot\widehat{c}_{t}(e)\cdot\widehat{c}_{t}(e)\leq\sum_{a}\sum_{e\in\mathcal{E}_{a}}\frac{p_{t}(e)}{(1-\gamma)\;p_{t}(a)}\;\widehat{c}_{t}(a)=\frac{1}{1-\gamma}\;\sum_{a}\frac{\widehat{c}_{t}(a)}{p_{t}(a)}\sum_{e\in\mathcal{E}_{a}}p_{t}(e)=\frac{1}{1-\gamma}\;\sum_{a}\widehat{c}_{t}(a)$.
  To complete the proof, take expectations over both sides and recall that $\operatornamewithlimits{\mathbb{E}}[\widehat{c}_{t}(a)]=c_{t}(a)\leq
  1$.'
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/exploration-parameter]]'
- '[[concepts/estimated-cumulative-squared-cost-g-hat-t]]'
- '[[concepts/fake-cost-function-on-arm]]'
- '[[concepts/fake-cost-function-on-expert]]'
- '[[concepts/number-of-arms-k]]'
- '[[concepts/exp4]]'
about_meta:
- target: '[[concepts/exploration-parameter]]'
  role: primary
  aspect: ''
- target: '[[concepts/estimated-cumulative-squared-cost-g-hat-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/fake-cost-function-on-arm]]'
  role: primary
  aspect: ''
- target: '[[concepts/fake-cost-function-on-expert]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-arms-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/exp4]]'
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

# Lemma 6.10

Fix parameter $\gamma\in[0,\tfrac{1}{2})$ and round $t$. Then $\operatornamewithlimits{\mathbb{E}}[\widehat{G}_{t}]\leq\tfrac{K}{1-\gamma}$.


## Proof

For each arm $a$, let $\mathcal{E}_{a}=\{e\in\mathcal{E}:a_{t,e}=a\}$ be the set of all experts that recommended this arm. Let p_t(a) := ∑_e ∈E_a p_t(e) be the probability that the expert chosen by Hedge recommends arm $a$. Then $q_{t}(a)=p_{t}(a)(1-\gamma)+\frac{\gamma}{K}\geq(1-\gamma)\;p_{t}(a)$. For each expert $e$, letting $a=a_{t,e}$ be the recommended arm, we have: $\widehat{c}_{t}(e)=\widehat{c}_{t}(a)\leq\frac{c_{t}(a)}{q_{t}(a)}\leq\frac{1}{q_{t}(a)}\leq\frac{1}{(1-\gamma)\;p_{t}(a)}$. Each realization of $\widehat{G}_{t}$ satisfies: $\widehat{G}_{t}:=\sum_{e\in\mathcal{E}}p_{t}(e)\;\widehat{c}_{t}^{2}(e)=\sum_{a}\sum_{e\in\mathcal{E}_{a}}p_{t}(e)\cdot\widehat{c}_{t}(e)\cdot\widehat{c}_{t}(e)\leq\sum_{a}\sum_{e\in\mathcal{E}_{a}}\frac{p_{t}(e)}{(1-\gamma)\;p_{t}(a)}\;\widehat{c}_{t}(a)=\frac{1}{1-\gamma}\;\sum_{a}\frac{\widehat{c}_{t}(a)}{p_{t}(a)}\sum_{e\in\mathcal{E}_{a}}p_{t}(e)=\frac{1}{1-\gamma}\;\sum_{a}\widehat{c}_{t}(a)$. To complete the proof, take expectations over both sides and recall that $\operatornamewithlimits{\mathbb{E}}[\widehat{c}_{t}(a)]=c_{t}(a)\leq 1$.
