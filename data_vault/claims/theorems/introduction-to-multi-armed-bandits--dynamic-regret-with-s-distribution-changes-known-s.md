---
slug: introduction-to-multi-armed-bandits--dynamic-regret-with-s-distribution-changes-known-s
label: Dynamic regret with S distribution changes (known S)
claim_type: theorem
statement: Assume the adversary changes the cost distribution at most $S$ times. One
  can re-use results for shifting regret, so as to obtain expected dynamic regret
  $\tilde{O}(\sqrt{SKT})$ when $S$ is known. This regret bound is optimal (Garivier
  and Moulines, 2011).
proof: ''
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/adversarial-bandits-problem]]'
- '[[concepts/randomized-oblivious-adversary]]'
- '[[concepts/dynamic-regret]]'
about_meta:
- target: '[[concepts/adversarial-bandits-problem]]'
  role: primary
  aspect: ''
- target: '[[concepts/randomized-oblivious-adversary]]'
  role: primary
  aspect: ''
- target: '[[concepts/dynamic-regret]]'
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

# Dynamic regret with S distribution changes (known S)

Assume the adversary changes the cost distribution at most $S$ times. One can re-use results for shifting regret, so as to obtain expected dynamic regret $\tilde{O}(\sqrt{SKT})$ when $S$ is known. This regret bound is optimal (Garivier and Moulines, 2011).
