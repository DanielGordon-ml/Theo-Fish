---
slug: introduction-to-multi-armed-bandits--theorem-3-9
label: Theorem 3.9
claim_type: theorem
statement: Bayesian Regret of Thompson Sampling is $\mathtt{BR}(T)=O(\sqrt{KT\log(T)})$.
proof: 'Let us use the confidence bounds and the confidence radius from (46). Note
  that they satisfy properties (47) and (48) with $\gamma=2$. By Lemma 3.10,


  $\mathtt{BR}(T)\leq O\left(\,\sqrt{\log T}\,\right)\sum_{t=1}^{T}\operatornamewithlimits{\mathbb{E}}\left[\;\frac{1}{\sqrt{n_{t}(a_{t})}}\;\right].$


  Moreover,


  $\sum_{t=1}^{T}\sqrt{\frac{1}{n_{t}(a_{t})}}=\sum_{\text{arms $a$}}\quad\sum_{\text{rounds
  $t$:\; $a_{t}=a$}}\;\;\frac{1}{\sqrt{n_{t}(a)}}=\sum_{\text{arms $a$}}\;\;\sum_{j=1}^{n_{T+1}(a)}\frac{1}{\sqrt{j}}=\underset{\text{arms
  $a$}}{\sum}O(\sqrt{n(a)}).$


  It follows that


  $\mathtt{BR}(T)\leq O\left(\,\sqrt{\log T}\,\right)\underset{\text{arms $a$}}{\sum}\sqrt{n(a)}\leq
  O\left(\,\sqrt{\log T}\,\right)\sqrt{K\underset{\text{arms $a$}}{\sum}n(a)}=O\left(\,\sqrt{KT\log
  T}\,\right),$


  where the intermediate step is by the arithmetic vs. quadratic mean inequality.'
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/thompson-sampling]]'
- '[[concepts/number-of-arms-k]]'
- '[[concepts/lower-confidence-bound]]'
- '[[concepts/bayesian-regret]]'
- '[[concepts/upper-confidence-bound]]'
- '[[concepts/time-horizon-t]]'
about_meta:
- target: '[[concepts/thompson-sampling]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-arms-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/lower-confidence-bound]]'
  role: primary
  aspect: ''
- target: '[[concepts/bayesian-regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/upper-confidence-bound]]'
  role: primary
  aspect: ''
- target: '[[concepts/time-horizon-t]]'
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

# Theorem 3.9

Bayesian Regret of Thompson Sampling is $\mathtt{BR}(T)=O(\sqrt{KT\log(T)})$.


## Proof

Let us use the confidence bounds and the confidence radius from (46). Note that they satisfy properties (47) and (48) with $\gamma=2$. By Lemma 3.10,

$\mathtt{BR}(T)\leq O\left(\,\sqrt{\log T}\,\right)\sum_{t=1}^{T}\operatornamewithlimits{\mathbb{E}}\left[\;\frac{1}{\sqrt{n_{t}(a_{t})}}\;\right].$

Moreover,

$\sum_{t=1}^{T}\sqrt{\frac{1}{n_{t}(a_{t})}}=\sum_{\text{arms $a$}}\quad\sum_{\text{rounds $t$:\; $a_{t}=a$}}\;\;\frac{1}{\sqrt{n_{t}(a)}}=\sum_{\text{arms $a$}}\;\;\sum_{j=1}^{n_{T+1}(a)}\frac{1}{\sqrt{j}}=\underset{\text{arms $a$}}{\sum}O(\sqrt{n(a)}).$

It follows that

$\mathtt{BR}(T)\leq O\left(\,\sqrt{\log T}\,\right)\underset{\text{arms $a$}}{\sum}\sqrt{n(a)}\leq O\left(\,\sqrt{\log T}\,\right)\sqrt{K\underset{\text{arms $a$}}{\sum}n(a)}=O\left(\,\sqrt{KT\log T}\,\right),$

where the intermediate step is by the arithmetic vs. quadratic mean inequality.
