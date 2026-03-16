---
type: remark
label: Remark 11.11
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: '63 Basic technique: hidden exploration'
related_entities: []
date_extracted: '2026-03-16T01:32:59.559993+00:00'
---

# Remark 11.11

A suitable $\epsilon>0$ exists if and only if $\Pr[G>0]>0$. Indeed, if $\Pr[G>0]>0$ then $\Pr[G>\delta]=\delta^{\prime}>0$ for some $\delta>0$, so $$ \operatornamewithlimits{\mathbb{E}}\left[G\cdot{\bf 1}_{\left\{\,G>0\,\right\}}\right]\geq\operatornamewithlimits{\mathbb{E}}\left[G\cdot{\bf 1}_{\left\{\,G>\delta\,\right\}}\right]=\Pr[G>\delta]\cdot\operatornamewithlimits{\mathbb{E}}[G\mid G>\delta]\geq\delta\cdot\delta^{\prime}>0. $$

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 63 Basic technique: hidden exploration
