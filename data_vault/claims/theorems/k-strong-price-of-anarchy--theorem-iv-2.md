---
slug: k-strong-price-of-anarchy--theorem-iv-2
label: Theorem IV.2
claim_type: theorem
statement: 'The Asynchronous $k$-Coalitional Best-Response Dynamics converge almost
  surely to the set of $k$-strong Nash equilibrium. Further, if $(G, W)$ is a $(\lambda,
  \mu)$-$k$-coalitionally smooth system, then after $T \geq 1$ update steps, the cumulative
  expected welfare satisfies

  $$\mathbb{E}\left[\frac{1}{T} \sum_{t=1}^{T} W(a^t)\right] \geq \frac{T-1}{2T} \frac{\sum_{\zeta=1}^{k}
  p_\zeta \lambda_\zeta}{1 + \sum_{\zeta=1}^{k} p_\zeta \mu_\zeta} W(a^{\mathrm{opt}}),$$

  where $p_\zeta$ is the probability a group of size $\zeta$ best responds.'
proof: 'First, we show that the Asynchronous $k$-Coalitional Best-Response Dynamics
  converges in general. A group $\Gamma$ revises their action only to one of strictly
  higher payoff if one exists. Consider the resulting Markov chain $\mathcal{M}$ with
  states $\mathcal{A}$. Any state $a \in A \backslash k\mathrm{SNE}$ has an outgoing
  edge with positive probability as there exists some group $\Gamma \in \mathcal{C}_{[k]}$
  that is selected with probability $p_{|\Gamma|}/|\mathcal{C}_{|\Gamma|}| > 0$ which
  would revise their action. Any state $a \in k\mathrm{SNE}$ has no outgoing edges
  with positive probability as no group $\Gamma \in \mathcal{C}_{[k]}$ can revise
  their action to strictly increase the welfare. Finally, there are no cycles (excluding
  self-loops) in $\mathcal{M}$, as every outgoing edge is directed from a joint action
  of lower welfare to one of strictly higher welfare. As such, the set $k\mathrm{SNE}$
  is absorbing and $\mathbb{P}[\lim_{t \to \infty} a^t \in k\mathrm{SNE}] = 1$.


  Now, consider that the system $(G, W)$ is $(\lambda, \mu)$-$k$-coalitionally smooth.
  As the selection of the updating group is random, the welfare at time $t+1$ is a
  random variable, even when conditioned on $a^t$; the expectation of the succeeding
  welfare can be written

  $$\mathbb{E}[W(a^{t+1}) | a^t = a] = \sum_{\zeta=1}^{k} p_\zeta \sum_{\Gamma \in
  \mathcal{C}_\zeta} \frac{1}{\binom{n}{\zeta}} W(a_\Gamma^+, a_{-\Gamma})$$

  $$\geq \sum_{\zeta=1}^{k} p_\zeta \sum_{\Gamma \in \mathcal{C}_\zeta} \frac{1}{\binom{n}{\zeta}}
  W(a_\Gamma^{\mathrm{opt}}, a_{-\Gamma})$$

  $$\geq \sum_{\zeta=1}^{k} p_\zeta (\lambda_\zeta W(a^{\mathrm{opt}}) - \mu_\zeta
  W(a))$$

  $$= (\sum_{\zeta=1}^{k} p_\zeta \lambda_\zeta) W(a^{\mathrm{opt}}) - (\sum_{\zeta=1}^{k}
  p_\zeta \mu_\zeta) W(a),$$

  where $a_\Gamma^+ \in \arg\max_{a_\Gamma \in A_\Gamma} W(a_\Gamma, a_{-\Gamma})$
  is the update state for the group $\Gamma$ following the dynamics. As $a_\Gamma^+$
  is a best response, the welfare is no better for selecting a different action, namely
  $a_\Gamma^{\mathrm{opt}}$. The final inequality holds from (5). Taking the expectation
  of $\mathbb{E}[W(a^{t+1}) | a^t = a]$ over $a^t$ gives

  $$\mathbb{E}[W(a^{t+1})] \geq (\sum_{\zeta=1}^{k} p_\zeta \lambda_\zeta) W(a^{\mathrm{opt}})
  - (\sum_{\zeta=1}^{k} p_\zeta \mu_\zeta) \mathbb{E}[W(a^t)].$$

  Rearranging terms shows

  $$\mathbb{E}[W(a^{t+1})] - \frac{\sum_{\zeta=1}^{k} p_\zeta \lambda_\zeta}{1 + \sum_{\zeta=1}^{k}
  p_\zeta \mu_\zeta} W(a^{\mathrm{opt}}) \geq (\sum_{\zeta=1}^{k} p_\zeta \mu_\zeta)\left(\frac{\sum_{\zeta=1}^{k}
  p_\zeta \lambda_\zeta}{1 + \sum_{\zeta=1}^{k} p_\zeta \mu_\zeta} W(a^{\mathrm{opt}})
  - \mathbb{E}[W(a^t)]\right).$$

  Observe that either $\mathbb{E}[W(a^t)] \geq \frac{\sum_{\zeta=1}^{k} p_\zeta \lambda_\zeta}{1
  + \sum_{\zeta=1}^{k} p_\zeta \mu_\zeta} W(a^{\mathrm{opt}})$ or $\mathbb{E}[W(a^{t+1})]
  - \frac{\sum_{\zeta=1}^{k} p_\zeta \lambda_\zeta}{1 + \sum_{\zeta=1}^{k} p_\zeta
  \mu_\zeta} W(a^{\mathrm{opt}}) \geq 0$. Accordingly, in expectation, every other
  update must satisfy the bound, giving the average cumulative welfare bound in (12).'
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/transient-performance]]'
- '[[concepts/k-strong-nash-equilibrium]]'
- '[[concepts/optimal-welfare]]'
- '[[concepts/asynchronous-k-coalitional-best-response-dynamics]]'
- '[[concepts/markov-chain-m]]'
- '[[concepts/lambda-mu-k-coalitionally-smooth-system]]'
- '[[concepts/probability-distribution-p-over-group-sizes]]'
- '[[concepts/expected-cumulative-welfare-bound]]'
about_meta:
- target: '[[concepts/transient-performance]]'
  role: primary
  aspect: ''
