# P-PHOTON-Z5-DUAL-WORM-CROSSCHECK-1

Independent dual closed-surface kernel for issue #756.

This directory is a zero-evidence engineering package. The source freeze proves
algorithmic correctness/ergodicity at its declared scope and prepares, but does
not execute, the `L=6,8` Ward cross-check.

Formal audit command:

```bash
env -i PATH=/usr/local/bin:/usr/bin:/bin LC_ALL=C LANG=C TZ=UTC \
  PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 \
  python3 probes/P-PHOTON-Z5-DUAL-WORM-CROSSCHECK-1/verify.py
```

The stdout must equal `EXPECTED.txt` byte for byte and stderr must be empty.
