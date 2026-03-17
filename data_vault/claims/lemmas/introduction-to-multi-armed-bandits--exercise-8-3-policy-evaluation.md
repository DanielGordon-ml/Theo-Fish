---
slug: introduction-to-multi-armed-bandits--exercise-8-3-policy-evaluation
label: Exercise 8.3 (Policy evaluation)
claim_type: lemma
statement: 'Use Bernstein Inequality to prove Lemma 8.13. In fact, prove a stronger
  statement: for each policy \pi and each \delta>0, with probability at least 1-\delta
  we have: |\mathtt{IPS}(\pi)-\tilde{r}(\pi)|\leq O\left(\sqrt{V\;\log(\frac{1}{\delta})/N}\right),
  where V=\max_{t}\sum_{a\in\mathcal{A}}\frac{1}{p_{t}(a)}.'
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/realized-policy-value]]'
- '[[concepts/concentration-inequality]]'
- '[[concepts/sampling-distribution]]'
- '[[concepts/minimum-sampling-probability]]'
- '[[concepts/ips-estimator]]'
about_meta:
- target: '[[concepts/realized-policy-value]]'
  role: primary
  aspect: ''
- target: '[[concepts/concentration-inequality]]'
  role: primary
  aspect: ''
- target: '[[concepts/sampling-distribution]]'
  role: primary
  aspect: ''
- target: '[[concepts/minimum-sampling-probability]]'
  role: primary
  aspect: ''
- target: '[[concepts/ips-estimator]]'
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

# Exercise 8.3 (Policy evaluation)

Use Bernstein Inequality to prove Lemma 8.13. In fact, prove a stronger statement: for each policy \pi and each \delta>0, with probability at least 1-\delta we have: |\mathtt{IPS}(\pi)-\tilde{r}(\pi)|\leq O\left(\sqrt{V\;\log(\frac{1}{\delta})/N}\right), where V=\max_{t}\sum_{a\in\mathcal{A}}\frac{1}{p_{t}(a)}.
