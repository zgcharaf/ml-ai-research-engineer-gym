# Exercise 02 — Gradient Checking an MLP

**Timebox:** 60 minutes  
**Theme:** Finite differences, verification

## Mission
Verify autograd gradients against centered finite differences.

## 0–10 min — Derive
Use [L(theta+eps)-L(theta-eps)]/(2eps) and compare with backprop.

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

> Why can ReLU make finite-difference checks ambiguous at zero?

Use: Question → Hypothesis → Experiment/derivation → Result → Interpretation → Limitations → Next experiment.

## Definition of done
- [ ] Code runs.
- [ ] Meaningful tests pass.
- [ ] I can explain the central equation without reading.
- [ ] Research note completed.
- [ ] Diff checked for confidential/company material.
- [ ] Commit and push.
