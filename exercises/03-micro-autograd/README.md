# Exercise 03 — Build a Tiny Autograd Engine

**Timebox:** 60 minutes  
**Theme:** Reverse-mode AD

## Mission
Implement scalar reverse-mode autodiff.

## 0–10 min — Derive
Store graph parents during forward execution, topologically sort, then propagate gradients backward with the chain rule.

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

> Why is reverse-mode AD ideal for a scalar loss with millions of parameters?

Use: Question → Hypothesis → Experiment/derivation → Result → Interpretation → Limitations → Next experiment.

## Definition of done
- [ ] Code runs.
- [ ] Meaningful tests pass.
- [ ] I can explain the central equation without reading.
- [ ] Research note completed.
- [ ] Diff checked for confidential/company material.
- [ ] Commit and push.
