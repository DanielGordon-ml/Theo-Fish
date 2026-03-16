---
type: theorem
label: Theorem 11.15
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 64 Repeated hidden exploration
related_entities: []
date_extracted: '2026-03-16T01:32:59.561418+00:00'
---

# Theorem 11.15

$\mathtt{RepeatedHE}$ with exploration probability $\epsilon>0$ and $N_{0}$ initial samples of arm $1$ is BIC as long as $\epsilon<\tfrac{1}{3}\,\operatornamewithlimits{\mathbb{E}}\left[G\cdot{\bf 1}_{\left\{\,G>0\,\right\}}\right]$, where $G=G_{N_{0}+1}$.

## Proof

The only remaining piece is the claim that the quantity $\operatornamewithlimits{\mathbb{E}}\left[G_{t}\cdot{\bf 1}_{\left\{\,G_{t}>0\,\right\}}\right]$ does not decrease over time. This claim holds for any sequence of signals $(\mathcal{S}_{1},\mathcal{S}_{2}\,,\ \ldots\ ,S_{T})$ such that each signal $S_{t}$ is determined by the next signal $S_{t+1}$. Fix round $t$. Applying Fact 11.6 twice, we obtain $\displaystyle\operatornamewithlimits{\mathbb{E}}[G_{t}\mid G_{t}>0]=\operatornamewithlimits{\mathbb{E}}[\mu_{2}-\mu_{1}\mid G_{t}>0]=\operatornamewithlimits{\mathbb{E}}[G_{t+1}\mid G_{t}>0]$. (The last equality uses the fact that $S_{t+1}$ determines $S_{t}$.) Then, $\displaystyle\operatornamewithlimits{\mathbb{E}}\left[G_{t}\cdot{\bf 1}_{\left\{\,G_{t}>0\,\right\}}\right] =\operatornamewithlimits{\mathbb{E}}[G_{t}\mid G_{t}>0]\cdot\Pr[G_{t}>0] =\operatornamewithlimits{\mathbb{E}}[G_{t+1}\mid G_{t}>0]\cdot\Pr[G_{t}>0] =\operatornamewithlimits{\mathbb{E}}\left[G_{t+1}\cdot{\bf 1}_{\left\{\,G_{t}>0\,\right\}}\right] \leq\operatornamewithlimits{\mathbb{E}}\left[G_{t+1}\cdot{\bf 1}_{\left\{\,G_{t+1}>0\,\right\}}\right]$. The last inequality holds because $x\cdot{\bf 1}_{\left\{\,\cdot\,\right\}}\leq x\cdot{\bf 1}_{\left\{\,x>0\,\right\}}$ for any $x\in R$.

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 64 Repeated hidden exploration
