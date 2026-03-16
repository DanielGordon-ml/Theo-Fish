---
type: theorem
label: Theorem 8.8
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 44 Contextual bandits with a policy class
related_entities: []
date_extracted: '2026-03-16T01:32:59.531652+00:00'
---

# Theorem 8.8

Let $\mathcal{O}$ be an exact classification oracle for some policy class $\Pi$. Algorithm\xa03 parameterized with oracle $\mathcal{O}$ and $N=T^{2/3}(K\log(|\Pi|T))^{\frac{1}{3}}$ has regret $\operatornamewithlimits{\mathbb{E}}[R_{\Pi}(T)]=O(T^{2/3})(K\log(|\Pi|T))^{\frac{1}{3}}.$

## Proof

Let us consider an arbitrary $N$ for now. For a given policy $\pi$, we estimate its expected reward $\mu(\pi)$ using the realized policy value from (109), where the action costs $\tilde{r}_{t}(\cdot)$ are from (110). Let us prove that $\tilde{r}(\pi)$ is an unbiased estimate for $\mu(\pi)$:

$$ $\displaystyle\operatornamewithlimits{\mathbb{E}}[\tilde{r}_{t}(a)\mid x_{t}]$ $\displaystyle=\mu(a\mid x_{t})$ (for each action $a\in\mathcal{A}$ ) $\displaystyle\operatornamewithlimits{\mathbb{E}}[\tilde{r}_{t}(\pi(x_{t}))\mid x_{t}]$ $\displaystyle=\mu(\pi(x)\mid x_{t})$ (plug in $a=\pi(x_{t})$ ) $\displaystyle\operatornamewithlimits{\mathbb{E}}_{x_{t}\sim D}[\tilde{r}_{t}(\pi(x_{t}))]$ $\displaystyle=\operatornamewithlimits{\mathbb{E}}_{x_{t}\sim D}[\mu(\pi(x_{t}))\mid x_{t}]$ (take expectation over both $\tilde{r}_{t}$ and $x_{t}$ ) $\displaystyle=\mu(\pi),$ $$

which implies $\operatornamewithlimits{\mathbb{E}}[\tilde{r}(\pi)]=\mu(\pi)$, as claimed. Now, let us use this estimate to set up a “clean event”: 

$$ $\left\{\mid\tilde{r}(\pi)-\mu(\pi)\mid\leq\mathtt{conf}(N)\text{ for all policies $\pi\in\Pi$}\right\},$ $$

where the confidence term is $\mathtt{conf}(N)=O(\sqrt{\frac{K\log(T|\Pi|)}{N}}).$ We can prove that the clean event does indeed happen with probability at least $1-\tfrac{1}{T}$, say, as an easy application of Chernoff Bounds. For intuition, the $K$ is present in the confidence radius is because the “fake rewards” $\tilde{r}_{t}(\cdot)$ could be as large as $K$. The $|\Pi|$ is there (inside the $\log$) because we take a Union Bound across all policies. And the $T$ is there because we need the “error probability” to be on the order of $\tfrac{1}{T}$.

Let $\pi^{*}=\pi^{*}_{\Pi}$ be an optimal policy. Since we have an exact classification oracle, $\tilde{r}(\pi_{0})$ is maximal among all policies $\pi\in\Pi$. In particular, $\tilde{r}(\pi_{0})\geq\tilde{r}(\pi^{*})$. If the clean event holds, then 

$$ $\mu(\pi^{\star})-\mu(\pi_{0})\leq 2\,\mathtt{conf}(N).$ $$

Thus, each round in exploitation contributes at most $\mathtt{conf}$ to expected regret. And each round of exploration contributes at most $1$. It follows that $\operatornamewithlimits{\mathbb{E}}[R_{\Pi}(T)]\leq N+2T\,\mathtt{conf}(N)$. Choosing $N$ so that $N=O(T\,\mathtt{conf}(N))$, we obtain $N=T^{2/3}(K\log(|\Pi|T))^{\frac{1}{3}}$ and $\operatornamewithlimits{\mathbb{E}}[R_{\Pi}(T)]=O(N)$. ∎

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 44 Contextual bandits with a policy class
