---
slug: k-strong-price-of-anarchy--proposition-v-1
label: Proposition V.1
claim_type: proposition
statement: 'A system $(G, W, U)$ that is $(\lambda, \mu)$-$k$-generalized-coalitionally
  smooth has $k$-strong price of anarchy satisfying

  $$\mathrm{SPoA}_k(G, W, U) \ge \frac{\lambda_\zeta}{1 + \mu_\zeta}, \ \forall \zeta
  \in [k].$$'
proof: 'Let $a^{k\mathrm{SNE}} \in \mathcal{A}$ denote a $k$-strong Nash equilibrium
  when agents follow objective function $U$, and let $a^{\mathrm{opt}} \in \arg\max_{a
  \in \mathcal{A}} W(a)$ denote an optimal joint action. For any $\zeta \in [k]$,
  we have

  $$W(a^{k\mathrm{SNE}}) \geq \frac{1}{\binom{n}{\zeta}} \sum_{\Gamma \in \mathcal{C}_\zeta}
  U(a_\Gamma^{\mathrm{opt}}, a_{-\Gamma}^{k\mathrm{SNE}}) - U(a^{k\mathrm{SNE}}) +
  W(a^{k\mathrm{SNE}})$$

  $$\geq \lambda_\zeta W(a^{\mathrm{opt}}) - \mu_\zeta W(a^{k\mathrm{SNE}}).$$

  Where the first inequality holds from $\frac{1}{\binom{n}{\zeta}} \sum_{\Gamma \in
  \mathcal{C}_\zeta} U(a_\Gamma^{\mathrm{opt}}, a_{-\Gamma}^{k\mathrm{SNE}}) - U(a^{k\mathrm{SNE}})
  \ge 0$ by $a^{k\mathrm{SNE}}$ being a $k$-strong Nash equilibrium and the second
  holds from Definition 3. Rearranging, we get $W(a^{k\mathrm{SNE}}) / W(a^{\mathrm{opt}})
  \geq \lambda_\zeta / (1 + \mu_\zeta)$.'
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/multiagent-system-with-utility-design]]'
- '[[concepts/lambda-mu-k-generalized-coalitionally-smooth]]'
- '[[concepts/k-strong-price-of-anarchy]]'
- '[[concepts/k-strong-nash-equilibrium-under-u]]'
about_meta:
- target: '[[concepts/multiagent-system-with-utility-design]]'
  role: primary
  aspect: ''
- target: '[[concepts/lambda-mu-k-generalized-coalitionally-smooth]]'
  role: primary
  aspect: ''
- target: '[[concepts/k-strong-price-of-anarchy]]'
  role: primary
  aspect: ''
- target: '[[concepts/k-strong-nash-equilibrium-under-u]]'
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

# Proposition V.1

A system $(G, W, U)$ that is $(\lambda, \mu)$-$k$-generalized-coalitionally smooth has $k$-strong price of anarchy satisfying
$$\mathrm{SPoA}_k(G, W, U) \ge \frac{\lambda_\zeta}{1 + \mu_\zeta}, \ \forall \zeta \in [k].$$


## Proof

Let $a^{k\mathrm{SNE}} \in \mathcal{A}$ denote a $k$-strong Nash equilibrium when agents follow objective function $U$, and let $a^{\mathrm{opt}} \in \arg\max_{a \in \mathcal{A}} W(a)$ denote an optimal joint action. For any $\zeta \in [k]$, we have
$$W(a^{k\mathrm{SNE}}) \geq \frac{1}{\binom{n}{\zeta}} \sum_{\Gamma \in \mathcal{C}_\zeta} U(a_\Gamma^{\mathrm{opt}}, a_{-\Gamma}^{k\mathrm{SNE}}) - U(a^{k\mathrm{SNE}}) + W(a^{k\mathrm{SNE}})$$
$$\geq \lambda_\zeta W(a^{\mathrm{opt}}) - \mu_\zeta W(a^{k\mathrm{SNE}}).$$
Where the first inequality holds from $\frac{1}{\binom{n}{\zeta}} \sum_{\Gamma \in \mathcal{C}_\zeta} U(a_\Gamma^{\mathrm{opt}}, a_{-\Gamma}^{k\mathrm{SNE}}) - U(a^{k\mathrm{SNE}}) \ge 0$ by $a^{k\mathrm{SNE}}$ being a $k$-strong Nash equilibrium and the second holds from Definition 3. Rearranging, we get $W(a^{k\mathrm{SNE}}) / W(a^{\mathrm{opt}}) \geq \lambda_\zeta / (1 + \mu_\zeta)$.
