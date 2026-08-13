# Portable post-lock artisan F8 computation

This is the standard-library-only primary package for the frozen public test
`C-GOLDEN-AME-vs-GG-ARTISANAL-F8-1-N` (issue #368).

Frozen public lock:

- commit `62c1e877c3817923dca6b922ebd4562f83d2bbea`;
- tree `9a8bf350f0f255bd74c0e7dabca665d0a46477c3`;
- `PREREG.md` SHA-256
  `0ffaca441435003aeb0779160e9fcdbca6c40a25c4ea2acce836ff3eca6e0137`.

The scientific verdict is `EXACT_NO_GG_ARTISANAL_9PLUS27`: the pinned golden
AME(4,6) tensor is outside both frozen Gross--Goedicke artisanal 9+27 LU plus
party-permutation orbits.  The exact witness is the first frozen coordinate,
`v0`; see `RESULT.md` and `EXACT_RESULT.json`.

Contents:

- `artisan_f8_lib.py`, `run_primary.py`: authoritative evaluator;
- `SOURCE_PINS.json`: recovery URLs and byte pins for the non-vendored
  golden and Gross--Goedicke sources;
- `prereg/`: exact public preregistration/lock copies;
- `GATE_REPORT.json`, `MODULAR_RESULT.json`, `GOLDEN_SIGNATURES.json`,
  `EXACT_RESULT.json`: deterministic certificates;
- `OUTPUT.txt`, `RESULT.md`: concise machine/human reports;
- `independent_gate_audit/`: independently written G0/G1 audit;
- `independent_f8_crosscheck/`: independently written contraction and exact
  reconstruction audit, using a third factor order;
- `TWO_RUN_DETERMINISM.json`: two-run byte-determinism certificate;
- `MANIFEST.sha256`, `verify_manifest.py`: package integrity check.

This is a notes-only result branch.  No Canon or Registry file is modified,
and no `PROMO.md` is created.
