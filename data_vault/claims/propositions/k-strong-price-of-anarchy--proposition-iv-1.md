---
slug: k-strong-price-of-anarchy--proposition-iv-1
label: Proposition IV.1
claim_type: proposition
statement: The k-Coalitional Round-Robin Dynamics converge in finite time and require
  $\mathcal{O}\left(m^n \left(\frac{1}{1-1/m}\right)^k\right)$ welfare evaluations.
proof: 'First, we verify that the output of Algorithm 1 is a $k$-strong Nash equilibrium,
  then we consider how long it takes Algorithm 1 to converge. Algorithm 1 terminates
  after a round in which no group $\Gamma \in \mathcal{C}_k$ can select a new action
  in which the welfare increases, i.e., $W(a) \geq W(a_\Gamma, a_{-\Gamma})$ for all
  $a_\Gamma \in \mathcal{A}_\Gamma$ and $\Gamma \in \mathcal{C}_k$ where $a$ is the
  output of Algorithm 1. A deviation for any subgroup $\Gamma'' \in \mathcal{C}_{[k]}$
  is subsumed by the joint action $(a_{\Gamma''}, a_{\Gamma \backslash \Gamma''})
  \in \mathcal{A}_\Gamma$. As such, a state $a$ terminates Algorithm 1 if and only
  if it satisfies (3) and is a $k$-strong Nash equilibrium.


  Without loss of generality, we assume each agent possesses $m$ actions; for each
  agent $i$ that has fewer actions, assign $m - |\mathcal{A}_i|$ dummy actions with
  minimum welfare. In one round of the $k$-Round-Robin dynamics, each group of agents
  is given the opportunity to deviate their action. First, we note that no group $\Gamma$
  will respond to the same complimentary group action $a_{-\Gamma}$ in two consecutive
  rounds unless $a$ is a $k$-strong Nash equilibrium. If the group $\Gamma$ rejects
  a group action $a_\Gamma$ in response to $a_{-\Gamma}$, the joint action $(a_\Gamma,
  a_{-\Gamma})$ is eliminated from consideration as an output of Algorithm 1. Accounting
  for overlaps between the groups, in any round that does not start in a $k$-strong
  Nash equilibrium, at least $y = \sum_{\zeta=1}^{k} \binom{n}{\zeta}(m-1)^\zeta$
  joint actions are eliminated. As there are $m^n$ joint actions in total, there can
  be at most $r \leq \lfloor \frac{m^n}{y} \rfloor + 1$ rounds that do not start in
  a $k$-strong Nash equilibrium; this proves the finite convergence time. In each
  round, there are exactly $\binom{n}{k} m^k$ welfare checks; thus, the total number
  of welfare checks is no more than $\left(\frac{m^n}{y} + 1\right) \binom{n}{k} m^k$.
  Removing lower order terms from $y$ gives the stated bound.'
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/running-time]]'
- '[[concepts/k-strong-nash-equilibrium]]'
- '[[concepts/joint-action-space]]'
- '[[concepts/k-coalitional-round-robin-dynamics]]'
- '[[concepts/number-of-welfare-evaluations-for-convergence]]'
about_meta:
- target: '[[concepts/running-time]]'
  role: primary
  aspect: ''
- target: '[[concepts/k-strong-nash-equilibrium]]'
  role: primary
  aspect: ''
- target: '[[concepts/joint-action-space]]'
  role: primary
  aspect: ''
- target: '[[concepts/k-coalitional-round-robin-dynamics]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-welfare-evaluations-for-convergence]]'
  role: primary
  aspect: ''
depends_on:
- '[[claims/k-strong-price-of-anarchy--proposition-ii-1]]'
- '[[claims/k-strong-price-of-anarchy--proposition-ii-1]]'
depends_on_meta:
- target: '[[claims/k-strong-price-of-anarchy--proposition-ii-1]]'
- target: '[[claims/k-strong-price-of-anarchy--proposition-ii-1]]'
sourced_from:
- '[[sources/k_strong_price_of_anarchy|k_strong_price_of_anarchy]]'
sourced_from_meta:
- target: '[[sources/k_strong_price_of_anarchy|k_strong_price_of_anarchy]]'
  section: ''
  page: ''
  confidence: 0.0
---

# Proposition IV.1

The k-Coalitional Round-Robin Dynamics converge in finite time and require $\mathcal{O}\left(m^n \left(\frac{1}{1-1/m}\right)^k\right)$ welfare evaluations.


## Proof

First, we verify that the output of Algorithm 1 is a $k$-strong Nash equilibrium, then we consider how long it takes Algorithm 1 to converge. Algorithm 1 terminates after a round in which no group $\Gamma \in \mathcal{C}_k$ can select a new action in which the welfare increases, i.e., $W(a) \geq W(a_\Gamma, a_{-\Gamma})$ for all $a_\Gamma \in \mathcal{A}_\Gamma$ and $\Gamma \in \mathcal{C}_k$ where $a$ is the output of Algorithm 1. A deviation for any subgroup $\Gamma' \in \mathcal{C}_{[k]}$ is subsumed by the joint action $(a_{\Gamma'}, a_{\Gamma \backslash \Gamma'}) \in \mathcal{A}_\Gamma$. As such, a state $a$ terminates Algorithm 1 if and only if it satisfies (3) and is a $k$-strong Nash equilibrium.

Without loss of generality, we assume each agent possesses $m$ actions; for each agent $i$ that has fewer actions, assign $m - |\mathcal{A}_i|$ dummy actions with minimum welfare. In one round of the $k$-Round-Robin dynamics, each group of agents is given the opportunity to deviate their action. First, we note that no group $\Gamma$ will respond to the same complimentary group action $a_{-\Gamma}$ in two consecutive rounds unless $a$ is a $k$-strong Nash equilibrium. If the group $\Gamma$ rejects a group action $a_\Gamma$ in response to $a_{-\Gamma}$, the joint action $(a_\Gamma, a_{-\Gamma})$ is eliminated from consideration as an output of Algorithm 1. Accounting for overlaps between the groups, in any round that does not start in a $k$-strong Nash equilibrium, at least $y = \sum_{\zeta=1}^{k} \binom{n}{\zeta}(m-1)^\zeta$ joint actions are eliminated. As there are $m^n$ joint actions in total, there can be at most $r \leq \lfloor \frac{m^n}{y} \rfloor + 1$ rounds that do not start in a $k$-strong Nash equilibrium; this proves the finite convergence time. In each round, there are exactly $\binom{n}{k} m^k$ welfare checks; thus, the total number of welfare checks is no more than $\left(\frac{m^n}{y} + 1\right) \binom{n}{k} m^k$. Removing lower order terms from $y$ gives the stated bound.
