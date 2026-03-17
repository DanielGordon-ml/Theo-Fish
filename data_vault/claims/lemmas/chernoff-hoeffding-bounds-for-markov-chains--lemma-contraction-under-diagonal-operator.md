---
slug: chernoff-hoeffding-bounds-for-markov-chains--lemma-contraction-under-diagonal-operator
label: Lemma (Contraction under diagonal operator)
claim_type: lemma
statement: For an ergodic Markov chain M with stationary distribution π and spectral
  expansion λ, and for any vector x ∈ L²(π) orthogonal to π (i.e., x·1 = 0), ‖xM‖_π
  ≤ λ‖x‖_π. Furthermore, for any diagonal matrix P with entries in [0,1], writing
  xPM = (xPM)^∥ + (xPM)^⊥ where (xPM)^∥ is the component parallel to π and (xPM)^⊥
  is the component perpendicular to π, we have ‖(xPM)^⊥‖_π ≤ λ·‖x‖_π·‖P‖_∞ and the
  total norm ‖xPM‖_π ≤ (1+λ)/2 · ‖x‖_π when entries of P are in [0,1].
proof: ''
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/orthogonality-with-pi]]'
- '[[concepts/l-pi-space]]'
- '[[concepts/spectral-expansion-lambda-m]]'
- '[[concepts/contraction-mapping]]'
- '[[concepts/perpendicular-component-operator]]'
- '[[concepts/parallel-component-operator]]'
about_meta:
- target: '[[concepts/orthogonality-with-pi]]'
  role: primary
  aspect: ''
- target: '[[concepts/l-pi-space]]'
  role: primary
  aspect: ''
- target: '[[concepts/spectral-expansion-lambda-m]]'
  role: primary
  aspect: ''
- target: '[[concepts/contraction-mapping]]'
  role: primary
  aspect: ''
- target: '[[concepts/perpendicular-component-operator]]'
  role: primary
  aspect: ''
- target: '[[concepts/parallel-component-operator]]'
  role: primary
  aspect: ''
depends_on: []
depends_on_meta: []
sourced_from:
- '[[sources/chernoff_hoeffding_bounds_for_markov_chains|chernoff_hoeffding_bounds_for_markov_chains]]'
sourced_from_meta:
- target: '[[sources/chernoff_hoeffding_bounds_for_markov_chains|chernoff_hoeffding_bounds_for_markov_chains]]'
  section: ''
  page: ''
  confidence: 0.0
---

# Lemma (Contraction under diagonal operator)

For an ergodic Markov chain M with stationary distribution π and spectral expansion λ, and for any vector x ∈ L²(π) orthogonal to π (i.e., x·1 = 0), ‖xM‖_π ≤ λ‖x‖_π. Furthermore, for any diagonal matrix P with entries in [0,1], writing xPM = (xPM)^∥ + (xPM)^⊥ where (xPM)^∥ is the component parallel to π and (xPM)^⊥ is the component perpendicular to π, we have ‖(xPM)^⊥‖_π ≤ λ·‖x‖_π·‖P‖_∞ and the total norm ‖xPM‖_π ≤ (1+λ)/2 · ‖x‖_π when entries of P are in [0,1].
