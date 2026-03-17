---
slug: introduction-to-multi-armed-bandits--eq-124-minimax-theorem
label: Eq. (124) — Minimax Theorem
claim_type: theorem
statement: '$$\min_{p\in\Delta_{\mathtt{rows}}}\;\max_{q\in\Delta_{\mathtt{cols}}}\;M(p,q)=\max_{q\in\Delta_{\mathtt{cols}}}\;\min_{p\in\Delta_{\mathtt{rows}}}\;M(p,q).$$

  In other words, the $\max$ and the $\min$ can be switched.'
proof: 'The $\geq$ direction is easy:

  $$M(p,q) \geq \min_{p''\in\Delta_{\mathtt{rows}}}M(p'',q) \quad \forall q\in\Delta_{\mathtt{cols}}$$

  $$\max_{q\in\Delta_{\mathtt{cols}}}M(p,q) \geq \max_{q\in\Delta_{\mathtt{cols}}}\;\min_{p''\in\Delta_{\mathtt{rows}}}M(p'',q).$$


  The $\leq$ direction is the difficult part. Let us consider a full-feedback version
  of the repeated game studied earlier. Let $\mathtt{ALG}$ be any algorithm with sublinear
  expected regret, e.g., $\mathtt{Hedge}$ algorithm from Chapter 27, and let $\mathtt{ADV}$
  be the best-response adversary. Define

  $$h(q):=\inf_{p\in\Delta_{\mathtt{rows}}}M(p,q)=\min_{\text{rows $i$}}\;M(i,q)$$

  for each distribution $q\in\Delta_{\mathtt{cols}}$, similarly to how $f(p)$ is defined
  in (119). We need to prove that

  $$\min_{p\in\Delta_{\mathtt{rows}}}f(p)\leq\max_{q\in\Delta_{\mathtt{cols}}}h(q).$$


  Let us take care of some preliminaries. Let $\bar{\jmath}$ be the average play of
  $\mathtt{ADV}$, as per Definition 9.2. Then:

  $$\operatornamewithlimits{\mathbb{E}}[\mathtt{cost}(i)] = \textstyle\sum_{t=1}^{T}\operatornamewithlimits{\mathbb{E}}[\,M(i,j_{t})\,]=T\,\operatornamewithlimits{\mathbb{E}}[\,M(i,\bar{\jmath})\,]=T\,M(i,\,\operatornamewithlimits{\mathbb{E}}[\bar{\jmath}])\qquad\text{for
  each row $i$}$$

  $$\tfrac{1}{T}\,\operatornamewithlimits{\mathbb{E}}[\mathtt{cost}^{*}] \leq\tfrac{1}{T}\,\min_{\text{rows
  $i$}}\operatornamewithlimits{\mathbb{E}}[\mathtt{cost}(i)]=\min_{\text{rows $i$}}M(i,\,\operatornamewithlimits{\mathbb{E}}[\bar{\jmath}])=\min_{p\in\Delta_{\mathtt{rows}}}M(p,\,\operatornamewithlimits{\mathbb{E}}[\bar{\jmath}])=h(\operatornamewithlimits{\mathbb{E}}[\bar{\jmath}]).$$


  The crux of the argument is as follows:

  $$\min_{p\in\Delta_{\mathtt{rows}}}f(p) \leq f(\,\operatornamewithlimits{\mathbb{E}}[\bar{\imath}]\,)
  \leq\tfrac{1}{T}\,\operatornamewithlimits{\mathbb{E}}[\mathtt{cost}(\mathtt{ALG})]
  \quad\text{(by best response, see (123))}$$

  $$=\tfrac{1}{T}\,\operatornamewithlimits{\mathbb{E}}[\mathtt{cost}^{*}]+\tfrac{\operatornamewithlimits{\mathbb{E}}[R(T)]}{T}
  \quad\text{(by definition of regret)}$$

  $$\leq h(\operatornamewithlimits{\mathbb{E}}[\bar{\jmath}])+\tfrac{\operatornamewithlimits{\mathbb{E}}[R(T)]}{T}
  \quad\text{(using $h(\cdot)$, see (129))}$$

  $$\leq\max_{q\in\Delta_{\mathtt{cols}}}h(q)+\tfrac{\operatornamewithlimits{\mathbb{E}}[R(T)]}{T}.$$


  Now, taking $T\to\infty$ implies Eq. (128) because $\operatornamewithlimits{\mathbb{E}}[R(T)]/T\to
  0$, completing the proof.'
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/hedge]]'
- '[[concepts/zero-sum-game]]'
- '[[concepts/game-matrix]]'
- '[[concepts/best-response-adversary]]'
- '[[concepts/d-rows]]'
- '[[concepts/minimax-value]]'
- '[[concepts/d-cols]]'
- '[[concepts/average-play]]'
- '[[concepts/m-p-q]]'
- '[[concepts/f-p]]'
- '[[concepts/sublinear-expected-regret]]'
- '[[concepts/h-function]]'
- '[[concepts/maximin-value]]'
about_meta:
- target: '[[concepts/hedge]]'
  role: primary
  aspect: ''
