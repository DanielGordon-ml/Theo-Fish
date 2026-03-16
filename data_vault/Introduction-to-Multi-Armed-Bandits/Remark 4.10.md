---
type: remark
label: Remark 4.10
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 21 Lipschitz bandits
related_entities: []
date_extracted: '2026-03-16T01:32:59.485915+00:00'
---

# Remark 4.10

Covering dimension is often stated without the multiplier: $\mathtt{COV}(X)=\inf_{c>0}\mathtt{COV}_{c}(X)$. This version is meaningful (and sometimes more convenient) for infinite metric spaces. However, for finite metric spaces it is trivially 0, so we need to fix the multiplier for a meaningful definition. Furthermore, our definition allows for more precise regret bounds, both for finite and infinite metric spaces. To de-mystify the infimum in Eq. (59), let us state a corollary: if $d=\mathtt{COV}_{c}(X)$ then $\displaystyle N_{\epsilon}(X)\leq c^{\prime}\cdot\epsilon^{-d}\qquad\forall c^{\prime}>c,\,\epsilon>0.$ (60)

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 21 Lipschitz bandits
