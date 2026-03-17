---
slug: introduction-to-multi-armed-bandits--theorem-4-2
label: Theorem 4.2
claim_type: theorem
statement: 'Let $\mathtt{ALG}$ be any algorithm for continuum-armed bandits with time
  horizon $T$ and Lipschitz constant $L$. There exists a problem instance $\mathcal{I}=\mathcal{I}(x^{*},\epsilon)$,
  for some $x^{*}\in[0,1]$ and $\epsilon>0$, such that

  $$\operatornamewithlimits{\mathbb{E}}\left[\,R(T)\mid\mathcal{I}\,\right]\geq\Omega\left(\,L^{1/3}\cdot
  T^{2/3}\,\right).$$'
proof: 'For simplicity of exposition, assume the Lipschitz constant is $L=1$; arbitrary
  $L$ is treated similarly.


  Fix $K\in\mathbb{N}$ and partition arms into $K$ disjoint intervals of length $\tfrac{1}{K}$.
  Use bump functions with $\epsilon=\tfrac{1}{2K}$ such that each interval either
  contains a bump or is completely flat. More formally, we use problem instances $\mathcal{I}(x^{*},\epsilon)$
  indexed by $a^{*}\in[K]:=\{1,\ldots,K\}$, where the best arm is $x^{*}=(2\epsilon-1)\cdot
  a^{*}+\epsilon$.


  We use problem instances $\mathcal{J}(a^{*},\epsilon)$ from $\mathtt{MainLB}$, with
  $K$ arms and the same time horizon $T$. The set of arms in these instances is denoted
  $[K]$. Each instance $\mathcal{J}=\mathcal{J}(a^{*},\epsilon)$ corresponds to an
  instance $\mathcal{I}=\mathcal{I}(x^{*},\epsilon)$ of CAB with $x^{*}=f(a^{*})$.
  In particular, each arm $a\in[K]$ in $\mathcal{J}$ corresponds to an arm $x=f(a)$
  in $\mathcal{I}$. We view $\mathcal{J}$ as a discrete version of $\mathcal{I}$.
  In particular, we have $\mu_{\mathcal{J}}(a)=\mu(f(a))$, where $\mu(\cdot)$ is the
  reward function for $\mathcal{I}$, and $\mu_{\mathcal{J}}(\cdot)$ is the reward
  function for $\mathcal{J}$.


  Consider an execution of $\mathtt{ALG}$ on problem instance $\mathcal{I}$ of CAB,
  and use it to construct an algorithm $\mathtt{ALG}^{\prime}$ which solves an instance
  $\mathcal{J}$ of $K$-armed bandits. Each round in algorithm $\mathtt{ALG}^{\prime}$
  proceeds as follows. $\mathtt{ALG}$ is called and returns some arm $x\in[0,1]$.
  This arm falls into the interval $[f(a)-\epsilon, f(a)+\epsilon)$ for some $a\in[K]$.
  Then algorithm $\mathtt{ALG}^{\prime}$ chooses arm $a$. When $\mathtt{ALG}^{\prime}$
  receives reward $r$, it uses $r$ and $x$ to compute reward $r_{x}\in\{0,1\}$ such
  that $\operatornamewithlimits{\mathbb{E}}[r_{x}\mid x]=\mu(x)$, and feed it back
  to $\mathtt{ALG}$. We define $r_{x}$ as follows:

  $$r_{x}=\begin{cases}r&\text{with probability $p_{x}\in[0,1]$}\\ X&\text{otherwise},\end{cases}$$

  where $X$ is an independent toss of a Bernoulli random variable with expectation
  $\tfrac{1}{2}$, and we set $p_{x}=1-|x-f(a)|/\epsilon$ so as to match the definition
  of $\mathcal{I}(x^{*},\epsilon)$ in Eq. (54). Then

  $$\operatornamewithlimits{\mathbb{E}}[r_{x}\mid x]=p_{x}\cdot\mu_{\mathcal{J}}(a)+(1-p_{x})\cdot\tfrac{1}{2}=\tfrac{1}{2}+(\mu_{\mathcal{J}}(a)-\tfrac{1}{2})\cdot
  p_{x}=\mu(x).$$


  For each round $t$, let $x_{t}$ and $a_{t}$ be the arms chosen by $\mathtt{ALG}$
  and $\mathtt{ALG}^{\prime}$, resp. Since $\mu_{\mathcal{J}}(a_{t})\geq\tfrac{1}{2}$,
  we have $\mu(x_{t})\leq\mu_{\mathcal{J}}(a_{t})$. It follows that the total expected
  reward of $\mathtt{ALG}$ on instance $\mathcal{I}$ cannot exceed that of $\mathtt{ALG}^{\prime}$
  on instance $\mathcal{J}$. Since the best arms in both problem instances have the
  same expected rewards $\tfrac{1}{2}+\epsilon$, it follows that

  $$\operatornamewithlimits{\mathbb{E}}[R(T)\mid\mathcal{I}]\geq\operatornamewithlimits{\mathbb{E}}[R^{\prime}(T)\mid\mathcal{J}],$$

  where $R(T)$ and $R^{\prime}(T)$ denote regret of $\mathtt{ALG}$ and $\mathtt{ALG}^{\prime}$,
  respectively.


  Recall that algorithm $\mathtt{ALG}^{\prime}$ can solve any $K$-armed bandits instance
  of the form $\mathcal{J}=\mathcal{J}(a^{*},\epsilon)$. Let us apply Theorem 4.3
  to derive a lower bound on the regret of $\mathtt{ALG}^{\prime}$. Specifically,
  let us fix $K=(T/4c)^{1/3}$, so as to ensure that $\epsilon\leq\sqrt{cK/T}$, as
  required in Theorem 4.3. Then for some instance $\mathcal{J}=\mathcal{J}(a^{*},\epsilon)$,

  $$\operatornamewithlimits{\mathbb{E}}[R^{\prime}(T)\mid\mathcal{J}]\geq\Omega(\sqrt{\epsilon
  T})=\Omega(T^{2/3}).$$

  Thus, taking the corresponding instance $\mathcal{I}$ of CAB, we conclude that $\operatornamewithlimits{\mathbb{E}}[R(T)\mid\mathcal{I}]\geq\Omega(T^{2/3})$.
  ∎'
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/lower-bound-on-regret]]'
- '[[concepts/bump-function-mu]]'
- '[[concepts/time-horizon-t]]'
- '[[concepts/continuum-armed-bandits]]'
- '[[concepts/lipschitz-constant-l]]'
- '[[concepts/problem-instance-i-x-epsilon]]'
- '[[concepts/regret-r-t]]'
about_meta:
- target: '[[concepts/lower-bound-on-regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/bump-function-mu]]'
  role: primary
  aspect: ''
