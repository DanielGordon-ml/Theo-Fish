---
slug: k-strong-price-of-anarchy--theorem-iii-3
label: Theorem III.3
claim_type: theorem
statement: 'The $k$-strong price of anarchy $\operatorname{SPoA}_k(\mathcal{G}_n,
  w)$ over the class of resource allocation games $\mathcal{G}_n$ with welfare function
  $w$ equals $1/Q^\star$, where $Q^\star$ is the value of the linear program (D):
  $\max_{\theta \in \mathbb{R}_{\geq 0}^{|\mathcal{T}|}} \sum_{e,x,o} w(o+x) \theta(e,x,o)$
  subject to $\sum_{e,x,o} \left(\binom{n}{\zeta} w(e+x) - \sum_{\substack{0 \leq
  \alpha \leq e \\ 0 \leq \beta \leq o \\ \alpha+\beta \leq \zeta}} \binom{e}{\alpha}\binom{o}{\beta}\binom{n-e-o}{\zeta-\alpha-\beta}
  w(e+x+\beta-\alpha)\right) \theta(e,x,o) \geq 0$, $\forall \zeta \in [k]$, and $\sum_{e,x,o}
  w(e+x) \theta(e,x,o) = 1$. Equivalently, $\operatorname{SPoA}_k(\mathcal{G}_n, w)
  = 1/\rho^\star$ where $\rho^\star$ is the value of the dual linear program $(\mathrm{P}[k])$.'
