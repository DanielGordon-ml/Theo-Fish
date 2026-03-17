---
slug: chernoff-hoeffding-bounds-for-markov-chains--claim-3-1
label: Claim 3.1
claim_type: theorem
statement: For an ergodic Markov chain $M$ with $\varepsilon$-mixing time $T(\varepsilon)$
  where $0 < \varepsilon \le 1/2$, it holds that $\lambda(M^{T(\varepsilon)}) \le
  \sqrt{2\varepsilon}$.
proof: 'The idea is to reduce to the reversible case by considering the reversiblization
  of $M^{T(\varepsilon)}$. Let $\tilde{M}^{T(\varepsilon)}$ be the time reversal of
  $M^{T(\varepsilon)}$, and $R \triangleq M^{T(\varepsilon)}\tilde{M}^{T(\varepsilon)}$
  be the reversiblization of $M^{T(\varepsilon)}$. By Claim 3.1, $\lambda(M^{T(\varepsilon)})
  = \sqrt{\lambda(R)}$. Let us recall (from Section 2) that $M$, $M^{T(\varepsilon)}$,
  and $\tilde{M}^{T(\varepsilon)}$ all share the same stationary distribution $\pi$.
  Next, we claim that the $\varepsilon$-mixing-time of $R$ is $1$. This is because
  $\|\varphi M^{T(\varepsilon)}\tilde{M}^{T(\varepsilon)} - \pi\|_{TV} \leq \|\varphi
  M^{T(\varepsilon)} - \pi\|_{TV} \leq \varepsilon$ where the second inequality uses
  the definition of $T(\varepsilon)$ and the first inequality holds since any Markov
  transition is a contraction mapping: for any Markov transition, say $\boldsymbol{S}
  = (s(i,j))$, and any vector $x$, $\|\boldsymbol{x}\boldsymbol{S}\|_1 = \sum_j |\sum_i
  x_i s(i,j)| \le \sum_j \sum_i |x_i| s(i,j) = \sum_i |x_i| = \|\boldsymbol{x}\|_1$;
  putting $x = \varphi M^{T(\varepsilon)} - \pi$ and $S = \tilde{M}^{T(\varepsilon)}$
  gives the first inequality. Now, by Lemma 4, $\lambda(R) \leq 2\varepsilon$, and
  hence $\lambda(M^{T(\varepsilon)}) = \sqrt{\lambda(R)} \le \sqrt{2\varepsilon}$,
  as desired.'
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/spectral-gap]]'
- '[[concepts/ergodic-markov-chains]]'
- '[[concepts/epsilon-mixing-time-t-epsilon]]'
- '[[concepts/time-reversal]]'
- '[[concepts/multiplicative-reversiblization]]'
- '[[concepts/spectral-expansion-lambda-m]]'
- '[[concepts/irreversible-markov-chain]]'
- '[[concepts/contraction-mapping]]'
- '[[concepts/irreversible-markov-chain]]'
- '[[concepts/ergodic-markov-chains]]'
- '[[concepts/multiplicative-reversiblization]]'
- '[[concepts/contraction-mapping]]'
- '[[concepts/epsilon-mixing-time-t-epsilon]]'
- '[[concepts/spectral-expansion-lambda-m]]'
- '[[concepts/time-reversal]]'
- '[[concepts/spectral-gap]]'
- '[[concepts/contraction-mapping]]'
- '[[concepts/spectral-gap]]'
- '[[concepts/ergodic-markov-chains]]'
- '[[concepts/irreversible-markov-chain]]'
- '[[concepts/time-reversal]]'
- '[[concepts/multiplicative-reversiblization]]'
- '[[concepts/spectral-expansion-lambda-m]]'
- '[[concepts/epsilon-mixing-time-t-epsilon]]'
about_meta:
- target: '[[concepts/spectral-gap]]'
  role: primary
  aspect: ''
- target: '[[concepts/ergodic-markov-chains]]'
  role: primary
  aspect: ''
- target: '[[concepts/epsilon-mixing-time-t-epsilon]]'
  role: primary
  aspect: ''
