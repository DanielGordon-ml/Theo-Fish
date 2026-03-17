---
slug: introduction-to-multi-armed-bandits--opt-fd-vs-opt-fa-gap-example
label: OPT_FD vs OPT_FA gap example
claim_type: proposition
statement: Generalizing the example above, $\mathtt{OPT_{FD}}$ could be up to $d$
  times larger than $\mathtt{OPT_{FA}}$.
proof: There are two arms $a \in \{1,2\}$ and two resources $i \in \{1,2\}$ other
  than time. In each round, each arm $a$ yields reward $1$, and consumes ${\bf 1}_{\{a=i\}}$
  units of each resource $i$. Both resources have budget $B$, and time horizon is
  $T=2B$. Then always playing the same arm gives the total reward of $B$, whereas
  alternating the two arms gives the total reward of $2B$. Choosing an arm uniformly
  (and independently) in each round yields the same expected total reward of $2B$,
  up to a low-order error term.
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/fixed-distribution-over-arms]]'
- '[[concepts/opt-fa]]'
- '[[concepts/fixed-arm]]'
- '[[concepts/bandits-with-knapsacks]]'
- '[[concepts/opt-fd]]'
about_meta:
- target: '[[concepts/fixed-distribution-over-arms]]'
  role: primary
  aspect: ''
- target: '[[concepts/opt-fa]]'
  role: primary
  aspect: ''
- target: '[[concepts/fixed-arm]]'
  role: primary
  aspect: ''
- target: '[[concepts/bandits-with-knapsacks]]'
  role: primary
  aspect: ''
- target: '[[concepts/opt-fd]]'
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

# OPT_FD vs OPT_FA gap example

Generalizing the example above, $\mathtt{OPT_{FD}}$ could be up to $d$ times larger than $\mathtt{OPT_{FA}}$.


## Proof

There are two arms $a \in \{1,2\}$ and two resources $i \in \{1,2\}$ other than time. In each round, each arm $a$ yields reward $1$, and consumes ${\bf 1}_{\{a=i\}}$ units of each resource $i$. Both resources have budget $B$, and time horizon is $T=2B$. Then always playing the same arm gives the total reward of $B$, whereas alternating the two arms gives the total reward of $2B$. Choosing an arm uniformly (and independently) in each round yields the same expected total reward of $2B$, up to a low-order error term.
