# ML/AI Research Engineer Gym

20 one-hour sessions designed to build **research-engineer depth**.

**derive → implement → test → explain → commit**

## Rules
1. Timebox each exercise to 60 minutes.
2. Derive before coding.
3. Do not copy a reference implementation before your first attempt.
4. End with tests and a research note.
5. One coherent commit per exercise.
6. Never push employer code, data, schemas, credentials, screenshots, internal docs, or business logic.

## Curriculum
01. Stable Softmax + Cross-Entropy
02. Gradient Checking an MLP
03. Build a Tiny Autograd Engine
04. Initialization + Signal Propagation
05. SGD, Momentum, Adam and AdamW
06. LayerNorm vs RMSNorm
07. Scaled Dot-Product Attention
08. Multi-Head Self-Attention
09. Transformer Block: Pre-Norm + Residuals
10. Rotary Positional Embeddings (RoPE)
11. Train a Tiny GPT to Overfit
12. KV Cache for Autoregressive Decoding
13. Warmup + Cosine Decay
14. Gradient Norms + Clipping
15. Mixed Precision + Loss Scaling
16. LoRA from Scratch
17. Toy Mixture-of-Experts Layer
18. Contrastive Learning + InfoNCE
19. Calibration + Expected Calibration Error
20. Mini Research Study: Pre-Norm vs Post-Norm

## Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install torch numpy matplotlib pytest
pytest -q
```
