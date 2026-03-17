---
slug: k-strong-price-of-anarchy--theorem-v-2
label: Theorem V.2
claim_type: theorem
statement: 'Any resource allocation problem $(G, W) \in \mathcal{G}_n \times \{w\}$
  with the utility rule $\widetilde{u}_\zeta$ is $(1, \widetilde{\rho}_\zeta - 1)$-$k$-generalized-coalitionally
  smooth, where $\widetilde{u}_\zeta$ and $\widetilde{\rho}_\zeta$ are solutions to
  the linear program,

  $$\begin{array}{rl} (\widetilde{\rho}_\zeta, \widetilde{u}_\zeta) \in \arg\min_{\rho
  \ge 0, u \in \mathbb{R}_{\ge 0}^{n+1}} & \rho \\ \mathrm{s.t.} & 0 \ge w(o+x) -
  \rho w(e+x) + \left(\binom{n}{\zeta} u(e+x) - \sum_{\substack{0 \le \alpha \le e
  \\ 0 \le \beta \le o \\ \alpha+\beta \le \zeta}} \binom{e}{\alpha}\binom{o}{\beta}\binom{n-e-o}{\zeta-\alpha-\beta}
  u(e+x+\beta-\alpha)\right) \\ & \forall (e,x,o) \in \mathcal{T}. \end{array} \quad
  (\mathrm{Q}\zeta)$$'
proof: 'Consider the parameterization described in the proof of Proposition III.2,
  where for any two actions $a, a'' \in \mathcal{A}$, we can rewrite $W(a) = \sum_{e,x,o}
  \theta(e,x,o) w(e+x)$ and $W(a'') = \sum_{e,x,o} \theta(e,x,o) w(o+x)$. Now, we
  can additionally rewrite $U(a) = \sum_{e,x,o} \theta(e,x,o) u(e+x)$ and

  $$\sum_{\Gamma \in \mathcal{C}_\zeta} U(a''_\Gamma, a_{-\Gamma}) = \sum_{e,x,o}
  \theta(e,x,o) \sum_{\substack{0 \le \alpha \le e \\ 0 \le \beta \le o \\ \alpha+\beta
  \le \zeta}} \binom{e}{\alpha}\binom{o}{\beta}\binom{n-e-o}{\zeta-\alpha-\beta} u(e+x+\beta-\alpha).$$

  We can now write out (16), the $(\lambda, \mu)$-$k$-generalized-coalitionally smooth
  constraint, as

  $$\sum_{e,x,o} \theta(e,x,o) \left(\frac{1}{\binom{n}{\zeta}} \sum_{\substack{0
  \le \alpha \le e \\ 0 \le \beta \le o \\ \alpha+\beta \le \zeta}} \binom{e}{\alpha}\binom{o}{\beta}\binom{n-e-o}{\zeta-\alpha-\beta}
  u(e+x+\beta-\alpha) - u(e+x)\right) \geq \sum_{e,x,o} \theta(e,x,o) \left(\lambda_\zeta
  w(o+x) - (\mu_\zeta+1) w(e+x)\right).$$

  As before, we can observe that this constraint is sufficiently satisfied when

  $$\frac{1}{\binom{n}{\zeta}} \sum_{\substack{0 \le \alpha \le e \\ 0 \le \beta \le
  o \\ \alpha+\beta \le \zeta}} \binom{e}{\alpha}\binom{o}{\beta}\binom{n-e-o}{\zeta-\alpha-\beta}
  u(e+x+\beta-\alpha) - u(e+x) \geq \lambda_\zeta w(o+x) - (\mu_\zeta+1) w(e+x), \quad
  \forall (e,x,o) \in \mathcal{T}.$$

  The task of finding smoothness parameters that give the best price of anarchy guarantee
  becomes the same problem as $(\mathsf{P}1\zeta)$ but now with constraint set (20).
  By substituting the decision variables $\rho = (1+\mu_\zeta)/\lambda_\zeta$ and
  $\nu = 1/(\binom{n}{\zeta}\lambda_\zeta) \geq 0$ we attain the new constraint set

  $$0 \geq w(o+x) - \rho w(e+x) + \nu\left(\binom{n}{\zeta} u(e+x) - \sum_{\substack{0
  \le \alpha \le e \\ 0 \le \beta \le o \\ \alpha+\beta \le \zeta}} \binom{e}{\alpha}\binom{o}{\beta}\binom{n-e-o}{\zeta-\alpha-\beta}
  u(e+x+\beta-\alpha)\right), \quad \forall (e,x,o) \in \mathcal{T}.$$

  The new objective becomes $1/\rho$. Finally, we let $u \in \mathbb{R}_{\geq 0}^n$
  become a decision variable in the program. Observe that every occurrence of $u$
  is multiplied by $\nu$, and every occurrence of $\nu$ multiplies $u$. As such, we
  can define the new decision variable $u'' = \nu u$ and retrieve the linear program
  $(\mathrm{Q}\zeta)$.'
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/lambda-mu-k-generalized-coalitionally-smooth]]'
- '[[concepts/utility-rule-u]]'
- '[[concepts/class-of-resource-allocation-problems]]'
- '[[concepts/resource-allocation-games]]'
- '[[concepts/optimal-utility-rule]]'
- '[[concepts/linear-program-qz]]'
- '[[concepts/utility-design-problem]]'
- '[[concepts/k-strong-price-of-anarchy]]'
- '[[concepts/utility-rule-u]]'
- '[[concepts/lambda-mu-k-generalized-coalitionally-smooth]]'
- '[[concepts/linear-program-qz]]'
- '[[concepts/optimal-utility-rule]]'
- '[[concepts/resource-allocation-games]]'
- '[[concepts/utility-design-problem]]'
- '[[concepts/class-of-resource-allocation-problems]]'
- '[[concepts/k-strong-price-of-anarchy]]'
about_meta:
- target: '[[concepts/lambda-mu-k-generalized-coalitionally-smooth]]'
  role: primary
  aspect: ''