- target: '[[concepts/k-strong-nash-equilibrium]]'
  role: primary
  aspect: ''
- target: '[[concepts/optimal-welfare]]'
  role: primary
  aspect: ''
- target: '[[concepts/asynchronous-k-coalitional-best-response-dynamics]]'
  role: primary
  aspect: ''
- target: '[[concepts/markov-chain-m]]'
  role: primary
  aspect: ''
- target: '[[concepts/lambda-mu-k-coalitionally-smooth-system]]'
  role: primary
  aspect: ''
- target: '[[concepts/probability-distribution-p-over-group-sizes]]'
  role: primary
  aspect: ''
- target: '[[concepts/expected-cumulative-welfare-bound]]'
  role: primary
  aspect: ''
depends_on:
- '[[claims/k-strong-price-of-anarchy--proposition-iii-2]]'
- '[[claims/k-strong-price-of-anarchy--proposition-iii-2]]'
- '[[claims/k-strong-price-of-anarchy--proposition-iii-2]]'
depends_on_meta:
- target: '[[claims/k-strong-price-of-anarchy--proposition-iii-2]]'
- target: '[[claims/k-strong-price-of-anarchy--proposition-iii-2]]'
- target: '[[claims/k-strong-price-of-anarchy--proposition-iii-2]]'
sourced_from:
- '[[sources/k_strong_price_of_anarchy|k_strong_price_of_anarchy]]'
sourced_from_meta:
- target: '[[sources/k_strong_price_of_anarchy|k_strong_price_of_anarchy]]'
  section: ''
  page: ''
  confidence: 0.0
---

# Theorem IV.2

The Asynchronous $k$-Coalitional Best-Response Dynamics converge almost surely to the set of $k$-strong Nash equilibrium. Further, if $(G, W)$ is a $(\lambda, \mu)$-$k$-coalitionally smooth system, then after $T \geq 1$ update steps, the cumulative expected welfare satisfies
$$\mathbb{E}\left[\frac{1}{T} \sum_{t=1}^{T} W(a^t)\right] \geq \frac{T-1}{2T} \frac{\sum_{\zeta=1}^{k} p_\zeta \lambda_\zeta}{1 + \sum_{\zeta=1}^{k} p_\zeta \mu_\zeta} W(a^{\mathrm{opt}}),$$
where $p_\zeta$ is the probability a group of size $\zeta$ best responds.


## Proof

