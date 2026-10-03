# Exact architecture replay: C-FIELD-J-LOCAL-INSTRUMENT-N

PUBLIC, NON-CANONICAL. This directory exposes an already frozen program
to the existing stock x86_64/aarch64 reproduction runner. It adds no new
experiment, scope, apparatus or hypothesis and changes no workflow.

- Original source: [notes/C-FIELD-J-LOCAL-INSTRUMENT-N/verify.py](https://github.com/mathorn1973/twist-j/blob/024936502544c2ec45acc8890a052c7b3aca26be/notes/C-FIELD-J-LOCAL-INSTRUMENT-N/verify.py)
- Receiving source pin: `024936502544c2ec45acc8890a052c7b3aca26be`.
- `verify.py` is a byte-identical copy of `verify.py`: SHA-256 `76f92f9b8fe0501f58d25bb16f3d066e3a0e5a39e01e80a1939657c88bd6bbcc`.
- `EXPECTED.txt` is the unchanged original stdout: SHA-256 `5ba56f3fa9036a0d5cc1fe13dba06250362850c3fbe38c6779c78fe106b694b1`.
- Original preparation, proof, exposure boundaries and local run remain
  in [`../../notes/C-FIELD-J-LOCAL-INSTRUMENT-N/`](../../notes/C-FIELD-J-LOCAL-INSTRUMENT-N/). Renaming an independent `break.py`
  for this runner does not turn it into the author implementation.

Run from the repository root with `python reproduce/C-FIELD-J-LOCAL-INSTRUMENT-N/verify.py`.
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
