---
type: exercise
label: Exercise 6.1 (lower bound) .
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 36 Exercises and hints
related_entities: []
date_extracted: '2026-03-16T01:32:59.516870+00:00'
---

# Exercise 6.1 (lower bound) .

Consider adversarial bandits with experts advice. Prove the lower bound in (87) for any given $(K,N,T)$. More precisely: construct a randomized problem instance for which any algorithm satisfies (87).
Hint: Split the time interval $1..T$ into $M=\tfrac{\ln N}{\ln K}$ non-overlapping sub-intervals of duration $T/M$ . For each sub-interval, construct the randomized problem instance from Chapter\xa02 (independently across the sub-intervals). Each expert recommends the same arm within any given sub-interval; the set of experts includes all experts of this form.

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 36 Exercises and hints
