---
type: theorem
label: Theorem 5.9
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: '26 Initial results: binary prediction with experts advice'
related_entities: []
date_extracted: '2026-03-16T01:32:59.505022+00:00'
---

# Theorem 5.9

The number of mistakes made by WMA with parameter $\epsilon\in(0,1)$ is at most $\frac{2}{1-\epsilon}\cdot\mathtt{cost}^{*}+\frac{2}{\epsilon}\cdot\ln{K}.$

## Proof

To analyze the algorithm, we first introduce some notation. Let $w_{t}(a)$ be the weight of expert $a$ before round $t$, and let $W_{t}=\sum_{a=1}^{K}w_{t}(a)$ be the total weight before round $t$. Let $S_{t}$ be the set of experts that made incorrect prediction at round $t$. We will use the following fact about logarithms: $\ln(1-x)<-x\qquad\forall x\in(0,1).$ (75) From the algorithm, $W_{1}=K$ and $W_{T+1}>w_{t}(a^{*})=(1-\epsilon)^{\mathtt{cost}^{*}}$. Therefore, we have $\frac{W_{T+1}}{W_{1}}>\frac{(1-\epsilon)^{\mathtt{cost}^{*}}}{K}.$ (76) Since the weights are non-increasing, we must have $W_{t+1}\leq W_{t}$ (77) If the algorithm makes mistake at round $t$, then $W_{t+1}=\sum_{a\in[K]}w_{t+1}(a)=\sum_{a\in S_{t}}(1-\epsilon)w_{t}(a)+\sum_{a\not\in S_{t}}w_{t}(a)=W_{t}-\epsilon\sum_{a\in S_{t}}w_{t}(a).$ Since we are using weighted majority vote, the incorrect prediction must have the majority vote: $\sum_{a\in S_{t}}w_{t}(a)\geq\tfrac{1}{2}W_{t}.$ Therefore, if the algorithm makes mistake at round $t$, we have $W_{t+1}\leq(1-\tfrac{\epsilon}{2})W_{t}.$ Combining with (76) and (77), we get $\frac{(1-\epsilon)^{\mathtt{cost}^{*}}}{K}<\frac{W_{T+1}}{W_{1}}=\prod_{t=1}^{T}\frac{W_{t+1}}{W_{t}}\leq(1-\tfrac{\epsilon}{2})^{M},$ where $M$ is the number of mistakes. Taking logarithm of both sides, we get $\mathtt{cost}^{*}\cdot\ln(1-\epsilon)-\ln{K}<M\cdot\ln(1-\tfrac{\epsilon}{2})<M\cdot(-\tfrac{\epsilon}{2}),$ where the last inequality follows from Eq. (75). Rearranging the terms, we get $M<\mathtt{cost}^{*}\cdot\tfrac{2}{\epsilon}\ln(\tfrac{1}{1-\epsilon})+\tfrac{2}{\epsilon}\ln{K}<\tfrac{2}{1-\epsilon}\cdot\mathtt{cost}^{*}+\tfrac{2}{\epsilon}\cdot\ln{K},$ where the last step follows from (75) with $x=\frac{\epsilon}{1-\epsilon}$.

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 26 Initial results: binary prediction with experts advice
