---
slug: introduction-to-multi-armed-bandits--lemma-13-3-pinsker-s-inequality-theorem-2-4-c
label: Lemma 13.3 (Pinsker's inequality, Theorem 2.4 (c))
claim_type: lemma
statement: Fix event $A\subset\Omega$. Then $2\left(p(A)-q(A)\right)^{2}\leq\mathtt{KL}(p,q)$.
proof: 'First, we claim that $\sum_{x\in B}p(x)\ln\frac{p(x)}{q(x)}\geq p(B)\ln\frac{p(B)}{q(B)}$
  for each event $B\subset\Omega$. (176)


  For each $x\in B$, define $p_{B}(x)=p(x)/p(B)$ and $q_{B}(x)=q(x)/q(B)$. Then


  $\sum_{x\in B}p(x)\ln\frac{p(x)}{q(x)} = p(B)\sum_{x\in B}p_{B}(x)\ln\frac{p(B)\cdot
  p_{B}(x)}{q(B)\cdot q_{B}(x)} = p(B)\left(\sum_{x\in B}p_{B}(x)\ln\frac{p_{B}(x)}{q_{B}(x)}\right)+p(B)\ln\frac{p(B)}{q(B)}\sum_{x\in
  B}p_{B}(x) \geq p(B)\ln\frac{p(B)}{q(B)}$ [since $\sum_{x\in B}p_{B}(x)\ln\frac{p_{B}(x)}{q_{B}(x)}=\mathtt{KL}(p_{B},q_{B})\geq
  0$].


  Now that we''ve proved (176), let us use it twice: for $B=A$ and for $B=\bar{A}$,
  the complement of $A$:


  $\sum_{x\in A}p(x)\ln\frac{p(x)}{q(x)}\geq p(A)\ln\frac{p(A)}{q(A)}$,

  $\sum_{x\notin A}p(x)\ln\frac{p(x)}{q(x)}\geq p(\bar{A})\ln\frac{p(\bar{A})}{q(\bar{A})}$.


  Now, let $a=p(A)$ and $b=q(A)$, and w.l.o.g. assume that $a<b$. Then:


  $\mathtt{KL}(p,q) \geq a\ln\frac{a}{b}+(1-a)\ln\frac{1-a}{1-b} = \int_{a}^{b}\left(-\frac{a}{x}+\frac{1-a}{1-x}\right)dx=\int_{a}^{b}\frac{x-a}{x(1-x)}dx
  \geq\int_{a}^{b}4(x-a)dx=2(b-a)^{2}.$ (since $x(1-x)\leq\tfrac{1}{4}$)'
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/probability-distribution]]'
- '[[concepts/kl-divergence]]'
- '[[concepts/event]]'
about_meta:
- target: '[[concepts/probability-distribution]]'
  role: primary
  aspect: ''
- target: '[[concepts/kl-divergence]]'
  role: primary
  aspect: ''
- target: '[[concepts/event]]'
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

# Lemma 13.3 (Pinsker's inequality, Theorem 2.4 (c))

Fix event $A\subset\Omega$. Then $2\left(p(A)-q(A)\right)^{2}\leq\mathtt{KL}(p,q)$.


## Proof

First, we claim that $\sum_{x\in B}p(x)\ln\frac{p(x)}{q(x)}\geq p(B)\ln\frac{p(B)}{q(B)}$ for each event $B\subset\Omega$. (176)

For each $x\in B$, define $p_{B}(x)=p(x)/p(B)$ and $q_{B}(x)=q(x)/q(B)$. Then

$\sum_{x\in B}p(x)\ln\frac{p(x)}{q(x)} = p(B)\sum_{x\in B}p_{B}(x)\ln\frac{p(B)\cdot p_{B}(x)}{q(B)\cdot q_{B}(x)} = p(B)\left(\sum_{x\in B}p_{B}(x)\ln\frac{p_{B}(x)}{q_{B}(x)}\right)+p(B)\ln\frac{p(B)}{q(B)}\sum_{x\in B}p_{B}(x) \geq p(B)\ln\frac{p(B)}{q(B)}$ [since $\sum_{x\in B}p_{B}(x)\ln\frac{p_{B}(x)}{q_{B}(x)}=\mathtt{KL}(p_{B},q_{B})\geq 0$].

Now that we've proved (176), let us use it twice: for $B=A$ and for $B=\bar{A}$, the complement of $A$:

$\sum_{x\in A}p(x)\ln\frac{p(x)}{q(x)}\geq p(A)\ln\frac{p(A)}{q(A)}$,
$\sum_{x\notin A}p(x)\ln\frac{p(x)}{q(x)}\geq p(\bar{A})\ln\frac{p(\bar{A})}{q(\bar{A})}$.

Now, let $a=p(A)$ and $b=q(A)$, and w.l.o.g. assume that $a<b$. Then:

$\mathtt{KL}(p,q) \geq a\ln\frac{a}{b}+(1-a)\ln\frac{1-a}{1-b} = \int_{a}^{b}\left(-\frac{a}{x}+\frac{1-a}{1-x}\right)dx=\int_{a}^{b}\frac{x-a}{x(1-x)}dx \geq\int_{a}^{b}4(x-a)dx=2(b-a)^{2}.$ (since $x(1-x)\leq\tfrac{1}{4}$)
