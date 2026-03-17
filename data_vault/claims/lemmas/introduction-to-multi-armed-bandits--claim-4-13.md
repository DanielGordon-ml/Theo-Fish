---
slug: introduction-to-multi-armed-bandits--claim-4-13
label: Claim 4.13
claim_type: lemma
statement: Assume that realized rewards take values on a finite set. Then Pr[E] ≥
  1 - 1/T².
proof: 'By Hoeffding Inequality, Pr[E_x] ≥ 1 - 1/T⁴ for each arm x ∈ X. However, one
  cannot immediately apply the Union Bound here because there may be too many arms.


  Fix an instance of Lipschitz bandits. Let X₀ be the set of all arms that can possibly
  be activated by the algorithm on this problem instance. Note that X₀ is finite;
  this is because the algorithm is deterministic, the time horizon T is fixed, and,
  as we assumed upfront, realized rewards can take only finitely many values. (This
  is the only place where we use this assumption.)


  Let N be the total number of arms activated by the algorithm. Define arms y_j ∈
  X₀, j ∈ [T], as follows:

  y_j = j-th arm activated, if j ≤ N; y_N, otherwise.


  Here N and y_j''s are random variables, the randomness coming from the reward realizations.
  Note that {y₁, ..., y_T} is precisely the set of arms activated in a given execution
  of the algorithm. Since the clean event holds trivially for all arms that are not
  activated, the clean event can be rewritten as E = ∩_{j=1}^T E_{y_j}.


  In what follows, we prove that the clean event E_{y_j} happens with high probability
  for each j ∈ [T].


  Fix an arm x ∈ X₀ and fix j ∈ [T]. Whether the event {y_j = x} holds is determined
  by the rewards of other arms. (Indeed, by the time arm x is selected by the algorithm,
  it is already determined whether x is the j-th arm activated!) Whereas whether the
  clean event E_x holds is determined by the rewards of arm x alone. It follows that
  the events {y_j = x} and E_x are independent. Therefore, if Pr[y_j = x] > 0 then


  Pr[E_{y_j} | y_j = x] = Pr[E_x | y_j = x] = Pr[E_x] ≥ 1 - 1/T⁴


  Now we can sum over all x ∈ X₀:


  Pr[E_{y_j}] = Σ_{x ∈ X₀} Pr[y_j = x] · Pr[E_{y_j} | x = y_j] ≥ 1 - 1/T⁴


  To complete the proof, we apply the Union bound over all j ∈ [T]:


  Pr[E_{y_j}, j ∈ [T]] ≥ 1 - 1/T³.'
strength: ''
status: unverified
human_notes: ''
about:
- '[[concepts/confidence-radius-r-t-a]]'
- '[[concepts/zooming-algorithm-for-lipschitz-bandits]]'
- '[[concepts/hoeffding-inequality]]'
- '[[concepts/clean-event]]'
about_meta:
- target: '[[concepts/confidence-radius-r-t-a]]'
  role: primary
  aspect: ''
- target: '[[concepts/zooming-algorithm-for-lipschitz-bandits]]'
  role: primary
  aspect: ''
- target: '[[concepts/hoeffding-inequality]]'
  role: primary
  aspect: ''
- target: '[[concepts/clean-event]]'
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

# Claim 4.13

Assume that realized rewards take values on a finite set. Then Pr[E] ≥ 1 - 1/T².


## Proof

By Hoeffding Inequality, Pr[E_x] ≥ 1 - 1/T⁴ for each arm x ∈ X. However, one cannot immediately apply the Union Bound here because there may be too many arms.

Fix an instance of Lipschitz bandits. Let X₀ be the set of all arms that can possibly be activated by the algorithm on this problem instance. Note that X₀ is finite; this is because the algorithm is deterministic, the time horizon T is fixed, and, as we assumed upfront, realized rewards can take only finitely many values. (This is the only place where we use this assumption.)

Let N be the total number of arms activated by the algorithm. Define arms y_j ∈ X₀, j ∈ [T], as follows:
y_j = j-th arm activated, if j ≤ N; y_N, otherwise.

Here N and y_j's are random variables, the randomness coming from the reward realizations. Note that {y₁, ..., y_T} is precisely the set of arms activated in a given execution of the algorithm. Since the clean event holds trivially for all arms that are not activated, the clean event can be rewritten as E = ∩_{j=1}^T E_{y_j}.

In what follows, we prove that the clean event E_{y_j} happens with high probability for each j ∈ [T].

Fix an arm x ∈ X₀ and fix j ∈ [T]. Whether the event {y_j = x} holds is determined by the rewards of other arms. (Indeed, by the time arm x is selected by the algorithm, it is already determined whether x is the j-th arm activated!) Whereas whether the clean event E_x holds is determined by the rewards of arm x alone. It follows that the events {y_j = x} and E_x are independent. Therefore, if Pr[y_j = x] > 0 then

Pr[E_{y_j} | y_j = x] = Pr[E_x | y_j = x] = Pr[E_x] ≥ 1 - 1/T⁴

Now we can sum over all x ∈ X₀:

Pr[E_{y_j}] = Σ_{x ∈ X₀} Pr[y_j = x] · Pr[E_{y_j} | x = y_j] ≥ 1 - 1/T⁴

To complete the proof, we apply the Union bound over all j ∈ [T]:

Pr[E_{y_j}, j ∈ [T]] ≥ 1 - 1/T³.
