# Exercise 09 — Transformer Block: Pre-Norm + Residuals

**Timebox:** 60 minutes  
**Theme:** Residual architecture

## Mission
Implement a pre-norm Transformer block.

## 0–10 min — Derive
Use y=x+MHA(LN(x)); z=y+MLP(LN(y)).

Write key equations and tensor shapes by hand.

## 10–40 min — Build
- [ ] Implement the core idea in `starter.py`.
- [ ] Add one edge case.
- [ ] Avoid high-level helpers where the exercise asks for a from-scratch implementation.

## 40–50 min — Test
- [ ] Replace the placeholder test with meaningful invariants.
- [ ] Check shapes, numerical behavior and gradients where relevant.

## 50–60 min — Research note
> Why does pre-norm generally improve deep optimization stability?

Use: Question → Hypothesis → Experiment/derivation → Result → Interpretation → Limitations → Next experiment.

## Definition of done
- [ ] Code runs.
- [ ] Meaningful tests pass.
- [ ] I can explain the central equation without reading.
- [ ] Research note completed.
- [ ] Diff checked for confidential/company material.
- [ ] Commit and push.
