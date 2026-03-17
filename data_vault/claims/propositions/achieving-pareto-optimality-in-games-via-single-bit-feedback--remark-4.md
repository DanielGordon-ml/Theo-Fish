---
slug: achieving-pareto-optimality-in-games-via-single-bit-feedback--remark-4
label: Remark 4
claim_type: proposition
statement: 'Consider that agents can observe the full joint action and use the message
  rule


  $m_{i}^{t}=\begin{cases}\mathbb{I}_{\{a_{i}^{t}\in\mathrm{BR}_{i}(a_{-i}^{t})\}}&\textrm{with
  probability }\epsilon^{\,1-w_{i}\cdot u_{i}^{t}},\\ 0&\textrm{otherwise},\end{cases}$


  where $\mathrm{BR}_{i}(a_{-i}^{t})\coloneqq\operatorname*{arg\,max}_{a_{i}\in A^{i}}\{u^{i}(a_{i},a_{-i}^{t})\}$
  is the best response set. Then, if a pure equilibrium exists, Algorithm 1 can learn
  Pareto-Optimal Equilibrium, even for relatively large $\epsilon$.'
proof: ''
strength: existential
status: unverified
human_notes: ''
about:
- '[[concepts/best-response-function]]'
- '[[concepts/exploration-parameter-epsilon]]'
- '[[concepts/pareto-optimal-equilibrium]]'
- '[[concepts/one-bit-signal]]'
- '[[concepts/pure-nash-equilibrium]]'
- '[[concepts/message-generation-rule]]'
- '[[concepts/sbc-pe-algorithm]]'
about_meta:
- target: '[[concepts/best-response-function]]'
  role: primary
  aspect: ''
- target: '[[concepts/exploration-parameter-epsilon]]'
  role: primary
  aspect: ''
- target: '[[concepts/pareto-optimal-equilibrium]]'
  role: primary
  aspect: ''
- target: '[[concepts/one-bit-signal]]'
  role: primary
  aspect: ''
- target: '[[concepts/pure-nash-equilibrium]]'
  role: primary
  aspect: ''
- target: '[[concepts/message-generation-rule]]'
  role: primary
  aspect: ''
- target: '[[concepts/sbc-pe-algorithm]]'
  role: primary
  aspect: ''
depends_on: []
depends_on_meta: []
sourced_from:
- '[[sources/2509.25921|Achieving Pareto Optimality in Games via Single-bit Feedback]]'
sourced_from_meta:
- target: '[[sources/2509.25921|Achieving Pareto Optimality in Games via Single-bit
    Feedback]]'
  section: ''
  page: ''
  confidence: 0.0
---

# Remark 4

Consider that agents can observe the full joint action and use the message rule

$m_{i}^{t}=\begin{cases}\mathbb{I}_{\{a_{i}^{t}\in\mathrm{BR}_{i}(a_{-i}^{t})\}}&\textrm{with probability }\epsilon^{\,1-w_{i}\cdot u_{i}^{t}},\\ 0&\textrm{otherwise},\end{cases}$

where $\mathrm{BR}_{i}(a_{-i}^{t})\coloneqq\operatorname*{arg\,max}_{a_{i}\in A^{i}}\{u^{i}(a_{i},a_{-i}^{t})\}$ is the best response set. Then, if a pure equilibrium exists, Algorithm 1 can learn Pareto-Optimal Equilibrium, even for relatively large $\epsilon$.
