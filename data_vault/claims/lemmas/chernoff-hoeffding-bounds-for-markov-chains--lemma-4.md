---
slug: chernoff-hoeffding-bounds-for-markov-chains--lemma-4
label: Lemma 4
claim_type: lemma
statement: Let $0 < \varepsilon \le 1/2$ be a parameter. Let $M$ be an ergodic reversible
  Markov chain with $\varepsilon$-mixing time $T(\varepsilon)$ and spectral expansion
  $\lambda(M)$. It holds that $\lambda(M) \leq (2\varepsilon)^{1/T(\varepsilon)}$.
proof: Recall that for an ergodic reversible Markov chain $M$, it holds that $\lambda(M^t)
  = \lambda^t(M)$ for every $t \in \mathbb{N}$. Hence, it suffices to show that $\lambda(M^{T(\epsilon)})
  \le 2\epsilon$. Also, recall that $\lambda(M^{T(\epsilon)})$ is simply the second
  largest eigenvalue (in absolute value) of $M^{T(\epsilon)}$. Let $\boldsymbol{v}$
  be the corresponding eigenvector, i.e. $v$ satisfies $vM^{T(\epsilon)} = \lambda(M^{T(\epsilon)})v$.
  Since $M$ is reversible, the entries of $v$ are real-valued. Also, notice that $v$
  is a left eigenvector of $M$ while $(1,1,...,1)^T$ is a right eigenvector of $M$
  (using the fact that each row of $M$ sums to one). Furthermore, $v$ and $(1,...,1)^T$
  do not share the same eigenvalue. So we have $\langle v, (1,...,1)^T \rangle = 0$,
  i.e. $\sum_i v_i = 0$. Therefore, by scaling $v$, we can assume w.l.o.g. that $x
  \triangleq v + \pi$ is a distribution. By Claim 3.3, $\|xM^{T(\varepsilon)} - \pi\|_{TV}
  \leq 2\varepsilon \|x - \pi\|_{TV}$, i.e. $\|xM^{T(\varepsilon)} - \pi\|_1 \leq
  2\varepsilon \|x - \pi\|_1$. Observing that $(xM^{T(\varepsilon)} - \pi)$ and $(x
  - \pi)$ are simply $\lambda(M^{T(\varepsilon)})v$ and $v$, the above inequality
  means $\lambda(M^{T(\varepsilon)})\|v\|_1 \leq 2\varepsilon \|v\|_1$, which implies
  $\lambda(M^{T(\varepsilon)}) \le 2\varepsilon$, as desired.
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/epsilon-mixing-time-t-epsilon]]'
- '[[concepts/reversible-markov-chain]]'
- '[[concepts/spectral-expansion-lambda-m]]'
- '[[concepts/ergodic]]'
about_meta:
- target: '[[concepts/epsilon-mixing-time-t-epsilon]]'
  role: primary
  aspect: ''
- target: '[[concepts/reversible-markov-chain]]'
  role: primary
  aspect: ''
- target: '[[concepts/spectral-expansion-lambda-m]]'
  role: primary
  aspect: ''
- target: '[[concepts/ergodic]]'
  role: primary
  aspect: ''
depends_on: []
depends_on_meta: []
sourced_from:
- '[[sources/chernoff_hoeffding_bounds_for_markov_chains|chernoff_hoeffding_bounds_for_markov_chains]]'
sourced_from_meta:
- target: '[[sources/chernoff_hoeffding_bounds_for_markov_chains|chernoff_hoeffding_bounds_for_markov_chains]]'
  section: ''
  page: ''
  confidence: 0.0
---

# Lemma 4

Let $0 < \varepsilon \le 1/2$ be a parameter. Let $M$ be an ergodic reversible Markov chain with $\varepsilon$-mixing time $T(\varepsilon)$ and spectral expansion $\lambda(M)$. It holds that $\lambda(M) \leq (2\varepsilon)^{1/T(\varepsilon)}$.


## Proof

Recall that for an ergodic reversible Markov chain $M$, it holds that $\lambda(M^t) = \lambda^t(M)$ for every $t \in \mathbb{N}$. Hence, it suffices to show that $\lambda(M^{T(\epsilon)}) \le 2\epsilon$. Also, recall that $\lambda(M^{T(\epsilon)})$ is simply the second largest eigenvalue (in absolute value) of $M^{T(\epsilon)}$. Let $\boldsymbol{v}$ be the corresponding eigenvector, i.e. $v$ satisfies $vM^{T(\epsilon)} = \lambda(M^{T(\epsilon)})v$. Since $M$ is reversible, the entries of $v$ are real-valued. Also, notice that $v$ is a left eigenvector of $M$ while $(1,1,...,1)^T$ is a right eigenvector of $M$ (using the fact that each row of $M$ sums to one). Furthermore, $v$ and $(1,...,1)^T$ do not share the same eigenvalue. So we have $\langle v, (1,...,1)^T \rangle = 0$, i.e. $\sum_i v_i = 0$. Therefore, by scaling $v$, we can assume w.l.o.g. that $x \triangleq v + \pi$ is a distribution. By Claim 3.3, $\|xM^{T(\varepsilon)} - \pi\|_{TV} \leq 2\varepsilon \|x - \pi\|_{TV}$, i.e. $\|xM^{T(\varepsilon)} - \pi\|_1 \leq 2\varepsilon \|x - \pi\|_1$. Observing that $(xM^{T(\varepsilon)} - \pi)$ and $(x - \pi)$ are simply $\lambda(M^{T(\varepsilon)})v$ and $v$, the above inequality means $\lambda(M^{T(\varepsilon)})\|v\|_1 \leq 2\varepsilon \|v\|_1$, which implies $\lambda(M^{T(\varepsilon)}) \le 2\varepsilon$, as desired.
