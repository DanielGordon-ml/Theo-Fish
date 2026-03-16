---
type: theorem
label: Theorem 3
paper: 'Combinatorial Network Optimization with Unknown Variables: Multi-Armed Bandits
  with Linear Rewards'
arxiv_id: '1011.4748'
section: VIII. K SIMULTANEOUS ACTIONS
related_entities:
- '[[Algorithm 3]]'
date_extracted: '2026-03-15T22:56:42.979122+00:00'
---

# Theorem 3

The expected regret under the LLR-K policy with $K$ arms selection is at most

$$
\left[ \frac { 4 a _ { \mathrm { m a x } } ^ { 2 } L ^ { 2 } ( L + 1 ) N \ln n } { \left( \Delta _ { \mathrm { m i n } } \right) ^ { 2 } } + N + \frac { \pi ^ { 2 } } { 3 } L K ^ { 2 L } N \right] \Delta _ { \mathrm { m a x } } .
$$

## Proof

The proof is similar to the proof of Theorem 2, but now we have a set of $K$ arms with $K$ largest expected rewards as the optimal arms. We denote this set as $\mathfrak { A } ^ { * } = \{ \mathbf { a } ^ { * , k } , 1 \leq k \leq K \}$ where $\mathbf { a } ^ { * , k }$ is the arm with $k$ -th largest expected reward. As in the proof of Theorem 2, we define $\widetilde { T } _ { i } ( n )$ as a counter when a non-optimal arm is played in the same way. Equation (9), (10), (11) and (13) still hold.

Note that each time when $\widetilde { I } _ { i } ( t ) = 1$ , there exists some arm such that a non-optimal arm is picked for which $m _ { i }$ is the minimum in this arm. We denote this arm as ${ \bf a } ( t )$ . Note that ${ \bf a } ( t )$ means there exists $m$ $, 1 \leq m \leq K$ , such that the following holds:

$$
\begin{array} { r l r } & { } & { \widetilde { T } _ { i } ( n ) \le l + \displaystyle \sum _ { t = N } ^ { n } \{ \displaystyle \sum _ { j \in \mathcal { A } _ { \mathtt { a } ^ { * } } , m } a _ { j } ^ { * , m } ( \hat { \overline { { \theta } } } _ { j , m _ { j } ( t ) } + C _ { t , m _ { j } ( t ) } ) } \\ & { } & { \qquad \le \displaystyle \sum _ { j \in \mathcal { A } _ { \mathtt { a } ( t ) } } a _ { j } ( t ) ( \hat { \overline { { \theta } } } _ { j , m _ { j } ( t ) } + C _ { t , m _ { j } ( t ) } ) , \widetilde { T } _ { i } ( t ) \ge l \} . } \end{array}
$$

Since at each time $K$ arms are played, so at time $t _ { : }$ , an random variable could be observed up to $K t$ times. Then (14) should be modified as:

$$
\begin{array} { r l } & { \widetilde { T } _ { i } ( n ) \le l + \displaystyle \sum _ { t = 1 } ^ { \infty } \displaystyle \sum _ { m _ { h _ { 1 } } = 1 } ^ { K t } \cdots \cdot \sum _ { \substack { m _ { h _ { 1 } | A ^ { * } } , m _ { 1 } = 1 } } ^ { K t } \displaystyle \sum _ { m _ { p _ { 1 } } = l } ^ { K t } \cdots \sum _ { \substack { m _ { p _ { 1 } | A _ { a ( t ) } | } = l } } ^ { K t } = l } \\ & { \qquad \{ \displaystyle \sum _ { j = 1 } ^ { | A _ { a ^ { * } } , m | } a _ { h _ { j } } ^ { * , m } ( \widehat { \tilde { \theta } } _ { h _ { j } , m _ { h _ { j } } } + C _ { t , m _ { h _ { j } } } ) } \\ & { \qquad \le \displaystyle \sum _ { j = 1 } ^ { | A _ { a ( t ) } | } a _ { p _ { j } } ( t ) ( \widehat { \tilde { \theta } } _ { p _ { j } , m _ { p _ { j } } } + C _ { t , m _ { p _ { j } } } ) \} . } \end{array}
$$

Equation (15) to (20) are similar by substituting $\mathbf { a } ^ { * }$ with $\mathbf { a } ^ { * , m }$ . So, we have:

$$
\begin{array} { r l } & { \mathbb { E } [ \widetilde { T } _ { i } ( n ) ] \le \left\lceil \frac { 4 ( L + 1 ) \ln n } { \left( \frac { \Delta _ { \operatorname* { m i n } } } { L o _ { \operatorname* { m a x } } } \right) ^ { 2 } } \right\rceil } \\ & { + \displaystyle \sum _ { t = 1 } ^ { \infty } \left( \sum _ { m _ { h _ { 1 } } = 1 } ^ { K t } \cdots \sum _ { \substack { m _ { h _ { 1 } , 4 ^ { * } } = 1 } } ^ { K t } \sum _ { m _ { p _ { 1 } } = l } ^ { K t } \cdots \sum _ { \substack { m _ { p _ { 1 } | \mathcal { A } _ { \ O ( t ) } | } = l } } ^ { K t } 2 L t ^ { - 2 ( L + 1 ) } \right) } \\ & { \le \frac { 4 a _ { \operatorname* { m a x } } ^ { 2 } L ^ { 2 } ( L + 1 ) \ln n } { ( \Delta _ { \operatorname* { m i n } } ) ^ { 2 } } + 1 + \frac { \pi ^ { 2 } } { 3 } L K ^ { 2 L } . } \end{array}
$$

Hence, we get the upper bound for the regret as:

$$
\mathfrak { R } _ { n } ^ { \pi } ( \Theta ) \leq \left[ \frac { 4 a _ { \operatorname* { m a x } } ^ { 2 } L ^ { 2 } ( L + 1 ) N \ln n } { \left( \Delta _ { \operatorname* { m i n } } \right) ^ { 2 } } + N + \frac { \pi ^ { 2 } } { 3 } L K ^ { 2 L } N \right] \Delta _ { \operatorname* { m a x } } .
$$

## Relationships

- **Uses:** [[Algorithm 3]]

## References

- Paper: [[index|Combinatorial Network Optimization with Unknown Variables: Multi-Armed Bandits with Linear Rewards]]
- Section: VIII. K SIMULTANEOUS ACTIONS