- target: '[[concepts/utility-rule-u]]'
  role: primary
  aspect: ''
- target: '[[concepts/class-of-resource-allocation-problems]]'
  role: primary
  aspect: ''
- target: '[[concepts/resource-allocation-games]]'
  role: primary
  aspect: ''
- target: '[[concepts/optimal-utility-rule]]'
  role: primary
  aspect: ''
- target: '[[concepts/linear-program-qz]]'
  role: primary
  aspect: ''
- target: '[[concepts/utility-design-problem]]'
  role: primary
  aspect: ''
- target: '[[concepts/k-strong-price-of-anarchy]]'
  role: primary
  aspect: ''
- target: '[[concepts/utility-rule-u]]'
  role: primary
  aspect: ''
- target: '[[concepts/lambda-mu-k-generalized-coalitionally-smooth]]'
  role: primary
  aspect: ''
- target: '[[concepts/linear-program-qz]]'
  role: primary
  aspect: ''
- target: '[[concepts/optimal-utility-rule]]'
  role: primary
  aspect: ''
- target: '[[concepts/resource-allocation-games]]'
  role: primary
  aspect: ''
- target: '[[concepts/utility-design-problem]]'
  role: primary
  aspect: ''
- target: '[[concepts/class-of-resource-allocation-problems]]'
  role: primary
  aspect: ''
- target: '[[concepts/k-strong-price-of-anarchy]]'
  role: primary
  aspect: ''
depends_on:
- '[[claims/k-strong-price-of-anarchy--proposition-iii-2]]'
- '[[claims/k-strong-price-of-anarchy--proposition-iii-2]]'
- '[[claims/k-strong-price-of-anarchy--proposition-iii-2]]'
- '[[claims/k-strong-price-of-anarchy--proposition-iii-2]]'
- '[[claims/k-strong-price-of-anarchy--proposition-iii-2]]'
- '[[claims/k-strong-price-of-anarchy--proposition-iii-2]]'
depends_on_meta:
- target: '[[claims/k-strong-price-of-anarchy--proposition-iii-2]]'
- target: '[[claims/k-strong-price-of-anarchy--proposition-iii-2]]'
- target: '[[claims/k-strong-price-of-anarchy--proposition-iii-2]]'
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

# Theorem V.2

