---
slug: introduction-to-multi-armed-bandits--claim-10-5
label: Claim 10.5
claim_type: lemma
statement: $T\cdot\mathtt{OPT}_{\mathtt{LP}}\geq\mathtt{OPT}$.
proof: 'Fix some algorithm $\mathtt{ALG}$ for $\mathtt{BwK}$. Let $\tau$ be the round
  after which this algorithm stops. Without loss of generality, if $\tau<T$ then $\mathtt{ALG}$
  continues to play the null arm in all rounds $\tau,\tau+1\,,\ \ldots\ ,T$.


  Let $X_{t}(a)={\bf 1}_{\left\{\,a_{t}=a\,\right\}}$ be the indicator variable of
  the event that $\mathtt{ALG}$ chooses arm $a$ in round $t$. Let $D\in\Delta_{K}$
  be the algorithm''s expected average play, as per Definition 9.2: i.e., for each
  arm $a$, $D(a)$ is the expected fraction of rounds in which this arm is chosen.


  First, we claim that the expected total adjusted reward is $\operatornamewithlimits{\mathbb{E}}[\mathtt{REW}(\mathtt{ALG})]=r(D)$.
  Indeed,


  $\operatornamewithlimits{\mathbb{E}}[r_{t}]=\textstyle\sum_{a\in[K]}\;\Pr[a_{t}=a]\cdot\operatornamewithlimits{\mathbb{E}}[r_{t}\mid
  a_{t}=a]=\textstyle\sum_{a\in[K]}\;\operatornamewithlimits{\mathbb{E}}[X_{t}(a)]\cdot
  r(a).$


  $\operatornamewithlimits{\mathbb{E}}[\mathtt{REW}]=\sum_{t\in[T]}\operatornamewithlimits{\mathbb{E}}[r_{t}]=\sum_{a\in[K]}r(a)\cdot\sum_{t\in[T]}\operatornamewithlimits{\mathbb{E}}[X_{t}(a)]=\sum_{a\in[K]}r(a)\cdot
  T\cdot D(a)=T\cdot r(D).$


  Similarly, the expected total consumption of each resource $i$ is $\sum_{t\in[T]}\operatornamewithlimits{\mathbb{E}}[c_{t,i}]=T\cdot
  c_{i}(D)$.


  Since the (modified) algorithm does not stop until time $T$, we have $\sum_{t\in[T]}c_{i,t}\leq
  B$, and consequently $c_{i}(D)\leq B/T$. Therefore, $D$ is a feasible solution for
  the linear program (141). It follows that $\operatornamewithlimits{\mathbb{E}}[\mathtt{REW}(\mathtt{ALG})]=r(D)\leq\mathtt{OPT}_{\mathtt{LP}}$.'
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/opt-lp]]'
- '[[concepts/linear-program-for-bwk]]'
- '[[concepts/optimal-reward-in-bwk]]'
- '[[concepts/bandits-with-knapsacks]]'
about_meta:
- target: '[[concepts/opt-lp]]'
  role: primary
  aspect: ''
- target: '[[concepts/linear-program-for-bwk]]'
  role: primary
  aspect: ''
- target: '[[concepts/optimal-reward-in-bwk]]'
  role: primary
  aspect: ''
- target: '[[concepts/bandits-with-knapsacks]]'
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

# Claim 10.5

$T\cdot\mathtt{OPT}_{\mathtt{LP}}\geq\mathtt{OPT}$.


## Proof

Fix some algorithm $\mathtt{ALG}$ for $\mathtt{BwK}$. Let $\tau$ be the round after which this algorithm stops. Without loss of generality, if $\tau<T$ then $\mathtt{ALG}$ continues to play the null arm in all rounds $\tau,\tau+1\,,\ \ldots\ ,T$.

Let $X_{t}(a)={\bf 1}_{\left\{\,a_{t}=a\,\right\}}$ be the indicator variable of the event that $\mathtt{ALG}$ chooses arm $a$ in round $t$. Let $D\in\Delta_{K}$ be the algorithm's expected average play, as per Definition 9.2: i.e., for each arm $a$, $D(a)$ is the expected fraction of rounds in which this arm is chosen.

First, we claim that the expected total adjusted reward is $\operatornamewithlimits{\mathbb{E}}[\mathtt{REW}(\mathtt{ALG})]=r(D)$. Indeed,

$\operatornamewithlimits{\mathbb{E}}[r_{t}]=\textstyle\sum_{a\in[K]}\;\Pr[a_{t}=a]\cdot\operatornamewithlimits{\mathbb{E}}[r_{t}\mid a_{t}=a]=\textstyle\sum_{a\in[K]}\;\operatornamewithlimits{\mathbb{E}}[X_{t}(a)]\cdot r(a).$

$\operatornamewithlimits{\mathbb{E}}[\mathtt{REW}]=\sum_{t\in[T]}\operatornamewithlimits{\mathbb{E}}[r_{t}]=\sum_{a\in[K]}r(a)\cdot\sum_{t\in[T]}\operatornamewithlimits{\mathbb{E}}[X_{t}(a)]=\sum_{a\in[K]}r(a)\cdot T\cdot D(a)=T\cdot r(D).$

Similarly, the expected total consumption of each resource $i$ is $\sum_{t\in[T]}\operatornamewithlimits{\mathbb{E}}[c_{t,i}]=T\cdot c_{i}(D)$.

Since the (modified) algorithm does not stop until time $T$, we have $\sum_{t\in[T]}c_{i,t}\leq B$, and consequently $c_{i}(D)\leq B/T$. Therefore, $D$ is a feasible solution for the linear program (141). It follows that $\operatornamewithlimits{\mathbb{E}}[\mathtt{REW}(\mathtt{ALG})]=r(D)\leq\mathtt{OPT}_{\mathtt{LP}}$.