proof: 'The proof can be outlined in four parts: first, the problem of finding $\operatorname{SPoA}_k(\mathcal{G}_n,
  w)$ is transformed and relaxed; second, the parameterization used in the proof of
  Proposition III.2 is used to turn the relaxed problem into a linear program. Next,
  an example is constructed to show the linear program provides a tight bound. Finally,
  we take the dual of said linear program.


  1) Relaxing the problem: Quantifying $\operatorname{SPoA}_k(\mathcal{G}_n, w)$ can
  be expressed as taking the minimum $k$-strong price of anarchy over all games in
  $\mathcal{G}_n$, i.e., $\min_{G \in \mathcal{G}_n} \frac{\min_{a^{k\mathrm{SNE}}
  \in k\mathrm{SNE}(G)} W(a^{k\mathrm{SNE}})}{\max_{a^{\mathrm{opt}} \in \mathcal{A}}
  W(a^{\mathrm{opt}})}$. To make this problem more approachable, we introduce several
  transformations and relaxations. First, rather than searching over the entire set
  of games $\mathcal{G}_n$, we search over the set of games $\hat{\mathcal{G}}_n$,
  in which each agent has exactly two actions. This reduction of the search space
  can be done without loss of generality, i.e., $\mathrm{SPoA}_k(\bar{\mathcal{G}}_n,
  w) = \mathrm{SPoA}_k(\hat{\mathcal{G}}_n, w)$. Trivially, $\hat{\mathcal{G}}_n \subset
  \bar{\mathcal{G}}_n$. Further, consider any game $G \in \mathcal{G}_n$; if for every
  player, each of their actions is removed except their action in the optimal allocation
  $a_i^{\mathrm{opt}}$ and their action in their worst $k$-strong Nash equilibrium
  $a_i^{k\mathrm{SNE}}$, the new problem will maintain the same $k$-strong price of
  anarchy, but will now exist in $\hat{\mathcal{G}}_n$. With this reduction, we will
  denote each player''s action set as $\hat{\mathcal{A}}_i = \{a_i^{\mathrm{opt}},
  a_i^{k\mathrm{SNE}}\}$. Second, we normalize each resource value $v_r$ such that
  the equilibrium welfare is one. Third, we invert the objective and consider the
  maximization of $W(a^{\mathrm{opt}})/W(a^{k\mathrm{SNE}})$. Finally, we sum over
  each of the $k$-coalition equilibrium constraints. For each $\zeta \in [k]$, rather
  than satisfying each inequality in (3), sum over every combination of the $\zeta$
  out of $n$ players, denoted $\mathcal{C}_\zeta$. Applying these reductions to (D1)
  gives (D2).


  2) Parameterization: We use the parameterization introduced in the proof of Proposition
  III.2 with respect to the joint actions $a = a^{k\mathrm{SNE}}$ and $a'' = a^{\mathrm{opt}}$.
  By considering any $\theta \in \mathbb{R}_{\geq 0}^{|\mathcal{T}|}$, we can parameterize
  any game $G \in \hat{\mathcal{G}}_n$; to find the worst-case price of anarchy, we
  search over all such parameters, i.e., look over the entire class of games. The
  linear program (D) is the result of the search for the vector $\theta$ that results
  in the highest price of anarchy.


  3) Constructing an example: Consider the following resource allocation problem:
  for each label $(e,x,o) \in \mathcal{T}$ and permutation $\sigma \in \Sigma_n$,
  define $nn!|\mathcal{T}|$ resources. Let $r_{i,j}^{(e,x,o)}$ denote resource $(e,x,o)$
  at position $i$ in ring $j$. For each ring with label $(e,x,o)$ and permutation
  $\sigma$, player $i$ has the actions $a_i^{k\mathrm{SNE}} = \{r_{\sigma(i),j}^{(e,x,o)},
  \ldots, r_{\sigma(i)+e+x-1 \% n, j}^{(e,x,o)}\}$ and $a_i^{\mathrm{opt}} = \{r_{\sigma(i)+e
  \% n, j}^{(e,x,o)}, \ldots, r_{\sigma(i)+e+x+o-1 \% n, j}^{(e,x,o)}\}$. Each resource
  of type $(e,x,o)$ has value $\theta(e,x,o)$. In the joint action $a^{k\mathrm{SNE}}$,
  the system welfare is $W(a^{k\mathrm{SNE}}) = \sum_{e,x,o} nn! \theta(e,x,o) w(e+x)$.
  Similarly, $W(a^{\mathrm{opt}}) = \sum_{e,x,o} nn! \theta(e,x,o) w(o+x)$. The coalition
  deviation welfare is $W(a_\Gamma^{\mathrm{opt}}, a_{-\Gamma}^{k\mathrm{SNE}}) =
  \sum_{e,x,o} \theta(e,x,o) \sum_{\substack{0 \leq \alpha \leq e \\ 0 \leq \beta
  \leq o \\ \alpha+\beta \leq \zeta}} nn! \binom{e}{\alpha}\binom{o}{\beta}\binom{n-e-o}{\zeta-\alpha-\beta}
  w(e+x+\beta-\alpha)$. Verifying $a^{k\mathrm{SNE}}$ is a $k$-strong Nash equilibrium
  holds whenever $\theta$ is feasible in (D). Accordingly, $\frac{1}{Q^\star} \leq
  \mathrm{SPoA}_k(\mathcal{G}_n, w) \leq \frac{1}{\sum_{e,x,o} \theta(e,x,o) w(o+x)}$.
  Letting $\theta$ take on the solution to (D) shows the bound is tight.


  4) Taking the Dual: The primal is feasible (consider $\theta(1,0,0) = 1/w(1)$ and
  zero otherwise). The feasible set is compact because from the equality constraint,
  $1 \geq \min_{y>0} w(y) \sum_{\substack{e,x,o \\ e+x>0}} \theta(e,x,o)$, and since
  $w(y) > 0$ for $y > 0$, each $\theta(e,x,o)$ with $e+x > 0$ is bounded. For $\theta(0,0,o)$,
  the equilibrium constraint at $\zeta=1$ gives $L \geq w(1) \sum_{o \in [n]} o\theta(0,0,o)$.
  The dual program is $\min_{\rho, \{\nu_\zeta \geq 0\}_{\zeta \in [k]}} \rho$ subject
  to $b^\top - \rho d^\top + \sum_{\zeta \in [k]} \nu_\zeta c_\zeta \leq 0$. From
  strong duality, (P1) provides the same value as (D). Expanding terms shows (P1)
  is equivalent to $(\mathrm{P}[k])$.'
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/common-interest-game]]'
- '[[concepts/linear-program-d]]'
- '[[concepts/resource-allocation-games]]'
- '[[concepts/modulo-operator]]'
- '[[concepts/system-welfare-function-w]]'
- '[[concepts/lambda-mu-k-coalitionally-smooth-game]]'
- '[[concepts/k-strong-price-of-anarchy]]'
- '[[concepts/class-of-resource-allocation-problems]]'
- '[[concepts/linear-program]]'
- '[[concepts/k-strong-nash-equilibrium]]'
- '[[concepts/dual-linear-program-p1]]'
- '[[concepts/set-of-games-g-n]]'
- '[[concepts/label-parameter]]'
- '[[concepts/label-parameter-vector]]'
- '[[concepts/linear-program-d]]'
- '[[concepts/resource-allocation-games]]'
- '[[concepts/system-welfare-function-w]]'
- '[[concepts/class-of-resource-allocation-problems]]'
- '[[concepts/set-of-games-g-n]]'
- '[[concepts/modulo-operator]]'
- '[[concepts/k-strong-nash-equilibrium]]'
- '[[concepts/common-interest-game]]'
- '[[concepts/linear-program]]'
- '[[concepts/label-parameter-vector]]'
- '[[concepts/label-parameter]]'
- '[[concepts/k-strong-price-of-anarchy]]'
- '[[concepts/dual-linear-program-p1]]'
- '[[concepts/lambda-mu-k-coalitionally-smooth-game]]'
- '[[concepts/k-strong-price-of-anarchy]]'
- '[[concepts/set-of-games-g-n]]'
- '[[concepts/k-strong-nash-equilibrium]]'
- '[[concepts/linear-program-d]]'
- '[[concepts/system-welfare-function-w]]'
- '[[concepts/modulo-operator]]'
- '[[concepts/dual-linear-program-p1]]'
- '[[concepts/label-parameter-vector]]'
- '[[concepts/class-of-resource-allocation-problems]]'
- '[[concepts/label-parameter]]'
- '[[concepts/common-interest-game]]'
- '[[concepts/linear-program]]'
- '[[concepts/lambda-mu-k-coalitionally-smooth-game]]'
- '[[concepts/resource-allocation-games]]'
- '[[concepts/class-of-resource-allocation-problems]]'
- '[[concepts/system-welfare-function-w]]'
- '[[concepts/resource-allocation-games]]'
- '[[concepts/common-interest-game]]'
- '[[concepts/label-parameter-vector]]'
- '[[concepts/set-of-games-g-n]]'
- '[[concepts/dual-linear-program-p1]]'
- '[[concepts/lambda-mu-k-coalitionally-smooth-game]]'
- '[[concepts/linear-program]]'
- '[[concepts/modulo-operator]]'
- '[[concepts/k-strong-nash-equilibrium]]'
- '[[concepts/k-strong-price-of-anarchy]]'
- '[[concepts/label-parameter]]'
- '[[concepts/linear-program-d]]'
about_meta:
- target: '[[concepts/common-interest-game]]'
  role: primary
  aspect: ''
