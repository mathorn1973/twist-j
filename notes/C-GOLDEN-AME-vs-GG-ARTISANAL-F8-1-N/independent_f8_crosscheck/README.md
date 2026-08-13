# Independent artisan-F8 cross-check

This directory is a portable, Python-standard-library-only audit of the
public preregistration `C-GOLDEN-AME-vs-GG-ARTISANAL-F8-1-N`.

Public lock:

- commit `62c1e877c3817923dca6b922ebd4562f83d2bbea`;
- `PREREG.md` SHA-256
  `0ffaca441435003aeb0779160e9fcdbca6c40a25c4ea2acce836ff3eca6e0137`.

The implementation was written independently of the primary evaluator.
It imports no repository module and contains no copied tensor table.  The
golden tensor is parsed from the pinned MATLAB source after byte, SHA-256,
and Git-blob checks.  `sym` and `sparse` are constructed directly from the
frozen formula (T).

See `RUN.md` for reproduction, `AUDIT.md` for the contraction and arithmetic
audit, `RESULT.md` for the result, and `result.json` for the canonical
machine-readable certificate.

