---
slug: introduction-to-multi-armed-bandits--theorem-4-1
label: Theorem 4.1
claim_type: theorem
statement: 'Consider continuum-armed bandits with Lipschitz constant $L$ and time
  horizon $T$. Uniform discretization with algorithm $\mathtt{ALG}$ satisfying (52)
  and discretization step $\epsilon=(TL^{2}/\log T)^{-1/3}$ attains

  $$\operatornamewithlimits{\mathbb{E}}[R(T)]\leq L^{1/3}\cdot T^{2/3}\cdot(1+c_{\mathtt{ALG}})(\log
  T)^{1/3}.$$'
proof: From equation (53), $\operatornamewithlimits{\mathbb{E}}[R(T)]\leq c_{\mathtt{ALG}}\cdot\sqrt{|S|\,T\log
  T}+T\cdot\mathtt{DE}(S)$. For uniform discretization with step $\epsilon$, we have
  $|S|=1/\epsilon$ and $\mathtt{DE}(S)\leq L\epsilon$. Indeed, if $x^{*}$ is a best
  arm on $X$, and $y$ is the closest arm to $x^{*}$ that lies in $S$, it follows that
  $|x^{*}-y|\leq\epsilon$, and therefore $\mu(x^{*})-\mu(y)\leq L\epsilon$. Substituting
  and setting $\epsilon=(TL^{2}/\log T)^{-1/3}$ to approximately equalize the two
  summands yields the stated bound.
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/continuum-armed-bandits]]'
- '[[concepts/lipschitz-constant-l]]'
- '[[concepts/expected-regret-r-t]]'
- '[[concepts/discretization-error-de-s]]'
- '[[concepts/time-horizon-t]]'
- '[[concepts/ucb1-algorithm]]'
about_meta:
- target: '[[concepts/continuum-armed-bandits]]'
  role: primary
  aspect: ''
- target: '[[concepts/lipschitz-constant-l]]'
  role: primary
  aspect: ''
- target: '[[concepts/expected-regret-r-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/discretization-error-de-s]]'
  role: primary
  aspect: ''
- target: '[[concepts/time-horizon-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/ucb1-algorithm]]'
  role: primary
  aspect: ''
depends_on:
- '[[claims/introduction-to-multi-armed-bandits--theorem-1-15]]'
depends_on_meta:
- target: '[[claims/introduction-to-multi-armed-bandits--theorem-1-15]]'
sourced_from:
- '[[sources/1904.07272|Introduction to Multi-Armed Bandits]]'
sourced_from_meta:
- target: '[[sources/1904.07272|Introduction to Multi-Armed Bandits]]'
  section: ''
  page: ''
  confidence: 0.0
---

# Theorem 4.1

Consider continuum-armed bandits with Lipschitz constant $L$ and time horizon $T$. Uniform discretization with algorithm $\mathtt{ALG}$ satisfying (52) and discretization step $\epsilon=(TL^{2}/\log T)^{-1/3}$ attains
$$\operatornamewithlimits{\mathbb{E}}[R(T)]\leq L^{1/3}\cdot T^{2/3}\cdot(1+c_{\mathtt{ALG}})(\log T)^{1/3}.$$


## Proof

From equation (53), $\operatornamewithlimits{\mathbb{E}}[R(T)]\leq c_{\mathtt{ALG}}\cdot\sqrt{|S|\,T\log T}+T\cdot\mathtt{DE}(S)$. For uniform discretization with step $\epsilon$, we have $|S|=1/\epsilon$ and $\mathtt{DE}(S)\leq L\epsilon$. Indeed, if $x^{*}$ is a best arm on $X$, and $y$ is the closest arm to $x^{*}$ that lies in $S$, it follows that $|x^{*}-y|\leq\epsilon$, and therefore $\mu(x^{*})-\mu(y)\leq L\epsilon$. Substituting and setting $\epsilon=(TL^{2}/\log T)^{-1/3}$ to approximately equalize the two summands yields the stated bound.
