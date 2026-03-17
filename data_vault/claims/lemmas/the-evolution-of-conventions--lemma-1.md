---
slug: the-evolution-of-conventions--lemma-1
label: Lemma 1
claim_type: lemma
statement: Let $P^\varepsilon$ be a regular perturbation of $P^0$ and let $\mu^\varepsilon$
  be its stationary distribution. Then $\lim_{\varepsilon \to 0} \mu^\varepsilon =
  \mu^0$ exists and $\mu^0$ is a stationary distribution of $P^0$. Moreover, $\mu_x^0
  > 0$ if and only if $\gamma(x) \leq \gamma(y)$ for all $y$ in $X$.
proof: Let $P'$ be the transition function of any aperiodic, irreducible, stationary
  Markov process defined on the finite space $X$. For each $z \in X$, define the number
  $p_z' = \sum_{T \in \mathcal{T}_z} \prod_{(x,y) \in T} P_{xy}'$, where $p_z'$ is
  positive because $P'$ is irreducible. Let $\mu_z' = p_z' / (\sum_{x \in X} p_x')
  > 0$. It may then be verified that $\mu' P' = \mu'$, from which it follows that
  $\mu'$ is the unique stationary distribution of $P'$ (See Freidlin and Wentzell
  (1984, Chapter 6, Lemma 3.1).) Now let us apply this result to the process $P^\varepsilon$
  hypothesized in Lemma 1. Let $p_z^\varepsilon = \sum_{T \in \mathcal{T}_z} \prod_{(x,y)
  \in T} P_{xy}^\varepsilon$. By the above result, the stationary distribution of
  $P^\varepsilon$ is given by the formula $\mu_z^\varepsilon = p_z^\varepsilon / \sum_{x
  \in X} p_x^\varepsilon$. Define $\gamma(z)$ as in (9) and let $\gamma^* = \min_z
  \gamma(z)$. We are going to show that $\mu_z^\varepsilon > 0$ if and only if $\gamma(z)
  = \gamma^*$. Choose a $z$-tree $T$ with resistance $\gamma(z)$ and consider the
  identity $\varepsilon^{-\gamma^*} \prod_{(x,y) \in T} P_{xy}^\varepsilon = \varepsilon^{r(T)
  - \gamma^*} \prod_{(x,y) \in T} \varepsilon^{-r(x,y)} P_{xy}^\varepsilon$. By (8),
  $\lim_{\varepsilon \to 0} \varepsilon^{-r(x,y)} P_{xy}^\varepsilon > 0$ for every
  $(x,y) \in T$. If $r(T) = \gamma(z) > \gamma^*$, it follows from (12) and (13) that
  $\lim_{\varepsilon \to 0} \varepsilon^{-\gamma^*} \prod_{(x,y) \in T} P_{xy}^\varepsilon
  = 0$, so $\lim_{\varepsilon \to 0} \varepsilon^{-\gamma^*} p_z^\varepsilon = 0$.
  Similarly, if $r(T) = \gamma(z) = \gamma^*$ we obtain $\lim_{\varepsilon \to 0}
  \varepsilon^{-\gamma^*} p_z^\varepsilon > 0$. From (13), (14), and the identity
  $\mu_z^\varepsilon = \varepsilon^{-\gamma^*} p_z^\varepsilon / \sum_{x \in X} \varepsilon^{-\gamma^*}
  p_x^\varepsilon$, it follows that $\lim_{\varepsilon \to 0} \mu_z^\varepsilon =
  0$ if $\gamma(z) > \gamma^*$ and $\lim_{\varepsilon \to 0} \mu_z^\varepsilon > 0$
  if $\gamma(z) = \gamma^*$. Thus we have shown that $\lim_{\varepsilon \to 0} \mu^\varepsilon$
  exists, and its support is the set of states $z$ that minimize $\gamma(z)$. Since
  $\mu^\varepsilon$ satisfies the equation $\mu^\varepsilon P^\varepsilon = \mu^\varepsilon$
  for every $\varepsilon > 0$, it follows from assumption (7) that $\mu^0 P^0 = \mu^0$.
  Hence $\mu^0$ is a stationary distribution of $P^0$. This completes the proof of
  Lemma 1.
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/shortest-arborescence]]'
- '[[concepts/perturbed-markov-process]]'
- '[[concepts/least-resistance-between-classes-r-ij]]'
- '[[concepts/resistance-r-x-y]]'
- '[[concepts/stationary-distribution-mu-epsilon]]'
- '[[concepts/j-tree]]'
- '[[concepts/resistance-graph]]'
- '[[concepts/stochastic-potential]]'
- '[[concepts/regular-perturbation]]'
- '[[concepts/z-tree]]'
- '[[concepts/stochastically-stable-states]]'
- '[[concepts/stationary-distribution-mu-epsilon]]'
- '[[concepts/least-resistance-between-classes-r-ij]]'
- '[[concepts/perturbed-markov-process]]'
- '[[concepts/stochastically-stable-states]]'
- '[[concepts/z-tree]]'
- '[[concepts/regular-perturbation]]'
- '[[concepts/stochastic-potential]]'
- '[[concepts/j-tree]]'
- '[[concepts/resistance-r-x-y]]'
- '[[concepts/shortest-arborescence]]'
- '[[concepts/resistance-graph]]'
about_meta:
- target: '[[concepts/shortest-arborescence]]'
  role: primary
  aspect: ''
- target: '[[concepts/perturbed-markov-process]]'
  role: primary
  aspect: ''
- target: '[[concepts/least-resistance-between-classes-r-ij]]'
  role: primary
  aspect: ''
- target: '[[concepts/resistance-r-x-y]]'
  role: primary
  aspect: ''
