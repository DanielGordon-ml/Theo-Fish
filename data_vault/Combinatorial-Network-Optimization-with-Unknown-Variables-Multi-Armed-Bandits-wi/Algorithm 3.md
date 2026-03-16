---
type: algorithm
label: Algorithm 3
paper: 'Combinatorial Network Optimization with Unknown Variables: Multi-Armed Bandits
  with Linear Rewards'
arxiv_id: '1011.4748'
section: VIII. K SIMULTANEOUS ACTIONS
related_entities:
- '[[Algorithm 1]]'
- '[[Theorem 3]]'
date_extracted: '2026-03-15T22:56:42.975600+00:00'
---

# Algorithm 3

1: // INITIALIZATION PART IS SAME AS IN ALGORITHM 1
2: // MAIN LOOP

5: Play arms $\{ { \bf a } \} _ { K } \in \mathcal { F }$ with $K$ largest values in (38)

$$
\sum _ { i \in \mathcal { A } _ { \mathbf { a } } } a _ { i } \left( \hat { \theta } _ { i } + \sqrt { \frac { \left( L + 1 \right) \ln n } { m _ { i } } } \right) ;
$$

6: Update $( \hat { \theta } _ { i } ) _ { 1 \times N } , ( m _ { i } ) _ { 1 \times N }$ for all arms accordingly;
7: end while

## Relationships

- **Extends:** [[Algorithm 1]]
- **Uses (inverse):** [[Theorem 3]]

## References

- Paper: [[index|Combinatorial Network Optimization with Unknown Variables: Multi-Armed Bandits with Linear Rewards]]
- Section: VIII. K SIMULTANEOUS ACTIONS