- target: '[[concepts/time-reversal]]'
  role: primary
  aspect: ''
- target: '[[concepts/multiplicative-reversiblization]]'
  role: primary
  aspect: ''
- target: '[[concepts/spectral-expansion-lambda-m]]'
  role: primary
  aspect: ''
- target: '[[concepts/irreversible-markov-chain]]'
  role: primary
  aspect: ''
- target: '[[concepts/contraction-mapping]]'
  role: primary
  aspect: ''
- target: '[[concepts/irreversible-markov-chain]]'
  role: primary
  aspect: ''
- target: '[[concepts/ergodic-markov-chains]]'
  role: primary
  aspect: ''
- target: '[[concepts/multiplicative-reversiblization]]'
  role: primary
  aspect: ''
- target: '[[concepts/contraction-mapping]]'
  role: primary
  aspect: ''
- target: '[[concepts/epsilon-mixing-time-t-epsilon]]'
  role: primary
  aspect: ''
- target: '[[concepts/spectral-expansion-lambda-m]]'
  role: primary
  aspect: ''
- target: '[[concepts/time-reversal]]'
  role: primary
  aspect: ''
- target: '[[concepts/spectral-gap]]'
  role: primary
  aspect: ''
- target: '[[concepts/contraction-mapping]]'
  role: primary
  aspect: ''
- target: '[[concepts/spectral-gap]]'
  role: primary
  aspect: ''
- target: '[[concepts/ergodic-markov-chains]]'
  role: primary
  aspect: ''
- target: '[[concepts/irreversible-markov-chain]]'
  role: primary
  aspect: ''
- target: '[[concepts/time-reversal]]'
  role: primary
  aspect: ''
- target: '[[concepts/multiplicative-reversiblization]]'
  role: primary
  aspect: ''
- target: '[[concepts/spectral-expansion-lambda-m]]'
  role: primary
  aspect: ''
- target: '[[concepts/epsilon-mixing-time-t-epsilon]]'
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

# Claim 3.1

For an ergodic Markov chain $M$ with $\varepsilon$-mixing time $T(\varepsilon)$ where $0 < \varepsilon \le 1/2$, it holds that $\lambda(M^{T(\varepsilon)}) \le \sqrt{2\varepsilon}$.


## Proof

The idea is to reduce to the reversible case by considering the reversiblization of $M^{T(\varepsilon)}$. Let $\tilde{M}^{T(\varepsilon)}$ be the time reversal of $M^{T(\varepsilon)}$, and $R \triangleq M^{T(\varepsilon)}\tilde{M}^{T(\varepsilon)}$ be the reversiblization of $M^{T(\varepsilon)}$. By Claim 3.1, $\lambda(M^{T(\varepsilon)}) = \sqrt{\lambda(R)}$. Let us recall (from Section 2) that $M$, $M^{T(\varepsilon)}$, and $\tilde{M}^{T(\varepsilon)}$ all share the same stationary distribution $\pi$. Next, we claim that the $\varepsilon$-mixing-time of $R$ is $1$. This is because $\|\varphi M^{T(\varepsilon)}\tilde{M}^{T(\varepsilon)} - \pi\|_{TV} \leq \|\varphi M^{T(\varepsilon)} - \pi\|_{TV} \leq \varepsilon$ where the second inequality uses the definition of $T(\varepsilon)$ and the first inequality holds since any Markov transition is a contraction mapping: for any Markov transition, say $\boldsymbol{S} = (s(i,j))$, and any vector $x$, $\|\boldsymbol{x}\boldsymbol{S}\|_1 = \sum_j |\sum_i x_i s(i,j)| \le \sum_j \sum_i |x_i| s(i,j) = \sum_i |x_i| = \|\boldsymbol{x}\|_1$; putting $x = \varphi M^{T(\varepsilon)} - \pi$ and $S = \tilde{M}^{T(\varepsilon)}$ gives the first inequality. Now, by Lemma 4, $\lambda(R) \leq 2\varepsilon$, and hence $\lambda(M^{T(\varepsilon)}) = \sqrt{\lambda(R)} \le \sqrt{2\varepsilon}$, as desired.
