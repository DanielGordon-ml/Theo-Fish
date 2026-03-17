---
slug: k-strong-price-of-anarchy--proposition-iii-2
label: Proposition III.2
claim_type: proposition
statement: 'The coalitional smoothness constraint (5) is satisfied for all games $G
  \in \mathcal{G}_n$ and all respective joint actions $a, a'' \in \mathcal{A}$ if
  and only if for each label $(e,x,o) \in \mathcal{T}$, the following holds: $\frac{1}{\binom{n}{\zeta}}
  \sum_{\substack{0 \leq \alpha \leq e \\ 0 \leq \beta \leq o \\ \alpha+\beta \leq
  \zeta}} \binom{e}{\alpha}\binom{o}{\beta}\binom{n-e-o}{\zeta-\alpha-\beta} w(e+x+\beta-\alpha)
  \geq \lambda_\zeta w(o+x) - \mu_\zeta w(e+x)$. The optimal smoothness parameters
  are found by the optimization problem $(\mathrm{P}\zeta)$.'
proof: 'The proof largely relies on introducing a parameterization that lets us treat
  (5) as a set of linear constraints. Consider a resource allocation game $(G, w)
  \in \mathcal{G}_n \times \{w\}$ and any two actions $a, a'' \in \mathcal{A}$. To
  each resource $r \in \mathcal{R}$, we assign a label $(e_r, x_r, o_r)$, where $e_r
  = |\{i \in N \mid r \in a_i \setminus a_i''\}|$, $x_r = |\{i \in N \mid r \in a_i
  \cap a_i''\}|$, $o_r = |\{i \in N \mid r \in a_i'' \setminus a_i\}|$. This is to
  say, $e_r$ denotes the number of agents utilizing resource $r$ in joint action $a$
  but not $a''$, $o_r$ is the number that uses resource $r$ in joint action $a''$
  but not $a$, and $x_r$ is the number that uses $r$ in both $a$ and $a''$. In the
  set of games $\mathcal{G}_n$, let $\mathcal{T} = \{(e,x,o) \in \mathbb{N}_{\geq
  0}^3 \mid 1 \leq e+x+o \leq n\}$ denote the set of possible labels, and $\theta(e,x,o)
  := \sum_{r \in \mathcal{R}_{(e,x,o)}} v_r$, where $\mathcal{R}_{(e,x,o)} = \{r \in
  \mathcal{R} \mid e_r = e, x_r = x, o_r = o\}$ denotes the set of resources with
  label $(e,x,o)$. The parameter $\theta \in \mathbb{R}_{\geq 0}^{|\mathcal{T}|}$
  is a vector with elements for each label. We will now express the terms in (5) using
  this parameterization. Because $W(a) = \sum_{r \in \mathcal{R}} v_r w(|a|_r)$ depends
  only on the number of agents utilizing a resource; we can represent $|a|_r = e_r
  + x_r$ and write the system welfare as $W(a) = \sum_{(e,x,o) \in \mathcal{T}} \left(\sum_{r
  \in \mathcal{R}_{e,x,o}} v_r\right) w(e+x) = \sum_{e,x,o} \theta(e,x,o) w(e+x)$.
  Similar steps can be followed to show $W(a'') = \sum_{e,x,o} \theta(e,x,o) w(o+x)$.
  Finally, the term $\sum_{\Gamma \in \mathcal{C}_\zeta} W(a_\Gamma'', a_{-\Gamma})$
  can similarly be transcribed by this parameterization, where the set of coalitions
  $\mathcal{C}_\zeta$ was partitioned according to the action profile of the agents
  in each coalition. We let $\alpha$ denote the number of agents in $\Gamma$ that
  utilize resource $r$ only in joint action $a$ and $\beta$ the number of agents in
  $\Gamma$ that utilize resource $r$ only in joint action $a''$. By simple counting
  arguments, there are exactly $\binom{e}{\alpha}\binom{o}{\beta}\binom{n-e-o}{\zeta-\alpha-\beta}$
  coalitions grouped with the same $\alpha$. This decomposition is possible as the
  number of agents utilizing resource $r$ after a group $\Gamma$ deviates is precisely
  $e+x+\beta-\alpha$. The smoothness constraint (5) is satisfied only if $\frac{1}{\binom{n}{\zeta}}
  \sum_{e,x,o} \theta(e,x,o) \sum_{\substack{0 \leq \alpha \leq e \\ 0 \leq \beta
  \leq o \\ \alpha+\beta \leq \zeta}} \binom{e}{\alpha}\binom{o}{\beta}\binom{n-e-o}{\zeta-\alpha-\beta}
  w(e+x+\beta-\alpha) \geq \lambda_\zeta \sum_{e,x,o} \theta(e,x,o) w(o+x) - \mu_\zeta
  \sum_{e,x,o} \theta(e,x,o) w(e+x)$. As $\theta(e,x,o) \geq 0$ for all $(e,x,o) \in
  \mathcal{T}$, it is sufficient to satisfy (9) for each label independently. Observe
  that (9) is independent of $a$, $a''$, and $G$. As such, this set of constraints
  serves as a sufficient condition that any $G \in \mathcal{G}_n$ satisfies (5) for
  all respective $a, a'' \in \mathcal{A}$. To find parameters $\lambda_\zeta$ and
  $\mu_\zeta$ that provide the best $k$-strong price of anarchy guarantee, we formulate
  the optimization problem $(\mathrm{P}1\zeta)$: $\max_{\lambda_\zeta, \mu_\zeta \geq
  0} \frac{\lambda_\zeta}{1+\mu_\zeta}$. We restrict $\lambda_\zeta$ to be non-negative,
  though this constraint is not active except in degenerate cases. Finally, we transform
  $(\mathrm{P}1\zeta)$ by substituting new decision variables $\rho = (1+\mu_\zeta)/\lambda_\zeta$
  and $\nu = 1/(\binom{n}{\zeta}\lambda_\zeta) \geq 0$. The new objective becomes
  $1/\rho$. Note that the constraint $(e,x,o) = (1,0,0)$ implies $\rho \geq 0$; we
  can thus invert the objective and change the minimization to a maximization, giving
  $(\mathrm{P}\zeta)$.'
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/binomial-coefficient]]'
- '[[concepts/label-parameter]]'
- '[[concepts/linear-program]]'
- '[[concepts/k-strong-price-of-anarchy]]'
- '[[concepts/class-of-resource-allocation-problems]]'
- '[[concepts/label-parameter-vector]]'
- '[[concepts/smoothness-parameter-optimization-problem]]'
- '[[concepts/resource-allocation-games]]'
- '[[concepts/lambda-mu-k-coalitionally-smooth-game]]'
- '[[concepts/binomial-coefficient]]'
- '[[concepts/smoothness-parameter-optimization-problem]]'
- '[[concepts/class-of-resource-allocation-problems]]'
- '[[concepts/label-parameter]]'
- '[[concepts/linear-program]]'
- '[[concepts/label-parameter-vector]]'
- '[[concepts/lambda-mu-k-coalitionally-smooth-game]]'
- '[[concepts/resource-allocation-games]]'
- '[[concepts/k-strong-price-of-anarchy]]'
- '[[concepts/smoothness-parameter-optimization-problem]]'
- '[[concepts/label-parameter-vector]]'
- '[[concepts/lambda-mu-k-coalitionally-smooth-game]]'
- '[[concepts/binomial-coefficient]]'
- '[[concepts/k-strong-price-of-anarchy]]'
- '[[concepts/linear-program]]'
- '[[concepts/class-of-resource-allocation-problems]]'
- '[[concepts/resource-allocation-games]]'
- '[[concepts/label-parameter]]'
about_meta:
- target: '[[concepts/binomial-coefficient]]'
  role: primary
  aspect: ''