- target: '[[concepts/linear-program-d]]'
  role: primary
  aspect: ''
- target: '[[concepts/resource-allocation-games]]'
  role: primary
  aspect: ''
- target: '[[concepts/modulo-operator]]'
  role: primary
  aspect: ''
- target: '[[concepts/system-welfare-function-w]]'
  role: primary
  aspect: ''
- target: '[[concepts/lambda-mu-k-coalitionally-smooth-game]]'
  role: primary
  aspect: ''
- target: '[[concepts/k-strong-price-of-anarchy]]'
  role: primary
  aspect: ''
- target: '[[concepts/class-of-resource-allocation-problems]]'
  role: primary
  aspect: ''
- target: '[[concepts/linear-program]]'
  role: primary
  aspect: ''
- target: '[[concepts/k-strong-nash-equilibrium]]'
  role: primary
  aspect: ''
- target: '[[concepts/dual-linear-program-p1]]'
  role: primary
  aspect: ''
- target: '[[concepts/set-of-games-g-n]]'
  role: primary
  aspect: ''
- target: '[[concepts/label-parameter]]'
  role: primary
  aspect: ''
- target: '[[concepts/label-parameter-vector]]'
  role: primary
  aspect: ''
- target: '[[concepts/linear-program-d]]'
  role: primary
  aspect: ''
