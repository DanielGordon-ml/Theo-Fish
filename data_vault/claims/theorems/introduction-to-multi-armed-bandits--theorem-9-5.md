---
slug: introduction-to-multi-armed-bandits--theorem-9-5
label: Theorem 9.5
claim_type: theorem
statement: 'Let $R''(T)$ be the regret of $\mathtt{ADV}$. Then the average costs/rewards
  converge, in the sense that

  $$\tfrac{1}{T}\,\mathtt{cost}(\mathtt{ALG})=\tfrac{1}{T}\,\mathtt{rew}(\mathtt{ADV})\in\left[v^{*}-\tfrac{R''(T)}{T},\,v^{*}+\tfrac{R(T)}{T}\right].$$

  Moreover, the average play $(\bar{\imath},\bar{\jmath})$ forms an $\epsilon_{T}$-approximate
  Nash equilibrium, with $\epsilon_{T}:=\tfrac{R(T)+R''(T)}{T}$:

  $$M(\bar{\imath},\,q)\leq v^{*}+\epsilon_{T}\qquad\forall q\in\Delta_{\mathtt{cols}},$$

  $$M(p,\,\bar{\jmath})\geq v^{*}-\epsilon_{T}\qquad\forall p\in\Delta_{\mathtt{rows}}.$$'
proof: 'First, express $\mathtt{cost}^*$ in terms of the function $h(\cdot)$:

  $$\mathtt{cost}(i) = \sum_{t=1}^{T} M(i, j_t) = T\, M(i, \bar{\jmath}) \quad \text{for
  each row } i$$

  $$\tfrac{1}{T}\, \mathtt{cost}^* = \min_{\text{rows } i} M(i, \bar{\jmath}) = h(\bar{\jmath}).$$

  Analyze ALG''s costs:

  $$\tfrac{1}{T}\, \mathtt{cost}(\mathtt{ALG}) - \tfrac{R(T)}{T} = \tfrac{1}{T}\,
  \mathtt{cost}^* = h(\bar{\jmath}) \leq h(q^*) = v^{\sharp} = v^*$$

  where the inequality is by definition of maximin strategy $q^*$ and the last equality
  by the minimax theorem.


  Similarly, analyze the rewards of ADV. Let $\mathtt{rew}(j) = \sum_{t=1}^{T} M(i_t,
  j)$ and $\mathtt{rew}^* := \max_{\text{columns } j} \mathtt{rew}(j)$. Then:

  $$\mathtt{rew}(j) = \sum_{t=1}^{T} M(i_t, j) = T\, M(\bar{\imath}, j) \quad \text{for
  each column } j$$

  $$\tfrac{1}{T}\, \mathtt{rew}^* = \max_{\text{columns } j} M(\bar{\imath}, j) =
  \max_{q \in \Delta_{\mathtt{cols}}} M(\bar{\imath}, q) = f(\bar{\imath}).$$

  Using the regret of ADV:

  $$\tfrac{1}{T}\, \mathtt{cost}(\mathtt{ALG}) + \tfrac{R''(T)}{T} = \tfrac{1}{T}\,
  \mathtt{rew}(\mathtt{ADV}) + \tfrac{R''(T)}{T} = \tfrac{1}{T}\, \mathtt{rew}^* =
  f(\bar{\imath}) \geq f(p^*) = v^*$$

  where the first equality uses the zero-sum property, the second is the regret definition
  for ADV, and the inequality is by definition of minimax strategy $p^*$.


  Putting together (131) and (133):

  $$v^* - \tfrac{R''(T)}{T} \leq f(\bar{\imath}) - \tfrac{R''(T)}{T} \leq \tfrac{1}{T}\,
  \mathtt{cost}(\mathtt{ALG}) \leq h(\bar{\jmath}) + \tfrac{R(T)}{T} \leq v^* + \tfrac{R(T)}{T}.$$'
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/convergence-rate]]'
- '[[concepts/regret-minimizing-algorithm]]'
- '[[concepts/regret-minimization]]'
- '[[concepts/game-matrix]]'
- '[[concepts/zero-sum-games]]'
- '[[concepts/approximate-nash-property]]'
- '[[concepts/nash-equilibrium]]'
about_meta:
- target: '[[concepts/convergence-rate]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret-minimizing-algorithm]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret-minimization]]'
  role: primary
  aspect: ''
