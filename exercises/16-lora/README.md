# Exercise 16 — LoRA from Scratch

**Timebox:** 60 minutes  
**Theme:** Parameter-efficient tuning

## Mission
Implement a LoRA-wrapped frozen linear layer.

## 0–10 min — Derive
Use W'=W+BA with rank r much smaller than matrix dimensions.

## 10–40 min — Build
- [ ] Implement the core idea in `starter.py`.
- [ ] Add one edge case.

## 40–50 min — Test
- [ ] Replace the placeholder with meaningful tests.
- [ ] Check shapes, numerical behavior and gradients where relevant.

## 50–60 min — Research note
> Why can low-rank updates capture useful fine-tuning directions?

## Definition of done
- [ ] Code runs.
- [ ] Meaningful tests pass.
- [ ] Central idea explainable without notes.
- [ ] Research note completed.
- [ ] Diff checked for confidential/company material.
