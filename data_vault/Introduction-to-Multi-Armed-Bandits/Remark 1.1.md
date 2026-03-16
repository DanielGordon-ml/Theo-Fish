---
type: remark
label: Remark 1.1
paper: Introduction to Multi-Armed Bandits
arxiv_id: '1904.07272'
section: 1 Model and examples
related_entities: []
date_extracted: '2026-03-16T01:32:59.439955+00:00'
---

# Remark 1.1

We use the following conventions in this chapter and throughout much of the book. We will use *arms* and *actions* interchangeably. Arms are denoted with $a$, rounds with $t$. There are $K$ arms and $T$ rounds. The set of all arms is $\mathcal{A}$. The mean reward of arm $a$ is $\mu(a):=\operatornamewithlimits{\mathbb{E}}[\mathcal{D}_{a}]$. The best mean reward is denoted $\mu^{*}:=\max_{a\in\mathcal{A}}\mu(a)$. The difference $\Delta(a):=\mu^{*}-\mu(a)$ describes how bad arm $a$ is compared to $\mu^{*}$; we call it the *gap* of arm $a$. An optimal arm is an arm $a$ with $\mu(a)=\mu^{*}$; note that it is not necessarily unique. We take $a^{*}$ to denote some optimal arm. $[n]$ denotes the set $\{1,2\,,\ \ldots\ ,n\}$.

## References

- Paper: [[index|Introduction to Multi-Armed Bandits]]
- Section: 1 Model and examples
