---
slug: introduction-to-multi-armed-bandits--lemma-3-4
label: Lemma 3.4
claim_type: lemma
statement: 'Let $H^{\prime}$ be a feasible $t^{\prime}$-history. Then $\mathbb{P}_{H\oplus
  H^{\prime}}=(\mathbb{P}_{H})_{H^{\prime}}$. More explicitly: $\mathbb{P}_{H\oplus
  H^{\prime}}(\mathcal{M})=\Pr_{\mu\sim\mathbb{P}_{H}}[\mu\in\mathcal{M}\mid H_{t^{\prime}}=H^{\prime}],\quad\forall\mathcal{M}\subset[0,1]^{K}.$'
proof: 'It suffices to prove the lemma for a singleton set $\mathcal{M}=\{\tilde{\mu}\}$,
  for any given vector $\tilde{\mu}\in\mathcal{F}$.


  Let $\mathtt{ALG}$ be the $(H\oplus H^{\prime})$-induced algorithm. Let $H^{\mathtt{ALG}}_{t}$
  denote its $t$-history, and let $H^{\mathtt{ALG}}_{S}$ denote its $S$-history, where
  $S=[t+t^{\prime}]\setminus[t]$. We will prove that $\mathbb{P}_{H\oplus H^{\prime}}(\mu=\tilde{\mu})=\Pr_{\mu\sim\mathbb{P}_{H}}[\mu=\tilde{\mu}\mid
  H^{\mathtt{ALG}}_{S}=H^{\prime}].$


  We are interested in two events: $\mathcal{E}_{t}=\{H^{\mathtt{ALG}}_{t}=H\}$ and
  $\mathcal{E}_{S}=\{H^{\mathtt{ALG}}_{S}=H^{\prime}\}$.


  Write $\mathbb{Q}$ for $\Pr_{\mu\sim\mathbb{P}_{H}}$ for brevity. We prove that
  $\mathbb{Q}[\cdot]=\Pr[\,\cdot\mid\mathcal{E}_{t}]$ for some events of interest.
  Formally,


  $\mathbb{Q}[\mu=\tilde{\mu}] = \mathbb{P}[\mu=\tilde{\mu}\mid\mathcal{E}_{t}]$ (by
  definition of $\mathbb{P}_{H}$)

  $\mathbb{Q}[\mathcal{E}_{S}\mid\mu=\tilde{\mu}] = \Pr[\mathcal{E}_{S}\mid\mu=\tilde{\mu},\mathcal{E}_{t}]$
  (by definition of $\mathtt{ALG}$)

  $\mathbb{Q}[\mathcal{E}_{S}\text{ and }\mu=\tilde{\mu}] = \mathbb{Q}[\mu=\tilde{\mu}]\cdot\mathbb{Q}[\mathcal{E}_{S}\mid\mu=\tilde{\mu}]
  = \mathbb{P}[\mu=\tilde{\mu}\mid\mathcal{E}_{t}]\cdot\Pr[\mathcal{E}_{S}\mid\mu=\tilde{\mu},\mathcal{E}_{t}]
  = \Pr[\mathcal{E}_{S}\text{ and }\mu=\tilde{\mu}\mid\mathcal{E}_{t}].$


  Summing up over all $\tilde{\mu}\in\mathcal{F}$, we obtain: $\mathbb{Q}[\mathcal{E}_{S}]=\sum_{\tilde{\mu}\in\mathcal{F}}\mathbb{Q}[\mathcal{E}_{S}\text{
  and }\mu=\tilde{\mu}]=\sum_{\tilde{\mu}\in\mathcal{F}}\Pr[\mathcal{E}_{S}\text{
  and }\mu=\tilde{\mu}\mid\mathcal{E}_{t}]=\Pr[\mathcal{E}_{S}\mid\mathcal{E}_{t}].$


  Now, the right-hand side of (41) is $\mathbb{Q}[\mu=\tilde{\mu}\mid\mathcal{E}_{S}]
  = \frac{\mathbb{Q}[\mu=\tilde{\mu}\text{ and }\mathcal{E}_{S}]}{\mathbb{Q}[\mathcal{E}_{S}]}=\frac{\Pr[\mathcal{E}_{S}\text{
  and }\mu=\tilde{\mu}\mid\mathcal{E}_{t}]}{\Pr[\mathcal{E}_{S}\mid\mathcal{E}_{t}]}=\frac{\Pr[\mathcal{E}_{t}\text{
  and }\mathcal{E}_{S}\text{ and }\mu=\tilde{\mu}]}{\Pr[\mathcal{E}_{t}\text{ and
  }\mathcal{E}_{S}]} = \Pr[\mu=\tilde{\mu}\mid\mathcal{E}_{t}\text{ and }\mathcal{E}_{S}].$


  The latter equals $\mathbb{P}_{H\oplus H^{\prime}}(\mu=\tilde{\mu})$, proving (41).


  It remains to switch from $\mathtt{ALG}$ to an arbitrary bandit algorithm. We apply
  Lemma 3.1 twice, to both sides of (41). The first application is simply that $\mathbb{P}_{H\oplus
  H^{\prime}}(\mu=\tilde{\mu})$ does not depend on the bandit algorithm. The second
  application is for prior distribution $\mathbb{P}_{H}$ and feasible $t^{\prime}$-history
  $H^{\prime}$. Let $\mathtt{ALG}^{\prime}$ be the $H^{\prime}$-induced algorithm,
  and let $H^{\mathtt{ALG}^{\prime}}_{t^{\prime}}$ be its $t^{\prime}$-history. Then
  $\Pr_{\mu\sim\mathbb{P}_{H}}[\mu=\tilde{\mu}\mid H^{\mathtt{ALG}}_{S}=H^{\prime}]=\Pr_{\mu\sim\mathbb{P}_{H}}[\mu=\tilde{\mu}\mid
  H^{\mathtt{ALG}^{\prime}}_{t^{\prime}}=H^{\prime}]=\Pr_{\mu\sim\mathbb{P}_{H}}[\mu=\tilde{\mu}\mid
  H_{t^{\prime}}=H^{\prime}].$ The second equality is by Lemma 3.1. We defined $\mathtt{ALG}^{\prime}$
  to switch from the $S$-history to the $t^{\prime}$-history. Thus, we''ve proved
  that the right-hand side of (42) equals $\mathbb{P}_{H\oplus H^{\prime}}(\mu=\tilde{\mu})$
  for an arbitrary bandit algorithm.'
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/bayesian-update]]'
- '[[concepts/sequential-bayesian-update]]'
- '[[concepts/h-consistent-algorithm]]'
- '[[concepts/bayesian-posterior-distribution]]'
- '[[concepts/feasible-t-history]]'
about_meta:
- target: '[[concepts/bayesian-update]]'
  role: primary
  aspect: ''
