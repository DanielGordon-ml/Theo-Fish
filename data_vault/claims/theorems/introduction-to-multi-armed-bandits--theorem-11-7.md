---
slug: introduction-to-multi-armed-bandits--theorem-11-7
label: Theorem 11.7
claim_type: theorem
statement: With probability at least $\mu_{1}^{0}-\mu_{2}^{0}$, $\mathtt{GREEDY}$
  never chooses arm $2$.
proof: 'In each round $t$, the key quantity is $Z_{t}=\operatorname{\mathbb{E}}[\mu_{1}-\mu_{2}\mid
  H_{t}]$. Indeed, arm $2$ is chosen if and only if $Z_{t}<0$. Let $\tau$ be the first
  round when $\mathtt{GREEDY}$ chooses arm $2$, or $T+1$ if this never happens. We
  use martingale techniques to prove that $\operatorname{\mathbb{E}}[Z_{\tau}]=\mu_{1}^{0}-\mu_{2}^{0}$.
  We obtain this via a standard application of the optional stopping theorem; we observe
  that $\tau$ is a stopping time relative to the sequence $\mathcal{H}=(H_{t}: t\in[T+1])$,
  and $(Z_{t}:t\in[T+1])$ is a martingale relative to $\mathcal{H}$. (The latter follows
  from a general fact that sequence $\operatorname{\mathbb{E}}[X\mid H_{t}]$, $t\in[T+1]$
  is a martingale w.r.t. $\mathcal{H}$ for any random variable $X$ with $\operatorname{\mathbb{E}}[|X|]<\infty$.
  It is known as Doob martingale for $X$.) The optional stopping theorem asserts that
  $\operatorname{\mathbb{E}}[Z_{\tau}]=\operatorname{\mathbb{E}}[Z_{1}]$ for any martingale
  $Z_{t}$ and any bounded stopping time $\tau$. The equation follows because $\operatorname{\mathbb{E}}[Z_{1}]=\mu_{1}^{0}-\mu_{2}^{0}$.
  On the other hand, by Bayes'' theorem it holds that $\operatorname{\mathbb{E}}[Z_{\tau}]=\Pr[\tau\leq
  T]\,\operatorname{\mathbb{E}}[Z_{\tau}\mid\tau\leq T]+\Pr[\tau>T]\,\operatorname{\mathbb{E}}[Z_{\tau}\mid\tau>T]$.
  Recall that $\tau\leq T$ implies that $\mathtt{GREEDY}$ chooses arm $2$ in round
  $\tau$, which in turn implies that $Z_{\tau}\leq 0$ by definition of $\mathtt{GREEDY}$.
  It follows that $\operatorname{\mathbb{E}}[Z_{\tau}\mid\tau\leq T]\leq 0$. Plugging
  this in, we find that $\mu_{1}^{0}-\mu_{2}^{0}=\operatorname{\mathbb{E}}[Z_{\tau}]\leq\Pr[\tau>T]$.
  And $\{\tau>T\}$ is precisely the event that $\mathtt{GREEDY}$ never tries arm 2.'
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/martingale-z-t]]'
- '[[concepts/greedy]]'
- '[[concepts/doob-martingale]]'
- '[[concepts/bayesian-regret]]'
- '[[concepts/incentivized-exploration]]'
- '[[concepts/stopping-time-tau]]'
- '[[concepts/prior-mean-reward]]'
about_meta:
- target: '[[concepts/martingale-z-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/greedy]]'
  role: primary
  aspect: ''
- target: '[[concepts/doob-martingale]]'
  role: primary
  aspect: ''
- target: '[[concepts/bayesian-regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/incentivized-exploration]]'
  role: primary
  aspect: ''
- target: '[[concepts/stopping-time-tau]]'
  role: primary
  aspect: ''
- target: '[[concepts/prior-mean-reward]]'
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

# Theorem 11.7

With probability at least $\mu_{1}^{0}-\mu_{2}^{0}$, $\mathtt{GREEDY}$ never chooses arm $2$.


## Proof

In each round $t$, the key quantity is $Z_{t}=\operatorname{\mathbb{E}}[\mu_{1}-\mu_{2}\mid H_{t}]$. Indeed, arm $2$ is chosen if and only if $Z_{t}<0$. Let $\tau$ be the first round when $\mathtt{GREEDY}$ chooses arm $2$, or $T+1$ if this never happens. We use martingale techniques to prove that $\operatorname{\mathbb{E}}[Z_{\tau}]=\mu_{1}^{0}-\mu_{2}^{0}$. We obtain this via a standard application of the optional stopping theorem; we observe that $\tau$ is a stopping time relative to the sequence $\mathcal{H}=(H_{t}: t\in[T+1])$, and $(Z_{t}:t\in[T+1])$ is a martingale relative to $\mathcal{H}$. (The latter follows from a general fact that sequence $\operatorname{\mathbb{E}}[X\mid H_{t}]$, $t\in[T+1]$ is a martingale w.r.t. $\mathcal{H}$ for any random variable $X$ with $\operatorname{\mathbb{E}}[|X|]<\infty$. It is known as Doob martingale for $X$.) The optional stopping theorem asserts that $\operatorname{\mathbb{E}}[Z_{\tau}]=\operatorname{\mathbb{E}}[Z_{1}]$ for any martingale $Z_{t}$ and any bounded stopping time $\tau$. The equation follows because $\operatorname{\mathbb{E}}[Z_{1}]=\mu_{1}^{0}-\mu_{2}^{0}$. On the other hand, by Bayes' theorem it holds that $\operatorname{\mathbb{E}}[Z_{\tau}]=\Pr[\tau\leq T]\,\operatorname{\mathbb{E}}[Z_{\tau}\mid\tau\leq T]+\Pr[\tau>T]\,\operatorname{\mathbb{E}}[Z_{\tau}\mid\tau>T]$. Recall that $\tau\leq T$ implies that $\mathtt{GREEDY}$ chooses arm $2$ in round $\tau$, which in turn implies that $Z_{\tau}\leq 0$ by definition of $\mathtt{GREEDY}$. It follows that $\operatorname{\mathbb{E}}[Z_{\tau}\mid\tau\leq T]\leq 0$. Plugging this in, we find that $\mu_{1}^{0}-\mu_{2}^{0}=\operatorname{\mathbb{E}}[Z_{\tau}]\leq\Pr[\tau>T]$. And $\{\tau>T\}$ is precisely the event that $\mathtt{GREEDY}$ never tries arm 2.
