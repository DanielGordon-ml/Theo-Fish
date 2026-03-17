---
slug: introduction-to-multi-armed-bandits--lemma-11-10
label: Lemma 11.10
claim_type: lemma
statement: Algorithm 1 (HiddenExploration) is BIC, for any target function $a_{\mathtt{trg}}$,
  as long as $\epsilon\leq\tfrac{1}{3}\,\operatornamewithlimits{\mathbb{E}}\left[G\cdot{\bf
  1}_{\left\{\,G>0\,\right\}}\right]$.
proof: 'We start with Claim 11.12 which shows it suffices to prove the BIC property
  for $\mathtt{rec}=2$, i.e., that $\operatornamewithlimits{\mathbb{E}}\left[\,\mu_{2}-\mu_{1}\mid\mathtt{rec}=2\,\right]>0$.
  Denote the event $\{\mathtt{rec}=2\}$ with $\mathcal{E}_{2}$. By Fact 11.6, $\operatornamewithlimits{\mathbb{E}}\left[\,\mu_{2}-\mu_{1}\mid\mathcal{E}_{2}\,\right]=\operatornamewithlimits{\mathbb{E}}[G\mid\mathcal{E}_{2}]$.
  We work with $F(\mathcal{E}):=\operatornamewithlimits{\mathbb{E}}\left[\,G\cdot{\bf
  1}_{\mathcal{E}}\,\right]$. Proving (164) is equivalent to proving $F(\mathcal{E}_{2})>0$.
  We use that $F(\mathcal{E}\cup\mathcal{E}^{\prime})=F(\mathcal{E})+F(\mathcal{E}^{\prime})$
  for disjoint events. Letting $\mathcal{E}_{\mathtt{explore}}$ and $\mathcal{E}_{\mathtt{exploit}}$
  be the events of choosing exploration and exploitation branches respectively, $F(\mathcal{E}_{2})=F(\mathcal{E}_{\mathtt{explore}}\text{
  and }\mathcal{E}_{2})+F(\mathcal{E}_{\mathtt{exploit}}\text{ and }\mathcal{E}_{2})$.
  For the exploitation branch, $\{\mathcal{E}_{\mathtt{exploit}}\text{ and }\mathcal{E}_{2}\}$
  and $\{\mathcal{E}_{\mathtt{exploit}}\text{ and }G>0\}$ are the same by the algorithm''s
  specification, so $F(\mathcal{E}_{\mathtt{exploit}}\text{ and }\mathcal{E}_{2})=F(\mathcal{E}_{\mathtt{exploit}}\text{
  and }G>0)=\operatornamewithlimits{\mathbb{E}}[G\mid G>0]\cdot\Pr[G>0]\cdot(1-\epsilon)=(1-\epsilon)\cdot
  F(G>0)$ by independence. For the exploration branch, $F(\mathcal{E}_{\mathtt{explore}}\text{
  and }\mathcal{E}_{2})=F(\mathcal{E}_{\mathtt{explore}}\text{ and }\mathcal{E}_{2}\text{
  and }G<0)+F(\mathcal{E}_{\mathtt{explore}}\text{ and }\mathcal{E}_{2}\text{ and
  }G\geq 0)\geq F(\mathcal{E}_{\mathtt{explore}}\text{ and }\mathcal{E}_{2}\text{
  and }G<0)=F(\mathcal{E}_{\mathtt{explore}}\text{ and }G<0)-F(\mathcal{E}_{\mathtt{explore}}\text{
  and }\neg\mathcal{E}_{2}\text{ and }G<0)\geq F(\mathcal{E}_{\mathtt{explore}}\text{
  and }G<0)=\operatornamewithlimits{\mathbb{E}}[G\mid G<0]\cdot\Pr[G<0]\cdot\epsilon=\epsilon\cdot
  F(G<0)$ by independence. Putting together: $F(\mathcal{E}_{2})\geq\epsilon\cdot
  F(G<0)+(1-\epsilon)\cdot F(G>0)$. Now $F(G<0)+F(G>0)=\operatornamewithlimits{\mathbb{E}}[\mu_{2}-\mu_{1}]$.
  Plugging back and rearranging, $F(\mathcal{E}_{2})>0$ whenever $F(G>0)>\epsilon\left(\,2F(G>0)+\operatornamewithlimits{\mathbb{E}}[\mu_{1}-\mu_{2}]\,\right)$.
  In particular, $\epsilon<\tfrac{1}{3}\cdot F(G>0)$ suffices.'
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/hiddenexploration]]'
- '[[concepts/bic-property]]'
- '[[concepts/exploration-probability-epsilon]]'
- '[[concepts/posterior-gap]]'
- '[[concepts/incentivized-exploration-bandit-problem]]'
about_meta:
- target: '[[concepts/hiddenexploration]]'
  role: primary
  aspect: ''
