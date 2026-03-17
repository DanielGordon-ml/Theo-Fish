---
slug: k-strong-price-of-anarchy--proposition-v-3
label: Proposition V.3
claim_type: proposition
statement: The reciprocal of the value of the linear program $(\mathrm{Q}[k])$ provides
  an upper bound on the $k$-strong price of anarchy under the optimal utility design.
  The program $(\mathrm{Q}[k])$ is obtained by generalizing the constraint set of
  $(\mathrm{P}[k])$ with respect to a utility rule $u$, yielding the constraint $0
  \geq w(o+x) - \rho w(e+x) + \sum_{\zeta \in [k]} \nu_\zeta \left(\binom{n}{\zeta}
  u(e+x) - \sum_{\substack{0 \leq \alpha \leq e \\ 0 \leq \beta \leq o \\ \alpha+\beta
  \leq \zeta}} \binom{e}{\alpha}\binom{o}{\beta}\binom{n-e-o}{\zeta-\alpha-\beta}
  u(e+x+\beta-\alpha)\right)$, $\forall (e,x,o) \in \mathcal{T}$, and then substituting
  the new decision variable $u_\zeta \in \mathbb{R}_{\geq 0}^n$ into each occurrence
  of $\nu_\zeta u$, which enlarges the feasible set.
proof: The proof is straightforward and simply requires generalizing the constraint
  set of $(\mathrm{P}[k])$. Consider taking the same steps as the proof of Theorem
  III.3 but with the equilibrium constraint defined by the utility rule $u$. This
  will result in the same linear program as in $(\mathrm{P}[k])$, but now with the
  constraint set $0 \geq w(o+x) - \rho w(e+x) + \sum_{\zeta \in [k]} \nu_\zeta (\binom{n}{\zeta}
  u(e+x) - \sum_{\substack{0 \leq \alpha \leq e \\ 0 \leq \beta \leq o \\ \alpha+\beta
  \leq \zeta}} \binom{e}{\alpha}\binom{o}{\beta}\binom{n-e-o}{\zeta-\alpha-\beta}
  u(e+x+\beta-\alpha))$, $\forall (e,x,o) \in \mathcal{T}$. At this point, the new
  linear program will provide tight bounds on a specified utility rule $u$. Finally,
  we substitute the new decision variable $u_\zeta \in \mathbb{R}_{\geq 0}^n$ into
  each occurrence of $\nu_\zeta u$. This enlarges the feasible set, which now subsumes
  all the feasible points that would evaluate a utility rule $u$ by satisfying $u
  = u_\zeta$ for all $\zeta \in [k]$. As we do not enforce this constraint, the value
  of the final program $(\mathrm{Q}[k])$ provides a lower bound on the original program,
  or its reciprocal provides an upper bound on the $k$-strong price of anarchy under
  the optimal utility design.
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/k-strong-price-of-anarchy]]'
- '[[concepts/utility-design-problem]]'
- '[[concepts/optimal-utility-rule]]'
- '[[concepts/linear-program-qz]]'
- '[[concepts/utility-rule-u]]'
- '[[concepts/class-of-resource-allocation-problems]]'
- '[[concepts/resource-allocation-games]]'
- '[[concepts/linear-program]]'
- '[[concepts/k-strong-price-of-anarchy]]'
- '[[concepts/linear-program-qz]]'
- '[[concepts/linear-program]]'
- '[[concepts/utility-rule-u]]'
- '[[concepts/class-of-resource-allocation-problems]]'
- '[[concepts/utility-design-problem]]'
- '[[concepts/resource-allocation-games]]'
- '[[concepts/optimal-utility-rule]]'
about_meta:
- target: '[[concepts/k-strong-price-of-anarchy]]'
  role: primary
  aspect: ''
- target: '[[concepts/utility-design-problem]]'
  role: primary
  aspect: ''
- target: '[[concepts/optimal-utility-rule]]'
  role: primary
  aspect: ''
- target: '[[concepts/linear-program-qz]]'
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
- target: '[[concepts/linear-program]]'
  role: primary
  aspect: ''
- target: '[[concepts/k-strong-price-of-anarchy]]'
  role: primary
  aspect: ''
- target: '[[concepts/linear-program-qz]]'
  role: primary
  aspect: ''
- target: '[[concepts/linear-program]]'
  role: primary
  aspect: ''
- target: '[[concepts/utility-rule-u]]'
  role: primary
  aspect: ''
- target: '[[concepts/class-of-resource-allocation-problems]]'
  role: primary
  aspect: ''
