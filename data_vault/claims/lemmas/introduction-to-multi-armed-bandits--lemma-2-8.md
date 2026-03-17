---
slug: introduction-to-multi-armed-bandits--lemma-2-8
label: Lemma 2.8
claim_type: lemma
statement: Consider a "best-arm identification" problem with $T \leq \frac{cK}{\epsilon^{2}}$,
  for a small enough absolute constant $c > 0$. Fix any deterministic algorithm for
  this problem. Then there exists at least $\lceil K/3 \rceil$ arms $a$ such that,
  for problem instances $\mathcal{I}_{a}$ defined in (17), we have $\Pr\left[y_{T}
  = a \mid \mathcal{I}_{a}\right] < \nicefrac{3}{4}$.
proof: 'Proof ($K=2$ arms): Let us set up the sample space which we will use in the
  proof. Let $(r_{t}(a): a \in [K], t \in [T])$ be a tuple of mutually independent
  Bernoulli random variables such that $\mathbb{E}[r_{t}(a)] = \mu(a)$. We refer to
  this tuple as the rewards table, where we interpret $r_{t}(a)$ as the reward received
  by the algorithm for the $t$-th time it chooses arm $a$. The sample space is $\Omega
  = \{0,1\}^{K \times T}$, where each outcome $\omega \in \Omega$ corresponds to a
  particular realization of the rewards table. Each problem instance $\mathcal{I}_{j}$
  defines distribution $P_{j}$ on $\Omega$: $P_{j}(A) = \Pr[A \mid \text{instance
  } \mathcal{I}_{j}]$ for each $A \subset \Omega$. Let $P_{j}^{a,t}$ be the distribution
  of $r_{t}(a)$ under instance $\mathcal{I}_{j}$, so that $P_{j} = \prod_{a \in [K],
  t \in [T]} P_{j}^{a,t}$.


  We need to prove that (22) holds for at least one of the arms. For the sake of contradiction,
  assume it fails for both arms. Let $A = \{y_{T} = 1\} \subset \Omega$ be the event
  that the algorithm predicts arm 1. Then $P_{1}(A) \geq \nicefrac{3}{4}$ and $P_{2}(A)
  \leq \nicefrac{1}{4}$, so their difference is $P_{1}(A) - P_{2}(A) \geq \nicefrac{1}{2}$.


  To arrive at a contradiction, we use a KL-divergence argument: $2(P_{1}(A) - P_{2}(A))^{2}
  \leq \mathtt{KL}(P_{1}, P_{2})$ (by Pinsker''s inequality) $= \sum_{a=1}^{K} \sum_{t=1}^{T}
  \mathtt{KL}(P_{1}^{a,t}, P_{2}^{a,t})$ (by Chain Rule) $\leq 2T \cdot 2\epsilon^{2}$
  (by Theorem on KL properties (d)). The last inequality holds because for each arm
  $a$ and each round $t$, one of the distributions $P_{1}^{a,t}$ and $P_{2}^{a,t}$
  is a fair coin $\mathtt{RC}_{0}$, and another is a biased coin $\mathtt{RC}_{\epsilon}$.
  Simplifying, $P_{1}(A) - P_{2}(A) \leq \epsilon\sqrt{2T} < \tfrac{1}{2}$ whenever
  $T \leq (\tfrac{1}{4\epsilon})^{2}$.


  General case: For the analysis, we consider an additional problem instance $\mathcal{I}_{0}
  = \{\mu_{i} = \tfrac{1}{2} \text{ for all arms } i\}$, the "base instance". Let
  $\mathbb{E}_{0}[\cdot]$ be the expectation given this problem instance. Also, let
  $T_{a}$ be the total number of times arm $a$ is played.


  We observe: There are $\geq \tfrac{2K}{3}$ arms $j$ such that $\mathbb{E}_{0}(T_{j})
  \leq \tfrac{3T}{K}$; There are $\geq \tfrac{2K}{3}$ arms $j$ such that $P_{0}(y_{T}
  = j) \leq \tfrac{3}{K}$. (To prove the first, assume for contradiction that we have
  more than $\frac{K}{3}$ arms with $\mathbb{E}_{0}(T_{j}) > \frac{3T}{K}$. Then the
  expected total number of times these arms are played is strictly greater than $T$,
  contradiction. The second is proved similarly.) By Markov inequality, $\mathbb{E}_{0}(T_{j})
  \leq \frac{3T}{K}$ implies that $\Pr[T_{j} \leq \frac{24T}{K}] \geq \nicefrac{7}{8}$.


  Since the sets of arms in (25) and (26) must overlap on at least $\frac{K}{3}$ arms,
  we conclude: There are at least $\nicefrac{K}{3}$ arms $j$ such that $\Pr[T_{j}
  \leq \tfrac{24T}{K}] \geq \nicefrac{7}{8}$ and $P_{0}(y_{T} = j) \leq \nicefrac{3}{K}$.


  Fix an arm $j$ satisfying the two properties. We prove $P_{j}[Y_{T} = j] \leq \nicefrac{1}{2}$.
  We consider a "reduced" sample space with arm $j$ played only $m = \min(T, 24T/K)$
  times: $\Omega^{*} = \Omega_{j}^{m} \times \prod_{\text{arms } a \neq j} \Omega_{a}^{T}$.
  For each problem instance $\mathcal{I}_{\ell}$, we define distribution $P^{*}_{\ell}$
  on $\Omega^{*}$ as a restriction of $P_{\ell}$ to the reduced sample space.


  We apply the KL-divergence argument to distributions $P^{*}_{0}$ and $P^{*}_{j}$:
  $2(P_{0}^{*}(A) - P_{j}^{*}(A))^{2} \leq \mathtt{KL}(P_{0}^{*}, P_{j}^{*})$ (by
  Pinsker''s inequality) $= \sum_{\text{arms } a} \sum_{t} \mathtt{KL}(P_{0}^{a,t},
  P_{j}^{a,t}) = \sum_{\text{arms } a \neq j} \sum_{t=1}^{T} \mathtt{KL}(P_{0}^{a,t},
  P_{j}^{a,t}) + \sum_{t=1}^{m} \mathtt{KL}(P_{0}^{j,t}, P_{j}^{j,t}) \leq 0 + m \cdot
  2\epsilon^{2}$. The last inequality holds because each arm $a \neq j$ has identical
  reward distributions under $\mathcal{I}_{0}$ and $\mathcal{I}_{j}$, and for arm
  $j$ we only sum over $m$ samples.


  Therefore, assuming $T \leq \frac{cK}{\epsilon^{2}}$ with small enough constant
  $c$, $|P_{0}^{*}(A) - P_{j}^{*}(A)| \leq \epsilon\sqrt{m} < \tfrac{1}{8}$ for all
  events $A \subset \Omega^{*}$.


  We apply (30) to events $A = \{y_{T} = j \text{ and } T_{j} \leq m\}$ and $A'' =
  \{T_{j} > m\}$. Note $A, A'' \subset \Omega^{*}$. Then: $P_{j}(A) \leq \tfrac{1}{8}
  + P_{0}(A) \leq \tfrac{1}{8} + P_{0}(y_{T} = j) \leq \tfrac{1}{4}$ (by choice of
  arm $j$). $P_{j}(A'') \leq \tfrac{1}{8} + P_{0}(A'') \leq \tfrac{1}{4}$ (by choice
  of arm $j$). $P_{j}(Y_{T} = j) \leq P_{j}(Y_{T} = j \text{ and } T_{j} \leq m) +
  P_{j}(T_{j} > m) = P_{j}(A) + P_{j}(A'') \leq \nicefrac{1}{2}$. This completes the
  proof.'
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/distribution-p-j]]'
- '[[concepts/number-of-arms-k]]'
- '[[concepts/reduced-sample-space-omega]]'
- '[[concepts/0-1-rewards]]'
- '[[concepts/kl-divergence]]'
- '[[concepts/bernoulli-distribution]]'
- '[[concepts/time-horizon-t]]'
- '[[concepts/deterministic-algorithm]]'
- '[[concepts/rewards-table]]'
- '[[concepts/best-arm-identification]]'
- '[[concepts/family-of-problem-instances]]'
- '[[concepts/parameter-epsilon]]'
- '[[concepts/sample-space-omega]]'
about_meta:
- target: '[[concepts/distribution-p-j]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-arms-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/reduced-sample-space-omega]]'
  role: primary
  aspect: ''