- target: '[[concepts/resource-allocation-games]]'
  role: primary
  aspect: ''
- target: '[[concepts/system-welfare-function-w]]'
  role: primary
  aspect: ''
- target: '[[concepts/class-of-resource-allocation-problems]]'
  role: primary
  aspect: ''
- target: '[[concepts/set-of-games-g-n]]'
  role: primary
  aspect: ''
- target: '[[concepts/modulo-operator]]'
  role: primary
  aspect: ''
- target: '[[concepts/k-strong-nash-equilibrium]]'
  role: primary
  aspect: ''
- target: '[[concepts/common-interest-game]]'
  role: primary
  aspect: ''
- target: '[[concepts/linear-program]]'
  role: primary
  aspect: ''
- target: '[[concepts/label-parameter-vector]]'
  role: primary
  aspect: ''
- target: '[[concepts/label-parameter]]'
  role: primary
  aspect: ''
- target: '[[concepts/k-strong-price-of-anarchy]]'
  role: primary
  aspect: ''
- target: '[[concepts/dual-linear-program-p1]]'
  role: primary
  aspect: ''
- target: '[[concepts/lambda-mu-k-coalitionally-smooth-game]]'
  role: primary
  aspect: ''
- target: '[[concepts/k-strong-price-of-anarchy]]'
  role: primary
  aspect: ''
- target: '[[concepts/set-of-games-g-n]]'
  role: primary
  aspect: ''
- target: '[[concepts/k-strong-nash-equilibrium]]'
  role: primary
  aspect: ''
- target: '[[concepts/linear-program-d]]'
  role: primary
  aspect: ''
- target: '[[concepts/system-welfare-function-w]]'
  role: primary
  aspect: ''
- target: '[[concepts/modulo-operator]]'
  role: primary
  aspect: ''
- target: '[[concepts/dual-linear-program-p1]]'
  role: primary
  aspect: ''
- target: '[[concepts/label-parameter-vector]]'
  role: primary
  aspect: ''
- target: '[[concepts/class-of-resource-allocation-problems]]'
  role: primary
  aspect: ''
- target: '[[concepts/label-parameter]]'
  role: primary
  aspect: ''
- target: '[[concepts/common-interest-game]]'
  role: primary
  aspect: ''
- target: '[[concepts/linear-program]]'
  role: primary
  aspect: ''
- target: '[[concepts/lambda-mu-k-coalitionally-smooth-game]]'
  role: primary
  aspect: ''
- target: '[[concepts/resource-allocation-games]]'
  role: primary
  aspect: ''
- target: '[[concepts/class-of-resource-allocation-problems]]'
  role: primary
  aspect: ''
- target: '[[concepts/system-welfare-function-w]]'
  role: primary
  aspect: ''
- target: '[[concepts/resource-allocation-games]]'
  role: primary
  aspect: ''
- target: '[[concepts/common-interest-game]]'
  role: primary
  aspect: ''
- target: '[[concepts/label-parameter-vector]]'
  role: primary
  aspect: ''
- target: '[[concepts/set-of-games-g-n]]'
  role: primary
  aspect: ''
- target: '[[concepts/dual-linear-program-p1]]'
  role: primary
  aspect: ''
- target: '[[concepts/lambda-mu-k-coalitionally-smooth-game]]'
  role: primary
  aspect: ''
- target: '[[concepts/linear-program]]'
  role: primary
  aspect: ''
- target: '[[concepts/modulo-operator]]'
  role: primary
  aspect: ''
