---
slug: introduction-to-multi-armed-bandits--theorem-6-7
label: Theorem 6.7
claim_type: theorem
statement: 'Consider adversarial bandits with expert advice, with a deterministic-oblivious
  adversary. Algorithm $\mathtt{Exp4}$ with parameters $\gamma=T^{-1/4}\;K^{1/2}\;(\log
  N)^{1/4}$ and $\epsilon=\epsilon_{u}$, $u=K/\gamma$, achieves regret

  $$\operatorname{\mathbb{E}}[R(T)]=O\left(T^{3/4}\;K^{1/2}\;(\log N)^{1/4}\right).$$'
proof: 'Note that $q_{t}(a)\geq\gamma/K>0$ for each arm $a$. According to Claim 6.5
  and Claim 6.2, the expected true regret of $\mathtt{Hedge}$ is upper-bounded by
  its expected fake regret: $\operatorname{\mathbb{E}}[R_{\mathtt{Hedge}}(T)]\leq\operatorname{\mathbb{E}}[\widehat{R}_{\mathtt{Hedge}}(T)]$.
  In each round $t$, our algorithm accumulates cost at most $1$ from the low-probability
  exploration, and cost $c_{t}(e_{t})$ from the chosen expert $e_{t}$. So the expected
  cost in this round is $\operatorname{\mathbb{E}}[c_{t}(a_{t})]\leq\gamma+\operatorname{\mathbb{E}}[c_{t}(e_{t})]$.
  Summing over all rounds, we obtain: $\operatorname{\mathbb{E}}[\mathtt{cost}(\mathtt{Exp4})]\leq\operatorname{\mathbb{E}}[\mathtt{cost}(\mathtt{Hedge})]+\gamma
  T$ and $\operatorname{\mathbb{E}}[R_{\mathtt{Exp4}}(T)]\leq\operatorname{\mathbb{E}}[R_{\mathtt{Hedge}}(T)]+\gamma
  T\leq\operatorname{\mathbb{E}}[\widehat{R}_{\mathtt{Hedge}}(T)]+\gamma T$. We can
  immediately derive a crude regret bound via Theorem 6.1. Observing $\widehat{c}_{t}(a)\leq
  1/q_{t}(a)\leq K/\gamma$, we can take $u=(K/\gamma)^{2}$ in the theorem, and conclude
  that $\operatorname{\mathbb{E}}[R_{\mathtt{Exp4}}(T)]\leq O\left(\frac{K}{\gamma}\cdot
  K^{1/2}\;(\log N)^{1/4}+\gamma T\right)$. To (approximately) minimize expected regret,
  choose $\gamma$ so as to equalize the two summands, giving $\gamma=T^{-1/4}\;K^{1/2}\;(\log
  N)^{1/4}$, which yields $\operatorname{\mathbb{E}}[R(T)]=O\left(T^{3/4}\;K^{1/2}\;(\log
  N)^{1/4}\right)$.'
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/time-horizon-t]]'
- '[[concepts/regret]]'
- '[[concepts/exp4]]'
- '[[concepts/fake-cost-function-on-arm]]'
- '[[concepts/exploration-parameter]]'
- '[[concepts/deterministic-oblivious-adversary]]'
- '[[concepts/number-of-arms-k]]'
- '[[concepts/adversarial-bandits-with-expert-advice]]'
- '[[concepts/hedge]]'
- '[[concepts/number-of-experts]]'
about_meta:
- target: '[[concepts/time-horizon-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/exp4]]'
  role: primary
  aspect: ''
- target: '[[concepts/fake-cost-function-on-arm]]'
  role: primary
  aspect: ''
- target: '[[concepts/exploration-parameter]]'
  role: primary
  aspect: ''
- target: '[[concepts/deterministic-oblivious-adversary]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-arms-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/adversarial-bandits-with-expert-advice]]'
  role: primary
  aspect: ''
- target: '[[concepts/hedge]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-experts]]'
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

# Theorem 6.7

Consider adversarial bandits with expert advice, with a deterministic-oblivious adversary. Algorithm $\mathtt{Exp4}$ with parameters $\gamma=T^{-1/4}\;K^{1/2}\;(\log N)^{1/4}$ and $\epsilon=\epsilon_{u}$, $u=K/\gamma$, achieves regret
$$\operatorname{\mathbb{E}}[R(T)]=O\left(T^{3/4}\;K^{1/2}\;(\log N)^{1/4}\right).$$


## Proof

Note that $q_{t}(a)\geq\gamma/K>0$ for each arm $a$. According to Claim 6.5 and Claim 6.2, the expected true regret of $\mathtt{Hedge}$ is upper-bounded by its expected fake regret: $\operatorname{\mathbb{E}}[R_{\mathtt{Hedge}}(T)]\leq\operatorname{\mathbb{E}}[\widehat{R}_{\mathtt{Hedge}}(T)]$. In each round $t$, our algorithm accumulates cost at most $1$ from the low-probability exploration, and cost $c_{t}(e_{t})$ from the chosen expert $e_{t}$. So the expected cost in this round is $\operatorname{\mathbb{E}}[c_{t}(a_{t})]\leq\gamma+\operatorname{\mathbb{E}}[c_{t}(e_{t})]$. Summing over all rounds, we obtain: $\operatorname{\mathbb{E}}[\mathtt{cost}(\mathtt{Exp4})]\leq\operatorname{\mathbb{E}}[\mathtt{cost}(\mathtt{Hedge})]+\gamma T$ and $\operatorname{\mathbb{E}}[R_{\mathtt{Exp4}}(T)]\leq\operatorname{\mathbb{E}}[R_{\mathtt{Hedge}}(T)]+\gamma T\leq\operatorname{\mathbb{E}}[\widehat{R}_{\mathtt{Hedge}}(T)]+\gamma T$. We can immediately derive a crude regret bound via Theorem 6.1. Observing $\widehat{c}_{t}(a)\leq 1/q_{t}(a)\leq K/\gamma$, we can take $u=(K/\gamma)^{2}$ in the theorem, and conclude that $\operatorname{\mathbb{E}}[R_{\mathtt{Exp4}}(T)]\leq O\left(\frac{K}{\gamma}\cdot K^{1/2}\;(\log N)^{1/4}+\gamma T\right)$. To (approximately) minimize expected regret, choose $\gamma$ so as to equalize the two summands, giving $\gamma=T^{-1/4}\;K^{1/2}\;(\log N)^{1/4}$, which yields $\operatorname{\mathbb{E}}[R(T)]=O\left(T^{3/4}\;K^{1/2}\;(\log N)^{1/4}\right)$.