- target: '[[concepts/sequential-bayesian-update]]'
  role: primary
  aspect: ''
- target: '[[concepts/h-consistent-algorithm]]'
  role: primary
  aspect: ''
- target: '[[concepts/bayesian-posterior-distribution]]'
  role: primary
  aspect: ''
- target: '[[concepts/feasible-t-history]]'
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

# Lemma 3.4

Let $H^{\prime}$ be a feasible $t^{\prime}$-history. Then $\mathbb{P}_{H\oplus H^{\prime}}=(\mathbb{P}_{H})_{H^{\prime}}$. More explicitly: $\mathbb{P}_{H\oplus H^{\prime}}(\mathcal{M})=\Pr_{\mu\sim\mathbb{P}_{H}}[\mu\in\mathcal{M}\mid H_{t^{\prime}}=H^{\prime}],\quad\forall\mathcal{M}\subset[0,1]^{K}.$


## Proof

It suffices to prove the lemma for a singleton set $\mathcal{M}=\{\tilde{\mu}\}$, for any given vector $\tilde{\mu}\in\mathcal{F}$.

Let $\mathtt{ALG}$ be the $(H\oplus H^{\prime})$-induced algorithm. Let $H^{\mathtt{ALG}}_{t}$ denote its $t$-history, and let $H^{\mathtt{ALG}}_{S}$ denote its $S$-history, where $S=[t+t^{\prime}]\setminus[t]$. We will prove that $\mathbb{P}_{H\oplus H^{\prime}}(\mu=\tilde{\mu})=\Pr_{\mu\sim\mathbb{P}_{H}}[\mu=\tilde{\mu}\mid H^{\mathtt{ALG}}_{S}=H^{\prime}].$

We are interested in two events: $\mathcal{E}_{t}=\{H^{\mathtt{ALG}}_{t}=H\}$ and $\mathcal{E}_{S}=\{H^{\mathtt{ALG}}_{S}=H^{\prime}\}$.

Write $\mathbb{Q}$ for $\Pr_{\mu\sim\mathbb{P}_{H}}$ for brevity. We prove that $\mathbb{Q}[\cdot]=\Pr[\,\cdot\mid\mathcal{E}_{t}]$ for some events of interest. Formally,

