---
slug: chernoff-hoeffding-bounds-for-markov-chains--proposition-v-1-comparison-with-gillman-wagner-for-reversible-chains
label: Proposition V.1 (Comparison with Gillman/Wagner for reversible chains)
claim_type: proposition
statement: For ergodic reversible Markov chains, the Hoeffding bound in Theorem I.3
  recovers Gillman's result (Theorem V.1) since λ(M) = 1 − γ(M) for reversible chains,
  giving Pr[X ≥ μ + δ] ≤ ‖φ/π‖_π · exp(−2γδ²/t). The Chernoff bound in Theorem I.2
  gives Pr[X ≥ (1+δ)μ] ≤ ‖φ/π‖_π · exp(−γμδ²/3), which improves on Wagner's Theorem
  V.2 by removing the log factor and replacing n with ‖φ/π‖_π.
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/spectral-gap]]'
- '[[concepts/chernoff-bound-for-markov-chains]]'
- '[[concepts/reversible-markov-chain]]'
- '[[concepts/spectral-expansion-lambda-m]]'
about_meta:
- target: '[[concepts/spectral-gap]]'
  role: primary
  aspect: ''
- target: '[[concepts/chernoff-bound-for-markov-chains]]'
  role: primary
  aspect: ''
- target: '[[concepts/reversible-markov-chain]]'
  role: primary
  aspect: ''
- target: '[[concepts/spectral-expansion-lambda-m]]'
  role: primary
  aspect: ''
depends_on:
- '[[claims/chernoff-hoeffding-bounds-for-markov-chains--theorem-i-2]]'
- '[[claims/chernoff-hoeffding-bounds-for-markov-chains--theorem-i-3]]'
depends_on_meta:
- target: '[[claims/chernoff-hoeffding-bounds-for-markov-chains--theorem-i-2]]'
- target: '[[claims/chernoff-hoeffding-bounds-for-markov-chains--theorem-i-3]]'
sourced_from:
- '[[sources/chernoff_hoeffding_bounds_for_markov_chains|chernoff_hoeffding_bounds_for_markov_chains]]'
sourced_from_meta:
- target: '[[sources/chernoff_hoeffding_bounds_for_markov_chains|chernoff_hoeffding_bounds_for_markov_chains]]'
  section: ''
  page: ''
  confidence: 0.0
---

# Proposition V.1 (Comparison with Gillman/Wagner for reversible chains)

For ergodic reversible Markov chains, the Hoeffding bound in Theorem I.3 recovers Gillman's result (Theorem V.1) since λ(M) = 1 − γ(M) for reversible chains, giving Pr[X ≥ μ + δ] ≤ ‖φ/π‖_π · exp(−2γδ²/t). The Chernoff bound in Theorem I.2 gives Pr[X ≥ (1+δ)μ] ≤ ‖φ/π‖_π · exp(−γμδ²/3), which improves on Wagner's Theorem V.2 by removing the log factor and replacing n with ‖φ/π‖_π.