- target: '[[concepts/k-strong-nash-equilibrium]]'
  role: primary
  aspect: ''
- target: '[[concepts/k-strong-price-of-anarchy]]'
  role: primary
  aspect: ''
- target: '[[concepts/label-parameter]]'
  role: primary
  aspect: ''
- target: '[[concepts/linear-program-d]]'
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

# Theorem III.3

The $k$-strong price of anarchy $\operatorname{SPoA}_k(\mathcal{G}_n, w)$ over the class of resource allocation games $\mathcal{G}_n$ with welfare function $w$ equals $1/Q^\star$, where $Q^\star$ is the value of the linear program (D): $\max_{\theta \in \mathbb{R}_{\geq 0}^{|\mathcal{T}|}} \sum_{e,x,o} w(o+x) \theta(e,x,o)$ subject to $\sum_{e,x,o} \left(\binom{n}{\zeta} w(e+x) - \sum_{\substack{0 \leq \alpha \leq e \\ 0 \leq \beta \leq o \\ \alpha+\beta \leq \zeta}} \binom{e}{\alpha}\binom{o}{\beta}\binom{n-e-o}{\zeta-\alpha-\beta} w(e+x+\beta-\alpha)\right) \theta(e,x,o) \geq 0$, $\forall \zeta \in [k]$, and $\sum_{e,x,o} w(e+x) \theta(e,x,o) = 1$. Equivalently, $\operatorname{SPoA}_k(\mathcal{G}_n, w) = 1/\rho^\star$ where $\rho^\star$ is the value of the dual linear program $(\mathrm{P}[k])$.


## Proof

The proof can be outlined in four parts: first, the problem of finding $\operatorname{SPoA}_k(\mathcal{G}_n, w)$ is transformed and relaxed; second, the parameterization used in the proof of Proposition III.2 is used to turn the relaxed problem into a linear program. Next, an example is constructed to show the linear program provides a tight bound. Finally, we take the dual of said linear program.

1) Relaxing the problem: Quantifying $\operatorname{SPoA}_k(\mathcal{G}_n, w)$ can be expressed as taking the minimum $k$-strong price of anarchy over all games in $\mathcal{G}_n$, i.e., $\min_{G \in \mathcal{G}_n} \frac{\min_{a^{k\mathrm{SNE}} \in k\mathrm{SNE}(G)} W(a^{k\mathrm{SNE}})}{\max_{a^{\mathrm{opt}} \in \mathcal{A}} W(a^{\mathrm{opt}})}$. To make this problem more approachable, we introduce several transformations and relaxations. First, rather than searching over the entire set of games $\mathcal{G}_n$, we search over the set of games $\hat{\mathcal{G}}_n$, in which each agent has exactly two actions. This reduction of the search space can be done without loss of generality, i.e., $\mathrm{SPoA}_k(\bar{\mathcal{G}}_n, w) = \mathrm{SPoA}_k(\hat{\mathcal{G}}_n, w)$. Trivially, $\hat{\mathcal{G}}_n \subset \bar{\mathcal{G}}_n$. Further, consider any game $G \in \mathcal{G}_n$; if for every player, each of their actions is removed except their action in the optimal allocation $a_i^{\mathrm{opt}}$ and their action in their worst $k$-strong Nash equilibrium $a_i^{k\mathrm{SNE}}$, the new problem will maintain the same $k$-strong price of anarchy, but will now exist in $\hat{\mathcal{G}}_n$. With this reduction, we will denote each player's action set as $\hat{\mathcal{A}}_i = \{a_i^{\mathrm{opt}}, a_i^{k\mathrm{SNE}}\}$. Second, we normalize each resource value $v_r$ such that the equilibrium welfare is one. Third, we invert the objective and consider the maximization of $W(a^{\mathrm{opt}})/W(a^{k\mathrm{SNE}})$. Finally, we sum over each of the $k$-coalition equilibrium constraints. For each $\zeta \in [k]$, rather than satisfying each inequality in (3), sum over every combination of the $\zeta$ out of $n$ players, denoted $\mathcal{C}_\zeta$. Applying these reductions to (D1) gives (D2).