- target: '[[concepts/label-parameter]]'
  role: primary
  aspect: ''
- target: '[[concepts/linear-program]]'
  role: primary
  aspect: ''
- target: '[[concepts/k-strong-price-of-anarchy]]'
  role: primary
  aspect: ''
- target: '[[concepts/class-of-resource-allocation-problems]]'
  role: primary
  aspect: ''
- target: '[[concepts/label-parameter-vector]]'
  role: primary
  aspect: ''
- target: '[[concepts/smoothness-parameter-optimization-problem]]'
  role: primary
  aspect: ''
- target: '[[concepts/resource-allocation-games]]'
  role: primary
  aspect: ''
- target: '[[concepts/lambda-mu-k-coalitionally-smooth-game]]'
  role: primary
  aspect: ''
- target: '[[concepts/binomial-coefficient]]'
  role: primary
  aspect: ''
- target: '[[concepts/smoothness-parameter-optimization-problem]]'
  role: primary
  aspect: ''
- target: '[[concepts/class-of-resource-allocation-problems]]'
  role: primary
  aspect: ''
- target: '[[concepts/label-parameter]]'
  role: primary
  aspect: ''
- target: '[[concepts/linear-program]]'
  role: primary
  aspect: ''
- target: '[[concepts/label-parameter-vector]]'
  role: primary
  aspect: ''