Any resource allocation problem $(G, W) \in \mathcal{G}_n \times \{w\}$ with the utility rule $\widetilde{u}_\zeta$ is $(1, \widetilde{\rho}_\zeta - 1)$-$k$-generalized-coalitionally smooth, where $\widetilde{u}_\zeta$ and $\widetilde{\rho}_\zeta$ are solutions to the linear program,
$$\begin{array}{rl} (\widetilde{\rho}_\zeta, \widetilde{u}_\zeta) \in \arg\min_{\rho \ge 0, u \in \mathbb{R}_{\ge 0}^{n+1}} & \rho \\ \mathrm{s.t.} & 0 \ge w(o+x) - \rho w(e+x) + \left(\binom{n}{\zeta} u(e+x) - \sum_{\substack{0 \le \alpha \le e \\ 0 \le \beta \le o \\ \alpha+\beta \le \zeta}} \binom{e}{\alpha}\binom{o}{\beta}\binom{n-e-o}{\zeta-\alpha-\beta} u(e+x+\beta-\alpha)\right) \\ & \forall (e,x,o) \in \mathcal{T}. \end{array} \quad (\mathrm{Q}\zeta)$$


## Proof

Consider the parameterization described in the proof of Proposition III.2, where for any two actions $a, a' \in \mathcal{A}$, we can rewrite $W(a) = \sum_{e,x,o} \theta(e,x,o) w(e+x)$ and $W(a') = \sum_{e,x,o} \theta(e,x,o) w(o+x)$. Now, we can additionally rewrite $U(a) = \sum_{e,x,o} \theta(e,x,o) u(e+x)$ and
$$\sum_{\Gamma \in \mathcal{C}_\zeta} U(a'_\Gamma, a_{-\Gamma}) = \sum_{e,x,o} \theta(e,x,o) \sum_{\substack{0 \le \alpha \le e \\ 0 \le \beta \le o \\ \alpha+\beta \le \zeta}} \binom{e}{\alpha}\binom{o}{\beta}\binom{n-e-o}{\zeta-\alpha-\beta} u(e+x+\beta-\alpha).$$
We can now write out (16), the $(\lambda, \mu)$-$k$-generalized-coalitionally smooth constraint, as
$$\sum_{e,x,o} \theta(e,x,o) \left(\frac{1}{\binom{n}{\zeta}} \sum_{\substack{0 \le \alpha \le e \\ 0 \le \beta \le o \\ \alpha+\beta \le \zeta}} \binom{e}{\alpha}\binom{o}{\beta}\binom{n-e-o}{\zeta-\alpha-\beta} u(e+x+\beta-\alpha) - u(e+x)\right) \geq \sum_{e,x,o} \theta(e,x,o) \left(\lambda_\zeta w(o+x) - (\mu_\zeta+1) w(e+x)\right).$$
As before, we can observe that this constraint is sufficiently satisfied when
$$\frac{1}{\binom{n}{\zeta}} \sum_{\substack{0 \le \alpha \le e \\ 0 \le \beta \le o \\ \alpha+\beta \le \zeta}} \binom{e}{\alpha}\binom{o}{\beta}\binom{n-e-o}{\zeta-\alpha-\beta} u(e+x+\beta-\alpha) - u(e+x) \geq \lambda_\zeta w(o+x) - (\mu_\zeta+1) w(e+x), \quad \forall (e,x,o) \in \mathcal{T}.$$
The task of finding smoothness parameters that give the best price of anarchy guarantee becomes the same problem as $(\mathsf{P}1\zeta)$ but now with constraint set (20). By substituting the decision variables $\rho = (1+\mu_\zeta)/\lambda_\zeta$ and $\nu = 1/(\binom{n}{\zeta}\lambda_\zeta) \geq 0$ we attain the new constraint set
$$0 \geq w(o+x) - \rho w(e+x) + \nu\left(\binom{n}{\zeta} u(e+x) - \sum_{\substack{0 \le \alpha \le e \\ 0 \le \beta \le o \\ \alpha+\beta \le \zeta}} \binom{e}{\alpha}\binom{o}{\beta}\binom{n-e-o}{\zeta-\alpha-\beta} u(e+x+\beta-\alpha)\right), \quad \forall (e,x,o) \in \mathcal{T}.$$
The new objective becomes $1/\rho$. Finally, we let $u \in \mathbb{R}_{\geq 0}^n$ become a decision variable in the program. Observe that every occurrence of $u$ is multiplied by $\nu$, and every occurrence of $\nu$ multiplies $u$. As such, we can define the new decision variable $u' = \nu u$ and retrieve the linear program $(\mathrm{Q}\zeta)$.
