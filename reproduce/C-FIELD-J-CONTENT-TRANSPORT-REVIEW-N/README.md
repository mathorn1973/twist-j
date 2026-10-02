# Exact architecture replay: C-FIELD-J-CONTENT-TRANSPORT-REVIEW-N

PUBLIC, NON-CANONICAL. This directory exposes an already frozen program
to the existing stock x86_64/aarch64 reproduction runner. It adds no new
experiment, scope, apparatus or hypothesis and changes no workflow.

- Original source: [notes/C-FIELD-J-CONTENT-TRANSPORT-REVIEW-N/break.py](https://github.com/mathorn1973/twist-j/blob/05e2f457e9f7d69f6f6649e9ec4094f4ebb08eaa/notes/C-FIELD-J-CONTENT-TRANSPORT-REVIEW-N/break.py)
- Receiving source pin: `05e2f457e9f7d69f6f6649e9ec4094f4ebb08eaa`.
- `verify.py` is a byte-identical copy of `break.py`: SHA-256 `d2aa61efa74bb26b323d9a940ac9269a8c7d1a561419869cf157abd14716467a`.
- `EXPECTED.txt` is the unchanged original stdout: SHA-256 `08bb207503943772e5c6e62b8f35fff1050d52decf654a280d30bc77feaeb000`.
- Original preparation, proof, exposure boundaries and local run remain
  in [`../../notes/C-FIELD-J-CONTENT-TRANSPORT-REVIEW-N/`](../../notes/C-FIELD-J-CONTENT-TRANSPORT-REVIEW-N/). Renaming an independent `break.py`
  for this runner does not turn it into the author implementation.

Run from the repository root with `python reproduce/C-FIELD-J-CONTENT-TRANSPORT-REVIEW-N/verify.py`.
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
