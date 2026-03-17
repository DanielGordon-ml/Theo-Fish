---
slug: introduction-to-multi-armed-bandits--theorem-5-6
label: Theorem 5.6
claim_type: theorem
statement: Consider binary prediction with experts advice. Assuming a perfect expert,
  the majority vote algorithm makes at most $\log_{2}K$ mistakes, where $K$ is the
  number of experts.
proof: Let $S_{t}$ be the set of experts who make no mistakes up to round $t$, and
  let $W_{t}=|S_{t}|$. Note that $W_{1}=K$, and $W_{t}\geq 1$ for all rounds $t$,
  because the perfect expert is always in $S_{t}$. If the algorithm makes a mistake
  at round $t$, then $W_{t+1}\leq W_{t}/2$ because the majority of experts in $S_{t}$
  is wrong and thus excluded from $S_{t+1}$. It follows that the algorithm cannot
  make more than $\log_{2}K$ mistakes.
strength: exact
status: unverified
human_notes: ''
about:
- '[[concepts/perfect-expert]]'
- '[[concepts/majority-vote-algorithm]]'
- '[[concepts/binary-prediction-with-expert-advice-problem]]'
- '[[concepts/number-of-experts-k]]'
- '[[concepts/mistake]]'
about_meta:
- target: '[[concepts/perfect-expert]]'
  role: primary
  aspect: ''
- target: '[[concepts/majority-vote-algorithm]]'
  role: primary
  aspect: ''
- target: '[[concepts/binary-prediction-with-expert-advice-problem]]'
  role: primary
  aspect: ''
- target: '[[concepts/number-of-experts-k]]'
  role: primary
  aspect: ''
- target: '[[concepts/mistake]]'
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

# Theorem 5.6

Consider binary prediction with experts advice. Assuming a perfect expert, the majority vote algorithm makes at most $\log_{2}K$ mistakes, where $K$ is the number of experts.


## Proof

Let $S_{t}$ be the set of experts who make no mistakes up to round $t$, and let $W_{t}=|S_{t}|$. Note that $W_{1}=K$, and $W_{t}\geq 1$ for all rounds $t$, because the perfect expert is always in $S_{t}$. If the algorithm makes a mistake at round $t$, then $W_{t+1}\leq W_{t}/2$ because the majority of experts in $S_{t}$ is wrong and thus excluded from $S_{t+1}$. It follows that the algorithm cannot make more than $\log_{2}K$ mistakes.
