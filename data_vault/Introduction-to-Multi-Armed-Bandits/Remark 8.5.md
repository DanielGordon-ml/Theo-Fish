---
type: remark
label: Remark 8.5
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 44 Contextual bandits with a policy class
related_entities: []
date_extracted: '2026-03-16T01:32:59.530184+00:00'
---

# Remark 8.5

A policy can be based on a *score predictor*: given a context $x$, it assigns a numerical score $\ u(a|x)$ to each action $a$. Such score can represent an estimated expected reward of this action, or some other quality measure. The policy simply picks an action with a highest predicted reward. For a concrete example, if contexts and actions are represented as known feature vectors in $\mathbb{R}^{d}$, a *linear* score predictor is $\ u(a|x)=aMx$, for some fixed $d\times d$ weight matrix $M$.

A policy can also be based on a *decision tree*, a flowchart in which each internal node corresponds to a “test” on some attribute(s) of the context (e.g.,\xa0is the user male of female), branches correspond to the possible outcomes of that test, and each terminal node is associated with a particular action. Execution starts from the “root node” of the flowchart and follows the branches until a terminal node is reached.

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 44 Contextual bandits with a policy class