- target: '[[concepts/lambda-mu-k-coalitionally-smooth-game]]'
  role: primary
  aspect: ''
- target: '[[concepts/resource-allocation-games]]'
  role: primary
  aspect: ''
- target: '[[concepts/k-strong-price-of-anarchy]]'
  role: primary
  aspect: ''
- target: '[[concepts/smoothness-parameter-optimization-problem]]'
  role: primary
  aspect: ''
- target: '[[concepts/label-parameter-vector]]'
  role: primary
  aspect: ''
- target: '[[concepts/lambda-mu-k-coalitionally-smooth-game]]'
  role: primary
  aspect: ''
- target: '[[concepts/binomial-coefficient]]'
  role: primary
  aspect: ''
- target: '[[concepts/k-strong-price-of-anarchy]]'
  role: primary
  aspect: ''
- target: '[[concepts/linear-program]]'
  role: primary
  aspect: ''
- target: '[[concepts/class-of-resource-allocation-problems]]'
  role: primary
  aspect: ''
- target: '[[concepts/resource-allocation-games]]'
  role: primary
  aspect: ''
- target: '[[concepts/label-parameter]]'
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

# Proposition III.2

The coalitional smoothness constraint (5) is satisfied for all games $G \in \mathcal{G}_n$ and all respective joint actions $a, a' \in \mathcal{A}$ if and only if for each label $(e,x,o) \in \mathcal{T}$, the following holds: $\frac{1}{\binom{n}{\zeta}} \sum_{\substack{0 \leq \alpha \leq e \\ 0 \leq \beta \leq o \\ \alpha+\beta \leq \zeta}} \binom{e}{\alpha}\binom{o}{\beta}\binom{n-e-o}{\zeta-\alpha-\beta} w(e+x+\beta-\alpha) \geq \lambda_\zeta w(o+x) - \mu_\zeta w(e+x)$. The optimal smoothness parameters are found by the optimization problem $(\mathrm{P}\zeta)$.


## Proof

