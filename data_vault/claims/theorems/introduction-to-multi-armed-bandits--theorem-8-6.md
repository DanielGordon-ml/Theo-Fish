---
slug: introduction-to-multi-armed-bandits--theorem-8-6
label: Theorem 8.6
claim_type: theorem
statement: Consider contextual bandits with policy class $\Pi$. Algorithm $\mathtt{Exp4}$
  with expert set $\Pi$ yields regret $\operatornamewithlimits{\mathbb{E}}[R_{\Pi}(T)]=O(\sqrt{KT\log|\Pi|})$.
  However, the running time per round is linear in $|\Pi|$.
proof: ''
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/regret-relative-to-policy-class-pi-r-pi-t]]'
- '[[concepts/number-of-arms-k]]'
- '[[concepts/time-horizon-t]]'
- '[[concepts/contextual-bandits-with-fixed-policy-class]]'
- '[[concepts/policy-class-pi]]'
- '[[concepts/exp4-algorithm]]'
about_meta:
- target: '[[concepts/regret-relative-to-policy-class-pi-r-pi-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-arms-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/time-horizon-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/contextual-bandits-with-fixed-policy-class]]'
  role: primary
  aspect: ''
- target: '[[concepts/policy-class-pi]]'
  role: primary
  aspect: ''
- target: '[[concepts/exp4-algorithm]]'
  role: primary
  aspect: ''
depends_on:
- '[[claims/introduction-to-multi-armed-bandits--theorem-6-11]]'
depends_on_meta:
- target: '[[claims/introduction-to-multi-armed-bandits--theorem-6-11]]'
sourced_from:
- '[[sources/1904.07272|Introduction to Multi-Armed Bandits]]'
sourced_from_meta:
- target: '[[sources/1904.07272|Introduction to Multi-Armed Bandits]]'
  section: ''
  page: ''
  confidence: 0.0
---

# Theorem 8.6

Consider contextual bandits with policy class $\Pi$. Algorithm $\mathtt{Exp4}$ with expert set $\Pi$ yields regret $\operatornamewithlimits{\mathbb{E}}[R_{\Pi}(T)]=O(\sqrt{KT\log|\Pi|})$. However, the running time per round is linear in $|\Pi|$.
