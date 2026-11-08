# Execution record

> **NON-CANONICAL.** Audit record only; no formal-probe or evidence authority.

## Chronology and exposure

1. The 251-minor census at `p = 5` was first computed in a scratch session
   before this packet existed. The result was known when `verify.py` and
   `break.py` were written.
2. Issue `#1682` recorded owner, branch, path, scope and the result-exposed
   status before any file of this directory was committed.
3. `verify.py` and `break.py` were then run with the commands below. No
   preregistration and no pre-execution pin is claimed.

## Executable hashes

```text
e47e17ea929ac58763debe546bbff9b8a2def271e843093a24b337d702e14144  verify.py
e86207141565ba81893cbf0f5145d240f0697483684dd4cbec0272883d71adca  break.py
```

## Environment

```text
platform:      Ubuntu 24.04
architecture:  x86_64
python:        3.13.16
dependencies:  standard library only
```

## Commands

```bash
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 notes/C-PRIME-FOURIER-SUPPORT-UNCERTAINTY-N/verify.py
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 notes/C-PRIME-FOURIER-SUPPORT-UNCERTAINTY-N/break.py
```

Both exit with status `0`. Exact stdouts are `EXPECTED.txt` (611 bytes) and
`BREAKER_EXPECTED.txt` (354 bytes). A second run of each was byte-identical.
Each run takes well under the 120 second limit.

## Not done

No second architecture. Ordinary CI on a notes-only pull request does not
execute these scripts and is not a two-architecture validation.