- target: '[[concepts/bic-property]]'
  role: primary
  aspect: ''
- target: '[[concepts/exploration-probability-epsilon]]'
  role: primary
  aspect: ''
- target: '[[concepts/posterior-gap]]'
  role: primary
  aspect: ''
- target: '[[concepts/incentivized-exploration-bandit-problem]]'
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

# Lemma 11.10

Algorithm 1 (HiddenExploration) is BIC, for any target function $a_{\mathtt{trg}}$, as long as $\epsilon\leq\tfrac{1}{3}\,\operatornamewithlimits{\mathbb{E}}\left[G\cdot{\bf 1}_{\left\{\,G>0\,\right\}}\right]$.


## Proof

We start with Claim 11.12 which shows it suffices to prove the BIC property for $\mathtt{rec}=2$, i.e., that $\operatornamewithlimits{\mathbb{E}}\left[\,\mu_{2}-\mu_{1}\mid\mathtt{rec}=2\,\right]>0$. Denote the event $\{\mathtt{rec}=2\}$ with $\mathcal{E}_{2}$. By Fact 11.6, $\operatornamewithlimits{\mathbb{E}}\left[\,\mu_{2}-\mu_{1}\mid\mathcal{E}_{2}\,\right]=\operatornamewithlimits{\mathbb{E}}[G\mid\mathcal{E}_{2}]$. We work with $F(\mathcal{E}):=\operatornamewithlimits{\mathbb{E}}\left[\,G\cdot{\bf 1}_{\mathcal{E}}\,\right]$. Proving (164) is equivalent to proving $F(\mathcal{E}_{2})>0$. We use that $F(\mathcal{E}\cup\mathcal{E}^{\prime})=F(\mathcal{E})+F(\mathcal{E}^{\prime})$ for disjoint events. Letting $\mathcal{E}_{\mathtt{explore}}$ and $\mathcal{E}_{\mathtt{exploit}}$ be the events of choosing exploration and exploitation branches respectively, $F(\mathcal{E}_{2})=F(\mathcal{E}_{\mathtt{explore}}\text{ and }\mathcal{E}_{2})+F(\mathcal{E}_{\mathtt{exploit}}\text{ and }\mathcal{E}_{2})$. For the exploitation branch, $\{\mathcal{E}_{\mathtt{exploit}}\text{ and }\mathcal{E}_{2}\}$ and $\{\mathcal{E}_{\mathtt{exploit}}\text{ and }G>0\}$ are the same by the algorithm's specification, so $F(\mathcal{E}_{\mathtt{exploit}}\text{ and }\mathcal{E}_{2})=F(\mathcal{E}_{\mathtt{exploit}}\text{ and }G>0)=\operatornamewithlimits{\mathbb{E}}[G\mid G>0]\cdot\Pr[G>0]\cdot(1-\epsilon)=(1-\epsilon)\cdot F(G>0)$ by independence. For the exploration branch, $F(\mathcal{E}_{\mathtt{explore}}\text{ and }\mathcal{E}_{2})=F(\mathcal{E}_{\mathtt{explore}}\text{ and }\mathcal{E}_{2}\text{ and }G<0)+F(\mathcal{E}_{\mathtt{explore}}\text{ and }\mathcal{E}_{2}\text{ and }G\geq 0)\geq F(\mathcal{E}_{\mathtt{explore}}\text{ and }\mathcal{E}_{2}\text{ and }G<0)=F(\mathcal{E}_{\mathtt{explore}}\text{ and }G<0)-F(\mathcal{E}_{\mathtt{explore}}\text{ and }\neg\mathcal{E}_{2}\text{ and }G<0)\geq F(\mathcal{E}_{\mathtt{explore}}\text{ and }G<0)=\operatornamewithlimits{\mathbb{E}}[G\mid G<0]\cdot\Pr[G<0]\cdot\epsilon=\epsilon\cdot F(G<0)$ by independence. Putting together: $F(\mathcal{E}_{2})\geq\epsilon\cdot F(G<0)+(1-\epsilon)\cdot F(G>0)$. Now $F(G<0)+F(G>0)=\operatornamewithlimits{\mathbb{E}}[\mu_{2}-\mu_{1}]$. Plugging back and rearranging, $F(\mathcal{E}_{2})>0$ whenever $F(G>0)>\epsilon\left(\,2F(G>0)+\operatornamewithlimits{\mathbb{E}}[\mu_{1}-\mu_{2}]\,\right)$. In particular, $\epsilon<\tfrac{1}{3}\cdot F(G>0)$ suffices.