- target: '[[concepts/time-horizon-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/continuum-armed-bandits]]'
  role: primary
  aspect: ''
- target: '[[concepts/lipschitz-constant-l]]'
  role: primary
  aspect: ''
- target: '[[concepts/problem-instance-i-x-epsilon]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret-r-t]]'
  role: primary
  aspect: ''
depends_on: []
depends_on_meta: []
sourced_from:
- '[[sources/1904.07272|Introduction to Multi-Armed Bandits]]'
sourced_from_meta:
- target: '[[sources/1904.07272|Introduction to Multi-Armed Bandits]]'
  section: ''
  page: ''
  confidence: 0.0
---

# Theorem 4.2

Let $\mathtt{ALG}$ be any algorithm for continuum-armed bandits with time horizon $T$ and Lipschitz constant $L$. There exists a problem instance $\mathcal{I}=\mathcal{I}(x^{*},\epsilon)$, for some $x^{*}\in[0,1]$ and $\epsilon>0$, such that
$$\operatornamewithlimits{\mathbb{E}}\left[\,R(T)\mid\mathcal{I}\,\right]\geq\Omega\left(\,L^{1/3}\cdot T^{2/3}\,\right).$$


## Proof

For simplicity of exposition, assume the Lipschitz constant is $L=1$; arbitrary $L$ is treated similarly.

Fix $K\in\mathbb{N}$ and partition arms into $K$ disjoint intervals of length $\tfrac{1}{K}$. Use bump functions with $\epsilon=\tfrac{1}{2K}$ such that each interval either contains a bump or is completely flat. More formally, we use problem instances $\mathcal{I}(x^{*},\epsilon)$ indexed by $a^{*}\in[K]:=\{1,\ldots,K\}$, where the best arm is $x^{*}=(2\epsilon-1)\cdot a^{*}+\epsilon$.