First, we show that the Asynchronous $k$-Coalitional Best-Response Dynamics converges in general. A group $\Gamma$ revises their action only to one of strictly higher payoff if one exists. Consider the resulting Markov chain $\mathcal{M}$ with states $\mathcal{A}$. Any state $a \in A \backslash k\mathrm{SNE}$ has an outgoing edge with positive probability as there exists some group $\Gamma \in \mathcal{C}_{[k]}$ that is selected with probability $p_{|\Gamma|}/|\mathcal{C}_{|\Gamma|}| > 0$ which would revise their action. Any state $a \in k\mathrm{SNE}$ has no outgoing edges with positive probability as no group $\Gamma \in \mathcal{C}_{[k]}$ can revise their action to strictly increase the welfare. Finally, there are no cycles (excluding self-loops) in $\mathcal{M}$, as every outgoing edge is directed from a joint action of lower welfare to one of strictly higher welfare. As such, the set $k\mathrm{SNE}$ is absorbing and $\mathbb{P}[\lim_{t \to \infty} a^t \in k\mathrm{SNE}] = 1$.

Now, consider that the system $(G, W)$ is $(\lambda, \mu)$-$k$-coalitionally smooth. As the selection of the updating group is random, the welfare at time $t+1$ is a random variable, even when conditioned on $a^t$; the expectation of the succeeding welfare can be written
$$\mathbb{E}[W(a^{t+1}) | a^t = a] = \sum_{\zeta=1}^{k} p_\zeta \sum_{\Gamma \in \mathcal{C}_\zeta} \frac{1}{\binom{n}{\zeta}} W(a_\Gamma^+, a_{-\Gamma})$$
$$\geq \sum_{\zeta=1}^{k} p_\zeta \sum_{\Gamma \in \mathcal{C}_\zeta} \frac{1}{\binom{n}{\zeta}} W(a_\Gamma^{\mathrm{opt}}, a_{-\Gamma})$$
$$\geq \sum_{\zeta=1}^{k} p_\zeta (\lambda_\zeta W(a^{\mathrm{opt}}) - \mu_\zeta W(a))$$
$$= (\sum_{\zeta=1}^{k} p_\zeta \lambda_\zeta) W(a^{\mathrm{opt}}) - (\sum_{\zeta=1}^{k} p_\zeta \mu_\zeta) W(a),$$
where $a_\Gamma^+ \in \arg\max_{a_\Gamma \in A_\Gamma} W(a_\Gamma, a_{-\Gamma})$ is the update state for the group $\Gamma$ following the dynamics. As $a_\Gamma^+$ is a best response, the welfare is no better for selecting a different action, namely $a_\Gamma^{\mathrm{opt}}$. The final inequality holds from (5). Taking the expectation of $\mathbb{E}[W(a^{t+1}) | a^t = a]$ over $a^t$ gives
$$\mathbb{E}[W(a^{t+1})] \geq (\sum_{\zeta=1}^{k} p_\zeta \lambda_\zeta) W(a^{\mathrm{opt}}) - (\sum_{\zeta=1}^{k} p_\zeta \mu_\zeta) \mathbb{E}[W(a^t)].$$
Rearranging terms shows
$$\mathbb{E}[W(a^{t+1})] - \frac{\sum_{\zeta=1}^{k} p_\zeta \lambda_\zeta}{1 + \sum_{\zeta=1}^{k} p_\zeta \mu_\zeta} W(a^{\mathrm{opt}}) \geq (\sum_{\zeta=1}^{k} p_\zeta \mu_\zeta)\left(\frac{\sum_{\zeta=1}^{k} p_\zeta \lambda_\zeta}{1 + \sum_{\zeta=1}^{k} p_\zeta \mu_\zeta} W(a^{\mathrm{opt}}) - \mathbb{E}[W(a^t)]\right).$$
Observe that either $\mathbb{E}[W(a^t)] \geq \frac{\sum_{\zeta=1}^{k} p_\zeta \lambda_\zeta}{1 + \sum_{\zeta=1}^{k} p_\zeta \mu_\zeta} W(a^{\mathrm{opt}})$ or $\mathbb{E}[W(a^{t+1})] - \frac{\sum_{\zeta=1}^{k} p_\zeta \lambda_\zeta}{1 + \sum_{\zeta=1}^{k} p_\zeta \mu_\zeta} W(a^{\mathrm{opt}}) \geq 0$. Accordingly, in expectation, every other update must satisfy the bound, giving the average cumulative welfare bound in (12).
