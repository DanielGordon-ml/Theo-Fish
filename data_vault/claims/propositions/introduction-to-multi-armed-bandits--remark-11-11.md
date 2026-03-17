---
slug: introduction-to-multi-armed-bandits--remark-11-11
label: Remark 11.11
claim_type: proposition
statement: A suitable $\epsilon>0$ exists (for Lemma 11.10) if and only if $\Pr[G>0]>0$.
  Indeed, if $\Pr[G>0]>0$ then $\Pr[G>\delta]=\delta^{\prime}>0$ for some $\delta>0$,
  so $\operatornamewithlimits{\mathbb{E}}\left[G\cdot{\bf 1}_{\left\{\,G>0\,\right\}}\right]\geq\operatornamewithlimits{\mathbb{E}}\left[G\cdot{\bf
  1}_{\left\{\,G>\delta\,\right\}}\right]=\Pr[G>\delta]\cdot\operatornamewithlimits{\mathbb{E}}[G\mid
  G>\delta]\geq\delta\cdot\delta^{\prime}>0.$
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/exploration-probability-epsilon]]'
- '[[concepts/bic-property]]'
- '[[concepts/posterior-gap]]'
about_meta:
- target: '[[concepts/exploration-probability-epsilon]]'
  role: primary
  aspect: ''
- target: '[[concepts/bic-property]]'
  role: primary
  aspect: ''
- target: '[[concepts/posterior-gap]]'
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

# Remark 11.11

A suitable $\epsilon>0$ exists (for Lemma 11.10) if and only if $\Pr[G>0]>0$. Indeed, if $\Pr[G>0]>0$ then $\Pr[G>\delta]=\delta^{\prime}>0$ for some $\delta>0$, so $\operatornamewithlimits{\mathbb{E}}\left[G\cdot{\bf 1}_{\left\{\,G>0\,\right\}}\right]\geq\operatornamewithlimits{\mathbb{E}}\left[G\cdot{\bf 1}_{\left\{\,G>\delta\,\right\}}\right]=\Pr[G>\delta]\cdot\operatornamewithlimits{\mathbb{E}}[G\mid G>\delta]\geq\delta\cdot\delta^{\prime}>0.$
