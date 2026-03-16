---
type: algorithm
label: Algorithm 1
paper: 'Combinatorial Network Optimization with Unknown Variables: Multi-Armed Bandits
  with Linear Rewards'
arxiv_id: '1011.4748'
section: Algorithm 1 Learning with Linear Rewards (LLR)
related_entities:
- '[[Algorithm 2]]'
- '[[Algorithm 3]]'
date_extracted: '2026-03-15T22:56:42.920547+00:00'
---

# Algorithm 1

1: // INITIALIZATION
2: If max $\lvert \mathcal { A } _ { \bf a } \rvert$ is known, let $L = \operatorname* { m a x } _ { \mathbf { a } } \left| \mathcal { A } _ { \mathbf { a } } \right|$ ; else, $L = N$ ;
3: for $\overset { \mathbf { a } } { p } = 1$ to $N$ do
4: $n = p$ ;
5: Play any arm a such that $p \in { \mathcal { A } } _ { \mathbf { a } }$ ;
6: Update $\left( { \hat { \theta } } _ { i } \right) _ { 1 \times N }$ , $( m _ { i } ) _ { 1 \times N }$ accordingly;
7: end for
8: // MAIN LOOP
9: while 1 do
10: $n = n + 1$ ;
11: Play an arm a which solves the maximization problem
$\mathbf { a } = \arg \operatorname* { m a x } _ { \mathbf { a } \in \mathcal { F } } \sum _ { i \in \mathcal { A } _ { \mathbf { a } } } a _ { i } \left( \hat { \theta } _ { i } + \sqrt { \frac { \left( L + 1 \right) \ln n } { m _ { i } } } \right) ;$
12: Update $( \hat { \theta } _ { i } ) _ { 1 \times N } , ( m _ { i } ) _ { 1 \times N }$ accordingly;

## Relationships

- **Extends (inverse):** [[Algorithm 2]]
- **Extends (inverse):** [[Algorithm 3]]

## References

- Paper: [[index|Combinatorial Network Optimization with Unknown Variables: Multi-Armed Bandits with Linear Rewards]]
- Section: Algorithm 1 Learning with Linear Rewards (LLR)