- target: '[[concepts/0-1-rewards]]'
  role: primary
  aspect: ''
- target: '[[concepts/kl-divergence]]'
  role: primary
  aspect: ''
- target: '[[concepts/bernoulli-distribution]]'
  role: primary
  aspect: ''
- target: '[[concepts/time-horizon-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/deterministic-algorithm]]'
  role: primary
  aspect: ''
- target: '[[concepts/rewards-table]]'
  role: primary
  aspect: ''
- target: '[[concepts/best-arm-identification]]'
  role: primary
  aspect: ''
- target: '[[concepts/family-of-problem-instances]]'
  role: primary
  aspect: ''
- target: '[[concepts/parameter-epsilon]]'
  role: primary
  aspect: ''
- target: '[[concepts/sample-space-omega]]'
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

# Lemma 2.8

Consider a "best-arm identification" problem with $T \leq \frac{cK}{\epsilon^{2}}$, for a small enough absolute constant $c > 0$. Fix any deterministic algorithm for this problem. Then there exists at least $\lceil K/3 \rceil$ arms $a$ such that, for problem instances $\mathcal{I}_{a}$ defined in (17), we have $\Pr\left[y_{T} = a \mid \mathcal{I}_{a}\right] < \nicefrac{3}{4}$.


## Proof

