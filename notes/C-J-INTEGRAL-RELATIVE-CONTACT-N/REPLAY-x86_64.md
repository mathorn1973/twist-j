# Same-source x86_64 reproduction

NON-CANONICAL / L1. Not independent review or public status promotion.

- Scientific input pin: `898160aab70bc8908174df56ddca7afec39fa42f`.
- Run checkout: `21d3ec39be369067dc10efb605a5853d69a1302e`.
- Checkout fetched directly through Git; all five scientific source files matched the input pin before execution. Worktree was clean.
- Compared against actual first stdout already committed in EXPECTED.txt.
- Start UTC: `2026-10-29T21:14:05.119571+00:00`.
- Platform: `Linux 6.18.33.2-microsoft-standard-WSL2`.
- Architecture: `x86_64`. Python: `3.12.3`.
- Command: `python -I -B notes/C-J-INTEGRAL-RELATIVE-CONTACT-N/verify.py`.
- Environment: `PYTHONHASHSEED=0`, `PYTHONDONTWRITEBYTECODE=1`.
- Timeout: 45 seconds. Exit: 0. Stderr: 0 bytes.
- Verifier SHA256: `0089529bd6f4a9488cbc74197a55912453fc48a1967859bce87c3986cea4951e`.
- Actual stdout: 776 bytes, SHA256 `89e49565965d9d417cebefd6eb7b36bea864788e8356bbad8901043f1ad66890`.
- Byte-identical to the committed first output: YES. All nine frozen groups passed.

Both architecture executions are author-controlled reproduction of one program. This is not a second implementation, independent acceptance, a formal public P-probe or a physical experiment. Required repository CI is separate and does not execute the notes audit. No frozen file was changed.

Custody: the execution-side attempt to publish its neutral receipt lacked Git write credentials and updated no public ref. This observed execution receipt is therefore recorded here on the public coordination surface before the authorized writer adds it to the same candidate branch. No scientific rerun or source change is needed.

Public receipt: https://github.com/mathorn1973/twist-j/issues/1832#issuecomment-6508498866
