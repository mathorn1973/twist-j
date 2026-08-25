# Run record

```text
STATUS:       NON-CANONICAL
AUTHORITY:    NONE
DATE:         2026-08-25
FROZEN PIN:   49ce4081e021171bc4c8c79a3fc7ffe4a496ea1a
```

## Primary verifier

```text
command: python3 verify.py
exit:    0
tail:
  A2 exact split: total=165 Q-outside=127 residual=38
  A2 residual Routh counts: {0: 0, 1: 8, 2: 1, 3: 29, 4: 0}
  A2 sole two-outside survivor: (4, -2)
  A3 exact split: total=11; only no-Q-outside pair=(4,-2)
  ALL EXACT ASSERTIONS PASS
```

## Independent compound-Schur cross-check

```text
command: python3 crosscheck_schur.py
exit:    0
tail:
  A0=FALSE (F-LOWER and F-TIE)
  A1=FALSE (F-LOWER and F-TIE)
  A2=TRUE (unique equality f_J)
  A3=TRUE (unique equality f_J)
```

## Blind breaker

The frozen v3 breaker was run once by its isolated lane before comparison
with the builder or theorem lanes.

```text
sha256: 2fc9c5ef4dea72cf0d95bbb409d5b0edfc57c0a3a2b5245b95497e70aeef1e04
bytes:  17346
exit:   0
post-run sha256 unchanged: yes
decisions:
  A0 NEGATIVE_F_TIE
  A1 NEGATIVE_F_LOWER
  A2 POSITIVE_COMPLETE_WINDOW
  A3 POSITIVE_COMPLETE_WINDOW
```

The detailed pre-run version history and fail-fast corrections are preserved
in `BREAKER_AUDIT.md`.

## Architecture matrix

| Host | `verify.py` | `crosscheck_schur.py` | frozen blind `breaker.py` |
|---|---|---|---|
| Linux x86_64 | exit 0 | exit 0 | exit 0 |
| Darwin arm64 | exit 0 | exit 0 | not replayed |

On Darwin arm64, `shasum -a 256 -c SHA256SUMS` passed before both exact quick
checks.  The blind breaker was intentionally not needed for the second-host
quick check; a later formal public probe must still produce its own pinned
two-architecture evidence.