- target: '[[concepts/zero-sum-game]]'
  role: primary
  aspect: ''
- target: '[[concepts/game-matrix]]'
  role: primary
  aspect: ''
- target: '[[concepts/best-response-adversary]]'
  role: primary
  aspect: ''
- target: '[[concepts/d-rows]]'
  role: primary
  aspect: ''
- target: '[[concepts/minimax-value]]'
  role: primary
  aspect: ''
- target: '[[concepts/d-cols]]'
  role: primary
  aspect: ''
- target: '[[concepts/average-play]]'
  role: primary
  aspect: ''
- target: '[[concepts/m-p-q]]'
  role: primary
  aspect: ''
- target: '[[concepts/f-p]]'
  role: primary
  aspect: ''
- target: '[[concepts/sublinear-expected-regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/h-function]]'
  role: primary
  aspect: ''
- target: '[[concepts/maximin-value]]'
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

# Eq. (124) — Minimax Theorem

$$\min_{p\in\Delta_{\mathtt{rows}}}\;\max_{q\in\Delta_{\mathtt{cols}}}\;M(p,q)=\max_{q\in\Delta_{\mathtt{cols}}}\;\min_{p\in\Delta_{\mathtt{rows}}}\;M(p,q).$$
In other words, the $\max$ and the $\min$ can be switched.


## Proof

The $\geq$ direction is easy:
$$M(p,q) \geq \min_{p'\in\Delta_{\mathtt{rows}}}M(p',q) \quad \forall q\in\Delta_{\mathtt{cols}}$$
$$\max_{q\in\Delta_{\mathtt{cols}}}M(p,q) \geq \max_{q\in\Delta_{\mathtt{cols}}}\;\min_{p'\in\Delta_{\mathtt{rows}}}M(p',q).$$

The $\leq$ direction is the difficult part. Let us consider a full-feedback version of the repeated game studied earlier. Let $\mathtt{ALG}$ be any algorithm with sublinear expected regret, e.g., $\mathtt{Hedge}$ algorithm from Chapter 27, and let $\mathtt{ADV}$ be the best-response adversary. Define
$$h(q):=\inf_{p\in\Delta_{\mathtt{rows}}}M(p,q)=\min_{\text{rows $i$}}\;M(i,q)$$
for each distribution $q\in\Delta_{\mathtt{cols}}$, similarly to how $f(p)$ is defined in (119). We need to prove that
$$\min_{p\in\Delta_{\mathtt{rows}}}f(p)\leq\max_{q\in\Delta_{\mathtt{cols}}}h(q).$$

Let us take care of some preliminaries. Let $\bar{\jmath}$ be the average play of $\mathtt{ADV}$, as per Definition 9.2. Then:
$$\operatornamewithlimits{\mathbb{E}}[\mathtt{cost}(i)] = \textstyle\sum_{t=1}^{T}\operatornamewithlimits{\mathbb{E}}[\,M(i,j_{t})\,]=T\,\operatornamewithlimits{\mathbb{E}}[\,M(i,\bar{\jmath})\,]=T\,M(i,\,\operatornamewithlimits{\mathbb{E}}[\bar{\jmath}])\qquad\text{for each row $i$}$$
$$\tfrac{1}{T}\,\operatornamewithlimits{\mathbb{E}}[\mathtt{cost}^{*}] \leq\tfrac{1}{T}\,\min_{\text{rows $i$}}\operatornamewithlimits{\mathbb{E}}[\mathtt{cost}(i)]=\min_{\text{rows $i$}}M(i,\,\operatornamewithlimits{\mathbb{E}}[\bar{\jmath}])=\min_{p\in\Delta_{\mathtt{rows}}}M(p,\,\operatornamewithlimits{\mathbb{E}}[\bar{\jmath}])=h(\operatornamewithlimits{\mathbb{E}}[\bar{\jmath}]).$$

The crux of the argument is as follows:
$$\min_{p\in\Delta_{\mathtt{rows}}}f(p) \leq f(\,\operatornamewithlimits{\mathbb{E}}[\bar{\imath}]\,) \leq\tfrac{1}{T}\,\operatornamewithlimits{\mathbb{E}}[\mathtt{cost}(\mathtt{ALG})] \quad\text{(by best response, see (123))}$$
$$=\tfrac{1}{T}\,\operatornamewithlimits{\mathbb{E}}[\mathtt{cost}^{*}]+\tfrac{\operatornamewithlimits{\mathbb{E}}[R(T)]}{T} \quad\text{(by definition of regret)}$$
$$\leq h(\operatornamewithlimits{\mathbb{E}}[\bar{\jmath}])+\tfrac{\operatornamewithlimits{\mathbb{E}}[R(T)]}{T} \quad\text{(using $h(\cdot)$, see (129))}$$
$$\leq\max_{q\in\Delta_{\mathtt{cols}}}h(q)+\tfrac{\operatornamewithlimits{\mathbb{E}}[R(T)]}{T}.$$

Now, taking $T\to\infty$ implies Eq. (128) because $\operatornamewithlimits{\mathbb{E}}[R(T)]/T\to 0$, completing the proof.
