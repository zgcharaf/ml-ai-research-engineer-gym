# Exercise 06 — LayerNorm vs RMSNorm

**Timebox:** 60 minutes  
**Theme:** Normalization

## Mission
Implement LayerNorm and RMSNorm manually and compare their behavior.

## 0–10 min — Derive
LayerNorm centers and rescales; RMSNorm rescales by RMS without mean subtraction.

Write key equations and tensor shapes by hand.

## 10–40 min — Build
- [ ] Implement the core idea in `starter.py`.
- [ ] Add one edge case.
- [ ] Avoid high-level helpers where the exercise asks for a from-scratch implementation.

## 40–50 min — Test
- [ ] Replace the placeholder test with meaningful invariants.
- [ ] Check shapes, numerical behavior and gradients where relevant.

## 50–60 min — Research note
> Which invariances does LayerNorm have that RMSNorm does not?

Use: Question → Hypothesis → Experiment/derivation → Result → Interpretation → Limitations → Next experiment.

## Definition of done
- [ ] Code runs.
- [ ] Meaningful tests pass.
- [ ] I can explain the central equation without reading.
- [ ] Research note completed.
- [ ] Diff checked for confidential/company material.
- [ ] Commit and push.
