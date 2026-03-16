---
type: theorem
label: Eq. (124)
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 50 The minimax theorem
related_entities: []
date_extracted: '2026-03-16T01:32:59.539539+00:00'
---

# Eq. (124)

\(\displaystyle\min_{p\in\Delta_{\mathtt{rows}}}\;\max_{q\in\Delta_{\mathtt{cols}}}\;M(p,q)=\max_{q\in\Delta_{\mathtt{cols}}}\;\min_{p\in\Delta_{\mathtt{rows}}}\;M(p,q).\)

## Proof

The $\geq$ direction is easy: $$\displaystyle M(p,q)$$ $$\displaystyle\geq\min_{p^{\prime}\in\Delta_{\mathtt{rows}}}M(p^{\prime},q)\qquad\forall q\in\Delta_{\mathtt{cols}}$$ $$\displaystyle\max_{q\in\Delta_{\mathtt{cols}}}M(p,q)$$ $$\displaystyle\geq\max_{q\in\Delta_{\mathtt{cols}}}\;\min_{p^{\prime}\in\Delta_{\mathtt{rows}}}M(p^{\prime},q).$$ The $\leq$ direction is the difficult part. Let us consider a full-feedback version of the repeated game studied earlier. Let $\mathtt{ALG}$ be any algorithm with subliner expected regret, e.g.,\xa0$\mathtt{Hedge}$ algorithm from Chapter\xa027, and let $\mathtt{ADV}$ be the best-response adversary. Define $$\displaystyle h(q):=\inf_{p\in\Delta_{\mathtt{rows}}}M(p,q)=\min_{\text{rows $i$}}\;M(i,q)$$ for each distribution $q\in\Delta_{\mathtt{cols}}$, similarly to how $f(p)$ is defined in (119). We need to prove that $$\displaystyle\min_{p\in\Delta_{\mathtt{rows}}}f(p)\leq\max_{q\in\Delta_{\mathtt{cols}}}h(q).$$ Let us take care of some preliminaries. Let $\bar{\jmath}$ be the average play of $\mathtt{ADV}$, as per Definition\xa09.2. Then: $$\displaystyle\operatornamewithlimits{\mathbb{E}}[\mathtt{cost}(i)]$$ $$\displaystyle=\textstyle\sum_{t=1}^{T}\operatornamewithlimits{\mathbb{E}}[\,M(i,j_{t})\,]=T\,\operatornamewithlimits{\mathbb{E}}[\,M(i,\bar{\jmath})\,]=T\,M(i,\,\operatornamewithlimits{\mathbb{E}}[\bar{\jmath}])\qquad\text{for each row $i$}$$ $$\displaystyle\tfrac{1}{T}\,\operatornamewithlimits{\mathbb{E}}[\mathtt{cost}^{*}]$$ $$\displaystyle\leq\tfrac{1}{T}\,\min_{\text{rows $i$}}\operatornamewithlimits{\mathbb{E}}[\mathtt{cost}(i)]=\min_{\text{rows $i$}}M(i,\,\operatornamewithlimits{\mathbb{E}}[\bar{\jmath}])=\min_{p\in\Delta_{\mathtt{rows}}}M(p,\,\operatornamewithlimits{\mathbb{E}}[\bar{\jmath}])=h(\operatornamewithlimits{\mathbb{E}}[\bar{\jmath}]).$$ The crux of the argument is as follows: $$\displaystyle\min_{p\in\Delta_{\mathtt{rows}}}f(p)$$ $$\displaystyle\leq f(\,\operatornamewithlimits{\mathbb{E}}[\bar{\imath}]\,)$$ $$\displaystyle\leq\tfrac{1}{T}\,\operatornamewithlimits{\mathbb{E}}[\mathtt{cost}(\mathtt{ALG})]$$ (by best response, see ( 123 )) $$\displaystyle=\tfrac{1}{T}\,\operatornamewithlimits{\mathbb{E}}[\mathtt{cost}^{*}]+\tfrac{\operatornamewithlimits{\mathbb{E}}[R(T)]}{T}$$ (by definition of regret) $$\displaystyle\leq h(\operatornamewithlimits{\mathbb{E}}[\bar{\jmath}])+\tfrac{\operatornamewithlimits{\mathbb{E}}[R(T)]}{T}$$ (using $h(\cdot)$ , see ( 129 )) $$\displaystyle\leq\max_{q\in\Delta_{\mathtt{cols}}}h(q)+\tfrac{\operatornamewithlimits{\mathbb{E}}[R(T)]}{T}.$$ Now, taking $T\to\infty$ implies Eq.\xa0(128) because $\operatornamewithlimits{\mathbb{E}}[R(T)]/T\to 0$, completing the proof.

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 50 The minimax theorem
