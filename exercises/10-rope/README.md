# Exercise 10 — Rotary Positional Embeddings (RoPE)

**Timebox:** 60 minutes  
**Theme:** Positional geometry

## Mission
Implement RoPE and apply it to Q/K.

## 0–10 min — Derive
Prove (R_p q)^T(R_r k)=q^T R_(r-p) k.

Write key equations and tensor shapes by hand.

## 10–40 min — Build
- [ ] Implement the core idea in `starter.py`.
- [ ] Add one edge case.
- [ ] Avoid high-level helpers where the exercise asks for a from-scratch implementation.

## 40–50 min — Test
- [ ] Replace the placeholder test with meaningful invariants.
- [ ] Check shapes, numerical behavior and gradients where relevant.

## 50–60 min — Research note
> Why does RoPE naturally encode relative position?

Use: Question → Hypothesis → Experiment/derivation → Result → Interpretation → Limitations → Next experiment.

## Definition of done
- [ ] Code runs.
- [ ] Meaningful tests pass.
- [ ] I can explain the central equation without reading.
- [ ] Research note completed.
- [ ] Diff checked for confidential/company material.
- [ ] Commit and push.
