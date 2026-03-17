---
slug: introduction-to-multi-armed-bandits--lemma-13-4-random-coins-theorem-2-4-d
label: Lemma 13.4 (Random coins, Theorem 2.4 (d))
claim_type: lemma
statement: Fix $\epsilon\in(0,\tfrac{1}{2})$. Let $\mathtt{RC}_{\epsilon}$ denote
  a random coin with bias $\tfrac{\epsilon}{2}$, i.e., a distribution over $\{0,1\}$
  with expectation $(1+\epsilon)/2$. Then $\mathtt{KL}(\mathtt{RC}_{\epsilon},\mathtt{RC}_{0})\leq
  2\epsilon^{2}$ and $\mathtt{KL}(\mathtt{RC}_{0},\mathtt{RC}_{\epsilon})\leq\epsilon^{2}$.
proof: '$\mathtt{KL}(\mathtt{RC}_{0},\mathtt{RC}_{\epsilon}) = \tfrac{1}{2}\,\ln(\tfrac{1}{1+\epsilon})+\tfrac{1}{2}\,\ln(\tfrac{1}{1-\epsilon})=-\tfrac{1}{2}\,\ln(1-\epsilon^{2})
  \leq-\tfrac{1}{2}\,(-2\epsilon^{2})$ (as $\log(1-\epsilon^{2})\geq-2\epsilon^{2}$
  whenever $\epsilon^{2}\leq\tfrac{1}{2}$) $=\epsilon^{2}.$


  $\mathtt{KL}(\mathtt{RC}_{\epsilon},\mathtt{RC}_{0}) = \tfrac{1+\epsilon}{2}\ln(1+\epsilon)+\tfrac{1-\epsilon}{2}\ln(1-\epsilon)
  = \tfrac{1}{2}\left(\ln(1+\epsilon)+\ln(1-\epsilon)\right)+\tfrac{\epsilon}{2}\left(\ln(1+\epsilon)-\ln(1-\epsilon)\right)
  = \tfrac{1}{2}\ln(1-\epsilon^{2})+\tfrac{\epsilon}{2}\ln\tfrac{1+\epsilon}{1-\epsilon}.$


  Now, $\ln(1-\epsilon^{2})<0$ and we can write $\ln\tfrac{1+\epsilon}{1-\epsilon}=\ln\left(1+\tfrac{2\epsilon}{1-\epsilon}\right)\leq\tfrac{2\epsilon}{1-\epsilon}$.
  Thus, we get:


  $\mathtt{KL}(\mathtt{RC}_{\epsilon},\mathtt{RC}_{0})<\tfrac{\epsilon}{2}\cdot\tfrac{2\epsilon}{1-\epsilon}=\tfrac{\epsilon^{2}}{1-\epsilon}\leq
  2\epsilon^{2}.$'
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/kl-divergence]]'
- '[[concepts/random-coin-rc-epsilon]]'
- '[[concepts/biased-coin-distribution]]'
about_meta:
- target: '[[concepts/kl-divergence]]'
  role: primary
  aspect: ''
- target: '[[concepts/random-coin-rc-epsilon]]'
  role: primary
  aspect: ''
- target: '[[concepts/biased-coin-distribution]]'
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

# Lemma 13.4 (Random coins, Theorem 2.4 (d))

Fix $\epsilon\in(0,\tfrac{1}{2})$. Let $\mathtt{RC}_{\epsilon}$ denote a random coin with bias $\tfrac{\epsilon}{2}$, i.e., a distribution over $\{0,1\}$ with expectation $(1+\epsilon)/2$. Then $\mathtt{KL}(\mathtt{RC}_{\epsilon},\mathtt{RC}_{0})\leq 2\epsilon^{2}$ and $\mathtt{KL}(\mathtt{RC}_{0},\mathtt{RC}_{\epsilon})\leq\epsilon^{2}$.


## Proof

$\mathtt{KL}(\mathtt{RC}_{0},\mathtt{RC}_{\epsilon}) = \tfrac{1}{2}\,\ln(\tfrac{1}{1+\epsilon})+\tfrac{1}{2}\,\ln(\tfrac{1}{1-\epsilon})=-\tfrac{1}{2}\,\ln(1-\epsilon^{2}) \leq-\tfrac{1}{2}\,(-2\epsilon^{2})$ (as $\log(1-\epsilon^{2})\geq-2\epsilon^{2}$ whenever $\epsilon^{2}\leq\tfrac{1}{2}$) $=\epsilon^{2}.$

$\mathtt{KL}(\mathtt{RC}_{\epsilon},\mathtt{RC}_{0}) = \tfrac{1+\epsilon}{2}\ln(1+\epsilon)+\tfrac{1-\epsilon}{2}\ln(1-\epsilon) = \tfrac{1}{2}\left(\ln(1+\epsilon)+\ln(1-\epsilon)\right)+\tfrac{\epsilon}{2}\left(\ln(1+\epsilon)-\ln(1-\epsilon)\right) = \tfrac{1}{2}\ln(1-\epsilon^{2})+\tfrac{\epsilon}{2}\ln\tfrac{1+\epsilon}{1-\epsilon}.$

Now, $\ln(1-\epsilon^{2})<0$ and we can write $\ln\tfrac{1+\epsilon}{1-\epsilon}=\ln\left(1+\tfrac{2\epsilon}{1-\epsilon}\right)\leq\tfrac{2\epsilon}{1-\epsilon}$. Thus, we get:

$\mathtt{KL}(\mathtt{RC}_{\epsilon},\mathtt{RC}_{0})<\tfrac{\epsilon}{2}\cdot\tfrac{2\epsilon}{1-\epsilon}=\tfrac{\epsilon^{2}}{1-\epsilon}\leq 2\epsilon^{2}.$