$\mathbb{Q}[\mu=\tilde{\mu}] = \mathbb{P}[\mu=\tilde{\mu}\mid\mathcal{E}_{t}]$ (by definition of $\mathbb{P}_{H}$)
$\mathbb{Q}[\mathcal{E}_{S}\mid\mu=\tilde{\mu}] = \Pr[\mathcal{E}_{S}\mid\mu=\tilde{\mu},\mathcal{E}_{t}]$ (by definition of $\mathtt{ALG}$)
$\mathbb{Q}[\mathcal{E}_{S}\text{ and }\mu=\tilde{\mu}] = \mathbb{Q}[\mu=\tilde{\mu}]\cdot\mathbb{Q}[\mathcal{E}_{S}\mid\mu=\tilde{\mu}] = \mathbb{P}[\mu=\tilde{\mu}\mid\mathcal{E}_{t}]\cdot\Pr[\mathcal{E}_{S}\mid\mu=\tilde{\mu},\mathcal{E}_{t}] = \Pr[\mathcal{E}_{S}\text{ and }\mu=\tilde{\mu}\mid\mathcal{E}_{t}].$

Summing up over all $\tilde{\mu}\in\mathcal{F}$, we obtain: $\mathbb{Q}[\mathcal{E}_{S}]=\sum_{\tilde{\mu}\in\mathcal{F}}\mathbb{Q}[\mathcal{E}_{S}\text{ and }\mu=\tilde{\mu}]=\sum_{\tilde{\mu}\in\mathcal{F}}\Pr[\mathcal{E}_{S}\text{ and }\mu=\tilde{\mu}\mid\mathcal{E}_{t}]=\Pr[\mathcal{E}_{S}\mid\mathcal{E}_{t}].$

Now, the right-hand side of (41) is $\mathbb{Q}[\mu=\tilde{\mu}\mid\mathcal{E}_{S}] = \frac{\mathbb{Q}[\mu=\tilde{\mu}\text{ and }\mathcal{E}_{S}]}{\mathbb{Q}[\mathcal{E}_{S}]}=\frac{\Pr[\mathcal{E}_{S}\text{ and }\mu=\tilde{\mu}\mid\mathcal{E}_{t}]}{\Pr[\mathcal{E}_{S}\mid\mathcal{E}_{t}]}=\frac{\Pr[\mathcal{E}_{t}\text{ and }\mathcal{E}_{S}\text{ and }\mu=\tilde{\mu}]}{\Pr[\mathcal{E}_{t}\text{ and }\mathcal{E}_{S}]} = \Pr[\mu=\tilde{\mu}\mid\mathcal{E}_{t}\text{ and }\mathcal{E}_{S}].$

The latter equals $\mathbb{P}_{H\oplus H^{\prime}}(\mu=\tilde{\mu})$, proving (41).

It remains to switch from $\mathtt{ALG}$ to an arbitrary bandit algorithm. We apply Lemma 3.1 twice, to both sides of (41). The first application is simply that $\mathbb{P}_{H\oplus H^{\prime}}(\mu=\tilde{\mu})$ does not depend on the bandit algorithm. The second application is for prior distribution $\mathbb{P}_{H}$ and feasible $t^{\prime}$-history $H^{\prime}$. Let $\mathtt{ALG}^{\prime}$ be the $H^{\prime}$-induced algorithm, and let $H^{\mathtt{ALG}^{\prime}}_{t^{\prime}}$ be its $t^{\prime}$-history. Then $\Pr_{\mu\sim\mathbb{P}_{H}}[\mu=\tilde{\mu}\mid H^{\mathtt{ALG}}_{S}=H^{\prime}]=\Pr_{\mu\sim\mathbb{P}_{H}}[\mu=\tilde{\mu}\mid H^{\mathtt{ALG}^{\prime}}_{t^{\prime}}=H^{\prime}]=\Pr_{\mu\sim\mathbb{P}_{H}}[\mu=\tilde{\mu}\mid H_{t^{\prime}}=H^{\prime}].$ The second equality is by Lemma 3.1. We defined $\mathtt{ALG}^{\prime}$ to switch from the $S$-history to the $t^{\prime}$-history. Thus, we've proved that the right-hand side of (42) equals $\mathbb{P}_{H\oplus H^{\prime}}(\mu=\tilde{\mu})$ for an arbitrary bandit algorithm.