- target: '[[concepts/stationary-distribution-mu-epsilon]]'
  role: primary
  aspect: ''
- target: '[[concepts/j-tree]]'
  role: primary
  aspect: ''
- target: '[[concepts/resistance-graph]]'
  role: primary
  aspect: ''
- target: '[[concepts/stochastic-potential]]'
  role: primary
  aspect: ''
- target: '[[concepts/regular-perturbation]]'
  role: primary
  aspect: ''
- target: '[[concepts/z-tree]]'
  role: primary
  aspect: ''
- target: '[[concepts/stochastically-stable-states]]'
  role: primary
  aspect: ''
- target: '[[concepts/stationary-distribution-mu-epsilon]]'
  role: primary
  aspect: ''
- target: '[[concepts/least-resistance-between-classes-r-ij]]'
  role: primary
  aspect: ''
- target: '[[concepts/perturbed-markov-process]]'
  role: primary
  aspect: ''
- target: '[[concepts/stochastically-stable-states]]'
  role: primary
  aspect: ''
- target: '[[concepts/z-tree]]'
  role: primary
  aspect: ''
- target: '[[concepts/regular-perturbation]]'
  role: primary
  aspect: ''
- target: '[[concepts/stochastic-potential]]'
  role: primary
  aspect: ''
- target: '[[concepts/j-tree]]'
  role: primary
  aspect: ''
- target: '[[concepts/resistance-r-x-y]]'
  role: primary
  aspect: ''
- target: '[[concepts/shortest-arborescence]]'
  role: primary
  aspect: ''
- target: '[[concepts/resistance-graph]]'
  role: primary
  aspect: ''
depends_on: []
depends_on_meta: []
sourced_from:
- '[[sources/the_evolution_of_conventions|the_evolution_of_conventions]]'
sourced_from_meta:
- target: '[[sources/the_evolution_of_conventions|the_evolution_of_conventions]]'
  section: ''
  page: ''
  confidence: 0.0
---

# Lemma 1

Let $P^\varepsilon$ be a regular perturbation of $P^0$ and let $\mu^\varepsilon$ be its stationary distribution. Then $\lim_{\varepsilon \to 0} \mu^\varepsilon = \mu^0$ exists and $\mu^0$ is a stationary distribution of $P^0$. Moreover, $\mu_x^0 > 0$ if and only if $\gamma(x) \leq \gamma(y)$ for all $y$ in $X$.


## Proof

Let $P'$ be the transition function of any aperiodic, irreducible, stationary Markov process defined on the finite space $X$. For each $z \in X$, define the number $p_z' = \sum_{T \in \mathcal{T}_z} \prod_{(x,y) \in T} P_{xy}'$, where $p_z'$ is positive because $P'$ is irreducible. Let $\mu_z' = p_z' / (\sum_{x \in X} p_x') > 0$. It may then be verified that $\mu' P' = \mu'$, from which it follows that $\mu'$ is the unique stationary distribution of $P'$ (See Freidlin and Wentzell (1984, Chapter 6, Lemma 3.1).) Now let us apply this result to the process $P^\varepsilon$ hypothesized in Lemma 1. Let $p_z^\varepsilon = \sum_{T \in \mathcal{T}_z} \prod_{(x,y) \in T} P_{xy}^\varepsilon$. By the above result, the stationary distribution of $P^\varepsilon$ is given by the formula $\mu_z^\varepsilon = p_z^\varepsilon / \sum_{x \in X} p_x^\varepsilon$. Define $\gamma(z)$ as in (9) and let $\gamma^* = \min_z \gamma(z)$. We are going to show that $\mu_z^\varepsilon > 0$ if and only if $\gamma(z) = \gamma^*$. Choose a $z$-tree $T$ with resistance $\gamma(z)$ and consider the identity $\varepsilon^{-\gamma^*} \prod_{(x,y) \in T} P_{xy}^\varepsilon = \varepsilon^{r(T) - \gamma^*} \prod_{(x,y) \in T} \varepsilon^{-r(x,y)} P_{xy}^\varepsilon$. By (8), $\lim_{\varepsilon \to 0} \varepsilon^{-r(x,y)} P_{xy}^\varepsilon > 0$ for every $(x,y) \in T$. If $r(T) = \gamma(z) > \gamma^*$, it follows from (12) and (13) that $\lim_{\varepsilon \to 0} \varepsilon^{-\gamma^*} \prod_{(x,y) \in T} P_{xy}^\varepsilon = 0$, so $\lim_{\varepsilon \to 0} \varepsilon^{-\gamma^*} p_z^\varepsilon = 0$. Similarly, if $r(T) = \gamma(z) = \gamma^*$ we obtain $\lim_{\varepsilon \to 0} \varepsilon^{-\gamma^*} p_z^\varepsilon > 0$. From (13), (14), and the identity $\mu_z^\varepsilon = \varepsilon^{-\gamma^*} p_z^\varepsilon / \sum_{x \in X} \varepsilon^{-\gamma^*} p_x^\varepsilon$, it follows that $\lim_{\varepsilon \to 0} \mu_z^\varepsilon = 0$ if $\gamma(z) > \gamma^*$ and $\lim_{\varepsilon \to 0} \mu_z^\varepsilon > 0$ if $\gamma(z) = \gamma^*$. Thus we have shown that $\lim_{\varepsilon \to 0} \mu^\varepsilon$ exists, and its support is the set of states $z$ that minimize $\gamma(z)$. Since $\mu^\varepsilon$ satisfies the equation $\mu^\varepsilon P^\varepsilon = \mu^\varepsilon$ for every $\varepsilon > 0$, it follows from assumption (7) that $\mu^0 P^0 = \mu^0$. Hence $\mu^0$ is a stationary distribution of $P^0$. This completes the proof of Lemma 1.
