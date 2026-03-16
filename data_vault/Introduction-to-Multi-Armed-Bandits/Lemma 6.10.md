---
type: lemma
label: Lemma 6.10
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 34 Improved analysis of 𝙴𝚡𝚙𝟺 \\mathtt{Exp4}
related_entities: []
date_extracted: '2026-03-16T01:32:59.514282+00:00'
---

# Lemma 6.10

Fix parameter $\gamma\in[0,\tfrac{1}{2})$ and round $t$. Then $\operatornamewithlimits{\mathbb{E}}[\widehat{G}_{t}]\leq\tfrac{K}{1-\gamma}$.

## Proof

For each arm $a$, let $\mathcal{E}_{a}=\{e\in\mathcal{E}:a_{t,e}=a\}$ be the set of all experts that recommended this arm. Let p_t(a) := \sum_{e \in \mathcal{E}_a} p_t(e) be the probability that the expert chosen by $\mathtt{Hedge}$ recommends arm $a$. Then $$ q_{t}(a)=p_{t}(a)(1-\gamma)+\frac{\gamma}{K}\geq(1-\gamma)\;p_{t}(a). $$ For each expert $e$, letting $a=a_{t,e}$ be the recommended arm, we have: $$ \widehat{c}_{t}(e)=\widehat{c}_{t}(a)\leq\frac{c_{t}(a)}{q_{t}(a)}\leq\frac{1}{q_{t}(a)}\leq\frac{1}{(1-\gamma)\;p_{t}(a)}. (90) $$ Each realization of $\widehat{G}_{t}$ satisfies: $$ \widehat{G}_{t} := \sum_{e\in\mathcal{E}}p_{t}(e)\;\widehat{c}_{t}^{2}(e) = \sum\limits_{a}\sum\limits_{e\in\mathcal{E}_{a}}p_{t}(e)\cdot\widehat{c}_{t}(e)\cdot\widehat{c}_{t}(e) \leq \sum\limits_{a}\sum\limits_{e\in\mathcal{E}_{a}}\frac{p_{t}(e)}{(1-\gamma)\;p_{t}(a)}\;\widehat{c}_{t}(a) = \frac{1}{1-\gamma}\;\sum\limits_{a}\frac{\widehat{c}_{t}(a)}{p_{t}(a)}\sum\limits_{e\in\mathcal{E}_{a}}p_{t}(e) = \frac{1}{1-\gamma}\;\sum\limits_{a}\widehat{c}_{t}(a). $$ To complete the proof, take expectations over both sides and recall that $\operatornamewithlimits{\mathbb{E}}[\widehat{c}_{t}(a)]=c_{t}(a)\leq 1$.

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 34 Improved analysis of 𝙴𝚡𝚙𝟺 \\mathtt{Exp4}