- target: '[[concepts/utility-design-problem]]'
  role: primary
  aspect: ''
- target: '[[concepts/resource-allocation-games]]'
  role: primary
  aspect: ''
- target: '[[concepts/optimal-utility-rule]]'
  role: primary
  aspect: ''
depends_on:
- '[[claims/k-strong-price-of-anarchy--theorem-iii-3]]'
- '[[claims/k-strong-price-of-anarchy--theorem-iii-3]]'
- '[[claims/k-strong-price-of-anarchy--theorem-iii-3]]'
- '[[claims/k-strong-price-of-anarchy--theorem-iii-3]]'
- '[[claims/k-strong-price-of-anarchy--theorem-iii-3]]'
- '[[claims/k-strong-price-of-anarchy--theorem-iii-3]]'
- '[[claims/k-strong-price-of-anarchy--theorem-iii-3]]'
- '[[claims/k-strong-price-of-anarchy--theorem-iii-3]]'
depends_on_meta:
- target: '[[claims/k-strong-price-of-anarchy--theorem-iii-3]]'
- target: '[[claims/k-strong-price-of-anarchy--theorem-iii-3]]'
- target: '[[claims/k-strong-price-of-anarchy--theorem-iii-3]]'
- target: '[[claims/k-strong-price-of-anarchy--theorem-iii-3]]'
- target: '[[claims/k-strong-price-of-anarchy--theorem-iii-3]]'
- target: '[[claims/k-strong-price-of-anarchy--theorem-iii-3]]'
- target: '[[claims/k-strong-price-of-anarchy--theorem-iii-3]]'
- target: '[[claims/k-strong-price-of-anarchy--theorem-iii-3]]'
sourced_from:
- '[[sources/k_strong_price_of_anarchy|k_strong_price_of_anarchy]]'
sourced_from_meta:
- target: '[[sources/k_strong_price_of_anarchy|k_strong_price_of_anarchy]]'
  section: ''
  page: ''
  confidence: 0.0
---

# Proposition V.3

The reciprocal of the value of the linear program $(\mathrm{Q}[k])$ provides an upper bound on the $k$-strong price of anarchy under the optimal utility design. The program $(\mathrm{Q}[k])$ is obtained by generalizing the constraint set of $(\mathrm{P}[k])$ with respect to a utility rule $u$, yielding the constraint $0 \geq w(o+x) - \rho w(e+x) + \sum_{\zeta \in [k]} \nu_\zeta \left(\binom{n}{\zeta} u(e+x) - \sum_{\substack{0 \leq \alpha \leq e \\ 0 \leq \beta \leq o \\ \alpha+\beta \leq \zeta}} \binom{e}{\alpha}\binom{o}{\beta}\binom{n-e-o}{\zeta-\alpha-\beta} u(e+x+\beta-\alpha)\right)$, $\forall (e,x,o) \in \mathcal{T}$, and then substituting the new decision variable $u_\zeta \in \mathbb{R}_{\geq 0}^n$ into each occurrence of $\nu_\zeta u$, which enlarges the feasible set.


## Proof

The proof is straightforward and simply requires generalizing the constraint set of $(\mathrm{P}[k])$. Consider taking the same steps as the proof of Theorem III.3 but with the equilibrium constraint defined by the utility rule $u$. This will result in the same linear program as in $(\mathrm{P}[k])$, but now with the constraint set $0 \geq w(o+x) - \rho w(e+x) + \sum_{\zeta \in [k]} \nu_\zeta (\binom{n}{\zeta} u(e+x) - \sum_{\substack{0 \leq \alpha \leq e \\ 0 \leq \beta \leq o \\ \alpha+\beta \leq \zeta}} \binom{e}{\alpha}\binom{o}{\beta}\binom{n-e-o}{\zeta-\alpha-\beta} u(e+x+\beta-\alpha))$, $\forall (e,x,o) \in \mathcal{T}$. At this point, the new linear program will provide tight bounds on a specified utility rule $u$. Finally, we substitute the new decision variable $u_\zeta \in \mathbb{R}_{\geq 0}^n$ into each occurrence of $\nu_\zeta u$. This enlarges the feasible set, which now subsumes all the feasible points that would evaluate a utility rule $u$ by satisfying $u = u_\zeta$ for all $\zeta \in [k]$. As we do not enforce this constraint, the value of the final program $(\mathrm{Q}[k])$ provides a lower bound on the original program, or its reciprocal provides an upper bound on the $k$-strong price of anarchy under the optimal utility design.
