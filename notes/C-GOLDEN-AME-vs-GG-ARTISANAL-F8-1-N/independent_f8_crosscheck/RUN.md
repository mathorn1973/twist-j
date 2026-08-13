# Reproduction

Requirements: Python 3.11 or newer; standard library only.

```sh
python3 crosscheck_f8.py \
  --source /path/to/pinned/AME46_ORIGINAL.m \
  --output result.json
```

The source must be exactly 8,515 bytes with SHA-256
`55fbc0ba2747b4e5adc5a5abd15ac7241a461ff8182268ebdae464d8a29cc9ae`
and Git-blob SHA-1 `e0d0e171d58b3360c39595d677ffc401a466112d`.
No source location is hard-coded.  `--output` may be any writable path.

For a modular-only diagnostic run, add `--skip-exact`.  Such a run reports
only locator mismatches and intentionally makes no exact union verdict.
`--progress` writes progress messages to stderr; it does not alter canonical
JSON or stdout.

Reference environment for the recorded run:

- Python `3.12.13`;
- one process, one core;
- modular census: 18.1 wall seconds;
- modular census plus three exact D0 replays: 67.6 and 71.0 wall seconds
  in the two complete runs.

Determinism was tested in two fresh complete processes.  `result.json` and
`result.rerun.json` were byte-identical; `run1.stdout` and `run2.stdout` were
byte-identical.  See `SHA256SUMS.txt`.
