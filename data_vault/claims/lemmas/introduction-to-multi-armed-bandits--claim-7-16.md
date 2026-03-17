---
slug: introduction-to-multi-armed-bandits--claim-7-16
label: Claim 7.16
claim_type: lemma
statement: Let $X$ be a random variable uniformly distributed on the interval $[-\frac{1}{\epsilon},
  \frac{1}{\epsilon}]$. We claim that for any $a \in [0, U/d]$ there exists a deterministic
  function $g(X, a)$ of $X$ and $a$ such that $g(X, a)$ and $X + a$ have the same
  marginal distribution, and $\Pr[g(X, a) \neq X] \leq \epsilon U/d$.
proof: Define $g(X, a) = \begin{cases} X & \text{if } X \in [a - \frac{1}{\epsilon},
  \frac{1}{\epsilon}], \\ a - X & \text{if } X \in [-\frac{1}{\epsilon}, a - \frac{1}{\epsilon}).
  \end{cases}$ It is easy to see that $g(X, a)$ is distributed uniformly on $[a -
  \frac{1}{\epsilon}, a + \frac{1}{\epsilon}]$. This is because $a - X$ is distributed
  uniformly on $[\frac{1}{\epsilon}, a + \frac{1}{\epsilon}]$ conditional on $X \in
  [-\frac{1}{\epsilon}, a - \frac{1}{\epsilon})$. Moreover, $\Pr[g(X, a) \neq X] \leq
  \Pr[X \notin [a - \frac{1}{\epsilon}, \frac{1}{\epsilon}]] = \epsilon a/2 \leq \frac{\epsilon
  U}{2d}$.
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/perturbation-distribution]]'
- '[[concepts/perturbation-parameter]]'
about_meta:
- target: '[[concepts/perturbation-distribution]]'
  role: primary
  aspect: ''
- target: '[[concepts/perturbation-parameter]]'
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

# Claim 7.16

Let $X$ be a random variable uniformly distributed on the interval $[-\frac{1}{\epsilon}, \frac{1}{\epsilon}]$. We claim that for any $a \in [0, U/d]$ there exists a deterministic function $g(X, a)$ of $X$ and $a$ such that $g(X, a)$ and $X + a$ have the same marginal distribution, and $\Pr[g(X, a) \neq X] \leq \epsilon U/d$.


## Proof

Define $g(X, a) = \begin{cases} X & \text{if } X \in [a - \frac{1}{\epsilon}, \frac{1}{\epsilon}], \\ a - X & \text{if } X \in [-\frac{1}{\epsilon}, a - \frac{1}{\epsilon}). \end{cases}$ It is easy to see that $g(X, a)$ is distributed uniformly on $[a - \frac{1}{\epsilon}, a + \frac{1}{\epsilon}]$. This is because $a - X$ is distributed uniformly on $[\frac{1}{\epsilon}, a + \frac{1}{\epsilon}]$ conditional on $X \in [-\frac{1}{\epsilon}, a - \frac{1}{\epsilon})$. Moreover, $\Pr[g(X, a) \neq X] \leq \Pr[X \notin [a - \frac{1}{\epsilon}, \frac{1}{\epsilon}]] = \epsilon a/2 \leq \frac{\epsilon U}{2d}$.
