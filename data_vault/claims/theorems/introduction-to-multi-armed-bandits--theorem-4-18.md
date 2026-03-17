---
slug: introduction-to-multi-armed-bandits--theorem-4-18
label: Theorem 4.18
claim_type: theorem
statement: Consider Lipschitz bandits with time horizon T. Assume that realized rewards
  take values on a finite set. For any given problem instance and any c > 0, the zooming
  algorithm attains regret E[R(T)] ≤ O(T^{(d+1)/(d+2)} (c log T)^{1/(d+2)}), where
  d is the zooming dimension with multiplier c.
proof: "Assuming the clean event E (which holds with probability ≥ 1 - 1/T² by Claim\
  \ 4.13), we analyze regret via covering numbers.\n\nFor r > 0, consider X_r = {x\
  \ ∈ X : r ≤ Δ(x) < 2r}. Fix i ∈ N and let Y_i = X_r where r = 2^{-i}. By Corollary\
  \ 4.15, for any two arms x, y ∈ Y_i, we have D(x,y) > r/3. If we cover Y_i with\
  \ subsets of diameter r/3, then arms x and y cannot lie in the same subset. Since\
  \ one can cover Y_i with N_{r/3}(Y_i) such subsets, it follows that |Y_i| ≤ N_{r/3}(Y_i).\n\
  \nUsing Corollary 4.16:\nR_i(T) := Σ_{x ∈ Y_i} Δ(x) · n_t(x) ≤ O(log T)/Δ(x) · N_{r/3}(Y_i)\
  \ ≤ O(log T)/r · N_{r/3}(Y_i).\n\nPick δ > 0, and consider arms with Δ(·) ≤ δ separately\
  \ from those with Δ(·) > δ. The total regret from the former cannot exceed δ per\
  \ round. Therefore:\n\nR(T) ≤ δT + Σ_{i: r=2^{-i} > δ} R_i(T)\n     ≤ δT + Σ_{i:\
  \ r=2^{-i} > δ} Θ(log T)/r · N_{r/3}(Y_i)\n     ≤ δT + O(c · log T) · (1/δ)^{d+1}\n\
  \nwhere d is the zooming dimension with multiplier c, so that N_{r/3}(X_r) ≤ c ·\
  \ r^{-d} for all r > 0.\n\nChoosing δ = (log T / T)^{1/(d+2)}:\nR(T) ≤ O(T^{(d+1)/(d+2)}\
  \ (c log T)^{1/(d+2)}).\n\nNote this choice is made in the analysis only; the algorithm\
  \ does not depend on δ."
strength: asymptotic
status: unverified
human_notes: ''
about:
- '[[concepts/expected-regret-r-t]]'
- '[[concepts/zooming-algorithm-for-lipschitz-bandits]]'
- '[[concepts/regret-bound]]'
- '[[concepts/zooming-dimension]]'
- '[[concepts/lipschitz-bandits-problem]]'
- '[[concepts/covering-number]]'
about_meta:
- target: '[[concepts/expected-regret-r-t]]'
  role: primary
  aspect: ''
- target: '[[concepts/zooming-algorithm-for-lipschitz-bandits]]'
  role: primary
  aspect: ''
- target: '[[concepts/regret-bound]]'
  role: primary
  aspect: ''
- target: '[[concepts/zooming-dimension]]'
  role: primary
  aspect: ''
- target: '[[concepts/lipschitz-bandits-problem]]'
  role: primary
  aspect: ''
- target: '[[concepts/covering-number]]'
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

# Theorem 4.18

Consider Lipschitz bandits with time horizon T. Assume that realized rewards take values on a finite set. For any given problem instance and any c > 0, the zooming algorithm attains regret E[R(T)] ≤ O(T^{(d+1)/(d+2)} (c log T)^{1/(d+2)}), where d is the zooming dimension with multiplier c.


## Proof

Assuming the clean event E (which holds with probability ≥ 1 - 1/T² by Claim 4.13), we analyze regret via covering numbers.

For r > 0, consider X_r = {x ∈ X : r ≤ Δ(x) < 2r}. Fix i ∈ N and let Y_i = X_r where r = 2^{-i}. By Corollary 4.15, for any two arms x, y ∈ Y_i, we have D(x,y) > r/3. If we cover Y_i with subsets of diameter r/3, then arms x and y cannot lie in the same subset. Since one can cover Y_i with N_{r/3}(Y_i) such subsets, it follows that |Y_i| ≤ N_{r/3}(Y_i).

Using Corollary 4.16:
R_i(T) := Σ_{x ∈ Y_i} Δ(x) · n_t(x) ≤ O(log T)/Δ(x) · N_{r/3}(Y_i) ≤ O(log T)/r · N_{r/3}(Y_i).

Pick δ > 0, and consider arms with Δ(·) ≤ δ separately from those with Δ(·) > δ. The total regret from the former cannot exceed δ per round. Therefore:

R(T) ≤ δT + Σ_{i: r=2^{-i} > δ} R_i(T)
     ≤ δT + Σ_{i: r=2^{-i} > δ} Θ(log T)/r · N_{r/3}(Y_i)
     ≤ δT + O(c · log T) · (1/δ)^{d+1}

where d is the zooming dimension with multiplier c, so that N_{r/3}(X_r) ≤ c · r^{-d} for all r > 0.

Choosing δ = (log T / T)^{1/(d+2)}:
R(T) ≤ O(T^{(d+1)/(d+2)} (c log T)^{1/(d+2)}).

Note this choice is made in the analysis only; the algorithm does not depend on δ.
