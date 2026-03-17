---
slug: introduction-to-multi-armed-bandits--theorem-2-1
label: Theorem 2.1
claim_type: theorem
statement: Fix time horizon $T$ and the number of arms $K$. For any bandit algorithm,
  there exists a problem instance such that $\operatorname{\mathbb{E}}[R(T)]\geq\Omega(\sqrt{KT})$.
proof: 'On a very high level, the proof proceeds as follows. We consider 0-1 rewards
  and the following family of problem instances, with parameter $\epsilon>0$ to be
  adjusted in the analysis: $\mathcal{I}_{j}$ where $\mu_{i}=\frac{1}{2}+\frac{\epsilon}{2}$
  for arm $i=j$ and $\mu_{i}=\frac{1}{2}$ for each arm $i\neq j$, for each $j=1,2,\ldots,K$.
  We prove that sampling each arm $\Omega(1/\epsilon^{2})$ times is necessary to determine
  whether this arm is good or bad. This leads to regret $\Omega(K/\epsilon)$. We complete
  the proof by plugging in $\epsilon=\Theta(\sqrt{K/T})$. (Full technical details
  are presented in subsequent steps.)'
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/stochastic-bandits-problem]]'
- '[[concepts/lower-bound-on-regret]]'
- '[[concepts/family-of-problem-instances]]'
- '[[concepts/number-of-arms-k]]'
- '[[concepts/time-horizon-t]]'
- '[[concepts/0-1-rewards]]'
- '[[concepts/regret-bound]]'
- '[[concepts/expected-regret-e-r-t]]'
about_meta:
- target: '[[concepts/stochastic-bandits-problem]]'
  role: primary
  aspect: ''
- target: '[[concepts/lower-bound-on-regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/family-of-problem-instances]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-arms-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/time-horizon-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/0-1-rewards]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret-bound]]'
  role: primary
  aspect: ''
- target: '[[concepts/expected-regret-e-r-t]]'
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

# Theorem 2.1

Fix time horizon $T$ and the number of arms $K$. For any bandit algorithm, there exists a problem instance such that $\operatorname{\mathbb{E}}[R(T)]\geq\Omega(\sqrt{KT})$.


## Proof

On a very high level, the proof proceeds as follows. We consider 0-1 rewards and the following family of problem instances, with parameter $\epsilon>0$ to be adjusted in the analysis: $\mathcal{I}_{j}$ where $\mu_{i}=\frac{1}{2}+\frac{\epsilon}{2}$ for arm $i=j$ and $\mu_{i}=\frac{1}{2}$ for each arm $i\neq j$, for each $j=1,2,\ldots,K$. We prove that sampling each arm $\Omega(1/\epsilon^{2})$ times is necessary to determine whether this arm is good or bad. This leads to regret $\Omega(K/\epsilon)$. We complete the proof by plugging in $\epsilon=\Theta(\sqrt{K/T})$. (Full technical details are presented in subsequent steps.)
