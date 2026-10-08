# Exercise 08 — Multi-Head Self-Attention

**Timebox:** 60 minutes  
**Theme:** Transformer internals

## Mission
Build multi-head self-attention from projections and your attention function.

## 0–10 min — Derive
Trace (B,T,D) -> (B,H,T,Dh) and back.

Write key equations and tensor shapes by hand.

## 10–40 min — Build
- [ ] Implement the core idea in `starter.py`.
- [ ] Add one edge case.
- [ ] Avoid high-level helpers where the exercise asks for a from-scratch implementation.

## 40–50 min — Test
- [ ] Replace the placeholder test with meaningful invariants.
- [ ] Check shapes, numerical behavior and gradients where relevant.

## 50–60 min — Research note
> What expressive advantage can multiple heads provide?

Use: Question → Hypothesis → Experiment/derivation → Result → Interpretation → Limitations → Next experiment.

## Definition of done
- [ ] Code runs.
- [ ] Meaningful tests pass.
- [ ] I can explain the central equation without reading.
- [ ] Research note completed.
- [ ] Diff checked for confidential/company material.
- [ ] Commit and push.
