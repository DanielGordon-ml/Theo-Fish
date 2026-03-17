---
slug: introduction-to-multi-armed-bandits--theorem-5-16
label: Theorem 5.16
claim_type: theorem
statement: 'Assume $\sum_{t\in[T]}\;\operatornamewithlimits{\mathbb{E}}[G_{t}]\leq
  uT$ for some known number $u$, where $\operatornamewithlimits{\mathbb{E}}[G_{t}]=\operatornamewithlimits{\mathbb{E}}\left[\,c_{t}^{2}(a_{t})\,\right]$
  as per (81). Then $\mathtt{Hedge}$ with parameter $\epsilon=\sqrt{\frac{\ln K}{3uT}}$
  achieves regret

  $$\operatornamewithlimits{\mathbb{E}}[\mathtt{cost}(\mathtt{ALG})-\mathtt{cost}^{*}]<2\sqrt{3}\cdot\sqrt{uT\ln{K}}.$$

  In particular, if $c_{t}(\cdot)\leq c$, for some known $c$, then one can take $u=c^{2}$.'
proof: 'We use Eq. (83) with $\alpha=\ln(\frac{1}{1-\epsilon})$ and $\beta=\alpha^{2}$
  to obtain:

  $$\alpha\operatornamewithlimits{\mathbb{E}}[\mathtt{cost}(\mathtt{ALG})]<\alpha^{2}\sum_{t\in[T]}\operatornamewithlimits{\mathbb{E}}[G_{t}]+\ln{K}+\alpha\operatornamewithlimits{\mathbb{E}}[\mathtt{cost}^{*}].$$

  Dividing both sides by $\alpha$ and moving terms around, we get

  $$\operatornamewithlimits{\mathbb{E}}[\mathtt{cost}(\mathtt{ALG})-\mathtt{cost}^{*}]<\frac{\ln{K}}{\alpha}+\alpha\sum_{t\in[T]}\operatornamewithlimits{\mathbb{E}}[G_{t}]<\frac{\ln{K}}{\epsilon}+3\epsilon\sum_{t\in[T]}\operatornamewithlimits{\mathbb{E}}[G_{t}],$$

  where the last step uses the fact that $\epsilon<\alpha<3\epsilon$ for $\epsilon\in(0,\nicefrac{1}{2})$.
  Substituting $\epsilon=\sqrt{\frac{\ln K}{3uT}}$ and $\sum_{t\in[T]}\operatornamewithlimits{\mathbb{E}}[G_{t}]\leq
  uT$, we get $\frac{\ln K}{\epsilon}+3\epsilon\cdot uT = \sqrt{3uT\ln K}+\sqrt{3uT\ln
  K}=2\sqrt{3uT\ln K}$.'
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/hedge]]'
- '[[concepts/g-t]]'
- '[[concepts/online-learning-with-experts]]'
- '[[concepts/regret]]'
about_meta:
- target: '[[concepts/hedge]]'
  role: primary
  aspect: ''
- target: '[[concepts/g-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/online-learning-with-experts]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret]]'
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

# Theorem 5.16

Assume $\sum_{t\in[T]}\;\operatornamewithlimits{\mathbb{E}}[G_{t}]\leq uT$ for some known number $u$, where $\operatornamewithlimits{\mathbb{E}}[G_{t}]=\operatornamewithlimits{\mathbb{E}}\left[\,c_{t}^{2}(a_{t})\,\right]$ as per (81). Then $\mathtt{Hedge}$ with parameter $\epsilon=\sqrt{\frac{\ln K}{3uT}}$ achieves regret
$$\operatornamewithlimits{\mathbb{E}}[\mathtt{cost}(\mathtt{ALG})-\mathtt{cost}^{*}]<2\sqrt{3}\cdot\sqrt{uT\ln{K}}.$$
In particular, if $c_{t}(\cdot)\leq c$, for some known $c$, then one can take $u=c^{2}$.


## Proof

We use Eq. (83) with $\alpha=\ln(\frac{1}{1-\epsilon})$ and $\beta=\alpha^{2}$ to obtain:
$$\alpha\operatornamewithlimits{\mathbb{E}}[\mathtt{cost}(\mathtt{ALG})]<\alpha^{2}\sum_{t\in[T]}\operatornamewithlimits{\mathbb{E}}[G_{t}]+\ln{K}+\alpha\operatornamewithlimits{\mathbb{E}}[\mathtt{cost}^{*}].$$
Dividing both sides by $\alpha$ and moving terms around, we get
$$\operatornamewithlimits{\mathbb{E}}[\mathtt{cost}(\mathtt{ALG})-\mathtt{cost}^{*}]<\frac{\ln{K}}{\alpha}+\alpha\sum_{t\in[T]}\operatornamewithlimits{\mathbb{E}}[G_{t}]<\frac{\ln{K}}{\epsilon}+3\epsilon\sum_{t\in[T]}\operatornamewithlimits{\mathbb{E}}[G_{t}],$$
where the last step uses the fact that $\epsilon<\alpha<3\epsilon$ for $\epsilon\in(0,\nicefrac{1}{2})$. Substituting $\epsilon=\sqrt{\frac{\ln K}{3uT}}$ and $\sum_{t\in[T]}\operatornamewithlimits{\mathbb{E}}[G_{t}]\leq uT$, we get $\frac{\ln K}{\epsilon}+3\epsilon\cdot uT = \sqrt{3uT\ln K}+\sqrt{3uT\ln K}=2\sqrt{3uT\ln K}$.
