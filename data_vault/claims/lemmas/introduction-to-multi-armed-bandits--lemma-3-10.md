---
slug: introduction-to-multi-armed-bandits--lemma-3-10
label: Lemma 3.10
claim_type: lemma
statement: 'Assume we have lower and upper bound functions that satisfy properties
  (47) and (48), for some parameter $\gamma>0$. Then Bayesian Regret of Thompson Sampling
  can be bounded as follows:


  $\mathtt{BR}(T)\leq 2\gamma+2\sum_{t=1}^{T}\operatornamewithlimits{\mathbb{E}}\left[\,r(a_{t},\>H_{t})\,\right].$'
proof: 'Fix round $t$. Interpreted as random variables, the chosen arm $a_{t}$ and
  the best arm $a^{*}$ are identically distributed given $t$-history $H_{t}$: for
  each feasible $t$-history $H$,


  $\Pr[a_{t}=a\mid H_{t}=H]=\Pr[a^{*}=a\mid H_{t}=H]\quad\text{for each arm $a$}.$


  It follows that


  $\operatornamewithlimits{\mathbb{E}}[\>U(a^{*},\>H)\>\mid\>H_{t}=H\>]=\operatornamewithlimits{\mathbb{E}}[\>U(a_{t},\>H)\>\mid\>H_{t}=H\>].$
  (49)


  Then Bayesian Regret suffered in round $t$ is


  $\mathtt{BR}_{t}:=\operatornamewithlimits{\mathbb{E}}\left[\,\mu(a^{*})-\mu(a_{t})\,\right]=\operatornamewithlimits{\mathbb{E}}_{H\sim
  H_{t}}\left[\,\operatornamewithlimits{\mathbb{E}}\left[\,\mu(a^{*})-\mu(a_{t})\mid
  H_{t}=H\,\right]\,\right]=\operatornamewithlimits{\mathbb{E}}_{H\sim H_{t}}\left[\,\operatornamewithlimits{\mathbb{E}}\left[\,U(a_{t},H)-\mu(a_{t})+\mu(a^{*})-U(a^{*},H)\mid
  H_{t}=H\,\right]\,\right]$ (by Eq. (49))

  $=\underbrace{\operatornamewithlimits{\mathbb{E}}\left[\,U(a_{t},H_{t})-\mu(a_{t})\,\right]}_{\text{Summand
  1}}+\underbrace{\operatornamewithlimits{\mathbb{E}}\left[\,\mu(a^{*})-U(a^{*},H_{t})\,\right]}_{\text{Summand
  2}}.$


  We will use properties (47) and (48) to bound both summands. Note that we cannot
  immediately use these properties because they assume a fixed arm $a$, whereas both
  $a_{t}$ and $a^{*}$ are random variables.


  $\operatornamewithlimits{\mathbb{E}}\left[\,\mu(a^{*})-U(a^{*},H_{t})\,\right]$
  (Summand 1)

  $\leq\operatornamewithlimits{\mathbb{E}}\left[\,(\mu(a^{*})-U(a^{*},H_{t}))^{+}\,\right]\leq\operatornamewithlimits{\mathbb{E}}\left[\,\sum_{\text{arms
  $a$}}\left[\,\mu(a)-U(a,H_{t})\,\right]^{+}\,\right]=\sum_{\text{arms $a$}}\operatornamewithlimits{\mathbb{E}}\left[\,\left(\,U(a,H_{t})-\mu(a)\,\right)^{-}\,\right]\leq
  K\cdot\frac{\gamma}{KT}=\frac{\gamma}{T}$ (by property (47)).


  $\operatornamewithlimits{\mathbb{E}}\left[\,U(a_{t},H_{t})-\mu(a_{t})\,\right]$
  (Summand 2)

  $=\operatornamewithlimits{\mathbb{E}}\left[\,2r(a_{t},H_{t})+L(a_{t},H_{t})-\mu(a_{t})\,\right]$
  (by definition of $r_{t}(\cdot)$)

  $=\operatornamewithlimits{\mathbb{E}}\left[\,2r(a_{t},H_{t})\,\right]+\operatornamewithlimits{\mathbb{E}}\left[\,L(a_{t},H_{t})-\mu(a_{t})\,\right]$


  $\operatornamewithlimits{\mathbb{E}}[L(a_{t},H_{t})-\mu(a_{t})]\leq\operatornamewithlimits{\mathbb{E}}\left[\,\left(\,L(a_{t},H_{t})-\mu(a_{t})\,\right)^{+}\,\right]\leq\operatornamewithlimits{\mathbb{E}}\left[\,\sum_{\text{arms
  $a$}}\left(\,L(a,H_{t})-\mu(a)\,\right)^{+}\,\right]=\sum_{\text{arms $a$}}\operatornamewithlimits{\mathbb{E}}\left[\,\left(\,\mu(a)-L(a,H_{t})\,\right)^{-}\,\right]\leq
  K\cdot\frac{\gamma}{KT}=\frac{\gamma}{T}$ (by property (48)).


  Thus, $\mathtt{BR}_{t}(T)\leq 2\frac{\gamma}{T}+2\,\operatornamewithlimits{\mathbb{E}}[r(a_{t},H_{t})]$.
  The theorem follows by summing up over all rounds $t$.'
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/confidence-radius-function-r]]'
- '[[concepts/thompson-sampling]]'
- '[[concepts/best-arm-a]]'
- '[[concepts/upper-confidence-bound-function-u]]'
- '[[concepts/property-48-for-l]]'
- '[[concepts/parameter-g]]'
- '[[concepts/bayesian-regret]]'
- '[[concepts/lower-confidence-bound-function-l]]'
- '[[concepts/chosen-arm-a-t]]'
- '[[concepts/property-47-for-u]]'
about_meta:
- target: '[[concepts/confidence-radius-function-r]]'
  role: primary
  aspect: ''
