# Exercise 04 — Initialization + Signal Propagation

**Timebox:** 60 minutes  
**Theme:** Xavier/Kaiming, variance propagation

## Mission
Measure activation/gradient variance through a deep MLP.

## 0–10 min — Derive
Derive Var(z_j) ≈ n Var(w) Var(x) under independence assumptions.

Write the key equations and tensor shapes by hand.

## 10–40 min — Build
- [ ] Implement the core idea in `starter.py`.
- [ ] Add one edge case.
- [ ] Keep the implementation independent of high-level helper functions where the exercise asks for it.

## 40–50 min — Test
- [ ] Replace the placeholder test with meaningful invariants.
- [ ] Check shapes and numerical behavior.
- [ ] Check gradients where relevant.

## 50–60 min — Research note
Answer in `NOTES.md`:

> Why does the correct initialization depend on the activation function?

Use: Question → Hypothesis → Experiment/derivation → Result → Interpretation → Limitations → Next experiment.

## Definition of done
- [ ] Code runs.
- [ ] Meaningful tests pass.
- [ ] I can explain the central equation without reading.
- [ ] Research note completed.
- [ ] Diff checked for confidential/company material.
- [ ] Commit and push.
