# Exercise 17 — Toy Mixture-of-Experts Layer

**Timebox:** 60 minutes  
**Theme:** Sparse routing

## Mission
Implement top-1 routing across several small experts.

## 0–10 min — Derive
Router scores select an expert per token; track expert usage.

## 10–40 min — Build
- [ ] Implement the core idea in `starter.py`.
- [ ] Add one edge case.

## 40–50 min — Test
- [ ] Replace the placeholder with meaningful tests.
- [ ] Check shapes, numerical behavior and gradients where relevant.

## 50–60 min — Research note
> Why are load-balancing losses needed in MoE systems?

## Definition of done
- [ ] Code runs.
- [ ] Meaningful tests pass.
- [ ] Central idea explainable without notes.
- [ ] Research note completed.
- [ ] Diff checked for confidential/company material.