2) Parameterization: We use the parameterization introduced in the proof of Proposition III.2 with respect to the joint actions $a = a^{k\mathrm{SNE}}$ and $a' = a^{\mathrm{opt}}$. By considering any $\theta \in \mathbb{R}_{\geq 0}^{|\mathcal{T}|}$, we can parameterize any game $G \in \hat{\mathcal{G}}_n$; to find the worst-case price of anarchy, we search over all such parameters, i.e., look over the entire class of games. The linear program (D) is the result of the search for the vector $\theta$ that results in the highest price of anarchy.

3) Constructing an example: Consider the following resource allocation problem: for each label $(e,x,o) \in \mathcal{T}$ and permutation $\sigma \in \Sigma_n$, define $nn!|\mathcal{T}|$ resources. Let $r_{i,j}^{(e,x,o)}$ denote resource $(e,x,o)$ at position $i$ in ring $j$. For each ring with label $(e,x,o)$ and permutation $\sigma$, player $i$ has the actions $a_i^{k\mathrm{SNE}} = \{r_{\sigma(i),j}^{(e,x,o)}, \ldots, r_{\sigma(i)+e+x-1 \% n, j}^{(e,x,o)}\}$ and $a_i^{\mathrm{opt}} = \{r_{\sigma(i)+e \% n, j}^{(e,x,o)}, \ldots, r_{\sigma(i)+e+x+o-1 \% n, j}^{(e,x,o)}\}$. Each resource of type $(e,x,o)$ has value $\theta(e,x,o)$. In the joint action $a^{k\mathrm{SNE}}$, the system welfare is $W(a^{k\mathrm{SNE}}) = \sum_{e,x,o} nn! \theta(e,x,o) w(e+x)$. Similarly, $W(a^{\mathrm{opt}}) = \sum_{e,x,o} nn! \theta(e,x,o) w(o+x)$. The coalition deviation welfare is $W(a_\Gamma^{\mathrm{opt}}, a_{-\Gamma}^{k\mathrm{SNE}}) = \sum_{e,x,o} \theta(e,x,o) \sum_{\substack{0 \leq \alpha \leq e \\ 0 \leq \beta \leq o \\ \alpha+\beta \leq \zeta}} nn! \binom{e}{\alpha}\binom{o}{\beta}\binom{n-e-o}{\zeta-\alpha-\beta} w(e+x+\beta-\alpha)$. Verifying $a^{k\mathrm{SNE}}$ is a $k$-strong Nash equilibrium holds whenever $\theta$ is feasible in (D). Accordingly, $\frac{1}{Q^\star} \leq \mathrm{SPoA}_k(\mathcal{G}_n, w) \leq \frac{1}{\sum_{e,x,o} \theta(e,x,o) w(o+x)}$. Letting $\theta$ take on the solution to (D) shows the bound is tight.

4) Taking the Dual: The primal is feasible (consider $\theta(1,0,0) = 1/w(1)$ and zero otherwise). The feasible set is compact because from the equality constraint, $1 \geq \min_{y>0} w(y) \sum_{\substack{e,x,o \\ e+x>0}} \theta(e,x,o)$, and since $w(y) > 0$ for $y > 0$, each $\theta(e,x,o)$ with $e+x > 0$ is bounded. For $\theta(0,0,o)$, the equilibrium constraint at $\zeta=1$ gives $L \geq w(1) \sum_{o \in [n]} o\theta(0,0,o)$. The dual program is $\min_{\rho, \{\nu_\zeta \geq 0\}_{\zeta \in [k]}} \rho$ subject to $b^\top - \rho d^\top + \sum_{\zeta \in [k]} \nu_\zeta c_\zeta \leq 0$. From strong duality, (P1) provides the same value as (D). Expanding terms shows (P1) is equivalent to $(\mathrm{P}[k])$.
