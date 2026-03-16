---
type: remark
label: Remark 2.2
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: Chapter 2 Lower Bounds
related_entities: []
date_extracted: '2026-03-16T01:32:59.454218+00:00'
---

# Remark 2.2

Note that (ii) implies (i), is because if regret is high in expectation over problem instances, then there exists at least one problem instance with high regret. Conversely, (i) implies (ii) if $|\mathcal{F}|$ is a constant: indeed, if we have high regret $H$ for some problem instance in $\mathcal{F}$, then in expectation over a uniform distribution over $\mathcal{F}$ regret is least $H/|\mathcal{F}|$. However, this argument breaks if $|\mathcal{F}|$ is large. Yet, a stronger version of (i) which says that regret is high for a *constant fraction* of the instances in $\mathcal{F}$ implies (ii), with uniform distribution over the instances, regardless of how large $|\mathcal{F}|$ is.

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: Chapter 2 Lower Bounds
