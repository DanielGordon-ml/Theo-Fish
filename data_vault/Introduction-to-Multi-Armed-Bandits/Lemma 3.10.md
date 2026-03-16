---
type: lemma
label: Lemma 3.10
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 17 Bayesian regret analysis
related_entities: []
date_extracted: '2026-03-16T01:32:59.474497+00:00'
---

# Lemma 3.10

Assume we have lower and upper bound functions that satisfy properties (47) and (48), for some parameter $\gamma>0$. Then Bayesian Regret of Thompson Sampling can be bounded as follows: $\mathtt{BR}(T)\leq \textstyle 2\gamma+2\sum_{t=1}^{T}\operatornamewithlimits{\mathbb{E}}\left[\,r(a_{t},\>H_{t})\,\right].$

## Proof

Fix round $t$. Interpreted as random variables, the chosen arm $a_{t}$ and the best arm $a^{*}$ are identically distributed given $t$-history $H_{t}$: for each feasible $t$-history $H$, $\Pr[a_{t}=a\mid H_{t}=H]=\Pr[a^{*}=a\mid H_{t}=H]\quad\text{for each arm $a$}$. It follows that $\operatornamewithlimits{\mathbb{E}}[\>U(a^{*},\>H)\>\mid\>H_{t}=H\>]=\operatornamewithlimits{\mathbb{E}}[\>U(a_{t},\>H)\>\mid\>H_{t}=H\>]$. (49) Then Bayesian Regret suffered in round $t$ is $\mathtt{BR}_{t}$ $:=\operatornamewithlimits{\mathbb{E}}\left[\,\mu(a^{*})-\mu(a_{t})\,\right]$ $=\operatornamewithlimits{\mathbb{E}}_{H\sim H_{t}}\left[\,\operatornamewithlimits{\mathbb{E}}\left[\,\mu(a^{*})-\mu(a_{t})\mid H_{t}=H\,\right]\,\right]$ $=\operatornamewithlimits{\mathbb{E}}_{H\sim H_{t}}\left[\,\operatornamewithlimits{\mathbb{E}}\left[\,U(a_{t},H)-\mu(a_{t})+\mu(a^{*})-U(a^{*},H)\mid H_{t}=H\,\right]\,\right]$ (by Eq. ( 49 )) $=\underbrace{\operatornamewithlimits{\mathbb{E}}\left[\,U(a_{t},H_{t})-\mu(a_{t})\,\right]}_{\text{Summand 1}}+\underbrace{\operatornamewithlimits{\mathbb{E}}\left[\,\mu(a^{*})-U(a^{*},H_{t})\,\right]}_{\text{Summand 2}}.$ We will use properties (47) and (48) to bound both summands. Note that we cannot *immediately* use these properties because they assume a fixed arm $a$, whereas both $a_{t}$ and $a^{*}$ are random variables. $\operatornamewithlimits{\mathbb{E}}\left[\,\mu(a^{*})-U(a^{*},H_{t})\,\right]$ (Summand 1) $\leq\operatornamewithlimits{\mathbb{E}}\left[\,(\mu(a^{*})-U(a^{*},H_{t}))^{+}\,\right]$ $\leq\operatornamewithlimits{\mathbb{E}}\left[\,\sum_{\text{arms $a$}}\left[\,\mu(a)-U(a,H_{t})\,\right]^{+}\,\right]$ $=\textstyle\sum_{\text{arms $a$}}\operatornamewithlimits{\mathbb{E}}\left[\,\left(\,U(a,H_{t})-\mu(a)\,\right)^{-}\,\right]$ $\leq K\cdot\frac{\gamma}{KT}=\frac{\gamma}{T}$ $\text{\emph{(by property (\ref{TS:eq:prop1}))}}.$ $\operatornamewithlimits{\mathbb{E}}\left[\,U(a_{t},H_{t})-\mu(a_{t})\,\right]$ (Summand 2) $=\operatornamewithlimits{\mathbb{E}}\left[\,2r(a_{t},H_{t})+L(a_{t},H_{t})-\mu(a_{t})\,\right]$ (by definition of $r_{t}(\cdot)$ ) $=\operatornamewithlimits{\mathbb{E}}\left[\,2r(a_{t},H_{t})\,\right]+\operatornamewithlimits{\mathbb{E}}\left[\,L(a_{t},H_{t})-\mu(a_{t})\,\right]$ $\operatornamewithlimits{\mathbb{E}}[L(a_{t},H_{t})-\mu(a_{t})]$ $\leq\operatornamewithlimits{\mathbb{E}}\left[\,\left(\,L(a_{t},H_{t})-\mu(a_{t})\,\right)^{+}\,\right]$ $\leq\operatornamewithlimits{\mathbb{E}}\left[\,\sum_{\text{arms $a$}}\left(\,L(a,H_{t})-\mu(a)\,\right)^{+}\,\right]$ $=\underset{\text{arms $a$}}{\sum}\operatornamewithlimits{\mathbb{E}}\left[\,\left(\,\mu(a)-L(a,H_{t})\,\right)^{-}\,\right]$ $\leq K\cdot\frac{\gamma}{KT}=\frac{\gamma}{T}$ $\text{\emph{(by property (\ref{TS:eq:prop2}))}}.$ Thus, $\mathtt{BR}_{t}(T)\leq 2\tfrac{\gamma}{T}+2\,\operatornamewithlimits{\mathbb{E}}[r(a_{t},H_{t})]$. The theorem follows by summing up over all rounds $t$. ∎

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 17 Bayesian regret analysis
