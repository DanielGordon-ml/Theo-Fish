---
slug: introduction-to-multi-armed-bandits--claim-7-13
label: Claim 7.13
claim_type: lemma
statement: For all rounds $i < j$, $\sum_{t=i}^{j} v_t \cdot M(v_{i:t}) \leq v_{i:j}
  \cdot M(v_{i:j})$.
proof: 'The proof is by induction on $j - i$. The claim is trivially satisfied for
  the base case $i = j$. For the inductive step: $\sum_{t=i}^{j-1} v_t \cdot M(v_{i:t})
  \leq v_{i:j-1} \cdot M(v_{i:j-1})$ (by the inductive hypothesis) $\leq v_{i:j-1}
  \cdot M(v_{i:j})$ (by (97) with $a = M(v_{i:j})$). Add $v_j \cdot M(v_{i:j})$ to
  both sides to complete the proof.'
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/optimization-oracle]]'
- '[[concepts/online-linear-optimization]]'
- '[[concepts/cost-evaluation-function]]'
about_meta:
- target: '[[concepts/optimization-oracle]]'
  role: primary
  aspect: ''
- target: '[[concepts/online-linear-optimization]]'
  role: primary
  aspect: ''
- target: '[[concepts/cost-evaluation-function]]'
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

# Claim 7.13

For all rounds $i < j$, $\sum_{t=i}^{j} v_t \cdot M(v_{i:t}) \leq v_{i:j} \cdot M(v_{i:j})$.


## Proof

The proof is by induction on $j - i$. The claim is trivially satisfied for the base case $i = j$. For the inductive step: $\sum_{t=i}^{j-1} v_t \cdot M(v_{i:t}) \leq v_{i:j-1} \cdot M(v_{i:j-1})$ (by the inductive hypothesis) $\leq v_{i:j-1} \cdot M(v_{i:j})$ (by (97) with $a = M(v_{i:j})$). Add $v_j \cdot M(v_{i:j})$ to both sides to complete the proof.
