# Exact architecture replay: C-FIELD-J-LOCAL-INSTRUMENT-REVIEW-N

PUBLIC, NON-CANONICAL. This directory exposes an already frozen program
to the existing stock x86_64/aarch64 reproduction runner. It adds no new
experiment, scope, apparatus or hypothesis and changes no workflow.

- Original source: [notes/C-FIELD-J-LOCAL-INSTRUMENT-REVIEW-N/break.py](https://github.com/mathorn1973/twist-j/blob/024936502544c2ec45acc8890a052c7b3aca26be/notes/C-FIELD-J-LOCAL-INSTRUMENT-REVIEW-N/break.py)
- Receiving source pin: `024936502544c2ec45acc8890a052c7b3aca26be`.
- `verify.py` is a byte-identical copy of `break.py`: SHA-256 `da26e40b9bbfd2534d0bc3e530d88fa505d9143d0d0c9542bb0e4493aeea69fd`.
- `EXPECTED.txt` is the unchanged original stdout: SHA-256 `49bc7306bedebd523a7cfa7f886e4ab854c631cb7e7a31045f7bd4f4339b13b7`.
- Original preparation, proof, exposure boundaries and local run remain
  in [`../../notes/C-FIELD-J-LOCAL-INSTRUMENT-REVIEW-N/`](../../notes/C-FIELD-J-LOCAL-INSTRUMENT-REVIEW-N/). Renaming an independent `break.py`
  for this runner does not turn it into the author implementation.

Run from the repository root with `python reproduce/C-FIELD-J-LOCAL-INSTRUMENT-REVIEW-N/verify.py`.
The script is standalone Python standard library. It must exit zero,
emit no stderr, and match the one committed EXPECTED byte for byte.
The stock runner enforces a 120-second per-program timeout.

Two successful architecture jobs must contain the actual REPRODUCE PASS
line for THIS directory; green notes-only CI is not a scientific replay.
Exact job pins and results are recorded separately after execution.
Each author/reviewer program matches its own expected output; their
different stdout files are not asserted equal to one another.

Finite audits supplement the existing mathematical proofs. No physical
preparation, actual occurrence, native-U realization or canonical status
is earned by this replay. Theorem scope does not transfer between machines.
