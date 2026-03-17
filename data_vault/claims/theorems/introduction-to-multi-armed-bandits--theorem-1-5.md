---
slug: introduction-to-multi-armed-bandits--theorem-1-5
label: Theorem 1.5
claim_type: theorem
statement: Explore-first achieves regret $\operatornamewithlimits{\mathbb{E}}\left[\,R(T)\,\right]\leq
  T^{2/3}\times O(K\log T)^{1/3}$.
proof: 'For $K=2$ arms: Define the clean event as the event that $|\bar{\mu}(a)-\mu(a)|\leq\mathtt{rad}$
  holds for all arms simultaneously, where $\mathtt{rad}:=\sqrt{2\log(T)/N}$. Consider
  the clean event. Let the best arm be $a^{*}$, and suppose the algorithm chooses
  the other arm $a\neq a^{*}$. This must have been because its average reward was
  better than that of $a^{*}$: $\bar{\mu}(a)>\bar{\mu}(a^{*})$. Since this is a clean
  event, we have: $\mu(a)+\mathtt{rad}\geq\bar{\mu}(a)>\bar{\mu}(a^{*})\geq\mu(a^{*})-\mathtt{rad}$.
  Re-arranging the terms, it follows that $\mu(a^{*})-\mu(a)\leq 2\,\mathtt{rad}$.
  Thus, each round in the exploitation phase contributes at most $2\,\mathtt{rad}$
  to regret. Each round in exploration trivially contributes at most $1$. We derive
  an upper bound on the regret: $R(T)\leq N+2\,\mathtt{rad}\cdot(T-2N)<N+2\,\mathtt{rad}\cdot
  T$. We choose $N=T^{2/3}\,(\log T)^{1/3}$, so the two summands are approximately
  equal, obtaining $R(T)\leq O\left(T^{2/3}\;(\log T)^{1/3}\right)$. For the bad event:
  Since regret can be at most $T$ and the bad event happens with very small probability,
  $\operatornamewithlimits{\mathbb{E}}\left[\,R(T)\,\right]=\operatornamewithlimits{\mathbb{E}}\left[\,R(T)\mid\text{clean
  event}\,\right]\times\Pr\left[\,\text{clean event}\,\right]+\operatornamewithlimits{\mathbb{E}}\left[\,R(T)\mid\text{bad
  event}\,\right]\times\Pr\left[\,\text{bad event}\,\right]\leq\operatornamewithlimits{\mathbb{E}}\left[\,R(T)\mid\text{clean
  event}\,\right]+T\times O\left(\,T^{-4}\,\right)\leq O\left(\,(\log T)^{1/3}\times
  T^{2/3}\,\right)$. For $K>2$ arms: Apply the union bound for the confidence inequality
  over the $K$ arms, and follow the same argument. Regret accumulated in exploration
  phase is now upper-bounded by $KN$. Working through the proof, we obtain $R(T)\leq
  NK+2\,\mathtt{rad}\cdot T$. We plug in $N=(T/K)^{2/3}\cdot O(\log T)^{1/3}$ and
  complete the proof the same way.'
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/bad-event]]'
- '[[concepts/number-of-arms-k]]'
- '[[concepts/expected-regret-e-r-t]]'
- '[[concepts/non-adaptive-exploration]]'
- '[[concepts/bounded-rewards]]'
- '[[concepts/confidence-radius]]'
- '[[concepts/explore-first-algorithm]]'
- '[[concepts/stochastic-bandits-problem]]'
- '[[concepts/hoeffding-inequality]]'
- '[[concepts/time-horizon-t]]'
- '[[concepts/clean-event]]'
about_meta:
- target: '[[concepts/bad-event]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-arms-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/expected-regret-e-r-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/non-adaptive-exploration]]'
  role: primary
  aspect: ''
- target: '[[concepts/bounded-rewards]]'
  role: primary
  aspect: ''
- target: '[[concepts/confidence-radius]]'
  role: primary
  aspect: ''
- target: '[[concepts/explore-first-algorithm]]'
  role: primary
  aspect: ''
- target: '[[concepts/stochastic-bandits-problem]]'
  role: primary
  aspect: ''
- target: '[[concepts/hoeffding-inequality]]'
  role: primary
  aspect: ''
- target: '[[concepts/time-horizon-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/clean-event]]'
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

# Theorem 1.5

Explore-first achieves regret $\operatornamewithlimits{\mathbb{E}}\left[\,R(T)\,\right]\leq T^{2/3}\times O(K\log T)^{1/3}$.


## Proof

For $K=2$ arms: Define the clean event as the event that $|\bar{\mu}(a)-\mu(a)|\leq\mathtt{rad}$ holds for all arms simultaneously, where $\mathtt{rad}:=\sqrt{2\log(T)/N}$. Consider the clean event. Let the best arm be $a^{*}$, and suppose the algorithm chooses the other arm $a\neq a^{*}$. This must have been because its average reward was better than that of $a^{*}$: $\bar{\mu}(a)>\bar{\mu}(a^{*})$. Since this is a clean event, we have: $\mu(a)+\mathtt{rad}\geq\bar{\mu}(a)>\bar{\mu}(a^{*})\geq\mu(a^{*})-\mathtt{rad}$. Re-arranging the terms, it follows that $\mu(a^{*})-\mu(a)\leq 2\,\mathtt{rad}$. Thus, each round in the exploitation phase contributes at most $2\,\mathtt{rad}$ to regret. Each round in exploration trivially contributes at most $1$. We derive an upper bound on the regret: $R(T)\leq N+2\,\mathtt{rad}\cdot(T-2N)<N+2\,\mathtt{rad}\cdot T$. We choose $N=T^{2/3}\,(\log T)^{1/3}$, so the two summands are approximately equal, obtaining $R(T)\leq O\left(T^{2/3}\;(\log T)^{1/3}\right)$. For the bad event: Since regret can be at most $T$ and the bad event happens with very small probability, $\operatornamewithlimits{\mathbb{E}}\left[\,R(T)\,\right]=\operatornamewithlimits{\mathbb{E}}\left[\,R(T)\mid\text{clean event}\,\right]\times\Pr\left[\,\text{clean event}\,\right]+\operatornamewithlimits{\mathbb{E}}\left[\,R(T)\mid\text{bad event}\,\right]\times\Pr\left[\,\text{bad event}\,\right]\leq\operatornamewithlimits{\mathbb{E}}\left[\,R(T)\mid\text{clean event}\,\right]+T\times O\left(\,T^{-4}\,\right)\leq O\left(\,(\log T)^{1/3}\times T^{2/3}\,\right)$. For $K>2$ arms: Apply the union bound for the confidence inequality over the $K$ arms, and follow the same argument. Regret accumulated in exploration phase is now upper-bounded by $KN$. Working through the proof, we obtain $R(T)\leq NK+2\,\mathtt{rad}\cdot T$. We plug in $N=(T/K)^{2/3}\cdot O(\log T)^{1/3}$ and complete the proof the same way.