- target: '[[concepts/thompson-sampling]]'
  role: primary
  aspect: ''
- target: '[[concepts/best-arm-a]]'
  role: primary
  aspect: ''
- target: '[[concepts/upper-confidence-bound-function-u]]'
  role: primary
  aspect: ''
- target: '[[concepts/property-48-for-l]]'
  role: primary
  aspect: ''
- target: '[[concepts/parameter-g]]'
  role: primary
  aspect: ''
- target: '[[concepts/bayesian-regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/lower-confidence-bound-function-l]]'
  role: primary
  aspect: ''
- target: '[[concepts/chosen-arm-a-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/property-47-for-u]]'
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

# Lemma 3.10

Assume we have lower and upper bound functions that satisfy properties (47) and (48), for some parameter $\gamma>0$. Then Bayesian Regret of Thompson Sampling can be bounded as follows:

$\mathtt{BR}(T)\leq 2\gamma+2\sum_{t=1}^{T}\operatornamewithlimits{\mathbb{E}}\left[\,r(a_{t},\>H_{t})\,\right].$


## Proof

Fix round $t$. Interpreted as random variables, the chosen arm $a_{t}$ and the best arm $a^{*}$ are identically distributed given $t$-history $H_{t}$: for each feasible $t$-history $H$,

$\Pr[a_{t}=a\mid H_{t}=H]=\Pr[a^{*}=a\mid H_{t}=H]\quad\text{for each arm $a$}.$

It follows that

$\operatornamewithlimits{\mathbb{E}}[\>U(a^{*},\>H)\>\mid\>H_{t}=H\>]=\operatornamewithlimits{\mathbb{E}}[\>U(a_{t},\>H)\>\mid\>H_{t}=H\>].$ (49)

Then Bayesian Regret suffered in round $t$ is

$\mathtt{BR}_{t}:=\operatornamewithlimits{\mathbb{E}}\left[\,\mu(a^{*})-\mu(a_{t})\,\right]=\operatornamewithlimits{\mathbb{E}}_{H\sim H_{t}}\left[\,\operatornamewithlimits{\mathbb{E}}\left[\,\mu(a^{*})-\mu(a_{t})\mid H_{t}=H\,\right]\,\right]=\operatornamewithlimits{\mathbb{E}}_{H\sim H_{t}}\left[\,\operatornamewithlimits{\mathbb{E}}\left[\,U(a_{t},H)-\mu(a_{t})+\mu(a^{*})-U(a^{*},H)\mid H_{t}=H\,\right]\,\right]$ (by Eq. (49))
$=\underbrace{\operatornamewithlimits{\mathbb{E}}\left[\,U(a_{t},H_{t})-\mu(a_{t})\,\right]}_{\text{Summand 1}}+\underbrace{\operatornamewithlimits{\mathbb{E}}\left[\,\mu(a^{*})-U(a^{*},H_{t})\,\right]}_{\text{Summand 2}}.$

We will use properties (47) and (48) to bound both summands. Note that we cannot immediately use these properties because they assume a fixed arm $a$, whereas both $a_{t}$ and $a^{*}$ are random variables.

$\operatornamewithlimits{\mathbb{E}}\left[\,\mu(a^{*})-U(a^{*},H_{t})\,\right]$ (Summand 1)
$\leq\operatornamewithlimits{\mathbb{E}}\left[\,(\mu(a^{*})-U(a^{*},H_{t}))^{+}\,\right]\leq\operatornamewithlimits{\mathbb{E}}\left[\,\sum_{\text{arms $a$}}\left[\,\mu(a)-U(a,H_{t})\,\right]^{+}\,\right]=\sum_{\text{arms $a$}}\operatornamewithlimits{\mathbb{E}}\left[\,\left(\,U(a,H_{t})-\mu(a)\,\right)^{-}\,\right]\leq K\cdot\frac{\gamma}{KT}=\frac{\gamma}{T}$ (by property (47)).

$\operatornamewithlimits{\mathbb{E}}\left[\,U(a_{t},H_{t})-\mu(a_{t})\,\right]$ (Summand 2)
$=\operatornamewithlimits{\mathbb{E}}\left[\,2r(a_{t},H_{t})+L(a_{t},H_{t})-\mu(a_{t})\,\right]$ (by definition of $r_{t}(\cdot)$)
$=\operatornamewithlimits{\mathbb{E}}\left[\,2r(a_{t},H_{t})\,\right]+\operatornamewithlimits{\mathbb{E}}\left[\,L(a_{t},H_{t})-\mu(a_{t})\,\right]$

$\operatornamewithlimits{\mathbb{E}}[L(a_{t},H_{t})-\mu(a_{t})]\leq\operatornamewithlimits{\mathbb{E}}\left[\,\left(\,L(a_{t},H_{t})-\mu(a_{t})\,\right)^{+}\,\right]\leq\operatornamewithlimits{\mathbb{E}}\left[\,\sum_{\text{arms $a$}}\left(\,L(a,H_{t})-\mu(a)\,\right)^{+}\,\right]=\sum_{\text{arms $a$}}\operatornamewithlimits{\mathbb{E}}\left[\,\left(\,\mu(a)-L(a,H_{t})\,\right)^{-}\,\right]\leq K\cdot\frac{\gamma}{KT}=\frac{\gamma}{T}$ (by property (48)).

Thus, $\mathtt{BR}_{t}(T)\leq 2\frac{\gamma}{T}+2\,\operatornamewithlimits{\mathbb{E}}[r(a_{t},H_{t})]$. The theorem follows by summing up over all rounds $t$.
