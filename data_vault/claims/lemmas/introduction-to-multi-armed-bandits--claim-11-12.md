---
slug: introduction-to-multi-armed-bandits--claim-11-12
label: Claim 11.12
claim_type: lemma
statement: Assume (163) holds for arm $\mathtt{rec}=2$. Then it also holds for $\mathtt{rec}=1$.
proof: If arm $2$ is never recommended, then the claim holds trivially since $\mu_{1}^{0}\geq\mu_{2}^{0}$.
  Now, suppose both arms are recommended with some positive probability. Then $0\geq\operatornamewithlimits{\mathbb{E}}[\mu_{2}-\mu_{1}]=\textstyle\sum_{a\in\{1,2\}}\;\operatornamewithlimits{\mathbb{E}}[\mu_{2}-\mu_{1}\mid\mathtt{rec}=a]\,\Pr[\mathtt{rec}=a].$
  Since $\operatornamewithlimits{\mathbb{E}}[\mu_{2}-\mu_{1}\mid\mathtt{rec}=2]>0$
  by the BIC assumption, $\operatornamewithlimits{\mathbb{E}}[\mu_{2}-\mu_{1}\mid\mathtt{rec}=1]<0$.
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/bic-property]]'
- '[[concepts/incentivized-exploration-bandit-problem]]'
- '[[concepts/prior-mean-mu-a-0]]'
about_meta:
- target: '[[concepts/bic-property]]'
  role: primary
  aspect: ''
- target: '[[concepts/incentivized-exploration-bandit-problem]]'
  role: primary
  aspect: ''
- target: '[[concepts/prior-mean-mu-a-0]]'
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

# Claim 11.12

Assume (163) holds for arm $\mathtt{rec}=2$. Then it also holds for $\mathtt{rec}=1$.


## Proof

If arm $2$ is never recommended, then the claim holds trivially since $\mu_{1}^{0}\geq\mu_{2}^{0}$. Now, suppose both arms are recommended with some positive probability. Then $0\geq\operatornamewithlimits{\mathbb{E}}[\mu_{2}-\mu_{1}]=\textstyle\sum_{a\in\{1,2\}}\;\operatornamewithlimits{\mathbb{E}}[\mu_{2}-\mu_{1}\mid\mathtt{rec}=a]\,\Pr[\mathtt{rec}=a].$ Since $\operatornamewithlimits{\mathbb{E}}[\mu_{2}-\mu_{1}\mid\mathtt{rec}=2]>0$ by the BIC assumption, $\operatornamewithlimits{\mathbb{E}}[\mu_{2}-\mu_{1}\mid\mathtt{rec}=1]<0$.
