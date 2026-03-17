---
slug: introduction-to-multi-armed-bandits--lemma-13-1-gibbs-inequality-theorem-2-4-a
label: Lemma 13.1 (Gibbs' Inequality, Theorem 2.4 (a))
claim_type: lemma
statement: $\mathtt{KL}(p,q)\geq 0$ for any two distributions $p,q$, with equality
  if and only if $p=q$.
proof: 'Let us define: $f(y)=y\ln(y)$. $f$ is a convex function under the domain $y>0$.
  Now, from the definition of the KL divergence we get:


  $\mathtt{KL}(p,q) = \sum_{x\in\Omega}q(x)\,\frac{p(x)}{q(x)}\ln\frac{p(x)}{q(x)}
  = \sum_{x\in\Omega}q(x)f\left(\frac{p(x)}{q(x)}\right) \geq f\left(\sum_{x\in\Omega}q(x)\frac{p(x)}{q(x)}\right)$
  (by Jensen''s inequality) $= f\left(\sum_{x\in\Omega}p(x)\right)=f(1)=0.$


  In the above application of Jensen''s inequality, $f$ is not a linear function,
  so the equality holds (i.e., $\mathtt{KL}(p,q)=0$) if and only if $p=q$.'
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/probability-distribution]]'
- '[[concepts/kl-divergence]]'
about_meta:
- target: '[[concepts/probability-distribution]]'
  role: primary
  aspect: ''
- target: '[[concepts/kl-divergence]]'
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

# Lemma 13.1 (Gibbs' Inequality, Theorem 2.4 (a))

$\mathtt{KL}(p,q)\geq 0$ for any two distributions $p,q$, with equality if and only if $p=q$.


## Proof

Let us define: $f(y)=y\ln(y)$. $f$ is a convex function under the domain $y>0$. Now, from the definition of the KL divergence we get:

$\mathtt{KL}(p,q) = \sum_{x\in\Omega}q(x)\,\frac{p(x)}{q(x)}\ln\frac{p(x)}{q(x)} = \sum_{x\in\Omega}q(x)f\left(\frac{p(x)}{q(x)}\right) \geq f\left(\sum_{x\in\Omega}q(x)\frac{p(x)}{q(x)}\right)$ (by Jensen's inequality) $= f\left(\sum_{x\in\Omega}p(x)\right)=f(1)=0.$

In the above application of Jensen's inequality, $f$ is not a linear function, so the equality holds (i.e., $\mathtt{KL}(p,q)=0$) if and only if $p=q$.
