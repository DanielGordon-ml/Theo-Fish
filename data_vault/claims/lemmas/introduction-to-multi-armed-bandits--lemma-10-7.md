---
slug: introduction-to-multi-armed-bandits--lemma-10-7
label: Lemma 10.7
claim_type: lemma
statement: 'Suppose $(D^{*},\lambda^{*})$ is a mixed Nash equilibrium for the Lagrangian
  game. Then

  (a) $1-\tfrac{T}{B}\,c_{i}(D^{*})\geq 0$ for each resource $i$, with equality if
  $\lambda_{i}^{*}>0$.

  (b) $D^{*}$ is an optimal solution for the linear program (141).

  (c) The minimax value of the Lagrangian game equals the LP value: $\mathcal{L}(D^{*},\lambda^{*})=\mathtt{OPT}_{\mathtt{LP}}$.'
proof: 'By the definition of the mixed Nash equilibrium,


  $\mathcal{L}(D^{*},\lambda)\geq\mathcal{L}(D^{*},\lambda^{*})\geq\mathcal{L}(D,\lambda^{*})\qquad\forall
  D\in\Delta_{K},\lambda\in\Delta_{d}.$


  Part (a). First, we claim that $Y_{i}:=1-\tfrac{T}{B}\,c_{i}(D^{*})\geq 0$ for each
  resource $i$ with $\lambda^{*}_{i}=1$.


  To prove this claim, assume $i$ is not the time resource (otherwise $c_{i}(D^{*})=B/T$,
  and we are done). Fix any arm $a$, and consider the distribution $D$ over arms which
  assigns probability 0 to arm $a$, puts probability $D^{*}(\mathtt{null})+D^{*}(a)$
  on the null arm, and coincides with $D^{*}$ on all other arms. Using Eq. (145),


  $0 \leq\mathcal{L}(D^{*},\lambda^{*})-\mathcal{L}(D,\lambda^{*}) =\left[r(D^{*})-r(D)\right]-\tfrac{T}{B}\,\left[c_{i}(D^{*})-c_{i}(D)\right]
  =D^{*}(a)\left[r(a)-\tfrac{T}{B}\,c_{i}(a)\right] \leq D^{*}(a)\left[1-\tfrac{T}{B}\,c_{i}(a)\right],\quad\forall
  a\in[K].$


  Summing over all arms, we obtain $Y_{i}\geq 0$, claim proved.


  Second, we claim that $Y_{i}\geq 0$ all resources $i$. Suppose this is not the case.
  Focus on resource $i$ with the smallest $Y_{i}<0$; note that $\lambda^{*}_{i}<1$
  by the first claim. Consider putting all probability on this resource: we have $\mathcal{L}(D^{*},i)<0=\mathcal{L}(D^{*},\mathtt{time})\leq\mathcal{L}(D^{*},\lambda^{*})$,
  contradicting (145).


  Third, assume that $\lambda_{i}^{*}>0$ and $Y_{i}>0$ for some resource $i$. Then
  $\mathcal{L}(D^{*},\lambda^{*})>r(D^{*})$. Now, consider distribution $\lambda$
  which puts probability $1$ on the dummy resource. Then $\mathcal{L}(D^{*},\lambda)=r(D^{*})<\mathcal{L}(D^{*},\lambda^{*})$,
  contradicting (145). Thus, $\lambda_{i}^{*}=0$ implies $Y_{i}>0$.


  Part (bc). By part (a), $D^{*}$ is a feasible solution to (141), and $\mathcal{L}(D^{*},\lambda^{*})=r(D^{*})$.
  Let $D$ be some other feasible solution for (141). Plugging in the feasibility constraints
  for $D$, we have $\mathcal{L}(D,\lambda^{*})\geq r(D)$. Then


  $r(D^{*})=\mathcal{L}(D^{*},\lambda^{*})\geq\mathcal{L}(D,\lambda^{*})\geq r(D).$


  So, $D^{*}$ is an optimal solution to the LP. In particular, $\mathtt{OPT}_{\mathtt{LP}}=r(D^{*})=\mathcal{L}(D^{*},\lambda^{*})$.'
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/lagrange-game]]'
- '[[concepts/linear-program-for-bwk]]'
- '[[concepts/mixed-nash-equilibrium]]'
- '[[concepts/opt-lp]]'
about_meta:
- target: '[[concepts/lagrange-game]]'
  role: primary
  aspect: ''
