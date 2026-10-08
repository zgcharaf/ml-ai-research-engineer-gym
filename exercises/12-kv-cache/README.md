# Exercise 12 — KV Cache for Autoregressive Decoding

**Timebox:** 60 minutes  
**Theme:** Inference systems

## Mission
Add a KV cache and benchmark decoding.

## 0–10 min — Derive
Reuse prior K/V projections rather than recomputing them at each decoding step.

## 10–40 min — Build
- [ ] Implement the core idea in `starter.py`.
- [ ] Add one edge case.

## 40–50 min — Test
- [ ] Replace the placeholder with meaningful tests.
- [ ] Check shapes, numerical behavior and gradients where relevant.

## 50–60 min — Research note
> What computation still grows with context length after KV caching?

## Definition of done
- [ ] Code runs.
- [ ] Meaningful tests pass.
- [ ] Central idea explainable without notes.
- [ ] Research note completed.
- [ ] Diff checked for confidential/company material.
