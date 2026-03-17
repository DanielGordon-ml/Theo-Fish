---
slug: introduction-to-multi-armed-bandits--theorem-6-11
label: Theorem 6.11
claim_type: theorem
statement: Consider adversarial bandits with expert advice, with a deterministic-oblivious
  adversary. Algorithm $\mathtt{Exp4}$ with parameters $\gamma\in[0,\tfrac{1}{2T})$
  and $\epsilon=\epsilon_{U}$, $U=\tfrac{K}{1-\gamma}$, achieves regret $\operatornamewithlimits{\mathbb{E}}[R(T)]\leq
  2\sqrt{3}\cdot\sqrt{TK\log N}+1.$
proof: 'From the analysis: $\operatornamewithlimits{\mathbb{E}}\left[\,\widehat{R}_{\mathtt{Hedge}}(T)\,\right]\leq
  2\sqrt{3/(1-\gamma)}\cdot\sqrt{TK\log N}$ using Lemma 6.10 and the regret bound
  for Hedge (Theorem 6.1) with $u=\tfrac{K}{1-\gamma}$. Then $\operatornamewithlimits{\mathbb{E}}\left[\,R_{\mathtt{Exp4}}(T)\,\right]\leq
  2\sqrt{3/(1-\gamma)}\cdot\sqrt{TK\log N}+\gamma T$ by Eq. (89), which gives $\leq
  2\sqrt{3}\cdot\sqrt{TK\log N}+2\gamma T$ since $\sqrt{1/(1-\gamma)}\leq 1+\gamma$.
  This was derived assuming w.l.o.g. that $2\sqrt{3}\cdot\sqrt{TK\log N}\leq T$. This
  holds for any $\gamma>0$, and choosing $\gamma\in[0,\tfrac{1}{2T})$ gives $\gamma
  T < 1/2$, yielding the result.'
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/number-of-arms-k]]'
- '[[concepts/deterministic-oblivious-adversary]]'
- '[[concepts/exp4]]'
- '[[concepts/time-horizon-t]]'
- '[[concepts/adversarial-bandits-with-expert-advice]]'
- '[[concepts/number-of-experts]]'
- '[[concepts/regret]]'
- '[[concepts/hedge]]'
about_meta:
- target: '[[concepts/number-of-arms-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/deterministic-oblivious-adversary]]'
  role: primary
  aspect: ''
- target: '[[concepts/exp4]]'
  role: primary
  aspect: ''
- target: '[[concepts/time-horizon-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/adversarial-bandits-with-expert-advice]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-experts]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret]]'
  role: primary
  aspect: ''
- target: '[[concepts/hedge]]'
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

# Theorem 6.11

Consider adversarial bandits with expert advice, with a deterministic-oblivious adversary. Algorithm $\mathtt{Exp4}$ with parameters $\gamma\in[0,\tfrac{1}{2T})$ and $\epsilon=\epsilon_{U}$, $U=\tfrac{K}{1-\gamma}$, achieves regret $\operatornamewithlimits{\mathbb{E}}[R(T)]\leq 2\sqrt{3}\cdot\sqrt{TK\log N}+1.$


## Proof

From the analysis: $\operatornamewithlimits{\mathbb{E}}\left[\,\widehat{R}_{\mathtt{Hedge}}(T)\,\right]\leq 2\sqrt{3/(1-\gamma)}\cdot\sqrt{TK\log N}$ using Lemma 6.10 and the regret bound for Hedge (Theorem 6.1) with $u=\tfrac{K}{1-\gamma}$. Then $\operatornamewithlimits{\mathbb{E}}\left[\,R_{\mathtt{Exp4}}(T)\,\right]\leq 2\sqrt{3/(1-\gamma)}\cdot\sqrt{TK\log N}+\gamma T$ by Eq. (89), which gives $\leq 2\sqrt{3}\cdot\sqrt{TK\log N}+2\gamma T$ since $\sqrt{1/(1-\gamma)}\leq 1+\gamma$. This was derived assuming w.l.o.g. that $2\sqrt{3}\cdot\sqrt{TK\log N}\leq T$. This holds for any $\gamma>0$, and choosing $\gamma\in[0,\tfrac{1}{2T})$ gives $\gamma T < 1/2$, yielding the result.
