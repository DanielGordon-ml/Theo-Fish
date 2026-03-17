---
slug: introduction-to-multi-armed-bandits--discretization-error-bound-for-uniform-discretization
label: Discretization error bound for uniform discretization
claim_type: lemma
statement: For uniform discretization of $[0,1]$ with discretization step $\epsilon$,
  $\mathtt{DE}(S)\leq L\epsilon$.
proof: If $x^{*}$ is a best arm on $X$, and $y$ is the closest arm to $x^{*}$ that
  lies in $S$, it follows that $|x^{*}-y|\leq\epsilon$, and therefore $\mu(x^{*})-\mu(y)\leq
  L\epsilon$.
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/lipschitz-constant-l]]'
- '[[concepts/lipschitz-condition]]'
- '[[concepts/continuum-armed-bandits]]'
- '[[concepts/discretization-error-de-s]]'
about_meta:
- target: '[[concepts/lipschitz-constant-l]]'
  role: primary
  aspect: ''
- target: '[[concepts/lipschitz-condition]]'
  role: primary
  aspect: ''
- target: '[[concepts/continuum-armed-bandits]]'
  role: primary
  aspect: ''
- target: '[[concepts/discretization-error-de-s]]'
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

# Discretization error bound for uniform discretization

For uniform discretization of $[0,1]$ with discretization step $\epsilon$, $\mathtt{DE}(S)\leq L\epsilon$.


## Proof

If $x^{*}$ is a best arm on $X$, and $y$ is the closest arm to $x^{*}$ that lies in $S$, it follows that $|x^{*}-y|\leq\epsilon$, and therefore $\mu(x^{*})-\mu(y)\leq L\epsilon$.
