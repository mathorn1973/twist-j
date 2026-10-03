# Exact architecture replay: C-FIELD-J-CONTENT-TRANSPORT-N

PUBLIC, NON-CANONICAL. This directory exposes an already frozen program
to the existing stock x86_64/aarch64 reproduction runner. It adds no new
experiment, scope, apparatus or hypothesis and changes no workflow.

- Original source: [notes/C-FIELD-J-CONTENT-TRANSPORT-N/verify.py](https://github.com/mathorn1973/twist-j/blob/05e2f457e9f7d69f6f6649e9ec4094f4ebb08eaa/notes/C-FIELD-J-CONTENT-TRANSPORT-N/verify.py)
- Receiving source pin: `05e2f457e9f7d69f6f6649e9ec4094f4ebb08eaa`.
- `verify.py` is a byte-identical copy of `verify.py`: SHA-256 `cc67d1fa3e2203cfc47498e10488ce02fdde5761b817509c2523fad5896ac883`.
- `EXPECTED.txt` is the unchanged original stdout: SHA-256 `386d9b9a1c801cc38b22aa04305ddf10dbe66a1cf38243e4f28e8686e0ed875f`.
- Original preparation, proof, exposure boundaries and local run remain
  in [`../../notes/C-FIELD-J-CONTENT-TRANSPORT-N/`](../../notes/C-FIELD-J-CONTENT-TRANSPORT-N/). Renaming an independent `break.py`
  for this runner does not turn it into the author implementation.

Run from the repository root with `python reproduce/C-FIELD-J-CONTENT-TRANSPORT-N/verify.py`.
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
