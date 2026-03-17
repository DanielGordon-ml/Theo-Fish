---
slug: introduction-to-multi-armed-bandits--lemma-13-2-chain-rule-for-product-distributions-theorem-2-4-b
label: Lemma 13.2 (Chain rule for product distributions, Theorem 2.4 (b))
claim_type: lemma
statement: Let the sample space be a product $\Omega=\Omega_{1}\times\Omega_{1}\times\dots\times\Omega_{n}$.
  Let $p$ and $q$ be two distributions on $\Omega$ such that $p=p_{1}\times p_{2}\times\dots\times
  p_{n}$ and $q=q_{1}\times q_{2}\times\dots\times q_{n}$, where $p_{j},q_{j}$ are
  distributions on $\Omega_{j}$, for each $j\in[n]$. Then $\mathtt{KL}(p,q)=\sum_{j=1}^{n}\mathtt{KL}(p_{j},q_{j})$.
proof: 'Let $x=(x_{1},x_{2},\dots,x_{n})\in\Omega$ such that $x_{i}\in\Omega_{i}$
  for all $i=1,\ldots,n$. Let $h_{i}(x_{i})=\ln\frac{p_{i}(x_{i})}{q_{i}(x_{i})}$.
  Then:


  $\mathtt{KL}(p,q) = \sum_{x\in\Omega}p(x)\ln\frac{p(x)}{q(x)} = \sum_{i=1}^{n}\sum_{x\in\Omega}p(x)h_{i}(x_{i})$
  [since $\ln\frac{p(x)}{q(x)}=\sum_{i=1}^{n}h_{i}(x_{i})$] $= \sum_{i=1}^{n}\sum_{x^{\star}_{i}\in\Omega_{i}}h_{i}(x_{i}^{\star})\sum_{\substack{x\in\Omega,\\
  x_{i}=x_{i}^{\star}}}p(x) = \sum_{i=1}^{n}\sum_{x_{i}\in\Omega_{i}}p_{i}(x_{i})h_{i}(x_{i})$
  [since $\sum_{x\in\Omega,\ x_{i}=x_{i}^{\star}}p(x)=p_{i}(x_{i}^{\star})$] $= \sum_{i=1}^{n}\mathtt{KL}(p_{i},q_{i}).$'
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/kl-divergence]]'
- '[[concepts/product-probability-distribution]]'
about_meta:
- target: '[[concepts/kl-divergence]]'
  role: primary
  aspect: ''
- target: '[[concepts/product-probability-distribution]]'
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

# Lemma 13.2 (Chain rule for product distributions, Theorem 2.4 (b))

Let the sample space be a product $\Omega=\Omega_{1}\times\Omega_{1}\times\dots\times\Omega_{n}$. Let $p$ and $q$ be two distributions on $\Omega$ such that $p=p_{1}\times p_{2}\times\dots\times p_{n}$ and $q=q_{1}\times q_{2}\times\dots\times q_{n}$, where $p_{j},q_{j}$ are distributions on $\Omega_{j}$, for each $j\in[n]$. Then $\mathtt{KL}(p,q)=\sum_{j=1}^{n}\mathtt{KL}(p_{j},q_{j})$.


## Proof

Let $x=(x_{1},x_{2},\dots,x_{n})\in\Omega$ such that $x_{i}\in\Omega_{i}$ for all $i=1,\ldots,n$. Let $h_{i}(x_{i})=\ln\frac{p_{i}(x_{i})}{q_{i}(x_{i})}$. Then:

$\mathtt{KL}(p,q) = \sum_{x\in\Omega}p(x)\ln\frac{p(x)}{q(x)} = \sum_{i=1}^{n}\sum_{x\in\Omega}p(x)h_{i}(x_{i})$ [since $\ln\frac{p(x)}{q(x)}=\sum_{i=1}^{n}h_{i}(x_{i})$] $= \sum_{i=1}^{n}\sum_{x^{\star}_{i}\in\Omega_{i}}h_{i}(x_{i}^{\star})\sum_{\substack{x\in\Omega,\\ x_{i}=x_{i}^{\star}}}p(x) = \sum_{i=1}^{n}\sum_{x_{i}\in\Omega_{i}}p_{i}(x_{i})h_{i}(x_{i})$ [since $\sum_{x\in\Omega,\ x_{i}=x_{i}^{\star}}p(x)=p_{i}(x_{i}^{\star})$] $= \sum_{i=1}^{n}\mathtt{KL}(p_{i},q_{i}).$
