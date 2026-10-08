# Exercise 11 — Train a Tiny GPT to Overfit

**Timebox:** 60 minutes  
**Theme:** Autoregressive LM

## Mission
Build a tiny GPT and intentionally overfit a tiny corpus.

## 0–10 min — Derive
Trace token ids -> embeddings -> blocks -> logits -> next-token cross-entropy.

## 10–40 min — Build
- [ ] Implement the core idea in `starter.py`.
- [ ] Add one edge case.

## 40–50 min — Test
- [ ] Replace the placeholder with meaningful tests.
- [ ] Check shapes, numerical behavior and gradients where relevant.

## 50–60 min — Research note
> Why is deliberate tiny-batch overfitting such a powerful debugging test?

## Definition of done
- [ ] Code runs.
- [ ] Meaningful tests pass.
- [ ] Central idea explainable without notes.
- [ ] Research note completed.
- [ ] Diff checked for confidential/company material.