- target: '[[concepts/linear-program-for-bwk]]'
  role: primary
  aspect: ''
- target: '[[concepts/mixed-nash-equilibrium]]'
  role: primary
  aspect: ''
- target: '[[concepts/opt-lp]]'
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

# Lemma 10.7

Suppose $(D^{*},\lambda^{*})$ is a mixed Nash equilibrium for the Lagrangian game. Then
(a) $1-\tfrac{T}{B}\,c_{i}(D^{*})\geq 0$ for each resource $i$, with equality if $\lambda_{i}^{*}>0$.
(b) $D^{*}$ is an optimal solution for the linear program (141).
(c) The minimax value of the Lagrangian game equals the LP value: $\mathcal{L}(D^{*},\lambda^{*})=\mathtt{OPT}_{\mathtt{LP}}$.


## Proof

By the definition of the mixed Nash equilibrium,

$\mathcal{L}(D^{*},\lambda)\geq\mathcal{L}(D^{*},\lambda^{*})\geq\mathcal{L}(D,\lambda^{*})\qquad\forall D\in\Delta_{K},\lambda\in\Delta_{d}.$

Part (a). First, we claim that $Y_{i}:=1-\tfrac{T}{B}\,c_{i}(D^{*})\geq 0$ for each resource $i$ with $\lambda^{*}_{i}=1$.

To prove this claim, assume $i$ is not the time resource (otherwise $c_{i}(D^{*})=B/T$, and we are done). Fix any arm $a$, and consider the distribution $D$ over arms which assigns probability 0 to arm $a$, puts probability $D^{*}(\mathtt{null})+D^{*}(a)$ on the null arm, and coincides with $D^{*}$ on all other arms. Using Eq. (145),

$0 \leq\mathcal{L}(D^{*},\lambda^{*})-\mathcal{L}(D,\lambda^{*}) =\left[r(D^{*})-r(D)\right]-\tfrac{T}{B}\,\left[c_{i}(D^{*})-c_{i}(D)\right] =D^{*}(a)\left[r(a)-\tfrac{T}{B}\,c_{i}(a)\right] \leq D^{*}(a)\left[1-\tfrac{T}{B}\,c_{i}(a)\right],\quad\forall a\in[K].$

Summing over all arms, we obtain $Y_{i}\geq 0$, claim proved.

Second, we claim that $Y_{i}\geq 0$ all resources $i$. Suppose this is not the case. Focus on resource $i$ with the smallest $Y_{i}<0$; note that $\lambda^{*}_{i}<1$ by the first claim. Consider putting all probability on this resource: we have $\mathcal{L}(D^{*},i)<0=\mathcal{L}(D^{*},\mathtt{time})\leq\mathcal{L}(D^{*},\lambda^{*})$, contradicting (145).

Third, assume that $\lambda_{i}^{*}>0$ and $Y_{i}>0$ for some resource $i$. Then $\mathcal{L}(D^{*},\lambda^{*})>r(D^{*})$. Now, consider distribution $\lambda$ which puts probability $1$ on the dummy resource. Then $\mathcal{L}(D^{*},\lambda)=r(D^{*})<\mathcal{L}(D^{*},\lambda^{*})$, contradicting (145). Thus, $\lambda_{i}^{*}=0$ implies $Y_{i}>0$.

Part (bc). By part (a), $D^{*}$ is a feasible solution to (141), and $\mathcal{L}(D^{*},\lambda^{*})=r(D^{*})$. Let $D$ be some other feasible solution for (141). Plugging in the feasibility constraints for $D$, we have $\mathcal{L}(D,\lambda^{*})\geq r(D)$. Then

$r(D^{*})=\mathcal{L}(D^{*},\lambda^{*})\geq\mathcal{L}(D,\lambda^{*})\geq r(D).$

So, $D^{*}$ is an optimal solution to the LP. In particular, $\mathtt{OPT}_{\mathtt{LP}}=r(D^{*})=\mathcal{L}(D^{*},\lambda^{*})$.
