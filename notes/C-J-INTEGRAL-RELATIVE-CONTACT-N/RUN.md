# Supplementary scientific run

NON-CANONICAL / L1 / candidate-C finite audit; analytical claims remain
conditional candidate-T pending independent review. No public P-probe.

## First execution

- Input pin: `898160aab70bc8908174df56ddca7afec39fa42f`.
- All five frozen files fetched from public immutable raw URLs and matched
  byte for byte before execution, in a clean checkout of that exact pin.
- Started UTC: `2026-10-29T21:05:46.155517+00:00`.
- Platform: `Darwin 27.0.0`.
- Architecture: `arm64`.
- Python: `3.13.13`.
- Command: `python -I -B notes/C-J-INTEGRAL-RELATIVE-CONTACT-N/verify.py`.
- Environment: `PYTHONHASHSEED=0`, `PYTHONDONTWRITEBYTECODE=1`.
- Timeout: 45 seconds.
- Exit code: 0. Stderr: 0 bytes.
- Verifier: 8702 bytes; SHA256
  `0089529bd6f4a9488cbc74197a55912453fc48a1967859bce87c3986cea4951e`.
- Actual stdout: 776 bytes; SHA256
  `89e49565965d9d417cebefd6eb7b36bea864788e8356bbad8901043f1ad66890`.
- Actual stdout is retained unchanged in EXPECTED.txt.

All nine groups passed on their frozen finite inventory. No code, proof or
threshold changed after the pin. Universal claims are not inferred from a
finite audit. This is author validation, not independent acceptance.
Ordinary notes CI is a separate repository check and does not run this script.
