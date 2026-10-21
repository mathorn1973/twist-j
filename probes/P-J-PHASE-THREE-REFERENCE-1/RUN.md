# First exact pinned run

PUBLIC / NON-CANONICAL / L1. A. M. Thorn. Apache-2.0.

```text
pin_commit: 6731b13455e221e097b33b6cf54d2356d00bef95
verifier_sha256: cbd542c2504913fee15257c0d67477cf7469ad070f99c0ef3b42b699fc889757
command: python3 probes/P-J-PHASE-THREE-REFERENCE-1/verify.py
platform: Debian GNU/Linux 12 (bookworm)
architecture: aarch64
python: 3.11.2
exit_code: 0
stdout_sha256: c94ccd06a464a9725856d10ab7d24dc7ecc17ea0a9cccde4b68ce3eb16d2d36e
stdout_bytes: 5927
stdout_lines: 7
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

Public pre-execution pin/readback receipt:
https://github.com/mathorn1973/twist-j/issues/1580#issuecomment-6237320746

Receipt UTC: 2026-10-17T17:11:23Z
Start UTC: 2026-10-17T17:12:02.872829+00:00
End UTC: 2026-10-17T17:12:57.277077+00:00
Elapsed: 54.404 seconds (measured execution metadata).
The unchanged per-verifier limit is 600 seconds.

This was the first scientific import/execution of the new verifier.
Before it, all five pinned files were publicly read back byte for byte,
then their receipt was itself read back. The process ran from the clean
public pin with LC_ALL=C, LANG=C, TZ=UTC, PYTHONHASHSEED=0 and
PYTHONDONTWRITEBYTECODE=1. After completion, PREREG.md, verify.py, PROOF.md,
README.md and SOURCES.tsv were still byte-identical to the public pin;
HEAD was unchanged and the worktree clean. The verifier itself checked
all three immutable runtime dependencies before import and after the audit.

EXPECTED.txt is the exact captured stdout, copied as bytes without
normalization or reconstruction. All scientific values are integers,
finite-field values or exact rational pairs. There are seven stdout lines,
ending in the explicit scientific PASS. No FALSIFIER fired. Exit 0 and
empty stderr are execution facts, separate from the scientific outcome.

The frozen inventory passed: 625 references and 3125 root evaluations;
18750 occupied contact cases, including 3750 ready cases; 50 complete
two-source prefixes, 300 main resource-restoration boundaries and their
full inverses; 25 actual funded relays with 50 accepted inputs and 25
distinct retained record sets; 200 complete wave/tape/pointer/energy
boundaries matched by the second implementation; 25 deleted-W prefixes
and one actual downstream control replay; one outside-family zero-piston
alias control. The 182-operation prefix, three shared references, one
shared work bit and single B=5 account were not altered after pin.

The observed maximum work was exactly 11978371/5248800, below the
predeclared analytical bound 23/5 and the common capacity 5. The observed
value did not set or alter the budget. Both old classical deposits
remained inside the unchanged guard for every ordered pair.

SparseWave is a separately written implementation of the wave/tape
equations in this same session. It is not an independent author and is
not a replacement for the original typed reader. The old reader's
general rational vector identity is proved separately in PROOF.md;
the fixed phase lookup follows its output. The work does not price the
prefix or establish native/physical admission.

The initial aarch64 run alone is one-architecture evidence. The required
public x86_64 and aarch64 jobs must replay the same PR head against this
same committed EXPECTED.txt. Their observed exact-head results, verifier
and stdout hashes, and immutable job links belong to the subsequent
public completion receipt. Same-session static review and dual
implementation remain separate from cross-architecture reproduction
and from independent scientific review.
