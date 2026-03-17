---
slug: k-strong-price-of-anarchy--proposition-iii-1
label: Proposition III.1
claim_type: proposition
statement: 'A system $(G, W)$ that is $(\lambda, \mu)$-$k$-coalitionally smooth has
  $k$-strong price of anarchy satisfying

  $$\operatorname{SPoA}_k(G, W) \geq \frac{\lambda_\zeta}{1 + \mu_\zeta}, \ \forall
  \zeta \in [k].$$'
proof: 'Let $a^{k\mathrm{SNE}} \in \mathcal{A}$ denote a $k$-strong Nash equilibrium
  in the system $(G, W)$ (i.e., satisfying Definition 1), and let $a^{\mathrm{opt}}
  \in \arg\max_{a \in \mathcal{A}} W(a)$ denote an optimal joint action. For any $\zeta
  \in [k]$, we have

  $$W(a^{k\mathrm{SNE}}) = \frac{1}{\binom{n}{\zeta}} \sum_{\Gamma \in \mathcal{C}_\zeta}
  W(a^{k\mathrm{SNE}})$$

  $$\geq \frac{1}{\binom{n}{\zeta}} \sum_{\Gamma \in \mathcal{C}_\zeta} W(a_\Gamma^{\mathrm{opt}},
  a_{-\Gamma}^{k\mathrm{SNE}})$$

  $$\geq \lambda_\zeta W(a^{\mathrm{opt}}) - \mu_\zeta W(a^{k\mathrm{SNE}}).$$

  Where (7a) holds from $|\mathcal{C}_\zeta| = \binom{n}{\zeta}$, (7b) holds from
  Definition 1, and (7c) holds from Definition 2. Rearranging, we get $W(a^{k\mathrm{SNE}})
  / W(a^{\mathrm{opt}}) \geq \lambda_\zeta / (1 + \mu_\zeta)$.'
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/k-strong-price-of-anarchy]]'
- '[[concepts/lambda-mu-k-coalitionally-smooth-game]]'
- '[[concepts/system-welfare]]'
- '[[concepts/k-strong-nash-equilibrium]]'
about_meta:
- target: '[[concepts/k-strong-price-of-anarchy]]'
  role: primary
  aspect: ''
- target: '[[concepts/lambda-mu-k-coalitionally-smooth-game]]'
  role: primary
  aspect: ''
- target: '[[concepts/system-welfare]]'
  role: primary
  aspect: ''
- target: '[[concepts/k-strong-nash-equilibrium]]'
  role: primary
  aspect: ''
depends_on: []
depends_on_meta: []
sourced_from:
- '[[sources/k_strong_price_of_anarchy|k_strong_price_of_anarchy]]'
sourced_from_meta:
- target: '[[sources/k_strong_price_of_anarchy|k_strong_price_of_anarchy]]'
  section: ''
  page: ''
  confidence: 0.0
---

# Proposition III.1

A system $(G, W)$ that is $(\lambda, \mu)$-$k$-coalitionally smooth has $k$-strong price of anarchy satisfying
$$\operatorname{SPoA}_k(G, W) \geq \frac{\lambda_\zeta}{1 + \mu_\zeta}, \ \forall \zeta \in [k].$$


## Proof

Let $a^{k\mathrm{SNE}} \in \mathcal{A}$ denote a $k$-strong Nash equilibrium in the system $(G, W)$ (i.e., satisfying Definition 1), and let $a^{\mathrm{opt}} \in \arg\max_{a \in \mathcal{A}} W(a)$ denote an optimal joint action. For any $\zeta \in [k]$, we have
$$W(a^{k\mathrm{SNE}}) = \frac{1}{\binom{n}{\zeta}} \sum_{\Gamma \in \mathcal{C}_\zeta} W(a^{k\mathrm{SNE}})$$
$$\geq \frac{1}{\binom{n}{\zeta}} \sum_{\Gamma \in \mathcal{C}_\zeta} W(a_\Gamma^{\mathrm{opt}}, a_{-\Gamma}^{k\mathrm{SNE}})$$
$$\geq \lambda_\zeta W(a^{\mathrm{opt}}) - \mu_\zeta W(a^{k\mathrm{SNE}}).$$
Where (7a) holds from $|\mathcal{C}_\zeta| = \binom{n}{\zeta}$, (7b) holds from Definition 1, and (7c) holds from Definition 2. Rearranging, we get $W(a^{k\mathrm{SNE}}) / W(a^{\mathrm{opt}}) \geq \lambda_\zeta / (1 + \mu_\zeta)$.