The proof largely relies on introducing a parameterization that lets us treat (5) as a set of linear constraints. Consider a resource allocation game $(G, w) \in \mathcal{G}_n \times \{w\}$ and any two actions $a, a' \in \mathcal{A}$. To each resource $r \in \mathcal{R}$, we assign a label $(e_r, x_r, o_r)$, where $e_r = |\{i \in N \mid r \in a_i \setminus a_i'\}|$, $x_r = |\{i \in N \mid r \in a_i \cap a_i'\}|$, $o_r = |\{i \in N \mid r \in a_i' \setminus a_i\}|$. This is to say, $e_r$ denotes the number of agents utilizing resource $r$ in joint action $a$ but not $a'$, $o_r$ is the number that uses resource $r$ in joint action $a'$ but not $a$, and $x_r$ is the number that uses $r$ in both $a$ and $a'$. In the set of games $\mathcal{G}_n$, let $\mathcal{T} = \{(e,x,o) \in \mathbb{N}_{\geq 0}^3 \mid 1 \leq e+x+o \leq n\}$ denote the set of possible labels, and $\theta(e,x,o) := \sum_{r \in \mathcal{R}_{(e,x,o)}} v_r$, where $\mathcal{R}_{(e,x,o)} = \{r \in \mathcal{R} \mid e_r = e, x_r = x, o_r = o\}$ denotes the set of resources with label $(e,x,o)$. The parameter $\theta \in \mathbb{R}_{\geq 0}^{|\mathcal{T}|}$ is a vector with elements for each label. We will now express the terms in (5) using this parameterization. Because $W(a) = \sum_{r \in \mathcal{R}} v_r w(|a|_r)$ depends only on the number of agents utilizing a resource; we can represent $|a|_r = e_r + x_r$ and write the system welfare as $W(a) = \sum_{(e,x,o) \in \mathcal{T}} \left(\sum_{r \in \mathcal{R}_{e,x,o}} v_r\right) w(e+x) = \sum_{e,x,o} \theta(e,x,o) w(e+x)$. Similar steps can be followed to show $W(a') = \sum_{e,x,o} \theta(e,x,o) w(o+x)$. Finally, the term $\sum_{\Gamma \in \mathcal{C}_\zeta} W(a_\Gamma', a_{-\Gamma})$ can similarly be transcribed by this parameterization, where the set of coalitions $\mathcal{C}_\zeta$ was partitioned according to the action profile of the agents in each coalition. We let $\alpha$ denote the number of agents in $\Gamma$ that utilize resource $r$ only in joint action $a$ and $\beta$ the number of agents in $\Gamma$ that utilize resource $r$ only in joint action $a'$. By simple counting arguments, there are exactly $\binom{e}{\alpha}\binom{o}{\beta}\binom{n-e-o}{\zeta-\alpha-\beta}$ coalitions grouped with the same $\alpha$. This decomposition is possible as the number of agents utilizing resource $r$ after a group $\Gamma$ deviates is precisely $e+x+\beta-\alpha$. The smoothness constraint (5) is satisfied only if $\frac{1}{\binom{n}{\zeta}} \sum_{e,x,o} \theta(e,x,o) \sum_{\substack{0 \leq \alpha \leq e \\ 0 \leq \beta \leq o \\ \alpha+\beta \leq \zeta}} \binom{e}{\alpha}\binom{o}{\beta}\binom{n-e-o}{\zeta-\alpha-\beta} w(e+x+\beta-\alpha) \geq \lambda_\zeta \sum_{e,x,o} \theta(e,x,o) w(o+x) - \mu_\zeta \sum_{e,x,o} \theta(e,x,o) w(e+x)$. As $\theta(e,x,o) \geq 0$ for all $(e,x,o) \in \mathcal{T}$, it is sufficient to satisfy (9) for each label independently. Observe that (9) is independent of $a$, $a'$, and $G$. As such, this set of constraints serves as a sufficient condition that any $G \in \mathcal{G}_n$ satisfies (5) for all respective $a, a' \in \mathcal{A}$. To find parameters $\lambda_\zeta$ and $\mu_\zeta$ that provide the best $k$-strong price of anarchy guarantee, we formulate the optimization problem $(\mathrm{P}1\zeta)$: $\max_{\lambda_\zeta, \mu_\zeta \geq 0} \frac{\lambda_\zeta}{1+\mu_\zeta}$. We restrict $\lambda_\zeta$ to be non-negative, though this constraint is not active except in degenerate cases. Finally, we transform $(\mathrm{P}1\zeta)$ by substituting new decision variables $\rho = (1+\mu_\zeta)/\lambda_\zeta$ and $\nu = 1/(\binom{n}{\zeta}\lambda_\zeta) \geq 0$. The new objective becomes $1/\rho$. Note that the constraint $(e,x,o) = (1,0,0)$ implies $\rho \geq 0$; we can thus invert the objective and change the minimization to a maximization, giving $(\mathrm{P}\zeta)$.