Proof ($K=2$ arms): Let us set up the sample space which we will use in the proof. Let $(r_{t}(a): a \in [K], t \in [T])$ be a tuple of mutually independent Bernoulli random variables such that $\mathbb{E}[r_{t}(a)] = \mu(a)$. We refer to this tuple as the rewards table, where we interpret $r_{t}(a)$ as the reward received by the algorithm for the $t$-th time it chooses arm $a$. The sample space is $\Omega = \{0,1\}^{K \times T}$, where each outcome $\omega \in \Omega$ corresponds to a particular realization of the rewards table. Each problem instance $\mathcal{I}_{j}$ defines distribution $P_{j}$ on $\Omega$: $P_{j}(A) = \Pr[A \mid \text{instance } \mathcal{I}_{j}]$ for each $A \subset \Omega$. Let $P_{j}^{a,t}$ be the distribution of $r_{t}(a)$ under instance $\mathcal{I}_{j}$, so that $P_{j} = \prod_{a \in [K], t \in [T]} P_{j}^{a,t}$.

We need to prove that (22) holds for at least one of the arms. For the sake of contradiction, assume it fails for both arms. Let $A = \{y_{T} = 1\} \subset \Omega$ be the event that the algorithm predicts arm 1. Then $P_{1}(A) \geq \nicefrac{3}{4}$ and $P_{2}(A) \leq \nicefrac{1}{4}$, so their difference is $P_{1}(A) - P_{2}(A) \geq \nicefrac{1}{2}$.