We use problem instances $\mathcal{J}(a^{*},\epsilon)$ from $\mathtt{MainLB}$, with $K$ arms and the same time horizon $T$. The set of arms in these instances is denoted $[K]$. Each instance $\mathcal{J}=\mathcal{J}(a^{*},\epsilon)$ corresponds to an instance $\mathcal{I}=\mathcal{I}(x^{*},\epsilon)$ of CAB with $x^{*}=f(a^{*})$. In particular, each arm $a\in[K]$ in $\mathcal{J}$ corresponds to an arm $x=f(a)$ in $\mathcal{I}$. We view $\mathcal{J}$ as a discrete version of $\mathcal{I}$. In particular, we have $\mu_{\mathcal{J}}(a)=\mu(f(a))$, where $\mu(\cdot)$ is the reward function for $\mathcal{I}$, and $\mu_{\mathcal{J}}(\cdot)$ is the reward function for $\mathcal{J}$.

Consider an execution of $\mathtt{ALG}$ on problem instance $\mathcal{I}$ of CAB, and use it to construct an algorithm $\mathtt{ALG}^{\prime}$ which solves an instance $\mathcal{J}$ of $K$-armed bandits. Each round in algorithm $\mathtt{ALG}^{\prime}$ proceeds as follows. $\mathtt{ALG}$ is called and returns some arm $x\in[0,1]$. This arm falls into the interval $[f(a)-\epsilon, f(a)+\epsilon)$ for some $a\in[K]$. Then algorithm $\mathtt{ALG}^{\prime}$ chooses arm $a$. When $\mathtt{ALG}^{\prime}$ receives reward $r$, it uses $r$ and $x$ to compute reward $r_{x}\in\{0,1\}$ such that $\operatornamewithlimits{\mathbb{E}}[r_{x}\mid x]=\mu(x)$, and feed it back to $\mathtt{ALG}$. We define $r_{x}$ as follows:
$$r_{x}=\begin{cases}r&\text{with probability $p_{x}\in[0,1]$}\\ X&\text{otherwise},\end{cases}$$
where $X$ is an independent toss of a Bernoulli random variable with expectation $\tfrac{1}{2}$, and we set $p_{x}=1-|x-f(a)|/\epsilon$ so as to match the definition of $\mathcal{I}(x^{*},\epsilon)$ in Eq. (54). Then
$$\operatornamewithlimits{\mathbb{E}}[r_{x}\mid x]=p_{x}\cdot\mu_{\mathcal{J}}(a)+(1-p_{x})\cdot\tfrac{1}{2}=\tfrac{1}{2}+(\mu_{\mathcal{J}}(a)-\tfrac{1}{2})\cdot p_{x}=\mu(x).$$

For each round $t$, let $x_{t}$ and $a_{t}$ be the arms chosen by $\mathtt{ALG}$ and $\mathtt{ALG}^{\prime}$, resp. Since $\mu_{\mathcal{J}}(a_{t})\geq\tfrac{1}{2}$, we have $\mu(x_{t})\leq\mu_{\mathcal{J}}(a_{t})$. It follows that the total expected reward of $\mathtt{ALG}$ on instance $\mathcal{I}$ cannot exceed that of $\mathtt{ALG}^{\prime}$ on instance $\mathcal{J}$. Since the best arms in both problem instances have the same expected rewards $\tfrac{1}{2}+\epsilon$, it follows that
$$\operatornamewithlimits{\mathbb{E}}[R(T)\mid\mathcal{I}]\geq\operatornamewithlimits{\mathbb{E}}[R^{\prime}(T)\mid\mathcal{J}],$$
where $R(T)$ and $R^{\prime}(T)$ denote regret of $\mathtt{ALG}$ and $\mathtt{ALG}^{\prime}$, respectively.

Recall that algorithm $\mathtt{ALG}^{\prime}$ can solve any $K$-armed bandits instance of the form $\mathcal{J}=\mathcal{J}(a^{*},\epsilon)$. Let us apply Theorem 4.3 to derive a lower bound on the regret of $\mathtt{ALG}^{\prime}$. Specifically, let us fix $K=(T/4c)^{1/3}$, so as to ensure that $\epsilon\leq\sqrt{cK/T}$, as required in Theorem 4.3. Then for some instance $\mathcal{J}=\mathcal{J}(a^{*},\epsilon)$,
$$\operatornamewithlimits{\mathbb{E}}[R^{\prime}(T)\mid\mathcal{J}]\geq\Omega(\sqrt{\epsilon T})=\Omega(T^{2/3}).$$
Thus, taking the corresponding instance $\mathcal{I}$ of CAB, we conclude that $\operatornamewithlimits{\mathbb{E}}[R(T)\mid\mathcal{I}]\geq\Omega(T^{2/3})$. ∎