- target: '[[concepts/game-matrix]]'
  role: primary
  aspect: ''
- target: '[[concepts/zero-sum-games]]'
  role: primary
  aspect: ''
- target: '[[concepts/approximate-nash-property]]'
  role: primary
  aspect: ''
- target: '[[concepts/nash-equilibrium]]'
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

# Theorem 9.5

Let $R'(T)$ be the regret of $\mathtt{ADV}$. Then the average costs/rewards converge, in the sense that
$$\tfrac{1}{T}\,\mathtt{cost}(\mathtt{ALG})=\tfrac{1}{T}\,\mathtt{rew}(\mathtt{ADV})\in\left[v^{*}-\tfrac{R'(T)}{T},\,v^{*}+\tfrac{R(T)}{T}\right].$$
Moreover, the average play $(\bar{\imath},\bar{\jmath})$ forms an $\epsilon_{T}$-approximate Nash equilibrium, with $\epsilon_{T}:=\tfrac{R(T)+R'(T)}{T}$:
$$M(\bar{\imath},\,q)\leq v^{*}+\epsilon_{T}\qquad\forall q\in\Delta_{\mathtt{cols}},$$
$$M(p,\,\bar{\jmath})\geq v^{*}-\epsilon_{T}\qquad\forall p\in\Delta_{\mathtt{rows}}.$$


## Proof

First, express $\mathtt{cost}^*$ in terms of the function $h(\cdot)$:
$$\mathtt{cost}(i) = \sum_{t=1}^{T} M(i, j_t) = T\, M(i, \bar{\jmath}) \quad \text{for each row } i$$
$$\tfrac{1}{T}\, \mathtt{cost}^* = \min_{\text{rows } i} M(i, \bar{\jmath}) = h(\bar{\jmath}).$$
Analyze ALG's costs:
$$\tfrac{1}{T}\, \mathtt{cost}(\mathtt{ALG}) - \tfrac{R(T)}{T} = \tfrac{1}{T}\, \mathtt{cost}^* = h(\bar{\jmath}) \leq h(q^*) = v^{\sharp} = v^*$$
where the inequality is by definition of maximin strategy $q^*$ and the last equality by the minimax theorem.

Similarly, analyze the rewards of ADV. Let $\mathtt{rew}(j) = \sum_{t=1}^{T} M(i_t, j)$ and $\mathtt{rew}^* := \max_{\text{columns } j} \mathtt{rew}(j)$. Then:
$$\mathtt{rew}(j) = \sum_{t=1}^{T} M(i_t, j) = T\, M(\bar{\imath}, j) \quad \text{for each column } j$$
$$\tfrac{1}{T}\, \mathtt{rew}^* = \max_{\text{columns } j} M(\bar{\imath}, j) = \max_{q \in \Delta_{\mathtt{cols}}} M(\bar{\imath}, q) = f(\bar{\imath}).$$
Using the regret of ADV:
$$\tfrac{1}{T}\, \mathtt{cost}(\mathtt{ALG}) + \tfrac{R'(T)}{T} = \tfrac{1}{T}\, \mathtt{rew}(\mathtt{ADV}) + \tfrac{R'(T)}{T} = \tfrac{1}{T}\, \mathtt{rew}^* = f(\bar{\imath}) \geq f(p^*) = v^*$$
where the first equality uses the zero-sum property, the second is the regret definition for ADV, and the inequality is by definition of minimax strategy $p^*$.

Putting together (131) and (133):
$$v^* - \tfrac{R'(T)}{T} \leq f(\bar{\imath}) - \tfrac{R'(T)}{T} \leq \tfrac{1}{T}\, \mathtt{cost}(\mathtt{ALG}) \leq h(\bar{\jmath}) + \tfrac{R(T)}{T} \leq v^* + \tfrac{R(T)}{T}.$$
