# Exercise 01 — Stable Softmax + Cross-Entropy

**Timebox:** 60 minutes  
**Theme:** Numerical stability, log-sum-exp

## Mission
Implement stable softmax and cross-entropy from scratch.

## 0–10 min — Derive
Prove softmax(z)=softmax(z-c), then choose c=max(z).

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

> Why is log-sum-exp more stable than softmax followed by log?

Use: Question → Hypothesis → Experiment/derivation → Result → Interpretation → Limitations → Next experiment.

## Definition of done
- [ ] Code runs.
- [ ] Meaningful tests pass.
- [ ] I can explain the central equation without reading.
- [ ] Research note completed.
- [ ] Diff checked for confidential/company material.
- [ ] Commit and push.
