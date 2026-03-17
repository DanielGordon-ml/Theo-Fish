---
slug: introduction-to-multi-armed-bandits--theorem-3-15
label: Theorem 3.15
claim_type: theorem
statement: 'For each problem instance, Thompson Sampling with approach (i) achieves,
  for all $\epsilon>0$,

  $$\operatorname{\mathbb{E}}[R(T)]\leq(1+\epsilon)\,C\,\log(T)+\frac{f(\mu)}{\epsilon^{2}},\quad\text{where}\quad
  C=\sum_{\text{arms $a$}:\,\Delta(a)<0}\;\frac{\mu(a^{*})-\mu(a)}{\mathtt{KL}(\mu(a),\mu^{*})}.$$

  Here $f(\mu)$ depends on the mean reward vector $\mu$, but not on $\epsilon$ or
  $T$.'
proof: ''
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/kl-divergence]]'
- '[[concepts/suboptimality-gap]]'
- '[[concepts/optimal-constant-c]]'
- '[[concepts/thompson-sampling]]'
- '[[concepts/independent-priors]]'
- '[[concepts/problem-dependent-function-f]]'
- '[[concepts/mean-reward-vector]]'
- '[[concepts/expected-regret-e-r-t]]'
about_meta:
- target: '[[concepts/kl-divergence]]'
  role: primary
  aspect: ''
- target: '[[concepts/suboptimality-gap]]'
  role: primary
  aspect: ''
- target: '[[concepts/optimal-constant-c]]'
  role: primary
  aspect: ''
- target: '[[concepts/thompson-sampling]]'
  role: primary
  aspect: ''
- target: '[[concepts/independent-priors]]'
  role: primary
  aspect: ''
- target: '[[concepts/problem-dependent-function-f]]'
  role: primary
  aspect: ''
- target: '[[concepts/mean-reward-vector]]'
  role: primary
  aspect: ''
- target: '[[concepts/expected-regret-e-r-t]]'
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

# Theorem 3.15

For each problem instance, Thompson Sampling with approach (i) achieves, for all $\epsilon>0$,
$$\operatorname{\mathbb{E}}[R(T)]\leq(1+\epsilon)\,C\,\log(T)+\frac{f(\mu)}{\epsilon^{2}},\quad\text{where}\quad C=\sum_{\text{arms $a$}:\,\Delta(a)<0}\;\frac{\mu(a^{*})-\mu(a)}{\mathtt{KL}(\mu(a),\mu^{*})}.$$
Here $f(\mu)$ depends on the mean reward vector $\mu$, but not on $\epsilon$ or $T$.
