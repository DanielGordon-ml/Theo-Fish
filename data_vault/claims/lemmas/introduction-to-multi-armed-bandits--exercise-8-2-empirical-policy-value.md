---
slug: introduction-to-multi-armed-bandits--exercise-8-2-empirical-policy-value
label: Exercise 8.2 (Empirical policy value)
claim_type: lemma
statement: Prove that realized policy value \tilde{r}(\pi), as defined in (109), is
  close to the policy value \mu(\pi). Specifically, observe that \operatorname{\mathbb{E}}[\tilde{r}(\pi)]=\mu(\pi).
  Next, fix \delta>0 and prove that |\mu(\pi)-\tilde{r}(\pi)|\leq\mathtt{conf}(N)
  with probability at least 1-\delta/|\Pi|, where the confidence term is \mathtt{conf}(N)=O\left(\sqrt{\frac{1}{N}\cdot\log(|\Pi|/\delta)}\right).
  Letting \pi_{0} be the policy with a largest realized policy value, it follows that
  \max_{\pi\in\Pi}\mu(\pi)-\mu(\pi_{0})\leq\mathtt{conf}(N) with probability at least
  1-\delta.
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/set-of-policies-pi]]'
- '[[concepts/realized-policy-value]]'
- '[[concepts/policy-value-mu-pi]]'
- '[[concepts/confidence-term-conf-n]]'
- '[[concepts/unbiasedness]]'
- '[[concepts/empirical-policy-value-r-pi]]'
about_meta:
- target: '[[concepts/set-of-policies-pi]]'
  role: primary
  aspect: ''
- target: '[[concepts/realized-policy-value]]'
  role: primary
  aspect: ''
- target: '[[concepts/policy-value-mu-pi]]'
  role: primary
  aspect: ''
- target: '[[concepts/confidence-term-conf-n]]'
  role: primary
  aspect: ''
- target: '[[concepts/unbiasedness]]'
  role: primary
  aspect: ''
- target: '[[concepts/empirical-policy-value-r-pi]]'
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

# Exercise 8.2 (Empirical policy value)

Prove that realized policy value \tilde{r}(\pi), as defined in (109), is close to the policy value \mu(\pi). Specifically, observe that \operatorname{\mathbb{E}}[\tilde{r}(\pi)]=\mu(\pi). Next, fix \delta>0 and prove that |\mu(\pi)-\tilde{r}(\pi)|\leq\mathtt{conf}(N) with probability at least 1-\delta/|\Pi|, where the confidence term is \mathtt{conf}(N)=O\left(\sqrt{\frac{1}{N}\cdot\log(|\Pi|/\delta)}\right). Letting \pi_{0} be the policy with a largest realized policy value, it follows that \max_{\pi\in\Pi}\mu(\pi)-\mu(\pi_{0})\leq\mathtt{conf}(N) with probability at least 1-\delta.
