# Exercise 14 — Gradient Norms + Clipping

**Timebox:** 60 minutes  
**Theme:** Training diagnostics

## Mission
Implement global grad norm and clipping.

## 0–10 min — Derive
Use ||g||=sqrt(sum_i ||g_i||^2) and scale by min(1,tau/||g||).

## 10–40 min — Build
- [ ] Implement the core idea in `starter.py`.
- [ ] Add one edge case.

## 40–50 min — Test
- [ ] Replace the placeholder with meaningful tests.
- [ ] Check shapes, numerical behavior and gradients where relevant.

## 50–60 min — Research note
> Why can clipping stabilize training without solving the root cause?

## Definition of done
- [ ] Code runs.
- [ ] Meaningful tests pass.
- [ ] Central idea explainable without notes.
- [ ] Research note completed.
- [ ] Diff checked for confidential/company material.