To arrive at a contradiction, we use a KL-divergence argument: $2(P_{1}(A) - P_{2}(A))^{2} \leq \mathtt{KL}(P_{1}, P_{2})$ (by Pinsker's inequality) $= \sum_{a=1}^{K} \sum_{t=1}^{T} \mathtt{KL}(P_{1}^{a,t}, P_{2}^{a,t})$ (by Chain Rule) $\leq 2T \cdot 2\epsilon^{2}$ (by Theorem on KL properties (d)). The last inequality holds because for each arm $a$ and each round $t$, one of the distributions $P_{1}^{a,t}$ and $P_{2}^{a,t}$ is a fair coin $\mathtt{RC}_{0}$, and another is a biased coin $\mathtt{RC}_{\epsilon}$. Simplifying, $P_{1}(A) - P_{2}(A) \leq \epsilon\sqrt{2T} < \tfrac{1}{2}$ whenever $T \leq (\tfrac{1}{4\epsilon})^{2}$.

General case: For the analysis, we consider an additional problem instance $\mathcal{I}_{0} = \{\mu_{i} = \tfrac{1}{2} \text{ for all arms } i\}$, the "base instance". Let $\mathbb{E}_{0}[\cdot]$ be the expectation given this problem instance. Also, let $T_{a}$ be the total number of times arm $a$ is played.

We observe: There are $\geq \tfrac{2K}{3}$ arms $j$ such that $\mathbb{E}_{0}(T_{j}) \leq \tfrac{3T}{K}$; There are $\geq \tfrac{2K}{3}$ arms $j$ such that $P_{0}(y_{T} = j) \leq \tfrac{3}{K}$. (To prove the first, assume for contradiction that we have more than $\frac{K}{3}$ arms with $\mathbb{E}_{0}(T_{j}) > \frac{3T}{K}$. Then the expected total number of times these arms are played is strictly greater than $T$, contradiction. The second is proved similarly.) By Markov inequality, $\mathbb{E}_{0}(T_{j}) \leq \frac{3T}{K}$ implies that $\Pr[T_{j} \leq \frac{24T}{K}] \geq \nicefrac{7}{8}$.

Since the sets of arms in (25) and (26) must overlap on at least $\frac{K}{3}$ arms, we conclude: There are at least $\nicefrac{K}{3}$ arms $j$ such that $\Pr[T_{j} \leq \tfrac{24T}{K}] \geq \nicefrac{7}{8}$ and $P_{0}(y_{T} = j) \leq \nicefrac{3}{K}$.

Fix an arm $j$ satisfying the two properties. We prove $P_{j}[Y_{T} = j] \leq \nicefrac{1}{2}$. We consider a "reduced" sample space with arm $j$ played only $m = \min(T, 24T/K)$ times: $\Omega^{*} = \Omega_{j}^{m} \times \prod_{\text{arms } a \neq j} \Omega_{a}^{T}$. For each problem instance $\mathcal{I}_{\ell}$, we define distribution $P^{*}_{\ell}$ on $\Omega^{*}$ as a restriction of $P_{\ell}$ to the reduced sample space.

We apply the KL-divergence argument to distributions $P^{*}_{0}$ and $P^{*}_{j}$: $2(P_{0}^{*}(A) - P_{j}^{*}(A))^{2} \leq \mathtt{KL}(P_{0}^{*}, P_{j}^{*})$ (by Pinsker's inequality) $= \sum_{\text{arms } a} \sum_{t} \mathtt{KL}(P_{0}^{a,t}, P_{j}^{a,t}) = \sum_{\text{arms } a \neq j} \sum_{t=1}^{T} \mathtt{KL}(P_{0}^{a,t}, P_{j}^{a,t}) + \sum_{t=1}^{m} \mathtt{KL}(P_{0}^{j,t}, P_{j}^{j,t}) \leq 0 + m \cdot 2\epsilon^{2}$. The last inequality holds because each arm $a \neq j$ has identical reward distributions under $\mathcal{I}_{0}$ and $\mathcal{I}_{j}$, and for arm $j$ we only sum over $m$ samples.

Therefore, assuming $T \leq \frac{cK}{\epsilon^{2}}$ with small enough constant $c$, $|P_{0}^{*}(A) - P_{j}^{*}(A)| \leq \epsilon\sqrt{m} < \tfrac{1}{8}$ for all events $A \subset \Omega^{*}$.

We apply (30) to events $A = \{y_{T} = j \text{ and } T_{j} \leq m\}$ and $A' = \{T_{j} > m\}$. Note $A, A' \subset \Omega^{*}$. Then: $P_{j}(A) \leq \tfrac{1}{8} + P_{0}(A) \leq \tfrac{1}{8} + P_{0}(y_{T} = j) \leq \tfrac{1}{4}$ (by choice of arm $j$). $P_{j}(A') \leq \tfrac{1}{8} + P_{0}(A') \leq \tfrac{1}{4}$ (by choice of arm $j$). $P_{j}(Y_{T} = j) \leq P_{j}(Y_{T} = j \text{ and } T_{j} \leq m) + P_{j}(T_{j} > m) = P_{j}(A) + P_{j}(A') \leq \nicefrac{1}{2}$. This completes the proof.
